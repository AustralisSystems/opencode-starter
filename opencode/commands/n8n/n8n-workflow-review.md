# N8N Workflow Review Command

**YAML Prompt**: `n8n-workflow-review-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Comprehensive human-centric workflow review for n8n workflows with focus on architecture, node selection, expression quality, error handling, and maintainability. This command provides detailed review findings with actionable recommendations for workflow improvement.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n best practices and architectural patterns
- `grep` - Real-world production workflow implementations on GitHub
- `sequential-thinking` - Structured review methodology
- `filesystem` - Workflow reading and analysis
- `memory` - Track review findings and decisions
- `time` - Timestamp review activities

**n8n-Specific MCP Tools:**
- `get_workflow_structure` - Comprehensive workflow structure analysis
- `analyze_workflow_architecture` - Architecture pattern evaluation
- `review_node_selection` - Node choice appropriateness assessment
- `analyze_expressions` - Expression quality review
- `assess_error_handling` - Error handling pattern review
- `evaluate_maintainability` - Maintainability assessment

## Review Focus Areas

### 1. Workflow Architecture Quality

**Architecture Assessment:**
- Workflow pattern appropriateness (linear, branching, parallel, complex)
- Data flow logic and efficiency
- Node organization and grouping
- Connection clarity and maintainability
- Scalability and extensibility considerations

**Architecture Best Practices:**
- Input validation at workflow entry
- Clear error handling boundaries
- Appropriate use of parallel processing
- Efficient data transformation approach
- Proper state management through workflow

### 2. Node Selection and Configuration Review

**Node Appropriateness:**
- Optimal node choices for requirements
- Alternative node considerations
- Node configuration completeness
- Credential management patterns
- Resource locator effectiveness

**Configuration Quality:**
- Parameter completeness and correctness
- Authentication and authorization setup
- Timeout and retry configuration
- Output filtering and data shaping
- Node-specific best practice adherence

### 3. Expression Quality and Maintainability

**Expression Review:**
- Expression complexity and readability
- Null safety and error handling
- Performance implications
- Maintainability considerations
- Alternative expression approaches

**Expression Best Practices:**
- Appropriate use of $json, $node references
- Proper null coalescing and default values
- Clear and self-documenting expressions
- Code node extraction for complex logic
- Consistent expression patterns

### 4. Error Handling and Reliability

**Error Handling Coverage:**
- Critical node error handling presence
- Error workflow completeness
- Fallback strategy implementation
- Recovery mechanism effectiveness
- Error notification appropriateness

**Reliability Patterns:**
- Retry logic for transient failures
- Circuit breaker implementations
- Graceful degradation strategies
- Data validation before processing
- Comprehensive error logging

### 5. Security and Compliance

**Security Review:**
- Credential management practices
- Sensitive data handling
- Input validation and sanitization
- Output filtering and masking
- Secret exposure risks

**Compliance Assessment:**
- Data retention policy adherence
- Audit logging completeness
- Access control patterns
- Encryption usage
- Privacy protection measures

### 6. Performance and Optimization

**Performance Review:**
- Parallel processing opportunities
- Sequential execution inefficiencies
- Redundant data transformations
- Resource-intensive operation identification
- Optimization potential quantification

**Optimization Recommendations:**
- Parallel execution improvements
- Expression optimization
- Node configuration tuning
- Connection architecture refinement
- Resource utilization enhancement

## Review Methodology

### Review Levels

**Level A (90-100%)**: Excellent - Production Ready
- Best practices consistently applied
- Optimal node selection and configuration
- Comprehensive error handling
- High maintainability

**Level B (80-89%)**: Good - Minor Improvements
- Generally good practices
- Appropriate node usage
- Adequate error handling
- Good maintainability

**Level C (70-79%)**: Acceptable - Moderate Issues
- Standard practices applied
- Functional node selection
- Basic error handling
- Acceptable maintainability

**Level D (60-69%)**: Below Standard - Significant Issues
- Inconsistent practices
- Suboptimal node choices
- Insufficient error handling
- Maintenance concerns

**Level F (<60%)**: Failing - Major Rework Needed
- Poor practices throughout
- Inappropriate node selection
- Missing error handling
- High maintenance burden

### Review Categories

**Critical Issues (Must Address):**
- Security vulnerabilities
- Data loss risks
- Performance blockers
- Scalability limitations
- Integration failures

**Major Issues (Should Address):**
- Suboptimal architectures
- Maintainability concerns
- Error handling gaps
- Performance inefficiencies
- Security weaknesses

**Minor Issues (Consider Addressing):**
- Expression improvements
- Documentation gaps
- Naming convention inconsistencies
- Optimization opportunities
- Best practice deviations

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Workflow_Review_Report_YYYY-MM-DD-HHMMSS.ipynb**
   - Comprehensive review findings
   - Issue categorization (critical, major, minor)
   - Overall review score and level
   - Detailed recommendations by category

2. **Architecture_Assessment_YYYY-MM-DD-HHMMSS.ipynb**
   - Workflow architecture evaluation
   - Pattern appropriateness analysis
   - Scalability and extensibility review
   - Alternative architecture suggestions

3. **Implementation_Recommendations_YYYY-MM-DD-HHMMSS.ipynb**
   - Specific improvement recommendations
   - Before/after examples for key changes
   - Implementation priority and effort
   - Expected quality improvements

## Advanced Review Areas

### 7. Production vs Test Environment Review

**Environment-Aware Configuration Assessment:**

**MANDATORY: Review $execution.mode usage for environment separation**

```javascript
// Review environment-aware patterns
const environmentReview = {
  // Check for $execution.mode usage
  usesExecutionMode: workflowJSON.nodes.some(n =>
    n.parameters?.jsCode?.includes('$execution.mode') ||
    n.parameters?.url?.includes('$execution.mode')
  ),

  // Environment-specific configuration patterns
  environmentPatterns: workflowJSON.nodes.map(node => ({
    name: node.name,
    type: node.type,
    hasEnvironmentLogic: checkEnvironmentLogic(node),
    recommendation: getEnvironmentRecommendation(node)
  })),

  // Production readiness
  productionReadiness: {
    testEndpointsIsolated: checkTestEndpointIsolation(),
    productionDataProtected: checkProductionDataProtection(),
    environmentVariablesUsed: checkEnvironmentVariables()
  }
}
```

**Environment-Aware Best Practices:**
```javascript
// HTTP Request node with environment awareness
{
  "parameters": {
    "url": "={{ $execution.mode === 'test' ? 'https://test-api.example.com' : 'https://api.example.com' }}/endpoint",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "{{ $execution.mode === 'test' ? 'testApiCredentials' : 'prodApiCredentials' }}"
  },
  "type": "n8n-nodes-base.httpRequest"
}

