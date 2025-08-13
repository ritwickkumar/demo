terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
}

provider "google" {
  project = "aqueous-nebula-426105-i3"
  region  = "us-central1"
}

resource "google_artifact_registry_repository" "repo" {
  location      = "us-central1"
  repository_id = "demo-repo"
  format        = "DOCKER"
}

resource "google_cloud_run_v2_service" "default" {
  name     = "hello-world-demo"
  location = "us-central1"

  template {
    containers {
      image = "gcr.io/cloudrun/placeholder"
    }
  }
}
