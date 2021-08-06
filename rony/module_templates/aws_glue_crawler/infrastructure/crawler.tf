resource "aws_iam_role" "lambda_decompress" {
  name        = "Role_Lambda_decompress_S3"
  path        = "/"
  description = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  policy      = file("./iam/Role_Lambda_decompress_S3.json")
}

resource "aws_iam_policy" "lambda_decompress" {
  name        = "Policy_Lambda_decompress_S3"
  path        = "/"
  description = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  policy      = file("./iam/Policy_Lambda_decompress_S3.json")
}

resource "aws_iam_role_policy_attachment" "lambda_attach" {
  role       = aws_iam_role.lambda_decompress.name
  policy_arn = aws_iam_policy.lambda_decompress.arn
}

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