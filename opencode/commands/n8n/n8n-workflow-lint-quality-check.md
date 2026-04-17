# N8N Workflow Lint and Quality Check Command

**YAML Prompt**: `n8n-workflow-lint-quality-check-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Automated quality validation for n8n workflows with comprehensive lint checking, expression validation, node configuration verification, and connection analysis. This command ensures workflow quality through systematic validation of workflow structure, expressions, and configurations.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n validation standards and best practices
- `grep` - Real-world workflow validation patterns on GitHub
- `sequential-thinking` - Structured validation methodology
- `filesystem` - Workflow file reading and analysis
- `memory` - Track validation findings during analysis
- `time` - Timestamp validation activities

**n8n-Specific MCP Tools:**
- `validate_workflow` - Comprehensive workflow structure validation
- `validate_workflow_connections` - Connection integrity checking
- `validate_workflow_expressions` - Expression syntax and logic validation
- `get_workflow_structure` - Workflow architecture analysis
- `list_workflow_issues` - Identify workflow problems
- `check_node_configurations` - Validate node settings

## Workflow Validation Dimensions

### 1. Workflow Structure Validation

**Workflow Integrity Checks:**
- Workflow JSON structure validity
- Required workflow properties present
- Workflow metadata completeness
- Settings and configuration validity

**Connection Validation:**
```javascript
// Connection structure verification
{
  "connections": {
    "Webhook": {
      "main": [[{ "node": "Set", "type": "main", "index": 0 }]]
    }
  }
}

// Validation checks:
// - All source nodes exist
// - All target nodes exist
// - Connection types are valid
// - No circular dependencies
// - No orphaned nodes
```

### 2. Node Configuration Validation

**Configuration Completeness:**
- All required node parameters configured
- Parameter values within valid ranges
- Credential references valid and secure
- Resource locators properly defined
- Options and flags appropriately set

**Node-Specific Validation:**
- **HTTP Request**: URL validity, method configuration, authentication setup
- **Webhook**: Path configuration, response handling, authentication settings
- **Code**: JavaScript/Python syntax validation, input/output handling
- **Database**: Connection settings, query syntax, data handling
- **Transform**: Expression syntax, data type compatibility

### 3. Expression Validation

**Expression Syntax Checking:**
```javascript
// Valid expressions:
{{ $json.data.user.name }}
{{ $node["HTTP Request"].json.items[0].id }}
{{ $items().length > 0 ? $json.value : 'default' }}

// Validation checks:
// - Proper {{ }} delimiters
// - Valid JavaScript syntax
// - Correct node references
// - Data path existence
// - Type compatibility
```

**Expression Quality Metrics:**
- Expression complexity assessment
- Null safety verification
- Type coercion validation
- Error handling presence
- Performance optimization opportunities

### 4. Security and Credentials Validation

**Credential Security:**
- No hardcoded credentials in workflows
- Proper credential references used
- Sensitive data properly masked
- Environment variable usage validated
- Secret management compliance

**Security Best Practices:**
- Authentication configuration validated
- Authorization patterns verified
- Data encryption compliance
- Input sanitization presence
- Output data filtering

### 5. Error Handling Validation

**Error Handling Patterns:**
- Error workflows connected properly
- Try/catch blocks in Code nodes
- Fallback logic implemented
- Error notification configured
- Recovery strategies defined

**Error Handling Quality:**
```json
{
  "node": "HTTP Request",
  "continueOnFail": true,
  "onError": "continueErrorOutput"
}
```

## Workflow Quality Metrics

### Quality Scoring Framework

**Level 5 (90-100%)**: Production Ready
- All validations pass
- No critical issues
- Optimal expressions
- Complete error handling
- Security best practices followed

**Level 4 (80-89%)**: Good Quality
- Minor warnings only
- Expressions functional but improvable
- Basic error handling present
- Security requirements met

**Level 3 (70-79%)**: Acceptable
- Some moderate issues
- Expression improvements needed
- Error handling gaps present
- Security review recommended

**Level 2 (60-69%)**: Below Standard
- Multiple issues present
- Expression problems identified
- Error handling insufficient
- Security concerns exist

**Level 1 (<60%)**: Needs Improvement
- Critical issues found
- Expression failures likely
- No error handling
- Security violations present

### Validation Categories

**Critical Issues (Must Fix):**
- Invalid JSON structure
- Missing required connections
- Expression syntax errors
- Security vulnerabilities
- Broken node configurations

**Warnings (Should Fix):**
- Unused nodes present
- Suboptimal expressions
- Missing error handlers
- Performance concerns
- Documentation gaps

**Suggestions (Consider):**
- Expression optimization opportunities
- Alternative node choices
- Performance improvements
- Maintainability enhancements
- Pattern upgrades

## Automated Quality Improvements

### Safe Auto-Fix Categories

**Automatically Fixable:**
- Expression formatting standardization
- Connection organization optimization
- Node position cleanup
- Metadata completion
- Documentation formatting

**Manual Review Required:**
- Complex expression rewrites
- Node configuration changes
- Connection architecture modifications
- Error handling additions
- Security implementations

### Validation Tools Integration

**Built-in Validators:**
```bash
# Workflow structure validation
validate_workflow(workflow_json)