// Code node with environment-specific logic
{
  "parameters": {
    "jsCode": `
if ($execution.mode === 'test') {
  // Use test data and mock responses
  return {
    json: {
      apiKey: 'test-key-12345',
      endpoint: 'https://sandbox.api.com',
      rateLimitBypass: true
    }
  };
} else if ($execution.mode === 'production') {
  // Use production credentials and endpoints
  return {
    json: {
      apiKey: $credentials.prodAPI.apiKey,
      endpoint: 'https://api.example.com',
      enableLogging: true,
      enableMonitoring: true
    }
  };
}
`
  },
  "type": "n8n-nodes-base.code"
}

// Webhook with environment-specific paths
{
  "parameters": {
    "path": "={{ $execution.mode === 'test' ? 'test/webhook' : 'webhook' }}",
    "authentication": "{{ $execution.mode === 'test' ? 'none' : 'headerAuth' }}"
  },
  "type": "n8n-nodes-base.webhook"
}
```

**Environment Review Checklist:**
- [ ] $execution.mode used to separate test and production endpoints
- [ ] Test environment uses sandbox/test API endpoints
- [ ] Production environment uses production credentials
- [ ] Environment-specific configuration clearly documented
- [ ] Test data isolation from production data
- [ ] Environment variables used for configuration
- [ ] No hardcoded production credentials in test mode
- [ ] Clear environment switching mechanism

### 8. Webhook Configuration Review

**Webhook Security and Functionality Assessment:**

**MANDATORY: Review webhook authentication and configuration**

```javascript
// Webhook configuration review
const webhookReview = {
  webhooks: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.webhook')
    .map(webhook => ({
      name: webhook.name,
      path: webhook.parameters.path,

      // Authentication review
      authentication: {
        method: webhook.parameters.authentication || 'none',
        isSecure: webhook.parameters.authentication !== 'none',
        hasHMAC: webhook.parameters.options?.rawBody === true,
        hasIPWhitelist: webhook.parameters.options?.ipWhitelist?.length > 0,
        recommendation: getAuthRecommendation(webhook.parameters)
      },

      // Request handling review
      requestHandling: {
        httpMethod: webhook.parameters.httpMethod,
        responseMode: webhook.parameters.responseMode,
        hasCustomResponse: webhook.parameters.options?.noResponseBody === false,
        handlesErrors: checkErrorHandling(webhook)
      },

      // Payload validation
      payloadValidation: {
        hasValidation: checkPayloadValidation(webhook),
        validationNode: findValidationNode(webhook.name),
        validatesRequired: checkRequiredFieldValidation(webhook)
      }
    })),

  // Overall webhook security score
  securityScore: calculateWebhookSecurityScore()
}
```

**Webhook Security Best Practices:**
```javascript
// Secure webhook with HMAC validation
{
  "parameters": {
    "httpMethod": "POST",
    "path": "customer-events",
    "authentication": "headerAuth",        // Basic security
    "options": {
      "rawBody": true,                    // Enable HMAC validation
      "allowedOrigins": [
        "https://trusted-service.com"
      ],
      "ipWhitelist": [
        "192.168.1.0/24",
        "10.0.0.0/8"
      ]
    }
  },
  "type": "n8n-nodes-base.webhook"
}

