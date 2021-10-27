resource "aws_glue_crawler" "glue_crawler" {
  count         = length(var.database_names)
  database_name = var.database_names[count.index]
  name          = "${local.prefix}-${var.database_names[count.index]}_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "${local.prefix}-${var.bucket_paths[count.index]}-${var.account}"
  }

  tags = local.common_tags

}