# Connection integrity check
validate_workflow_connections(workflow_id)

# Expression validation
validate_workflow_expressions(workflow_id)

# Node configuration check
check_node_configurations(workflow_id)
```

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Workflow_Validation_Report_YYYY-MM-DD-HHMMSS.ipynb**
   - Comprehensive validation results
   - Critical issues, warnings, and suggestions
   - Quality score and metrics
   - Auto-fix opportunities identified

2. **Expression_Analysis_YYYY-MM-DD-HHMMSS.ipynb**
   - All expressions documented and validated
   - Syntax errors and warnings
   - Optimization recommendations
   - Security concerns flagged

3. **Node_Configuration_Review_YYYY-MM-DD-HHMMSS.ipynb**
   - Node-by-node configuration analysis
   - Missing parameters identified
   - Invalid settings flagged
   - Best practice recommendations

4. **Quality_Fixes_Applied_YYYY-MM-DD-HHMMSS.ipynb** (if auto-fixes applied)
   - Summary of automatic fixes applied
   - Manual review items flagged
   - Validation re-run results

## Workflow Validation Checklist

### Structure Validation
- [ ] Workflow JSON structure valid
- [ ] All required properties present
- [ ] Metadata complete and accurate
- [ ] Settings properly configured
- [ ] No structural errors

### Connection Validation
- [ ] All connections valid and complete
- [ ] No orphaned nodes present
- [ ] No circular dependencies
- [ ] Connection types appropriate
- [ ] Data flow logical and efficient

### Node Validation
- [ ] All nodes properly configured
- [ ] Required parameters set
- [ ] Credentials properly referenced
- [ ] Resource locators valid
- [ ] Node options appropriate

### Expression Validation
- [ ] All expressions syntactically valid
- [ ] Node references correct
- [ ] Data paths verified
- [ ] Type compatibility ensured
- [ ] Null safety implemented

### Security Validation
- [ ] No hardcoded credentials
- [ ] Secrets properly managed
- [ ] Authentication configured
- [ ] Input validation present
- [ ] Output filtering implemented

### Error Handling Validation
- [ ] Error workflows connected
- [ ] Try/catch blocks present
- [ ] Fallback logic implemented
- [ ] Error notifications configured
- [ ] Recovery strategies defined

### Quality Metrics
- [ ] Overall quality score calculated
- [ ] Performance metrics assessed
- [ ] Maintainability evaluated
- [ ] Security compliance verified
- [ ] Best practices followed

### 6. Execution Testing Validation

**Actual Workflow Execution Testing:**

**MANDATORY: Test actual workflow execution, not just static validation**

```javascript
// Execute workflow with test data
n8n_trigger_webhook_workflow({
  workflowId: 'workflow-to-test',
  testData: {
    // Representative test data
    id: 'test-123',
    data: { /* realistic test payload */ }
  }
})

// Verify execution results
const executions = n8n_list_executions({
  workflowId: 'workflow-to-test',
  limit: 5
})

