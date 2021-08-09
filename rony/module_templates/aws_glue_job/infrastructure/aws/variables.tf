variable "glue_scripts" {
  description = "List of glue scripts to be uploaded"
  type        = list(string)
  default     = ["glue_script1", "glue_script2"]
}

variable "glue_scripts_max_capacity" {
  description = "Max DPU capacity for each glue script"
  type        = list(number)
  default     = [5, 5]
}