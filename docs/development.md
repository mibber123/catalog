# Development

## Requirements

- Python 3.10+
- Docker Desktop
- Kubernetes
- Helm
- kubectl
- Git

## Local Setup

Clone the repository.

```
git clone <repository>
cd catalog
```

Create a virtual environment.

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies.

```
pip install -r requirements.txt
```

Apply migrations.

```
python manage.py migrate
```

Run the development server.

```
python manage.py runserver
```

## Testing

Execute the test suite.

```
make test
```

## Repository Verification

Run all repository validation checks.

```
make verify
```

This performs:

- Helm lint
- Pytest execution

## Useful Commands

| Command | Description |
|----------|-------------|
| make help | Show available commands |
| make verify | Run repository checks |
| make test | Execute tests |
| make helm-lint | Validate Helm chart |
| make status | Display Kubernetes resources |
| make argocd | Port-forward ArgoCD |
