# N8N Workflow Gap Analysis Command

**YAML Prompt**: `n8n-workflow-gap-analysis-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Comprehensive gap analysis comparing current n8n workflow implementation against requirements, best practices, and modern patterns. This command identifies coverage gaps, missing functionality, and improvement opportunities to ensure complete requirements fulfillment.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n best practices and standards
- `grep` - Production workflow patterns on GitHub
- `sequential-thinking` - Structured gap analysis methodology
- `filesystem` - Workflow and requirements analysis
- `memory` - Track gaps and analysis findings
- `time` - Timestamp analysis activities

**n8n-Specific MCP Tools:**
- `get_workflow_structure` - Workflow coverage analysis
- `compare_with_requirements` - Requirements vs implementation comparison
- `identify_missing_features` - Feature gap identification
- `assess_pattern_compliance` - Best practice gap analysis
- `calculate_coverage_metrics` - Coverage percentage calculation
- `prioritize_gaps` - Gap prioritization by impact

## Gap Analysis Dimensions

### 1. Requirements Coverage

**Functional Requirements:**
- Trigger implementation completeness
- Data transformation coverage
- Integration completeness
- Output delivery fulfillment
- Business logic implementation

**Non-Functional Requirements:**
- Performance requirements met
- Security requirements fulfilled
- Reliability requirements satisfied
- Scalability requirements achieved
- Compliance requirements met

### 2. Feature Completeness

**Core Features:**
- Required workflow triggers
- Essential data transformations
- Critical integrations
- Key output mechanisms
- Core business logic

**Advanced Features:**
- Optional enhancements
- Performance optimizations
- Advanced error handling
- Monitoring and logging
- Extended integrations

### 3. Best Practice Compliance

**n8n Best Practices:**
- Template usage patterns
- Node selection appropriateness
- Expression quality standards
- Error handling patterns
- Performance patterns

**Industry Standards:**
- Automation best practices
- Integration patterns
- Data processing standards
- Security compliance
- Operational excellence

## Gap Classification

### Gap Severity Levels

**Critical Gaps (P0):**
- Missing core functionality
- Security vulnerabilities
- Data loss risks
- Integration failures
- Compliance violations

**High Priority Gaps (P1):**
- Incomplete features
- Performance issues
- Reliability concerns
- Maintainability problems
- Best practice violations

**Medium Priority Gaps (P2):**
- Optional features missing
- Optimization opportunities
- Documentation gaps
- Minor pattern deviations
- Enhancement opportunities

**Low Priority Gaps (P3):**
- Nice-to-have features
- Minor improvements
- Cosmetic enhancements
- Future considerations
- Long-term optimizations

## Analysis Methodology

### Coverage Analysis

**Requirements Traceability:**
```
Requirement  Implementation Mapping
- REQ-001: User Authentication  [Webhook  IF Node  Auth Validation]
- REQ-002: Data Transformation  [HTTP Request  Set Node]
- REQ-003: Error Notification  [MISSING - GAP IDENTIFIED]
```

**Coverage Metrics:**
- Functional coverage: X% of requirements implemented
- Feature coverage: Y% of features complete
- Pattern coverage: Z% of best practices applied
- Security coverage: W% of security requirements met

### Gap Impact Assessment

**Impact Categories:**
- **Business Impact**: Revenue, user experience, compliance
- **Technical Impact**: Performance, security, maintainability
- **Operational Impact**: Support burden, monitoring, deployment
- **Risk Impact**: Data loss, security breach, downtime

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Gap_Analysis_Executive_Summary_YYYY-MM-DD-HHMMSS.ipynb**
   - Overall coverage metrics
   - Critical gaps summary
   - Business impact assessment
   - Investment priorities

2. **Requirements_Coverage_Analysis_YYYY-MM-DD-HHMMSS.ipynb**
   - Requirement-by-requirement analysis
   - Implementation mapping
   - Coverage gaps identified
   - Missing functionality documented

3. **Pattern_Compliance_Assessment_YYYY-MM-DD-HHMMSS.ipynb**
   - Best practice gap analysis
   - Pattern compliance scoring
   - Improvement recommendations
   - Modern pattern adoption opportunities

4. **Gap_Remediation_Roadmap_YYYY-MM-DD-HHMMSS.ipynb**
   - Prioritized gap closure plan
   - Implementation timeline
   - Effort and resource estimates
   - Success criteria definition

## Critical n8n Best Practice Gap Analysis

### 5. Error Handling Gaps

**Error Handling Implementation Gap Assessment:**

**MANDATORY: Identify missing error handling patterns**

```javascript
// Error handling gap analysis
const errorHandlingGaps = {
  // Error Trigger workflow
  errorTriggerGap: {
    hasErrorTrigger: workflowJSON.settings?.errorWorkflow !== undefined,
    gap: !workflowJSON.settings?.errorWorkflow,
    severity: 'CRITICAL',
    impact: 'No centralized error handling, errors go unnoticed',
    remediation: 'Create Error Trigger workflow and link to main workflow'
  },

  // Node-level error configuration
  nodeErrorConfigGaps: workflowJSON.nodes
    .filter(n => ['httpRequest', 'postgres', 'mysql', 'webhook'].includes(n.type.split('.')[1]))
    .filter(n => !n.continueOnFail && !n.retryOnFail)
    .map(node => ({
      node: node.name,
      gap: 'Missing error configuration',
      severity: 'HIGH',
      impact: 'Node failures halt entire workflow',
      remediation: 'Add continueOnFail: true, retryOnFail: true, maxTries: 3'
    })),

  // Error connections
  errorConnectionGaps: identifyMissingErrorConnections(),

  // Custom error messages
  errorMessageGaps: {
    hasContextualErrors: checkContextualErrorMessages(),
    gap: !checkContextualErrorMessages(),
    severity: 'MEDIUM',
    impact: 'Generic error messages, difficult debugging',
    remediation: 'Add execution context to all error messages'
  }
}
```

**Error Handling Gap Classification:**

**Gap 1: Missing Error Trigger Workflow (CRITICAL)**
```javascript
// Current state: No error handling
{
  "settings": {
    "executionOrder": "v1"
    // NO errorWorkflow configured
  }
}

