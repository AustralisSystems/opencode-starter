# Post-Deployment Validation Commands Summary

**Created:** 2025-10-02
**Version:** 1.0.0
**Purpose:** Comprehensive post-deployment validation to prevent false "100% successful deployment" claims

---

## Overview

These validation command pairs provide **thorough, paranoid-level post-deployment validation** to catch real deployment issues that have been missed in the past. Both commands use **STRICT pass/fail criteria** and will FAIL at any significant issue.

### Critical Philosophy

**NEVER claim "100% successful deployment" unless EVERY validation check passes completely.**

- Be PARANOID, not optimistic
- ANY error = potential FAIL
- Catch ALL issues, warnings, and anomalies
- Generate detailed remediation steps for EVERY issue found
- Use strict pass/fail criteria to prevent false positives

---

## Command Pair 1: Generic App Deployment Validation

### Files Created

1. **`deployments-app-validate.md`** - Documentation and execution instructions
2. **`deployments-app-validate-prompt.yaml`** - MCP prompt with validation protocol

### Purpose

Validate generic application deployments including:
- Docker containers
- Docker Compose stacks
- Basic cloud applications
- Local deployments

### Key Validation Phases (8 Total)

#### Phase 1: Container/Service Status Validation
- Container status (running, healthy, restart count)
- All expected containers present
- Resource usage (CPU, memory)
- Container logs for errors
- Crash loops or restart cycles
- Image versions

#### Phase 2: Health Endpoint Validation
- Test health endpoints (/health, /ready, /live)
- Verify 200 OK responses (5 attempts minimum)
- Response times < 1000ms
- Payload structure validation
- Consistency across attempts

#### Phase 3: API Functionality Validation
- Test critical API endpoints
- Authentication/authorization
- Response formats and data integrity
- Error handling (404, 400, 500)
- Rate limiting validation
- CORS configuration

#### Phase 4: Service Connectivity Validation
- Inter-service communication
- Database connections and queries
- External service integrations
- Message queue connectivity
- Cache connectivity (Redis, Memcached)
- DNS resolution

#### Phase 5: Log Analysis (CRITICAL)
- Search for ERROR, CRITICAL, FATAL, PANIC
- Stack traces or exceptions
- Expected startup messages
- Configuration errors
- Security-related errors
- Resource exhaustion warnings
- Timeout or connection errors

#### Phase 6: Smoke Testing
- End-to-end workflows
- Core functionality paths
- Data persistence (CRUD operations)
- Background jobs/workers
- Scheduled tasks
- Authentication flows

#### Phase 7: Performance Baseline
- Response times (p50, p95, p99)
- Resource utilization baselines
- Throughput capacity
- Concurrent request handling (10, 50, 100)
- Database query performance
- Cache hit rates

#### Phase 8: Comprehensive Reporting
- Generate validation report
- Categorize issues (CRITICAL, HIGH, MEDIUM, LOW)
- Detailed remediation steps for EACH issue
- Rollback recommendation
- STRICT PASS/FAIL determination

### Arguments

```yaml
deployment_target: "[application/service name]"
platform: "[docker|docker-compose|cloud|local]"
health_endpoints: "[optional: /health,/ready,/live]"
api_endpoints: "[optional: /api/users,/api/products]"
validation_depth: "[basic|standard|comprehensive|paranoid]" # Default: standard
```

### FAIL Criteria (ANY = FAIL)

- ANY ERROR in logs (unless explicitly acceptable)
- ANY container restart cycle
- ANY failing health check (non-200 response)
- ANY 500 error from API
- ANY missing required resource
- ANY connectivity failure
- ANY performance degradation beyond thresholds

### Deliverables

1. **`./project/docs/deployments/Validation_Report-{{YYYY-MM-DD-HHMMSS}}.md`**
   - Executive summary with pass/fail
   - All 8 phases with findings
   - Complete issue list with severity
   - Remediation steps for all issues
   - Rollback recommendation

2. **`./project/docs/deployments/Validation_Results-{{YYYY-MM-DD-HHMMSS}}.json`**
   - Structured results for automation
   - All validation data in JSON format

3. **`./project/docs/deployments/Remediation_Steps-{{YYYY-MM-DD-HHMMSS}}.md`** (if issues found)
   - Issue-by-issue remediation guide
   - Root cause analysis
   - Step-by-step fix instructions
   - Prevention recommendations

---

## Command Pair 2: Kubernetes Deployment Validation

### Files Created

