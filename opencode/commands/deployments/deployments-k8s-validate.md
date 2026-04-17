# === Kubernetes Deployment Validation: Comprehensive Post-Deployment Verification Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the Kubernetes validation requirements and understand what needs to be verified
2. Plan your approach and identify critical validation points specific to K8s
3. Consider the implications of failures, security issues, and edge cases
4. Only then proceed with the actual validation execution

**This thinking requirement is MANDATORY and must be followed for every validation action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance-prompt.md`
2. **READ AND COMPLY**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md`
3. **VERIFY**: User has given explicit permission to proceed
4. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance-prompt.md requirements and DEPLOYMENT-STRUCTURE.md compliance, and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification and mandatory structure adherence

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Claiming "100% successful deployment" without thorough K8s validation
- Ignoring pod restarts, errors, or CrashLoopBackOff states
- Skipping security validation or network policy checks
- Proceeding with incomplete Kubernetes resource validation
- Marking deployment as successful when pods are failing
- Using superficial checks instead of deep K8s-specific validation
- Declaring success based on deployment status alone without pod verification

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO FALSE POSITIVES** - every K8s issue must be caught and reported
- **NO OPTIMISTIC REPORTING** - be paranoid about pod states and resource status
- **NO SHORTCUTS** - validate all Kubernetes resources completely
- **NO ASSUMPTIONS** - verify every K8s object explicitly
- **NO PARTIAL VALIDATION** - complete all K8s-specific phases
- **NO IGNORING POD ISSUES** - any CrashLoopBackOff = FAIL
- **NO SKIPPING SECURITY** - validate Pod Security Standards compliance
- **NO SUCCESS CLAIMS** - unless EVERY K8s resource is healthy

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MANDATORY STRUCTURE DOCUMENT:**
   - Read `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` thoroughly
   - Understand the Kubernetes deployment structure
   - Verify application structure compliance

2. **READ VALIDATION CHECKLIST:**
   - Read `.claude/commands/deployments/VALIDATION-CHECKLIST.md`
   - Understand all K8s-specific validation requirements
   - Follow comprehensive Kubernetes validation procedures

3. **READ PROJECT DOCUMENTATION:**
   - Check `./docs` directory thoroughly
   - Review Kubernetes deployment documentation
   - Understand application architecture and K8s manifests
   - Study health check and probe requirements
   - Review service mesh configuration if applicable

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to comprehensive Kubernetes validation requirements.

### **VALIDATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR COMPREHENSIVE KUBERNETES POST-DEPLOYMENT VALIDATION ONLY:**

- **MUST:** Perform exhaustive validation of Kubernetes deployments
- **MUST:** Catch ALL K8s deployment issues and failures
- **MUST:** Validate pod health, readiness, and liveness
- **MUST:** Test all Kubernetes services and ingress configurations
- **MUST:** Analyze pod logs for errors, warnings, and anomalies
- **MUST:** Verify all K8s resource status (ConfigMaps, Secrets, PVCs, etc.)
- **MUST:** Execute integration tests within cluster
- **MUST:** Validate security policies and RBAC
- **MUST:** Generate comprehensive validation reports
- **MUST:** Be VERY STRICT - mark as FAIL at any K8s issue
- **FORBIDDEN:** Claiming success when any pod is failing
- **FORBIDDEN:** Superficial or incomplete K8s validation
- **FORBIDDEN:** Ignoring CrashLoopBackOff, ImagePullBackOff, or Error states

**STRICT KUBERNETES VALIDATION CRITERIA (ANY OF THESE = FAIL):**

- ANY pod not in Running state (Pending, CrashLoopBackOff, Error, ImagePullBackOff)
- ANY pod restart count > 0 in last 10 minutes
- ANY ERROR, CRITICAL, or FATAL message in pod logs
- ANY failing liveness or readiness probe
- ANY Service without valid endpoints
- ANY PersistentVolumeClaim not in Bound status
- ANY security policy violation
- ANY RBAC permission error
- ANY Ingress configuration error
- ANY resource limit exceeded or OOMKilled pod

### **MANDATORY REPOSITORY STRUCTURE REFERENCE:**

**BEFORE EXECUTING**, you MUST understand the Kubernetes deployment structure being validated:

1. **READ**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` for complete K8s deployment structure
2. **UNDERSTAND**: apps/, infrastructure/, clusters/, gitops/ structure
3. **VALIDATE**: Against canonical Kubernetes deployment requirements
4. **REFERENCE**: VALIDATION-CHECKLIST.md for K8s-specific validation requirements

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-k8s-validate-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for deployment_name, namespace, k8s_platform, validation_depth
3. **FOLLOW PROTOCOL**: Execute all K8s validation phases according to comprehensive specifications
4. **BE VERY STRICT**: Treat every K8s anomaly as a potential critical issue
5. **DOCUMENT RESULTS**: Create comprehensive validation reports with all K8s findings
6. **VERIFY COMPLETION**: Confirm 100% validation completeness and accurate PASS/FAIL determination

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "kubernetes-deployment-validation-prompt"
arguments:
  deployment_name: "[name of the deployment to validate]"
  namespace: "[Kubernetes namespace where deployment exists]"
  k8s_platform: "[k8s|docker-desktop|minikube|kind|aws-eks|azure-aks|gcp-gke|on-premises]"
  service_name: "[optional: service name for connectivity testing]"
  ingress_host: "[optional: ingress hostname for external testing]"
  validation_depth: "[basic|standard|comprehensive|paranoid]" # Default: comprehensive
  run_integration_tests: "[true|false]" # Default: true
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments
- [ ] ALL K8s validation phases completed (12 phases total)
- [ ] Pod status fully verified (ALL Running, 0 restarts)
- [ ] Pod logs analyzed (ZERO critical issues)
- [ ] Service and Ingress validated and tested
- [ ] ConfigMap and Secret validation confirmed
- [ ] All K8s resources status verified (PVC Bound, HPA active, etc.)
- [ ] Rollout status confirmed successful
- [ ] Health and readiness probes all passing
- [ ] API endpoints tested from within cluster
- [ ] Security validation completed (Pod Security Standards, NetworkPolicies, RBAC)
- [ ] Monitoring integration verified (ServiceMonitor, Prometheus)
- [ ] Integration tests executed successfully
- [ ] Comprehensive validation report generated with all findings
- [ ] Accurate PASS/FAIL determination (VERY STRICT criteria applied)
- [ ] Kubectl remediation commands provided for ALL issues found

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL VALIDATION OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] Validation report has reverse date stamp in filename
- [ ] Results JSON file has proper timestamp
- [ ] Remediation steps document includes timestamp
- [ ] All validation artifacts follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating validation files without proper reverse date stamps
- Using inconsistent date formats within same validation session
- Missing timestamps in validation documentation

### **KUBERNETES VALIDATION PHASES:**

**PHASE 1: Pod Status Validation**
- Check ALL pods are Running (not Pending, CrashLoopBackOff, Error, ImagePullBackOff)
- Verify pod restart counts (MUST be 0 or minimal and stable)
- Check pod readiness and liveness probe status (all passing)
- Validate pod resource requests and limits are defined
- Check for OOMKilled or Evicted pods
- Verify correct number of replicas are running (desired = current = ready)
- Validate pod scheduling (no unschedulable pods)
- Check pod conditions (PodScheduled, Initialized, ContainersReady, Ready)

**PHASE 2: Pod Log Analysis**
- Retrieve logs from ALL pods in the deployment
- Search for ERROR, CRITICAL, FATAL, PANIC messages
- Check for stack traces and exceptions
- Validate expected startup messages are present
- Check init container logs (if present)
- Analyze sidecar container logs (service mesh, logging, monitoring)
- Detect configuration errors or missing environment variables
- Check for security-related errors (auth failures, permission denied)
- Verify no resource exhaustion warnings

**PHASE 3: Service and Ingress Validation**
- Verify Service has valid endpoints (kubectl get endpoints)
- Check Service selector matches pod labels exactly
- Test Service port accessibility from within cluster
- Validate Service type (ClusterIP, NodePort, LoadBalancer)
- Test Ingress configuration and routing rules
- Verify Ingress backend services are correct
- Test external access through Ingress (if applicable)
- Check TLS certificate validity (if HTTPS)
- Validate Ingress annotations (nginx, traefik, etc.)

**PHASE 4: ConfigMap and Secret Validation**
- Verify ConfigMaps exist and are mounted correctly in pods
- Check Secret volumes are present and accessible
- Validate environment variables from ConfigMaps/Secrets are set
- Check for missing or misconfigured values
- Verify no secrets are exposed in logs or environment
- Test ConfigMap/Secret updates are propagated (if applicable)

**PHASE 5: Resource Status Validation**
- Check PersistentVolumeClaim status (MUST be Bound, not Pending/Lost)
- Verify PVC storage usage and capacity
- Check HorizontalPodAutoscaler status and metrics
- Validate VerticalPodAutoscaler recommendations (if used)
- Check NetworkPolicy configuration and enforcement
- Verify ServiceAccount and RBAC permissions
- Check ResourceQuota and LimitRange compliance
- Validate PodDisruptionBudget configuration

**PHASE 6: Rollout Status Validation**
- Verify Deployment rollout completed successfully
- Check ReplicaSet status (old vs new)
- Validate no ongoing rollbacks
- Check rollout history (kubectl rollout history)
- Verify desired vs actual replica count
- Check deployment strategy (RollingUpdate settings)
- Validate maxSurge and maxUnavailable configuration
- Check rollout annotations and status messages

**PHASE 7: Health and Readiness Probes**
- Test liveness probe endpoints from within pods
- Test readiness probe endpoints from within pods
- Verify probe configurations are correct (path, port, headers)
- Check probe success rates (must be 100%)
- Test startup probes if defined
- Validate probe timing (initialDelaySeconds, periodSeconds, timeoutSeconds)
- Check failureThreshold and successThreshold values
- Verify probes are not causing false positives

**PHASE 8: API Endpoint Testing (from within cluster)**
- Create test pod in same namespace for testing
- Test internal service communication (ClusterIP)
- Validate API endpoints functionality via Service DNS
- Test inter-pod networking
- Check DNS resolution (service.namespace.svc.cluster.local)
- Validate service mesh routing (if Istio/Linkerd/Consul)
- Test load balancing across pod replicas
- Clean up test pod after validation

**PHASE 9: Security Validation**
- Verify Pod Security Standards compliance (Baseline or Restricted)
- Check container security contexts (runAsNonRoot, readOnlyRootFilesystem)
- Validate NetworkPolicies are in effect (default-deny recommended)
- Check RBAC permissions are correct and least-privilege
- Verify no privileged containers are running
- Check capabilities are dropped appropriately
- Validate seccomp and AppArmor profiles (if configured)
- Check image pull secrets and registry authentication

**PHASE 10: Monitoring and Observability**
- Check ServiceMonitor is created and active (Prometheus Operator)
- Verify Prometheus is scraping metrics from pods
- Check metric endpoints are accessible (/metrics)
- Verify Grafana dashboard availability (if configured)
- Validate log forwarding to aggregation system (if configured)
- Test alerting rules if configured (PrometheusRule)
- Check distributed tracing integration (Jaeger/Zipkin if configured)
- Validate custom metrics for HPA (if configured)

**PHASE 11: Integration Testing**
- Test database connectivity from pods (if applicable)
- Verify external service integrations (APIs, webhooks)
- Test message queue connections (Kafka, RabbitMQ, Redis)
- Validate cache connectivity (Redis, Memcached)
- Check S3/blob storage access (if applicable)
- Test service mesh mTLS (if Istio/Linkerd)
- Validate cross-namespace communication (if required)
- Execute end-to-end workflow tests

**PHASE 12: Reporting and Remediation**
- Generate comprehensive validation report with timestamps
- Document ALL issues found (categorize by severity: CRITICAL, HIGH, MEDIUM, LOW)
- Provide kubectl commands for remediation for EACH issue
- Create detailed rollback plan if needed (kubectl rollout undo)
- Mark deployment as **PASS** or **FAIL** (be VERY STRICT!)
- Include performance metrics and resource usage
- Provide security remediation steps
- Generate automated remediation scripts if possible

**FAIL CRITERIA (ANY OF THESE = AUTOMATIC FAIL):**

- ANY pod not in Running state
- ANY pod with restart count > 0 in last 10 minutes
- ANY error in pod logs (unless explicitly acknowledged and acceptable)
- ANY failing health check (liveness or readiness probe)
- ANY Service without endpoints
- ANY PVC not in Bound status
- ANY security policy violation (Pod Security Standards, NetworkPolicy)
- ANY RBAC permission error
- ANY Ingress configuration error
- ANY OOMKilled or Evicted pod
- ANY integration test failure

### **VALIDATION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY KUBERNETES VALIDATION OUTPUTS:**

1. **`./project/docs/deployments/K8s_Validation_Report-{{YYYY-MM-DD-HHMMSS}}.md`** - Comprehensive K8s validation report with all findings, kubectl remediation commands, and pass/fail determination
2. **`./project/docs/deployments/K8s_Validation_Results-{{YYYY-MM-DD-HHMMSS}}.json`** - Structured JSON results for automated processing and CI/CD integration
3. **`./project/docs/deployments/K8s_Remediation_Steps-{{YYYY-MM-DD-HHMMSS}}.md`** - Detailed kubectl remediation commands and step-by-step fix instructions for ALL issues found (only if issues exist)

**REPORT STRUCTURE:**

```markdown
# Kubernetes Deployment Validation Report
**Deployment Name:** {{deployment_name}}
**Namespace:** {{namespace}}
**K8s Platform:** {{k8s_platform}}
**Validation Timestamp:** {{YYYY-MM-DD HH:MM:SS UTC}}
**Validation Depth:** {{validation_depth}}
**Overall Result:**  PASS /  FAIL

