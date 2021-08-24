resource "aws_s3_bucket" "bucket_glue_job" {
  bucket = "${var.prefix}-${var.bucket_glue_job}-${var.account}"
  acl    = "private"

    tags = local.common_tags

    server_side_encryption_configuration {
      rule {
        apply_server_side_encryption_by_default {
          sse_algorithm = "AES256"
       }
     }
   }
}