import click
import os
import re
import sys
from .writer import copy_files, write_readme_file, write_docs_file
from .validation import get_operational_system, check_version_python, check_python_compile
from .__init__ import __version__ as version

LOCAL_PATH = os.getcwd()

logo = r"""

 _ __ ___  _ __  _   _
| '__/ _ \| '_ \| | | |
| | | (_) | | | | |_| |
|_|  \___/|_| |_|\__, |
                 |___/
v{}
""".format(
    version
)


@click.group()
def cli():
    pass


@cli.command()
def info():
    """
    Checks that Rony is correctly installed
    """
    click.echo(logo)


@cli.command()
@click.argument("project_name")
def new(project_name):
    """Create a new Rony project

    Args:
        project_name (str): Name to project
    """
    click.echo(f"Creating project {project_name}")
    # Create project folders
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "etl", "notebooks"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "dags"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "scripts"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "infrastructure"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "tests"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, "docs"))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, ".github", "workflows"))

    # Copy project files
    copy_files(LOCAL_PATH, project_name)
    write_readme_file(LOCAL_PATH, project_name)
    write_docs_file(LOCAL_PATH, project_name)

    os.chdir(project_name)
    env_name = f"{project_name}_env"
    os.environ["ENV_NAME"] = env_name
    check_python_compile()

    # Create git repo
    os.system("git init")
    print(
        "A git repository was created. You should add your files and make your first commit.\n"
    )


@click.argument("image_name")
@cli.command()
def build(image_name):
    """Build a docker image with given image_name. Only run if you have docker installed.
    One should be at the root directory

    Args:
        image_name (str): Name to image docker
    """
    if not os.path.exists("Dockerfile"):
        click.echo("You gotta have a Dockerfile file.")
    else:
        os.system(f"docker build -t {image_name} .")


@click.argument("image_name")
@cli.command()
def run(image_name):
    """Run a container with given image_name.
    Only run if you have docker installed.]

    Args:
        image_name (str): Name to image docker
    """
    if not os.path.exists("Dockerfile"):
        click.echo("You gotta have a Dockerfile file")
    else:
        os.system(f"docker run --rm {image_name}")
