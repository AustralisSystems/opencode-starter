# N8N Workflow Implementation Command

**YAML Prompt**: `n8n-workflow-implementation-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Build and deploy n8n workflows using validated design artifacts. This command transforms design specifications into executable n8n workflows with comprehensive validation and deployment to n8n instance (if configured).

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n workflow building patterns and best practices
- `grep` - Real-world workflow implementation examples on GitHub
- `sequential-thinking` - Structured implementation approach
- `filesystem` - Read design artifacts and write workflow files
- `memory` - Track implementation progress and decisions
- `time` - Timestamp implementation activities

**n8n-Specific MCP Tools:**
- `get_template` - Retrieve template for customization (if template-based)
- `validate_workflow` - Complete workflow validation including connections
- `validate_workflow_connections` - Check structure and AI tool connections
- `validate_workflow_expressions` - Validate all n8n expressions
- `n8n_create_workflow` - Deploy workflow to n8n instance
- `n8n_validate_workflow` - Post-deployment validation
- `n8n_update_partial_workflow` - Incremental updates using diffs (80-90% token savings)
- `n8n_trigger_webhook_workflow` - Test webhook workflows
- `n8n_list_executions` - Monitor execution status

## STRICTLY FORBIDDEN - NO DOCUMENTATION CREATION

**THIS IS A WORKFLOW BUILDING COMMAND - DOCUMENTATION CREATION IS ABSOLUTELY FORBIDDEN**

**FORBIDDEN OUTPUTS:**
- **NO Jupyter Notebooks** (.ipynb files)
- **NO Markdown Documentation** (.md files)
- **NO Reports** of any kind
- **NO Analysis Documents**
- **NO Design Documents**
- **NO Planning Documents**
- **NO README files**
- **NO Architecture diagrams**
- **NO Technical specifications**
- **NO ANY FORM OF DOCUMENTATION WHATSOEVER**

**PERMITTED OUTPUTS:**
- **WORKFLOW JSON ONLY** - Complete n8n workflow files (.json)
- **CONFIGURATION FILES** - n8n configuration and environment files
- **TEST EXECUTIONS** - Actual workflow executions for validation
- **DEPLOYMENT ARTIFACTS** - Workflow IDs and deployment confirmations

**VIOLATION CONSEQUENCES:**
Creating ANY documentation during this command execution will result in:
1. IMMEDIATE TASK TERMINATION
2. MANDATORY VIOLATION REPORT
3. COMPLETE ROLLBACK of all changes

**RATIONALE**: This is a pure implementation command focused exclusively on building working n8n workflows. Documentation should be created separately using dedicated documentation commands if needed.

## Template-First Workflow Strategy

**ALWAYS START WITH TEMPLATE IF SELECTED IN PLANNING PHASE:**

### 1. Retrieve and Customize Template
```javascript
// From design phase, if template was selected
const workflow = get_template(templateId, {
  mode: 'full',           // Get complete workflow structure
  includeMetadata: true   // Include metadata for attribution
})