// Webhook with payload validation
{
  "connections": {
    "Customer Webhook": {
      "main": [[{ "node": "Validate Payload", "type": "main", "index": 0 }]],
      "error": [[{ "node": "Invalid Request Response", "type": "main", "index": 0 }]]
    }
  }
}

// Payload validation Code node
{
  "parameters": {
    "jsCode": `
// HMAC signature validation
const crypto = require('crypto');
const receivedSignature = $json.headers['x-hmac-sha256'];
const payload = JSON.stringify($json.body);
const secret = $credentials.webhookSecret.secret;
const expectedSignature = crypto.createHmac('sha256', secret).update(payload).digest('hex');

if (receivedSignature !== expectedSignature) {
  throw new Error('Invalid HMAC signature');
}

// Required field validation
if (!$json.body.id || !$json.body.eventType || !$json.body.data) {
  throw new Error('Missing required fields: id, eventType, or data');
}

return { json: $json.body };
`
  },
  "name": "Validate Payload",
  "type": "n8n-nodes-base.code",
  "continueOnFail": true
}
```

**Webhook Review Checklist:**
- [ ] Authentication configured (not 'none' for production)
- [ ] HMAC signature validation implemented (rawBody: true)
- [ ] IP whitelisting configured for known sources
- [ ] Allowed origins specified for CORS
- [ ] Payload validation node present
- [ ] Required field validation implemented
- [ ] Error responses properly configured
- [ ] Custom response messages for security (don't leak info)
- [ ] Webhook paths follow naming conventions
- [ ] Request logging implemented

### 9. Pagination Handling Review

**API Pagination Pattern Assessment:**

**MANDATORY: Review pagination implementation for data completeness**

```javascript
// Pagination pattern review
const paginationReview = {
  apiNodes: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.httpRequest')
    .map(node => ({
      name: node.name,

      // Pagination detection
      hasPagination: checkPaginationPattern(node),

      // Pagination methods
      paginationMethod: identifyPaginationMethod(node),
      // Methods: 'offset-limit', 'cursor', 'page-number', 'link-header', 'none'

      // Completeness checks
      fetchesAllPages: checkCompleteFetch(node),
      hasLoopLogic: checkLoopPattern(node),
      hasStopCondition: checkStopCondition(node),

      // Data handling
      aggregatesResults: checkResultAggregation(node),
      handlesErrors: checkPaginationErrors(node)
    })),

  // Overall pagination quality
  paginationQuality: calculatePaginationQuality()
}
```

**Pagination Best Practices:**

**Offset/Limit Pagination:**
```javascript
// Loop Over Items with pagination
{
  "nodes": [
    {
      "parameters": {
        "jsCode": `
// Generate pagination parameters
const pageSize = 100;
const totalPages = Math.ceil(5000 / pageSize);  // Assuming 5000 total items

const pages = Array.from({ length: totalPages }, (_, i) => ({
  offset: i * pageSize,
  limit: pageSize
}));

return pages.map(p => ({ json: p }));
`
      },
      "name": "Generate Pages",
      "type": "n8n-nodes-base.code"
    },
    {
      "parameters": {
        "url": "https://api.example.com/data?offset={{ $json.offset }}&limit={{ $json.limit }}",
        "method": "GET"
      },
      "name": "Fetch Page",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "parameters": {
        "aggregate": "aggregateAllItemData"
      },
      "name": "Aggregate Results",
      "type": "n8n-nodes-base.aggregate"
    }
  ]
}
```

**Cursor-Based Pagination:**
```javascript
// Recursive pagination with cursor
{
  "parameters": {
    "jsCode": `
const allResults = [];
let cursor = null;
let hasMore = true;

while (hasMore) {
  const url = cursor
    ? \`https://api.example.com/data?cursor=\${cursor}\`
    : 'https://api.example.com/data';

  const response = await $http.get(url);

  allResults.push(...response.data.items);

  cursor = response.data.nextCursor;
  hasMore = response.data.hasMore;

  // Safety limit
  if (allResults.length > 10000) {
    console.warn('Reached 10,000 item limit, stopping pagination');
    break;
  }
}

return allResults.map(item => ({ json: item }));
`
  },
  "name": "Fetch All Pages (Cursor)",
  "type": "n8n-nodes-base.code"
}
```

**Pagination Review Checklist:**
- [ ] Pagination implemented for APIs with multiple pages
- [ ] Appropriate pagination method used (offset, cursor, page)
- [ ] All pages fetched (loop until complete)
- [ ] Stop condition implemented (prevent infinite loops)
- [ ] Results properly aggregated
- [ ] Rate limiting between page requests
- [ ] Error handling for failed pages
- [ ] Maximum page limit safety check
- [ ] Pagination state tracked if needed

### 10. Custom Execution Data Review

**$execution.customData Usage Assessment:**

**MANDATORY: Review execution metadata and correlation**

```javascript
// Custom execution data review
const executionDataReview = {
  // Check for custom execution data usage
  usesCustomData: workflowJSON.nodes.some(n =>
    n.parameters?.jsCode?.includes('$execution.customData')
  ),

  // Execution metadata tracking
  metadataTracking: {
    tracksSource: checkSourceTracking(),
    tracksUser: checkUserTracking(),
    tracksPriority: checkPriorityTracking(),
    tracksCorrelation: checkCorrelationTracking()
  },

  // Data flow analysis
  dataFlow: workflowJSON.nodes
    .filter(n => n.type === 'n8n-nodes-base.code')
    .map(node => ({
      name: node.name,
      setsCustomData: node.parameters.jsCode?.includes('customData ='),
      readsCustomData: node.parameters.jsCode?.includes('$execution.customData'),
      customDataFields: extractCustomDataFields(node)
    })),

  // Use cases identified
  useCases: identifyCustomDataUseCases()
}
```

**Custom Execution Data Best Practices:**
```javascript
// Set custom execution data at workflow start
{
  "parameters": {
    "jsCode": `
// Set execution metadata
$execution.customData = {
  source: $json.headers['x-source'] || 'unknown',
  requestId: $json.headers['x-request-id'] || $execution.id,
  priority: $json.priority || 'normal',
  customerId: $json.customerId,
  environment: $execution.mode === 'test' ? 'test' : 'production',
  startTime: new Date().toISOString()
};

return { json: $json };
`
  },
  "name": "Set Execution Metadata",
  "type": "n8n-nodes-base.code"
}

