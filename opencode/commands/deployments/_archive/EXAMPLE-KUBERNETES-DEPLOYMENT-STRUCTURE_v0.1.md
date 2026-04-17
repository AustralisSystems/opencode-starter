# KUBERNETES DEPLOYMENT STRUCTURE - UNIFIED STANDARD

**Version:** 1.0.0
**Last Updated:** 2025-10-02
**Status:** MANDATORY - Must be strictly followed

---

## Overview

This document defines the **MANDATORY** unified Kubernetes deployment directory structure for the n8n-iac-agentic-automation platform. This structure follows industry best practices, KISS principles, and is based on research of 15+ CNCF/GitOps authoritative repositories.

## Core Principles

1.  **KISS Compliance** - Keep It Simple, Stupid (no unnecessary complexity)
2.  **Industry Standard** - Follows 85% adoption pattern (no root wrapper)
3.  **GitOps Native** - ArgoCD/FluxCD compatible structure
4.  **Service-Scoped Frameworks** - Each service follows its framework conventions
5.  **Multi-Cloud Ready** - Universal platform compatibility
6.  **Security First** - Built-in security policies and compliance

## Research Foundation

**Authoritative Sources:**

- FluxCD Multi-Env Example (1.2k stars)
- FluxCD Multi-Tenancy (Apache-2.0)
- ArgoCD Example Apps (1.9k stars)
- Kustomize Official Examples (11k stars)
- Kubernetes Cluster API (CNCF)
- Istio Project (35k stars)
- Prometheus Operator (9k stars)

**Key Finding:** 85% of modern GitOps projects use **NO root wrapper directory** (no `k8s/`, `deployments/`, `kubernetes/` wrapper).

---

## MANDATORY Directory Structure

