# Contributing to Rony

## Getting started

### Forking repository

The first step in contributing to Rony is to fork the repository and clone the fork to your machine.

### Remove any Rony installations

```bash
pip uninstall rony
```

### "Install" Rony in development mode

Inside your fork directory, use the following command:

```bash
python setup.py develop 
```

This command will "install" Rony in [development mode](https://setuptools.readthedocs.io/en/latest/userguide/development_mode.html).
That way, the Rony cli command will point directly to the source code. Any changes you make to the code will be immediately available.

## Adding new modules

All Rony module templates are kept in ["rony/module_templates/"](rony/module_templates) folder.
To add a new module, you just need to add a folder named after the module and add all the files and folders from the module to it.

The files and folders need to respect the exact same folder structure they will have on the user's project.

When a user install your module, all the files will be copied to the project's directory following the same structure of the "module_template" folder.
If any file already exists on user's project, its content will be appended with the template content.

### Module template config file

Optionally, you can add a json file containing some information about the module, and any inputs to be asked to the user:

```json
{
    "info": "Base files with implemented example",
    "input_info": [
        ["project_name", "My Project", "Enter your project name"],
        ["project_start_date", "01/01/21", "Enter the date your project started"]
    ],
    "instructions":[
        "This will be displayed on the terminal right after the module is added",
        "Each element of this list will be a line on the terminal"
    ],
    "developers":[
        "rony@a3data.com.br"
    ]
}
```

The config file needs to have the same name as the module template folder, with the `.json` extension.

The `info` field of the json is used as a description of the module, when user uses autocompletion.

The `input_info` field of the json contains a list of lists. Each list contains information about one of the module's user inputs:

- 1st element is the name of the input
- 2nd element is the default value
- 3rd element is the text the user will be prompted when being asked for the input

The `instructions` field of the json contains a list of strings. The content of this list will be displayed to the users right after the new module is added to their project.

The `developers` field of the json contains a list of strings. The content of this list will be displayed to the users right after the new module is added to their project.


### Using jinja template files

Optionally, you can let Rony process the template files as [jinja](https://jinja.palletsprojects.com/en/2.11.x/) templates.

To let Rony know the file needs to be interpreted as a jinja template, you just need to add `.tpl`before the file extension (`sample.py`would become `sample.tpl.py`).

All the user inputs are passed to the template as keys of `inputs` variable. For example:

#### **`README.tpl.md`**
``` jinja
# {{ inputs['project_name'] }}

Project started in {{ inputs['project_start_date'] }}.


**Please, complete here information on using and testing this project.**
```

After the template above is processed, it will become:

#### **`README.md`**
``` md
# My Project

Project started in 01/01/21.


**Please, complete here information on using and testing this project.**
```

### Empty Folders and .gitignore files

Empty folders added to the templates, would not be added to Rony's git repository.

To deal with that a empty file named `.ronyignore` needs to be added to empty folders. Those files will be ignored by Rony and will not be added to the user's project

Similarly `.gitignore` files inside the templates would be processed by git and other files could be mistakenly ignored by git. To deal with that the `.gitignore` can be renamed to `.tpl.gitignore`. They will be ignored by git, but will be renamed by Rony when populating the user's project.


## Creating plugins for Rony

It is possible to create plugins to extend Rony's functionality. Rony considers a plugin any package which name starts with `rony_`.

Currently, the only functionality that can be extended via plugins, is the `add-module` functionality. The plugins can add new modules to be available via `rony add-module` command.

To create a plugin you can use [this example repo](https://github.com/RodrigoATorres/rony_a3_modules). To add new modules you should follow the same procedure as adding modules directly to Rony. Just add the files to the `module_templates` folder.