#### Terraform Apply #####

cd infrastructure/gcp/

terraform init
terraform workspace select $1 || terraform workspace new $1
terraform destroy $2

cd ../../

###########################