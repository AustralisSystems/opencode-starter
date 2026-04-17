# N8N Workflow Planning Command

**YAML Prompt**: `n8n-workflow-planning-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Strategic planning for n8n workflow development based on requirements analysis, template discovery, and node selection. This command creates comprehensive workflow plans that leverage n8n's 2,500+ templates and extensive node library to design optimal automation solutions.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n documentation and workflow best practices
- `grep` - Real-world workflow implementations on GitHub
- `sequential-thinking` - Structured workflow planning methodology
- `filesystem` - Requirements and constraints analysis
- `memory` - Track planning decisions and rationale
- `time` - Timestamp planning activities

**n8n-Specific MCP Tools:**
- `tools_documentation` - Understand n8n MCP capabilities at session start
- `search_templates` - Text-based template search
- `search_templates_by_metadata` - Smart template filtering (complexity, audience, time, service)
- `get_templates_for_task` - Curated templates by task type
- `list_node_templates` - Templates using specific nodes
- `search_nodes` - Node discovery by functionality
- `list_nodes` - Browse nodes by category
- `list_ai_tools` - Discover AI-capable nodes

## Template-First Workflow Strategy

**ALWAYS CHECK FOR EXISTING TEMPLATES FIRST (2,500+ available, 97.5% have metadata):**

### 1. Search by Metadata (Most Effective)
```javascript
// Filter by complexity and audience
search_templates_by_metadata({
  complexity: 'simple',           // simple|intermediate|advanced
  targetAudience: 'marketers',    // marketers|developers|analysts|business-users
  maxSetupMinutes: 30,            // Time constraint filter
  requiredService: 'slack'        // Service requirement
})
```

### 2. Search by Task (Curated Collections)
```javascript
// Get pre-curated templates for common tasks
get_templates_for_task('webhook_processing')
// Common tasks: webhook_processing, slack_integration,
// data_transformation, api_integration, email_automation
```

### 3. Search by Text (Keyword Search)
```javascript
search_templates('slack notification webhook')
```

### 4. Search by Nodes (Templates Using Specific Nodes)
```javascript
list_node_templates(['n8n-nodes-base.webhook', 'n8n-nodes-base.slack'])
```

**Template Usage Best Practices:**
- Templates save 70-90% development time
- **MANDATORY ATTRIBUTION**: "Based on template by **[Author Name]** (@username) - [template URL on n8n.io]"
- Validate templates before use (may need updates)
- Customize templates to fit specific requirements
- Document template modifications

## Node Discovery Strategy

### Progressive Node Discovery Approach

**1. Broad Search (Understand Options):**
```javascript
search_nodes({query: 'database'})
list_nodes({category: 'trigger'|'action'|'transform'})
```

**2. Get Essentials (Quick Understanding - Only 10-20 Essential Properties):**
```javascript
// START HERE for quick node understanding
get_node_essentials('n8n-nodes-base.postgres')
```

**3. Targeted Search (Specific Properties):**
```javascript
search_node_properties('n8n-nodes-base.httpRequest', 'authentication')
```

**4. Task-Based Templates (Pre-Configured):**
```javascript
get_node_for_task('send_email'|'store_data'|'transform_json')
// Get working configurations immediately
```

**5. Full Documentation (When Needed):**
```javascript
get_node_documentation('n8n-nodes-base.slack')
// Comprehensive human-readable docs
```

## Workflow Requirements Analysis

### Requirements Gathering Matrix

**Functional Requirements:**
- **Trigger Type**: webhook, schedule, manual, email, event-driven
- **Data Sources**: APIs, databases, files, webhooks, services
- **Data Transformations**: filtering, mapping, aggregation, enrichment
- **Actions**: notifications, data storage, API calls, file operations
- **Outputs**: destinations, formats, delivery methods

**Non-Functional Requirements:**
- **Performance**: execution frequency, data volume, latency requirements
- **Reliability**: error handling, retry logic, fallback strategies
- **Security**: authentication, data encryption, secret management
- **Compliance**: data retention, audit logging, regulatory requirements
- **Scalability**: concurrent executions, resource limits, growth projections

### Workflow Type Classification

**Automation Workflows:**
- Event-driven process automation
- Scheduled task automation
- Conditional routing and branching

**Integration Workflows:**
- System-to-system data sync
- API orchestration
- Service composition

**Data Processing Workflows:**
- ETL (Extract, Transform, Load)
- Data enrichment and validation
- Batch processing pipelines

**Webhook Workflows:**
- Real-time event processing
- Webhook receivers and processors
- API gateway patterns

## Architecture Planning

### Workflow Design Patterns

**1. Linear Pipeline Pattern:**
```
[Trigger]  [Transform]  [Action]
```
- Simple, sequential processing
- Best for straightforward automations

**2. Branching Pattern:**
```
                [Action A]
