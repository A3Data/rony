resource "google_cloudfunctions_function_iam_member" "invoker_fn_example_script" {
  project        = google_cloudfunctions_function.fn_example_script.project
  region         = google_cloudfunctions_function.fn_example_script.region
  cloud_function = google_cloudfunctions_function.fn_example_script.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
  depends_on = [google_cloudfunctions_function.fn_example_script]
}