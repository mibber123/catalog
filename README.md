# Django REST API Template

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Enabled-326CE5)
![Helm](https://img.shields.io/badge/Helm-Chart-0F1689)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-EF7B4D)
![License](https://img.shields.io/badge/License-MIT-blue)

A Django REST API template featuring a complete GitOps deployment pipeline using Docker, Kubernetes, Helm, ArgoCD and GitHub Actions.

---

## Features

- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Kubernetes
- Helm Chart
- ArgoCD GitOps deployment
- GitHub Actions CI/CD
- Semantic Release
- Automatic container publishing to GHCR
- Automatic image deployment through ArgoCD
- CRUD REST API
- Health endpoint
- Readiness & Liveness probes
- Automated database migrations
- Pytest test suite
- Makefile for common development tasks

---

## Architecture

```
Developer
     │
     ▼
 GitHub Repository
     │
 GitHub Actions
     │
 Build Docker Image
     │
 Push GHCR Image
     │
 Update Helm values.yaml
     │
     ▼
 Git Repository
     │
 ArgoCD watches repository
     │
     ▼
 Kubernetes Cluster
     │
 ├── PostgreSQL
 ├── Migration Job
 ├── Django Deployment
 ├── Service
 └── Ingress
```

---

## Repository Structure

```
.
├── api/
├── bookcatalog/
├── docs/
├── envs/
├── helm/
│   ├── app-chart/
│   ├── argo/
│   └── postgres/
├── .github/
├── Dockerfile
├── Makefile
└── README.md
```

---

## Quick Start

Clone the repository

```bash
git clone https://github.com/mibber123/catalog.git
cd catalog
```

Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run locally

```bash
python manage.py migrate
python manage.py runserver
```

---

## Development Commands

Run tests

```bash
make test
```

Verify repository

```bash
make verify
```

Helm validation

```bash
make helm-lint
```

Show available commands

```bash
make help
```

---

## Deployment

Deployment is fully automated.

1. Push changes to GitHub.
2. GitHub Actions builds and publishes a Docker image.
3. Semantic Release creates a version.
4. The production Helm values file is updated.
5. ArgoCD detects the Git change.
6. Kubernetes performs the deployment automatically.

---

## REST API

### Health

```
GET /api/
```

Returns

```json
{
    "status": "ok"
}
```

### Books

```
GET    /api/books/
POST   /api/books/
GET    /api/books/{id}/
PUT    /api/books/{id}/
DELETE /api/books/{id}/
```

---

## Documentation

Additional documentation can be found in the `docs/` directory.

- Architecture
- Deployment
- Development
- GitHub Actions
- Helm
- Troubleshooting

---

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Kubernetes
- Helm
- ArgoCD
- GitHub Actions
- GitHub Container Registry
- Semantic Release
- Pytest

---

## Author

- [ben](https://github.com/mibber123)
