resource "google_storage_bucket" "bucket_functions" {
  name          = "${var.bucket_functions}-${var.account}"
  location      = var.region_id
  storage_class = "STANDARD"
}

resource "null_resource" "fn_write_file_gcs_bgq" {
  triggers = {
    always_run = uuid()
  }

  provisioner "local-exec" {
    command = "zip -rj ../../functions/fn_write_file_gcs_bgq_${local.uuid}.zip ../../functions/fn_write_file_gcs_bgq"
  }
}

resource "google_storage_bucket_object" "fn_write_file_gcs_bgq" {
  name       = "fn_write_file_gcs_bgq_${local.uuid}"
  bucket     = "${var.bucket_functions}-${var.account}"
  source     = "../../functions/fn_write_file_gcs_bgq_${local.uuid}.zip"
  depends_on = [null_resource.fn_write_file_gcs_bgq, google_storage_bucket.bucket_functions]
}