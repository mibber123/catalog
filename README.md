# Book Catalog API

![Django CI](https://github.com/mibber123/catalog/actions/workflows/django.yml/badge.svg)

A cloud-native REST API built with **Django REST Framework**, demonstrating a modern GitOps deployment pipeline using Docker, Kubernetes, Helm, ArgoCD and GitHub Actions.

---

# Features

- RESTful API built with Django REST Framework
- PostgreSQL database
- SQLite support for local development
- Docker containerisation
- Helm chart deployment
- ArgoCD GitOps continuous deployment
- GitHub Actions CI/CD pipeline
- Semantic Release automated versioning
- GitHub Container Registry (GHCR)

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Application |
| Django 5 | Web Framework |
| Django REST Framework | REST API |
| PostgreSQL | Production Database |
| SQLite | Local Development |
| Docker | Containerisation |
| Kubernetes (k3d) | Container Orchestration |
| Helm | Kubernetes Package Management |
| ArgoCD | GitOps Deployment |
| GitHub Actions | Continuous Integration / Deployment |
| GHCR | Container Registry |

---

# Project Structure

```
catalog/
│
├── api/                     # Django REST API
├── bookcatalog/             # Django project configuration
│
├── helm/
│   ├── argo/                # ArgoCD configuration
│   ├── catalog-chart/       # Helm chart
│   └── postgres/            # PostgreSQL values
│
├── envs/
│   └── prod/
│       └── values.yaml      # Production deployment values
│
├── .github/
│   ├── actions/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── manage.py
└── README.md
```

---

# Local Development

Clone the repository

```bash
git clone git@github.com:mibber123/catalog.git
cd catalog
```

Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply database migrations

```bash
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

Application URL

```
http://127.0.0.1:8000/api/
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# Testing

Run the Django test suite

```bash
python manage.py test
```

or

```bash
pytest
```

---

# CI/CD Pipeline

GitHub Actions automatically performs the following:

- Installs project dependencies
- Runs automated tests
- Checks database migrations
- Creates Semantic Releases
- Builds Docker images
- Pushes images to GitHub Container Registry
- Updates the production Helm values
- Triggers automatic deployment through ArgoCD

---

# GitOps Deployment Flow

```
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ├── Tests
    ├── Migration Checks
    ├── Semantic Release
    ├── Build Docker Image
    ├── Push Image to GHCR
    └── Update envs/prod/values.yaml
                │
                ▼
             GitHub
                │
                ▼
             ArgoCD
                │
                ▼
          Helm Chart Sync
                │
                ▼
      PreSync Migration Job
                │
                ▼
      Kubernetes Deployment
                │
                ▼
          Running Application
```

---

# Kubernetes Architecture

```
                Internet
                    │
                    ▼
               Ingress
                    │
                    ▼
           ClusterIP Service
                    │
                    ▼
              Deployment
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Pod 1       Pod 2       Pod 3
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/books/` | List books |
| GET | `/api/books/{id}/` | Retrieve a book |
| POST | `/api/books/` | Create a book |
| PUT | `/api/books/{id}/` | Update a book |
| DELETE | `/api/books/{id}/` | Delete a book |

---

# Future Improvements

- Health monitoring
- Metrics and observability
- Horizontal Pod Autoscaling
- Resource requests and limits
- Multiple deployment environments
- TLS and HTTPS
- Production secrets management
- Helm chart reuse across projects

---

# Author

Ben
