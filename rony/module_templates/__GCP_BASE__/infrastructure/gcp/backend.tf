# Backend configuration require a google storage bucket.
terraform {
  backend "gcs" {
    bucket      = ""
    prefix      = "prod"
    credentials = "../../config/service-account.json"
  }
}