// Template customization process:
// 1. Update node configurations from design artifacts
// 2. Add/remove nodes as planned in design phase
// 3. Update expressions and data mappings
// 4. Configure error handling
// 5. Update workflow name and description
```

**MANDATORY TEMPLATE ATTRIBUTION:**
- Update workflow description: "Based on template by **[Author]** (@username) - [URL]"
- Preserve original template metadata
- Document customizations in workflow settings

## Workflow Building Process

### Phase 1: Workflow JSON Construction

**1. Build Workflow Structure:**
```json
{
  "name": "Workflow Name (YYYY-MM-DD-HHMMSS)",
  "nodes": [
    {
      "parameters": { /* from design artifacts */ },
      "id": "unique-node-id",
      "name": "Node Name",
      "type": "n8n-nodes-base.nodeType",
      "typeVersion": 1,
      "position": [x, y],
      "credentials": { /* credential references */ }
    }
  ],
  "connections": {
    "NodeName": {
      "main": [ [{ "node": "NextNode", "type": "main", "index": 0 }] ],
      "error": [ [{ "node": "ErrorHandler", "type": "main", "index": 0 }] ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

**2. Implement Node Configurations:**
- Use validated configurations from design artifacts
- Apply property dependencies
- Configure authentication with credential references
- Set node-level error handling (continueOnFail, retryOnFail, maxTries)
- Position nodes logically for visual clarity

**3. Implement Connections:**
- Build main execution paths from design
- Implement error handling connections
- Configure branching and conditional logic
- Set up parallel processing paths

**4. Implement Expressions:**
- Apply data transformation expressions from design
- Implement conditional logic expressions
- Configure array operations
- Set fallback values for undefined/null cases

### Phase 2: Validation Execution

**PRE-DEPLOYMENT VALIDATION (MANDATORY):**

```javascript
// Step 1: Complete workflow validation
const validationResult = validate_workflow(workflow)
// Must pass: structure, nodes, connections, expressions

// Step 2: Connection validation
const connectionResult = validate_workflow_connections(workflow)
// Must pass: all connections valid, no orphaned nodes

// Step 3: Expression validation
const expressionResult = validate_workflow_expressions(workflow)
// Must pass: all expressions syntax-correct
```

**VALIDATION FAILURE HANDLING:**
- **DO NOT PROCEED** if any validation fails
- Fix all errors before deployment
- Re-validate after fixes
- Document fixes applied

### Phase 3: Deployment (If n8n API Configured)

**DEPLOYMENT SEQUENCE:**

```javascript
// Step 1: Create workflow in n8n
const created = n8n_create_workflow(validatedWorkflow)
// Returns: { id: 'workflow-id', name: 'workflow-name' }

// Step 2: Post-deployment validation
const deployValidation = n8n_validate_workflow({ id: created.id })
// Ensures workflow is valid in actual n8n environment

// Step 3: Activate workflow (if applicable)
// Manual activation or programmatic activation

// Step 4: Test execution (if webhook or manual trigger)
if (workflowType === 'webhook') {
  const testResult = n8n_trigger_webhook_workflow({
    workflowId: created.id,
    testData: { /* test payload */ }
  })
}

// Step 5: Monitor first executions
const executions = n8n_list_executions({
  workflowId: created.id,
  limit: 5
})
// Check for successful execution
```

### Phase 4: Post-Deployment Testing

**TESTING WORKFLOW EXECUTIONS:**

**1. Webhook Workflows:**
```javascript
// Send test payload to webhook URL
n8n_trigger_webhook_workflow({
  workflowId: created.id,
  testData: {
    // Representative test data
  }
})

// Check execution results
const executions = n8n_list_executions({
  workflowId: created.id,
  limit: 1
})
// Verify: execution successful, data processed correctly
```

**2. Manual Trigger Workflows:**
- Execute manually in n8n UI
- Monitor execution results
- Verify data flow and transformations
- Check error handling

**3. Schedule Workflows:**
- Trigger manually for immediate test
- Verify schedule configuration
- Monitor first scheduled execution

## Error Handling Implementation

### Node-Level Error Configuration

```json
{
  "parameters": { /* node config */ },
  "continueOnFail": true,      // Continue workflow on error
  "retryOnFail": true,          // Automatic retry
  "maxTries": 3,                // Max retry attempts
  "waitBetweenTries": 1000     // Delay between retries (ms)
}
```

### Workflow-Level Error Handling

**Error Connection Implementation:**
```json
"connections": {
  "MainNode": {
    "main": [ [{ "node": "SuccessPath", "type": "main", "index": 0 }] ],
    "error": [ [{ "node": "ErrorHandler", "type": "main", "index": 0 }] ]
  },
  "ErrorHandler": {
    "main": [ [{ "node": "ErrorNotification", "type": "main", "index": 0 }] ]
  }
}
```

## Error Trigger Workflow Implementation

### Build Centralized Error Handler

**MANDATORY: Implement Error Trigger workflow for production workflows**

**1. Create Error Trigger Workflow:**

```json
{
  "name": "Error_Handler_YYYY-MM-DD-HHMMSS",
  "nodes": [
    {
      "parameters": {},
      "id": "error-trigger-node",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Format error with context\nconst errorData = {\n  workflow: {\n    id: $json.workflow.id,\n    name: $json.workflow.name\n  },\n  execution: {\n    id: $json.execution.id,\n    mode: $json.execution.mode\n  },\n  error: {\n    message: $json.error.message,\n    node: $json.error.node.name,\n    stack: $json.error.stack,\n    timestamp: new Date().toISOString()\n  },\n  severity: $json.error.message.includes('CRITICAL') ? 'critical' : 'warning'\n};\n\nreturn { json: errorData };"
      },
      "id": "format-error-node",
      "name": "Format Error Details",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "leftValue": "={{ $json.severity }}",
              "rightValue": "critical",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "severity-switch",
      "name": "Check Severity",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [650, 300]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "C12345",
          "mode": "id"
        },
        "text": "= *CRITICAL ERROR*\\n\\n*Workflow:* {{ $json.workflow.name }}\\n*Error:* {{ $json.error.message }}\\n*Node:* {{ $json.error.node }}\\n*Execution ID:* {{ $json.execution.id }}\\n*Time:* {{ $json.error.timestamp }}",
        "otherOptions": {}
      },
      "id": "slack-critical",
      "name": "Slack Critical Alert",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [850, 200],
      "credentials": {
        "slackOAuth2Api": {
          "id": "1",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "C67890",
          "mode": "id"
        },
        "text": "= *Warning*\\n*Workflow:* {{ $json.workflow.name }}\\n*Error:* {{ $json.error.message }}",
        "otherOptions": {}
      },
      "id": "slack-warning",
      "name": "Slack Warning",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [850, 400],
      "credentials": {
        "slackOAuth2Api": {
          "id": "1",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Error Trigger": {
      "main": [[{"node": "Format Error Details", "type": "main", "index": 0}]]
    },
    "Format Error Details": {
      "main": [[{"node": "Check Severity", "type": "main", "index": 0}]]
    },
    "Check Severity": {
      "main": [
        [{"node": "Slack Critical Alert", "type": "main", "index": 0}],
        [{"node": "Slack Warning", "type": "main", "index": 0}]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

**2. Link Main Workflow to Error Handler:**

```json
{
  "name": "Main_Workflow_YYYY-MM-DD-HHMMSS",
  "settings": {
    "executionOrder": "v1",
    "errorWorkflow": "error-handler-workflow-id"  // Link to Error Trigger workflow
  },
  "nodes": [ /* main workflow nodes */ ]
}
```

**3. Implement Node-Level Error Configuration:**

```json
{
  "parameters": { /* API call config */ },
  "id": "api-call-node",
  "name": "External API Call",
  "type": "n8n-nodes-base.httpRequest",
  "continueOnFail": true,         // Don't halt workflow
  "retryOnFail": true,            // Auto-retry
  "maxTries": 3,                  // 3 attempts
  "waitBetweenTries": 2000,       // 2 second wait
  "onError": "continueErrorOutput" // Send to error connection
}
```

**Implementation Checklist:**
- [ ] Create Error Trigger workflow JSON
- [ ] Implement error formatting Code node
- [ ] Configure severity routing (Switch node)
- [ ] Implement notification nodes (Slack/Discord/Email)
- [ ] Link main workflow to error handler via settings.errorWorkflow
- [ ] Configure node-level error settings (continueOnFail, retryOnFail, maxTries)

## Testing Implementation

### Comprehensive Test Strategy

**MANDATORY: Implement tests alongside workflows**

**1. Unit Test Implementation (Code Node Testing):**

```json
{
  "name": "Unit_Tests_YYYY-MM-DD-HHMMSS",
  "nodes": [
    {
      "parameters": {},
      "id": "manual-trigger",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Unit test for data transformation logic\nconst testCases = [\n  {\n    input: { price: 100, tax: 0.1 },\n    expected: { total: 110 }\n  },\n  {\n    input: { price: 50, tax: 0.2 },\n    expected: { total: 60 }\n  }\n];\n\nconst results = testCases.map(test => {\n  const result = test.input.price * (1 + test.input.tax);\n  return {\n    input: test.input,\n    expected: test.expected.total,\n    actual: result,\n    passed: result === test.expected.total\n  };\n});\n\nreturn results.map(r => ({ json: r }));"
      },
      "id": "unit-test-code",
      "name": "Run Unit Tests",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {},
          "conditions": [
            {
              "leftValue": "={{ $json.passed }}",
              "rightValue": true,
              "operator": {
                "type": "boolean",
                "operation": "true"
              }
            }
          ]
        }
      },
      "id": "check-tests",
      "name": "All Tests Passed?",
      "type": "n8n-nodes-base.if",
      "position": [650, 300]
    }
  ],
  "connections": {
    "Manual Trigger": {
      "main": [[{"node": "Run Unit Tests", "type": "main", "index": 0}]]
    },
    "Run Unit Tests": {
      "main": [[{"node": "All Tests Passed?", "type": "main", "index": 0}]]
    }
  }
}
```

**2. Integration Test Implementation:**

```json
{
  "name": "Integration_Tests_YYYY-MM-DD-HHMMSS",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "test-webhook",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Test Webhook",
      "type": "n8n-nodes-base.webhook",
      "webhookId": "test-integration",
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Validate webhook payload\nif (!$json.body.id || !$json.body.data) {\n  throw new Error('Invalid payload structure');\n}\nreturn { json: $json.body };"
      },
      "id": "validate-payload",
      "name": "Validate Input",
      "type": "n8n-nodes-base.code",
      "position": [450, 300],
      "continueOnFail": true
    },
    {
      "parameters": {
        "url": "={{ $execution.mode === 'test' ? 'https://test-api.com' : 'https://api.com' }}/process",
        "method": "POST",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "data",
              "value": "={{ $json }}"
            }
          ]
        }
      },
      "id": "api-call",
      "name": "Process Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [650, 300],
      "retryOnFail": true,
      "maxTries": 3
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { success: true, execution_id: $execution.id } }}"
      },
      "id": "respond",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [850, 300]
    }
  ],
  "connections": {
    "Test Webhook": {
      "main": [[{"node": "Validate Input", "type": "main", "index": 0}]]
    },
    "Validate Input": {
      "main": [[{"node": "Process Data", "type": "main", "index": 0}]],
      "error": [[{"node": "Respond to Webhook", "type": "main", "index": 0}]]
    },
    "Process Data": {
      "main": [[{"node": "Respond to Webhook", "type": "main", "index": 0}]]
    }
  }
}
```

**3. End-to-End Test Execution:**

```javascript
// After deploying test workflow, execute E2E tests
n8n_trigger_webhook_workflow({
  workflowId: 'integration-test-workflow-id',
  testData: {
    id: 'test-123',
    data: { /* test payload */ }
  }
})

