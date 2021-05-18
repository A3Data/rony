resource "google_storage_bucket" "bucket_name" {
  name          = var.bucket_name
  location      = var.location
  storage_class = "STANDARD"
}

resource "google_storage_bucket_object" "empty_folder" {
  name          = "empty_folder/"
  content       = "Empty folder"
  bucket        = var.bucket_name
}