[Trigger]  [IF]
                [Action B]
```
- Conditional logic and routing
- Multiple execution paths

**3. Parallel Processing Pattern:**
```
                  [API Call A] 
[Trigger]  [Split]               [Merge]  [Action]
                  [API Call B] 
```
- Concurrent operations
- Improved performance

**4. Error Handling Pattern:**
```
[Trigger]  [Try: Main Flow]  [Success Action]
                 (on error)
         [Error Handler]  [Notification/Recovery]
```
- Robust error management
- Graceful degradation

### Connection Architecture

**Data Flow Mapping:**
- Map data flow between nodes
- Identify transformation requirements
- Plan expression usage for data manipulation
- Design connection structure (main, error paths)

**Expression Planning:**
- Variable references: `$json`, `$node["NodeName"].json`
- Data transformation expressions
- Conditional logic expressions
- Error handling expressions

## Error Workflow Planning

### Error Handling Architecture Strategy

**MANDATORY: Plan error handling BEFORE implementation to ensure robust workflows**

**1. Error Trigger Workflow Planning:**
```
[Main Workflow]  (on error)  [Error Trigger]  [Error Handler Workflow]

                                              [Log Error]  [Notify Team]  [Recovery Action]
```

**Planning Checklist:**
- [ ] Identify all potential error points in main workflow
- [ ] Design Error Trigger workflow for centralized error handling
- [ ] Plan error notification channels (Slack, Discord, email)
- [ ] Design error logging strategy with execution context
- [ ] Plan recovery actions and fallback workflows

**2. Node-Level Error Configuration Planning:**

**For Each Critical Node:**
```javascript
{
  "continueOnFail": true,        // Continue workflow on error
  "retryOnFail": true,           // Retry failed operations
  "maxTries": 3,                 // Maximum retry attempts
  "waitBetweenTries": 1000       // Wait time between retries (ms)
}
```

**Planning Decisions:**
- Which nodes should continue on fail vs halt workflow
- Retry strategies for external API calls
- Timeout configurations for long-running operations
- Error message customization with context

**3. Error Connection Patterns Planning:**

**Main + Error Path Architecture:**
```
[Node A]  main    [Node B]  main    [Success Action]
         error              error

     [Error Handler A]  [Error Handler B]
```

**Plan Error Connections For:**
- API integration nodes (external service failures)
- Database operations (connection/query failures)
- Data transformation nodes (validation errors)
- Webhook receivers (malformed requests)

**4. Error Notification Workflow Design:**

**Slack/Discord Error Notification Pattern:**
```javascript
// Error Trigger  Code Node (Format Error)  Slack/Discord
{
  "title": "Workflow Error: {{ $workflow.name }}",
  "message": "{{ $json.error.message }}",
  "execution_id": "{{ $execution.id }}",
  "workflow_id": "{{ $workflow.id }}",
  "timestamp": "{{ $now.toISO() }}",
  "error_node": "{{ $json.error.node.name }}"
}
```

**Planning Requirements:**
- Error notification channels and recipients
- Error message format and content
- Alert severity levels (critical, warning, info)
- Escalation rules for critical errors

## Security Requirements Planning

### Security Architecture Strategy

**MANDATORY: Define security requirements during planning phase**

**1. Credential Management Planning:**

**Credential Types to Plan:**
- API Keys and Tokens
- OAuth2 Credentials
- Database Credentials
- Webhook Secrets
- Service Account Keys

**Planning Checklist:**
- [ ] Identify all required credentials
- [ ] Plan credential storage strategy (n8n credentials vs external secrets)
- [ ] Design credential rotation procedures
- [ ] Plan credential testing and validation
- [ ] Document credential access requirements

**2. Webhook Security Planning:**

**Webhook Security Patterns:**
```javascript
// Webhook Node Security Configuration
{
  "authenticationMethod": "headerAuth",  // or hmacAuth, basicAuth
  "headerAuthParameter": "X-API-Key",
  "hmacSecret": "{{$credentials.webhookSecret}}",
  "allowedOrigins": ["https://trusted-domain.com"],
  "ipWhitelist": ["192.168.1.0/24"]
}
```

**Planning Requirements:**
- Webhook authentication method selection
- HMAC signature validation planning
- IP whitelisting requirements
- Request validation strategy

**3. Authentication Validation Planning:**

**For Each External Integration:**
- Authentication method (OAuth2, API Key, Basic Auth, JWT)
- Token refresh strategy
- Authentication failure handling
- Credential validation checkpoints

**4. Security Audit Planning:**

**Plan Security Validation:**
- Use `n8n audit` command for security scanning
- Identify sensitive data in workflows
- Plan data sanitization points
- Design secure logging (exclude secrets)

**5. External Secrets Management Planning:**

**For Production Workflows:**
- Plan integration with external secrets managers (HashiCorp Vault, AWS Secrets Manager)
- Design secret rotation procedures
- Plan environment-specific credentials (dev, staging, production)

## Testing Strategy Planning

### Comprehensive Testing Architecture

**MANDATORY: Plan testing strategy during workflow design phase**

**1. Unit Testing Planning:**

**Test Individual Node Logic:**
```javascript
// Code Node Unit Test Pattern
const testCases = [
  { input: {...}, expected: {...} },
  { input: {...}, expected: {...} }
];

