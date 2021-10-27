resource "aws_kinesis_stream" "rony_kinesis_stream" {
  name             = "${local.prefix}-${var.kinesis_stream_name}-${var.account}"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

  tags = local.common_tags

}