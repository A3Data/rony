import click
import os
import re
import sys
from os import path
from .writer import copy_files, write_readme_file
from .__init__ import __version__ as version

LOCAL_PATH = os.getcwd()

logo = r"""

 _ __ ___  _ __  _   _ 
| '__/ _ \| '_ \| | | |
| | | (_) | | | | |_| |
|_|  \___/|_| |_|\__, |
                 |___/ 
v{}
""".format(version)

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
@click.argument('project_name')
def new(project_name):
    """
    Create a new Rony project
    """
    click.echo(f"Creating project {project_name}")
    # Create project folders
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'etl/notebooks'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'dags'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'scripts'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'tests'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, '.github/workflows'))

    # Copy project files
    copy_files(LOCAL_PATH, project_name)
    write_readme_file(LOCAL_PATH, project_name)

    os.chdir(project_name)
    new.env_name = f"{project_name}_env"

    # Create git repo
    os.system('git init')
    print("A git repository was created. You should add your files and make your first commit.\n")


env_name = new.env_name    
    
def get_operational_system():
    """
    Check which user's operating system    
    """
    os = sys.platform
    if sys.platform == "linux":
        return "Linux"
    elif sys.platform == "win32":
        return "Windows"
    elif sys.platform == "darwin":
        return "MacOS"
    elif sys.platform == "freebsd8":
        return "FreeBSD"


def check_version_python():
    """
    Checks whether the version of python installed on the system is compatible
    """
    if sys.version_info >= (3,6):
        return True
    else:
        return False

def check_python_compile():
    """
    Checks python3 path location 
    """
    message_env = f"Creating virtual environment {env_name}"
    if get_operational_system() == "Linux" and check_version_python() == True:
        if path.exists("/usr/bin/python3") == True:
            print(message_env)
            os.system(f"python3 -m venv {env_name}")
        else:
            print(message_env)
            os.system(f"python -m venv {env_name}")
    elif get_operational_system() == "Windows" and check_version_python() == True:
        print(message_env)
        os.system(f"python -m venv {env_name}")
    elif get_operational_system() == "MacOS" and check_version_python() == True:
        print(message_env)
        os.system(f"python -m venv {env_name}")
    elif check_version_python == False:
        print('The python version is not supported. Rony is compatible with the version of >= Python 3.6')

check_python_compile()

@click.argument('image_name')
@cli.command()
def build(image_name):
    """
    Build a docker image with given image_name. Only run if you have docker installed.
    One should be at the root directory.
    """
    if not os.path.exists('Dockerfile'):
        click.echo("You gotta have a Dockerfile file.")
    else:
        os.system(f'docker build -t {image_name} .')


@click.argument('image_name')
@cli.command()
def run(image_name):
    """
    Run a container with given image_name. 
    Only run if you have docker installed.
    """
    if not os.path.exists('Dockerfile'):
        click.echo("You gotta have a Dockerfile file")
    else:
        os.system(f'docker run --rm {image_name}')
