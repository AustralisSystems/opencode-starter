# N8N Workflow Quality Analysis Command

**YAML Prompt**: `n8n-workflow-quality-analysis-prompt.yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ BEFORE COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## Purpose

Deep workflow quality analysis with comprehensive metrics, pattern assessment, and maintainability evaluation for n8n workflows. This command provides detailed quality insights, performance analysis, and actionable improvement recommendations based on n8n best practices.

## MCP Tool Requirements

**Mandatory MCP Tools:**
- `context7` - Latest n8n quality standards and best practices
- `grep` - Production-quality workflow patterns on GitHub
- `sequential-thinking` - Structured quality analysis methodology
- `filesystem` - Workflow analysis and metrics calculation
- `memory` - Track quality metrics during analysis
- `time` - Timestamp quality assessment activities

**n8n-Specific MCP Tools:**
- `get_workflow_metrics` - Calculate workflow complexity metrics
- `analyze_workflow_performance` - Performance pattern analysis
- `get_workflow_structure` - Architectural analysis
- `list_workflow_patterns` - Pattern identification and assessment
- `calculate_quality_score` - Overall quality scoring
- `identify_improvement_opportunities` - Optimization recommendations

## Quality Analysis Dimensions

### 1. Workflow Complexity and Maintainability

**Complexity Metrics:**
- **Node Count**: Total nodes in workflow (Target: <50 for simple, <100 for complex)
- **Connection Complexity**: Average connections per node (Target: <3)
- **Expression Complexity**: Nested expression depth (Target: <4 levels)
- **Workflow Depth**: Maximum execution path length (Target: <15 nodes)

**Maintainability Assessment:**
- Documentation completeness (node notes, workflow description)
- Naming convention consistency
- Logical grouping and organization
- Code node readability
- Pattern consistency across workflow

### 2. n8n-Specific Quality Patterns

**Workflow Architecture Patterns:**
```javascript
// Linear Pipeline (Simple)
[Webhook]  [Transform]  [Database]  [Response]
// Complexity Score: Low
// Maintainability: High

// Branching Logic (Moderate)
[Trigger]  [IF]  {
  true: [Process A]  [Merge],
  false: [Process B]  [Merge]
}  [Action]
// Complexity Score: Medium
// Maintainability: Medium

// Complex Orchestration (Advanced)
[Webhook]  [Split]  [
  [API Call 1]  [Transform 1],
  [API Call 2]  [Transform 2],
  [API Call 3]  [Transform 3]
]  [Merge]  [Aggregate]  [Respond]
// Complexity Score: High
// Maintainability: Requires documentation
```

### 3. Expression Quality Assessment

**Expression Patterns Analysis:**
```javascript
// Simple Expression (Good)
{{ $json.user.email }}
// Complexity: 1, Readability: High

// Moderate Expression (Acceptable)
{{ $json.items.filter(i => i.status === 'active').length }}
// Complexity: 2, Readability: Medium

// Complex Expression (Needs Review)
{{ $json.data.reduce((acc, item) => {
  return acc + (item.value > 100 ? item.value * 0.9 : item.value);
}, 0) }}
// Complexity: 4, Readability: Low, Recommendation: Extract to Code node
```

**Expression Quality Metrics:**
- Average expression complexity
- Null safety implementation rate
- Error handling coverage in expressions
- Performance optimization opportunities
- Code node vs inline expression balance

### 4. Performance Analysis

**Execution Efficiency:**
- Parallel processing utilization
- Unnecessary sequential processing
- Redundant data transformations
- Inefficient API call patterns
- Resource-intensive operations

**Optimization Opportunities:**
```javascript
// Inefficient (Sequential)
[HTTP Request 1]  [HTTP Request 2]  [HTTP Request 3]

// Optimized (Parallel)
[Split]  [
  [HTTP Request 1],
  [HTTP Request 2],
  [HTTP Request 3]
]  [Merge]

