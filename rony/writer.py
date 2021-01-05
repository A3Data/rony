import os
import shutil
import rony

def copy_files(LOCAL_PATH, project_name):
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'Dockerfile'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'run.py'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'lambda_function.py'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'etl', 'lambda_requirements.txt'), os.path.join(LOCAL_PATH, project_name, 'etl'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'requirements.txt'), os.path.join(LOCAL_PATH, project_name))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'cloudwatch.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'glue_crawler.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'iam.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'lambda.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'main.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 's3.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))
    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'infrastructure', 'variables.tf'), os.path.join(LOCAL_PATH, project_name, 'infrastructure'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'scripts', 'build_lambda_package.sh'), os.path.join(LOCAL_PATH, project_name, 'scripts'))

    shutil.copy(os.path.join(rony.__path__[0], 'base_files', 'tests', 'test_lambda.py'), os.path.join(LOCAL_PATH, project_name, 'tests'))
