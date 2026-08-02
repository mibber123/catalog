# Architecture

## Overview

This project follows a GitOps deployment model using Kubernetes, Helm, ArgoCD and GitHub Actions.

The application consists of a Django REST API backed by a PostgreSQL database. Container images are built automatically through GitHub Actions and deployed using ArgoCD whenever changes are detected in the repository.

## High-Level Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Run Tests
    ├── Build Docker Image
    ├── Push Image to GHCR
    ├── Create Semantic Release
    └── Update Helm values.yaml
              │
              ▼
Git Repository
              │
              ▼
ArgoCD
              │
              ▼
Kubernetes Cluster
              │
      ┌───────┴────────┐
      │                │
 PostgreSQL      Django API
      │                │
      └──────┬─────────┘
             │
        Kubernetes Service
             │
          Ingress
             │
          REST Clients
```

## Components

### Django REST API

Provides REST endpoints for the application and business logic.

### PostgreSQL

Stores persistent application data.

### Helm

Packages the Kubernetes manifests into a reusable deployment chart.

### ArgoCD

Continuously monitors the Git repository and synchronises the Kubernetes cluster with the desired state.

### GitHub Actions

Provides Continuous Integration and Continuous Deployment by:

- Running tests
- Building Docker images
- Publishing images to GitHub Container Registry
- Creating Semantic Releases
- Updating deployment configuration

## Repository Layout

```
api/
bookcatalog/
docs/
envs/
helm/
.github/
```
