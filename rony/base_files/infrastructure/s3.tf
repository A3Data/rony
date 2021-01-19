resource "aws_s3_bucket" "dl" {
  bucket = "${var.base_bucket_name}-${var.account}"
  acl    = "private"

  tags = {
    foo = "bar"
  }
  
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
