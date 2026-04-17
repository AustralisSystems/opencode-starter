# N8N Workflow Refactor Command

**YAML Prompt**: `n8n-workflow-refactor-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Systematic workflow refactoring and optimization for n8n workflows with focus on improving architecture, expression quality, error handling, and performance while preserving functionality. This command applies best practices and design patterns to enhance workflow quality and maintainability.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n refactoring patterns and best practices
- `grep` - Production refactoring examples on GitHub
- `sequential-thinking` - Structured refactoring methodology
- `filesystem` - Workflow reading, modification, and validation
- `memory` - Track refactoring changes and decisions
- `time` - Timestamp refactoring activities

**n8n-Specific MCP Tools:**
- `get_workflow_structure` - Workflow analysis before refactoring
- `refactor_workflow_architecture` - Architecture improvement tools
- `optimize_expressions` - Expression refactoring and optimization
- `improve_error_handling` - Error handling enhancement
- `validate_workflow` - Post-refactoring validation
- `test_workflow` - Functionality preservation verification

## Refactoring Focus Areas

### 1. Architecture Refactoring

**Pattern Improvements:**
- Linear to parallel processing conversion
- Sequential to branching logic optimization
- Complex workflow simplification
- Node organization and grouping
- Connection architecture refinement

**Architecture Best Practices:**
- Input validation pattern implementation
- Error boundary pattern application
- Async optimization pattern adoption
- State management pattern improvement
- Logging pattern enhancement

### 2. Expression Refactoring

**Expression Optimization:**
- Complex expressions to Code nodes
- Expression simplification
- Null safety implementation
- Error handling addition
- Performance optimization

**Expression Best Practices:**
- Clear $json and $node references
- Proper null coalescing
- Self-documenting expressions
- Consistent expression patterns
- Type-safe operations

### 3. Node Optimization

**Node Configuration:**
- Optimal node selection
- Configuration improvements
- Credential management enhancement
- Resource locator optimization
- Parameter tuning

**Node Best Practices:**
- Appropriate node choices
- Complete configuration
- Secure credential handling
- Efficient resource usage
- Best practice adherence

### 4. Error Handling Enhancement

**Error Handling Improvements:**
- Error workflow implementation
- Try/catch block addition
- Fallback logic creation
- Recovery mechanism implementation
- Error notification setup

**Reliability Patterns:**
- Retry logic implementation
- Circuit breaker patterns
- Graceful degradation
- Data validation
- Comprehensive error logging

### 5. Performance Optimization

**Performance Improvements:**
- Parallel processing implementation
- Sequential operation elimination
- Redundant transformation removal
- Resource-intensive operation optimization
- Caching strategy implementation

**Optimization Patterns:**
- Async execution patterns
- Batch processing implementation
- Connection pooling
- Response caching
- Resource optimization

## Refactoring Methodology

### Refactoring Phases

**Phase 1: Analysis and Planning**
- Load workflow and analyze structure
- Identify refactoring opportunities
- Prioritize improvements by impact
- Plan refactoring approach
- Estimate effort and risk

**Phase 2: Architecture Refactoring**
- Implement pattern improvements
- Optimize workflow structure
- Enhance node organization
- Refine connection architecture
- Validate architectural changes

**Phase 3: Expression Optimization**
- Refactor complex expressions
- Implement null safety
- Add error handling
- Optimize performance
- Validate expression changes

**Phase 4: Error Handling Enhancement**
- Implement error workflows
- Add fallback logic
- Create recovery mechanisms
- Setup error notifications
- Validate error handling

**Phase 5: Performance Optimization**
- Implement parallel processing
- Eliminate inefficiencies
- Remove redundancies
- Optimize resources
- Measure performance improvements

**Phase 6: Validation and Testing**
- Validate workflow structure
- Test functionality preservation
- Verify error handling
- Measure performance gains
- Document refactoring changes

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Refactoring_Applied_YYYY-MM-DD-HHMMSS.ipynb**
   - Summary of refactoring changes
   - Before/after comparisons
   - Performance improvements
   - Quality enhancements

2. **Architecture_Improvements_YYYY-MM-DD-HHMMSS.ipynb**
   - Architecture refactoring details
   - Pattern implementations
   - Structure optimizations
   - Validation results

3. **Refactored_Workflow_YYYY-MM-DD-HHMMSS.json**
   - Complete refactored workflow
   - All improvements applied
   - Validated and tested
   - Ready for deployment

4. **Validation_Report_YYYY-MM-DD-HHMMSS.ipynb**
   - Functionality preservation verification
   - Quality improvement measurements
   - Performance gain analysis
   - Refactoring success criteria

## Advanced Refactoring Patterns

### 6. Error Workflow Refactoring

**Error Handling Enhancement and Implementation:**

**MANDATORY: Implement Error Trigger workflow and node-level error configuration**

```javascript
// Error handling refactoring analysis
const errorRefactoring = {
  currentState: analyzeCurrentErrorHandling(workflowJSON),
  requiredImprovements: [
    'Implement Error Trigger workflow',
    'Add node-level error configuration',
    'Create error connections',
    'Implement error notification workflow'
  ],
  refactoringSteps: generateErrorRefactoringPlan()
}
```

**Step 1: Create Error Trigger Workflow**
```json
{
  "name": "Error_Handler_Central",
  "nodes": [
    {
      "parameters": {},
      "id": "error-trigger",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "const errorData = {\n  workflow: { id: $json.workflow.id, name: $json.workflow.name },\n  execution: { id: $json.execution.id, mode: $json.execution.mode },\n  error: {\n    message: $json.error.message,\n    node: $json.error.node.name,\n    stack: $json.error.stack,\n    timestamp: new Date().toISOString()\n  },\n  severity: $json.error.message.includes('CRITICAL') ? 'critical' : 'warning'\n};\nreturn { json: errorData };"
      },
      "name": "Format Error",
      "type": "n8n-nodes-base.code",
      "position": [450, 300]
    }
  ],
  "connections": {
    "Error Trigger": { "main": [[{ "node": "Format Error", "type": "main", "index": 0 }]] }
  }
}
```

**Step 2: Link Main Workflow to Error Handler**
```javascript
// Add to main workflow settings
{
  "settings": {
    "errorWorkflow": "<error-trigger-workflow-id>",  // Link Error Trigger
    "executionOrder": "v1"
  }
}
```

**Step 3: Add Node-Level Error Configuration**
```javascript
// Refactor critical nodes with error handling
{
  "parameters": { /* existing config */ },
  "continueOnFail": true,
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000,
  "onError": "continueErrorOutput"
}
```

**Error Workflow Refactoring Checklist:**
- [ ] Create centralized Error Trigger workflow
- [ ] Link main workflow to error handler
- [ ] Add node-level error configuration to critical nodes
- [ ] Implement error connections for risky operations
- [ ] Add error notification workflow (Slack/Discord)
- [ ] Implement custom error messages with context
- [ ] Test error scenarios and recovery

### 7. Performance Optimization Refactoring

**Execution Efficiency Enhancement:**

**MANDATORY: Optimize timeouts, batching, and rate limiting**

**Step 1: Optimize Timeouts**
```javascript
// Add workflow-level timeout
{
  "settings": {
    "executionTimeout": 300,  // 5 minutes
    "saveExecutionProgress": true
  }
}

