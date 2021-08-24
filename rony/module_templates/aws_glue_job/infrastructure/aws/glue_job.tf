resource "aws_s3_bucket_object" "glue_script_s3_object" {
  count  = length(var.glue_scripts)
  bucket = aws_s3_bucket.bucket_glue_job.id
  key    = "../etl/glue_scripts/${var.glue_scripts[count.index]}.py"
  source = "../etl/glue_scripts/${var.glue_scripts[count.index]}.py"
  #etag   = filemd5(".glue_scripts/${var.glue_scripts[count.index]}.py")
}

resource "aws_glue_job" "glue_job" {
  count        = length(var.glue_scripts)
  name         = var.glue_scripts[count.index]
  role_arn     = aws_iam_role.glue_role.arn
  glue_version = "2.0"
  command {
    script_location = "s3://${var.bucket_glue_job}-${var.account}/etl/glue_scripts/${var.glue_scripts[count.index]}.py"
    python_version  = "3"
  }

  depends_on = [
    aws_s3_bucket_object.glue_script_s3_object,
  ]

}