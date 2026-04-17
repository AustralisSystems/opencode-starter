# === Universal Code End-to-End Testing: AI-Driven Multi-Service Integration Validation Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ AND INDEX**: `.claude/commands/ai-agent-compliance.md`
2. **READ AND INDEX**: `.claude/commands/core/code-protocol-compliance-prompt.md`
3. **READ AND INDEX**: `.claude/commands/test/test-protocol-service-examples.md`
4. **VERIFY**: User has given explicit permission to proceed
5. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of data or services in production code
- **NO TODOs** - complete ALL work immediately
- **NO SHORTCUTS** - implement properly ALWAYS
- **NO STUBS** - write complete implementations
- **NO FIXED DATA** - use real, dynamic data
- **NO HARDCODED VALUES** - use configuration
- **NO WORKAROUNDS** - fix root causes
- **NO FAKE IMPLEMENTATIONS** - real code only
- **NO PLACEHOLDER CODE** - production-ready only
- **NO TEMPORARY SOLUTIONS** - permanent fixes only

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read implementation documents for context
   - Review analysis documents for insights
   - Study documentation documents for patterns

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest documentation
   - Find official framework/library docs
   - Search GitHub for example implementations
   - Review industry best practices
   - Study similar successful projects
   - Check Stack Overflow for common patterns

**SEARCH PRIORITIES:**

- Official documentation (latest version)
- GitHub repositories with high stars
- Industry standard implementations
- Recent blog posts/tutorials (< 1 year old)
- Community best practices

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **END-TO-END-TESTING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR END-TO-END INTEGRATION TESTING ONLY:**

- **MUST:** Implement comprehensive end-to-end testing across all service integrations
- **MUST:** Create detailed multi-service workflow validation procedures
- **MUST:** Generate comprehensive integration testing frameworks and scenarios
- **MUST:** Provide complete end-to-end testing reports with timestamp documentation
- **FORBIDDEN:** Execute ANY actual service implementations or system changes
- **FORBIDDEN:** Modify ANY production services or configurations
- **FORBIDDEN:** Create ANY new service implementations
- **MUST:** Output end-to-end testing results in markdown documents with timestamp tracking

**END-TO-END TESTING FOCUS AREAS:**

- Multi-service integration workflow validation
- Complete user journey testing across all system components
- Data flow validation through entire system architecture
- Service communication and dependency testing
- Performance validation of complete end-to-end scenarios
- Error handling and recovery across service boundaries
- Security validation throughout complete workflows

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-protocol-end-to-end-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for testing_scope, integration_level, workflow_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the end-to-end testing protocol specifications
4. **VERIFY COMPLETION**: Ensure all end-to-end testing objectives and validation criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive end-to-end testing reports with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% end-to-end testing coverage and validation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-protocol-end-to-end-prompt"
arguments:
  testing_scope: "[comprehensive|critical-paths|user-journeys|service-integration|performance-focused|security-focused]"
  integration_level: "[basic|standard|advanced|enterprise|full-system]"
  workflow_complexity: "[simple|standard|complex|enterprise|comprehensive]"
  environment_target: "[optional: local|development|staging|production|multi-environment]"
  validation_depth: "[optional: functional|performance|security|comprehensive]"
  automation_level: "[optional: manual|hybrid|automated|full-automation]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All end-to-end testing phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive multi-service integration testing completed
