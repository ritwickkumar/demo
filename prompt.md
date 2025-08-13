I want to create a full CI/CD pipeline for a "Hello World" web app, triggered by a push to my GitHub repository. Use the variables from my open .env file to generate all necessary files and setup commands.

1.  **Project Documentation:**
    * Generate a `DESIGN.md` and a user-friendly `README.md`.

2.  **Infrastructure as Code (IaC):**
    * Generate a `main.tf` script to provision the Artifact Registry repo and the Cloud Run service.
    * Provide and execute the `terraform` commands..

3.  **Application Code & Tests:**
    * Generate the Python code (`main.py`) and dependencies (`requirements.txt`).
    * Create a `Dockerfile` to containerize the app.
    * Generate a `pytest` unit test (`test_main.py`).

4.  **Continuous Deployment Pipeline:**
    * **Generate a `cloudbuild.yaml` file.** This file should define the automated steps to build the Docker image, push it to Artifact Registry, and deploy the new version to the Cloud Run service created by Terraform.

5.  **Verification:**
    * After the pipeline runs, what `gcloud` command can I use to stream the logs from the Cloud Run service to verify the deployment?