## Executive Summary
[Clear summary of K8s validation results, critical findings, and overall deployment health]

## Kubernetes Resource Status
- **Deployment:** {{status}}
- **ReplicaSets:** {{count}} ({{desired}} desired, {{current}} current, {{ready}} ready)
- **Pods:** {{count}} ({{running}}/{{pending}}/{{failed}})
- **Services:** {{count}} ({{with_endpoints}}/{{total}})
- **Ingress:** {{count}} ({{healthy}}/{{total}})
- **PVCs:** {{count}} ({{bound}}/{{total}})
- **ConfigMaps:** {{count}}
- **Secrets:** {{count}}

## Validation Phases

### Phase 1: Pod Status Validation
- **Status:**  PASS /  FAIL
- **Pod States:**
  - Running: {{count}}
  - Pending: {{count}}
  - CrashLoopBackOff: {{count}}
  - Error: {{count}}
- **Restart Counts:** [pod-name: {{count}}]
- **Findings:**
  - [Detailed findings with kubectl output]

### Phase 2: Pod Log Analysis
- **Status:**  PASS /  FAIL
- **Errors Found:** {{count}}
- **Warnings Found:** {{count}}
- **Findings:**
  - [Log analysis results with excerpts]

[... All 12 phases ...]

## Issues Found

