resource "aws_iam_role" "glue_role" {
  name               = "${local.prefix}_Role_GlueCrawler"
  path               = "/"
  description        = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  assume_role_policy = file("./permissions/Role_GlueCrawler.json")
}

resource "aws_iam_policy" "glue_policy" {
  name        = "${local.prefix}_Policy_GlueCrawler"
  path        = "/"
  description = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  policy      = file("./permissions/Policy_GlueCrawler.json")
}

resource "aws_iam_role_policy_attachment" "glue_attach" {
  role       = aws_iam_role.glue_role.name
  policy_arn = aws_iam_policy.glue_policy.arn
}