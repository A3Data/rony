import os
import shutil
from datetime import datetime
import rony

def copy_files(LOCAL_PATH, project_name):
    """Copy files to project

    Args:
        LOCAL_PATH (str): Local Path
        project_name (str): Project Name
    """    
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'Dockerfile'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'run.py'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'lambda_function.py'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'lambda_requirements.txt'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'requirements.txt'), os.path.join(LOCAL_PATH, project_name))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', '.gitignore'), os.path.join(LOCAL_PATH, project_name))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'cloudwatch.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'glue_crawler.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'iam.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'lambda.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'main.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 's3.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'variables.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'ecr.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'scripts', 'build_lambda_package.sh'), os.path.join(LOCAL_PATH, project_name, 'scripts'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'tests', 'test_lambda.py'), os.path.join(LOCAL_PATH, project_name, 'tests'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'ci', 'github_ci.yml'), os.path.join(LOCAL_PATH, project_name, '.github', 'workflows'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'ci', 'README.md'), os.path.join(LOCAL_PATH, project_name, '.github', 'workflows'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'dags', 'conditional_example.py'), os.path.join(LOCAL_PATH, project_name, 'dags'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'dags', 'titanic_example.py'), os.path.join(LOCAL_PATH, project_name, 'dags'))


def write_readme_file(LOCAL_PATH, project_name):
    with open(os.path.join(LOCAL_PATH, project_name, 'README.md'), 'w+') as outfile:
        outfile.write(f"""# {project_name}

Project started in {datetime.today().strftime("%B %d, %Y")}.

**Please, complete here information on using and testing this project.**
""")