// Validate execution
const executions = n8n_list_executions({
  workflowId: 'integration-test-workflow-id',
  limit: 1
})

// Check: execution.finished === true, execution.data.resultData.error === undefined
```

**Test Implementation Checklist:**
- [ ] Create unit test workflow for Code node logic
- [ ] Implement integration test workflow for API interactions
- [ ] Configure test vs production endpoints using $execution.mode
- [ ] Execute test workflows and validate results
- [ ] Document test coverage and results

## Queue Mode Configuration

### Production Scaling Implementation

**MANDATORY: Configure queue mode for production workflows with high volume**

**1. Queue Mode Environment Configuration:**

```bash
# .env or n8n configuration
EXECUTIONS_MODE=queue           # Enable queue mode
QUEUE_BULL_REDIS_HOST=localhost
QUEUE_BULL_REDIS_PORT=6379
QUEUE_BULL_REDIS_DB=0
QUEUE_HEALTH_CHECK_ACTIVE=true
```

**2. Worker Configuration:**

```bash
# Start main n8n instance (queue mode)
n8n start --tunnel

# Start worker instances (separate processes/containers)
n8n worker --concurrency=10

# Scale workers horizontally
docker-compose up -d --scale n8n-worker=5
```

**3. Workflow Queue Configuration:**

```json
{
  "name": "High_Volume_Workflow_YYYY-MM-DD-HHMMSS",
  "settings": {
    "executionOrder": "v1",
    "executionTimeout": 300,        // 5 minute timeout
    "saveExecutionProgress": true,  // Save progress for queue recovery
    "saveDataSuccessExecution": "all",
    "saveDataErrorExecution": "all"
  },
  "nodes": [ /* workflow nodes */ ]
}
```

**4. Queue Monitoring Implementation:**

```json
{
  "name": "Queue_Monitor_YYYY-MM-DD-HHMMSS",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [{ "field": "minutes", "minutesInterval": 5 }]
        }
      },
      "id": "schedule",
      "name": "Every 5 Minutes",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Check queue health via Redis or n8n API\nconst queueStats = {\n  waiting: $getWorkflowStaticData('global').queueWaiting || 0,\n  active: $getWorkflowStaticData('global').queueActive || 0,\n  completed: $getWorkflowStaticData('global').queueCompleted || 0,\n  failed: $getWorkflowStaticData('global').queueFailed || 0\n};\n\nif (queueStats.waiting > 1000) {\n  return { json: { alert: 'HIGH_QUEUE', stats: queueStats } };\n}\n\nreturn { json: { status: 'OK', stats: queueStats } };"
      },
      "id": "check-queue",
      "name": "Check Queue Status",
      "type": "n8n-nodes-base.code",
      "position": [450, 300]
    }
  ]
}
```

**Queue Mode Checklist:**
- [ ] Configure queue mode in environment variables
- [ ] Set up Redis for Bull queue
- [ ] Configure worker instances with concurrency
- [ ] Implement queue monitoring workflow
- [ ] Configure workflow execution timeout
- [ ] Enable execution progress saving

## Tunnel Mode Setup

### Local Webhook Testing Configuration

**MANDATORY: Use tunnel mode for local webhook development**

**1. Start n8n with Tunnel Mode:**

```bash
# Enable tunnel for local webhook testing
n8n start --tunnel

