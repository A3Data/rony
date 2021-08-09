resource "google_cloudfunctions_function" "fn_example_script" {
  name                  = "fn_example_script"
  runtime               = "python38"
  available_memory_mb   = 2048
  source_archive_bucket = google_storage_bucket_object.fn_example_script.bucket
  source_archive_object = google_storage_bucket_object.fn_example_script.name
  timeout               = 540
  entry_point           = "fn_example_script"
  environment_variables = {
    name   = "fn_example_script"
  }
  depends_on = [google_storage_bucket_object.fn_example_script]

  event_trigger {
    event_type  = "google.storage.object.finalize"
    resource    = "${var.bucket_names[0]}-${var.account}"
  }
}