// Validation checks:
// - execution.finished === true
// - execution.data.resultData.error === undefined
// - execution.data.resultData.runData contains expected nodes
// - output data matches expected format
```

**Execution Testing Checklist:**
- [ ] Workflow executes successfully with test data
- [ ] All nodes in execution path complete without errors
- [ ] Data transformations produce expected outputs
- [ ] Error handling triggers correctly for invalid inputs
- [ ] Webhook responses return expected status and data
- [ ] Execution time within acceptable limits

**Test Scenarios to Validate:**
```javascript
// Scenario 1: Happy path test
{
  testName: 'Valid data processing',
  input: { /* valid payload */ },
  expectedNodes: ['Webhook', 'Validate', 'Transform', 'API Call', 'Response'],
  expectedOutput: { success: true, data: {...} }
}

// Scenario 2: Error handling test
{
  testName: 'Invalid data triggers error handler',
  input: { /* invalid payload */ },
  expectedNodes: ['Webhook', 'Validate', 'Error Handler', 'Error Response'],
  expectedError: 'Validation failed: missing required field'
}

// Scenario 3: Edge case test
{
  testName: 'Null value handling',
  input: { id: null, data: undefined },
  expectedBehavior: 'Graceful handling with default values'
}
```

### 7. Performance Testing Validation

**Execution Performance Benchmarking:**

**MANDATORY: Validate performance meets requirements**

```javascript
// Performance test configuration
const performanceTests = [
  {
    testName: 'Single execution baseline',
    iterations: 1,
    expectedDuration: 2000,  // 2 seconds max
    payload: { /* standard payload */ }
  },
  {
    testName: 'Concurrent execution test',
    iterations: 10,
    concurrency: 5,
    expectedDuration: 5000,  // 5 seconds for 10 executions
    payload: { /* standard payload */ }
  },
  {
    testName: 'Large payload test',
    iterations: 1,
    payload: { items: Array(1000).fill({...}) },  // 1000 items
    expectedDuration: 5000
  }
]

// Execute performance tests
for (const test of performanceTests) {
  const startTime = Date.now()

  // Execute workflow
  await n8n_trigger_webhook_workflow({
    workflowId: 'workflow-id',
    testData: test.payload
  })

  const duration = Date.now() - startTime

  // Validate performance
  if (duration > test.expectedDuration) {
    console.warn(`Performance issue: ${test.testName} took ${duration}ms (expected ${test.expectedDuration}ms)`)
  }
}
```

**Performance Validation Checks:**
- [ ] Single execution completes within timeout (< 2s for simple, < 10s for complex)
- [ ] Concurrent executions scale appropriately
- [ ] Large payload handling within limits
- [ ] Node execution times measured and documented
- [ ] API call latency within acceptable range
- [ ] Data transformation performance validated
- [ ] Queue mode performance tested (if applicable)

**Performance Metrics to Collect:**
```javascript
{
  "workflow_performance": {
    "total_execution_time": "1.5s",
    "node_execution_times": {
      "Webhook": "50ms",
      "Validate": "100ms",
      "API Call": "800ms",
      "Transform": "200ms",
      "Response": "50ms"
    },
    "bottlenecks": [
      { node: "API Call", duration: "800ms", recommendation: "Consider caching" }
    ],
    "throughput": "10 executions/second",
    "queue_wait_time": "0ms (queue mode disabled)"
  }
}
```

### 8. Security Audit Integration

**n8n Security Audit Command:**

**MANDATORY: Run security audit before production deployment**

```bash
# Run n8n built-in security audit
n8n audit

