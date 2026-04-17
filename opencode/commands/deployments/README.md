# Deployments Commands - Universal Kubernetes Deployment Framework

## Overview

This directory contains the comprehensive universal Kubernetes deployment framework for Claude Code CLI. The framework is designed following industry best practices, microservices architecture patterns, KISS principles, and enterprise-grade security standards.

## Framework Components

###  Core Documentation

- **`KUBERNETES-DEPLOYMENT-STRUCTURE.md`** - **MANDATORY** directory and file structure that MUST be strictly adhered to
- **`K8S-DEPLOYMENT-TEMPLATES.md`** - Universal Kubernetes deployment templates with production-ready configurations
- **`VALIDATION-CHECKLIST.md`** - Comprehensive validation checklist for framework compliance
- **`README.md`** - This overview document

###  Architecture Commands

- **`deployments-k8s-architecture-prompt.yaml`** - MCP prompt for comprehensive Kubernetes architecture design
- **`deployments-k8s-architecture.md`** - Architecture design command documentation and execution guide

###  Planning Commands

- **`deployments-planning-prompt.yaml`** - MCP prompt for comprehensive deployment planning
- **`deployments-planning.md`** - Deployment planning command documentation and execution guide

###  Implementation Commands

- **`deployments-implement-prompt.yaml`** - MCP prompt for deployment execution with KISS principles
- **`deployments-implement.md`** - Deployment implementation command documentation and execution guide

###  Legacy Commands (Retained for Compatibility)

- **`deployments-app-planning-prompt.yaml`** - Legacy planning prompt (superseded by universal planning)
- **`deployments-app-planning.md`** - Legacy planning documentation
- **`deployments-app-deploy-prompt.yaml`** - Legacy deploy prompt (superseded by universal implementation)
- **`deployments-app-deploy.md`** - Legacy deploy documentation

## Command Usage

### Architecture Phase

Design comprehensive Kubernetes deployment architecture with universal platform compatibility:

```bash
# Universal Kubernetes architecture design
/deployments-k8s-architecture [repository-name] [repository-type] [deployment-scope] [platforms] [environments]

# Examples:
/deployments-k8s-architecture user-platform multi-service service-mesh aws-eks,azure-aks,k8s development,staging,production
/deployments-k8s-architecture web-app web-application single-service k8s,gcp-gke development,production
/deployments-k8s-architecture api-ecosystem microservice ecosystem multi-cloud development,staging,pre-production,production
```

### Planning Phase

Execute comprehensive deployment planning with universal platform compatibility:

```bash
# Universal Kubernetes deployment planning
/deployments-planning [application-name] [architecture-type] [platforms] [environments]

# Examples:
/deployments-planning user-service microservice aws-eks,azure-aks development,staging,production
/deployments-planning web-app web-application k8s,gcp-gke development,production
/deployments-planning api-gateway api-service multi-cloud development,staging,pre-production,production
```

### Implementation Phase

Execute deployment to target environment and platform:

```bash
# Universal Kubernetes deployment implementation
/deployments-implement [application] [environment] [platform] [options]

# Examples:
/deployments-implement user-service development k8s
/deployments-implement web-app staging aws-eks --deployment-strategy=blue-green
/deployments-implement api-gateway production azure-aks --rollback-enabled=true
```

### Complete Workflow

The recommended workflow follows a three-phase approach:

```bash
# Phase 1: Architecture Design
/deployments-k8s-architecture my-platform multi-service service-mesh aws-eks,azure-aks development,staging,production

# Phase 2: Detailed Planning (after architecture approval)
/deployments-planning user-service microservice aws-eks development,staging,production

# Phase 3: Implementation (after planning approval)
/deployments-implement user-service development aws-eks --deployment-strategy=rolling

# Complete Example Workflow:
# 1. Design overall platform architecture
/deployments-k8s-architecture e-commerce-platform multi-service ecosystem aws-eks,azure-aks,gcp-gke development,staging,production

# 2. Plan specific service deployment
/deployments-planning user-service microservice aws-eks development,staging,production

# 3. Execute deployment to development
/deployments-implement user-service development aws-eks

# 4. Promote to staging after validation
/deployments-implement user-service staging aws-eks --deployment-strategy=blue-green

# 5. Deploy to production with advanced strategy
/deployments-implement user-service production aws-eks --deployment-strategy=canary
```

## Framework Features

