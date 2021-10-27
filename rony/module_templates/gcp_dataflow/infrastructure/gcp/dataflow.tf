resource "google_dataflow_job" "dataflow_job" {
  name                    = var.dataflow_job_name
  template_gcs_path       = "gs://${var.bucket_dataflow}-${var.account}/templates/${var.dataflow_job_name}"
  temp_gcs_location       = "gs://${var.bucket_dataflow}-${var.account}/temp"
  enable_streaming_engine = true
  max_workers             = 2
  on_delete               = "cancel"
  project                 = var.project_id
  region                  = var.region_id
  depends_on              = [null_resource.dataflow_job]
}