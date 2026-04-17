# === Kubernetes Deployment Execution: K8s-Specific Deployment Orchestration ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance-prompt.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance-prompt.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns
- Ignoring K8s security standards
- Skipping K8s resource validation

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of data or services in production code
- **NO TODOs** - complete ALL work immediately
- **NO SHORTCUTS** - implement properly ALWAYS
- **NO STUBS** - write complete implementations
- **NO FIXED DATA** - use real, dynamic data
- **NO HARDCODED VALUES** - use configuration
- **NO WORKAROUNDS** - fix root causes
- **NO FAKE IMPLEMENTATIONS** - real code only
- **NO PLACEHOLDER CODE** - production-ready only
- **NO TEMPORARY SOLUTIONS** - permanent fixes only
- **NO K8s SECURITY BYPASSES** - follow all K8s security standards
- **NO K8s RESOURCE VIOLATIONS** - respect all K8s resource limits

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ KUBERNETES DOCUMENTATION:**

   - Check official Kubernetes documentation
   - Review K8s security best practices
   - Study K8s deployment patterns
   - Understand K8s resource management

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review K8s architecture documentation
   - Study K8s API documentation

3. **SEARCH ONLINE FOR K8s BEST PRACTICES:**
   - Use web search for latest K8s documentation
   - Find official K8s framework/library docs
   - Search GitHub for K8s example implementations
   - Review K8s industry best practices
   - Study similar successful K8s projects
   - Check Stack Overflow for K8s common patterns

**SEARCH PRIORITIES:**

- Official Kubernetes documentation (latest version)
- K8s security best practices (Pod Security Standards)
- K8s monitoring and observability patterns
- K8s deployment strategies (rolling, blue-green, canary)
- K8s platform-specific documentation (EKS, AKS, GKE)

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to Kubernetes best practices.

### **K8s DEPLOYMENT-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR KUBERNETES DEPLOYMENT EXECUTION ONLY:**

- **MUST:** Execute actual K8s deployment to specified environment and platform
- **MUST:** Build, deploy, and validate K8s applications
- **MUST:** Perform K8s health checks and verification
- **MUST:** Follow K8s security standards and best practices
- **MUST:** Use atomic K8s deployment practices
- **MUST:** Implement K8s security validations with standard approaches
- **MUST:** Configure K8s monitoring and alerting
- **FORBIDDEN:** Create extensive planning documentation (use `/deployments-planning` first)
- **FORBIDDEN:** Perform comprehensive analysis without execution
- **MUST:** Focus on K8s deployment execution with K8s best practices

**K8s DEPLOYMENT EXECUTION FOCUS:**

- Build and deploy K8s application components using K8s strategies
- Execute K8s deployment strategy (rolling, blue-green, canary) with K8s approaches
- Validate K8s deployment success through K8s health checks
- Monitor K8s deployment progress with K8s monitoring
- Perform post-deployment verification using K8s methods
- Execute K8s rollback if deployment fails using K8s procedures

**IF K8s BUILD/DEPLOY ISSUES OCCUR:**

- Follow debugging protocol in `./.claude/commands/code/code-debug.md`
- Use refactoring protocol in `./.claude/commands/code/code-refactor.md`
- Apply planning protocol if major changes needed
- Implement fixes per K8s best practices
- Ensure K8s security compliance per K8s standards

### **MANDATORY REPOSITORY STRUCTURE REFERENCE:**

**BEFORE EXECUTING**, you MUST read and understand the canonical repository structure:

