terraform {
  backend "gcs" {
    bucket         = "my-bucket-state-backend"
    prefix         = "prod"
  }
}