# zip o diretorio da function fn_stg_bgq
resource "null_resource" "fn_example_script" {
  triggers     = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command    = "zip -urj ../etl/fn_example_script.zip ../etl/fn_example_script"
  }
}

# copia o arquivo para o bucket
resource "google_storage_bucket_object" "fn_example_script" {
  name       = "fn_example_script"
  bucket     = var.bucket_functions
  source     = "../functions/fn_load_gcs_bgq.zip"
  depends_on = [null_resource.fn_example_script]
}


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
    resource    = var.bucket_datalake
  }
}