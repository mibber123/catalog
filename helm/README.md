# Helm Charts

This directory contains all Helm-related resources used to deploy the application and supporting infrastructure to Kubernetes.

## Structure

```
helm/
├── README.md
├── catalog-chart/
└── argo/
```

### catalog-chart/

Contains the custom Helm chart for the Django application.

Resources include:

- Deployment
- Service
- ConfigMap
- Ingress
- Migration Job (Helm Hooks)
- Supporting templates

This chart is deployed by ArgoCD and is configured using the environment-specific values files located under `envs/`.

---

### argo/

Contains configuration values used to deploy ArgoCD itself using the official Argo Helm Chart.

The chart is **not** stored in this repository; only the custom configuration (`values.yaml`) is maintained here.

Example installation:

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

kubectl create namespace argocd

helm install argocd argo/argo-cd \
    -n argocd \
    -f ./helm/argo/values.yaml
```

## Notes

- Application-specific configuration should be placed in the appropriate environment values file under `envs/`.
- Third-party Helm charts should not be copied into this repository unless custom modifications are required.