// Performance Improvement: 3x faster
```

### 5. Error Handling and Reliability

**Error Handling Coverage:**
- Percentage of nodes with error handling
- Error workflow completeness
- Fallback strategy implementation
- Recovery mechanism presence
- Error notification configuration

**Reliability Patterns:**
- Retry logic for API calls
- Timeout configuration
- Circuit breaker patterns
- Graceful degradation
- Data validation before processing

### 6. Security and Compliance

**Security Quality Assessment:**
- Credential management practices
- Sensitive data handling
- Input validation coverage
- Output sanitization
- API key and secret exposure risk

**Compliance Patterns:**
- Data retention policies
- Audit logging implementation
- Access control patterns
- Encryption usage
- Privacy protection measures

## Quality Scoring Framework

### Overall Quality Score Calculation

**Score Components:**
1. **Structure Quality (25%)**
   - Workflow organization
   - Node arrangement
   - Connection clarity
   - Documentation completeness

2. **Expression Quality (20%)**
   - Expression complexity
   - Null safety
   - Error handling
   - Performance optimization

3. **Error Handling (20%)**
   - Coverage percentage
   - Pattern quality
   - Recovery strategies
   - Notification setup

4. **Performance (15%)**
   - Execution efficiency
   - Resource utilization
   - Optimization implementation
   - Parallel processing usage

5. **Security (10%)**
   - Credential management
   - Data protection
   - Input validation
   - Secret handling

6. **Maintainability (10%)**
   - Documentation quality
   - Code readability
   - Pattern consistency
   - Technical debt

### Quality Levels

**Level 5 (90-100%)**: Optimizing - Industry Leading
- Production-ready with best practices
- Comprehensive error handling and monitoring
- Optimal performance and security
- Excellent documentation and maintainability

**Level 4 (80-89%)**: Quantitatively Managed
- Well-structured with good practices
- Adequate error handling
- Good performance and security
- Documented with minor gaps

**Level 3 (70-79%)**: Defined - Well Architected
- Organized with standard practices
- Basic error handling present
- Acceptable performance
- Minimal documentation

**Level 2 (60-69%)**: Managed - Functional
- Working but needs improvement
- Inconsistent error handling
- Performance concerns exist
- Limited documentation

**Level 1 (<60%)**: Basic - Needs Significant Work
- Quality issues throughout
- Poor error handling
- Performance problems
- Insufficient documentation

## Workflow Pattern Assessment

### Best Practice Patterns

**Recommended Patterns:**
- **Input Validation Pattern**: Validate data at workflow entry
- **Error Boundary Pattern**: Comprehensive error handling blocks
- **Async Optimization Pattern**: Parallel processing for independent operations
- **State Management Pattern**: Consistent data flow through workflow
- **Logging Pattern**: Strategic logging for debugging and monitoring

**Anti-Patterns to Identify:**
- Sequential execution of independent operations
- Missing error handling on critical nodes
- Hardcoded values instead of configuration
- Overly complex expressions (should be Code nodes)
- Lack of input validation
- Poor credential management
- Insufficient documentation

## Deliverables

All deliverables use reverse date stamp format: **YYYY-MM-DD-HHMMSS**

1. **Workflow_Quality_Dashboard_YYYY-MM-DD-HHMMSS.ipynb**
   - Comprehensive quality metrics and scoring
   - Visual quality score breakdown
   - Trend analysis (if historical data available)
   - Comparative benchmarking

2. **Quality_Analysis_Report_YYYY-MM-DD-HHMMSS.ipynb**
   - Detailed analysis by dimension
   - Pattern identification and assessment
   - Issue prioritization with impact analysis
   - Specific improvement recommendations

3. **Performance_Analysis_YYYY-MM-DD-HHMMSS.ipynb**
   - Execution efficiency analysis
   - Bottleneck identification
   - Optimization opportunities
   - Resource utilization assessment

4. **Security_Compliance_Review_YYYY-MM-DD-HHMMSS.ipynb**
   - Security pattern analysis
   - Credential management assessment
   - Compliance gap identification
   - Risk mitigation recommendations

5. **Improvement_Roadmap_YYYY-MM-DD-HHMMSS.ipynb**
   - Prioritized improvement recommendations
   - Effort vs impact assessment
   - Implementation guidance
   - Expected quality improvements

## Quality Analysis Checklist

### Complexity Analysis
- [ ] Node count assessed and scored
- [ ] Connection complexity calculated
- [ ] Expression complexity measured
- [ ] Workflow depth analyzed
- [ ] Maintainability score calculated

### Pattern Assessment
- [ ] Workflow architecture pattern identified
- [ ] Best practices adherence verified
- [ ] Anti-patterns detected and documented
- [ ] Pattern consistency evaluated
- [ ] Alternative patterns considered

### Expression Analysis
- [ ] All expressions catalogued and analyzed
- [ ] Complexity metrics calculated
- [ ] Null safety assessed
- [ ] Performance impact evaluated
- [ ] Optimization opportunities identified

### Performance Analysis
- [ ] Execution efficiency measured
- [ ] Parallel processing opportunities identified
- [ ] Bottlenecks detected and documented
- [ ] Resource utilization assessed
- [ ] Optimization recommendations created

### Error Handling Analysis
- [ ] Error handling coverage calculated
- [ ] Error patterns evaluated
- [ ] Recovery strategies assessed
- [ ] Notification setup verified
- [ ] Reliability improvements identified

### Security Analysis
- [ ] Credential management reviewed
- [ ] Sensitive data handling assessed
- [ ] Input validation coverage measured
- [ ] Secret exposure risks identified
- [ ] Security improvements recommended

### Quality Scoring
- [ ] Overall quality score calculated
- [ ] Component scores determined
- [ ] Quality level assigned
- [ ] Improvement priorities identified
- [ ] Target quality goals defined

## Advanced n8n Quality Analysis

### 7. Execution Timeout Analysis

**Execution Timeout Configuration Assessment:**

**MANDATORY: Analyze execution timeout settings for production readiness**

```javascript
// Analyze workflow timeout configuration
const timeoutAnalysis = {
  // Workflow-level timeout
  workflowTimeout: workflowJSON.settings?.executionTimeout || 'not_configured',

  // Environment timeout settings
  environmentConfig: {
    EXECUTIONS_TIMEOUT: process.env.EXECUTIONS_TIMEOUT || 300,  // Default 5 min
    EXECUTIONS_TIMEOUT_MAX: process.env.EXECUTIONS_TIMEOUT_MAX || 3600  // Default 1 hour
  },

  // Node-specific timeout analysis
  nodeTimeouts: workflowJSON.nodes.map(node => ({
    name: node.name,
    type: node.type,
    hasTimeout: node.parameters?.timeout !== undefined,
    timeoutValue: node.parameters?.timeout,
    recommendation: getTimeoutRecommendation(node.type)
  })),

  // Risk assessment
  risks: identifyTimeoutRisks(workflowJSON)
}

