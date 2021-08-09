resource "aws_s3_bucket" "bucket_functions" {
<<<<<<< HEAD:rony/module_templates/aws_lambda_function/infrastructure/aws/storage.tf
  bucket       = "${var.prefix}-${var.bucket_functions}-${var.account}"
  acl          = "private"
=======
  bucket = "${var.bucket_functions}-${var.account}"
  acl    = "private"
>>>>>>> daf0fae4887af821d5bdf26960b100797f88781f:rony/module_templates/aws_lambda_function/infrastructure/storage.tf

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
<<<<<<< HEAD:rony/module_templates/aws_lambda_function/infrastructure/aws/storage.tf
    command    = "zip -urj ../../functions/fn_example_script.zip ../../functions/fn_example_script"
=======
    command = "zip -urj ../functions/fn_example_script.zip ../functions/fn_example_script"
>>>>>>> daf0fae4887af821d5bdf26960b100797f88781f:rony/module_templates/aws_lambda_function/infrastructure/storage.tf
  }
}