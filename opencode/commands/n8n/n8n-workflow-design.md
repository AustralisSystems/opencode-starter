# N8N Workflow Design Command

**YAML Prompt**: `n8n-workflow-design-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Detailed workflow architecture design including node configuration, connection architecture, expression planning, and error handling design. This command transforms planning artifacts into concrete workflow designs with validated node configurations ready for implementation.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n node configuration patterns and best practices
- `grep` - Real-world node configuration examples on GitHub
- `sequential-thinking` - Structured design methodology
- `filesystem` - Read planning artifacts and existing workflows
- `memory` - Track design decisions and configuration choices
- `time` - Timestamp design activities

**n8n-Specific MCP Tools:**
- `get_node_essentials` - Quick node understanding (10-20 essential properties)
- `get_node_for_task` - Pre-configured node templates for common tasks
- `search_node_properties` - Find specific node properties (e.g., authentication)
- `get_property_dependencies` - Understand property relationships
- `get_node_documentation` - Comprehensive node documentation when needed
- `validate_node_minimal` - Quick required fields validation
- `validate_node_operation` - Full configuration validation with profile
- `get_template` - Retrieve template for customization (if using template)

## Template-First Workflow Strategy

**ALWAYS CHECK FOR EXISTING TEMPLATES FIRST (2,500+ available, 97.5% have metadata):**

### 1. Retrieve Selected Template (If Applicable)
```javascript
// From planning phase, if template was selected
get_template(templateId, {
  mode: 'full',           // Get complete workflow structure
  includeMetadata: true   // Include metadata for attribution
})
```

### 2. Template Customization Strategy
- Validate template against current n8n version
- Map template nodes to planned requirements
- Identify nodes requiring configuration changes
- Plan additional nodes or connections needed
- Document customization rationale

**Template Usage Best Practices:**
- Templates save 70-90% design time
- **MANDATORY ATTRIBUTION**: "Based on template by **[Author Name]** (@username) - [template URL on n8n.io]"
- Validate all node configurations (templates may be outdated)
- Customize expressions to match your data structure
- Update error handling for production requirements

## Node Discovery Strategy

### Progressive Node Discovery Approach

**1. Load Essential Node Information:**
```javascript
// START HERE for quick node understanding (80-90% token savings)
get_node_essentials('n8n-nodes-base.httpRequest')
// Returns only 10-20 essential properties
```

**2. Targeted Property Search:**
```javascript
// Find specific configuration aspects
search_node_properties('n8n-nodes-base.postgres', 'authentication')
search_node_properties('n8n-nodes-base.slack', 'channel')
```

**3. Get Pre-Configured Templates:**
```javascript
// Get working configurations immediately
get_node_for_task('send_email')        // Email sending config
get_node_for_task('store_data')        // Database storage config
get_node_for_task('transform_json')    // Data transformation config
```

**4. Understand Property Dependencies:**
```javascript
// Before setting complex properties
get_property_dependencies('n8n-nodes-base.httpRequest', 'authentication')
// Returns: which properties are required/optional based on selection
```

**5. Full Documentation (When Needed):**
```javascript
// Comprehensive human-readable docs
get_node_documentation('n8n-nodes-base.slack')
```

## Node Configuration Design

### Configuration Design Matrix

**For Each Node in Workflow:**

1. **Node Selection Validation**
   - Verify node type meets requirement
   - Check node capabilities against needs
   - Validate node is available in target n8n version

2. **Essential Configuration Design**
   ```javascript
   // Design essential parameters first
   {
     "resource": "message",           // Primary resource type
     "operation": "send",             // Operation to perform
     "authentication": "oauth2",      // Auth method
     // ... essential parameters only
   }
   ```

3. **Property Dependency Planning**
   - Identify dependent properties
   - Plan configuration sequence
   - Design conditional configurations

4. **Pre-Validation Strategy**
   ```javascript
   // Validate configuration before building
   validate_node_minimal('n8n-nodes-base.slack', {
     resource: 'message',
     operation: 'send',
     channel: '#general'
   })

   // Full validation with profile
   validate_node_operation('n8n-nodes-base.slack', fullConfig, 'runtime')
   ```

### Authentication & Credentials Design

**Credential Configuration Patterns:**

1. **OAuth2 Authentication**
   ```javascript
   {
     "authentication": "oauth2",
     "oauthTokenUrl": "https://oauth.service.com/token",
     "clientId": "={{$credentials.clientId}}",
     "clientSecret": "={{$credentials.clientSecret}}"
   }
   ```

2. **API Key Authentication**
   ```javascript
   {
     "authentication": "apiKey",
     "apiKeyLocation": "header",
     "apiKeyName": "Authorization",
     "apiKeyValue": "={{$credentials.apiKey}}"
   }
   ```

3. **Basic Authentication**
   ```javascript
   {
     "authentication": "basicAuth",
     "user": "={{$credentials.user}}",
     "password": "={{$credentials.password}}"
   }
   ```

## Connection Architecture Design

### Data Flow Mapping

**1. Main Execution Path:**
```
[Trigger Node]
     (main output)
