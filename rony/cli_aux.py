import importlib
import pkgutil
import click

plugins = [
    importlib.import_module(name)
    for finder, name, ispkg in pkgutil.iter_modules()
    if name.startswith("rony_")
]


def get_cli_decorators(command):
    """Return the decorators to be added to commands

    Args:
        command (str): Name of the command ran
    """

    all_decorators = []

    for plugin in plugins:
        if hasattr(plugin, "cli_aux"):
            all_decorators += plugin.cli_aux.get_cli_decorators(command)

    return all_decorators


def get_modules_to_add(command, opts, ctx):
    """Return the modules to be added base on the command ran

    Args:
        command (str): Name of the command ran
        opts (dict): Dict with options and flags passade to the command line
    """

    all_modules = []

    if command == "new":
        if opts["excludeci"] == False:
            all_modules += ["CI_workflows"] 

        if opts["provider"] == "aws":

            all_modules += [ "__AWS_BASE__"]

            if opts["autoconfirm"]:
                all_modules += [
                    "aws_simple_storage_service",
                    "aws_glue_crawler",
                    "aws_lambda_function",
                ]
            else:
                if click.confirm("Add S3 module?", default=True):
                    all_modules.append("aws_simple_storage_service")
                if click.confirm("Add GLUE CRAWLER module?", default=True):
                    all_modules.append("aws_glue_crawler")
                if click.confirm("Add LAMBDA FUNCTION module?", default=True):
                    all_modules.append("aws_lambda_function")

        if opts["provider"] == "gcp":
            
            all_modules += ["__GCP_BASE__"]

            if opts["autoconfirm"]:
                all_modules += [
                    "gcp_cloud_storage",
                    "gcp_bigquery",
                    "gcp_cloud_function",
                    "gcp_pubsub",
                ]
            else:
                if click.confirm("Add CLOUD_STORAGE module?", default=True):
                    all_modules.append("gcp_cloud_storage")
                if click.confirm("Add BIGQUERY module?", default=True):
                    all_modules.append("gcp_bigquery")
                if click.confirm("Add CLOUD FUNCTION module?", default=True):
                    all_modules.append("gcp_cloud_function")
                if click.confirm("Add PUBSUB module?", default=True):
                    all_modules.append("gcp_pubsub")

    for plugin in plugins:
        if hasattr(plugin, "cli_aux") and hasattr(plugin.cli_aux, "get_modules_to_add"):
            all_modules += plugin.cli_aux.get_modules_to_add(command, opts, ctx)

    return all_modules


def get_autocomplete(command, opt_name):
    def autocomplete(ctx, args, incomplete):
        return [opt for opt in options if (incomplete in opt[0])]

    options = []

    if command == "new":
        if opt_name == "provider":
            options.append(("aws", "AWS provider"))
            options.append(("gcp", "GCP provider"))

    for plugin in plugins:
        if hasattr(plugin, "cli_aux") and hasattr(plugin.cli_aux, "get_autocomplete"):
            options += plugin.cli_aux.get_autocomplete(command, opt_name)

    return autocomplete