// Add node-level timeouts
{
  "parameters": {
    "url": "https://api.example.com/data",
    "timeout": 30000  // 30 seconds
  },
  "type": "n8n-nodes-base.httpRequest"
}
```

**Step 2: Implement Rate Limiting**
```json
{
  "nodes": [
    {
      "parameters": {
        "options": { "loopMode": "item" }
      },
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches"
    },
    {
      "parameters": {
        "url": "https://api.example.com/item/{{ $json.id }}",
        "method": "GET"
      },
      "name": "API Call",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "parameters": {
        "amount": 100,
        "unit": "milliseconds"
      },
      "name": "Wait",
      "type": "n8n-nodes-base.wait"
    }
  ],
  "connections": {
    "Loop Over Items": { "main": [[{ "node": "API Call", "type": "main", "index": 0 }]] },
    "API Call": { "main": [[{ "node": "Wait", "type": "main", "index": 0 }]] },
    "Wait": { "main": [[{ "node": "Loop Over Items", "type": "main", "index": 0 }]] }
  }
}
```

**Step 3: Implement Batching**
```javascript
{
  "parameters": {
    "batchSize": 100,
    "options": {
      "reset": false
    }
  },
  "name": "Batch Items",
  "type": "n8n-nodes-base.splitInBatches"
}
```

**Performance Optimization Checklist:**
- [ ] Workflow execution timeout configured
- [ ] Node-specific timeouts added
- [ ] Rate limiting implemented (Loop + Wait)
- [ ] Batching configured for bulk operations
- [ ] Execution progress saving enabled
- [ ] Queue mode configured (if high volume)
- [ ] Performance metrics tracked

### 8. Security Enhancement Refactoring

**Security Hardening Implementation:**

**MANDATORY: Improve credential management and webhook security**

**Step 1: Credential Management Improvement**
```javascript
// BEFORE: Hardcoded credentials
{
  "parameters": {
    "url": "https://api.example.com/data",
    "headerParameters": {
      "parameters": [
        { "name": "X-API-Key", "value": "hardcoded-key-123" }  // BAD!
      ]
    }
  }
}