function getTimeoutRecommendation(nodeType) {
  const recommendations = {
    'n8n-nodes-base.httpRequest': 30000,      // 30 seconds
    'n8n-nodes-base.postgres': 60000,         // 1 minute
    'n8n-nodes-base.mysql': 60000,            // 1 minute
    'n8n-nodes-base.webhook': 10000,          // 10 seconds
    'n8n-nodes-base.code': 5000,              // 5 seconds
    'default': 30000
  }
  return recommendations[nodeType] || recommendations.default
}
```

**Timeout Configuration Best Practices:**
```javascript
{
  "settings": {
    "executionTimeout": 300,              // 5 minute workflow timeout
    "saveExecutionProgress": true,        // Enable recovery
    "saveDataSuccessExecution": "all",    // Full execution data
    "saveDataErrorExecution": "all"       // Error debugging
  },
  "nodes": [
    {
      "parameters": {
        "url": "https://api.example.com",
        "timeout": 30000,                 // 30 second node timeout
        "retry": {
          "maxTries": 3,
          "waitBetweenTries": 1000
        }
      },
      "type": "n8n-nodes-base.httpRequest"
    }
  ]
}
```

**Timeout Analysis Checklist:**
- [ ] Workflow-level execution timeout configured appropriately
- [ ] Critical nodes have explicit timeout settings
- [ ] Timeout values match operation complexity (API: 30s, DB: 60s)
- [ ] Long-running operations use appropriate timeouts (< EXECUTIONS_TIMEOUT)
- [ ] Timeout error handling configured (continueOnFail, retryOnFail)
- [ ] Execution progress saving enabled for recovery
- [ ] Timeout monitoring and alerting configured

### 8. Queue Mode Scalability Analysis

**Queue Mode Configuration Assessment:**

**MANDATORY: Assess queue mode setup for production scaling**

```javascript
// Queue mode configuration analysis
const queueModeAnalysis = {
  // Environment configuration
  queueModeEnabled: process.env.EXECUTIONS_MODE === 'queue',

  queueConfig: {
    redisHost: process.env.QUEUE_BULL_REDIS_HOST,
    redisPort: process.env.QUEUE_BULL_REDIS_PORT,
    redisDB: process.env.QUEUE_BULL_REDIS_DB,
    healthCheckActive: process.env.QUEUE_HEALTH_CHECK_ACTIVE === 'true'
  },

  // Worker configuration
  workerConfig: {
    concurrency: process.env.QUEUE_WORKER_CONCURRENCY || 10,
    maxJobsPerWorker: process.env.QUEUE_WORKER_MAX_JOBS || 100
  },

  // Workflow queue readiness
  workflowQueueReadiness: {
    hasExecutionTimeout: workflowJSON.settings?.executionTimeout !== undefined,
    hasProgressSaving: workflowJSON.settings?.saveExecutionProgress === true,
    hasErrorLogging: workflowJSON.settings?.saveDataErrorExecution !== 'none',
    isStateless: !usesWorkflowStaticData(workflowJSON),  // Stateless preferred for queue

    readinessScore: calculateQueueReadiness(workflowJSON)
  },

  // Scaling assessment
  scalingMetrics: {
    estimatedThroughput: calculateThroughput(workflowJSON),
    recommendedWorkers: calculateWorkerCount(estimatedLoad),
    queueCapacity: calculateQueueCapacity(),
    scalingRecommendations: generateScalingRecommendations()
  }
}
```

**Queue Mode Best Practices:**
```javascript
// Workflow configuration for queue mode
{
  "settings": {
    "executionOrder": "v1",
    "executionTimeout": 300,
    "saveExecutionProgress": true,       // CRITICAL for queue recovery
    "saveDataSuccessExecution": "all",
    "saveDataErrorExecution": "all"
  }
}

