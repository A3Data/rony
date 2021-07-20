########   Job files Storage    ############
resource "google_storage_bucket" "rony_job_files" {
  name          = var.rony_job_files
  location      = var.region_id
  storage_class = "STANDARD"
}

########   Upload dag files to cloud storage   ############
resource "google_storage_bucket_object" "upload_dag_composer_dataproc" {
	name = "dags/dataproc_dag.py"
	bucket = google_composer_environment.composer.config.dag_gcs_prefix
	source = "../dags/dataproc_dag.py"
}

########   Upload job files to cloud storage   ############
resource "google_storage_bucket_object" "upload_job_files" {
	name = "titanic_job"
	bucket = var.bucket_composer
	source = "../jobs/titanic_job.py"
}