// Plan test coverage for:
// - Data transformation logic
// - Validation functions
// - Error handling paths
// - Edge cases
```

**Planning Checklist:**
- [ ] Identify all Code nodes requiring unit tests
- [ ] Design test data sets for validation
- [ ] Plan edge case testing scenarios
- [ ] Design assertion strategies

**2. Integration Testing Planning:**

**Test Workflow Segments:**
```javascript
// Webhook Trigger  Processing  Response pattern
// Plan integration tests for:
// - Webhook receipt and parsing
// - Data transformation pipeline
// - External API interactions
// - Database operations
```

**Planning Requirements:**
- Test workflow segment boundaries
- Mock external service responses
- Plan test data persistence
- Design cleanup procedures

**3. End-to-End Testing Planning:**

**Complete Workflow Validation:**
```javascript
// Production-like test execution
// Plan E2E tests for:
// - Full workflow execution paths
// - Error scenarios and recovery
// - Performance under load
// - Concurrent execution handling
```

**E2E Test Planning:**
- [ ] Define test scenarios covering all execution paths
- [ ] Plan test environment setup
- [ ] Design test data generation
- [ ] Plan result validation methods
- [ ] Define success criteria

**4. Execution Testing Planning:**

**Test Execution Modes:**
```javascript
// Use $execution.mode for environment-aware testing
if ($execution.mode === 'test') {
  // Use test endpoints and data
} else if ($execution.mode === 'production') {
  // Use production endpoints
}
```

**Planning Decisions:**
- Test vs production endpoint strategy
- Test data generation approach
- Execution isolation strategy
- Test result tracking

**5. Webhook Testing Planning:**

**Webhook Validation Strategy:**
```javascript
// Plan webhook testing:
// 1. Tunnel mode for local testing (n8n tunnel)
// 2. Request validation testing
// 3. Authentication testing
// 4. Payload format validation
// 5. Error response testing
```

**Webhook Test Planning:**
- [ ] Plan tunnel mode configuration for local testing
- [ ] Design request validation test cases
- [ ] Plan authentication test scenarios
- [ ] Design malformed request handling tests

## Monitoring and Logging Planning

### Observability Architecture Strategy

**MANDATORY: Plan monitoring and logging infrastructure**

**1. Execution Monitoring Planning:**

**Monitoring Requirements:**
```javascript
// Plan monitoring for:
{
  "execution_success_rate": "% of successful executions",
  "execution_duration": "Average and P95 execution time",
  "error_rate": "% of failed executions",
  "retry_count": "Number of retry attempts",
  "queue_depth": "Pending executions (queue mode)"
}
```

**Planning Checklist:**
- [ ] Define key performance indicators (KPIs)
- [ ] Plan metric collection points
- [ ] Design alerting thresholds
- [ ] Plan monitoring dashboard layout
- [ ] Define SLA targets

**2. Custom Logging Planning:**

**Structured Logging Strategy:**
```javascript
// Custom log format planning
{
  "timestamp": "{{ $now.toISO() }}",
  "workflow_id": "{{ $workflow.id }}",
  "execution_id": "{{ $execution.id }}",
  "workflow_name": "{{ $workflow.name }}",
  "node_name": "{{ $node.name }}",
  "event_type": "execution_start|execution_success|execution_error",
  "metadata": {
    "input_count": "{{ $input.all().length }}",
    "output_count": "{{ $json.items.length }}",
    "duration_ms": "{{ $now - $execution.startedAt }}"
  }
}
```

**Logging Planning:**
- [ ] Define log levels (debug, info, warn, error)
- [ ] Plan log storage strategy
- [ ] Design log retention policies
- [ ] Plan log aggregation approach
- [ ] Define sensitive data exclusion rules

**3. Health Check Planning:**

**Workflow Health Monitoring:**
```javascript
// Plan health check workflow:
// 1. Schedule node  Every 5 minutes
// 2. HTTP Request  Check workflow endpoint
// 3. Condition  Validate response
// 4. Alert  Notify on failure
```

**Health Check Requirements:**
- [ ] Define health check endpoints
- [ ] Plan health check frequency
- [ ] Design health status criteria
- [ ] Plan failure notification strategy
- [ ] Define recovery procedures

**4. Performance Tracking Planning:**

**Performance Metrics to Track:**
- Execution time per workflow
- Node execution duration
- API call latency
- Data transformation time
- Queue wait time (if using queue mode)

**Planning Decisions:**
- Performance baseline establishment
- Performance degradation detection
- Bottleneck identification strategy
- Performance optimization triggers

**5. Audit Trail Planning:**

**Compliance and Audit Requirements:**
```javascript
// Plan audit logging for:
{
  "user_actions": "Who triggered the workflow",
  "data_access": "What data was accessed",
  "changes": "What modifications were made",
  "timestamp": "When the action occurred",
  "workflow_version": "Which version was executed"
}
```

**Audit Planning:**
- [ ] Define audit requirements (regulatory compliance)
- [ ] Plan audit log format and storage
- [ ] Design audit trail completeness validation
- [ ] Plan audit log retention (compliance requirements)
- [ ] Define audit log access controls

## Performance Baselines Planning

### Performance Optimization Strategy

**MANDATORY: Define performance requirements and optimization strategy**

**1. Rate Limiting Strategy Planning:**

**Loop Over Items with Wait Pattern:**
```javascript
// Plan rate limiting for API calls
// Loop Over Items Node Configuration:
{
  "batchSize": 10,              // Process 10 items at a time
  "options": {
    "loopMode": "item"          // Process item by item
  }
}