1. **READ**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` for complete Kubernetes deployment structure
2. **UNDERSTAND**: NO root wrapper directories (no k8s/, deployments/, kubernetes/ wrapper)
3. **USE**: apps/, infrastructure/, services/, clusters/, gitops/, helm-charts/, ci/, scripts/, docs/, tests/, .templates/
4. **VALIDATE**: Reference VALIDATION-CHECKLIST.md for compliance requirements

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-k8s-deploy-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for environment, k8s_platform, namespace
3. **FOLLOW PROTOCOL**: Execute all phases according to the K8s deployment protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive K8s deployment documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% K8s deployment success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "k8s-deploy-prompt"
arguments:
  environment: "[dev|development|test|testing|stage|staging|prod|production]"
  k8s_platform: "[k8s|docker-desktop|minikube|kind|k3s|aws-eks|azure-aks|gcp-gke|on-premises|openshift|tanzu]"
  deployment_strategy: "[optional: rolling|blue-green|canary|recreate]"
  namespace: "[optional: target K8s namespace]"
  image_tag: "[optional: container image tag]"
  rollback_enabled: "[optional: true|false]"
  dry_run: "[optional: true|false]"
  force_rebuild: "[optional: true|false]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All K8s deployment phases completed according to protocol with timestamp tracking
- [ ] 100% successful K8s deployment to target environment and platform
- [ ] All K8s health checks passed and services are running (timestamped)
- [ ] Comprehensive K8s deployment documentation created with reverse date stamps
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL K8s DEPLOYMENT OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All K8s deployment reports (.md) have reverse date stamps in filenames
- [ ] All K8s build artifact logs include precise timestamps
- [ ] All K8s health check results include timestamp documentation
- [ ] All K8s deployment validation reports include proper date stamps
- [ ] All K8s monitoring setup guides follow consistent date stamp format
- [ ] All K8s quickstart guides include proper date stamps
- [ ] All K8s lifecycle management guides include timestamp documentation
- [ ] All K8s terraform infrastructure guides follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating K8s deployment files without proper reverse date stamps
- Using inconsistent date formats within same K8s deployment session
- Missing timestamps in K8s deployment documentation

### **K8s IMPLEMENTATION REQUIREMENTS:**

**KUBERNETES BEST PRACTICES - MANDATORY PRINCIPLES:**

1. **K8s Manifest Management:**

   - Use Kustomize overlays for environment-specific configs
   - Apply K8s resource patches and transformations
   - Use Helm charts for complex deployments
   - Validate K8s YAML syntax and structure

2. **K8s Security Standards:**

   - Enforce Pod Security Standards (Restricted profile)
   - Apply Network Policies with security rules
   - Configure RBAC roles and bindings
   - Use SecurityContexts and constraints

3. **K8s Resource Management:**

   - Set appropriate resource requests and limits
   - Use ConfigMaps and Secrets for configuration
   - Implement proper health checks
   - Configure resource quotas and limits

4. **K8s Monitoring and Observability:**

   - Use ServiceMonitor for Prometheus integration
   - Configure Grafana dashboards
   - Implement structured logging
   - Set up alerting rules

5. **K8s Lifecycle Management:**
   - Implement rolling updates
   - Configure blue-green deployments
   - Use canary deployments for testing
   - Implement proper rollback procedures

### **PLATFORM-SPECIFIC K8s IMPLEMENTATIONS:**

**LOCAL K8s DEVELOPMENT:**

- Use kubectl apply for direct manifest deployment
- Simple NodePort or LoadBalancer services
- Basic local storage configurations
- Straightforward networking setup

**AWS EKS:**

- Use AWS Load Balancer Controller
- Configure EBS CSI driver for persistent storage
- Apply IRSA for service authentication
- Use ALB Ingress annotations

**AZURE AKS:**

- Use Application Gateway Ingress Controller
- Configure Azure CSI drivers
- Apply Pod Identity or Workload Identity
- Use Azure Load Balancer

**GCP GKE:**

- Use GCP Load Balancer
- Configure GCP CSI drivers
- Apply Workload Identity
- Use GCE Ingress

**ON-PREMISES:**

- Use MetalLB for load balancing
- Configure local storage provisioners
- Use Ingress NGINX
- Implement manual scaling policies

### **K8s DEPLOYMENT STRATEGY IMPLEMENTATIONS:**

**ROLLING DEPLOYMENT (DEFAULT):**

```bash
# Simple rolling deployment using kubectl
kubectl apply -f k8s-manifests/
kubectl rollout status deployment/{app-name}
kubectl get pods -l app={app-name}
```

**BLUE-GREEN DEPLOYMENT:**

```bash
# Simple blue-green deployment
kubectl apply -f k8s-manifests/green/
kubectl get deployment {app-name}-green
# Switch service selector from blue to green
kubectl patch service {app-name} -p '{"spec":{"selector":{"version":"green"}}}'
```

**CANARY DEPLOYMENT:**

```bash
# Simple canary deployment
kubectl apply -f k8s-manifests/canary/
kubectl scale deployment {app-name}-canary --replicas=1
# Monitor and scale up based on metrics
```

### **K8s SECURITY VALIDATION:**

**POD SECURITY STANDARDS:**

```yaml
# Simple Pod Security Context
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000

