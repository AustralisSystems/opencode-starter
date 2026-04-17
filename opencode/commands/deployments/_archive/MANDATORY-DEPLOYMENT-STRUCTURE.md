# MANDATORY KUBERNETES DEPLOYMENT DIRECTORY STRUCTURE

## Overview

This document defines the **MANDATORY** directory and file structure for universal Kubernetes deployments that MUST BE STRICTLY ADHERED TO across all environments, platforms, and applications. This structure follows KISS principles while ensuring production-ready, secure, and scalable deployments.

## Core Principles

1. **KISS Compliance**: Keep It Simple, Stupid - No unnecessary complexity
2. **Universal Compatibility**: Works across local K8s, AWS EKS, Azure AKS, GCP GKE, and on-premises
3. **GitOps Ready**: Structured for ArgoCD, Flux, and other GitOps tools
4. **Security First**: Built-in security policies and compliance
5. **Environment Agnostic**: Consistent deployment patterns across all environments
6. **Microservices Compatible**: Supports both microservices and monolithic architectures

## MANDATORY Directory Structure

```
deployments/                           # Root deployment directory
├── README.md                          # MANDATORY: Deployment guide and overview
├── DEPLOYMENT-STANDARDS.md            # MANDATORY: Standards and compliance requirements
├── .gitignore                         # MANDATORY: Exclude secrets and temporary files
├── k8s/                              # MANDATORY: Main Kubernetes configurations
│   ├── apps/                         # MANDATORY: Application-specific deployments
│   │   ├── {app-name}/               # MANDATORY: One directory per application/microservice
│   │   │   ├── base/                 # MANDATORY: Base Kustomize configuration
│   │   │   │   ├── kustomization.yaml
│   │   │   │   ├── deployment.yaml
│   │   │   │   ├── service.yaml
│   │   │   │   ├── configmap.yaml
│   │   │   │   ├── ingress.yaml
│   │   │   │   └── hpa.yaml           # Horizontal Pod Autoscaler
│   │   │   ├── overlays/             # MANDATORY: Environment-specific overlays
│   │   │   │   ├── development/      # MANDATORY: Development environment
│   │   │   │   │   ├── kustomization.yaml
│   │   │   │   │   ├── replica-patch.yaml
│   │   │   │   │   ├── resource-patch.yaml
│   │   │   │   │   └── env-vars.yaml
│   │   │   │   ├── staging/          # MANDATORY: Staging environment
│   │   │   │   │   ├── kustomization.yaml
│   │   │   │   │   ├── replica-patch.yaml
│   │   │   │   │   ├── resource-patch.yaml
│   │   │   │   │   └── env-vars.yaml
│   │   │   │   └── production/       # MANDATORY: Production environment
│   │   │   │       ├── kustomization.yaml
│   │   │   │       ├── replica-patch.yaml
│   │   │   │       ├── resource-patch.yaml
│   │   │   │       ├── env-vars.yaml
│   │   │   │       └── pdb.yaml      # Pod Disruption Budget
│   │   │   ├── configs/              # MANDATORY: Configuration templates
│   │   │   │   ├── app-config.yaml
│   │   │   │   ├── logging-config.yaml
│   │   │   │   └── monitoring-config.yaml
│   │   │   ├── secrets/              # MANDATORY: Secret templates (NO ACTUAL SECRETS)
│   │   │   │   ├── secret-template.yaml
│   │   │   │   ├── external-secret.yaml
│   │   │   │   └── sealed-secret.yaml
│   │   │   ├── policies/             # MANDATORY: Application-specific policies
│   │   │   │   ├── network-policy.yaml
│   │   │   │   ├── pod-security-policy.yaml
│   │   │   │   └── resource-quota.yaml
│   │   │   ├── tests/                # MANDATORY: Deployment validation tests
│   │   │   │   ├── health-check.yaml
│   │   │   │   ├── integration-test.yaml
│   │   │   │   └── smoke-test.yaml
│   │   │   ├── monitoring/           # MANDATORY: Application monitoring
│   │   │   │   ├── servicemonitor.yaml
│   │   │   │   ├── prometheusrule.yaml
│   │   │   │   └── grafana-dashboard.json
│   │   │   └── docs/                 # MANDATORY: Application deployment documentation
│   │   │       ├── README.md
│   │   │       ├── DEPLOYMENT.md
│   │   │       ├── TROUBLESHOOTING.md
│   │   │       └── API.md
│   │   └── _templates/               # MANDATORY: Application template directory
│   │       ├── microservice/         # Template for new microservices
│   │       ├── web-app/             # Template for web applications
│   │       ├── database/            # Template for database deployments
│   │       └── worker/              # Template for background workers
│   ├── infrastructure/               # MANDATORY: Shared infrastructure components
│   │   ├── ingress-controllers/      # MANDATORY: Ingress controller deployments
│   │   │   ├── nginx/
│   │   │   ├── traefik/
│   │   │   └── istio/
│   │   ├── service-mesh/            # MANDATORY: Service mesh configurations
│   │   │   ├── istio/
│   │   │   ├── linkerd/
│   │   │   └── consul-connect/
│   │   ├── cert-manager/            # MANDATORY: Certificate management
│   │   │   ├── cert-manager.yaml
│   │   │   ├── cluster-issuer.yaml
│   │   │   └── certificates.yaml
│   │   ├── external-secrets/        # MANDATORY: External secrets management
│   │   │   ├── external-secrets-operator.yaml
│   │   │   ├── secret-stores.yaml
│   │   │   └── cluster-secret-store.yaml
│   │   ├── storage-classes/         # MANDATORY: Storage class definitions
│   │   │   ├── fast-ssd.yaml
│   │   │   ├── standard.yaml
│   │   │   └── backup.yaml
│   │   └── dns/                     # MANDATORY: DNS and service discovery
│   │       ├── external-dns.yaml
│   │       └── coredns-config.yaml
│   ├── monitoring/                   # MANDATORY: Observability stack
│   │   ├── prometheus/              # MANDATORY: Prometheus monitoring
│   │   │   ├── prometheus.yaml
│   │   │   ├── prometheus-operator.yaml
│   │   │   └── recording-rules.yaml
│   │   ├── grafana/                 # MANDATORY: Grafana dashboards
│   │   │   ├── grafana.yaml
│   │   │   ├── dashboards/
│   │   │   └── datasources.yaml
│   │   ├── jaeger/                  # MANDATORY: Distributed tracing
│   │   │   ├── jaeger-operator.yaml
│   │   │   └── jaeger-instance.yaml
│   │   ├── alertmanager/            # MANDATORY: Alert management
│   │   │   ├── alertmanager.yaml
│   │   │   └── alert-routes.yaml
│   │   └── logging/                 # MANDATORY: Log aggregation
│   │       ├── elasticsearch/
│   │       ├── logstash/
│   │       ├── kibana/
│   │       └── fluent-bit/
│   ├── security/                     # MANDATORY: Security policies and configurations
│   │   ├── network-policies/        # MANDATORY: Network segmentation
│   │   │   ├── default-deny.yaml
│   │   │   ├── allow-dns.yaml
│   │   │   └── microservice-policies.yaml
│   │   ├── pod-security-policies/   # MANDATORY: Pod security standards
│   │   │   ├── restricted.yaml
│   │   │   ├── baseline.yaml
│   │   │   └── privileged.yaml
│   │   ├── opa-gatekeeper/          # MANDATORY: Policy enforcement
│   │   │   ├── gatekeeper.yaml
│   │   │   ├── constraint-templates/
│   │   │   └── constraints/
│   │   ├── rbac/                    # MANDATORY: Role-based access control
│   │   │   ├── cluster-roles.yaml
│   │   │   ├── service-accounts.yaml
│   │   │   └── role-bindings.yaml
│   │   └── admission-controllers/   # MANDATORY: Admission control
│   │       ├── validating-webhooks.yaml
│   │       └── mutating-webhooks.yaml
│   ├── networking/                   # MANDATORY: Network configurations
│   │   ├── load-balancers/
│   │   ├── service-mesh-config/
│   │   └── ingress-configs/
│   ├── platforms/                    # MANDATORY: Platform-specific configurations
│   │   ├── aws/                     # AWS EKS specific
│   │   │   ├── load-balancer-controller.yaml
│   │   │   ├── ebs-csi-driver.yaml
│   │   │   ├── efs-csi-driver.yaml
│   │   │   ├── cluster-autoscaler.yaml
│   │   │   └── iam-roles.yaml
│   │   ├── azure/                   # Azure AKS specific
│   │   │   ├── application-gateway.yaml
│   │   │   ├── azure-disk-csi.yaml
│   │   │   ├── azure-file-csi.yaml
│   │   │   └── cluster-autoscaler.yaml
│   │   ├── gcp/                     # GCP GKE specific
│   │   │   ├── gce-ingress.yaml
│   │   │   ├── gcp-compute-csi.yaml
│   │   │   ├── gcp-filestore-csi.yaml
│   │   │   └── cluster-autoscaler.yaml
│   │   └── on-premises/             # On-premises specific
│   │       ├── metallb.yaml
│   │       ├── local-path-provisioner.yaml
│   │       └── nfs-provisioner.yaml
│   └── environments/                 # MANDATORY: Global environment configurations
│       ├── development/
│       │   ├── namespace.yaml
│       │   ├── resource-quotas.yaml
│       │   └── limit-ranges.yaml
│       ├── staging/
│       │   ├── namespace.yaml
│       │   ├── resource-quotas.yaml
│       │   └── limit-ranges.yaml
│       └── production/
│           ├── namespace.yaml
│           ├── resource-quotas.yaml
│           ├── limit-ranges.yaml
│           └── priority-classes.yaml
├── helm-charts/                      # MANDATORY: Custom Helm charts directory
│   ├── microservice/                # Generic microservice chart
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   ├── values-dev.yaml
│   │   ├── values-staging.yaml
│   │   ├── values-prod.yaml
│   │   └── templates/
│   ├── web-app/                     # Web application chart
│   └── database/                    # Database deployment chart
├── gitops/                          # MANDATORY: GitOps configurations
│   ├── argocd/                      # ArgoCD configurations
│   │   ├── installation/
│   │   │   ├── argocd.yaml
│   │   │   └── argocd-values.yaml
│   │   ├── projects/
│   │   │   ├── default-project.yaml
│   │   │   └── production-project.yaml
│   │   ├── repositories/
│   │   │   └── repo-credentials.yaml
│   │   └── applications/
│   │       ├── app-of-apps.yaml
│   │       ├── infrastructure-apps.yaml
│   │       └── application-sets/
│   ├── flux/                        # Flux v2 configurations
│   │   ├── installation/
│   │   │   └── flux-system.yaml
│   │   ├── sources/
│   │   │   ├── git-repositories.yaml
│   │   │   └── oci-repositories.yaml
│   │   ├── kustomizations/
│   │   │   ├── infrastructure.yaml
│   │   │   └── applications.yaml
│   │   └── helm-releases/
│   └── applications/                # Application definitions
│       ├── infrastructure/
│       └── microservices/
├── ci/                              # MANDATORY: CI/CD pipeline configurations
│   ├── github-actions/              # GitHub Actions workflows
│   │   ├── build-and-test.yml
│   │   ├── security-scan.yml
│   │   ├── deploy-staging.yml
│   │   └── deploy-production.yml
│   ├── gitlab-ci/                   # GitLab CI configurations
│   │   ├── .gitlab-ci.yml
│   │   ├── build-stage.yml
│   │   ├── test-stage.yml
│   │   └── deploy-stage.yml
│   ├── jenkins/                     # Jenkins pipeline configurations
│   │   ├── Jenkinsfile
│   │   └── pipeline-templates/
│   └── tekton/                      # Tekton pipeline configurations
│       ├── tasks/
│       ├── pipelines/
│       └── triggers/
├── scripts/                         # MANDATORY: Deployment automation scripts
│   ├── setup-cluster.sh            # Initial cluster setup
│   ├── deploy-app.sh               # Application deployment script
│   ├── rollback.sh                 # Rollback script
│   ├── health-check.sh             # Health validation script
│   ├── backup.sh                   # Backup automation
│   └── monitoring-setup.sh         # Monitoring stack setup
├── docs/                           # MANDATORY: Comprehensive documentation
│   ├── README.md                   # Overview and getting started
│   ├── DEPLOYMENT-GUIDE.md         # Detailed deployment guide
│   ├── ARCHITECTURE.md             # Architecture documentation
│   ├── SECURITY.md                 # Security guidelines and policies
│   ├── MONITORING.md               # Monitoring and observability guide
│   ├── TROUBLESHOOTING.md          # Common issues and solutions
│   ├── RUNBOOKS.md                 # Operational runbooks
│   ├── DISASTER-RECOVERY.md        # DR procedures and plans
│   └── API-REFERENCE.md            # API documentation
└── tests/                          # MANDATORY: Integration and validation tests
    ├── unit/                       # Unit tests for configurations
    ├── integration/                # Integration tests
    ├── e2e/                        # End-to-end tests
    ├── security/                   # Security validation tests
    ├── performance/                # Performance and load tests
    └── chaos/                      # Chaos engineering tests
```