[Transform Node]
     (main output)
[Action Node]
     (main output)
[Success Notification]
```

**2. Error Handling Path:**
```
[Any Node]
     (error output)
[Error Handler Node]
     (main output)
[Error Notification/Recovery]
```

**3. Branching Logic:**
```
[Trigger Node]
    
[IF Node]
     (true)  [Action A]
     (false)  [Action B]
```

**4. Parallel Processing:**
```
[Trigger Node]
    
[Split In Batches]
      [API Call 1]
      [API Call 2]
      [API Call 3]
        
    [Merge Node]
```

### Connection Type Design

**Main Connections:**
- Primary data flow between nodes
- Successful execution path
- Expected data transformations

**Error Connections:**
- Error handling and recovery
- Fallback operations
- Notification of failures

**Conditional Connections:**
- IF node branching
- Switch node routing
- Filter node splitting

## Expression Planning

### Data Transformation Expressions

**1. Basic Data Access:**
```javascript
// Current node output
$json.fieldName

// Specific node output
$node["NodeName"].json.fieldName

// Array item access
$json.items[0].value

// Previous node data
$input.all()[0].json.data
```

**2. Data Transformation:**
```javascript
// String manipulation
{{ $json.email.toLowerCase() }}
{{ $json.name.trim().split(' ')[0] }}

// Number operations
{{ $json.price * 1.1 }}  // Add 10%
{{ Math.round($json.value * 100) / 100 }}  // Round to 2 decimals

// Date operations
{{ new Date($json.timestamp).toISOString() }}
{{ DateTime.now().plus({ days: 7 }).toISO() }}  // Luxon
```

**3. Conditional Logic:**
```javascript
// Ternary operators
{{ $json.status === 'active' ? 'enabled' : 'disabled' }}

// Null coalescing
{{ $json.customField ?? 'default value' }}

// Complex conditions
{{ $json.score > 80 ? 'excellent' : $json.score > 60 ? 'good' : 'needs improvement' }}
```

**4. Array Operations:**
```javascript
// Map array
{{ $json.items.map(item => item.id) }}

// Filter array
{{ $json.items.filter(item => item.active === true) }}

// Reduce array
{{ $json.items.reduce((sum, item) => sum + item.price, 0) }}
```

### Expression Validation Strategy

**Pre-Build Validation:**
- Test expressions with sample data
- Validate syntax before workflow creation
- Check for common errors (undefined, null)
- Plan fallback values

**Validation Tools:**
```javascript
// Will be validated during workflow validation
validate_workflow_expressions(workflow)
```

## Error Handling Design

### Error Handling Patterns

**1. Try-Catch Pattern:**
```
[Trigger]
    
[Set: Try Block]
    
[Risky Operation]
     (success)  [Success Action]
     (error)  [Error Handler]  [Notification]
```

**2. Fallback Pattern:**
```
[Primary API Call]
     (success)  [Process Data]
     (error)  [Fallback API]  [Process Data]
```

**3. Retry Pattern:**
```
[API Call with Retry]
    - Configure: maxRetries: 3
    - Configure: retryDelay: 1000ms
     (success)  [Continue]
     (final error)  [Error Handler]
```

**4. Graceful Degradation:**
```
[Main Workflow]
     (error)  [Log Error]  [Partial Success Response]
