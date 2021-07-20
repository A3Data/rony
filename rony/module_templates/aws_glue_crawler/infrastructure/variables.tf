variable "database_names" {
  description = "Create databases with these names"
  type        = list(string)
  default = [
    #landing-zone
    "dl_teste_titanic",
    "dl_teste_enem"
  ]
}

variable "bucket_paths" {
  description = "Paths to S3 bucket used by the crawler"
  type        = list(string)
  default = [
    "s3://datalake-dev-ney-127012818163/raw-data/titanic/",
    "s3://datalake-dev-ney-127012818163/raw-data/enem/"
  ]
}