## MANDATORY File Requirements

### Root Level Files

1. **README.md** - MUST include:

   - Project overview and purpose
   - Quick start guide
   - Directory structure explanation
   - Deployment commands
   - Contact information and support

2. **DEPLOYMENT-STANDARDS.md** - MUST include:

   - Deployment standards and requirements
   - Security compliance requirements
   - Resource limits and quotas
   - Naming conventions
   - Environment promotion process

3. **.gitignore** - MUST exclude:
   - Actual secrets and credentials
   - Temporary files and cache
   - Build artifacts
   - Local development files

### Application Directory Requirements

Each application directory MUST include:

1. **Base Kustomize Configuration**:

   - `kustomization.yaml` - Base configuration
   - `deployment.yaml` - Kubernetes Deployment
   - `service.yaml` - Kubernetes Service
   - `configmap.yaml` - Application configuration
   - `ingress.yaml` - Ingress configuration (if needed)
   - `hpa.yaml` - Horizontal Pod Autoscaler

2. **Environment Overlays**:

   - Development, staging, and production overlays
   - Environment-specific resource patches
   - Environment-specific configuration

3. **Security Policies**:

   - Network policies for microsegmentation
   - Pod security policies/standards
   - Resource quotas and limits

4. **Monitoring Configuration**:

   - ServiceMonitor for Prometheus
   - PrometheusRule for alerting
   - Grafana dashboard configuration