```

### Error Configuration Design

**Node-Level Error Handling:**
```javascript
{
  "continueOnFail": true,           // Continue workflow on error
  "retryOnFail": true,              // Automatic retry
  "maxTries": 3,                    // Max retry attempts
  "waitBetweenTries": 1000         // Delay between retries
}
```

**Workflow-Level Error Handling:**
- Design error output connections
- Plan error notification strategy
- Define recovery procedures
- Document error scenarios

## Error Trigger Workflow Design

### Centralized Error Handling Architecture

**MANDATORY: Design Error Trigger workflows for production-grade error handling**

**1. Error Trigger Workflow Pattern:**

```javascript
// Main Workflow Configuration
{
  "settings": {
    "errorWorkflow": "error_handler_workflow_id"
  }
}

// Error Trigger Workflow Design:
[Error Trigger]  // Automatically triggered on any workflow error

[Code Node: Format Error]
{
  "errorDetails": {
    "workflow_id": "{{ $json.workflow.id }}",
    "workflow_name": "{{ $json.workflow.name }}",
    "execution_id": "{{ $json.execution.id }}",
    "error_message": "{{ $json.error.message }}",
    "error_node": "{{ $json.error.node.name }}",
    "error_timestamp": "{{ $now.toISO() }}",
    "error_stack": "{{ $json.error.stack }}"
  }
}

[Switch Node: Error Severity]
  (critical)  [Slack Alert]  [PagerDuty Alert]
  (warning)   [Email Notification]
  (info)      [Log to Database]
```

**Design Checklist:**
- [ ] Create dedicated Error Trigger workflow for each critical workflow
- [ ] Design error data formatting and enrichment logic
- [ ] Plan error severity classification (critical, warning, info)
- [ ] Design notification routing based on severity
- [ ] Plan error logging and persistence strategy

**2. Node-Level Error Configuration Design:**

```javascript
// For Each Critical Node, Design Error Config:
{
  "name": "API Call to External Service",
  "type": "n8n-nodes-base.httpRequest",
  "continueOnFail": true,        // Don't halt entire workflow
  "retryOnFail": true,           // Automatic retry
  "maxTries": 3,                 // 3 retry attempts
  "waitBetweenTries": 2000,      // 2 seconds between retries
  "alwaysOutputData": true,      // Output data even on fail
  "onError": "continueErrorOutput"  // Send to error connection
}
```

**Error Configuration Strategy:**
- **API Calls**: Always enable retry (maxTries: 3, wait: 1000-3000ms)
- **Database Operations**: Retry with exponential backoff
- **Data Transformations**: continueOnFail for partial processing
- **Notifications**: No retry, but log failures
- **Critical Operations**: Halt workflow on error (continueOnFail: false)

**3. Error Connection Architecture Design:**

```
Main Path Design:
[Webhook Trigger]
    (main)
[Validate Input]
    (main)         (error)
[API Call]      [Validation Error Handler]  [400 Response]
    (main)         (error)
[Process Data]  [API Error Handler]  [Error Trigger]  [Alert]
    (main)
[Success Response]
```

**Connection Design Requirements:**
- [ ] Design main execution path for happy path
- [ ] Design error connections for each failure point
- [ ] Plan error output structure for each node
- [ ] Design error aggregation strategy (if multiple errors)
- [ ] Plan error recovery connections

**4. Custom Error Message Design:**

```javascript
// Code Node: Custom Error Formatting
const errorContext = {
  error: {
    type: "API_RATE_LIMIT_EXCEEDED",
    message: `Rate limit exceeded for ${$json.api_name}. Retry after ${$json.retry_after} seconds.`,
    severity: "warning",
    retry_strategy: "exponential_backoff",
    execution_context: {
      workflow_id: $workflow.id,
      workflow_name: $workflow.name,
      execution_id: $execution.id,
      node_name: $node.name,
      input_data: $json,
      timestamp: $now.toISO()
    },
    resolution_steps: [
      "Wait for retry_after period",
      "Check API quota status",
      "Contact API provider if persists"
    ]
  }
};