// AFTER: Credential reference
{
  "parameters": {
    "url": "https://api.example.com/data",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "apiKeyAuth"
  },
  "credentials": {
    "apiKeyAuth": {
      "id": "1",
      "name": "API Credentials"
    }
  }
}
```

**Step 2: Webhook Security Enhancement**
```javascript
// BEFORE: Unsecured webhook
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook",
    "authentication": "none"  // INSECURE!
  }
}

// AFTER: Secured webhook with HMAC
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook",
    "authentication": "headerAuth",
    "options": {
      "rawBody": true,  // Enable HMAC validation
      "ipWhitelist": ["192.168.1.0/24"],
      "allowedOrigins": ["https://trusted-domain.com"]
    }
  }
}
```

**Step 3: Run Security Audit**
```bash
# Execute security audit
n8n audit

# Fix identified issues
# - Remove hardcoded secrets
# - Update credential references
# - Enable webhook authentication
# - Mask sensitive data in logs
```

**Security Enhancement Checklist:**
- [ ] All credentials moved to credential store
- [ ] No hardcoded secrets in workflow JSON
- [ ] Webhook authentication configured
- [ ] HMAC signature validation implemented
- [ ] IP whitelisting configured
- [ ] Sensitive data masked in logs
- [ ] n8n audit executed with no findings

### 9. Testing Coverage Improvement

**Test Implementation and Enhancement:**

**MANDATORY: Add missing unit, integration, and E2E tests**

**Step 1: Implement Unit Tests**
```json
{
  "name": "Unit_Tests_Workflow",
  "nodes": [
    {
      "parameters": {},
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger"
    },
    {
      "parameters": {
        "jsCode": "const testCases = [\n  { input: { price: 100, tax: 0.1 }, expected: 110 },\n  { input: { price: 50, tax: 0.2 }, expected: 60 }\n];\n\nconst results = testCases.map(test => {\n  const result = test.input.price * (1 + test.input.tax);\n  return {\n    input: test.input,\n    expected: test.expected,\n    actual: result,\n    passed: result === test.expected\n  };\n});\n\nreturn results.map(r => ({ json: r }));"
      },
      "name": "Run Unit Tests",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Step 2: Implement Integration Tests**
```json
{
  "name": "Integration_Tests_Workflow",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "test-integration"
      },
      "name": "Test Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "parameters": {
        "url": "={{ $execution.mode === 'test' ? 'https://test-api.com' : 'https://api.com' }}/process",
        "method": "POST",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [{ "name": "data", "value": "={{ $json }}" }]
        }
      },
      "name": "API Call",
      "type": "n8n-nodes-base.httpRequest"
    }
  ]
}
```

**Step 3: Execute E2E Tests**
```javascript
// Trigger test workflow
n8n_trigger_webhook_workflow({
  workflowId: 'integration-test-id',
  testData: { id: 'test-123', data: {...} }
})

// Validate results
const executions = n8n_list_executions({
  workflowId: 'integration-test-id',
  limit: 1
})
```

**Testing Coverage Checklist:**
- [ ] Unit test workflow created for Code nodes
- [ ] Integration test workflow created
- [ ] E2E test scenarios defined and executed
- [ ] Test vs production endpoints configured
- [ ] Test data generation implemented
- [ ] Test execution results validated
- [ ] Test coverage documented

### 10. Monitoring Enhancement Refactoring

**Observability Implementation:**

**MANDATORY: Improve logging and health checks**

**Step 1: Implement Structured Logging**
```javascript
{
  "parameters": {
    "jsCode": `
const logEntry = {
  timestamp: new Date().toISOString(),
  level: 'INFO',
  execution: {
    id: $execution.id,
    workflow_id: $workflow.id,
    workflow_name: $workflow.name,
    node_name: $node.name,
    mode: $execution.mode
  },
  event: {
    type: 'api_call_success',
    description: 'Data processed successfully',
    duration_ms: Date.now() - $execution.startedAt,
    record_count: $json.items?.length || 0
  },
  data: {
    id: $json.id,
    email: maskEmail($json.email)  // Mask sensitive data
  }
};

console.log(JSON.stringify(logEntry));
return { json: $json };
`
  },
  "name": "Structured Logger",
  "type": "n8n-nodes-base.code"
}
```

**Step 2: Implement Health Check Workflow**
```json
{
  "name": "Health_Check_Workflow",
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
        "jsCode": "const healthStatus = {\n  timestamp: new Date().toISOString(),\n  workflow: {\n    active: $workflow.active,\n    errorRate: calculateErrorRate($workflow.id, 3600000),\n    avgDuration: calculateAvgDuration($workflow.id, 3600000)\n  },\n  dependencies: {\n    api: await checkAPIHealth('https://api.example.com/health'),\n    database: await checkDatabaseHealth()\n  },\n  status: determineOverallHealth()\n};\n\nif (healthStatus.status !== 'healthy') {\n  return { json: { ...healthStatus, alert: true } };\n}\n\nreturn { json: healthStatus };"
      },
      "name": "Health Check",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Monitoring Enhancement Checklist:**
- [ ] Structured logging implemented (JSON format)
- [ ] Critical events logged with metadata
- [ ] Performance metrics tracked
- [ ] Sensitive data masked in logs
- [ ] Health check workflow created
- [ ] Dependency health monitored
- [ ] Alert thresholds configured
- [ ] External monitoring integrated

## Success Criteria

- [ ] Workflow architecture refactored and improved
- [ ] Expressions optimized and simplified
- [ ] Error handling enhanced and comprehensive
- [ ] Performance optimized with measurable gains
- [ ] Node configuration improved
- [ ] All refactoring validated and tested
- [ ] Functionality completely preserved
- [ ] Quality improvements documented
- [ ] All deliverables created with proper reverse date stamps
- [ ] Refactored workflow ready for deployment

**Error Workflow Refactoring:**
- [ ] Error Trigger workflow created and linked
- [ ] Node-level error configuration added
- [ ] Error connections implemented
- [ ] Error notification workflow configured
- [ ] Custom error messages with context

**Performance Optimization:**
- [ ] Workflow and node timeouts configured
- [ ] Rate limiting implemented (Loop + Wait)
- [ ] Batching configured for bulk operations
- [ ] Queue mode configured (if applicable)
- [ ] Performance metrics tracked

**Security Enhancement:**
- [ ] All credentials in credential store
- [ ] No hardcoded secrets
- [ ] Webhook authentication configured
- [ ] HMAC validation implemented
- [ ] Security audit passed

**Testing Coverage:**
- [ ] Unit test workflow created
- [ ] Integration test workflow created
- [ ] E2E tests executed and passing
- [ ] Test coverage documented

**Monitoring Enhancement:**
- [ ] Structured logging implemented
- [ ] Health check workflow created
- [ ] Performance metrics tracked
- [ ] Alert channels configured

## Command Integration

- **Previous Phase**: `n8n-workflow-review`, `n8n-workflow-quality-analysis`, or `n8n-workflow-lint-quality-check`
- **Parallel**: None (refactoring should be isolated)
- **Next Phase**: `n8n-workflow-lint-quality-check` (validation) or workflow deployment

## Next Phase Preparation

After refactoring completion:

```bash
# Validate refactored workflow:
/n8n-workflow-lint-quality-check --workflow-file="Refactored_Workflow_YYYY-MM-DD-HHMMSS.json"

# Quality analysis of refactored workflow:
/n8n-workflow-quality-analysis --workflow-file="Refactored_Workflow_YYYY-MM-DD-HHMMSS.json"

# Deploy if validation passes
```

---

**Note**: This is a refactoring command that modifies workflows to improve quality while preserving functionality. All changes are validated and tested. Refactored workflow is saved as new file with timestamp.
