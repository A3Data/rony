resource "google_pubsub_topic" "rony_topic" {
  name = var.pubsub_topic
}

resource "google_pubsub_subscription" "rony_sub" {
  name  = var.pubsub_subscription
  topic = google_pubsub_topic.rony_topic.name

  # 7 dias
  message_retention_duration = "604800s"
  retain_acked_messages      = true

  ack_deadline_seconds = 20

  # Nunca expira
  expiration_policy {
    ttl = ""
  }

  # Prazo de atraso mínimo de entrega
  retry_policy {
    minimum_backoff = "10s"
  }

  enable_message_ordering = false
}