return errorContext;
```

**Custom Error Design Checklist:**
- [ ] Design structured error format with context
- [ ] Include execution metadata in error messages
- [ ] Design actionable resolution steps
- [ ] Plan error categorization taxonomy
- [ ] Design error correlation IDs for tracking

**5. Error Notification Channel Design:**

```javascript
// Slack Error Notification Design
{
  "channel": "#production-alerts",
  "blocks": [
    {
      "type": "header",
      "text": " Workflow Error: {{ $json.workflow_name }}"
    },
    {
      "type": "section",
      "fields": [
        {"type": "mrkdwn", "text": "*Error:* {{ $json.error_message }}"},
        {"type": "mrkdwn", "text": "*Node:* {{ $json.error_node }}"},
        {"type": "mrkdwn", "text": "*Execution ID:* {{ $json.execution_id }}"},
        {"type": "mrkdwn", "text": "*Time:* {{ $json.timestamp }}"}
      ]
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": "View Execution",
          "url": "https://n8n.yourcompany.com/execution/{{ $json.execution_id }}"
        }
      ]
    }
  ]
}
```

**Notification Design Requirements:**
- [ ] Design Slack/Discord message format with rich formatting
- [ ] Plan email notification templates (HTML)
- [ ] Design SMS alerts for critical errors (PagerDuty, Twilio)
- [ ] Plan notification routing rules (who gets what)
- [ ] Design notification rate limiting (avoid alert fatigue)

## Rate Limiting and Performance Design

### API Rate Limiting Architecture

**MANDATORY: Design rate limiting for all external API integrations**

**1. Loop Over Items with Wait Pattern Design:**

```javascript
// Pattern: Loop Over Items  API Call  Wait  Continue

// Loop Over Items Node Configuration:
{
  "name": "Loop Over API Requests",
  "type": "n8n-nodes-base.splitInBatches",
  "batchSize": 10,              // Process 10 items per batch
  "options": {
    "reset": false              // Don't reset between runs
  }
}

// HTTP Request Node (inside loop):
{
  "name": "API Call",
  "type": "n8n-nodes-base.httpRequest",
  "url": "https://api.service.com/resource/{{ $json.id }}",
  "method": "GET"
}

// Wait Node Configuration:
{
  "name": "Rate Limit Wait",
  "type": "n8n-nodes-base.wait",
  "amount": 200,                // 200ms wait
  "unit": "milliseconds"
}

// Result: 5 requests per second max (200ms * 5 = 1000ms)
```

**Rate Limit Design Strategy:**
- [ ] Identify API rate limits for each external service
- [ ] Calculate optimal batch sizes and wait times
- [ ] Design burst handling strategy
- [ ] Plan rate limit exceeded error handling
- [ ] Design dynamic rate limit adjustment (based on headers)

**2. Batching Strategy Design:**

```javascript
// Batch Processing Design for High-Volume Operations

// Database Bulk Insert Pattern:
{
  "batchSize": 1000,            // 1000 records per batch
  "operation": "insert",
  "table": "customer_data",
  "bulkInsert": true            // Use bulk insert API
}

// API Batch Endpoint Pattern:
{
  "endpoint": "/api/v1/batch",
  "method": "POST",
  "batchPayload": "{{ $json.items.slice(0, 100) }}", // 100 items per request
  "timeout": 30000              // 30 second timeout
}
```

**Batching Design Checklist:**
- [ ] Design batch sizes for database operations
- [ ] Plan API batch endpoint usage (if available)
- [ ] Design batch timeout configuration
- [ ] Plan batch failure handling (partial success)
- [ ] Design batch progress tracking

**3. Execution Timeout Design:**

```javascript
// Workflow-Level Timeout Configuration:
{
  "settings": {
    "executionTimeout": 300,    // 5 minutes max execution
    "maxExecutionTime": 600     // 10 minutes absolute max
  }
}

// Node-Level Timeout Configuration:
{
  "httpRequest": {
    "timeout": 30000,           // 30 second API timeout
    "continueOnFail": true      // Don't halt on timeout
  },
  "database": {
    "timeout": 60000,           // 1 minute DB timeout
    "retryOnTimeout": true
  },
  "webhook": {
    "timeout": 10000            // 10 second webhook timeout
  }
}
```

**Timeout Design Strategy:**
- [ ] Define workflow execution timeout based on requirements
- [ ] Design node-specific timeouts for each operation type
- [ ] Plan timeout error handling and notifications
- [ ] Design timeout retry strategy
- [ ] Plan timeout recovery procedures

**4. Static Data Management Design:**

```javascript
// Workflow Static Data Design
// Use $getWorkflowStaticData() for cross-execution persistence

// Rate Limit Counter Design:
const staticData = $getWorkflowStaticData('global');

if (!staticData.rateLimitCounter) {
  staticData.rateLimitCounter = {
    count: 0,
    resetTime: new Date().getTime() + 3600000  // 1 hour window
  };
}

