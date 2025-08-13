I want to create a full CI/CD pipeline for a "Hello World" web app, triggered by a push to my GitHub repository. Use the variables from my open .env file to generate all necessary files and setup commands.

**Important Guidelines:**
*   The `.env` file contains secrets and should NOT be checked into the Git repository.
*   The Git remote URL is specified in the `.env` file.

1.  **Project Documentation:**
    *   Generate a `DESIGN.md` and a user-friendly `README.md`.

2.  **Infrastructure as Code (IaC):**
    *   Generate a `main.tf` script to provision the Artifact Registry repo and the Cloud Run service.
    *   **Note:** For the initial deployment, use the placeholder image `gcr.io/cloudrun/placeholder` in the `google_cloud_run_v2_service` resource.
    *   Provide and execute the `terraform` commands.

3.  **Application Code & Tests:**
    *   Generate the Python code (`main.py`) and dependencies (`requirements.txt`).
    *   **Note on dependencies:** For a more robust build, pin all dependency versions in `requirements.txt`. After installing the necessary packages in a local virtual environment, you can generate a complete and pinned list of dependencies using the command `pip freeze > requirements.txt`.
    *   Create a `Dockerfile` to containerize the app.
    *   Generate a `pytest` unit test (`test_main.py`).

4.  **Git Setup:**
    *   Create a `.gitignore` file that includes `.env`, `*.tfstate*`, and the `.terraform` directory.

5.  **Continuous Deployment Pipeline:**
    *   Generate a `cloudbuild.yaml` file. This file should define the automated steps to build the Docker image, push it to Artifact Registry, and deploy the new version to the Cloud Run service.
    *   **Note:** In the `cloudbuild.yaml` file, configure the build options to use `CLOUD_LOGGING_ONLY` for logging.

6.  **Verification:**
    *   After the pipeline runs, what `gcloud` command can I use to stream the logs from the Cloud Run service to verify the deployment?