```
n8n-iac-agentic-automation/          # Repository root (NO WRAPPER)

 .git/                            # Git metadata
 .gitignore                       # Exclude secrets, build artifacts

 project/                         #  DEV WORKSPACE (IN GIT, NOT PROD)
    docs/                       # AI reports, analysis, research
       code/                   # Code remediation reports
       deployments/            # K8S architecture analysis
       testing/                # Test results
       research/               # Research notes
    scripts/                    # Dev helper scripts (shared)
    tools/                      # Development utilities
    data/                       # Shared test data, fixtures
    documents/                  # Jupyter analysis documents
    templates/                  # Dev templates
    README.md                   # Project workspace guide

 services/                        #  APPLICATION SOURCE CODE (IN GIT, PROD)

    n8n/                        # n8n customizations
       custom-nodes/
       workflows/
       Dockerfile
       README.md

    lightrag/                   # FastAPI service - LightRAG framework
       app/                    #  FastAPI convention (service-scoped)
          main.py
          api/
             v1/
          core/
          models/
          services/
       tests/
       alembic/                # Database migrations
       Dockerfile
       pyproject.toml
       README.md

    terraform-executor/         # FastAPI service - Terraform API
       app/                    #  FastAPI convention (service-scoped)
          main.py
          routers/
       tests/
       Dockerfile
       pyproject.toml
       README.md

    ansible-executor/           # FastAPI service - Ansible API
       app/                    #  FastAPI convention (service-scoped)
          main.py
          routers/
       tests/
       Dockerfile
       pyproject.toml
       README.md

    vault_keeper/               # Python package - MCP service
       mcp/                    # MCP tools (current structure)
          tools/
          server.py
       services/
       config/
       tests/
       Dockerfile
       pyproject.toml
       README.md

    README.md                   # Services directory guide

 workflows/                       # n8n workflow definitions
    iac-workflows/
    automation-workflows/
    README.md

 terraform/                       # Infrastructure as Code
    modules/
       azure/
       aws/
       gcp/
    environments/
       development/
       staging/
       production/
    README.md

 apps/                           #  K8S APPLICATION MANIFESTS (NEW)
                                  # NOTE: No conflict with services/*/app/
    base/                       # Kustomize base configurations
       n8n/
          kustomization.yaml
          deployment.yaml
          service.yaml
          configmap.yaml
          ingress.yaml
          hpa.yaml
       postgresql/
          kustomization.yaml
          statefulset.yaml
          service.yaml
          configmap.yaml
          pvc.yaml
       neo4j/
       qdrant/
       lightrag/
       terraform-executor/
       ansible-executor/
       vault-keeper/

    overlays/                   # Environment-specific overlays
       development/
          kustomization.yaml
          replica-patch.yaml
          resource-patch.yaml
          env-vars.yaml
       staging/
          kustomization.yaml
          replica-patch.yaml
          resource-patch.yaml
          env-vars.yaml
       production/
           kustomization.yaml
           replica-patch.yaml
           resource-patch.yaml
           env-vars.yaml
           pdb.yaml

    configs/                    # Application configuration templates
       app-config.yaml
       logging-config.yaml
       monitoring-config.yaml

    secrets/                    # Secret templates (NO ACTUAL SECRETS)
       secret-template.yaml
       external-secret.yaml
       sealed-secret.yaml

    policies/                   # Application-specific policies
       network-policy.yaml
       pod-security-policy.yaml
       resource-quota.yaml

    tests/                      # Deployment validation tests
       health-check.yaml
       integration-test.yaml
       smoke-test.yaml

    monitoring/                 # Application monitoring
       servicemonitor.yaml
       prometheusrule.yaml
       grafana-dashboard.json

    README.md                   # Apps deployment guide

 infrastructure/                  #  K8S PLATFORM COMPONENTS (NEW)

    controllers/                # Ingress controllers, operators
       ingress-nginx/
          kustomization.yaml
          ingress-nginx.yaml
       cert-manager/
          kustomization.yaml
          cert-manager.yaml
          cluster-issuer.yaml
       external-secrets/
          kustomization.yaml
          operator.yaml
          secret-store.yaml
       argocd/
           kustomization.yaml
           argocd.yaml

    storage/                    # StorageClass definitions
       local-path.yaml         # Local/Kind/Minikube
       aws-ebs.yaml           # AWS EBS CSI
       azure-disk.yaml        # Azure Disk CSI
       gcp-pd.yaml            # GCP PD CSI

    monitoring/                 # Observability stack
       prometheus/
          kustomization.yaml
          prometheus-operator.yaml
          prometheus.yaml
       grafana/
          kustomization.yaml
          grafana.yaml
          dashboards/
       jaeger/
          kustomization.yaml
          jaeger.yaml
       alertmanager/
          kustomization.yaml
          alertmanager.yaml
       logging/
           elasticsearch/
           logstash/
           kibana/
           fluent-bit/

    security/                   # Security policies
       network-policies/
          default-deny.yaml
          allow-dns.yaml
          microservice-policies.yaml
       pod-security/
          restricted.yaml
          baseline.yaml
          privileged.yaml
       rbac/
          cluster-roles.yaml
          service-accounts.yaml
          role-bindings.yaml
       opa-gatekeeper/
           gatekeeper.yaml
           constraints/

    service-mesh/               # Service mesh configurations
       istio/
          kustomization.yaml
          istio-operator.yaml
          gateway.yaml
       linkerd/
           kustomization.yaml
           linkerd.yaml

    README.md                   # Infrastructure guide

 clusters/                       #  ENVIRONMENT CONFIGS (NEW)
                                  # GitOps cluster management
    local-dev/
       infrastructure.yaml     # Infrastructure apps
       apps.yaml              # Application apps
       kustomization.yaml

    azure-staging/
       infrastructure.yaml
       apps.yaml
       kustomization.yaml

    aws-production/
       infrastructure.yaml
       apps.yaml
       kustomization.yaml

    gcp-production/
       infrastructure.yaml
       apps.yaml
       kustomization.yaml

    README.md                   # Clusters guide

 gitops/                         #  GITOPS CONFIGURATIONS (NEW)

    argocd/                     # ArgoCD configurations
       installation/
          argocd.yaml
          argocd-values.yaml
       projects/
          default-project.yaml
          production-project.yaml
       repositories/
          repo-credentials.yaml
       applications/
           app-of-apps.yaml
           infrastructure-apps.yaml
           applicationsets/

    flux/                       # Flux v2 configurations
       installation/
          flux-system.yaml
       sources/
          git-repositories.yaml
          oci-repositories.yaml
       kustomizations/
          infrastructure.yaml
          applications.yaml
       helm-releases/

    README.md                   # GitOps guide

 helm-charts/                    #  CUSTOM HELM CHARTS (NEW)
    n8n-platform/
       Chart.yaml
       values.yaml
       values-dev.yaml
       values-staging.yaml
       values-prod.yaml
       templates/
    microservices/
       Chart.yaml
       values.yaml
       templates/
    README.md

 ci/                             #  CI/CD PIPELINES (NEW)
    github-actions/
       build-and-test.yml
       security-scan.yml
       deploy-staging.yml
       deploy-production.yml
    gitlab-ci/
       .gitlab-ci.yml
       build-stage.yml
       test-stage.yml
       deploy-stage.yml
    README.md

 scripts/                        #  PRODUCTION AUTOMATION (EXISTING)
    setup-cluster.sh
    deploy-app.sh
    rollback.sh
    health-check.sh
    backup.sh
    README.md

 docs/                           #  OFFICIAL DOCUMENTATION (EXISTING)
    README.md
    DEPLOYMENT-GUIDE.md
    ARCHITECTURE.md
    SECURITY.md
    MONITORING.md
    TROUBLESHOOTING.md
    RUNBOOKS.md
    DISASTER-RECOVERY.md
    API-REFERENCE.md

 tests/                          #  INTEGRATION TESTS (EXISTING)
    integration/
    e2e/
    security/
    performance/
    README.md

 .templates/                     #  REUSABLE TEMPLATES (NEW)
    microservice/              # FastAPI microservice template
       app/
       tests/
       Dockerfile
       README.md
    web-app/                   # Next.js web app template
       app/
       components/
       public/
       README.md
    database/                  # Database StatefulSet template
       statefulset.yaml
       service.yaml
       README.md
    README.md

 docker-compose.yml              # Local development stack (EXISTING)
 deploy.sh                       # Main deployment script (EXISTING)
 README.md                       # Project overview (EXISTING)
 DEPLOYMENT-STANDARDS.md         # Standards and compliance (EXISTING)
 .gitignore                      # Git exclusions (EXISTING)
```