// Wait Node Configuration:
{
  "amount": 100,                // Wait 100ms between requests
  "unit": "milliseconds"
}

// Pattern: Loop Over Items  API Call  Wait  Continue
```

**Planning Decisions:**
- [ ] Identify all external API calls requiring rate limiting
- [ ] Determine API rate limits for each service
- [ ] Calculate optimal batch sizes
- [ ] Plan wait times between requests
- [ ] Design burst handling strategy

**2. Batching Strategy Planning:**

**Batch Processing Patterns:**
```javascript
// Plan batching for high-volume operations:
{
  "batch_size": 100,            // Items per batch
  "concurrent_batches": 5,      // Parallel batch processing
  "batch_timeout": 30000,       // 30 second timeout per batch
  "error_handling": "continue"  // Continue on batch failure
}
```

**Batching Requirements:**
- Database bulk operations (INSERT, UPDATE)
- API bulk endpoints
- File processing operations
- Data aggregation tasks

**3. Execution Timeout Planning:**

**Timeout Configuration Strategy:**
```javascript
// Plan execution timeouts:
{
  "EXECUTIONS_TIMEOUT": 300,        // 5 minutes max execution
  "EXECUTIONS_TIMEOUT_MAX": 3600,   // 1 hour absolute max
  "nodeTimeout": {
    "httpRequest": 30000,           // 30 second API timeout
    "database": 60000,              // 1 minute DB timeout
    "webhook": 10000                // 10 second webhook timeout
  }
}
```

**Planning Checklist:**
- [ ] Define workflow execution timeout
- [ ] Set node-specific timeouts
- [ ] Plan timeout error handling
- [ ] Design timeout notification strategy
- [ ] Plan timeout recovery procedures

**4. Static Data Management Planning:**

**Workflow Static Data Strategy:**
```javascript
// Use $getWorkflowStaticData() for persistence
// Plan static data for:
{
  "lastProcessedId": 12345,         // Track processing state
  "rateLimitCounter": 150,          // Track API usage
  "errorCount": 5,                  // Track error patterns
  "lastSuccessfulRun": "2025-01-02T10:00:00Z"
}
```

**Static Data Planning:**
- [ ] Identify data requiring persistence across executions
- [ ] Plan static data structure and schema
- [ ] Design static data cleanup strategy
- [ ] Plan static data size limits
- [ ] Define static data access patterns

**5. Queue Mode Planning (Production Scaling):**

**Queue Mode Architecture:**
```javascript
// Plan queue mode for production:
{
  "mode": "queue",                  // vs "regular" mode
  "concurrency": 10,                // Max concurrent executions
  "queueRecoveryInterval": 60,      // Recovery check interval
  "maxQueue": 1000                  // Max queued executions
}
```

**Queue Mode Planning:**
- [ ] Determine if queue mode is required
- [ ] Plan worker node configuration
- [ ] Design queue monitoring strategy
- [ ] Plan queue overflow handling
- [ ] Define scaling rules

**6. Custom Execution Data Planning:**

**Execution Context Management:**
```javascript
// Plan custom execution data usage:
{
  "executionData": {
    "sourceSystem": "CRM",
    "recordType": "customer",
    "processingStage": "enrichment",
    "priority": "high"
  }
}
```

**Execution Data Planning:**
- [ ] Define custom execution metadata
- [ ] Plan execution context tracking
- [ ] Design execution correlation strategy
- [ ] Plan execution data retention

## Implementation Roadmap Template

### Phase 1: Template Selection and Evaluation (Week 1)
- [ ] Execute template discovery using multiple search strategies
- [ ] Evaluate top 3-5 templates against requirements
- [ ] Document template selection rationale or custom build justification
- [ ] Plan template customization requirements
- [ ] Identify gaps between template and requirements

### Phase 2: Node Selection and Configuration Planning (Week 1-2)
- [ ] Map requirements to available nodes
- [ ] Select optimal nodes for each workflow component
- [ ] Plan node configurations using get_node_essentials
- [ ] Document node selection decisions
- [ ] Identify custom node requirements (if any)

### Phase 3: Architecture Design (Week 2)
- [ ] Design workflow structure and connection map
- [ ] Plan data transformations and expressions
- [ ] Design error handling strategy
- [ ] Plan validation checkpoints
- [ ] Document architecture decisions

### Phase 4: Validation Strategy (Week 2)
- [ ] Define pre-build validation requirements
- [ ] Plan node configuration validation approach
- [ ] Design workflow validation strategy
- [ ] Plan testing approach (unit, integration, E2E)
- [ ] Define success criteria

### Phase 5: Deployment Planning (Week 3)
- [ ] Plan deployment environment (local, cloud, self-hosted)
- [ ] Design deployment automation strategy
- [ ] Plan monitoring and observability approach
- [ ] Define rollback procedures
- [ ] Document deployment requirements

## Risk Assessment

### Technical Risks
- **Template Compatibility**: Selected template may require significant modification
- **Node Availability**: Required functionality may not exist in available nodes
- **Performance**: Workflow complexity may impact execution time
- **Integration**: External services may have API limitations

### Mitigation Strategies
- Validate template compatibility early
- Research custom node development if needed
- Plan performance optimization from the start
- Test integration points thoroughly
- Design fallback strategies

## Decision Framework

### Template vs Custom Build Decision Matrix

**Use Template When:**
- Close match to requirements (>70% overlap)
- Well-maintained and recently updated
- Clear documentation and attribution
- Acceptable customization effort (<30% changes)

**Build Custom When:**
- No suitable template found (< 50% match)
- Unique business logic requirements
- Complex custom integrations needed
- Specific performance requirements

### Node Selection Criteria

**Priority Factors:**
1. **Functionality Match**: 40% - Meets requirement exactly
2. **Reliability**: 25% - Stable, well-maintained node
3. **Performance**: 20% - Execution speed and efficiency
4. **Documentation**: 15% - Clear docs and examples

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Workflow_Requirements_Analysis_YYYY-MM-DD-HHMMSS.ipynb**
   - Complete requirements documentation
   - Functional and non-functional requirements
   - Use case scenarios and user stories
   - Success criteria and acceptance tests

2. **Template_and_Node_Selection_YYYY-MM-DD-HHMMSS.ipynb**
   - Template discovery results and evaluation
   - Template selection rationale or custom build justification
   - Node selection matrix with scoring
   - Alternatives considered and rejected

3. **Workflow_Architecture_Plan_YYYY-MM-DD-HHMMSS.ipynb**
   - High-level workflow architecture diagram
   - Data flow mapping and transformations
   - Connection architecture and expression planning
   - Error handling and recovery design

4. **Implementation_Roadmap_YYYY-MM-DD-HHMMSS.ipynb**
   - Phased implementation plan with timelines
   - Resource requirements and allocations
   - Risk assessment and mitigation strategies
   - Success criteria and validation checkpoints

## Success Criteria

**Core Planning:**
- [ ] Requirements clearly documented with functional and non-functional aspects
- [ ] Template discovery completed using multiple search strategies
- [ ] Templates evaluated and best option selected (or custom build justified)
- [ ] All required nodes identified and mapped to requirements
- [ ] Node selection decisions documented with rationale
- [ ] Workflow architecture designed with clear data flow
- [ ] Expression usage planned for data transformations
- [ ] Implementation roadmap created with realistic phases
- [ ] Risk assessment completed with mitigation strategies
- [ ] All deliverables created with proper reverse date stamps
- [ ] Template attribution documented (if using template)
- [ ] Validation strategy defined for each phase

**Error Handling Planning:**
- [ ] Error Trigger workflow architecture designed
- [ ] Node-level error configuration strategy planned (continueOnFail, retryOnFail, maxTries)
- [ ] Error connection patterns mapped for main and error paths
- [ ] Error notification workflow planned (Slack/Discord/Email)
- [ ] Custom error messages with execution context planned

**Security Planning:**
- [ ] All required credentials identified and categorized
- [ ] Credential management strategy defined (storage, rotation, validation)
- [ ] Webhook security configuration planned (authentication, HMAC, IP whitelist)
- [ ] Authentication validation strategy defined for all integrations
- [ ] Security audit approach planned (n8n audit command usage)
- [ ] External secrets management strategy defined (if applicable)

**Testing Planning:**
- [ ] Unit testing strategy defined for Code nodes and transformations
- [ ] Integration testing approach planned for workflow segments
- [ ] End-to-end testing scenarios defined for complete workflows
- [ ] Execution testing strategy planned (test vs production modes)
- [ ] Webhook testing approach defined (tunnel mode, validation)
- [ ] Test data generation and cleanup strategy planned

**Monitoring and Logging Planning:**
- [ ] Execution monitoring KPIs and metrics defined
- [ ] Custom logging strategy planned with structured format
- [ ] Health check workflows designed with alerting strategy
- [ ] Performance tracking metrics and baselines defined
- [ ] Audit trail requirements and retention policies planned

**Performance Planning:**
- [ ] Rate limiting strategy designed (Loop Over Items with Wait pattern)
- [ ] Batching strategy planned for high-volume operations
- [ ] Execution timeout configuration defined (workflow and node-level)
- [ ] Static data management strategy planned for state persistence
- [ ] Queue mode architecture planned for production scaling (if required)
- [ ] Custom execution data strategy defined for context tracking

## Command Integration

- **Previous Phase**: *None* (This is the first command in the workflow lifecycle)
- **Parallel**: `n8n-workflow-gap-analysis` (for existing workflow assessment)
- **Next Phase**: `n8n-workflow-design` (detailed node configuration and connection design)

## Next Phase Preparation

After planning approval, proceed to detailed design:

```bash
# Execute design phase with planning artifacts
/n8n-workflow-design --planning-doc="Workflow_Architecture_Plan_YYYY-MM-DD-HHMMSS.ipynb"

# Example with specific workflow type
/n8n-workflow-design --workflow-type=integration --complexity=intermediate
```

---

**Note**: This is a planning command that produces comprehensive workflow planning documentation. No actual workflow building occurs in this phase. The planning artifacts serve as the foundation for the design and implementation phases.
