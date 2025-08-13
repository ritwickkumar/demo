I want to create a full CI/CD pipeline for a simple, single-page web app, triggered by a push to my GitHub repository. Use the variables from my open .env file to generate all necessary files and setup commands.

**Important Guidelines:**
*   The `.env` file contains secrets and should NOT be checked into the Git repository.
*   The Git remote URL is specified in the `.env` file.

**Application Architecture:**
The application will be a single-page application (SPA) with the following structure:
*   **Frontend:** A single `index.html` file with inline CSS and JavaScript.
*   **Backend:** A Python Flask application that will serve the `index.html` file.

---

### 1. Application Code

*   Please generate a single `index.html` file.
*   The page should have a clean and modern layout with:
    *   A main header with a title like "My Awesome App".
    *   A short, engaging paragraph of text below the header.
    *   A section displaying three feature cards arranged in a row. Each card should have a simple icon, a feature title, and a brief description.
*   Generate a Python Flask application (`main.py`) that serves the `index.html` file.
*   Generate a `requirements.txt` file with the necessary Python dependencies (e.g., Flask). Pin the dependency versions.

### 2. Project Documentation

*   Generate a `DESIGN.md` and a user-friendly `README.md` that reflect the new, simplified architecture.

### 3. Infrastructure as Code (IaC)

*   Generate a `main.tf` script to provision the Artifact Registry repo and the Cloud Run service.
*   **Note:** For the initial deployment, use the placeholder image `gcr.io/cloudrun/placeholder` in the `google_cloud_run_v2_service` resource.
*   Provide and execute the `terraform` commands.

### 4. Containerization

*   Create a `Dockerfile` that creates a production-ready container. This should be a simple Dockerfile that uses a Python image, copies the application code (`main.py`, `requirements.txt`, `index.html`), installs the Python dependencies, and defines the `CMD` to run the Flask application.

### 5. Git Setup

*   Create a `.gitignore` file that includes `.env`, `*.tfstate*`, and the `.terraform` directory.

### 6. Continuous Deployment Pipeline

*   Generate a `cloudbuild.yaml` file. This file should define the automated steps to:
    1.  Build the Docker image.
    2.  Push the Docker image to Artifact Registry.
    3.  Deploy the new version to the Cloud Run service.
*   **Note:** In the `cloudbuild.yaml` file, configure the build options to use `CLOUD_LOGGING_ONLY` for logging.

### 7. Verification

*   After the pipeline runs, what `gcloud` command can I use to stream the logs from the Cloud Run service to verify the deployment?