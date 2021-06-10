resource "google_service_account" "composer" {
  account_id   = "composer-env-account"
  display_name = "Test Service Account for Composer Environment"
}