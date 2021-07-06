resource "aws_glue_crawler" "glue_crawler" {
  count         = length(var.database_names)
  database_name = var.database_names[count.index]
  name          = "${var.database_names[count.index]}_crawler"
  #role          = aws_iam_role.glue_role.arn
  role = "GlueCrawlerRole"

  s3_target {
    path = var.bucket_paths[count.index]
  }

  # tags = merge(
  # local.common_tags,
  # map("Name", "tag_name")
  # )

  tags = {
    Project      = "Datalake"
    Owner        = "Data Engineering"
    BusinessUnit = "Data"
    Billing      = "Infrastructure"
    Environment  = "Prod"
    UserEmail    = "rony@a3data.com.br"
    Name         = "rony-exploration-cluster"
    Environment  = "Production"
  }
}