# Kubernetes Deployment & Integration Test

## Prerequisites

- Minikube or Kind installed
- Python 3.x installed
- `requests` library (Install via `pip install requests`)

## Setup & Deployment

1. Start Minikube:

   ```bash
   minikube start
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
   minikube service frontend-service --url
   python test_integration.py```
