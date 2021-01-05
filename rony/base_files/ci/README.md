# Github Actions file - Instructions

This sample Github Actions file is set up to deploy infrastructure to AWS. 
It does not actually deploy anything but it sets up a terraform project, validate it and
show `terraform plan`. 

In order to run it correctly, you must set up two **SECRETS**:

- **AWS_ACCESS_KEY_ID**
- **AWS_SECRET_ACCESS_KEY**

for this pipeline uses an AWS action as a building block.

If you don't have an AWS account, set up a fake secret values so you can run the pipeline.