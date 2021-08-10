resource "aws_s3_bucket_object" "glue_script_s3_object" {
  count  = length(var.glue_scripts)
  bucket = "${local.prefix}-${aws_s3_bucket.dl.id}"
  key    = "/.glue_scripts/${var.glue_scripts[count.index]}.py"
  source = ".glue_scripts/${var.glue_scripts[count.index]}.py"
  etag   = filemd5(".glue_scripts/${var.glue_scripts[count.index]}.py")
}


resource "aws_glue_job" "glue_job" {
  count        = length(var.glue_scripts)
  name         = "${local.prefix}-${var.glue_scripts[count.index]}"
  role_arn     = aws_iam_role.glue_job.arn
  max_capacity = var.glue_scripts_max_capacity[count.index]
  glue_version = "2.0"
  command {
    script_location = "s3://${aws_s3_bucket.dl.bucket}/.glue_scripts/${var.glue_scripts[count.index]}.py"
    python_version  = "3"
  }
  default_arguments = {
    "--additional-python-modules" = "pyarrow==2,awswrangler==2.7.0"
  }
  depends_on = [
    aws_s3_bucket_object.glue_script_s3_object,
  ]
}