// Environment configuration (.env)
EXECUTIONS_MODE=queue
QUEUE_BULL_REDIS_HOST=localhost
QUEUE_BULL_REDIS_PORT=6379
QUEUE_BULL_REDIS_DB=0
QUEUE_HEALTH_CHECK_ACTIVE=true
QUEUE_WORKER_CONCURRENCY=10              // Adjust based on resources
QUEUE_WORKER_MAX_JOBS=100
```

**Queue Mode Monitoring Workflow:**
```json
{
  "name": "Queue_Health_Monitor",
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
        "jsCode": "const queueStats = $getWorkflowStaticData('global');\nif (queueStats.waiting > 1000) {\n  return { json: { alert: 'HIGH_QUEUE', count: queueStats.waiting } };\n}\nreturn { json: { status: 'OK' } };"
      },
      "name": "Check Queue",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Queue Scalability Checklist:**
- [ ] Queue mode environment variables configured
- [ ] Redis connection established and tested
- [ ] Worker concurrency optimized for resources
- [ ] Workflow execution timeout configured
- [ ] Execution progress saving enabled
- [ ] Queue health monitoring implemented
- [ ] Worker scaling strategy defined
- [ ] Queue overflow handling configured

### 9. Audit Trail Analysis

**Audit Logging Completeness Assessment:**

**MANDATORY: Analyze audit trail for compliance and debugging**

```javascript
// Audit trail analysis
const auditAnalysis = {
  // Execution data retention
  dataRetention: {
    successExecutions: workflowJSON.settings?.saveDataSuccessExecution || 'none',
    errorExecutions: workflowJSON.settings?.saveDataErrorExecution || 'none',
    manualExecutions: workflowJSON.settings?.saveManualExecutions !== false
  },

  // Audit logging coverage
  auditCoverage: {
    // Check for audit logging nodes
    hasAuditLog: workflowJSON.nodes.some(n =>
      n.type === 'n8n-nodes-base.code' &&
      n.parameters.jsCode.includes('audit') ||
      n.parameters.jsCode.includes('log')
    ),

    // Execution metadata tracking
    tracksExecutionMetadata: workflowJSON.nodes.some(n =>
      n.type === 'n8n-nodes-base.code' &&
      n.parameters.jsCode.includes('$execution.id') &&
      n.parameters.jsCode.includes('$workflow.id')
    ),

    // User action tracking
    tracksUserActions: workflowJSON.nodes.some(n =>
      n.parameters?.jsCode?.includes('$execution.user') ||
      n.parameters?.jsCode?.includes('$execution.mode')
    )
  },

  // Compliance requirements
  complianceChecks: {
    dataRetentionPolicy: checkDataRetentionPolicy(),
    accessControlLogging: checkAccessControlLogging(),
    changeTracking: checkChangeTracking(),
    sensitiveDataHandling: checkSensitiveDataLogging()
  }
}
```

