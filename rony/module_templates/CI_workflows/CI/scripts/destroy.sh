#!/bin/sh
set -e

#### Terraform Apply #####



export AWS_CSM_ENABLED=true
export AWS_CSM_PORT=31000
export AWS_CSM_HOST=127.0.0.1

cd infrastructure/

(iamlive --output-file './policy.json' > /dev/null &)

terraform init
terraform workspace select $1
terraform destroy $2

pkill iamlive

sleep 1
echo PERMISSIONS USED:
cat ./policy.json

cd ..

###########################