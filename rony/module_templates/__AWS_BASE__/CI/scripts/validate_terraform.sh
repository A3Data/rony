### Validate terraform

cd infrastructure/aws/
terraform init -backend=false
terraform validate
# terraform fmt -check
cd ../../

#####################