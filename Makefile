.DEFAULT_GOAL := help

PROJECT := catalog
RELEASE := app
CHART := ./helm/app-chart
NAMESPACE := default
ARGO_URL := http://localhost:8081/argocd

GREEN := \033[0;32m
BLUE := \033[0;34m
RESET := \033[0m

# =============================================================================
# Workflow
# =============================================================================

env:
	cd ~/projects/catalog \source .venv/bin/activate

verify:
	@printf "$(BLUE)Running repository verification...$(RESET)\n"
	@$(MAKE) --no-print-directory helm-lint
	@$(MAKE) --no-print-directory helm-render
	@$(MAKE) --no-print-directory test
	@printf "$(GREEN)Repository verification complete.$(RESET)\n"

start:
	k3d cluster start mycluster

status:
	kubectl get pods
	kubectl get svc
	kubectl get ingress

cred:
	kubectl -n argocd get secret argocd-initial-admin-secret \-o jsonpath="{.data.password}" | base64 -d

argocd:
	kubectl -n argocd port-forward svc/argocd-server 8082:443

argo:
	argocd:
	@echo "ArgoCD UI: http://localhost:8081/argocd"

stop:
	k3d cluster stop mycluster

# =============================================================================
# Django
# =============================================================================

run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

test:
	python -m pytest

shell:
	python manage.py shell

createsuperuser:
	python manage.py createsuperuser

# =============================================================================
# Helm
# =============================================================================

helm-lint:
	helm lint $(CHART)

helm-template:
	helm template $(RELEASE) $(CHART)

helm-render:
	@helm template $(RELEASE) $(CHART) > /dev/null

helm-install:
	helm install $(RELEASE) $(CHART) -n $(NAMESPACE)

helm-upgrade:
	helm upgrade $(RELEASE) $(CHART) -n $(NAMESPACE)

helm-uninstall:
	helm uninstall $(RELEASE) -n $(NAMESPACE)

# =============================================================================
# Kubernetes
# =============================================================================

pods:
	kubectl get pods

pods-watch:
	kubectl get pods -w

services:
	kubectl get services

ingress:
	kubectl get ingress

jobs:
	kubectl get jobs

# =============================================================================
# ArgoCD
# =============================================================================

argocd:
	kubectl port-forward svc/argocd-server -n argocd 8081:443

sync:
	kubectl rollout restart deployment/$(PROJECT)

logs:
	kubectl logs -f deployment/$(PROJECT)

# =============================================================================
# Utility
# =============================================================================

check: helm-lint test
	@echo ""
	@echo "All checks passed."





tree:
	tree -a -I '.git|.venv|__pycache__|.pytest_cache'

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

help:
	@printf "\n"
	@printf "=========================================\n"
	@printf "         Django Deployment Toolkit\n"
	@printf "=========================================\n\n"

	@printf "Django\n"
	@printf "  make run\n"
	@printf "  make migrate\n"
	@printf "  make makemigrations\n"
	@printf "  make test\n"
	@printf "  make shell\n"
	@printf "  make createsuperuser\n\n"

	@printf "Docker\n"
	@printf "  make docker-build\n"
	@printf "  make docker-up\n"
	@printf "  make docker-down\n\n"

	@printf "Helm\n"
	@printf "  make helm-lint\n"
	@printf "  make helm-template\n\n"

	@printf "Kubernetes\n"
	@printf "  make pods\n"
	@printf "  make pods-watch\n"
	@printf "  make services\n"
	@printf "  make ingress\n"
	@printf "  make jobs\n\n"

	@printf "ArgoCD\n"
	@printf "  make argocd\n\n"
