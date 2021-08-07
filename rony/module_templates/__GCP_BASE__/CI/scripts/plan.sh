#### Terraform Plan #####

./CI/scripts/pre_terraform.sh

cd infrastructure/gcp/
terraform init
terraform workspace select $1 || terraform workspace new $1
terraform plan
cd ../../

######################################