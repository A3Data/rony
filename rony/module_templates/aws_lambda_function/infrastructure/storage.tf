resource "aws_s3_bucket" "bucket_functions" {
  name          = var.bucket_functions
  location      = var.region_id
  storage_class = "STANDARD"
}

resource "null_resource" "fn_example_script" {
  triggers     = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command    = "zip -urj ../functions/fn_example_script.zip ../functions/fn_example_script"
  }
}