###  Architecture Design Capabilities

- **Repository Analysis**: Component discovery and dependency mapping
- **Universal Architecture**: Platform-agnostic Kubernetes patterns
- **Ingress Controller Design**: Comprehensive traffic management and routing
- **Service Mesh Integration**: Istio, Linkerd, Consul Connect patterns
- **Security Architecture**: Pod Security Standards and network policies
- **Observability Design**: Prometheus, Grafana, Jaeger, ELK/EFK integration

###  Universal Platform Support

- **Local Development**: Docker Desktop, Minikube, Kind, K3s
- **Cloud Platforms**: AWS EKS, Azure AKS, GCP GKE
- **Enterprise**: On-premises, OpenShift, VMware Tanzu
- **Multi-Cloud**: Hybrid deployments across platforms

###  Architecture Patterns

- **Microservices**: Service mesh integration, communication patterns
- **Web Applications**: Frontend/backend separation, static content serving
- **API Services**: Gateway patterns, load balancing, rate limiting
- **Database Services**: StatefulSet patterns, persistent storage, backup
- **Worker Services**: Job processing, queue integration, scaling

###  Deployment Strategies

- **Rolling Deployment**: Standard Kubernetes rolling updates
- **Blue-Green Deployment**: Zero-downtime parallel environment switching
- **Canary Deployment**: Progressive traffic routing with validation
- **Recreate Deployment**: Complete replacement for stateful applications

###  Security-First Approach

- **Pod Security Standards**: Restricted profile enforcement
- **Network Policies**: Microsegmentation and traffic control
- **RBAC**: Role-based access control with least privilege
- **Secret Management**: External Secrets Operator integration
- **Admission Control**: OPA Gatekeeper policy enforcement

###  CI/CD Integration

- **GitOps Workflows**: ArgoCD and Flux integration patterns
- **Pipeline Templates**: GitHub Actions, GitLab CI, Jenkins
- **Security Scanning**: SAST, container scanning, manifest validation
- **Progressive Delivery**: Automated rollout and rollback

###  Monitoring and Observability

- **Metrics Collection**: Prometheus ServiceMonitor integration
- **Alerting**: PrometheusRule with threshold-based alerts
- **Distributed Tracing**: Jaeger and OpenTelemetry patterns
- **Log Aggregation**: ELK/EFK stack integration
- **Dashboard**: Grafana dashboard configurations

###  KISS Principles Adherence

- Simple, straightforward configurations over complex ones
- Standard Kubernetes resources over custom resources
- Clear, readable manifest files
- Basic, effective monitoring and health checks
- Simple deployment strategies first
- Well-established patterns and practices

## Directory Structure Compliance

All deployments MUST follow the structure defined in `KUBERNETES-DEPLOYMENT-STRUCTURE.md`:

```
repository-name/                     # Repository root (NO WRAPPER)
 project/                        # Dev workspace (IN GIT, NOT PROD)
 services/                       # Application source code
    {service-name}/            # Per-service directory
        app/                   # Service code (framework-specific)
        tests/
        Dockerfile
        README.md
 apps/                          # K8S application manifests
    base/                      # Kustomize base configurations
       {service-name}/
           kustomization.yaml
           deployment.yaml
           service.yaml
           configmap.yaml
           ingress.yaml
    overlays/                  # Environment-specific overlays
       development/
       staging/
       production/
    configs/                   # Configuration templates
    secrets/                   # Secret templates
    policies/                  # Security policies
    tests/                     # Deployment tests
    monitoring/                # Monitoring configs
 infrastructure/                 # K8S platform components
    controllers/               # Ingress controllers, operators
    storage/                   # StorageClass definitions
    monitoring/                # Observability stack
    security/                  # Security policies
    service-mesh/              # Service mesh configs
 clusters/                      # Environment configs
 gitops/                        # GitOps configurations
 helm-charts/                   # Custom Helm charts
 ci/                            # CI/CD pipelines
 scripts/                       # Production automation
 docs/                          # Official documentation
 tests/                         # Integration tests
 .templates/                    # Reusable templates
```

## Template Usage

### Microservice Template

```bash
# Copy the microservice template
cp -r .templates/microservice services/my-service

# Customize for your application
sed -i 's/microservice-template/my-service/g' apps/base/my-service/*.yaml

# Deploy to development
kubectl apply -k apps/overlays/development
```

