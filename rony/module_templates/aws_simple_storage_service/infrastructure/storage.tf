resource "aws_s3_bucket" "buckets" {
  count   = length(var.bucket_names)
  bucket  = "${var.bucket_names[count.index]}-${var.account}"
  acl     = "private"


# tags = merge(
# local.common_tags,
# map("Name", "tag_name")
# )

tags = {
    Project        = "Datalake"
    Owner          = "Data Engineering"
    BusinessUnit   = "Data"
    Billing        = "Infrastructure"
    Environment    = "Prod"
    UserEmail      = "rony@a3data.com.br"
    Name           = "rony-exploration-cluster"
    Environment    = "Production"
  }

server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