**Audit Trail Best Practices:**
```javascript
// Comprehensive audit logging pattern
{
  "parameters": {
    "jsCode": `
// Comprehensive audit log
const auditLog = {
  timestamp: new Date().toISOString(),

  // Execution context
  execution: {
    id: $execution.id,
    mode: $execution.mode,  // 'manual', 'trigger', 'webhook', 'retry'
    startedAt: $execution.startedAt,
    user: $execution.user || 'system'
  },

  // Workflow context
  workflow: {
    id: $workflow.id,
    name: $workflow.name,
    active: $workflow.active,
    version: $workflow.versionId || 'unknown'
  },

  // Action performed
  action: {
    type: 'data_access|data_modification|external_api_call',
    description: 'User data retrieved from CRM',
    node: $node.name,
    input_count: $input.all().length,
    output_count: $json.items?.length || 1
  },

  // Data access tracking (compliance)
  dataAccess: {
    tables: ['customers', 'orders'],
    recordIds: $json.items?.map(i => i.id) || [],
    sensitiveFields: ['email', 'phone'],
    purpose: 'customer_support_query'
  }
};

// Store audit log (database, file, or external service)
return { json: auditLog };
`
  },
  "name": "Audit Logger",
  "type": "n8n-nodes-base.code"
}
```

**Audit Trail Checklist:**
- [ ] Execution data retention configured (success and error)
- [ ] Audit logging nodes implemented at critical points
- [ ] Execution metadata tracked (ID, user, timestamp, mode)
- [ ] User actions logged with context
- [ ] Data access logged for compliance (GDPR, HIPAA)
- [ ] Change tracking implemented for modifications
- [ ] Sensitive data handling logged appropriately
- [ ] Audit log retention policy defined and enforced

### 10. Backup/Recovery Pattern Analysis

**Backup and Recovery Strategy Assessment:**

**MANDATORY: Analyze backup and disaster recovery capabilities**

```javascript
// Backup/recovery analysis
const backupAnalysis = {
  // Workflow backup strategy
  workflowBackup: {
    versionControl: checkGitIntegration(workflowJSON),
    exportCapability: true,  // n8n export:workflow command
    backupFrequency: 'manual',  // Should be automated
    backupLocation: process.env.WORKFLOW_BACKUP_PATH || 'not_configured'
  },

  // Execution data recovery
  executionRecovery: {
    progressSaving: workflowJSON.settings?.saveExecutionProgress === true,
    dataRetention: workflowJSON.settings?.saveDataSuccessExecution !== 'none',
    errorDataRetention: workflowJSON.settings?.saveDataErrorExecution !== 'none',
    recoverableStates: identifyRecoverableStates(workflowJSON)
  },

  // Static data persistence
  staticDataBackup: {
    usesStaticData: usesWorkflowStaticData(workflowJSON),
    staticDataPersistence: process.env.DB_TYPE !== undefined,  // PostgreSQL/MySQL
    staticDataBackupStrategy: checkStaticDataBackup()
  },

  // Credential backup
  credentialBackup: {
    credentialCount: countCredentialReferences(workflowJSON),
    credentialExportSupported: true,
    secretsManagement: checkExternalSecretsManager()
  },

  // Recovery procedures
  recoveryProcedures: {
    hasRecoveryWorkflow: false,  // Should implement
    documentedRecoverySteps: false,  // Should document
    testedRecoveryPlan: false,  // Should test
    rpo: 'unknown',  // Recovery Point Objective
    rto: 'unknown'   // Recovery Time Objective
  }
}
```

**Backup Best Practices:**
```bash
# Automated workflow backup script
#!/bin/bash

# Export all workflows
n8n export:workflow --all --output=./backups/workflows/

# Export credentials (encrypted)
n8n export:credentials --all --output=./backups/credentials/

# Backup workflow static data (if using database)
pg_dump -h localhost -U n8n n8n_db > ./backups/db/n8n_backup_$(date +%Y%m%d).sql

# Commit to Git
git add backups/
git commit -m "chore(backup): automated workflow backup $(date +%Y-%m-%d)"
git push origin backup-branch

# Upload to cloud storage
aws s3 sync ./backups/ s3://n8n-backups/$(date +%Y-%m-%d)/
```

**Recovery Workflow Implementation:**
```json
{
  "name": "Disaster_Recovery_Workflow",
  "nodes": [
    {
      "parameters": {
        "jsCode": `
