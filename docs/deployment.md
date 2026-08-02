# Deployment

## Deployment Workflow

The project follows a GitOps deployment strategy.

```
Git Commit
      │
      ▼
GitHub Actions
      │
      ▼
Docker Image Build
      │
      ▼
Publish Image (GHCR)
      │
      ▼
Update values.yaml
      │
      ▼
Git Commit
      │
      ▼
ArgoCD detects change
      │
      ▼
Helm Upgrade
      │
      ▼
Migration Job
      │
      ▼
Rolling Deployment
```

## Kubernetes Resources

The Helm chart deploys:

- Deployment
- Service
- Ingress
- ConfigMap
- Migration Job

The PostgreSQL database is deployed using the Bitnami PostgreSQL Helm chart.

## Health Checks

The deployment includes:

- Readiness Probe
- Liveness Probe

These ensure traffic is only routed to healthy application instances.

## Automatic Migrations

Before each deployment a Kubernetes Job executes:

```
python manage.py migrate
```

This ensures the database schema is updated before new application pods become available.