# Output includes:
# - Exposed credentials in workflows
# - Hardcoded secrets
# - Insecure node configurations
# - Webhook security issues
# - Authentication vulnerabilities
```

**Security Scanning Checklist:**
- [ ] n8n audit command executed successfully
- [ ] No exposed credentials found in workflow JSON
- [ ] No hardcoded API keys or secrets detected
- [ ] All credentials properly referenced from credential store
- [ ] Webhook authentication configured (HMAC, Basic Auth, or Header Auth)
- [ ] Sensitive data masked in logs and outputs
- [ ] Environment variables used for secrets (not workflow JSON)

**Security Validation Patterns:**
```javascript
// Scan workflow JSON for security issues
const securityChecks = {
  noHardcodedSecrets: !workflowJSON.includes('api_key') &&
                      !workflowJSON.includes('password') &&
                      !workflowJSON.includes('secret'),

  credentialReferences: workflowJSON.nodes.every(node =>
    node.credentials ? Object.keys(node.credentials).length > 0 : true
  ),

  webhookSecurity: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.webhook')
    .every(webhook =>
      webhook.parameters.authentication !== 'none' ||
      webhook.parameters.options?.rawBody === true  // For HMAC validation
    ),

  sensitiveDataMasking: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.code')
    .every(code =>
      !code.parameters.jsCode.includes('console.log($json.password)') &&
      !code.parameters.jsCode.includes('console.log($json.apiKey)')
    )
}
```

**Security Audit Findings Template:**
```javascript
{
  "security_audit_results": {
    "status": "PASS|FAIL",
    "findings": [
      {
        "severity": "CRITICAL|HIGH|MEDIUM|LOW",
        "issue": "Hardcoded API key found in HTTP Request node",
        "location": "Node: 'External API Call', parameter: 'headerParameters'",
        "remediation": "Move API key to credential store and reference via $credentials",
        "status": "OPEN|FIXED"
      }
    ],
    "compliance_checks": {
      "credential_management": "PASS",
      "webhook_security": "FAIL - No authentication configured",
      "data_masking": "PASS",
      "environment_variables": "PASS"
    }
  }
}
```

### 9. Custom Error Message Validation

**Error Message Context Validation:**

**MANDATORY: Ensure error messages include execution context**

```javascript
// Error message best practices validation
const errorMessageChecks = {
  // Check Error Trigger workflow
  hasErrorTrigger: workflowJSON.settings?.errorWorkflow !== undefined,

  // Check error message formatting in Code nodes
  errorMessagesHaveContext: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.code')
    .every(code => {
      const hasContextualErrors =
        code.parameters.jsCode.includes('$workflow') &&
        code.parameters.jsCode.includes('$execution') &&
        code.parameters.jsCode.includes('$json.error');
      return hasContextualErrors || !code.parameters.jsCode.includes('throw new Error');
    }),

  // Check node-level error configuration
  criticalNodesHaveErrorConfig: workflowJSON.nodes
    .filter(n => ['httpRequest', 'postgres', 'mysql'].includes(n.type.split('.')[1]))
    .every(node =>
      node.continueOnFail === true ||
      node.retryOnFail === true ||
      workflowJSON.connections[node.name]?.error
    )
}
```

**Error Message Quality Criteria:**
```javascript
// Good error message example (WITH context)
const goodErrorMessage = {
  message: `Workflow: ${$workflow.name}, Node: ${$node.name}, Execution: ${$execution.id}, Error: API call failed - ${error.message}`,
  context: {
    workflow_id: $workflow.id,
    workflow_name: $workflow.name,
    execution_id: $execution.id,
    node_name: $node.name,
    timestamp: new Date().toISOString(),
    input_data: $json
  }
}

// Bad error message example (NO context)
const badErrorMessage = {
  message: 'Error occurred'  // Not helpful!
}
```

**Error Message Validation Checklist:**
- [ ] Error messages include workflow name and ID
- [ ] Error messages include execution ID
- [ ] Error messages include node name where error occurred
- [ ] Error messages include timestamp
- [ ] Error messages include original error details
- [ ] Error Trigger workflow formats errors with full context
- [ ] Critical nodes have custom error messages (not generic)
- [ ] Error notifications include actionable information

### 10. Webhook Testing Validation

**Comprehensive Webhook Testing:**

**MANDATORY: Validate webhook functionality and security**

```bash
# Start n8n with tunnel mode for testing
n8n start --tunnel

# Output: Tunnel URL: https://random-subdomain.n8n.app
```

**Webhook Test Scenarios:**
```javascript
// Test 1: Valid webhook request
await fetch('https://tunnel-url.n8n.app/webhook/test-path', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'valid-api-key',
    'X-HMAC-Signature': 'calculated-signature'
  },
  body: JSON.stringify({
    id: 'test-123',
    data: { /* valid payload */ }
  })
})
// Expected: 200 OK, correct response data

// Test 2: Invalid authentication
await fetch('https://tunnel-url.n8n.app/webhook/test-path', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'invalid-key'
  },
  body: JSON.stringify({...})
})
// Expected: 401 Unauthorized

// Test 3: Malformed payload
await fetch('https://tunnel-url.n8n.app/webhook/test-path', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'valid-api-key'
  },
  body: 'invalid json'
})
// Expected: 400 Bad Request or error handler triggered

