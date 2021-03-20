resource "aws_glue_trigger" "{{ inputs['trigger_name'] }}" {
  name     = "{{ inputs['trigger_name'] }}"
  schedule = "{{ inputs['cron_str'] }}"
  type     = "SCHEDULED"

  actions {
    job_name = aws_glue_job.{{ inputs['job_name'] }}.name
  }
}