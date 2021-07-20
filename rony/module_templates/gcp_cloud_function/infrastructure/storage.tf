resource "google_storage_bucket" "bucket_functions" {
  name          = var.bucket_functions
  location      = var.region_id
  storage_class = "STANDARD"
}

resource "null_resource" "fn_example_script" {
  triggers     = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command    = "zip -urj ../functions/fn_example_script.zip ../functions/fn_example_script"
  }
}

resource "google_storage_bucket_object" "fn_example_script" {
  name       = "fn_example_script"
  bucket     = var.bucket_functions
  source     = "../functions/fn_example_script.zip"
  depends_on = [null_resource.fn_example_script, google_storage_bucket.bucket_functions]
}