### CRITICAL Issues (Deployment Breaking)
[List all critical K8s issues with kubectl commands to fix]

### HIGH Priority Issues (Functionality Impacted)
[List all high priority issues]

### MEDIUM Priority Issues (Should Address Soon)
[List all medium priority issues]

### LOW Priority Issues (Minor Optimizations)
[List all low priority issues]

## Kubectl Remediation Commands

### Immediate Actions (Execute Now)
```bash
# Fix CrashLoopBackOff pods
kubectl delete pod {{pod-name}} -n {{namespace}}

# Rollback deployment if needed
kubectl rollout undo deployment/{{deployment-name}} -n {{namespace}}

# Scale down and up to force recreation
kubectl scale deployment/{{deployment-name}} --replicas=0 -n {{namespace}}
kubectl scale deployment/{{deployment-name}} --replicas=3 -n {{namespace}}
```

### Security Remediations
```bash
# Apply network policies
kubectl apply -f infrastructure/security/network-policies/

# Update Pod Security Standards
kubectl label namespace {{namespace}} pod-security.kubernetes.io/enforce=restricted
```

### Resource Fixes
```bash
# Fix PVC issues
kubectl get pvc -n {{namespace}}
kubectl describe pvc {{pvc-name}} -n {{namespace}}

# Update ConfigMaps
kubectl apply -f apps/base/{{service}}/configmap.yaml
kubectl rollout restart deployment/{{deployment-name}} -n {{namespace}}
```

## Rollback Decision
**Recommendation:** [ROLLBACK IMMEDIATELY / MONITOR CLOSELY / PROCEED WITH CONFIDENCE]
**Rollback Command:** `kubectl rollout undo deployment/{{deployment-name}} -n {{namespace}}`
**Justification:** [Clear reasoning for recommendation]

## Monitoring and Alerting
- ServiceMonitor Status: {{status}}
- Prometheus Scraping: {{status}}
- Alert Rules Active: {{count}}
- Grafana Dashboard: {{url}}

## Security Compliance
- Pod Security Standard: {{standard}} (Baseline/Restricted)
- NetworkPolicies Active: {{count}}
- RBAC Configured: {{status}}
- Secrets Management: {{method}}

## Performance Metrics
- Average Response Time: {{ms}}
- Resource Usage: CPU {{%}}, Memory {{%}}
- HPA Status: {{current}}/{{desired}} replicas
- Error Rate: {{%}}

## Appendix
### Pod Logs Excerpts
[Critical log entries from all pods]

### Kubectl Describe Output
[Key resource descriptions]

### Integration Test Results
[Test execution results]
```

### **NEXT PHASE PREPARATION:**

```bash
# If validation FAILS, execute immediate rollback:
kubectl rollout undo deployment/{{deployment-name}} -n {{namespace}}

# Verify rollback
kubectl rollout status deployment/{{deployment-name}} -n {{namespace}}

# If validation PASSES, proceed with confidence
# Document the successful deployment
# Proceed to production (if this was staging)
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE KUBERNETES POST-DEPLOYMENT VALIDATION ONLY through the MCP prompt protocol. Be VERY STRICT and PARANOID about Kubernetes resource states. Any pod not Running = FAIL. Any error in logs = FAIL. Any security violation = FAIL. The validation logic is defined in `deployments-k8s-validate-prompt.yaml` and executed according to Model Context Protocol standards. This command NEVER claims success unless EVERY Kubernetes resource is healthy and EVERY check passes completely. Generate detailed kubectl remediation commands for ALL issues found. Use VERY STRICT pass/fail criteria to prevent false positives.
