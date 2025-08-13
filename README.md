# Hello World CI/CD Pipeline

This project implements a full CI/CD pipeline for a "Hello World" web application using Google Cloud, Terraform, and GitHub.

## Overview

When code is pushed to the GitHub repository, a Google Cloud Build trigger is activated. This trigger executes the steps defined in `cloudbuild.yaml` to:
1.  Build the Docker image for the Python application.
2.  Push the image to Google Artifact Registry.
3.  Deploy the new image to the Google Cloud Run service.

## Prerequisites

-   A Google Cloud Platform project.
-   A GitHub repository for your application code.
-   `gcloud` CLI installed and authenticated.
-   `terraform` CLI installed.

## One-Time Setup

1.  **Provision Infrastructure**: Run the provided Terraform commands to create the Artifact Registry repository and the Cloud Run service.
2.  **Connect GitHub Repository**: In the Google Cloud Console, go to Cloud Build > Triggers and connect your GitHub repository.
3.  **Create a Trigger**: Create a push trigger that points to the `cloudbuild.yaml` file in your repository.

After this one-time setup, any push to your repository will automatically trigger a new build and deployment.
