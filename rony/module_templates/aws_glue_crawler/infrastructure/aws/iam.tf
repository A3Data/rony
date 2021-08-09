resource "aws_iam_role" "glue_role" {
<<<<<<< HEAD:rony/module_templates/aws_glue_crawler/infrastructure/aws/iam.tf
  name                    = "${var.prefix}_Role_GlueCrawler"
  path                    = "/"
  description             = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  assume_role_policy      = file("./permissions/Role_GlueCrawler.json")
=======
  name               = "Role_GlueCrawler"
  path               = "/"
  description        = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  assume_role_policy = file("./permissions/Role_GlueCrawler.json")
>>>>>>> daf0fae4887af821d5bdf26960b100797f88781f:rony/module_templates/aws_glue_crawler/infrastructure/iam.tf
}

resource "aws_iam_policy" "glue_policy" {
  name        = "${var.prefix}_Policy_GlueCrawler"
  path        = "/"
  description = "Provides write permissions to CloudWatch Logs and S3 Full Access"
  policy      = file("./permissions/Policy_GlueCrawler.json")
}

resource "aws_iam_role_policy_attachment" "glue_attach" {
  role       = aws_iam_role.glue_role.name
  policy_arn = aws_iam_policy.glue_policy.arn
}