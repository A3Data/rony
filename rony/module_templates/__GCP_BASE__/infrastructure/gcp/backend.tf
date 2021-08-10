# Backend configuration require a google storage bucket.
terraform {
  backend "gcs" {
    bucket = ""
    prefix = "state/terraform.tfstate"
  }
}