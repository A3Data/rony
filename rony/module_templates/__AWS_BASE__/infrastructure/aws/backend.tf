# Backend configuration require a AWS storage bucket.
terraform {
  backend "s3" {
    bucket = "terraform-state-rony"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}