5. **Documentation**:
   - Application-specific deployment guide
   - Troubleshooting documentation
   - API documentation (if applicable)

## MANDATORY Standards Compliance

### Naming Conventions

1. **Resources**: Use kebab-case (e.g., `my-application`)
2. **Labels**: Follow standard Kubernetes labels
3. **Annotations**: Use consistent annotation patterns
4. **Environments**: Use standard environment names (development, staging, production)

### Required Labels

All Kubernetes resources MUST include these labels:

```yaml
labels:
  app.kubernetes.io/name: <app-name>
  app.kubernetes.io/instance: <instance-name>
  app.kubernetes.io/version: <version>
  app.kubernetes.io/component: <component>
  app.kubernetes.io/part-of: <application>
  app.kubernetes.io/managed-by: <tool>
  environment: <environment>
```

### Required Annotations

All deployments MUST include these annotations:

```yaml
annotations:
  deployment.kubernetes.io/revision: <revision>
  kubectl.kubernetes.io/last-applied-configuration: <config>
  argocd.argoproj.io/sync-wave: <wave>
```

### Resource Requirements

All containers MUST specify:

```yaml
resources:
  requests:
    memory: <request-memory>
    cpu: <request-cpu>
  limits:
    memory: <limit-memory>
    cpu: <limit-cpu>
```