# Output will show:
# Tunnel URL: https://random-subdomain.n8n.app
# Use this URL for webhook endpoints
```

**2. Webhook Configuration for Tunnel:**

```json
{
  "name": "Webhook_Development_YYYY-MM-DD-HHMMSS",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "customer-webhook",
        "options": {
          "rawBody": true  // Preserve raw body for signature validation
        }
      },
      "id": "webhook-node",
      "name": "Customer Webhook",
      "type": "n8n-nodes-base.webhook",
      "webhookId": "customer-webhook-dev",
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "// Log webhook receipt for debugging\nconst webhookData = {\n  received_at: new Date().toISOString(),\n  headers: $json.headers,\n  body: $json.body,\n  query: $json.query,\n  tunnel_url: process.env.WEBHOOK_URL || 'https://tunnel.n8n.app'\n};\n\nconsole.log('Webhook received:', webhookData);\nreturn { json: webhookData };"
      },
      "id": "log-webhook",
      "name": "Log Webhook Data",
      "type": "n8n-nodes-base.code",
      "position": [450, 300]
    }
  ],
  "connections": {
    "Customer Webhook": {
      "main": [[{"node": "Log Webhook Data", "type": "main", "index": 0}]]
    }
  }
}
```

**3. Test Webhook with Tunnel:**

```javascript
// After deploying webhook workflow with tunnel
n8n_trigger_webhook_workflow({
  workflowId: 'webhook-dev-workflow-id',
  testData: {
    headers: {
      'x-api-key': 'test-key',
      'content-type': 'application/json'
    },
    body: {
      id: 'test-123',
      data: { /* test payload */ }
    }
  }
})

