# Troubleshooting

## Helm

Validate templates.

```
make helm-lint
```

Render manifests.

```
helm template app ./helm/app-chart
```

## Kubernetes

Display resources.

```
kubectl get all
```

View logs.

```
kubectl logs deployment/app
```

Describe a resource.

```
kubectl describe deployment app
```

## ArgoCD

Port-forward the dashboard.

```
make argocd
```

Retrieve the initial password.

```
kubectl -n argocd get secret argocd-initial-admin-secret \
-o jsonpath="{.data.password}" | base64 -d
```

## Common Issues

### Image not updating

Verify:

- GitHub Action completed successfully.
- The production values file contains the new image tag.
- ArgoCD has synchronised successfully.

### Pods stuck in Pending

Check:

```
kubectl describe pod <pod-name>
```

### Migration Job failing

Inspect the logs.

```
kubectl logs job/app-migrate
```

### Helm template errors

Render the templates.

```
helm template app ./helm/app-chart
```

This usually identifies invalid template syntax before deployment.

### Health probe failures

Verify the endpoint responds successfully.

```
GET /api/
```

A successful response should return:

```json
{
    "status": "ok"
}
```
