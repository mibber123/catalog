# Book Catalog API

![Django CI](https://github.com/mibber123/catalog/actions/workflows/django.yml/badge.svg)

A RESTful Book Catalog API built with Django REST Framework as part of a cloud-native software development module.

## Features

- Django REST Framework API
- PostgreSQL support
- SQLite support for local development
- Docker & Docker Compose
- Kubernetes (k3d)
- GitHub Actions Continuous Integration

## Tech Stack

- Python 3.10
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- Kubernetes (k3d)
- GitHub Actions

## Getting Started

### Clone the repository

```bash
git clone git@github.com:mibber123/catalog.git
cd catalog
```

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/api/
```

## Running with Docker

Build the image:

```bash
docker compose build
```

Start the application:

```bash
docker compose up
```

## Running Tests

```bash
python manage.py test
```

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs Django tests
- Validates every push and pull request to `main`


## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/books/ | List all books |
| GET | /api/books/{id}/ | Get a single book |
| POST | /api/books/ | Create a book |
| PUT | /api/books/{id}/ | Update a book |
| DELETE | /api/books/{id}/ | Delete a book |


## Project Structure

catalog/
├── api/
├── bookcatalog/
├── .github/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py

catalog/
│
├── k8s/
│   ├── nginx-pod.yaml
│   ├── nginx-deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── ...


## Kubernetes Diagram

Internet
    │
    ▼
Ingress
    │
    ▼
Service (ClusterIP)
    │
    ▼
Deployment
    │
    ▼
Pod 1
Pod 2
Pod 3


Browser
     │
localhost:8081
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
     ▼
+---------+
| Pod #1  |
+---------+
+---------+
| Pod #2  |
+---------+
+---------+
| Pod #3  |
+---------+


## Author
Ben


## eventual

Portfolio

├── Cloud Native Demo
│   ├── Docker
│   ├── Kubernetes
│   ├── GitHub Actions
│   └── Helm
│
├── Data Engineering
│   ├── ETL Pipelines
│   ├── Airflow (later)
│   ├── Spark (later)
│   ├── SQL
│   └── Python
│
├── Tableau Dashboards
│
├── REST APIs
│
└── Python Projects