# Quick Start

After installing Rony you can test if the installation is ok by running:

```bash
rony info
```

and you shall see a cute logo. Then,

1) Create a new project:

```bash
rony new project_rony
```

2) Rony already creates a virtual environment for the project. 
Windows users can activate it with 

```
<project_name>_env\Scripts\activate
```

Linux and MacOS users can do

```bash
source <project_name>_env/bin/activate
```

3) After activating, you should install some libraries. There are a few suggestions in “requirements.txt” file:

```bash
pip install -r requirements.txt
```

## Implementation suggestions

When you start a new `rony` project, you will by default create a project with `aws` as `provider` and you will be asked which modules you want to implement in yout project.

You can implement modules after the project creation using the following command in your project's root folder. 

```bash
rony add-module <module_name>
```

The module_name can be found on the module_templates folder in the rony project folder.

When you start a new `rony` project, you will find:

- an `infrastructure` folder with terraform code creating on the chosen provider:
  - a backend file
    - For the aws provider, you will need to create a bucket manually and reference its name on the bucket variable.
  - a provider file
  - a variables file
  - files for the modules implemented during the project creation

- a `CI` folder with a docker-composer file and CI scripts and tests
  
- a `Makefile` file containing shortcut commands for the project

You also have a `scripts` folder with a bash file that builds a lambda deploy package.

**Feel free to adjust and adapt everything according to your needs.**
