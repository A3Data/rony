import click
import os
import re
import sys
from .writer import *
from .__init__ import __version__ as version

LOCAL_PATH = os.getcwd()

logo = r"""
 ____                   
|  _ \ ___  _ __  _   _ 
| |_) / _ \| '_ \| | | |
|  _ < (_) | | | | |_| |
|_| \_\___/|_| |_|\__, |
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
@click.option('-imp', '--implemented', 'implemented', prompt='Do you want to start with an implemented example (recommended) [y/n]?', 
            default='y', show_default=True)
def new(project_name, implemented):
    """
    Create a new Rony project
    """
    if implemented in ['yes', 'ye', 'y', 'Yes', 'YES', 'Y']:
        file_source = 'file_text'
    elif implemented in ['no', 'n', 'No', 'NO', 'N']:
        file_source = 'not_implemented_file_text'
    
    click.echo(f"Creating project {project_name}")
    # Create project folders
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'etl'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'dags'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'scripts'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, 'tests'))
    os.makedirs(os.path.join(LOCAL_PATH, project_name, '.github/workflows'))

    
    