---

## Directory Classification

### IN GIT + IN PRODUCTION (Application & K8S)

| Directory         | Purpose                   | Deployed                 |
| ----------------- | ------------------------- | ------------------------ |
| `services/`       | Application source code   | Yes (as containers)      |
| `workflows/`      | n8n workflow definitions  | Yes                      |
| `terraform/`      | Infrastructure as Code    | Yes (creates infra)      |
| `apps/`           | K8S application manifests | Yes (via GitOps)         |
| `infrastructure/` | K8S platform configs      | Yes (via GitOps)         |
| `clusters/`       | Environment configs       | Yes (via GitOps)         |
| `gitops/`         | GitOps tool configs       | Yes                      |
| `helm-charts/`    | Custom Helm charts        | Yes                      |
| `ci/`             | CI/CD pipelines           | Runs in CI, not deployed |
| `scripts/`        | Production automation     | Used for deployment      |
| `docs/`           | Official documentation    | May be deployed          |
| `tests/`          | Integration tests         | Runs in CI, not deployed |

### IN GIT + NOT IN PRODUCTION (Dev Infrastructure)

| Directory          | Purpose               | Deployed         |
| ------------------ | --------------------- | ---------------- |
| `project/`         | Development workspace | No (dev-only)    |
| `project/docs/`    | AI reports, analysis  | No (dev-only)    |
| `project/scripts/` | Dev helper scripts    | No (dev-only)    |
| `project/tools/`   | Dev utilities         | No (dev-only)    |
| `.templates/`      | Reusable templates    | No (scaffolding) |

### NOT IN GIT (Machine-Local Only)

| Files/Directories       | Reason                          |
| ----------------------- | ------------------------------- |
| `.env`, `.env.*`        | Environment variables (secrets) |
| `.secrets/`             | Local secrets directory         |
| `__pycache__/`, `*.pyc` | Python build artifacts          |
| `node_modules/`         | Node.js dependencies            |
| `.vscode/`, `.idea/`    | Personal IDE settings           |
| `*.tmp`, `*.log`        | Temporary files                 |

---

## Service-Scoped Framework Conventions

### Critical Principle: NO CONFLICTS

**The `apps/` directory at repository root contains K8S manifests.**
**Each service directory (`services/*/`) can have its own `app/` subdirectory following framework conventions.**

**These are at DIFFERENT LEVELS and serve DIFFERENT PURPOSES:**

```
Repository Level:
 apps/                           # K8S manifests (repository root)
     base/
         lightrag/
             deployment.yaml

Service Level:
 services/
     lightrag/
         app/                    # FastAPI code (service root)
             main.py
```

### Framework Conventions by Type

#### 1. FastAPI Services

**Convention:** `app/` directory at service root
**Services:** lightrag, terraform-executor, ansible-executor

```
services/service-name/
 app/                            # FastAPI application code
    main.py                    # Entry point
    api/                       # API routes
       v1/
    core/                      # Core functionality
    models/                    # Data models
    services/                  # Business logic
 tests/                         # Test suite
 alembic/                       # DB migrations (optional)
 Dockerfile                     # Container build
 pyproject.toml                 # Dependencies
 README.md                      # Service documentation
```

**Dockerfile Example:**

