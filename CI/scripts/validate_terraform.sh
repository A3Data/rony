#!/bin/sh
set -e

# Recursive function to install module ant its dependencies
install_module()
{
    d="../../rony/module_templates/$1/"
    # Extracting module name from module path
    module_name=$(basename "$d")
    # Module json file path
    json_path=$(echo $d | sed 's|/$|.json|')

    echo "$module_name"
    jq -c '.dependencies|.[]' $json_path | while read i; do
        dep_name=$(echo  $i | sed 's/"//g')
        echo dep_name
        install_module "$dep_name"
    done

   rony add-module $module_name -y
}


validade_module()
{
    # Installing module
    mkdir $1
    cd $1
    install_module $1

    # Running terraform validade on each module
    GREEN='\033[0;32m'
    NC='\033[0m' # No Color
    echo "${GREEN}VALIDATING TERRAFORM FOR MODULE: $1 ${NC}"
    ./CI/scripts/validate_terraform.sh
    cd ..
}


# Install rony
pip3 install .

# Creates testing directory
rm -rf ./ci-test
mkdir ./ci-test
cd ./ci-test


# If no arguments are supplied, all modules will be validated
# If module name is supplied as an argument, it will be validated
if [ $# -eq 0 ]
  then
    # Iterating over all module templates
    for d in ../rony/module_templates/*/ ; do
        module_name=$(basename "$d")
        validade_module $module_name
    done
  else
    validade_module $1
fi