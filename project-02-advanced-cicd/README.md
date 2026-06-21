Project 02 – Advanced Docker CI/CD Pipeline

End-to-end CI/CD pipeline for a Flask application using Docker, Docker Compose, PostgreSQL, GitHub Actions, and Docker Hub.

Architecture
Developer Push
      ↓
GitHub Actions
      ↓
Lint
      ↓
Pytest
      ↓
Docker Build
      ↓
Push Image to Docker Hub
      ↓
docker pull
      ↓
Run Container Anywhere
Project Structure
project-02-advanced-cicd/
├── app/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .dockerignore
├── .gitignore
└── .github/
    └── workflows/
        └── cicd.yml
Step 1 – Build Flask Application

Created:

app/app.py

Simple Flask application:

@app.route("/")
def home():
    return "Project 02 Advanced CI/CD"
Step 2 – Create Dockerfile

Built a container image for the Flask application.

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python","app/app.py"]
Step 3 – Run Container
docker build -t flask-cicd .

docker run -d -p 5000:5000 flask-cicd

Verified:

http://localhost:5000
Step 4 – Add PostgreSQL with Docker Compose

Created:

docker-compose.yml

Services:

Flask App
PostgreSQL

Features:

Named volume
Custom network
Environment variables
Health checks
Restart policies

Started stack:

docker compose up -d

Verified:

docker compose ps
Step 5 – Create GitHub Actions Workflow

Created:

.github/workflows/cicd.yml

Pipeline:

lint
 ↓
test
 ↓
build
Step 6 – Lint Job

Setup Python:

uses: actions/setup-python@v5

Install dependencies:

pip install -r requirements.txt
pip install ruff

Run:

ruff check .
Step 7 – Test Job

Runs after lint succeeds:

needs: lint

Install dependencies:

pip install -r requirements.txt
pip install -r requirements-dev.txt

Run pytest:

python -m pytest
Step 8 – Build Job

Runs after tests:

needs: test

Uses:

docker/setup-buildx-action

Login to Docker Hub:

docker/login-action

Using GitHub Secrets:

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN

Build and push image:

docker/build-push-action

Image:

syedaftab04/project-02:v1
Step 9 – GitHub Actions Pipeline

Successful pipeline:

Lint ✅

Test ✅

Build ✅

GitHub Actions automatically:

Pulls code
Runs lint checks
Executes tests
Builds Docker image
Pushes image to Docker Hub
Step 10 – Deploy Anywhere

Pull image:

docker pull syedaftab04/project-02:v1

Run container:

docker run -d -p 7000:5000 --name project02 syedaftab04/project-02:v1

Open:

http://localhost:7000

Output:

Project 02 Advanced CI/CD
Docker Hub

Repository:

syedaftab04/project-02

Tag:

v1
Technologies Used
Python
Flask
pytest
Docker
Dockerfile
Buildx
Docker Hub
Docker Compose
Networks
Volumes
Healthchecks
PostgreSQL
GitHub Actions
Multi-job workflow
Secrets
Build pipeline
CI/CD
Lint
Test
Build
Deploy
Troubleshooting
YAML Indentation Errors

Issue:

Invalid workflow file
Unexpected value "python-version"

Solution:

Fixed YAML indentation inside:

with:
  python-version: "3.12"
Wrong Repository

Issue:

Project pushed into:

docker-labs.git

Wanted:

GitHub-Actions-Practice.git

Solution:

Updated remote:

git remote remove origin

git remote add origin git@github.com:saftab4-arch/GitHub-Actions-Practice.git
venv Accidentally Committed

Issue:

Thousands of files pushed.

Solution:

Added:

venv/
__pycache__/
.env

Removed cached files:

git rm -r --cached venv
Project Files Appeared at Repository Root

Issue:

Files were outside the intended folder.

Solution:

Moved everything into:

project-02-advanced-cicd/

Updated paths inside:

context:
file:
requirements.txt
pytest
requirements.txt Not Found

Error:

No such file or directory: requirements.txt

Solution:

Updated workflow:

pip install -r project-02-advanced-cicd/requirements.txt
pytest Not Found

Error:

No module named pytest

Solution:

Installed development dependencies:

pip install -r requirements-dev.txt
ModuleNotFoundError: app

Error:

No module named app

Solution:

Executed pytest from project directory:

cd project-02-advanced-cicd

python -m pytest tests
Final Result

✅ Flask application

✅ PostgreSQL container

✅ Docker Compose networking

✅ Volumes and healthchecks

✅ GitHub Actions pipeline

✅ Docker Hub image publishing

✅ Deployment from Docker Hub

✅ Fully automated CI/CD workflow

Result

A code push now automatically performs:

Push
 ↓
Lint
 ↓
Tests
 ↓
Build Docker Image
 ↓
Push to Docker Hub
 ↓
Pull and Run Anywhere

Project 02 – Advanced CI/CD : COMPLETE
