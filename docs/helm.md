# Helm

## Overview

The application is deployed using a reusable Helm chart.

```
helm/
├── app-chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates
```

## Templates

The chart deploys:

- Deployment
- Service
- ConfigMap
- Ingress
- Migration Job

## Helper Templates

Common resource names are generated through helper templates.

Examples include:

- app.fullname
- app.image
- app.configMapName
- app.databaseSecretName
- app.migrationJobName

Using helpers removes duplicated logic and simplifies maintenance.

## Validation

Validate the chart.

```
make helm-lint
```

Render manifests.

```
helm template app ./helm/app-chart
```

## Configuration

Application settings are configured through `values.yaml`.

This includes:

- replica count
- image repository
- image tag
- resource limits
- image pull secrets
- database secret