// Test 4: HMAC signature validation
const payload = JSON.stringify({ test: 'data' })
const signature = crypto.createHmac('sha256', 'secret').update(payload).digest('hex')

await fetch('https://tunnel-url.n8n.app/webhook/secure-path', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-HMAC-SHA256': signature
  },
  body: payload
})
// Expected: 200 OK (signature valid)
```

**Webhook Validation Checklist:**
- [ ] n8n started with --tunnel flag for local testing
- [ ] Tunnel URL documented and accessible
- [ ] Webhook authentication validated (Header Auth, HMAC, Basic Auth)
- [ ] Valid requests processed successfully
- [ ] Invalid authentication rejected (401)
- [ ] Malformed payloads handled gracefully (400)
- [ ] HMAC signature validation working (if configured)
- [ ] Webhook response format correct
- [ ] Error responses include appropriate status codes
- [ ] Webhook logging captures all requests

**Webhook Security Configuration Validation:**
```javascript
// Validate webhook node security settings
const webhookSecurityCheck = workflowJSON.nodes
  .filter(n => n.type === 'n8n-nodes-base.webhook')
  .map(webhook => ({
    name: webhook.name,
    authentication: webhook.parameters.authentication || 'none',
    hasHmacValidation: webhook.parameters.options?.rawBody === true,
    hasIpWhitelist: webhook.parameters.options?.ipWhitelist?.length > 0,
    isSecure: webhook.parameters.authentication !== 'none' ||
              webhook.parameters.options?.rawBody === true
  }))

// All webhooks should have isSecure === true
```

## Success Criteria

- [ ] All workflow structure validations pass
- [ ] Connection integrity verified
- [ ] Node configurations validated
- [ ] All expressions syntactically correct
- [ ] Security compliance confirmed
- [ ] Error handling adequately implemented
- [ ] Quality score meets threshold (70%)
- [ ] Critical issues resolved
- [ ] All deliverables created with proper reverse date stamps
- [ ] Auto-fix opportunities identified and applied where safe
- [ ] Manual review items documented for complex changes

**Execution Testing:**
- [ ] Workflow executes successfully with test data
- [ ] All execution test scenarios pass (happy path, error cases, edge cases)
- [ ] Execution results match expected outputs
- [ ] Error handling triggers correctly
- [ ] Webhook responses validated

**Performance Testing:**
- [ ] Performance benchmarks executed and documented
- [ ] Execution time within acceptable limits
- [ ] Concurrent execution performance validated
- [ ] Bottlenecks identified and documented
- [ ] Performance recommendations provided

**Security Audit:**
- [ ] n8n audit command executed with no critical findings
- [ ] No hardcoded secrets detected
- [ ] All credentials properly referenced
- [ ] Webhook security validated
- [ ] Sensitive data masking verified
- [ ] Security audit findings documented and remediated

**Error Message Validation:**
- [ ] Error messages include full execution context
- [ ] Error Trigger workflow formats errors correctly
- [ ] Custom error messages implemented for critical nodes
- [ ] Error notifications include actionable information

**Webhook Testing:**
- [ ] Tunnel mode configured and tested
- [ ] Webhook authentication validated
- [ ] Valid requests processed successfully
- [ ] Invalid requests rejected appropriately
- [ ] HMAC signature validation working (if configured)
- [ ] Webhook security configuration validated

## Command Integration

- **Previous Phase**: `n8n-workflow-implementation` (validate after implementation)
- **Parallel**: `n8n-workflow-quality-analysis` (comprehensive quality assessment)
- **Next Phase**: `n8n-workflow-review` (human review of findings) or `n8n-workflow-refactor` (apply improvements)

## Next Phase Preparation

After validation completion, proceed based on findings:

```bash
# If critical issues found, review and fix:
/n8n-workflow-review --validation-report="Workflow_Validation_Report_YYYY-MM-DD-HHMMSS.ipynb"

# If moderate issues, refactor workflow:
/n8n-workflow-refactor --workflow-id=<id> --focus-areas="expressions,error-handling"

# If validation passes, proceed to testing:
/n8n-workflow-test --workflow-id=<id>
```

---

**Note**: This is a validation command that produces comprehensive workflow quality reports and identifies issues. Safe auto-fixes are applied where possible, but complex changes require manual review. No functionality changes occur without validation.