// Recovery validation
const recovery = {
  workflow: {
    id: $workflow.id,
    lastBackup: $getWorkflowStaticData('global').lastBackup,
    backupStatus: checkBackupExists($workflow.id)
  },

  actions: {
    validateBackup: validateWorkflowBackup(),
    restoreFromBackup: restoreWorkflow($workflow.id),
    verifyFunctionality: testWorkflowExecution()
  }
};

return { json: recovery };
`
      },
      "name": "Recovery Validator",
      "type": "n8n-nodes-base.code"
    }
  ]
}
```

**Backup/Recovery Checklist:**
- [ ] Automated workflow backup configured (daily/weekly)
- [ ] Workflow export to version control (Git)
- [ ] Execution progress saving enabled
- [ ] Static data persistence configured
- [ ] Credential backup strategy implemented
- [ ] Recovery procedures documented
- [ ] Recovery testing performed regularly
- [ ] RPO/RTO defined and achievable
- [ ] Cloud backup for disaster recovery

### 11. Health Check Pattern Analysis

**Health Check Implementation Assessment:**

**MANDATORY: Analyze workflow health monitoring**

```javascript
// Health check analysis
const healthCheckAnalysis = {
  // Workflow-level health checks
  workflowHealth: {
    hasHealthCheckEndpoint: workflowJSON.nodes.some(n =>
      n.type === 'n8n-nodes-base.webhook' &&
      n.parameters.path?.includes('health')
    ),

    hasScheduledHealthCheck: workflowJSON.nodes.some(n =>
      n.type === 'n8n-nodes-base.scheduleTrigger'
    ),

    healthCheckFrequency: identifyHealthCheckFrequency(workflowJSON)
  },

  // Dependency health checks
  dependencyHealth: {
    checksExternalAPIs: checkAPIHealthMonitoring(workflowJSON),
    checksDatabases: checkDatabaseHealthMonitoring(workflowJSON),
    checksCredentials: checkCredentialValidation(workflowJSON)
  },

  // Alerting configuration
  alertingConfig: {
    hasAlertingWorkflow: workflowJSON.settings?.errorWorkflow !== undefined,
    alertChannels: identifyAlertChannels(workflowJSON),
    alertThresholds: extractAlertThresholds(workflowJSON)
  },

  // Self-healing capabilities
  selfHealing: {
    hasAutoRecovery: checkAutoRecoveryPatterns(workflowJSON),
    hasCircuitBreaker: checkCircuitBreakerPatterns(workflowJSON),
    hasFallbackLogic: checkFallbackPatterns(workflowJSON)
  }
}
```

**Health Check Workflow Implementation:**
```json
{
  "name": "System_Health_Monitor",
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
        "jsCode": `
// Comprehensive health check
const healthStatus = {
  timestamp: new Date().toISOString(),

  // Workflow health
  workflow: {
    active: $workflow.active,
    lastExecution: await getLastExecution($workflow.id),
    errorRate: calculateErrorRate($workflow.id, 3600000),  // Last hour
    avgDuration: calculateAvgDuration($workflow.id, 3600000)
  },

  // Dependency health
  dependencies: {
    api: await checkAPIHealth('https://api.example.com/health'),
    database: await checkDatabaseHealth(),
    redis: await checkRedisHealth(),
    credentials: await validateCredentials()
  },

  // Resource health
  resources: {
    queueSize: $getWorkflowStaticData('global').queueSize || 0,
    activeExecutions: await getActiveExecutions(),
    memoryUsage: process.memoryUsage(),
    cpuUsage: await getCPUUsage()
  },

  // Overall status
  status: determineOverallHealth(),
  alerts: generateHealthAlerts()
};

// Alert if unhealthy
if (healthStatus.status !== 'healthy') {
  return { json: { ...healthStatus, alert: true } };
}

return { json: healthStatus };
`
      },
      "name": "Health Check",
      "type": "n8n-nodes-base.code"
    },
    {
      "parameters": {
        "conditions": {
          "conditions": [
            {
              "leftValue": "={{ $json.alert }}",
              "rightValue": true,
              "operator": { "type": "boolean", "operation": "true" }
            }
          ]
        }
      },
      "name": "Alert Required?",
      "type": "n8n-nodes-base.if"
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": { "__rl": true, "value": "C12345", "mode": "id" },
        "text": "= *Health Alert*\n\nWorkflow: {{ $json.workflow.name }}\nStatus: {{ $json.status }}\nError Rate: {{ $json.workflow.errorRate }}%\nDependencies: {{ $json.dependencies }}"
      },
      "name": "Send Alert",
      "type": "n8n-nodes-base.slack"
    }
  ],
  "connections": {
    "Every 5 Minutes": {
      "main": [[{ "node": "Health Check", "type": "main", "index": 0 }]]
    },
    "Health Check": {
      "main": [[{ "node": "Alert Required?", "type": "main", "index": 0 }]]
    },
    "Alert Required?": {
      "main": [[{ "node": "Send Alert", "type": "main", "index": 0 }], []]
    }
  }
}
```

