variable "account" {
  default = 123456789
}

variable "bucket_names" {
  description = "Create cloud storage"
  type        = list(string)
  default = [
    "landing-zone",
    "processing-zone",
    "delivery-zone"
  ]
}