// Check and update counter
if (new Date().getTime() > staticData.rateLimitCounter.resetTime) {
  staticData.rateLimitCounter = { count: 0, resetTime: new Date().getTime() + 3600000 };
}

staticData.rateLimitCounter.count++;

// State Tracking Design:
staticData.lastProcessedId = $json.id;
staticData.processingStage = 'enrichment';
staticData.errorCount = (staticData.errorCount || 0) + 1;
```

**Static Data Design Checklist:**
- [ ] Design static data structure and schema
- [ ] Plan rate limit counter tracking
- [ ] Design processing state persistence
- [ ] Plan static data cleanup strategy
- [ ] Design static data size limits (avoid bloat)

## Webhook Security Design

### Secure Webhook Architecture

**MANDATORY: Design webhook security for all webhook-triggered workflows**

**1. Webhook Authentication Design:**

```javascript
// Header-Based Authentication:
{
  "webhookPath": "customer-webhook",
  "authenticationMethod": "headerAuth",
  "authentication": {
    "type": "generic",
    "properties": {
      "headerAuth": {
        "name": "X-API-Key",
        "value": "={{ $credentials.webhookApiKey }}"
      }
    }
  }
}

// HMAC Signature Validation:
{
  "webhookPath": "secure-webhook",
  "authenticationMethod": "hmacAuth",
  "authentication": {
    "type": "generic",
    "properties": {
      "hmacAuth": {
        "secret": "={{ $credentials.webhookSecret }}",
        "algorithm": "sha256",
        "encoding": "hex",
        "headerName": "X-Hub-Signature-256"
      }
    }
  }
}

// Basic Authentication:
{
  "webhookPath": "basic-auth-webhook",
  "authenticationMethod": "basicAuth",
  "authentication": {
    "type": "generic",
    "properties": {
      "basicAuth": {
        "user": "={{ $credentials.webhookUser }}",
        "password": "={{ $credentials.webhookPassword }}"
      }
    }
  }
}
```

**Security Design Checklist:**
- [ ] Select appropriate authentication method (headerAuth, hmacAuth, basicAuth, none)
- [ ] Design credential storage strategy
- [ ] Plan authentication failure handling
- [ ] Design request validation logic
- [ ] Plan IP whitelisting (if required)

**2. Request Validation Design:**

```javascript
// Code Node: Webhook Request Validation
const request = $json.body;
const headers = $json.headers;

// Validation checks:
const validations = {
  // 1. Required headers
  hasApiKey: headers['x-api-key'] === $credentials.webhookApiKey,

  // 2. Request structure
  hasRequiredFields: request.id && request.timestamp && request.data,

  // 3. Timestamp freshness (within 5 minutes)
  isFresh: (Date.now() - new Date(request.timestamp).getTime()) < 300000,

  // 4. Request signature (HMAC)
  validSignature: verifyHMAC(request, headers['x-signature']),

  // 5. Allowed origins
  allowedOrigin: ['https://trusted-service.com'].includes(headers['origin'])
};

// Validation result
if (Object.values(validations).every(v => v === true)) {
  return { valid: true, data: request };
} else {
  throw new Error(`Webhook validation failed: ${JSON.stringify(validations)}`);
}
```

**Validation Design Requirements:**
- [ ] Design required field validation
- [ ] Plan timestamp freshness check
- [ ] Design signature verification logic
- [ ] Plan origin/referrer validation
- [ ] Design malformed request handling

**3. IP Whitelisting Design:**

```javascript
// Code Node: IP Whitelist Validation
const allowedIPs = [
  '192.168.1.0/24',         // Internal network
  '203.0.113.0/24',         // Partner network
  '198.51.100.42'           // Specific IP
];

const requestIP = $json.headers['x-forwarded-for'] || $json.headers['x-real-ip'];

function isIPAllowed(ip, whitelist) {
  // IP validation logic
  // Support CIDR notation and exact matches
  return whitelist.some(allowed => matchesIPRange(ip, allowed));
}