### Web Application Template

```bash
# Copy the web application template
cp -r .templates/web-app services/my-webapp

# Customize configurations
# Edit deployment, service, ingress files as needed

# Deploy with ArgoCD
kubectl apply -f gitops/argocd/applications/my-webapp-app.yaml
```

## Security Requirements

### Pod Security Standards

All pods MUST implement the Restricted Pod Security Standard:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000

containerSecurityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

### Network Policies

All applications MUST implement network microsegmentation:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### RBAC

All applications MUST use dedicated service accounts with minimal permissions:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-service-account
automountServiceAccountToken: false
```

## Monitoring Requirements

### Metrics Collection

All applications MUST expose metrics for Prometheus:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-metrics
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
    - port: metrics
      interval: 30s
```

### Health Checks

All applications MUST implement health endpoints:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

## Validation Commands

### Manifest Validation

```bash
# Validate Kubernetes manifests
kubeval apps/base/**/*.yaml
kubeval infrastructure/**/*.yaml

# Validate Kustomize builds
kustomize build apps/overlays/production --dry-run

# Security validation with Conftest
conftest verify --policy infrastructure/security/ apps/**/*.yaml
```

### Deployment Testing

```bash
# Dry run deployment
kubectl apply -k apps/overlays/development --dry-run=server

# Test health checks
kubectl run test-pod --image=curlimages/curl --rm -i --restart=Never \
  -- curl -f http://my-app-service/health
```

## Troubleshooting

### Common Issues

1. **Pod Security Standard Violations**

   ```bash
   # Check pod security context
   kubectl describe pod <pod-name>
   kubectl get pod <pod-name> -o yaml | grep securityContext -A 10
   ```

2. **Network Policy Blocking Traffic**

   ```bash
   # Check network policies
   kubectl get networkpolicies
   kubectl describe networkpolicy <policy-name>
   ```

3. **Resource Limits Exceeded**

   ```bash
   # Check resource usage
   kubectl top pods
   kubectl describe pod <pod-name> | grep -A 5 "Limits\|Requests"
   ```

4. **Health Check Failures**
   ```bash
   # Test health endpoints
   kubectl exec -it <pod-name> -- wget -qO- http://localhost:8080/health
   kubectl logs <pod-name> | grep health
   ```

### Debug Commands

```bash
# Get deployment status
kubectl get deployments
kubectl describe deployment <deployment-name>

# Check pod logs
kubectl logs -l app=<app-name> --tail=100

# Check events
kubectl get events --sort-by='.lastTimestamp'

# Test service connectivity
kubectl exec -it debug-pod -- nslookup <service-name>
```

## Best Practices

### Development Workflow

1. **Plan First**: Always use `/deployments-planning` before implementation
2. **Start Simple**: Use KISS principles, avoid over-engineering
3. **Security by Design**: Implement Pod Security Standards from day one
4. **Test Early**: Use dry-run and validation commands frequently
5. **Monitor Everything**: Implement metrics and health checks

### Production Deployment

1. **Blue-Green or Canary**: Use advanced deployment strategies for critical applications
2. **Resource Limits**: Always define resource requests and limits
3. **Pod Disruption Budgets**: Implement PDBs for availability guarantees
4. **Backup and Recovery**: Plan disaster recovery procedures
5. **Security Scanning**: Integrate security scanning in CI/CD pipelines

### Platform Optimization

- **AWS EKS**: Use AWS Load Balancer Controller, EBS CSI drivers, IRSA
- **Azure AKS**: Use Application Gateway, Azure CSI drivers, Pod Identity
- **GCP GKE**: Use GCP Load Balancer, GCP CSI drivers, Workload Identity
- **On-premises**: Use MetalLB, local storage provisioners, Ingress NGINX

## Support and Maintenance

### Regular Tasks

- Security updates and vulnerability scanning
- Configuration drift detection and remediation
- Performance monitoring and optimization
- Backup and disaster recovery testing
- Cost optimization and resource right-sizing

### Emergency Procedures

- Incident response and escalation procedures
- Automated rollback procedures for failed deployments
- Disaster recovery activation and validation
- Security breach response and containment

---

**ENFORCEMENT**: This deployment framework is MANDATORY for all Kubernetes deployments. It ensures consistent, secure, and scalable deployment practices across all environments and platforms. All team members MUST follow these standards and use the provided templates and commands.