### Security Requirements

All pods MUST include:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
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
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Platform-Specific Adaptations

### AWS EKS

- Use AWS Load Balancer Controller
- Implement EBS/EFS CSI drivers
- Configure Cluster Autoscaler
- Use IAM Roles for Service Accounts (IRSA)

### Azure AKS

- Use Azure Application Gateway
- Implement Azure Disk/File CSI drivers
- Configure Cluster Autoscaler
- Use Azure AD integration

### GCP GKE

- Use GCP Load Balancer
- Implement GCP Compute/Filestore CSI drivers
- Configure Cluster Autoscaler
- Use Google Cloud IAM integration

### On-Premises

- Use MetalLB for load balancing
- Implement local storage provisioners
- Configure manual scaling
- Use LDAP/Active Directory integration

## GitOps Integration

### ArgoCD Requirements

- Application definitions MUST use ApplicationSets for multi-environment
- Sync policies MUST be configured appropriately
- Progressive sync strategies MUST be implemented
- Notification integrations MUST be configured

### Flux Requirements

- GitRepository sources MUST be configured
- Kustomization resources MUST be structured properly
- HelmRelease resources MUST follow best practices
- Multi-tenancy MUST be implemented where needed

## CI/CD Pipeline Requirements

### Build Stage

- MUST include container image building
- MUST include security scanning (SAST, container scan)
- MUST include unit and integration testing
- MUST include artifact signing

