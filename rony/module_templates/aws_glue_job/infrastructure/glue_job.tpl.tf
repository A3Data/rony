
resource "aws_glue_job" "{{ inputs['job_name'] }}" {
  name     = "{{ inputs['job_name'] }}"
  role_arn = aws_iam_role.glue_role.arn
  command {
    script_location = "{{  's3://${' + inputs['bucket'] +'.bucket/' + inputs['script_s3_key']}}"
  }
  depends_on = [
    aws_s3_bucket_object.my_script,
  ]
}

resource "aws_s3_bucket_object" "my_script" {
  bucket = {{ inputs['bucket'] }}.id
  key    = {{ inputs['script_s3_key'] }}
  source = "{{ inputs['script_local_path'] }}"
  etag   = "{{ '${filemd5("' + inputs['script_local_path'] + '")}' }}"
}