**Health Check Checklist:**
- [ ] Scheduled health check workflow implemented
- [ ] Health check endpoint available (webhook)
- [ ] External API health monitored
- [ ] Database connectivity checked
- [ ] Credential validity verified
- [ ] Queue health monitored (if queue mode)
- [ ] Resource usage tracked (CPU, memory)
- [ ] Error rate threshold alerting configured
- [ ] Self-healing patterns implemented
- [ ] Health check results logged and trended

## Success Criteria

- [ ] Comprehensive quality metrics calculated and documented
- [ ] Overall quality score determined with breakdown
- [ ] All quality dimensions analyzed thoroughly
- [ ] Workflow patterns identified and assessed
- [ ] Performance analysis completed with recommendations
- [ ] Security compliance reviewed and gaps identified
- [ ] Error handling coverage measured and evaluated
- [ ] Improvement opportunities prioritized by impact
- [ ] All deliverables created with proper reverse date stamps
- [ ] Actionable recommendations provided for each quality gap
- [ ] Quality improvement roadmap created with effort estimates

**Execution Timeout Analysis:**
- [ ] Workflow execution timeout configured appropriately
- [ ] Node-specific timeouts analyzed and optimized
- [ ] Timeout error handling validated
- [ ] Long-running operation timeouts reviewed
- [ ] Execution progress saving enabled
- [ ] Timeout monitoring and alerting configured

**Queue Mode Scalability:**
- [ ] Queue mode configuration assessed
- [ ] Worker concurrency optimized
- [ ] Workflow queue readiness validated
- [ ] Scaling metrics calculated
- [ ] Queue monitoring implemented
- [ ] Worker scaling strategy defined

**Audit Trail Analysis:**
- [ ] Execution data retention configured
- [ ] Audit logging coverage verified
- [ ] User action tracking implemented
- [ ] Data access logging for compliance
- [ ] Change tracking validated
- [ ] Audit log retention policy defined

**Backup/Recovery Analysis:**
- [ ] Automated backup strategy validated
- [ ] Version control integration verified
- [ ] Execution recovery capability confirmed
- [ ] Static data backup strategy assessed
- [ ] Credential backup validated
- [ ] Recovery procedures documented and tested
- [ ] RPO/RTO objectives defined

**Health Check Analysis:**
- [ ] Health check workflow implementation verified
- [ ] Dependency health monitoring validated
- [ ] Alerting configuration assessed
- [ ] Self-healing capabilities identified
- [ ] Health check frequency optimized
- [ ] Resource monitoring implemented

## Command Integration

- **Previous Phase**: `n8n-workflow-implementation` or `n8n-workflow-lint-quality-check` (after validation)
- **Parallel**: `n8n-workflow-review` (human review), `n8n-workflow-lint-quality-check` (automated validation)
- **Next Phase**: `n8n-workflow-refactor` (apply improvements) or `n8n-workflow-gap-analysis` (compare to requirements)

## Next Phase Preparation

After quality analysis completion, proceed based on findings:

```bash
# If quality score is low (<70%), refactor workflow:
/n8n-workflow-refactor --workflow-id=<id> --focus="quality-improvements" \
  --analysis-report="Workflow_Quality_Dashboard_YYYY-MM-DD-HHMMSS.ipynb"

# If specific gaps identified, run gap analysis:
/n8n-workflow-gap-analysis --workflow-id=<id> \
  --quality-report="Quality_Analysis_Report_YYYY-MM-DD-HHMMSS.ipynb"

# If quality is acceptable, proceed to review:
/n8n-workflow-review --workflow-id=<id> \
  --quality-score=<score> --focus-areas="high-priority-findings"
```

---

**Note**: This is an analysis command that produces comprehensive quality assessment reports and improvement recommendations. No workflow modifications occur during analysis. Use refactor or review commands to implement improvements.
