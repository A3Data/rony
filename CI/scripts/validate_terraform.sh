#!/bin/bash
set -e

source ./CI/scripts/helpers.sh

validade_module()
{
    # Installing module
    mkdir $1
    cd $1
    install_module $1

    # Running terraform validade on each module
    GREEN='\033[0;32m'
    NC='\033[0m' # No Color
    echo -e "${GREEN}VALIDATING TERRAFORM FOR MODULE: $1 ${NC}"
    chmod +x ./CI/scripts/validate_terraform.sh
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