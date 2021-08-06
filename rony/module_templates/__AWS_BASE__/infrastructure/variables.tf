variable "project_id" {
  default       = ""
}

variable "region_id" {
  default       = ""
}

variable "zone_id" {
  default       = ""
}

# Prefix configuration and project common tags
locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Project        = "Datalake"
    ManagedBy      = "Terraform"
    Department     = "systems",
    Provider       = "A3DATA",
    Owner          = "Data Engineering"
    BusinessUnit   = "Data"
    Billing        = "Infrastructure"
    Environment    = terraform.workspace
    UserEmail      = "rony@a3data.com.br"
  }
}