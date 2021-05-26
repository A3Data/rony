# Github Actions file - Instructions

This sample Github Actions file is set up to deploy infrastructure to AWS. 
It does not actually deploy anything but it sets up a terraform project, validate it and
show `terraform plan`. 

In order to run it correctly, you must set up two **SECRETS**:

- **AWS_ACCESS_KEY_ID**
- **AWS_SECRET_ACCESS_KEY**

for this pipeline uses an AWS action as a building block.

If you **don't have an AWS account**, you should delete this section:

```yaml
    - name: HashiCorp - Setup Terraform
      uses: hashicorp/setup-terraform@v1.2.1
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1

    - name: Terraform Apply
      run: |
        cd infrastructure
        terraform init
        terraform validate
        terraform plan
```