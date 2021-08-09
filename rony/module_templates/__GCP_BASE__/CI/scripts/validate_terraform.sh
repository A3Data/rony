### Validate terraform

cd infrastructure/gcp/
terraform init -backend=false
terraform validate
# terraform fmt -check
cd ../../

#####################