1. **`deployments-k8s-validate.md`** - Documentation and execution instructions
2. **`deployments-k8s-validate-prompt.yaml`** - MCP prompt with K8s validation protocol

### Purpose

Validate Kubernetes deployments with K8s-specific comprehensive checks including:
- K8s (generic)
- Docker Desktop Kubernetes
- Minikube
- Kind
- AWS EKS
- Azure AKS
- GCP GKE
- On-premises clusters

### Key Validation Phases (12 Total)

#### Phase 1: Pod Status Validation
- ALL pods Running (not Pending/CrashLoopBackOff/Error)
- Pod restart counts (0 or stable)
- Readiness and liveness probe status
- Resource requests and limits
- OOMKilled or Evicted pods
- Correct number of replicas
- Pod conditions (PodScheduled, Ready, etc.)

#### Phase 2: Pod Log Analysis
- Logs from ALL pods
- ERROR, CRITICAL, FATAL, PANIC messages
- Stack traces and exceptions
- Init container logs
- Sidecar container logs
- Configuration errors
- Security-related errors

#### Phase 3: Service and Ingress Validation
- Service has valid endpoints
- Service selector matches pod labels
- Service port accessibility
- Ingress configuration
- External access through Ingress
- TLS certificate validity
- Ingress annotations

#### Phase 4: ConfigMap and Secret Validation
- ConfigMaps mounted correctly
- Secrets present and accessible
- Environment variables set
- No missing/misconfigured values
- No secrets exposed in logs

#### Phase 5: Resource Status Validation
- PVC status (Bound, not Pending)
- PVC storage usage
- HPA status and metrics
- NetworkPolicy configuration
- ServiceAccount and RBAC
- ResourceQuota compliance
- PodDisruptionBudget

#### Phase 6: Rollout Status Validation
- Deployment rollout completed
- ReplicaSet status
- No ongoing rollbacks
- Rollout history
- Desired vs actual replicas

#### Phase 7: Health and Readiness Probes
- Liveness probe endpoints
- Readiness probe endpoints
- Probe configurations
- Probe success rates (100%)
- Startup probes
- Probe timing validation

#### Phase 8: API Endpoint Testing (from within cluster)
- Test pod creation in same namespace
- Internal service communication
- API endpoints via Service DNS
- Inter-pod networking
- DNS resolution
- Service mesh routing (if configured)
- Load balancing validation

#### Phase 9: Security Validation
- Pod Security Standards compliance
- Container security contexts
- NetworkPolicies in effect
- RBAC permissions (least-privilege)
- No privileged containers
- Capabilities dropped
- seccomp/AppArmor profiles

#### Phase 10: Monitoring and Observability
- ServiceMonitor created and active
- Prometheus scraping metrics
- Metric endpoints accessible
- Grafana dashboard availability
- Log forwarding (if configured)
- Alerting rules (if configured)
- Distributed tracing (if configured)

#### Phase 11: Integration Testing
- Database connectivity from pods
- External service integrations
- Message queue connections
- Cache connectivity
- S3/blob storage access
- Service mesh mTLS
- Cross-namespace communication
- End-to-end workflows

#### Phase 12: Comprehensive Reporting
- K8s validation report with timestamps
- Issues categorized by severity
- kubectl remediation commands for EACH issue
- Detailed rollback plan
- VERY STRICT PASS/FAIL determination
- Performance metrics
- Security compliance status

### Arguments

```yaml
deployment_name: "[deployment name]"
namespace: "[K8s namespace]"
k8s_platform: "[k8s|docker-desktop|minikube|kind|aws-eks|azure-aks|gcp-gke|on-premises]"
service_name: "[optional: service name]"
ingress_host: "[optional: ingress hostname]"
validation_depth: "[basic|standard|comprehensive|paranoid]" # Default: comprehensive
run_integration_tests: "[true|false]" # Default: true
```

### FAIL Criteria (ANY = FAIL)

- ANY pod not in Running state
- ANY pod restart count > 0 in last 10 minutes
- ANY ERROR in pod logs
- ANY failing liveness/readiness probe
- ANY Service without endpoints
- ANY PVC not in Bound status
- ANY security policy violation
- ANY RBAC permission error
- ANY Ingress configuration error
- ANY OOMKilled or Evicted pod
- ANY integration test failure

### Deliverables

1. **`./project/docs/deployments/K8s_Validation_Report-{{YYYY-MM-DD-HHMMSS}}.md`**
   - Executive summary with K8s pass/fail
   - Kubernetes resource status summary
   - All 12 phases with kubectl evidence
   - Complete issue list with kubectl remediation
   - Security compliance status
   - Monitoring status
   - Rollback decision with kubectl commands
   - Performance metrics
   - Appendix with pod logs and kubectl output