// Required implementation:
{
  "settings": {
    "executionOrder": "v1",
    "errorWorkflow": "<error-trigger-workflow-id>"
  }
}

// Plus: Create Error Trigger workflow with notification
```

**Gap 2: Missing Node-Level Error Configuration (HIGH)**
```javascript
// Current state: No error handling on critical nodes
{
  "parameters": { "url": "https://api.example.com" },
  "type": "n8n-nodes-base.httpRequest"
  // NO continueOnFail, retryOnFail, maxTries
}

// Required implementation:
{
  "parameters": { "url": "https://api.example.com" },
  "type": "n8n-nodes-base.httpRequest",
  "continueOnFail": true,
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000
}
```

**Error Handling Gap Checklist:**
- [ ] Error Trigger workflow missing
- [ ] Node-level error configuration missing
- [ ] Error connections not implemented
- [ ] Custom error messages lack context
- [ ] Error notification workflow missing
- [ ] Recovery strategies not defined

### 6. Testing Coverage Gaps

**Testing Implementation Gap Assessment:**

**MANDATORY: Identify missing test scenarios and coverage**

```javascript
// Testing coverage gap analysis
const testingGaps = {
  // Unit testing
  unitTestGaps: {
    hasUnitTests: checkForUnitTestWorkflows(),
    gap: !checkForUnitTestWorkflows(),
    severity: 'HIGH',
    impact: 'Code node logic untested, bugs in production',
    remediation: 'Create unit test workflow for all Code nodes',
    missingTests: identifyCodeNodesWithoutTests()
  },

  // Integration testing
  integrationTestGaps: {
    hasIntegrationTests: checkForIntegrationTestWorkflows(),
    gap: !checkForIntegrationTestWorkflows(),
    severity: 'HIGH',
    impact: 'API integrations untested, integration failures in production',
    remediation: 'Create integration test workflow with test endpoints'
  },

  // End-to-end testing
  e2eTestGaps: {
    hasE2ETests: checkForE2ETestScenarios(),
    gap: !checkForE2ETestScenarios(),
    severity: 'MEDIUM',
    impact: 'Complete workflow paths untested',
    remediation: 'Define and execute E2E test scenarios'
  },

  // Test vs production separation
  environmentTestGaps: {
    usesExecutionMode: checkExecutionModeUsage(),
    gap: !checkExecutionModeUsage(),
    severity: 'CRITICAL',
    impact: 'Test executions may affect production data',
    remediation: 'Use $execution.mode to separate test and production endpoints'
  }
}
```

**Testing Gap Classification:**

**Gap 1: No Unit Tests (HIGH)**
```javascript
// Missing: Unit test workflow
{
  "name": "Unit_Tests_MISSING",
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger"
    },
    {
      "parameters": {
        "jsCode": "const testCases = [...];\nconst results = testCases.map(...);\nreturn results;"
      },
      "name": "Run Unit Tests",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Gap 2: No Test/Production Separation (CRITICAL)**
```javascript
// Current state: Production endpoints used in all modes
{
  "parameters": {
    "url": "https://api.example.com/data"  // ALWAYS production!
  }
}

// Required implementation:
{
  "parameters": {
    "url": "={{ $execution.mode === 'test' ? 'https://test-api.example.com' : 'https://api.example.com' }}/data"
  }
}
```

**Testing Coverage Gap Checklist:**
- [ ] Unit test workflows missing
- [ ] Integration test workflows missing
- [ ] E2E test scenarios not defined
- [ ] Test vs production endpoints not separated
- [ ] Test data generation missing
- [ ] Test execution validation missing

### 7. Security Implementation Gaps

**Security Configuration Gap Assessment:**

**MANDATORY: Identify security vulnerabilities and missing safeguards**

```javascript
// Security implementation gap analysis
const securityGaps = {
  // Credential management
  credentialGaps: {
    hasHardcodedSecrets: scanForHardcodedSecrets(),
    gap: scanForHardcodedSecrets(),
    severity: 'CRITICAL',
    impact: 'Exposed API keys and passwords in workflow JSON',
    remediation: 'Move all credentials to credential store',
    exposedSecrets: identifyExposedSecrets()
  },

  // Webhook security
  webhookSecurityGaps: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.webhook')
    .filter(w => w.parameters.authentication === 'none')
    .map(webhook => ({
      webhook: webhook.name,
      gap: 'No authentication configured',
      severity: 'CRITICAL',
      impact: 'Unauthenticated webhook access, security breach risk',
      remediation: 'Configure headerAuth or HMAC authentication'
    })),

  // Audit command execution
  securityAuditGap: {
    hasRunAudit: false,  // Assume not run
    gap: true,
    severity: 'HIGH',
    impact: 'Unknown security vulnerabilities',
    remediation: 'Execute n8n audit command and fix findings'
  },

  // Sensitive data masking
  dataMaskingGaps: {
    masksSensitiveData: checkSensitiveDataMasking(),
    gap: !checkSensitiveDataMasking(),
    severity: 'HIGH',
    impact: 'Passwords, API keys logged in plain text',
    remediation: 'Implement sensitive data masking in all logging'
  }
}
```

**Security Gap Classification:**

**Gap 1: Hardcoded Credentials (CRITICAL)**
```javascript
// Current state: Hardcoded API key
{
  "parameters": {
    "url": "https://api.example.com",
    "headerParameters": {
      "parameters": [
        { "name": "X-API-Key", "value": "sk-1234567890" }  // EXPOSED!
      ]
    }
  }
}

// Required implementation:
{
  "parameters": {
    "url": "https://api.example.com",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "apiKeyAuth"
  },
  "credentials": {
    "apiKeyAuth": { "id": "1", "name": "API Credentials" }
  }
}
```

**Gap 2: Unsecured Webhooks (CRITICAL)**
```javascript
// Current state: No authentication
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook",
    "authentication": "none"  // INSECURE!
  }
}

// Required implementation:
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook",
    "authentication": "headerAuth",
    "options": {
      "rawBody": true,  // HMAC validation
      "ipWhitelist": ["192.168.1.0/24"]
    }
  }
}
```

**Security Implementation Gap Checklist:**
- [ ] Hardcoded credentials in workflow JSON
- [ ] Webhook authentication not configured
- [ ] n8n audit command not executed
- [ ] Sensitive data not masked in logs
- [ ] HMAC signature validation missing
- [ ] IP whitelisting not configured

### 8. Monitoring and Logging Gaps

**Observability Implementation Gap Assessment:**

**MANDATORY: Identify missing monitoring and logging infrastructure**

```javascript
// Monitoring and logging gap analysis
const monitoringGaps = {
  // Structured logging
  structuredLoggingGaps: {
    hasStructuredLogging: checkStructuredLogging(),
    gap: !checkStructuredLogging(),
    severity: 'HIGH',
    impact: 'Unstructured logs, difficult debugging and monitoring',
    remediation: 'Implement JSON structured logging with metadata'
  },

  // Performance metrics
  performanceMetricsGaps: {
    tracksPerformance: checkPerformanceTracking(),
    gap: !checkPerformanceTracking(),
    severity: 'MEDIUM',
    impact: 'No performance visibility, cannot identify bottlenecks',
    remediation: 'Add performance metric tracking to critical nodes'
  },

  // Health check workflow
  healthCheckGaps: {
    hasHealthCheck: checkHealthCheckWorkflow(),
    gap: !checkHealthCheckWorkflow(),
    severity: 'HIGH',
    impact: 'No proactive monitoring, undetected failures',
    remediation: 'Create scheduled health check workflow'
  },

  // Error alerting
  errorAlertingGaps: {
    hasErrorAlerts: workflowJSON.settings?.errorWorkflow !== undefined,
    gap: !workflowJSON.settings?.errorWorkflow,
    severity: 'CRITICAL',
    impact: 'Errors go unnoticed, no team notification',
    remediation: 'Implement Error Trigger workflow with Slack/Discord alerts'
  },

  // External monitoring integration
  externalMonitoringGaps: {
    hasAPMIntegration: checkAPMIntegration(),
    gap: !checkAPMIntegration(),
    severity: 'MEDIUM',
    impact: 'Limited observability, no centralized monitoring',
    remediation: 'Integrate with APM (Prometheus, Grafana, ELK)'
  }
}
```

**Monitoring Gap Classification:**

**Gap 1: No Structured Logging (HIGH)**
```javascript
// Current state: No logging or console.log only
{
  "parameters": {
    "jsCode": "console.log('Processing data');  // Unstructured!"
  }
}

// Required implementation:
{
  "parameters": {
    "jsCode": `
const logEntry = {
  timestamp: new Date().toISOString(),
  level: 'INFO',
  execution: {
    id: $execution.id,
    workflow_id: $workflow.id,
    node_name: $node.name
  },
  event: {
    type: 'data_processing',
    description: 'Processing customer data',
    record_count: $json.items.length
  }
};
console.log(JSON.stringify(logEntry));
`
  }
}
```

**Gap 2: No Health Check Workflow (HIGH)**
```javascript
// Missing: Health check workflow
{
  "name": "Health_Check_MISSING",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [{ "field": "minutes", "minutesInterval": 5 }]
        }
      },
      "name": "Every 5 Minutes",
      "type": "n8n-nodes-base.scheduleTrigger"
    },
    {
      "parameters": {
        "jsCode": "const health = { workflow: await checkHealth(), dependencies: await checkAPIs() }; return { json: health };"
      },
      "name": "Health Check",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Monitoring and Logging Gap Checklist:**
- [ ] Structured logging not implemented
- [ ] Performance metrics not tracked
- [ ] Health check workflow missing
- [ ] Error alerting not configured
- [ ] External monitoring not integrated
- [ ] Sensitive data logged in plain text

### 9. Performance Optimization Gaps

**Performance Configuration Gap Assessment:**

**MANDATORY: Identify performance bottlenecks and missing optimizations**

```javascript
// Performance optimization gap analysis
const performanceGaps = {
  // Execution timeout configuration
  timeoutGaps: {
    hasWorkflowTimeout: workflowJSON.settings?.executionTimeout !== undefined,
    gap: workflowJSON.settings?.executionTimeout === undefined,
    severity: 'HIGH',
    impact: 'Workflows may hang indefinitely',
    remediation: 'Configure executionTimeout in workflow settings'
  },

  // Rate limiting
  rateLimitingGaps: {
    hasRateLimiting: checkRateLimitingPattern(),
    gap: !checkRateLimitingPattern(),
    severity: 'HIGH',
    impact: 'API rate limits exceeded, blocked requests',
    remediation: 'Implement Loop Over Items with Wait node pattern'
  },

  // Batching
  batchingGaps: {
    hasBatching: checkBatchingPattern(),
    gap: !checkBatchingPattern(),
    severity: 'MEDIUM',
    impact: 'Inefficient processing, slow execution',
    remediation: 'Implement Split In Batches for bulk operations'
  },

  // Queue mode configuration
  queueModeGaps: {
    usesQueueMode: process.env.EXECUTIONS_MODE === 'queue',
    gap: process.env.EXECUTIONS_MODE !== 'queue',
    severity: 'HIGH',
    impact: 'Cannot scale for high volume, execution bottleneck',
    remediation: 'Configure queue mode with Redis and worker instances',
    applicableIf: 'High volume workloads (>100 executions/hour)'
  },

  // Static data management
  staticDataGaps: {
    usesStaticData: checkStaticDataUsage(),
    gap: !checkStaticDataUsage() && requiresStatePersistence(),
    severity: 'MEDIUM',
    impact: 'Cannot persist state across executions',
    remediation: 'Use $getWorkflowStaticData() for state management'
  }
}
```

**Performance Gap Classification:**

**Gap 1: No Execution Timeout (HIGH)**
```javascript
// Current state: No timeout configured
{
  "settings": {
    "executionOrder": "v1"
    // NO executionTimeout
  }
}

// Required implementation:
{
  "settings": {
    "executionOrder": "v1",
    "executionTimeout": 300,  // 5 minutes
    "saveExecutionProgress": true
  }
}
```

**Gap 2: No Rate Limiting (HIGH)**
```javascript
// Current state: Uncontrolled API calls
{
  "nodes": [
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest"
      // Calls API for ALL items without rate limiting
    }
  ]
}

