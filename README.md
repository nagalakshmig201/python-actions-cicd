# Python Actions CI/CD

A small FastAPI service used to practice GitHub Actions and Docker.

## Step 1: Run and test the app locally

Prerequisites: Python 3.12+ and Docker Desktop.

From PowerShell in this project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/health` and confirm the response is `{"status":"ok"}`.
Use `Ctrl+C` to stop the local server.

## Step 2: Build and run the container

```powershell
docker build -t python-actions-cicd:local .
docker run --rm -p 8000:8000 python-actions-cicd:local
```

In another terminal, open `http://127.0.0.1:8000/health`. Stop the container
with `Ctrl+C`.

## Step 3: GitHub Actions CI and GHCR publishing

The workflow in `.github/workflows/ci.yml` runs tests on pull requests, pushes
to `main`, and manual runs. On a push to `main`, it also builds the Docker image
and publishes `latest`, `main`, and commit-SHA tags to GitHub Container Registry
(GHCR). It uses the repository-provided `GITHUB_TOKEN`; no personal access token
or repository secret is needed. The workflow grants package-write permission
only to the publish job.

After pushing this repository to GitHub, open its **Actions** tab to follow the
test and publish jobs. The published image will be at
`ghcr.io/<owner>/python-actions-cicd`; package visibility can be changed in the
package settings if you want to share it publicly.