### Deploy Stage

- MUST include environment-specific deployment
- MUST include health checks and validation
- MUST include rollback capabilities
- MUST include monitoring and alerting integration

### Security Integration

- MUST include vulnerability scanning
- MUST include policy validation
- MUST include secret scanning
- MUST include compliance checking

## Validation and Testing

### Pre-Deployment Testing

- Configuration validation using kubeval/conftest
- Security policy validation
- Resource requirement validation
- Network policy validation

### Post-Deployment Testing

- Health check validation
- Integration testing
- Performance testing
- Security testing

## Monitoring and Observability

### Required Metrics

- Application performance metrics
- Infrastructure metrics
- Business metrics
- Security metrics

### Required Logs

- Application logs
- Access logs
- Audit logs
- Security logs

### Required Traces

- Distributed tracing for microservices
- Database query tracing
- External service call tracing
- Error and exception tracing

## Compliance and Governance

### Security Compliance

- Pod Security Standards (Restricted)
- Network segmentation policies
- RBAC implementation
- Secret management best practices

### Operational Compliance

- Resource quotas and limits
- Multi-environment separation
- Backup and disaster recovery
- Monitoring and alerting

## Migration and Adoption

### Phase 1: Foundation Setup

1. Create directory structure
2. Implement basic Kustomize configurations
3. Set up CI/CD pipelines
4. Configure monitoring stack

### Phase 2: Security and Governance

1. Implement security policies
2. Configure RBAC
3. Set up policy enforcement
4. Implement secret management

### Phase 3: Advanced Features

1. Implement GitOps workflows
2. Configure service mesh
3. Implement advanced monitoring
4. Set up disaster recovery

### Phase 4: Optimization

1. Performance tuning
2. Cost optimization
3. Advanced security features
4. Chaos engineering implementation

## Support and Maintenance

### Regular Tasks

- Security updates and patches
- Configuration drift detection
- Performance monitoring and tuning
- Backup and restore testing

### Emergency Procedures

- Incident response procedures
- Rollback procedures
- Disaster recovery activation
- Security breach response

---

**ENFORCEMENT**: This structure is MANDATORY and MUST be followed exactly. Any deviations require explicit approval and documentation. The structure supports KISS principles while ensuring enterprise-grade deployment capabilities across all platforms and environments.
