resource "google_storage_bucket" "bucket_datalake" {
  name          = var.bucket_datalake
  location      = var.region_id
  storage_class = "STANDARD"
}

# create empty folder inside the bucket
resource "google_storage_bucket_object" "landing_zone" {
  name          = "landing_zone/"
  content       = "Landing_zone"
  bucket        = var.bucket_datalake
  depends_on    = [google_storage_bucket.bucket_datalake]
}