// Alternative: Use curl to test tunnel URL
// curl -X POST https://random-subdomain.n8n.app/webhook/customer-webhook \
//   -H "Content-Type: application/json" \
//   -H "X-API-Key: test-key" \
//   -d '{"id":"test-123","data":{}}'
```

**Tunnel Mode Checklist:**
- [ ] Start n8n with --tunnel flag
- [ ] Note tunnel URL for webhook configuration
- [ ] Configure webhook nodes for development
- [ ] Test webhooks using tunnel URL
- [ ] Implement webhook logging for debugging
- [ ] Switch to production webhook URLs for deployment

## Version Control Integration

### Git Workflow Implementation

**MANDATORY: Implement version control for production workflows**

**1. Workflow Export and Commit:**

```bash
# Export workflow JSON
n8n export:workflow --id=<workflow-id> --output=workflows/

# Add to Git
git add workflows/{workflow-name}_YYYY-MM-DD-HHMMSS.json

# Commit with conventional format
git commit -m "feat(n8n): add customer onboarding workflow

- Implement webhook trigger for customer data
- Add CRM integration with error handling
- Configure queue mode for high volume
- Add Error Trigger workflow for monitoring

 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to development branch
git push origin development
```

**2. Workflow Metadata for Version Tracking:**

```json
{
  "name": "Customer_Onboarding_v2.5.0_YYYY-MM-DD-HHMMSS",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "production-instance-id"
  },
  "tags": [
    {
      "createdAt": "2025-01-02T15:00:00.000Z",
      "updatedAt": "2025-01-02T15:00:00.000Z",
      "id": "1",
      "name": "production"
    },
    {
      "id": "2",
      "name": "v2.5.0"
    },
    {
      "id": "3",
      "name": "customer-onboarding"
    }
  ],
  "settings": {
    "executionOrder": "v1",
    "saveExecutionProgress": true,
    "saveDataSuccessExecution": "all",
    "saveDataErrorExecution": "all"
  }
}
```

**3. CI/CD Integration Implementation:**

```yaml
# .github/workflows/n8n-deploy.yml (already designed, now implement)
name: Deploy n8n Workflows

