resource "aws_s3_bucket" "dl" {
  bucket = "${var.base_bucket_name}-${var.account}"
  acl    = "private"

  tags = {
    foo = "bar"
  }

}