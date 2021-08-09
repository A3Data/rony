#### Terraform Format GCP #####

./CI/scripts/pre_terraform.sh

cd infrastructure/gcp/
terraform fmt
cd ../../

######################################