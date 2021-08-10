# Backend configuration require a google storage bucket.
terraform {
  backend "gcs" {
    bucket = ""
    key    = "state/terraform.tfstate"
  }
}