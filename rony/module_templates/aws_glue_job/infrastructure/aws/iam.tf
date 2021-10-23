data "template_file" "policy_glue_job" {
  template = file("./permissions/Policy_Glue_Job.tplt.json")
  vars = {
    bucket_name = aws_s3_bucket.bucket_glue_job.id
  }
}

resource "aws_iam_role" "glue_role" {
  name = "Role-testes-Crawler"

  assume_role_policy = file("./permissions/Role_Glue_Job.json")

  tags = {
    projeto = "datalake"
  }

}


resource "aws_iam_policy" "glue_policy" {
  name        = "Policy-glue-testes-ServiceRole"
  path        = "/"
  description = "Policy for AWS Glue service role which allows access to related services including EC2, S3, and Cloudwatch Logs"

  policy = file("./permissions/Policy_Glue_Job.tplt.json")

}


resource "aws_iam_role_policy_attachment" "glue_attach" {
  role       = aws_iam_role.glue_role.name
  policy_arn = aws_iam_policy.glue_policy.arn
}