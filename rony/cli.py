import click
import os
from .validation import get_operational_system, check_version_python, check_python_compile
from .module_writer import modules_autocomplete, write_module, create_module_from_diff
from .cli_aux import get_modules_to_add, get_cli_decorators, get_autocomplete
from .__init__ import __version__ as version

from datetime import datetime

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
@click.option('--provider', '-p', default = 'aws', autocompletion = get_autocomplete('new', 'provider'))
@click.pass_context
def new(ctx, project_name, **kwargs):
    """Create a new Rony project

    Args:
        project_name (str): Name to project
        kwargs (dict): Flags and options
    """
    click.echo(f"Creating project {project_name}")

    # Inputs to be passed to all modules
    custom_inputs = {
        'project_name':project_name, 
        "project_start_date": datetime.today().strftime("%B %d, %Y")
    }    

    # Creating project directory
    os.makedirs(os.path.join(LOCAL_PATH, project_name))

    # Getting all modules to be added
    module_names = get_modules_to_add('new', kwargs, ctx)

    # Running modules
    for module_name in set(module_names):
        write_module(
            os.path.join(LOCAL_PATH, project_name),
            module_name,
            True,
            custom_inputs,
        )
        
    os.chdir(project_name)
    env_name = f"{project_name}_env"
    os.environ["ENV_NAME"] = env_name
    check_python_compile()

    # Create git repo
    os.system("git init")
    print(
        "A git repository was created. You should add your files and make your first commit.\n"
    )

for dec in get_cli_decorators('new'):
    new = dec(new)

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


@click.argument("module_name", type = click.STRING, autocompletion=modules_autocomplete)
@click.option('-y','--autoconfirm', is_flag=True)
@cli.command()
def add_module(module_name, autoconfirm):
    """Add new module to rony project
    One should be at the root directory

    Args:
        module_name (str): Name of the module to be added
    """
    write_module(LOCAL_PATH, module_name, autoconfirm)


@click.argument("module_name", type = click.STRING, autocompletion=modules_autocomplete)
@cli.command()
def diff_2_module(module_name):
    """Add new module to rony project
    One should be at the root directory

    Args:
        module_name (str): Name of the module to be added
    """
    create_module_from_diff(module_name)