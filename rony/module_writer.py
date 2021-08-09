import click
import os
from packaging import version
from datetime import datetime
import json
from jinja2 import Template
import rony

import importlib
import pkgutil
import subprocess
from unidiff import PatchSet

plugins_dirs = [
    importlib.import_module(name).__path__[0]
    for finder, name, ispkg in pkgutil.iter_modules()
    if name.startswith("rony_")
]

EXCLUDE_DIRS = ["__pycache__"]


def get_modules():
    def get_module_info(module_name, parent_dir):
        config_file = os.path.join(parent_dir, f"{module_name}.json")
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                data = json.load(f)
            return data
        else:
            return {}

    def comp_modules_version(info1, info2):
        v1 = version.parse(info1.get("version", "0.0.0"))
        v2 = version.parse(info2.get("version", "0.0.0"))
        return v1 < v2

    parent_dirs = [rony.__path__[0]] + plugins_dirs
    modules_dirs = [os.path.join(parent, "module_templates") for parent in parent_dirs]
    if os.path.exists(os.path.join(os.path.expanduser("~"), "MyRonyModules")):
        modules_dirs += [os.path.join(os.path.expanduser("~"), "MyRonyModules")]

    module_paths = {}
    module_info = {}
    module_desc = {}

    for modules_dir in reversed(modules_dirs):
        for module_name in next(os.walk(modules_dir))[1]:

            tmp_info = get_module_info(module_name, modules_dir)
            if (module_name in module_paths.keys()) and comp_modules_version(
                tmp_info, module_info[module_name]
            ):
                continue
            else:
                module_paths[module_name] = os.path.join(modules_dir, module_name)
                module_info[module_name] = tmp_info
                module_desc[module_name] = tmp_info.get("info", "")

    return module_paths, module_desc


def modules_autocomplete(ctx, args, incomplete):
    """Get list of modules available for installation

    Args:
        ctx:
        args:
        incomplete:
    """

    _, module_desc = get_modules()
    return [
        (key, module_desc[key])
        for key in module_desc.keys()
        if (incomplete in key) and key[:2] != "__"
    ]


def write_module(
    LOCAL_PATH,
    module_name,
    autoconfirm=False,
    custom_inputs={},
):
    """Copy files to project

    Args:
        LOCAL_PATH (str): Local Path
        project_name (str): Project Name
    """

    def get_inputs(input_info, autoconfirm=False):
        input_data = {}
        for info in input_info:
            if autoconfirm:
                input_data[info[0]] = info[1]
            else:
                input_data[info[0]] = click.prompt(info[2], default=info[1])
        return input_data

    module_paths, _ = get_modules()
    module_path = module_paths[module_name]
    config_file = os.path.join(os.path.dirname(module_path), f"{module_name}.json")

    # Load config file
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            data = json.load(f)
    else:
        data = {"input_info": []}

    # Request input data
    data["inputs"] = get_inputs(data["input_info"], autoconfirm)
    data["inputs"].update(custom_inputs)

    # Process files
    files_to_create = {}
    files_to_append = {}
    dirs_to_create = []

    for dir_path, dirs, files in os.walk(module_path):

        dir_name = os.path.basename(dir_path)
        rel_path = os.path.relpath(dir_path, module_path)
        local_dir_path = os.path.join(LOCAL_PATH, rel_path)

        if dir_name in EXCLUDE_DIRS:
            continue

        for d in dirs:
            if d in EXCLUDE_DIRS:
                continue
            local_d_path = os.path.join(local_dir_path, d)
            if not os.path.exists(local_d_path):
                dirs_to_create.append(local_d_path)

        for f in files:

            if f == ".ronyignore":
                continue

            outputText = open(os.path.join(dir_path, f), "r", encoding="latin-1").read()

            if ".tpl." in f:
                template = Template(outputText)
                outputText = template.render(**data)

            local_f_path = os.path.join(local_dir_path, f.replace(".tpl.", "."))
            if os.path.exists(local_f_path):
                files_to_append[local_f_path] = outputText
            else:
                files_to_create[local_f_path] = outputText

    # Show changes to user and ask for permission

    if not autoconfirm:
        click.secho("DIRECTORIES TO BE CREATED:", fg="green", bold=True)
        for key in dirs_to_create:
            click.secho(key, fg="green")

        click.secho("FILES TO BE CREATED:", fg="green", bold=True)
        for key, text in files_to_create.items():
            click.secho(key, fg="green")
            click.secho("\t+  ".join(("\n" + text).splitlines(True)) + "\n")

        click.secho("FILES TO BE APPENDED:", fg="yellow", bold=True)
        for key, text in files_to_append.items():
            click.secho(key, fg="yellow")
            click.secho("\t+  ".join(("\n" + text).splitlines(True)) + "\n")

    if (not autoconfirm) and (
        not click.confirm("Do you want to continue?", default=True, abort=True)
    ):
        return

    # Print instructions
    if not autoconfirm:
        click.secho("INSTRUCTIONS", fg="green", bold=True)
        click.secho("\n".join(data.get("instructions", [])))
        click.secho("DEVELOPED BY:", fg="green", bold=True)
        click.secho(", ".join(data.get("developers", [])))

    # Create and append files and dirs

    for directory in dirs_to_create:
        if not os.path.exists(directory):
            os.makedirs(directory)

    for key, text in files_to_create.items():
        directory = os.path.dirname(key)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(key, "wb") as f:
            f.write(text.encode("latin-1"))

    for key, text in files_to_append.items():
        with open(key, "ab") as f:
            f.write(("\n\n" + text).encode("latin-1"))


def create_module_from_diff(module_name):

    if (
        subprocess.call(
            ["git", "branch"], stderr=subprocess.STDOUT, stdout=open(os.devnull, "w")
        )
        != 0
    ):
        click.Abort("Current directory is not a git repository")

    patch_file = f".rony_{module_name}.patch"
    module_path = os.path.join(os.path.expanduser("~"), "MyRonyModules", module_name)

    p = subprocess.call(["git", "diff", "--no-prefix"], stdout=open(patch_file, "w"))

    patch_set = PatchSet.from_filename(patch_file)

    for patched_file in patch_set:

        file_path = patched_file.path
        added_lines = []
        for hunk in patched_file:
            for line in hunk:
                if line.is_added:
                    added_lines.append(line.value)

        module_file_path = os.path.join(module_path, file_path)
        module_dir_path = os.path.dirname(module_file_path)

        if not os.path.exists(module_dir_path):
            os.makedirs(module_dir_path)

        with open(module_file_path, "w") as f:
            f.write("".join(added_lines))

    os.remove(patch_file)

    info = click.prompt("Please your modules description", default="")
    inst = click.prompt(
        "Please instructions to be displayed to the users after they add this module",
        default="",
    )
    developer = click.prompt("Please enter your email", default="")

    with open(module_path + ".json", "w") as f:
        f.write(
            json.dumps(
                {
                    "info": info,
                    "instructions": [inst],
                    "developers": [developer],
                    "input_info": [],
                    "version": "0.0.0",
                },
                sort_keys=True,
                indent=4,
                separators=(",", ": "),
            )
        )
