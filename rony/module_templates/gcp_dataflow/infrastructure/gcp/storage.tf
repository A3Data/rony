resource "google_storage_bucket" "bucket_dataflow" {
  name          = "${var.bucket_dataflow}-${var.account}"
  location      = var.region_id
  storage_class = "STANDARD"
  force_destroy = true
}

resource "null_resource" "dataflow_job" {
  triggers = {
    always_run = uuid()
  }

  provisioner "local-exec" {
    command = "chmod +x ../../dataflow/scripts/deploy_custom_dataflow_templates.sh"
  }

  provisioner "local-exec" {
    command = join(" ", [
      "../../dataflow/scripts/deploy_custom_dataflow_templates.sh",
      var.project_id,
      var.region_id,
      "gs://${var.bucket_dataflow}-${var.account}/temp",
      "gs://${var.bucket_dataflow}-${var.account}/templates/${var.dataflow_job_name}",
      "projects/${var.project_id}/topics/${var.pubsub_topic_name}",
      "gs://${var.bucket_names[0]}-${var.account}/pubsub/events/"
    ])
  }

  depends_on = [google_storage_bucket.bucket_dataflow]
}