// Required implementation:
{
  "nodes": [
    {
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "parameters": { "options": { "loopMode": "item" } }
    },
    {
      "name": "API Call",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "parameters": { "amount": 100, "unit": "milliseconds" }
    }
  ]
}
```

**Gap 3: Queue Mode Not Configured (HIGH)**
```bash
# Current state: Regular mode
EXECUTIONS_MODE=regular  # Cannot scale

# Required configuration:
EXECUTIONS_MODE=queue
QUEUE_BULL_REDIS_HOST=localhost
QUEUE_BULL_REDIS_PORT=6379
QUEUE_WORKER_CONCURRENCY=10
```

**Performance Optimization Gap Checklist:**
- [ ] Workflow execution timeout not configured
- [ ] Node-level timeouts missing
- [ ] Rate limiting not implemented
- [ ] Batching not configured
- [ ] Queue mode not enabled (high volume)
- [ ] Static data management not used
- [ ] Performance metrics not tracked

## Success Criteria

- [ ] Complete requirements coverage analysis
- [ ] All gaps identified and classified
- [ ] Coverage metrics calculated and documented
- [ ] Business impact assessed for each gap
- [ ] Technical impact evaluated
- [ ] Gaps prioritized by severity and impact
- [ ] Remediation roadmap created with timeline
- [ ] Resource estimates provided
- [ ] All deliverables created with proper reverse date stamps
- [ ] Executive summary ready for stakeholder review

**Error Handling Gap Analysis:**
- [ ] Error Trigger workflow gaps identified
- [ ] Node-level error configuration gaps documented
- [ ] Error connection gaps classified
- [ ] Custom error message gaps assessed
- [ ] Error notification gaps prioritized

**Testing Coverage Gap Analysis:**
- [ ] Unit test gaps identified
- [ ] Integration test gaps documented
- [ ] E2E test gaps classified
- [ ] Test environment separation gaps assessed
- [ ] Test coverage metrics calculated

**Security Implementation Gap Analysis:**
- [ ] Credential management gaps identified
- [ ] Webhook security gaps documented
- [ ] Security audit gaps classified
- [ ] Data masking gaps assessed
- [ ] HMAC validation gaps prioritized

**Monitoring and Logging Gap Analysis:**
- [ ] Structured logging gaps identified
- [ ] Performance metrics gaps documented
- [ ] Health check gaps classified
- [ ] Error alerting gaps assessed
- [ ] External monitoring gaps prioritized

**Performance Optimization Gap Analysis:**
- [ ] Timeout configuration gaps identified
- [ ] Rate limiting gaps documented
- [ ] Batching gaps classified
- [ ] Queue mode gaps assessed
- [ ] Static data gaps prioritized

## Command Integration

- **Previous Phase**: `n8n-workflow-implementation`, `n8n-workflow-review`, or `n8n-workflow-quality-analysis`
- **Parallel**: `n8n-workflow-quality-analysis` (quality assessment)
- **Next Phase**: `n8n-workflow-planning` (for gap closure) or `n8n-workflow-refactor` (for improvements)

## Next Phase Preparation

After gap analysis completion:

```bash
# If critical gaps found, plan gap closure:
/n8n-workflow-planning --gap-analysis="Gap_Analysis_Executive_Summary_YYYY-MM-DD-HHMMSS.ipynb" \
  --focus="gap-closure"

# If moderate gaps, refactor workflow:
/n8n-workflow-refactor --workflow-id=<id> \
  --gap-report="Requirements_Coverage_Analysis_YYYY-MM-DD-HHMMSS.ipynb"

# If minor gaps, document and schedule:
# Create backlog items from Gap_Remediation_Roadmap
```

---

**Note**: This is an analysis command that identifies gaps between requirements and implementation. No workflow modifications occur. Use planning or refactor commands to address identified gaps.
