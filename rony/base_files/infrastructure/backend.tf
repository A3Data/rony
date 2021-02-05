terraform {
  backend "s3" {
    bucket         = "my-bucket-state-backend"
    key            = "terraform.tfstate"
<<<<<<< HEAD
    region         = "us-east-1"
=======
    region         = var.aws_region
>>>>>>> origin/main
  }
}