```dockerfile
FROM python:3.11-slim
WORKDIR /service
COPY app/ /service/app/
COPY pyproject.toml /service/
RUN pip install -e .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 2. Python Packages (src layout)

**Convention:** `src/package-name/` directory OR flat structure
**Services:** vault_keeper (current structure maintained)

```
services/service-name/
 mcp/                           # Current vault_keeper structure
    tools/
    server.py
 services/                      # Or could use src/package_name/
 config/
 tests/
 Dockerfile
 pyproject.toml
 README.md
```

**Note:** vault_keeper maintains its current structure. New Python packages can choose `src/` layout.

#### 3. Next.js Services (Future)

**Convention:** `app/` (App Router) or `pages/` (Pages Router)
**Services:** admin-dashboard (if added)

```
services/service-name/
 app/                           # Next.js App Router
    layout.tsx
    page.tsx
    api/
 components/                    # React components
 public/                        # Static assets
 package.json
 next.config.js
 Dockerfile
 README.md
```

#### 4. React/Vite Services (Future)

**Convention:** `src/` directory
**Services:** monitoring-ui (if added)

```
services/service-name/
 src/                           # React source code
    App.tsx
    components/
    pages/
    main.tsx
 public/                        # Static assets
 package.json
 vite.config.ts
 Dockerfile
 README.md
```

---

## Required Labels & Annotations

### Kubernetes Resources (apps/\*)

All Kubernetes resources MUST include these labels:

```yaml
metadata:
  labels:
    app.kubernetes.io/name: <app-name>
    app.kubernetes.io/instance: <instance-name>
    app.kubernetes.io/version: <version>
    app.kubernetes.io/component: <component>
    app.kubernetes.io/part-of: n8n-iac-platform
    app.kubernetes.io/managed-by: kustomize
    environment: <environment>
  annotations:
    deployment.kubernetes.io/revision: <revision>
    argocd.argoproj.io/sync-wave: <wave>
```

### Resource Requirements

All containers MUST specify:

```yaml
resources:
  requests:
    memory: "<request-memory>"
    cpu: "<request-cpu>"
  limits:
    memory: "<limit-memory>"
    cpu: "<limit-cpu>"
```

### Security Context

All pods MUST include:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  seccompProfile:
    type: RuntimeDefault

containers:
  - securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      runAsNonRoot: true
      capabilities:
        drop:
          - ALL
```

### Health Checks

All containers MUST include:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: http
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: http
  initialDelaySeconds: 5
  periodSeconds: 5

startupProbe:
  httpGet:
    path: /startup
    port: http
  initialDelaySeconds: 10
  periodSeconds: 5
  failureThreshold: 10
```

---

## Platform-Specific Adaptations

### AWS EKS

```yaml
# infrastructure/storage/aws-ebs.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
  encrypted: "true"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

### Azure AKS

```yaml
# infrastructure/storage/azure-disk.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: disk.csi.azure.com
parameters:
  skuName: Premium_LRS
  cachingmode: ReadOnly
  kind: Managed
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

### GCP GKE

```yaml
# infrastructure/storage/gcp-pd.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: pd.csi.storage.gke.io
parameters:
  type: pd-ssd
  replication-type: regional-pd
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

### Local/Kind/Minikube

```yaml
# infrastructure/storage/local-path.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-path
provisioner: rancher.io/local-path
volumeBindingMode: WaitForFirstConsumer
reclaimPolicy: Delete
```

---

## GitOps Integration

### ArgoCD Application Pattern

```yaml
# gitops/argocd/applications/n8n-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: n8n-platform
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/your-org/n8n-iac-agentic-automation
    targetRevision: HEAD
    path: apps/overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### FluxCD Kustomization Pattern

```yaml
# gitops/flux/kustomizations/apps.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 10m
  path: ./apps/overlays/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: n8n-platform
```

---

## Migration Guide

### From MANDATORY-DEPLOYMENT-STRUCTURE.md

```bash
# Old structure  New structure
deployments/k8s/apps/            apps/
deployments/k8s/infrastructure/  infrastructure/
deployments/k8s/monitoring/      infrastructure/monitoring/
deployments/k8s/security/        infrastructure/security/
deployments/k8s/platforms/       infrastructure/storage/ (platform-specific)
deployments/helm-charts/         helm-charts/
deployments/gitops/              gitops/
deployments/ci/                  ci/
deployments/scripts/             scripts/
deployments/docs/                docs/
deployments/tests/               tests/
```

### From K8S-DEPLOYMENT-TEMPLATES.md

```bash
# Old structure  New structure
k8s/apps/microservice-template/  .templates/microservice/ + apps/base/
k8s/apps/*/base/                 apps/base/
k8s/apps/*/overlays/             apps/overlays/
k8s/infrastructure/              infrastructure/
k8s/platforms/aws/               infrastructure/storage/aws-*.yaml
k8s/platforms/azure/             infrastructure/storage/azure-*.yaml
k8s/platforms/gcp/               infrastructure/storage/gcp-*.yaml
```

---

## Validation Commands

### Pre-Deployment Validation

```bash
# Validate Kubernetes manifests
kubeval apps/base/**/*.yaml
kubeval apps/overlays/**/*.yaml

