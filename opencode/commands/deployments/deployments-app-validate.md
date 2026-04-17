# === Generic Application Deployment Validation: Comprehensive Post-Deployment Verification Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the validation requirements and understand what needs to be verified
2. Plan your approach and identify critical validation points
3. Consider the implications of failures and edge cases
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

- Claiming "100% success" without thorough validation
- Ignoring errors in logs or health checks
- Skipping critical validation phases
- Proceeding with incomplete validation
- Marking deployment as successful when issues exist
- Using superficial checks instead of deep validation
- Declaring success based on container status alone

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO FALSE POSITIVES** - every issue must be caught and reported
- **NO OPTIMISTIC REPORTING** - be paranoid and thorough
- **NO SHORTCUTS** - run all validation phases completely
- **NO ASSUMPTIONS** - verify everything explicitly
- **NO PARTIAL VALIDATION** - complete all phases
- **NO IGNORING WARNINGS** - investigate all anomalies
- **NO SKIPPING LOGS** - analyze all log output thoroughly
- **NO SUCCESS CLAIMS** - unless EVERY check passes

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MANDATORY STRUCTURE DOCUMENT:**
   - Read `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` thoroughly
   - Understand the deployment structure to validate against
   - Verify application structure compliance

2. **READ VALIDATION CHECKLIST:**
   - Read `.claude/commands/deployments/VALIDATION-CHECKLIST.md`
   - Understand all validation requirements
   - Follow comprehensive validation procedures

3. **READ PROJECT DOCUMENTATION:**
   - Check `./docs` directory thoroughly
   - Review deployment documentation
   - Understand application architecture
   - Study health check requirements
   - Review API endpoint documentation

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to comprehensive validation requirements.

### **VALIDATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR COMPREHENSIVE POST-DEPLOYMENT VALIDATION ONLY:**

- **MUST:** Perform exhaustive validation of deployed applications
- **MUST:** Catch ALL deployment issues and failures
- **MUST:** Validate container/service health and stability
- **MUST:** Test all API endpoints and functionality
- **MUST:** Analyze logs for errors, warnings, and anomalies
- **MUST:** Verify service connectivity and integrations
- **MUST:** Execute smoke tests and end-to-end workflows
- **MUST:** Generate comprehensive validation reports
- **MUST:** Be STRICT and PARANOID - mark as FAIL at any significant issue
- **FORBIDDEN:** Claiming success when issues exist
- **FORBIDDEN:** Superficial or incomplete validation
- **FORBIDDEN:** Ignoring errors, warnings, or anomalies

**STRICT VALIDATION CRITERIA (ANY OF THESE = FAIL):**

- Any ERROR, CRITICAL, or FATAL message in logs
- Any CrashLoopBackOff or failing container
- Any failing health check endpoint
- Any 500 error from API endpoints
- Any missing required resource or service
- Any security policy violation
- Any resource limit exceeded
- Any persistent restart cycles
- Any connectivity failures

### **MANDATORY REPOSITORY STRUCTURE REFERENCE:**

**BEFORE EXECUTING**, you MUST understand the repository structure being validated:

1. **READ**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` for complete deployment structure
2. **UNDERSTAND**: Deployment architecture and expected components
3. **VALIDATE**: Against canonical structure requirements
4. **REFERENCE**: VALIDATION-CHECKLIST.md for validation requirements

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-app-validate-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for deployment_target, platform, endpoints, validation_depth
3. **FOLLOW PROTOCOL**: Execute all validation phases according to comprehensive validation specifications
4. **BE PARANOID**: Treat every anomaly as a potential critical issue
5. **DOCUMENT RESULTS**: Create comprehensive validation reports with all findings
6. **VERIFY COMPLETION**: Confirm 100% validation completeness achieved and accurate PASS/FAIL determination

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "generic-app-deployment-validation-prompt"
arguments:
  deployment_target: "[application or service name that was deployed]"
  platform: "[docker|docker-compose|cloud|local]"
  health_endpoints: "[optional: comma-separated health endpoints like /health,/ready,/live]"
  api_endpoints: "[optional: comma-separated API endpoints to validate]"
  validation_depth: "[basic|standard|comprehensive|paranoid]" # Default: standard
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments
- [ ] ALL validation phases completed (no skipping)
- [ ] Container/service status fully verified
- [ ] Health endpoints validated (200 OK, consistent responses)
- [ ] API functionality thoroughly tested
- [ ] Service connectivity confirmed
- [ ] Logs analyzed for errors and warnings (ZERO critical issues)
- [ ] Smoke tests executed successfully
- [ ] Performance baseline measured
- [ ] Comprehensive validation report generated with all findings
- [ ] Accurate PASS/FAIL determination (STRICT criteria applied)
- [ ] Remediation steps provided for ALL issues found

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

### **VALIDATION PHASES:**

**PHASE 1: Container/Service Status Validation**
- Check container status (running, healthy, restart count)
- Verify all expected containers are present
- Check container resource usage (CPU, memory)
- Validate container logs for errors and warnings
- Check for crash loops or restart cycles
- Measure time since last restart
- Verify container image versions

**PHASE 2: Health Endpoint Validation**
- Test health endpoints (/health, /ready, /live)
- Verify response codes (MUST be 200, not 404/500)
- Check response times (< 1000ms acceptable threshold)
- Validate health endpoint payload structure
- Test multiple times to ensure consistency (minimum 5 attempts)
- Verify health check dependencies (database, cache, external services)

**PHASE 3: API Functionality Validation**
- Test critical API endpoints with real requests
- Verify authentication/authorization works correctly
- Check API response formats and data integrity
- Test error handling (404, 400, 500 responses)
- Validate API rate limiting if configured
- Test API versioning and backwards compatibility
- Verify CORS configuration if applicable

**PHASE 4: Service Connectivity Validation**
- Test inter-service communication
- Validate database connections and query execution
- Check external service integrations
- Verify message queue connections and message processing
- Test cache connectivity (Redis, Memcached)
- Validate DNS resolution
- Test network policies and firewall rules

**PHASE 5: Log Analysis (CRITICAL PHASE)**
- Search logs for ERROR, CRITICAL, FATAL, PANIC messages
- Check for stack traces or exceptions
- Validate expected startup messages are present
- Check for configuration errors
- Analyze warning messages for potential issues
- Verify no security-related errors
- Check for resource exhaustion warnings
- Look for timeout or connection errors

**PHASE 6: Smoke Testing**
- Execute basic end-to-end workflows
- Test core functionality paths
- Validate data persistence
- Check background jobs/workers
- Test scheduled tasks if applicable
- Verify file upload/download functionality
- Test user authentication flows

**PHASE 7: Performance Baseline**
- Measure response times for key endpoints (p50, p95, p99)
- Check resource utilization baselines (CPU, memory, disk, network)
- Validate throughput capacity
- Test concurrent request handling (10, 50, 100 concurrent)
- Measure database query performance
- Check cache hit rates

**PHASE 8: Comprehensive Reporting and Remediation**
- Generate comprehensive validation report with ALL findings
- Document all issues found with severity levels:
  - CRITICAL: Deployment is broken, immediate action required
  - HIGH: Significant issues that impact functionality
  - MEDIUM: Issues that should be addressed soon
  - LOW: Minor issues or optimizations
- Provide detailed remediation steps for EACH issue:
  - Clear description of the problem
  - Root cause analysis
  - Step-by-step fix instructions
  - Commands to resolve (docker/kubectl/cloud CLI)
  - Prevention recommendations
- Create rollback recommendation if needed
- Mark deployment as **PASS** or **FAIL** (be STRICT!)

**FAIL CRITERIA (ANY OF THESE = AUTOMATIC FAIL):**

- ANY error in logs (unless explicitly acknowledged and acceptable)
- ANY container restart cycle (CrashLoopBackOff, repeated restarts)
- ANY failing health check (non-200 response)
- ANY 500 error from API endpoints
- ANY missing required resource or dependency
- ANY security configuration error
- ANY persistent connectivity failure
- ANY data corruption or persistence issue
- ANY performance degradation beyond acceptable thresholds

### **VALIDATION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY VALIDATION OUTPUTS:**

1. **`./project/docs/deployments/Validation_Report-{{YYYY-MM-DD-HHMMSS}}.md`** - Comprehensive validation report with all findings, severity levels, and pass/fail determination
2. **`./project/docs/deployments/Validation_Results-{{YYYY-MM-DD-HHMMSS}}.json`** - Structured JSON results for automated processing
3. **`./project/docs/deployments/Remediation_Steps-{{YYYY-MM-DD-HHMMSS}}.md`** - Detailed remediation steps for ALL issues found (only if issues exist)

**REPORT STRUCTURE:**

```markdown
# Application Deployment Validation Report
**Deployment Target:** {{deployment_target}}
**Platform:** {{platform}}
**Validation Timestamp:** {{YYYY-MM-DD HH:MM:SS UTC}}
**Validation Depth:** {{validation_depth}}
**Overall Result:**  PASS /  FAIL

## Executive Summary
[Clear summary of validation results, key findings, and overall deployment health]

## Validation Phases

### Phase 1: Container/Service Status Validation
- **Status:**  PASS /  FAIL
- **Findings:**
  - [Detailed findings with evidence]

### Phase 2: Health Endpoint Validation
- **Status:**  PASS /  FAIL
- **Findings:**
  - [Health check results, response times, consistency]

[... All 8 phases ...]

## Issues Found

### CRITICAL Issues
[List all critical issues with full details]

### HIGH Priority Issues
[List all high priority issues]

### MEDIUM Priority Issues
[List all medium priority issues]

### LOW Priority Issues
[List all low priority issues]

## Recommendations

### Immediate Actions Required
[Critical actions that must be taken now]

### Short-term Improvements
[Improvements to implement within days]

### Long-term Optimizations
[Strategic improvements for future iterations]

## Rollback Decision
**Recommendation:** [ROLLBACK IMMEDIATELY / MONITOR CLOSELY / PROCEED WITH CONFIDENCE]
**Justification:** [Clear reasoning for recommendation]

## Appendix
- Container logs excerpts
- API test results
- Performance metrics
- Configuration validation
```

### **NEXT PHASE PREPARATION:**

```bash
# If validation FAILS, execute rollback immediately:
docker-compose down && docker-compose up -d  # For Docker Compose
kubectl rollout undo deployment/{{name}}     # For Kubernetes

# If validation PASSES, proceed with confidence
# Document the successful deployment and move to production (if staging)
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE POST-DEPLOYMENT VALIDATION ONLY through the MCP prompt protocol. Be PARANOID and THOROUGH, not optimistic. Any significant issue = FAIL. The validation logic is defined in `deployments-app-validate-prompt.yaml` and executed according to Model Context Protocol standards. This command NEVER claims success unless EVERY check passes completely. Generate detailed remediation steps for ALL issues found. Use STRICT pass/fail criteria to prevent false positives.
