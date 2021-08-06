resource "aws_lambda_function" "decompresss3" {
  filename      = "../lambda/decompress_s3_obj.zip"
  function_name = "decompressS3"
  role          = aws_iam_role.lambda_decompress.arn
  handler       = "handler.handler"
  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = filebase64sha256("../lambda/decompress_s3_obj.zip")
  runtime = "python3.8"
  timeout = 900
  memory_size = 10000
  // environment {
  //   variables = {
  //   }
  // }

  tags = local.common_tags

}
