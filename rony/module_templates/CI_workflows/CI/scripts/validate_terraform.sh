#!/bin/sh
set -e

### Validate terraform

cd infrastructure/
terraform init -backend=false
terraform validate
terraform fmt -check
cd ..

#####################