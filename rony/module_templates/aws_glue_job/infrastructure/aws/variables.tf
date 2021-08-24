
variable "glue_scripts" {
  description = "List of glue scripts to be uploaded"
  type        = list(string)
  default = [
    "process_base_educacao",
    "teste_script"
  ]
}

variable "bucket_glue_job" {
  default = "bucket_glue_job"
}

