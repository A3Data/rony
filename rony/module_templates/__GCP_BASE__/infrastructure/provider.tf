provider "google" {
  credentials = file("")
  project     = var.project_id
  region      = var.region_id
  zone        = var.zone_id
}