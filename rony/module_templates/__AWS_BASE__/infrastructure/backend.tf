# Backend configuration require a AWS storage bucket.
terraform {
  backend "aws" {
    bucket        = "terraform-state"
    key           = "state/terraform.tfstate"
    region        = "us-east-1"
  }
}