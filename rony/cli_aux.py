import importlib
import pkgutil

plugins = [
    importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('rony_')
]

def get_cli_decorators(command):
    """Return the decorators to be added to commands

    Args:
        command (str): Name of the command ran
    """

    all_decorators = []

    for plugin in plugins:
        if hasattr(plugin, 'cli_aux'):
            all_decorators += plugin.cli_aux.get_cli_decorators(command)

    return all_decorators



def get_modules_to_add(command, opts, ctx):
    """Return the modules to be added base on the command ran

    Args:
        command (str): Name of the command ran
        opts (dict): Dict with options and flags passade to the command line
    """

    all_modules = []

    if command == 'new':
        if opts['provider'] == 'aws':
            all_modules.append('__AWS_BASE__')

    for plugin in plugins:
        if hasattr(plugin, 'cli_aux'):
            all_modules += plugin.cli_aux.get_modules_to_add(command, opts, ctx)

    return all_modules



