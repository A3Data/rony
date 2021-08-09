resource "google_storage_bucket" "bucket_datalake" {
  count         = length(var.bucket_names)
  name          = "${var.bucket_names[count.index]}-${var.account}"
  location      = var.region_id
  storage_class = "STANDARD"
}

# folder inside landing-zone
resource "google_storage_bucket_object" "public_dataset" {
  name       = "public_dataset/"
  content    = "folder"
  bucket     = "${var.bucket_names[0]}-${var.account}"
  depends_on = [google_storage_bucket.bucket_datalake]
}