if (!isIPAllowed(requestIP, allowedIPs)) {
  return {
    statusCode: 403,
    body: { error: 'IP not whitelisted' }
  };
}
```

**IP Whitelisting Design:**
- [ ] Define allowed IP ranges (CIDR notation)
- [ ] Plan IP validation logic
- [ ] Design IP blocking response
- [ ] Plan dynamic IP whitelist updates
- [ ] Design IP logging for security audit

## CI/CD Pipeline Design

### Deployment Automation Architecture

**MANDATORY: Design CI/CD integration for production workflows**

**1. GitHub Actions Workflow Design:**

```yaml
# .github/workflows/n8n-deploy.yml
name: Deploy n8n Workflows

on:
  push:
    branches: [main]
    paths:
      - 'workflows/**/*.json'

jobs:
  validate-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Validate workflow JSON
        run: |
          for file in workflows/*.json; do
            jq empty "$file" || exit 1
          done

      - name: n8n CLI validation
        run: |
          npm install -g n8n
          n8n validate-workflow workflows/*.json

      - name: Deploy to n8n instance
        env:
          N8N_API_KEY: ${{ secrets.N8N_API_KEY }}
          N8N_BASE_URL: ${{ secrets.N8N_BASE_URL }}
        run: |
          for file in workflows/*.json; do
            curl -X POST "$N8N_BASE_URL/api/v1/workflows" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" \
              -H "Content-Type: application/json" \
              -d @"$file"
          done

      - name: Run integration tests
        run: |
          npm run test:integration
```

**CI/CD Design Checklist:**
- [ ] Design workflow validation step (JSON syntax, n8n validation)
- [ ] Plan automated testing integration
- [ ] Design deployment strategy (staging, production)
- [ ] Plan rollback procedures
- [ ] Design deployment notifications

**2. Version Control Integration Design:**

```javascript
// Workflow Metadata for Version Control
{
  "name": "Customer Onboarding Workflow",
  "version": "2.5.0",
  "description": "Automated customer onboarding with CRM integration",
  "tags": ["production", "customer", "crm"],
  "settings": {
    "saveExecutionProgress": true,
    "saveDataSuccessExecution": "all",
    "saveDataErrorExecution": "all"
  },
  "meta": {
    "gitCommit": "a1b2c3d4",
    "deployedBy": "github-actions",
    "deployedAt": "2025-01-02T15:30:00Z",
    "environment": "production"
  }
}
```

**Version Control Design:**
- [ ] Design workflow versioning strategy (semantic versioning)
- [ ] Plan Git commit hooks for workflow changes
- [ ] Design change log generation
- [ ] Plan workflow diffing and comparison
- [ ] Design workflow backup before deployment

**3. Environment-Specific Configuration Design:**

```javascript
// Use $execution.mode for environment detection
const config = {
  development: {
    apiUrl: 'https://dev-api.service.com',
    webhookUrl: 'http://localhost:5678/webhook',
    logLevel: 'debug',
    notificationChannel: '#dev-alerts'
  },
  staging: {
    apiUrl: 'https://staging-api.service.com',
    webhookUrl: 'https://staging-n8n.company.com/webhook',
    logLevel: 'info',
    notificationChannel: '#staging-alerts'
  },
  production: {
    apiUrl: 'https://api.service.com',
    webhookUrl: 'https://n8n.company.com/webhook',
    logLevel: 'warn',
    notificationChannel: '#production-alerts'
  }
};

// Auto-detect environment
const environment = $execution.mode === 'manual' ? 'development' :
                   process.env.N8N_ENV || 'production';

const currentConfig = config[environment];
```

**Environment Design Checklist:**
- [ ] Design environment detection logic
- [ ] Plan environment-specific configurations
- [ ] Design credential switching per environment
- [ ] Plan environment variable usage
- [ ] Design environment validation

## Validation Strategy

### Pre-Build Validation

**1. Node Configuration Validation:**
```javascript
// Quick required fields check
validate_node_minimal(nodeType, minimalConfig)

// Full operation-aware validation
validate_node_operation(nodeType, fullConfig, 'runtime')
```

**2. Property Dependency Validation:**
```javascript
// Ensure all dependencies are met
get_property_dependencies(nodeType, propertyName)
```

**3. Configuration Completeness Check:**
- All required fields configured
- Authentication properly set
- Expressions syntax-checked
- Error handling configured

### Design Validation Checklist

- [ ] All nodes have validated configurations
- [ ] Authentication/credentials planned
- [ ] Expressions designed and syntax-checked
- [ ] Connections mapped (main and error paths)
- [ ] Error handling strategy defined
- [ ] Data transformations planned
- [ ] Performance considerations addressed
- [ ] Security requirements met

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Node_Configuration_Design_YYYY-MM-DD-HHMMSS.ipynb**
   - Complete node configuration specifications
   - Configuration validation results
   - Property dependencies documentation
   - Authentication and credential design
   - Node-level error handling configuration

2. **Connection_Architecture_YYYY-MM-DD-HHMMSS.ipynb**
   - Connection map with data flow visualization
   - Main execution path design
   - Error handling path design
   - Branching and conditional logic design
   - Parallel processing architecture (if applicable)

3. **Expression_and_Data_Mapping_YYYY-MM-DD-HHMMSS.ipynb**
   - Expression design for all data transformations
   - Expression syntax validation
   - Sample data with expected outputs
   - Fallback value strategies
   - Complex expression documentation

4. **Error_Handling_Strategy_YYYY-MM-DD-HHMMSS.ipynb**
   - Error handling pattern selection
   - Node-level error configuration
   - Workflow-level error handling design
   - Recovery and fallback procedures
   - Error notification design

## Success Criteria

**Core Design:**
- [ ] All nodes configured with validated parameters
- [ ] Node configurations pass validate_node_minimal checks
- [ ] Node configurations pass validate_node_operation validation
- [ ] Property dependencies identified and planned
- [ ] Authentication and credentials properly designed
- [ ] Connection map complete and validated
- [ ] Main execution path clearly defined
- [ ] Expressions designed and syntax-checked
- [ ] Data transformations planned with sample data
- [ ] All deliverables created with proper reverse date stamps
- [ ] Template attribution documented (if using template)
- [ ] Design ready for implementation phase

**Error Trigger Workflow Design:**
- [ ] Error Trigger workflow designed for centralized error handling
- [ ] Error workflow linked to main workflows via settings.errorWorkflow
- [ ] Node-level error configuration designed (continueOnFail, retryOnFail, maxTries, waitBetweenTries)
- [ ] Error connection architecture designed (main and error paths)
- [ ] Custom error message format designed with execution context
- [ ] Error notification channels designed (Slack, Discord, Email, PagerDuty)
- [ ] Error severity classification designed (critical, warning, info)

**Rate Limiting and Performance Design:**
- [ ] Loop Over Items with Wait pattern designed for rate limiting
- [ ] Batch sizes and wait times calculated for each API
- [ ] Batching strategy designed for high-volume operations
- [ ] Execution timeout configuration designed (workflow and node-level)
- [ ] Static data management designed for state persistence
- [ ] Rate limit exceeded error handling designed
- [ ] Performance optimization strategies documented

**Webhook Security Design:**
- [ ] Webhook authentication method selected (headerAuth, hmacAuth, basicAuth)
- [ ] Webhook credential configuration designed
- [ ] Request validation logic designed (headers, payload, signature)
- [ ] IP whitelisting designed (if required)
- [ ] Malformed request handling designed
- [ ] Webhook security testing approach planned

**CI/CD Pipeline Design:**
- [ ] GitHub Actions workflow designed for deployment automation
- [ ] Workflow validation steps designed (JSON syntax, n8n validation)
- [ ] Deployment strategy designed (staging, production)
- [ ] Version control integration designed (semantic versioning, Git hooks)
- [ ] Environment-specific configuration designed (dev, staging, production)
- [ ] Environment detection logic designed ($execution.mode)
- [ ] Rollback procedures designed
- [ ] Deployment notifications designed

## Command Integration

- **Previous Phase**: `n8n-workflow-planning` (strategic planning and template selection)
- **Next Phase**: `n8n-workflow-implementation` (workflow building and deployment)
- **Parallel**: `n8n-workflow-gap-analysis` (for existing workflow design review)

## Next Phase Preparation

After design approval, proceed to implementation:

```bash
# Execute implementation phase with design artifacts
/n8n-workflow-implementation --design-doc="Node_Configuration_Design_YYYY-MM-DD-HHMMSS.ipynb"

# Example with specific workflow type
/n8n-workflow-implementation --workflow-type=integration --validate-first=true
```

---

**Note**: This is a design command that produces comprehensive workflow design documentation with validated node configurations. The design artifacts serve as the blueprint for the implementation phase. All node configurations are pre-validated to ensure they will work during implementation.