2. **`./project/docs/deployments/K8s_Validation_Results-{{YYYY-MM-DD-HHMMSS}}.json`**
   - Structured K8s results for CI/CD
   - All validation data in JSON format

3. **`./project/docs/deployments/K8s_Remediation_Steps-{{YYYY-MM-DD-HHMMSS}}.md`** (if issues found)
   - Issue-by-issue kubectl remediation
   - Root cause analysis
   - kubectl diagnosis commands
   - kubectl fix commands
   - kubectl verification commands
   - Prevention recommendations

---

## Common Features

### Mandatory Repository Structure Reference

Both commands include:
```yaml
**MANDATORY REPOSITORY STRUCTURE:**
YOU MUST read `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` to understand the canonical Kubernetes deployment structure.
- NO root wrapper directories (no k8s/, deployments/, kubernetes/)
- Use: apps/, infrastructure/, services/, clusters/, gitops/, helm-charts/, ci/, scripts/, docs/, tests/, .templates/
- Reference VALIDATION-CHECKLIST.md for validation requirements
```

### Strict Validation Philosophy

**Both commands enforce:**

1. **Zero Tolerance for Errors**
   - ANY error in logs = FAIL (unless explicitly acceptable)
   - ANY failing health check = FAIL
   - ANY security violation = FAIL

2. **Comprehensive Coverage**
   - ALL logs analyzed
   - ALL endpoints tested
   - ALL resources validated
   - ALL connectivity verified

3. **Detailed Remediation**
   - Every issue documented
   - Root cause analysis provided
   - Step-by-step fix instructions
   - Prevention recommendations

4. **Evidence-Based Reporting**
   - All findings backed by evidence
   - Command output included
   - Metrics and baselines documented
   - Clear rollback recommendations

### Date Stamp Requirements

**ALL validation files use reverse date stamp format: YYYY-MM-DD-HHMMSS**

- Enables chronological sorting
- UTC time for all timestamps
- Consistent format across all deliverables

---

## Usage Examples

### Generic App Validation

```bash
# Basic validation
/deployments-app-validate my-api docker-compose

# Comprehensive validation with endpoints
/deployments-app-validate my-api docker \
  --health-endpoints=/health,/ready \
  --api-endpoints=/api/users,/api/products \
  --validation-depth=comprehensive

# Paranoid validation (maximum scrutiny)
/deployments-app-validate my-api cloud \
  --validation-depth=paranoid
```

### Kubernetes Validation

```bash
# Standard K8s validation
/deployments-k8s-validate my-deployment production k8s

# Comprehensive AWS EKS validation
/deployments-k8s-validate api-gateway production aws-eks \
  --service-name=api-gateway-service \
  --ingress-host=api.example.com \
  --validation-depth=comprehensive

# Paranoid GCP GKE validation with integration tests
/deployments-k8s-validate user-service staging gcp-gke \
  --validation-depth=paranoid \
  --run-integration-tests=true
```

---

## Expected Outcomes

### When Deployment is TRULY Successful

**Generic App Validation:**
-  All containers running with 0 restarts
-  All health checks returning 200 OK consistently
-  All API endpoints responding correctly
-  Zero errors in logs
-  All connectivity validated
-  All smoke tests passing
-  Performance within acceptable thresholds
-  **Result: PASS**

**Kubernetes Validation:**
-  All pods in Running state with 0 restarts
-  All health/readiness probes passing
-  All Services have valid endpoints
-  Zero errors in pod logs
-  All K8s resources in healthy state
-  Security policies compliant
-  Monitoring active and scraping
-  All integration tests passing
-  **Result: PASS**

### When Deployment Has Issues

**Generic App Validation:**
-  Containers restarting (CrashLoopBackOff detected)
-  Health checks failing or inconsistent
-  Errors found in logs
-  API endpoints returning 500 errors
-  Database connectivity issues
-  **Result: FAIL**
-  Detailed remediation steps provided
-  Rollback recommendation: ROLLBACK IMMEDIATELY

**Kubernetes Validation:**
-  Pods in CrashLoopBackOff state
-  Services without endpoints
-  Errors in pod logs
-  PVC not Bound
-  Security policy violations
-  **Result: FAIL**
-  kubectl remediation commands provided
-  Rollback command: `kubectl rollout undo deployment/{{name}} -n {{namespace}}`

