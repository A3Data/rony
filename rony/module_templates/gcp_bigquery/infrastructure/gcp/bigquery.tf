resource "google_bigquery_dataset" "dataset" {
  dataset_id                 = "rony_lab"
  friendly_name              = "rony_lab"
  description                = "Rony laboratory"
  location                   = var.region_id
  delete_contents_on_destroy = true
}

resource "google_bigquery_table" "table" {
  dataset_id          = "rony_lab"
  friendly_name       = "iris"
  table_id            = "iris"
  schema              = file("../../schemas/iris.json")
  description         = "Titanic example"
  project             = var.project_id
  deletion_protection = false
  depends_on          = [google_bigquery_dataset.dataset]
}