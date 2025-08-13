# Technical Design Document: CI/CD Pipeline for Simple Web App

## 1. Introduction

This document outlines the technical design for a continuous integration and continuous deployment (CI/CD) pipeline for a simple, single-page web application. The pipeline is triggered by a push to a GitHub repository and automates the build and deployment process.

## 2. Project Goal

The primary goal is to create a fully automated CI/CD pipeline that:
-   Provisions the necessary infrastructure using Terraform.
-   Builds a containerized version of the application upon code changes.
-   Pushes the container image to a secure artifact repository.
-   Deploys the new version of the application to a serverless environment.

## 3. Architecture

The architecture is designed for simplicity and automation:

-   **Version Control**: GitHub is the source code repository.
-   **CI/CD**: Google Cloud Build is used to create a build pipeline that is triggered by a push to the GitHub repository.
-   **Infrastructure as Code**: Terraform is used for the one-time setup of the Google Cloud resources.
-   **Artifact Management**: Google Artifact Registry stores the Docker container images.
-   **Compute Platform**: Google Cloud Run runs the containerized application in a serverless environment.
-   **Application**: A Python Flask application serves a single `index.html` file with inline CSS and JavaScript.

## 4. Technologies Used

-   **Cloud Provider**: Google Cloud Platform (GCP)
-   **IaC**: Terraform
-   **CI/CD**: Google Cloud Build
-   **Containerization**: Docker
-   **Application**: Python 3, Flask, HTML5
-   **Version Control**: GitHub