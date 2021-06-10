resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "dataset_name"
  friendly_name               = "dataset_friendly_name"
  description                 = "Example of dataset"
  location                    = var.region_id
  delete_contents_on_destroy  = true
}

resource "google_bigquery_table" "table" {
  dataset_id          = "dataset_name"
  friendly_name       = "table_friendly_name"
  table_id            = "table_name"
  schema              = file("../schemas/iris.json")
  description         = "Example of table"
  project             = var.project_id
  deletion_protection = false
  depends_on          = [google_bigquery_dataset.dataset]
}