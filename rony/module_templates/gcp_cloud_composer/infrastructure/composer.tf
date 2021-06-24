resource "google_composer_environment" "composer" {
  name   = var.composer_name
  region = var.region_id
  config {
    software_config {
      image_version = "composer-1.17.0-preview.3-airflow-2.0.1"

      python_version = "3"

      airflow_config_overrides = {
        core-load_example = "True"
      }

      pypi_packages = {
        scipy = "==1.1.0"
      }

      env_variables = {
        EXAMPLE = "example"
      }
    }

    node_count = 3

    node_config {
      zone         = var.zone_id
      machine_type = "n1-standard-1"

      network    = google_compute_network.composer.id
      subnetwork = google_compute_subnetwork.composer.id
    }
  }
}

resource "google_compute_network" "composer" {
  name                    = "composer-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "composer" {
  name          = "composer-subnetwork"
  ip_cidr_range = "10.2.0.0/16"
  region        = var.region_id
  network       = google_compute_network.composer.id
}
