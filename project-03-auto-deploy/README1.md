# Project 03 – Advanced CI/CD Pipeline with GitHub Actions, Docker & Self-Hosted Runner

## Overview

This project demonstrates a production-style CI/CD pipeline for a Python Flask application using:

* Docker
* Docker Compose
* GitHub Actions
* Matrix testing
* Ruff linting
* Pytest
* Docker Hub
* Self-hosted GitHub runner
* Continuous Deployment

---

# Architecture

```
Git Push
    ↓
GitHub Actions CI
(Test → Lint → Build)
    ↓
Docker Hub
    ↓
GitHub Actions CD
(Self-hosted Runner)
    ↓
docker compose pull
docker compose up -d
    ↓
Flask Application + PostgreSQL
```

---

# Technologies Used

* Python
* Flask
* PostgreSQL
* Docker
* Docker Compose
* GitHub Actions
* Docker Hub
* Ruff
* Pytest
* Self-hosted Runner

---

# Project Structure

```
project-03-auto-deploy/

├── app/
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
│
└── .github/workflows
    ├── project03-ci.yml
    └── project03-cd.yml
```

---

# Application Containers

## Flask App

* Port 5000
* Runs inside Docker
* Uses non-root user

## PostgreSQL

* PostgreSQL 17
* Persistent volume
* Health checks enabled

---

# Docker Security

Created non-root user:

```dockerfile
RUN useradd -m appuser

USER appuser
```

This avoids running the container as root.

---

# CI Pipeline

## Matrix Testing

Python versions:

* 3.12
* 3.13

Both versions are tested automatically.

---

## Install Dependencies

```yaml
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## Ruff Linting

```yaml
ruff check .
```

Checks code quality.

---

## Unit Tests

```yaml
pytest
```

Tests application functionality.

---

## Test Report Generation

```yaml
pytest --junitxml=report.xml
```

Generates XML reports.

---

## Upload Artifacts

```yaml
actions/upload-artifact@v4
```

Stores test reports inside GitHub Actions.

---

## Docker Build

Image created:

```
syedaftab04/project03-auto-deploy:latest
```

Image pushed to Docker Hub automatically.

---

# CD Pipeline

Triggered after CI success.

Uses:

```yaml
workflow_run
```

Runs only when:

```
Project 03 CI = success
```

Deploys using a self-hosted runner.

---

# Self-Hosted Runner

Installed locally:

```
actions-runner/
```

Configured with:

```bash
./config.sh
```

Started using:

```bash
./run.sh
```

Runner listens for deployment jobs.

---

# Deployment Commands

```bash
cd /home/syedaftab04/cicd-new-project/project-03-auto-deploy

docker compose pull

docker compose up -d
```

Updates containers with latest image.

---

# Running Containers

```bash
docker ps
```

Expected:

```
flask-app
postgres-db
```

---

# View Logs

Application:

```bash
docker logs flask-app
```

Compose logs:

```bash
docker compose logs
```

Live logs:

```bash
docker compose logs -f
```

---

# Troubleshooting

## YAML Errors

Cause:

Incorrect indentation.

Fix:

Verify spacing and syntax.

---

## Requirements Not Found

Cause:

Wrong working directory.

Fix:

```yaml
defaults:
  run:
    working-directory: project-03-auto-deploy
```

---

## Self-hosted Runner Cannot Find Repository

Cause:

Repository not checked out.

Fix:

```yaml
- uses: actions/checkout@v4
```

---

## CD Fails

Cause:

Wrong project path.

Fix:

```bash
cd /home/syedaftab04/cicd-new-project/project-03-auto-deploy
```

---

## Docker Hub Login Issues

Verify secrets:

* DOCKER_USERNAME
* DOCKER_PASSWORD

---

# Skills Practiced

✅ Docker

✅ Docker Compose

✅ Matrix Testing

✅ Ruff

✅ Pytest

✅ GitHub Actions

✅ Artifacts

✅ Docker Hub

✅ Self-hosted Runners

✅ Continuous Deployment

✅ CI/CD Architecture

---

# Final Pipeline

```
Git Push
     ↓
Project 03 CI
     ↓
Matrix Tests
     ↓
Lint
     ↓
Pytest
     ↓
Build Docker Image
     ↓
Push to Docker Hub
     ↓
Project 03 CD
     ↓
Self-hosted Runner
     ↓
docker compose pull
     ↓
docker compose up -d
     ↓
Flask App + PostgreSQL
```

---

# Next Project

Project 04 – Zero-Touch Deployment with Watchtower & Discord Notifications

Git Push

↓

Build Image

↓

Push to Docker Hub

↓

Watchtower Detects New Image

↓

Automatic Container Update

↓

Discord Notification