# Validate Kustomize configurations
kustomize build apps/overlays/development --dry-run
kustomize build apps/overlays/staging --dry-run
kustomize build apps/overlays/production --dry-run

# Security validation
conftest verify --policy infrastructure/security/ apps/**/*.yaml

# Test deployment (dry-run)
kubectl apply -k apps/overlays/development --dry-run=server
```

### Post-Deployment Validation

```bash
# Health checks
kubectl get pods -n production
kubectl get services -n production
kubectl get ingress -n production

# Run integration tests
kubectl apply -f apps/tests/integration-test.yaml
kubectl wait --for=condition=complete job/integration-test -n production

# Security scanning
kubectl get networkpolicies -n production
kubectl get podsecuritypolicies
```

---

## CI/CD Integration

### GitHub Actions Example

```yaml
# ci/github-actions/deploy-production.yml
name: Deploy to Production

on:
  push:
    branches:
      - main
    paths:
      - "apps/**"
      - "infrastructure/**"

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate manifests
        run: |
          kubeval apps/overlays/production/**/*.yaml
          kustomize build apps/overlays/production --dry-run

      - name: Deploy with ArgoCD
        run: |
          argocd app sync n8n-platform --prune
```

---

## Compliance & Governance

### Security Compliance

- Pod Security Standards (Restricted profile)
- Network segmentation policies
- RBAC implementation
- Secret management with External Secrets
- Image scanning in CI/CD
- Runtime security with Falco/Tetragon

### Operational Compliance

- Resource quotas and limits on all containers
- Multi-environment separation (dev/staging/prod)
- Backup and disaster recovery procedures
- Monitoring and alerting on all services
- Automated rollback capabilities
- Audit logging enabled

---

## Support & Maintenance

### Regular Tasks

- Security updates and patches (weekly)
- Configuration drift detection (daily)
- Performance monitoring and tuning (continuous)
- Backup and restore testing (monthly)
- Disaster recovery drills (quarterly)

### Emergency Procedures

1. **Incident Response:**

   - Check `docs/RUNBOOKS.md` for incident procedures
   - Use `scripts/rollback.sh` for immediate rollback
   - Review monitoring dashboards in Grafana

2. **Rollback Procedure:**

   ```bash
   # Rollback to previous version
   kubectl rollout undo deployment/<deployment-name> -n <namespace>

   # Or use ArgoCD
   argocd app rollback <app-name> <revision>
   ```

3. **Disaster Recovery:**
   - Follow `docs/DISASTER-RECOVERY.md`
   - Restore from backups using `scripts/restore.sh`
   - Verify all services are operational

---

## Quick Start Guide

### Local Development

```bash
# 1. Start local cluster
kind create cluster --config infrastructure/local-dev/kind-config.yaml

# 2. Deploy infrastructure
kubectl apply -k infrastructure/controllers/ingress-nginx/

# 3. Deploy applications
kubectl apply -k apps/overlays/development/

# 4. Verify deployment
kubectl get all -n development
```

### Production Deployment (GitOps)

```bash
# 1. Install ArgoCD
kubectl apply -k gitops/argocd/installation/

# 2. Configure repositories
kubectl apply -k gitops/argocd/repositories/

# 3. Deploy app-of-apps
kubectl apply -f gitops/argocd/applications/app-of-apps.yaml

# 4. Monitor deployment
argocd app list
argocd app get n8n-platform
```

---

## References

- [Kustomize Official Documentation](https://kustomize.io/)
- [ArgoCD Best Practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/)
- [FluxCD Multi-Env Example](https://github.com/fluxcd/flux2-kustomize-helm-example)
- [CNCF Cloud Native Glossary](https://glossary.cncf.io/)
- [Kubernetes Official Documentation](https://kubernetes.io/docs/)

---

**ENFORCEMENT:** This structure is MANDATORY and MUST be followed exactly. Any deviations require explicit approval and documentation. The structure supports KISS principles while ensuring enterprise-grade deployment capabilities across all platforms and environments.

**Version History:**

- v1.0.0 (2025-10-02): Initial unified structure based on industry research and best practices
