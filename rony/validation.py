import os
import sys
from os import path

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
    env_name = os.environ.get("ENV_NAME")
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