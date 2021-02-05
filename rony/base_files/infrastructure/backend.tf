terraform {
  backend "s3" {
    bucket         = "my-bucket-state-backend"
    key            = "terraform.tfstate"
    region         = var.aws_region
  }
}