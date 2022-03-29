#### Terraform Apply #####

./CI/scripts/pre_terraform.sh

export AWS_CSM_ENABLED=true
export AWS_CSM_PORT=31000
export AWS_CSM_HOST=127.0.0.1

cd infrastructure/aws/

(iamlive --output-file './policy.json' > /dev/null &)

terraform init
terraform workspace select $1 || terraform workspace new $1
terraform apply $2

pkill iamlive

sleep 1
echo ""
GREEN='\033[0;32m'
NC='\033[0m' # No Color
echo -e "${GREEN}PERMISSIONS USED:${NC}"
cat ./policy.json

cd ../..

###########################