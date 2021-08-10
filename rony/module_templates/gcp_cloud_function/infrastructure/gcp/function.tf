resource "google_cloudfunctions_function" "fn_write_file_gcs_bgq" {
  name                  = "fn_write_file_gcs_bgq"
  runtime               = "python38"
  available_memory_mb   = 2048
  source_archive_bucket = google_storage_bucket_object.fn_write_file_gcs_bgq.bucket
  source_archive_object = google_storage_bucket_object.fn_write_file_gcs_bgq.name
  timeout               = 540
  entry_point           = "fn_write_file_gcs_bgq"
  environment_variables = {
    project_id   = var.project_id
    dataset_name = google_bigquery_dataset.dataset.dataset_id
    table_name   = google_bigquery_table.table.table_id
  }
  depends_on = [google_storage_bucket_object.fn_write_file_gcs_bgq]

  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = "${var.bucket_names[0]}-${var.account}"
  }
}