on:
  push:
    branches: [main]
    paths:
      - 'workflows/**/*.json'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Validate workflows
        run: |
          npm install -g n8n
          for file in workflows/*.json; do
            n8n validate-workflow "$file"
          done

      - name: Deploy to production
        env:
          N8N_API_KEY: ${{ secrets.N8N_PROD_API_KEY }}
          N8N_URL: ${{ secrets.N8N_PROD_URL }}
        run: |
          for file in workflows/*.json; do
            curl -X POST "$N8N_URL/api/v1/workflows/import" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" \
              -H "Content-Type: application/json" \
              -d @"$file"
          done
```

**Version Control Checklist:**
- [ ] Export workflow JSON to Git repository
- [ ] Add workflow metadata with version and tags
- [ ] Commit with conventional commit format
- [ ] Push to development branch
- [ ] Implement GitHub Actions for deployment
- [ ] Configure production deployment secrets
- [ ] Test CI/CD pipeline with staging environment

## Incremental Updates Pattern

**For Updates to Existing Workflows:**

```javascript
// Use diff operations for 80-90% token savings
n8n_update_partial_workflow({
  workflowId: 'existing-workflow-id',
  operations: [
    {
      type: 'updateNode',
      nodeId: 'node-to-update',
      changes: {
        parameters: { /* updated parameters */ }
      }
    },
    {
      type: 'addNode',
      node: { /* new node configuration */ }
    },
    {
      type: 'updateConnection',
      from: 'NodeA',
      to: 'NodeB',
      connectionType: 'main'
    }
  ]
})

