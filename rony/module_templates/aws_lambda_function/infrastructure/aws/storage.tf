resource "aws_s3_bucket" "bucket_functions" {
  bucket = "${local.prefix}-${var.bucket_functions}-${var.account}"
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

resource "null_resource" "fn_example_script" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "zip -rj ../../functions/fn_example_script.zip ../../functions/fn_example_script"
  }
}