// Use custom execution data for routing
{
  "parameters": {
    "conditions": {
      "conditions": [
        {
          "leftValue": "={{ $execution.customData.priority }}",
          "rightValue": "high",
          "operator": { "type": "string", "operation": "equals" }
        }
      ]
    }
  },
  "name": "Route by Priority",
  "type": "n8n-nodes-base.if"
}

// Use custom execution data for logging
{
  "parameters": {
    "jsCode": `
const logEntry = {
  timestamp: new Date().toISOString(),
  execution_id: $execution.id,
  request_id: $execution.customData?.requestId,
  customer_id: $execution.customData?.customerId,
  source: $execution.customData?.source,
  priority: $execution.customData?.priority,
  node: $node.name,
  result: $json
};

console.log(JSON.stringify(logEntry));
return { json: $json };
`
  },
  "name": "Log with Execution Context",
  "type": "n8n-nodes-base.code"
}

// Use for execution correlation across workflows
{
  "parameters": {
    "url": "https://api.example.com/process",
    "headers": {
      "X-Request-ID": "={{ $execution.customData.requestId }}",
      "X-Source-Workflow": "={{ $workflow.name }}"
    }
  },
  "name": "API Call with Correlation",
  "type": "n8n-nodes-base.httpRequest"
}
```

**Custom Execution Data Review Checklist:**
- [ ] Custom execution data set at workflow entry
- [ ] Execution correlation ID tracked (request ID)
- [ ] Source system/channel tracked
- [ ] User/customer context tracked
- [ ] Priority/urgency tracked
- [ ] Custom data used for routing decisions
- [ ] Custom data included in logging
- [ ] Custom data passed to external systems (headers)
- [ ] Custom data used for monitoring/alerting

### 11. Monitoring Implementation Review

**Observability and Logging Assessment:**

**MANDATORY: Review monitoring and logging implementation**

```javascript
// Monitoring implementation review
const monitoringReview = {
  // Logging coverage
  logging: {
    hasStructuredLogging: checkStructuredLogging(),
    logsCriticalEvents: checkCriticalEventLogging(),
    logsExecutionMetadata: checkMetadataLogging(),
    logsPerformanceMetrics: checkPerformanceLogging(),
    logsSensitiveDataSafely: checkSensitiveDataMasking()
  },

  // Metrics collection
  metrics: {
    tracksExecutionDuration: checkDurationTracking(),
    tracksErrorRates: checkErrorRateTracking(),
    tracksAPILatency: checkLatencyTracking(),
    tracksThroughput: checkThroughputTracking()
  },

  // Alerting configuration
  alerting: {
    hasErrorAlerts: workflowJSON.settings?.errorWorkflow !== undefined,
    hasPerformanceAlerts: checkPerformanceAlerts(),
    hasAvailabilityAlerts: checkAvailabilityAlerts(),
    alertChannels: identifyAlertChannels()
  },

  // External monitoring integration
  externalMonitoring: {
    hasAPMIntegration: checkAPMIntegration(),
    hasLogAggregation: checkLogAggregation(),
    hasMetricsExport: checkMetricsExport()
  }
}
```

**Monitoring Best Practices:**

**Structured Logging Implementation:**
```javascript
{
  "parameters": {
    "jsCode": `
// Structured log entry
const logEntry = {
  // Standard fields
  timestamp: new Date().toISOString(),
  level: 'INFO',  // DEBUG, INFO, WARN, ERROR, CRITICAL
  service: 'n8n-workflow',

  // Execution context
  execution: {
    id: $execution.id,
    workflow_id: $workflow.id,
    workflow_name: $workflow.name,
    node_name: $node.name,
    mode: $execution.mode
  },

  // Custom context
  context: {
    customer_id: $execution.customData?.customerId,
    request_id: $execution.customData?.requestId,
    source: $execution.customData?.source
  },

  // Event details
  event: {
    type: 'api_call_success',
    description: 'Customer data retrieved from CRM',
    duration_ms: Date.now() - $execution.startedAt,
    record_count: $json.items?.length || 0
  },

  // Sensitive data masking
  data: {
    id: $json.id,
    email: maskEmail($json.email),  // user@example.com -> u***@example.com
    recordsProcessed: $json.items?.length
  }
};

// Output to console (picked up by log aggregator)
console.log(JSON.stringify(logEntry));

return { json: $json };
`
  },
  "name": "Structured Logger",
  "type": "n8n-nodes-base.code"
}
```

**Performance Metrics Tracking:**
```javascript
{
  "parameters": {
    "jsCode": `
// Track performance metrics
const metrics = {
  workflow_id: $workflow.id,
  execution_id: $execution.id,
  timestamp: new Date().toISOString(),

  // Performance metrics
  performance: {
    total_duration_ms: Date.now() - $execution.startedAt,
    node_durations: $getWorkflowStaticData('node').nodeDurations || {},
    api_latency_ms: Date.now() - apiCallStart,
    transformation_time_ms: Date.now() - transformStart
  },

  // Throughput metrics
  throughput: {
    items_processed: $input.all().length,
    items_output: $json.items?.length || 0,
    items_per_second: ($json.items?.length || 0) / ((Date.now() - $execution.startedAt) / 1000)
  },

  // Resource metrics
  resources: {
    memory_used_mb: process.memoryUsage().heapUsed / 1024 / 1024,
    queue_size: $getWorkflowStaticData('global').queueSize || 0
  }
};

// Send metrics to monitoring system
await $http.post('https://metrics.example.com/api/metrics', metrics);

return { json: $json };
`
  },
  "name": "Track Performance Metrics",
  "type": "n8n-nodes-base.code"
}
```

**Monitoring Review Checklist:**
- [ ] Structured logging implemented (JSON format)
- [ ] Critical events logged (start, success, error)
- [ ] Execution metadata included in logs
- [ ] Performance metrics tracked and logged
- [ ] Sensitive data masked in logs
- [ ] Error rate tracking implemented
- [ ] API latency tracked
- [ ] Throughput metrics collected
- [ ] Error Trigger workflow configured for alerts
- [ ] External monitoring integration (APM, logs)
- [ ] Log aggregation configured (ELK, Splunk)
- [ ] Metrics export configured (Prometheus, Grafana)
- [ ] Alert channels configured (Slack, email)

## Success Criteria

- [ ] Complete workflow architecture reviewed and assessed
- [ ] All nodes evaluated for appropriateness and configuration
- [ ] Expression quality comprehensively analyzed
- [ ] Error handling coverage thoroughly assessed
- [ ] Security and compliance reviewed
- [ ] Performance optimization opportunities identified
- [ ] Overall review score and level assigned
- [ ] All issues categorized by severity and impact
- [ ] Actionable recommendations provided with examples
- [ ] All deliverables created with proper reverse date stamps
- [ ] Implementation priorities clearly defined with effort estimates

**Production vs Test Review:**
- [ ] $execution.mode usage validated for environment separation
- [ ] Test endpoints properly isolated
- [ ] Production credentials protected
- [ ] Environment-specific configuration documented
- [ ] Environment variables used appropriately

**Webhook Configuration Review:**
- [ ] Webhook authentication configured (not 'none')
- [ ] HMAC signature validation implemented
- [ ] Payload validation present
- [ ] IP whitelisting configured
- [ ] Error responses properly configured

**Pagination Handling Review:**
- [ ] Pagination implemented for multi-page APIs
- [ ] All pages fetched completely
- [ ] Stop conditions implemented
- [ ] Results properly aggregated
- [ ] Rate limiting between pages

**Custom Execution Data Review:**
- [ ] Custom execution data used for correlation
- [ ] Source/user/priority tracked
- [ ] Execution metadata in logging
- [ ] Custom data used for routing
- [ ] Correlation IDs tracked

**Monitoring Implementation Review:**
- [ ] Structured logging implemented
- [ ] Performance metrics tracked
- [ ] Error rate monitoring configured
- [ ] Alert channels configured
- [ ] External monitoring integrated
- [ ] Sensitive data masked in logs

## Command Integration

- **Previous Phase**: `n8n-workflow-implementation`, `n8n-workflow-lint-quality-check`, or `n8n-workflow-quality-analysis`
- **Parallel**: `n8n-workflow-quality-analysis` (metric-based analysis), `n8n-workflow-gap-analysis` (requirements comparison)
- **Next Phase**: `n8n-workflow-refactor` (apply improvements) or workflow deployment

## Next Phase Preparation

After review completion, proceed based on findings:

```bash
# If review score is below B (< 80%), refactor workflow:
/n8n-workflow-refactor --workflow-id=<id> \
  --review-report="Workflow_Review_Report_YYYY-MM-DD-HHMMSS.ipynb" \
  --focus-areas="critical-issues,major-issues"

# If review is acceptable but gaps exist, run gap analysis:
/n8n-workflow-gap-analysis --workflow-id=<id> \
  --review-findings="Implementation_Recommendations_YYYY-MM-DD-HHMMSS.ipynb"

# If review is excellent (A level), proceed to deployment preparation
```

---

**Note**: This is a review command that produces comprehensive workflow assessment reports with human-centric analysis and actionable recommendations. No workflow modifications occur during review. Use refactor command to implement improvements.
