provider "google" {
  credentials = file("../config/service-account.json")
  project     = var.project_id
  region      = var.region_id
  zone        = var.zone_id
}

