resource "aws_lambda_function" "decompresss3" {
  filename      = "../../functions/fn_example_script.zip"
  function_name = "${local.prefix}_decompressS3"
  role          = aws_iam_role.lambda_decompress.arn
  handler       = "handler.handler"
  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  #source_code_hash = filebase64sha256("../functions/fn_example_script.zip")
  runtime     = "python3.8"
  timeout     = 900
  memory_size = 10000
  // environment {
  //   variables = {
  //   }
  // }

  tags = local.common_tags

}