// Validate after update
n8n_validate_workflow({ id: 'existing-workflow-id' })
```

## Expression Implementation Patterns

### Basic Data Access
```javascript
// In workflow JSON:
"parameters": {
  "value": "={{ $json.fieldName }}"
}
```

### Data Transformation
```javascript
"parameters": {
  "email": "={{ $json.email.toLowerCase() }}",
  "price": "={{ $json.price * 1.1 }}",
  "date": "={{ new Date($json.timestamp).toISOString() }}"
}
```

### Conditional Logic
```javascript
"parameters": {
  "status": "={{ $json.score > 80 ? 'excellent' : 'needs improvement' }}",
  "value": "={{ $json.customField ?? 'default value' }}"
}
```

### Array Operations
```javascript
"parameters": {
  "ids": "={{ $json.items.map(item => item.id) }}",
  "active": "={{ $json.items.filter(item => item.active === true) }}"
}
```

## Workflow File Management

### File Naming Convention
```
{workflow-name}_YYYY-MM-DD-HHMMSS.json
```

### File Structure
- Save workflow JSON to appropriate directory
- Include timestamp in filename
- Preserve version history (if using git)
- Keep backup of working versions

## Deliverables

**NO DOCUMENTATION DELIVERABLES - WORKFLOW BUILDING ONLY COMMAND**

This command produces WORKFLOWS ONLY:
- Complete n8n workflow JSON files
- Deployed workflow IDs (if deployed)
- Validation results (pass/fail status only)
- Execution test results (success/failure status)

**REMINDER**: This is a pure implementation command. NO Jupyter Notebooks, NO Markdown files, NO reports of any kind will be created. Documentation creation is STRICTLY FORBIDDEN per the protocol above.

## Success Criteria

**Core Implementation:**
- [ ] Workflow JSON built successfully from design artifacts
- [ ] All nodes configured with validated parameters
- [ ] Connections implemented correctly (main and error paths)
- [ ] Expressions implemented and syntax-validated
- [ ] Pre-deployment validation passed (validate_workflow)
- [ ] Connection validation passed (validate_workflow_connections)
- [ ] Expression validation passed (validate_workflow_expressions)
- [ ] Workflow deployed to n8n (if configured)
- [ ] Post-deployment validation passed (n8n_validate_workflow)
- [ ] Workflow file saved with proper naming convention
- [ ] Template attribution included (if template-based)

**Error Trigger Implementation:**
- [ ] Error Trigger workflow JSON created with proper structure
- [ ] Error formatting Code node implemented
- [ ] Severity routing Switch node configured
- [ ] Notification nodes implemented (Slack/Discord/Email)
- [ ] Main workflow linked to Error Trigger via settings.errorWorkflow
- [ ] Node-level error configuration applied (continueOnFail, retryOnFail, maxTries, waitBetweenTries)
- [ ] Error connections implemented for critical nodes
- [ ] Error Trigger workflow tested and validated

**Testing Implementation:**
- [ ] Unit test workflow created for Code node logic
- [ ] Integration test workflow implemented for API interactions
- [ ] Test vs production endpoints configured using $execution.mode
- [ ] E2E tests executed successfully
- [ ] Test workflows deployed and validated
- [ ] Test execution results verified (all tests passing)

**Queue Mode Configuration:**
- [ ] Queue mode environment variables configured (EXECUTIONS_MODE=queue)
- [ ] Redis connection configured for Bull queue
- [ ] Worker instances configured with concurrency settings
- [ ] Queue monitoring workflow implemented
- [ ] Workflow timeout configuration applied
- [ ] Execution progress saving enabled

**Tunnel Mode Setup:**
- [ ] n8n started with --tunnel flag for webhook testing
- [ ] Tunnel URL documented for webhook configuration
- [ ] Webhook workflows configured for tunnel mode
- [ ] Webhook logging implemented for debugging
- [ ] Webhooks tested successfully using tunnel URL
- [ ] Production webhook URLs configured for deployment

**Version Control Integration:**
- [ ] Workflow JSON exported to Git repository
- [ ] Workflow metadata added (version, tags, environment)
- [ ] Git commit created with conventional format
- [ ] Changes pushed to development branch
- [ ] GitHub Actions workflow file created (.github/workflows/n8n-deploy.yml)
- [ ] CI/CD secrets configured (N8N_API_KEY, N8N_BASE_URL)
- [ ] CI/CD pipeline tested with staging environment

## Command Integration

- **Previous Phase**: `n8n-workflow-design` (detailed node configuration and connection design)
- **Next Phase**: `n8n-workflow-lint-quality-check` (workflow validation and quality checks)
- **Parallel**: None (implementation is sequential)

## Next Phase Preparation

After implementation completion, proceed to quality checks:

```bash
# Execute lint and quality check phase
/n8n-workflow-lint-quality-check --workflow-file="{workflow-name}_YYYY-MM-DD-HHMMSS.json"

# Or if deployed
/n8n-workflow-lint-quality-check --workflow-id="deployed-workflow-id"
```

---

**Note**: This is an implementation command that generates executable n8n workflows, not documentation. The workflow JSON is the deliverable, along with deployment confirmation and validation status.