---

## Integration with CI/CD

Both validation commands output structured JSON results for CI/CD integration:

```json
{
  "deployment_target": "my-api",
  "platform": "docker-compose",
  "validation_timestamp": "2025-10-02T14:30:00Z",
  "validation_depth": "comprehensive",
  "overall_result": "FAIL",
  "phases": [
    {
      "phase": "Phase 1: Container Status",
      "status": "FAIL",
      "findings": ["Container restarting", "High memory usage"]
    }
  ],
  "issues_found": [
    {
      "severity": "CRITICAL",
      "description": "Container in restart loop",
      "remediation": "Check logs and fix root cause"
    }
  ],
  "performance_metrics": {
    "response_time_p99": "1500ms",
    "cpu_usage": "75%",
    "memory_usage": "85%"
  }
}
```

**CI/CD Pipeline Integration:**

```yaml
# GitHub Actions Example
- name: Validate Deployment
  run: /deployments-app-validate my-api docker-compose

- name: Check Validation Results
  run: |
    RESULT=$(jq -r '.overall_result' ./project/docs/deployments/Validation_Results-*.json)
    if [ "$RESULT" != "PASS" ]; then
      echo "Deployment validation FAILED"
      exit 1
    fi
```

---

## Key Differences from Previous Approaches

### What Makes These Validation Commands Different

1. **Paranoid by Design**
   - Assumes deployment might be broken
   - Validates EVERYTHING, not just surface-level
   - Strict fail criteria (any significant issue = FAIL)

2. **Comprehensive Log Analysis**
   - Analyzes ALL logs thoroughly
   - Searches for errors, warnings, exceptions
   - Catches issues that silent failures hide

3. **Multi-Phase Validation**
   - 8 phases for generic apps
   - 12 phases for Kubernetes
   - Each phase has specific fail criteria

4. **Evidence-Based Reporting**
   - Every finding backed by evidence
   - Command output included
   - Metrics and baselines documented

5. **Actionable Remediation**
   - Step-by-step fix instructions for EVERY issue
   - Specific commands to resolve problems
   - Prevention recommendations

6. **Strict Pass/Fail Determination**
   - Clear, objective criteria
   - No optimistic assumptions
   - Rollback recommendations when needed

---

## Preventing False "100% Success" Claims

### How These Commands Prevent False Positives

1. **Multiple Validation Attempts**
   - Health checks tested 5+ times
   - Ensures consistency, not just one-time success

2. **Deep Log Analysis**
   - Searches for errors, warnings, exceptions
   - Catches issues buried in logs

3. **Real Functionality Testing**
   - Smoke tests execute real workflows
   - API endpoints tested with real requests
   - Database queries executed

4. **Resource State Validation**
   - Verifies actual resource states
   - Checks restart counts, error states
   - Validates resource usage

5. **Connectivity Verification**
   - Tests all service dependencies
   - Validates database connections
   - Checks external integrations

6. **Performance Baseline**
   - Measures actual performance
   - Compares against thresholds
   - Detects degradation

7. **Security Compliance**
   - Validates security policies
   - Checks RBAC permissions
   - Verifies Pod Security Standards

---

## Rollback Procedures

### Generic App Rollback

```bash
# Docker Compose
docker-compose down
docker-compose up -d --force-recreate

# Docker
docker stop {{container}}
docker rm {{container}}
docker run -d {{previous_image}}
```

### Kubernetes Rollback

```bash
# Immediate rollback to previous revision
kubectl rollout undo deployment/{{deployment-name}} -n {{namespace}}

# Rollback to specific revision
kubectl rollout undo deployment/{{deployment-name}} -n {{namespace}} --to-revision={{revision}}

# Verify rollback
kubectl rollout status deployment/{{deployment-name}} -n {{namespace}}

# Check pods after rollback
kubectl get pods -n {{namespace}} -l app={{deployment-name}}
```

---

## Conclusion

These validation command pairs provide **comprehensive, thorough, and paranoid-level post-deployment validation** to ensure deployments are truly successful. They catch real issues that have been missed in the past, preventing false "100% successful deployment" claims.

**Key Takeaways:**

-  Be PARANOID, not optimistic
-  Validate EVERYTHING thoroughly
-  Use STRICT pass/fail criteria
-  Provide detailed remediation for ALL issues
-  Generate evidence-based reports
-  NEVER claim success when issues exist

**Remember:** A deployment is only successful if EVERY validation check passes completely. When in doubt, FAIL and provide remediation steps.
