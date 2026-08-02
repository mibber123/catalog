# GitHub Actions

## Overview

GitHub Actions automates testing, container builds and deployments.

The workflow is triggered whenever changes are pushed to the repository.

## Pipeline

```
Push
 │
 ▼
Run Tests
 │
 ▼
Build Docker Image
 │
 ▼
Publish to GHCR
 │
 ▼
Semantic Release
 │
 ▼
Update Helm values
 │
 ▼
Commit values.yaml
```

## Semantic Release

Semantic Release automatically:

- Calculates the next version
- Creates Git tags
- Generates GitHub Releases
- Updates the CHANGELOG

Commit messages follow Conventional Commits.

Examples:

```
feat:
fix:
refactor:
docs:
chore:
```

## Automatic Deployment

Once the production values file has been updated, ArgoCD detects the Git change and deploys the new version automatically.
