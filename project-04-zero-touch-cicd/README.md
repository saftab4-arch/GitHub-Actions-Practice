# Project 04 – Zero-Touch CI/CD Platform

## Overview

This project implements a production-style CI/CD pipeline using Docker, GitHub Actions, Docker Hub, Docker Compose, and a self-hosted GitHub Actions runner.

The pipeline automatically tests, builds, pushes, and deploys a Flask application after successful validation.

---

## Architecture

```
Developer
    ↓
Git Push
    ↓
GitHub Actions CI
─────────────────────
Python Matrix Testing
(3.12 & 3.13)

Ruff Linting

Pytest

Artifact Upload

Docker Image Build

Push Image to Docker Hub
─────────────────────
    ↓
workflow_run
    ↓
GitHub Actions CD
─────────────────────
Self-Hosted Runner

Create .env

docker compose pull web

docker compose up -d

Verify Deployment
─────────────────────
    ↓
Flask Application
    ↓
PostgreSQL
    ↓
Redis
```

---

# Technologies Used

* Python Flask
* Gunicorn
* Docker
* Docker Compose
* PostgreSQL
* Redis
* GitHub Actions
* Docker Hub
* Self-Hosted Runner
* Pytest
* Ruff
* Linux

---

# Project Structure

```
project-04-zero-touch-cicd
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── __init__.py
│
├── tests/
│   └── test_app.py
│
├── scripts/
│   └── health-check.sh
│
├── docker-compose.yml
├── requirements-dev.txt
├── pytest.ini
├── .github/workflows/
│   ├── project04-ci.yml
│   └── project04-cd.yml
└── README.md
```

---

# CI Pipeline

## Trigger

* push
* workflow_dispatch

## Matrix Testing

* Python 3.12
* Python 3.13

## CI Stages

### Checkout Repository

Downloads source code.

### Install Dependencies

Installs application and development requirements.

### Ruff Linting

Checks code quality.

### Pytest

Runs automated tests.

### Artifact Upload

Uploads test reports.

### Build Docker Image

Creates Docker image.

### Push Image to Docker Hub

Publishes image for deployment.

---

# CD Pipeline

## Trigger

Automatic:

```
workflow_run:
  workflows: ["Project 04 CI"]
```

Manual:

```
workflow_dispatch
```

## Deployment Steps

### Create .env file

Creates environment variables from GitHub Secrets.

### Pull Latest Image

```
docker compose pull web
```

### Deploy Containers

```
docker compose up -d
```

### Verify Deployment

```
curl http://localhost:5000
```

---

# Docker Components

## Web Service

Flask + Gunicorn

## Database

PostgreSQL 16

## Cache

Redis

---

# Self Hosted Runner

The CD pipeline runs on a Linux self-hosted runner.

Runner startup:

```bash
cd ~/actions-runner
./run.sh
```

Output:

```
Connected to GitHub
Listening for Jobs
Running job: deploy
Job deploy completed with result: Succeeded
```

---

# Features

✅ Matrix Testing (3.12 & 3.13)

✅ Ruff Linting

✅ Pytest

✅ Artifact Upload

✅ Docker Build

✅ Docker Hub Push

✅ workflow_run Trigger

✅ Self-Hosted Runner

✅ Docker Compose Deployment

✅ PostgreSQL

✅ Redis

✅ Environment Variables from Secrets

✅ Automatic Continuous Deployment

---

# Future Enhancements

Project 05:

* Watchtower Zero-Touch Deployment
* Discord Notifications
* Nginx Reverse Proxy
* Gunicorn
* AWS ALB
* Cloudflare
* Redis
* RDS PostgreSQL
* Three-Tier Architecture
* Fully Automated Production Deployment
