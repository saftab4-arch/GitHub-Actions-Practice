# Project 02 – Advanced Docker CI/CD Pipeline

End-to-end CI/CD pipeline for a Flask application using **Docker, Docker Compose, PostgreSQL, GitHub Actions, and Docker Hub**. A single code push automatically lints, tests, builds, and publishes a container image that can be pulled and run anywhere.

---

## Architecture

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
   Lint  (ruff)
      │
      ▼
  Pytest
      │
      ▼
 Docker Build
      │
      ▼
Push Image → Docker Hub
      │
      ▼
  docker pull
      │
      ▼
Run Container Anywhere
```

---

## Project Structure

```text
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
```

---

## Build Steps

### Step 1 – Build the Flask Application

Created `app/app.py` — a simple Flask application:

```python
@app.route("/")
def home():
    return "Project 02 Advanced CI/CD"
```

### Step 2 – Create the Dockerfile

Built a container image for the Flask application:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/app.py"]
```

### Step 3 – Run the Container

```bash
docker build -t flask-cicd .
docker run -d -p 5000:5000 flask-cicd
```

Verified at: `http://localhost:5000`

### Step 4 – Add PostgreSQL with Docker Compose

Created `docker-compose.yml` with two services:

- **Flask App**
- **PostgreSQL**

Features: named volume, custom network, environment variables, health checks, and restart policies.

```bash
docker compose up -d
docker compose ps   # verify
```

### Step 5 – Create the GitHub Actions Workflow

Created `.github/workflows/cicd.yml` with a three-stage pipeline:

```text
lint → test → build
```

### Step 6 – Lint Job

```yaml
- uses: actions/setup-python@v5

# install dependencies
pip install -r requirements.txt
pip install ruff

# run
ruff check .
```

### Step 7 – Test Job

Runs after lint succeeds (`needs: lint`):

```yaml
needs: lint

# install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# run
python -m pytest
```

### Step 8 – Build Job

Runs after tests (`needs: test`):

```yaml
needs: test
```

Uses `docker/setup-buildx-action`, logs into Docker Hub with `docker/login-action`, and builds/pushes with `docker/build-push-action`.

GitHub Secrets used:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Resulting image:

```text
syedaftab04/project-02:v1
```

### Step 9 – GitHub Actions Pipeline

Successful pipeline:

| Stage | Status |
|-------|--------|
| Lint  | ✅ |
| Test  | ✅ |
| Build | ✅ |

GitHub Actions automatically pulls the code, runs lint checks, executes tests, builds the Docker image, and pushes it to Docker Hub.

### Step 10 – Deploy Anywhere

```bash
docker pull syedaftab04/project-02:v1
docker run -d -p 7000:5000 --name project02 syedaftab04/project-02:v1
```

Open `http://localhost:7000` → Output: **Project 02 Advanced CI/CD**

**Docker Hub:** repository `syedaftab04/project-02`, tag `v1`

---

## Technologies Used

| Category | Tools |
|----------|-------|
| Language / Framework | Python, Flask |
| Testing | pytest |
| Containers | Docker, Dockerfile, Buildx, Docker Hub |
| Orchestration | Docker Compose, Networks, Volumes, Healthchecks |
| Database | PostgreSQL |
| CI/CD | GitHub Actions (multi-job workflow), Secrets, Lint → Test → Build → Deploy |

---

## Troubleshooting

Issues hit during the build and how they were fixed:

| # | Issue | Root Cause | Fix |
|---|-------|-----------|-----|
| 1 | **YAML indentation error** — `Invalid workflow file: Unexpected value "python-version"` | Bad indentation under `with:` | Corrected indentation: `with:` → `python-version: "3.12"` |
| 2 | **Wrong repository** — pushed into `docker-labs.git` instead of `GitHub-Actions-Practice.git` | Wrong remote origin | `git remote remove origin` then `git remote add origin git@github.com:saftab4-arch/GitHub-Actions-Practice.git` |
| 3 | **venv accidentally committed** — thousands of files pushed | `venv/` not ignored | Added `venv/`, `__pycache__/`, `.env` to `.gitignore`; `git rm -r --cached venv` |
| 4 | **Project files at repo root** | Files created outside intended folder | Moved everything into `project-02-advanced-cicd/`; updated `context:` / `file:` paths |
| 5 | **`requirements.txt` not found** — `No such file or directory` | Workflow used wrong path | `pip install -r project-02-advanced-cicd/requirements.txt` |
| 6 | **pytest not found** — `No module named pytest` | Dev deps not installed | `pip install -r requirements-dev.txt` |
| 7 | **`ModuleNotFoundError: app`** | pytest run from wrong directory | `cd project-02-advanced-cicd && python -m pytest tests` |

### Fix detail — YAML indentation

```yaml
with:
  python-version: "3.12"
```

### Fix detail — `.gitignore`

```gitignore
venv/
__pycache__/
.env
```

```bash
git rm -r --cached venv
```

---

## Final Result

- ✅ Flask application
- ✅ PostgreSQL container
- ✅ Docker Compose networking
- ✅ Volumes and healthchecks
- ✅ GitHub Actions pipeline
- ✅ Docker Hub image publishing
- ✅ Deployment from Docker Hub
- ✅ Fully automated CI/CD workflow

A code push now automatically performs:

```text
Push → Lint → Tests → Build Docker Image → Push to Docker Hub → Pull and Run Anywhere
```

**Project 02 – Advanced CI/CD : COMPLETE** ✅