# Simple Container Security Context
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

**NETWORK POLICIES:**

```yaml
# Simple default-deny network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

### **K8s MONITORING SETUP:**

**PROMETHEUS INTEGRATION:**

```yaml
# Simple ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: { app-name }
spec:
  selector:
    matchLabels:
      app: { app-name }
  endpoints:
    - port: metrics
      interval: 30s
```

**BASIC ALERTING:**

```yaml
# Simple PrometheusRule
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: {app-name}-alerts
spec:
  groups:
  - name: {app-name}
    rules:
    - alert: ApplicationDown
      expr: up{job="{app-name}"} == 0
      for: 5m
```

### **K8s IMPLEMENTATION DELIVERABLES - EXECUTION ARTIFACTS ONLY:**

**MANDATORY K8s DEPLOYMENT OUTPUT FILES - NO DOCUMENTATION:**

1. **Kubernetes Cluster Validated** - Cluster connectivity and permissions verified
2. **Container Images Built and Pushed** - Application images in container registry
3. **Kubernetes Resources Applied** - Deployments, services, configmaps, secrets deployed
4. **Pod Health Status Confirmed** - All pods running and ready
5. **Service Connectivity Verified** - Internal and external service accessibility
6. **Monitoring Stack Deployed** - Prometheus, Grafana, and alerting active
7. **Security Policies Applied** - Pod Security Standards and network policies enforced
8. **Rollback Capability Tested** - Previous deployment versions available for rollback

**FORBIDDEN DELIVERABLES:**

- No documentation files (.md files)
- No quickstart deployment guides
- No lifecycle management guides
- No Terraform infrastructure guides
- No monitoring configuration guides
- No setup or tutorial documentation

### **K8s ROLLBACK PROCEDURES:**

**SIMPLE K8s ROLLBACK COMMANDS:**

```bash
# Rolling deployment rollback
kubectl rollout undo deployment/{app-name}
kubectl rollout status deployment/{app-name}

# Blue-green rollback
kubectl patch service {app-name} -p '{"spec":{"selector":{"version":"blue"}}}'

# Canary rollback
kubectl scale deployment {app-name}-canary --replicas=0
```

### **K8s TROUBLESHOOTING:**

**BASIC K8s DEBUGGING COMMANDS:**

```bash
# Check K8s deployment status
kubectl get deployments
kubectl describe deployment {app-name}

# Check K8s pod status
kubectl get pods -l app={app-name}
kubectl describe pod {pod-name}
kubectl logs {pod-name}

# Check K8s service connectivity
kubectl get services
kubectl describe service {app-name}

# Check K8s ingress configuration
kubectl get ingress
kubectl describe ingress {app-name}

# Check K8s events
kubectl get events --sort-by='.lastTimestamp'
```

### **NEXT PHASE K8s MONITORING:**

After successful K8s deployment, monitor using K8s tools:

```bash
# Basic K8s monitoring commands
kubectl top pods -l app={app-name}
kubectl top nodes
kubectl get events --sort-by='.lastTimestamp'

# Simple K8s health checks
curl -f http://{service-endpoint}/health
kubectl exec -it {pod-name} -- wget -qO- http://localhost:8080/health
```

---

**ENFORCEMENT:** This command performs KUBERNETES DEPLOYMENT EXECUTION ONLY through the MCP prompt protocol with STRICT adherence to Kubernetes best practices and security standards. The comprehensive K8s deployment logic is defined in `deployments-k8s-deploy-prompt.yaml` and executed according to Model Context Protocol standards. All implementations must follow Kubernetes best practices, security standards, and established patterns. Use `/deployments-planning` for comprehensive planning before K8s implementation. Focus on production-ready K8s deployment execution with proper timestamp documentation and reverse date stamp requirements.