- [ ] All user journey workflows validated and documented (timestamped)
- [ ] Complete data flow validation through entire system (timestamped)
- [ ] Service communication and dependency testing validated (timestamped)
- [ ] Performance validation of end-to-end scenarios completed (timestamped)
- [ ] Error handling and recovery testing across services (timestamped)
- [ ] Security validation throughout complete workflows (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL END-TO-END TESTING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All end-to-end testing deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All integration testing documentation includes precise timestamps
- [ ] All workflow validation reports include timestamp tracking
- [ ] All service communication testing includes proper date stamps
- [ ] All performance validation follows consistent date stamp format
- [ ] All security testing documentation includes timestamps
- [ ] All error handling testing includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating end-to-end testing files without proper reverse date stamps
- Using inconsistent date formats within same testing session
- Missing timestamps in integration testing documentation

### **END-TO-END TESTING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After end-to-end testing completion, analyze with:
/test-results-analysis [testing-scope] [integration-level] [additional-options]

# Examples:
/test-results-analysis comprehensive full-system
/test-results-analysis user-journeys advanced
/test-results-analysis performance-focused enterprise
```

---

**ENFORCEMENT:** This command performs END-TO-END INTEGRATION TESTING ONLY through the MCP prompt protocol. The comprehensive testing logic is defined in `test-protocol-end-to-end-prompt.yaml` and executed according to Model Context Protocol standards. No actual service implementation or system changes are performed. Use `/test-results-analysis` for result analysis after testing is complete.

model_context:
role: "AI-driven end-to-end integration testing specialist for multi-service workflow validation"
domain: "End-to-End Testing, Multi-Service Integration, Workflow Validation, System Integration"
goal: >
Implement comprehensive end-to-end testing that validates complete user workflows across
all system services, ensures proper service integration and communication, validates
data flow through the entire system architecture, and provides complete integration
testing coverage using Jupyter Notebook format with evidence, metrics, workflow
documentation, and integration validation including Mermaid diagrams.

configuration:

## Overview

This protocol defines comprehensive end-to-end test scenarios, templates, and patterns for validating complete user workflows across all 10 services in the n8n IaC Agentic Automation Platform. These tests validate real-world scenarios from initial user interaction through complete data processing, storage, and visualization. This file is referenced by the `test-protocol-end-to-end-prompt.yaml` MCP prompt.

## Service Architecture for E2E Testing

```
┌──────────────────────────────────────────────────────────────┐
│                    End-to-End Test Flow                       │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  1. n8n (Workflow Orchestration)                             │
│      ↓                                                        │
│  2. PostgreSQL (Workflow State & Data)                       │
│      ↓                                                        │
│  3. Neo4j (Knowledge Graph)                                  │
│      ↓                                                        │
│  4. Qdrant (Vector Embeddings)                               │
│      ↓                                                        │
│  5. LightRAG (RAG Operations)                                │
│      ↓                                                        │
│  6. MinIO (Artifact Storage)                                 │
│      ↓                                                        │
│  7. Terraform Executor (Infrastructure)                      │
│      ↓                                                        │
│  8. Ansible Executor (Configuration)                         │
│      ↓                                                        │
│  9. Prometheus (Metrics Collection)                          │
│      ↓                                                        │
│  10. Grafana (Visualization)                                 │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

## Complete End-to-End Test Scenarios

### Scenario 1: Workflow Creation and Execution

**Test ID:** E2E-001
**Objective:** Validate complete workflow lifecycle from creation to monitoring

```yaml
test_scenario:
  name: "Complete Workflow Lifecycle"
  services_involved: [n8n, PostgreSQL, Neo4j, Prometheus, Grafana]

  test_steps:
    1_workflow_creation:
      - Action: Create new workflow in n8n UI
      - Validation: Workflow saved to PostgreSQL
      - Expected: Workflow ID generated, state persisted

    2_workflow_execution:
      - Action: Trigger workflow execution
      - Validation: Execution state in PostgreSQL
      - Expected: Status updates in real-time

    3_knowledge_graph_update:
      - Action: Workflow creates knowledge nodes
      - Validation: Nodes created in Neo4j
      - Expected: Graph relationships established

    4_metrics_collection:
      - Action: Execution metrics generated
      - Validation: Metrics in Prometheus
      - Expected: Execution time, success rate tracked

    5_visualization:
      - Action: View metrics in Grafana
      - Validation: Dashboard updated
      - Expected: Real-time visualization of workflow metrics

  expected_results:
    - Workflow successfully created and stored
    - Execution completed with proper state tracking
    - Knowledge graph updated with new relationships
    - Metrics collected and visualized
    - Complete audit trail available

  performance_benchmarks:
    workflow_creation_time: "< 500ms"
    execution_start_latency: "< 200ms"
    state_persistence_time: "< 100ms"
    metrics_update_interval: "< 5s"
    dashboard_refresh_rate: "< 2s"
```

### Scenario 2: RAG Pipeline Processing

**Test ID:** E2E-002
**Objective:** Validate complete RAG pipeline from document ingestion to query

```yaml
test_scenario:
  name: "RAG Pipeline End-to-End"
  services_involved: [n8n, MinIO, LightRAG, Qdrant, Neo4j, PostgreSQL]

  test_steps:
    1_document_upload:
      - Action: Upload document via n8n workflow
      - Validation: Document stored in MinIO
      - Expected: S3 URL generated, metadata saved

    2_document_processing:
      - Action: LightRAG processes document
      - Validation: Processing status tracked
      - Expected: Document parsed and chunked

    3_embedding_generation:
      - Action: Generate vector embeddings
      - Validation: Embeddings stored in Qdrant
      - Expected: Vectors indexed and searchable

    4_knowledge_extraction:
      - Action: Extract entities and relationships
      - Validation: Knowledge graph in Neo4j
      - Expected: Entities and relations created

    5_query_execution:
      - Action: Execute semantic search query
      - Validation: Results from RAG pipeline
      - Expected: Relevant documents retrieved

  expected_results:
    - Document successfully uploaded and stored
    - Processing pipeline completed without errors
    - Embeddings generated and indexed
    - Knowledge graph populated
    - Queries return relevant results

  performance_benchmarks:
    document_upload_time: "< 2s"
    processing_time_per_page: "< 500ms"
    embedding_generation_time: "< 200ms/chunk"
    query_response_time: "< 500ms"
    relevance_score: "> 0.8"
```

### Scenario 3: Infrastructure Automation

**Test ID:** E2E-003
**Objective:** Validate infrastructure provisioning through workflow automation

```yaml
test_scenario:
  name: "Infrastructure as Code Automation"
  services_involved:
    [n8n, Terraform Executor, Ansible Executor, PostgreSQL, Prometheus]

  test_steps:
    1_infrastructure_request:
      - Action: Submit infrastructure request via n8n
      - Validation: Request logged in PostgreSQL
      - Expected: Request ID generated, parameters saved

    2_terraform_execution:
      - Action: Terraform executor provisions resources
      - Validation: Terraform state tracked
      - Expected: Resources created, state updated

    3_ansible_configuration:
      - Action: Ansible executor configures resources
      - Validation: Configuration playbook executed
      - Expected: Resources configured, inventory updated

    4_validation_checks:
      - Action: Validate infrastructure health
      - Validation: Health checks pass
      - Expected: All resources operational

    5_monitoring_setup:
      - Action: Configure monitoring for new resources
      - Validation: Prometheus targets added
      - Expected: Metrics collection started

  expected_results:
    - Infrastructure request processed successfully
    - Resources provisioned via Terraform
    - Configuration applied via Ansible
    - Health checks passing
    - Monitoring configured and active

  performance_benchmarks:
    request_processing_time: "< 5s"
    terraform_plan_time: "< 30s"
    ansible_playbook_time: "< 60s"
    health_check_time: "< 10s"
    monitoring_setup_time: "< 15s"
```

### Scenario 4: Data Integration Pipeline

**Test ID:** E2E-004
**Objective:** Validate data flow across all storage systems

```yaml
test_scenario:
  name: "Complete Data Integration"
  services_involved: [All 10 services]

  test_steps:
    1_data_ingestion:
      - Action: Ingest data through n8n webhook
      - Validation: Data received and validated
      - Expected: Webhook response 200 OK

    2_data_transformation:
      - Action: Transform data in n8n workflow
      - Validation: Transformation rules applied
      - Expected: Data structure normalized

    3_relational_storage:
      - Action: Store structured data in PostgreSQL
      - Validation: Data persisted in tables
      - Expected: ACID compliance maintained

    4_graph_relationships:
      - Action: Create graph relationships in Neo4j
      - Validation: Nodes and edges created
      - Expected: Graph traversal possible

    5_vector_indexing:
      - Action: Generate and store vectors in Qdrant
      - Validation: Vectors indexed
      - Expected: Similarity search functional

    6_object_storage:
      - Action: Store artifacts in MinIO
      - Validation: Objects accessible via S3 API
      - Expected: Versioning and lifecycle policies active

    7_infrastructure_update:
      - Action: Update infrastructure based on data
      - Validation: Terraform/Ansible execution
      - Expected: Infrastructure scaled accordingly

    8_metrics_generation:
      - Action: Generate metrics from pipeline
      - Validation: Prometheus scraping metrics
      - Expected: Custom metrics available

    9_dashboard_update:
      - Action: Update Grafana dashboards
      - Validation: Visualizations refreshed
      - Expected: Real-time data displayed

    10_rag_enrichment:
      - Action: Enrich data with RAG
      - Validation: Context added from knowledge base
      - Expected: Enhanced data output

  expected_results:
    - Data successfully flows through all services
    - Each service processes data correctly
    - Data consistency maintained
    - Complete audit trail available
    - All integrations functional

  performance_benchmarks:
    total_pipeline_time: "< 10s"
    data_consistency: "100%"
    service_availability: "> 99.9%"
    error_rate: "< 0.1%"
    throughput: "> 100 records/second"
```

## User Journey Test Cases

### Journey 1: Business User Creating Automation

```yaml
user_journey:
  persona: "Business Analyst"
  goal: "Create automated report generation"

  steps:
    1_login:
      - Access n8n UI
      - Authenticate with credentials
      - Navigate to workflow editor

    2_workflow_design:
      - Drag and drop nodes
      - Configure data sources
      - Set schedule trigger

    3_test_execution:
      - Execute test run
      - Review output
      - Validate results

    4_deployment:
      - Activate workflow
      - Configure alerts
      - Set up monitoring

    5_monitoring:
      - View execution history
      - Check performance metrics
      - Review generated reports

  success_criteria:
    - Workflow created without technical knowledge
    - Automated execution successful
    - Reports generated on schedule
    - Metrics visible in dashboard
```

### Journey 2: DevOps Engineer Deploying Infrastructure

```yaml
user_journey:
  persona: "DevOps Engineer"
  goal: "Deploy multi-cloud infrastructure"

  steps:
    1_template_selection:
      - Browse infrastructure templates
      - Select multi-cloud template
      - Customize parameters

    2_validation:
      - Review Terraform plan
      - Validate security policies
      - Check cost estimates

    3_deployment:
      - Approve deployment
      - Monitor provisioning
      - Verify resources

    4_configuration:
      - Apply Ansible playbooks
      - Configure services
      - Set up monitoring

    5_validation:
      - Run health checks
      - Verify connectivity
      - Test failover scenarios

  success_criteria:
    - Infrastructure deployed across clouds
    - All services configured correctly
    - Monitoring and alerts active
    - Disaster recovery tested
```

## Integration Test Patterns

### Pattern 1: Service Chain Validation

```python
def test_service_chain():
    """Test complete service chain integration"""

    # Step 1: Create workflow in n8n
    workflow_id = create_n8n_workflow({
        "name": "Test Workflow",
        "nodes": ["webhook", "transform", "database"]
    })

    # Step 2: Execute workflow
    execution_id = execute_workflow(workflow_id, test_data)

    # Step 3: Verify PostgreSQL state
    assert verify_postgresql_state(execution_id) == "completed"

    # Step 4: Check Neo4j graph
    assert verify_neo4j_nodes(workflow_id) > 0

    # Step 5: Validate Prometheus metrics
    assert get_prometheus_metric("workflow_execution_total") > 0

    # Step 6: Verify Grafana dashboard
    assert verify_grafana_panel("workflow_metrics") == "active"
```

### Pattern 2: Data Consistency Validation

```python
def test_data_consistency():
    """Validate data consistency across all storage systems"""

    test_record = {
        "id": "test_123",
        "data": "test_data",
        "timestamp": datetime.now()
    }

    # Store in PostgreSQL
    pg_id = store_postgresql(test_record)

    # Create Neo4j node
    neo4j_node = create_neo4j_node(test_record)

    # Generate and store vector
    vector = generate_embedding(test_record["data"])
    qdrant_id = store_qdrant_vector(vector, test_record["id"])

    # Store artifact in MinIO
    minio_url = store_minio_artifact(test_record)

    # Verify consistency
    assert postgresql_get(pg_id) == test_record
    assert neo4j_get_node(neo4j_node) == test_record
    assert qdrant_search(vector)[0]["id"] == test_record["id"]
    assert minio_get(minio_url)["data"] == test_record["data"]
```

## Performance Benchmarks

### Service Response Time Benchmarks

```yaml
benchmarks:
  service_response_times:
    n8n_api: "< 200ms"
    postgresql_query: "< 50ms"
    neo4j_traversal: "< 100ms"
    qdrant_search: "< 150ms"
    lightrag_processing: "< 500ms"
    minio_upload: "< 300ms"
    terraform_plan: "< 30s"
    ansible_playbook: "< 60s"
    prometheus_query: "< 100ms"
    grafana_render: "< 500ms"

  end_to_end_workflows:
    simple_workflow: "< 2s"
    rag_pipeline: "< 5s"
    infrastructure_provision: "< 5m"
    data_integration: "< 10s"
    monitoring_update: "< 1s"

  concurrent_operations:
    max_concurrent_workflows: 100
    max_concurrent_users: 500
    max_throughput: "1000 ops/sec"

  resource_utilization:
    cpu_usage: "< 70%"
    memory_usage: "< 80%"
    disk_io: "< 85%"
    network_bandwidth: "< 75%"
```

## Failure Recovery Scenarios

### Scenario 1: Service Failure Recovery

```yaml
failure_scenario:
  name: "PostgreSQL Failure Recovery"

  test_steps:
    1_simulate_failure:
      - Action: Stop PostgreSQL container
      - Expected: n8n enters degraded mode

    2_verify_failover:
      - Action: Check failover mechanisms
      - Expected: Read-only mode activated

    3_recovery:
      - Action: Restart PostgreSQL
      - Expected: Service recovers, data intact

    4_validation:
      - Action: Verify data consistency
      - Expected: No data loss, full functionality restored
```

### Scenario 2: Network Partition Recovery

```yaml
failure_scenario:
  name: "Network Partition Handling"

  test_steps:
    1_simulate_partition:
      - Action: Create network partition
      - Expected: Services detect partition

    2_verify_isolation:
      - Action: Check service isolation
      - Expected: Services continue in isolated mode

    3_heal_partition:
      - Action: Restore network connectivity
      - Expected: Services reconnect

    4_data_reconciliation:
      - Action: Verify data reconciliation
      - Expected: Consistency restored
```

## Test Data Templates

### Template 1: Workflow Test Data

```json
{
  "workflow_test_data": {
    "simple_workflow": {
      "trigger": "webhook",
      "payload": {
        "test_id": "{{TEST_ID}}",
        "timestamp": "{{TIMESTAMP}}",
        "data": "test_data"
      }
    },
    "complex_workflow": {
      "trigger": "schedule",
      "nodes": ["transform", "branch", "merge"],
      "test_cases": [
        { "input": "A", "expected": "X" },
        { "input": "B", "expected": "Y" }
      ]
    }
  }
}
```

### Template 2: Infrastructure Test Data

```yaml
infrastructure_test_data:
  terraform_variables:
    environment: "test"
    region: "us-east-1"
    instance_type: "t3.micro"

  ansible_inventory:
    hosts:
      - name: "test-server-1"
        ip: "10.0.1.10"
      - name: "test-server-2"
        ip: "10.0.1.11"
```

## Validation Matrices

### Service Integration Matrix

```
| Service A | Service B | Integration Type | Status | Test Coverage |
|-----------|-----------|------------------|--------|---------------|
| n8n | PostgreSQL | Data Persistence | ✓ | 100% |
| n8n | Neo4j | Graph Creation | ✓ | 95% |
| n8n | MinIO | File Storage | ✓ | 90% |
| LightRAG | Qdrant | Vector Storage | ✓ | 100% |
| LightRAG | Neo4j | Knowledge Graph | ✓ | 85% |
| Terraform | n8n | API Integration | ✓ | 80% |
| Ansible | n8n | API Integration | ✓ | 75% |
| Prometheus | All Services | Metrics | ✓ | 100% |
| Grafana | Prometheus | Visualization | ✓ | 100% |
```

### Data Flow Validation Matrix

```
| Data Type | Source | Destination | Transformation | Validation |
|-----------|--------|-------------|----------------|------------|
| Workflow State | n8n | PostgreSQL | JSON → Relational | Schema |
| Knowledge | Documents | Neo4j | Text → Graph | Relationships |
| Embeddings | Text | Qdrant | Text → Vectors | Similarity |
| Artifacts | n8n | MinIO | Binary → S3 | Checksum |
| Metrics | All | Prometheus | Events → TimeSeries | Labels |
```

## Monitoring and Alerting for E2E Tests

### Test Execution Monitoring

```yaml
monitoring_config:
  prometheus_metrics:
    - e2e_test_duration_seconds
    - e2e_test_success_total
    - e2e_test_failure_total
    - service_integration_errors_total
    - data_consistency_violations_total

  grafana_dashboards:
    - name: "E2E Test Overview"
      panels:
        - "Test Execution Timeline"
        - "Service Integration Status"
        - "Data Flow Visualization"
        - "Performance Metrics"
        - "Error Rate Analysis"

  alerting_rules:
    - alert: "E2E Test Failure"
      condition: "e2e_test_failure_total > 0"
      severity: "critical"

    - alert: "Service Integration Error"
      condition: "service_integration_errors_total > 5"
      severity: "warning"

    - alert: "Performance Degradation"
      condition: "e2e_test_duration_seconds > threshold"
      severity: "warning"
```

## Compliance and Security Validation

### Security Test Scenarios

```yaml
security_tests:
  authentication_flow:
    - Test OAuth2 authentication
    - Validate JWT tokens
    - Check session management
    - Verify MFA if enabled

  authorization_checks:
    - Test role-based access
    - Validate resource permissions
    - Check API authorization
    - Verify data access controls

  data_protection:
    - Test encryption in transit
    - Validate encryption at rest
    - Check data masking
    - Verify audit logging
```

## Test Automation Scripts

### E2E Test Orchestration Script

```python
class E2ETestOrchestrator:
    """Orchestrates end-to-end test execution across all services"""

    def __init__(self):
        self.services = self.initialize_services()
        self.test_suite = self.load_test_suite()

    def run_e2e_tests(self):
        """Execute complete E2E test suite"""

        results = []

        # Phase 1: Service Health Checks
        for service in self.services:
            assert self.health_check(service), f"{service} not healthy"

        # Phase 2: Execute Test Scenarios
        for scenario in self.test_suite:
            result = self.execute_scenario(scenario)
            results.append(result)

        # Phase 3: Validate Results
        self.validate_results(results)

        # Phase 4: Generate Report
        return self.generate_report(results)

    def execute_scenario(self, scenario):
        """Execute individual test scenario"""

        # Setup test environment
        self.setup_test_data(scenario)

        # Execute test steps
        for step in scenario.steps:
            self.execute_step(step)
            self.validate_step(step)

        # Cleanup
        self.cleanup_test_data(scenario)

        return scenario.get_results()
```

## Continuous E2E Testing Strategy

### CI/CD Integration

```yaml
ci_cd_integration:
  pipeline_stages:
    - stage: "E2E Test Preparation"
      steps:
        - Setup test environment
        - Load test data
        - Verify service health

    - stage: "E2E Test Execution"
      steps:
        - Run smoke tests
        - Execute full E2E suite
        - Collect metrics

    - stage: "Result Analysis"
      steps:
        - Analyze test results
        - Generate reports
        - Update dashboards

    - stage: "Cleanup"
      steps:
        - Archive test results
        - Clean test data
        - Reset environment

  schedule:
    smoke_tests: "*/30 * * * *" # Every 30 minutes
    full_suite: "0 */6 * * *" # Every 6 hours
    performance_tests: "0 2 * * *" # Daily at 2 AM
```

## Success Criteria

### E2E Test Success Metrics

```yaml
success_metrics:
  functional_criteria:
    - All user journeys complete successfully
    - All service integrations functional
    - Data consistency maintained across services
    - All workflows execute without errors

  performance_criteria:
    - Response times within benchmarks
    - Throughput meets requirements
    - Resource utilization within limits
    - No performance degradation over time

  reliability_criteria:
    - Service availability > 99.9%
    - Failure recovery < 5 minutes
    - Data integrity 100%
    - Zero data loss scenarios

  security_criteria:
    - All authentication flows secure
    - Authorization properly enforced
    - Data encryption active
    - Audit trail complete
```

---

This protocol provides comprehensive guidance for end-to-end testing across all services in the n8n IaC platform, ensuring complete validation of user workflows, service integrations, and system reliability.
