resource "google_storage_bucket" "bucket_datalake" {
  count         = length(var.bucket_names)
  name          = "${var.bucket_names[count.index]}-${var.account}"
  location      = var.region_id
  storage_class = "STANDARD"
}