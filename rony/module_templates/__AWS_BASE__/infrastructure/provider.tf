provider "aws" {
  credentials = file("../config/service-account.json")
  project     = var.project_id
  region      = var.region_id
  zone        = var.zone_id
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}



