resource "google_composer_environment" "composer" {
  name   = var.composer_example
  region = var.region_id
  config {
    node_count = 4

    node_config {
      zone         = var.zone_id
      machine_type = "e2-medium"

      network    = google_compute_network.composer.id
      subnetwork = google_compute_subnetwork.composer.id

      service_account = google_service_account.composer.name
    }
  }
}

resource "google_compute_network" "composer" {
  name                    = "composer-test-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "composer" {
  name          = "composer-test-subnetwork"
  ip_cidr_range = "10.2.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.composer.id
}