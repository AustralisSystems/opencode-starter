# === Universal End-to-End Testing: AI-Driven Multi-Service Integration Validation Protocol ===

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
3. **READ AND INDEX**: `.claude/commands/test/test-protocol-end-to-end.md`
4. **VERIFY**: User has given explicit permission to proceed
5. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Executing E2E tests without validating all service dependencies
- Skipping service integration validation steps
- Ignoring data flow verification requirements
- Proceeding without understanding service architecture
- Creating incomplete E2E test reports
- Using mocked services in E2E testing

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of any services in end-to-end testing
- **NO SHORTCUTS** - validate ALL service interactions
- **NO STUBS** - use real services for E2E tests
- **NO FIXED DATA** - use dynamic test data generation
- **NO HARDCODED VALUES** - use configuration-driven testing
- **NO WORKAROUNDS** - fix actual integration issues
- **NO FAKE IMPLEMENTATIONS** - real service integration only
- **NO PLACEHOLDER CODE** - production-ready E2E tests
- **NO TEMPORARY SOLUTIONS** - permanent test infrastructure

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ E2E TEST DOCUMENTATION:**

   - Read `test-protocol-end-to-end.md` for E2E methodology
   - Review all service integration documentation
   - Study data flow architecture documents
   - Check existing E2E test results

2. **READ SERVICE DOCUMENTATION:**

   - n8n workflow orchestration docs
   - PostgreSQL integration guides
   - Neo4j graph database docs
   - Qdrant vector database docs
   - LightRAG service documentation
   - MinIO S3 storage docs
   - Terraform executor API docs
   - Ansible executor API docs
   - Prometheus monitoring docs
   - Grafana visualization docs

3. **RESEARCH ONLINE E2E PRACTICES:**
   - Use web search for multi-service testing strategies
   - Find integration testing best practices
   - Search GitHub for E2E test examples
   - Review microservices testing patterns
   - Study distributed system testing

**SEARCH PRIORITIES:**

- Official service integration documentation
- Multi-service testing frameworks
- GitHub repositories with comprehensive E2E tests
- Recent distributed testing tutorials
- Community integration testing standards

---

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **TEST-EXECUTION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR END-TO-END TESTING EXECUTION ONLY:**

- **MUST:** Execute comprehensive end-to-end testing across all platform services
- **MUST:** Validate complete user workflows and service integrations
- **MUST:** Test real data flows and system interactions
- **MUST:** Generate detailed test execution reports and matrices
- **FORBIDDEN:** Execute ANY actual deployment or infrastructure changes
- **FORBIDDEN:** Modify ANY production systems or live configurations
- **FORBIDDEN:** Deploy ANY code or make system changes
- **MUST:** Output test results in markdown documents with timestamp tracking

**TEST EXECUTION FOCUS AREAS:**

- End-to-end workflow validation across all 10 services
- Service integration testing and data flow validation
- Performance benchmarking and reliability testing
- User journey validation and experience testing
- Failure recovery and resilience testing
- Monitoring and observability validation
- Security boundary and compliance testing

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-end-to-end-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for test_scope, environment_target, service_coverage
3. **FOLLOW PROTOCOL**: Execute all phases according to the testing protocol specifications
4. **VERIFY COMPLETION**: Ensure all test objectives and validation criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive test execution reports with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% test coverage and validation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-end-to-end-prompt"
arguments:
  test_scope: "[full-platform|workflow-focus|service-integration|performance-focus|user-journey|all-scenarios]"
  environment_target: "[local|development|staging|production|multi-environment|all-environments]"
  service_coverage: "[all-services|core-services|specific-services|integration-focus|performance-critical]"
  complexity_level: "[optional: basic|standard|comprehensive|enterprise]"
  performance_requirements: "[optional: baseline, performance SLA requirements]"
  compliance_validation: "[optional: security, regulatory compliance requirements]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All testing phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive end-to-end testing completed across all targeted services
- [ ] All service integrations validated and documented (timestamped)
- [ ] Complete user workflows tested with validation matrices (timestamped)
- [ ] Performance benchmarks executed and analyzed (timestamped)
- [ ] Failure recovery scenarios tested and validated (timestamped)
- [ ] Security and compliance testing completed (timestamped)
- [ ] Monitoring and observability validation performed (timestamped)
- [ ] Data flow consistency verified across all services (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL TEST EXECUTION OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All test execution deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All test result documentation includes precise timestamps
- [ ] All service validation reports include timestamp documentation
- [ ] All performance benchmark reports include proper date stamps
- [ ] All security testing follows consistent date stamp format
- [ ] All monitoring validation documentation includes timestamps
- [ ] All user journey testing includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating test execution files without proper reverse date stamps
- Using inconsistent date formats within same testing session
- Missing timestamps in test result documentation

### **TEST EXECUTION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After test execution completion, analyze results with:
/test-execution-analysis [test-scope] [environment] [additional-options]

# Examples:
/test-execution-analysis full-platform local
/test-execution-analysis workflow-focus staging
/test-execution-analysis performance-focus production
```

---

**ENFORCEMENT:** This command performs END-TO-END TESTING EXECUTION ONLY through the MCP prompt protocol. The comprehensive testing logic is defined in `test-end-to-end-prompt.yaml` and executed according to Model Context Protocol standards. No actual system changes or deployments are performed. Use `/test-analysis` for result analysis after testing is complete.

model_context:
role: "AI-driven end-to-end testing specialist for complete multi-service workflow validation"
domain: "End-to-End Testing, Service Integration, Workflow Validation, Data Flow Testing, System Reliability"
goal: >
Execute comprehensive end-to-end testing across all 10 services in the n8n IaC platform.
MANDATORY validation of complete user workflows from initial interaction through all backend
services to final visualization. Generate detailed E2E test reports using Jupyter Notebook
format with complete service interaction matrices and integration certification.

configuration:

# E2E test scope - MANDATORY EXHAUSTIVE COVERAGE

e2e_test_scope:
all_services_tested: true # MUST test all 10 services
complete_workflows: true # MUST validate entire workflows
data_flow_validation: true # MUST track data through all services
service_integration: true # MUST test all service interactions
user_journey_testing: true # MUST validate user scenarios
performance_benchmarking: true # MUST benchmark complete workflows
failure_recovery: true # MUST test failure scenarios
monitoring_validation: true # MUST validate observability

# Service coverage - ALL 10 SERVICES MANDATORY

service_requirements:
n8n_orchestration: true # Workflow creation and execution
postgresql_persistence: true # Data and state persistence
neo4j_graph: true # Knowledge graph operations
qdrant_vectors: true # Vector storage and search
lightrag_processing: true # RAG pipeline operations
minio_storage: true # Artifact and file storage
terraform_executor: true # Infrastructure automation
ansible_executor: true # Configuration automation
prometheus_metrics: true # Metrics collection
grafana_visualization: true # Dashboard and visualization

# Integration validation requirements

integration_requirements:
service_to_service: true # MANDATORY: All service pairs
data_consistency: true # MANDATORY: Cross-service data validation
transaction_integrity: true # MANDATORY: ACID compliance
event_propagation: true # MANDATORY: Event flow validation
error_handling: true # MANDATORY: Error propagation
performance_impact: true # MANDATORY: Integration overhead
security_boundaries: true # MANDATORY: Security validation

# MCP tool integration

mcp_tool_usage:
neo4j_memory_tracking: true # MANDATORY: Track E2E test progress
sequential_thinking: true # MANDATORY: Structure E2E approach
playwright_ui_testing: true # MANDATORY: Test n8n UI workflows
context7_research: true # MANDATORY: Research best practices
grep_examples: true # MANDATORY: Find E2E patterns
fetch_api_testing: true # MANDATORY: Test service APIs
filesystem_validation: true # MANDATORY: Validate file operations
time_performance: true # MANDATORY: Track timing metrics

instructions:

- Phase 1: E2E Test Environment Setup and Validation

  - MANDATORY: Complete environment preparation:
    - Service dependency validation:
      - Verify ALL 10 services are operational
      - Check ALL service health endpoints
      - Validate ALL inter-service connectivity
      - Test ALL API endpoints availability
      - Confirm ALL database connections
      - DOUBLE-CHECK: No service degradation
    - Test data preparation:
      - Create comprehensive test datasets
      - Generate workflow templates
      - Prepare document samples for RAG
      - Create infrastructure templates
      - Setup monitoring dashboards
      - MANDATORY: Cover all test scenarios
    - Network and security validation:
      - Verify service mesh connectivity
      - Test authentication mechanisms
      - Validate authorization flows
      - Check encryption in transit
      - Verify data isolation
      - FORBIDDEN: Security vulnerabilities
  - E2E test orchestration setup:
    - Test workflow design:
      - Design complete user journeys
      - Map service interaction flows
      - Plan data validation checkpoints
      - Define performance benchmarks
      - Create failure injection points
      - MANDATORY: Complete test coverage

- Phase 2: Workflow Orchestration E2E Testing

  - MANDATORY: Complete workflow validation:
    - n8n workflow lifecycle testing:
      - Create workflows via UI and API
      - Execute workflows with various triggers
      - Validate workflow state in PostgreSQL
      - Test workflow versioning and rollback
      - Verify execution history tracking
      - MANDATORY: All workflow operations tested
    - Data persistence validation:
      - Verify workflow data in PostgreSQL
      - Check execution logs persistence
      - Validate credential storage
      - Test backup and recovery
      - Verify data consistency
      - DOUBLE-CHECK: No data loss scenarios
    - Knowledge graph integration:
      - Test workflow-to-graph mapping
      - Validate entity creation in Neo4j
      - Check relationship generation
      - Test graph traversal queries
      - Verify knowledge extraction
      - FORBIDDEN: Orphaned graph nodes

- Phase 3: RAG Pipeline End-to-End Testing

  - MANDATORY: Complete RAG pipeline validation:
    - Document processing workflow:
      - Upload documents via n8n workflow
      - Verify storage in MinIO S3
      - Test LightRAG processing pipeline
      - Validate chunk generation
      - Check metadata extraction
      - MANDATORY: Complete document lifecycle
    - Vector embedding validation:
      - Test embedding generation
      - Verify vector storage in Qdrant
      - Validate similarity search
      - Test vector indexing performance
      - Check retrieval accuracy
      - DOUBLE-CHECK: Embedding quality metrics
    - Knowledge enrichment testing:
      - Test entity extraction to Neo4j
      - Validate relationship discovery
      - Check knowledge graph updates
      - Test context retrieval
      - Verify RAG query responses
      - FORBIDDEN: Hallucinated responses

- Phase 4: Infrastructure Automation E2E Testing

  - MANDATORY: Complete IaC validation:
    - Terraform execution workflow:
      - Test infrastructure requests via n8n
      - Validate Terraform plan generation
      - Execute infrastructure provisioning
      - Verify state management
      - Test rollback procedures
      - MANDATORY: Infrastructure lifecycle tested
    - Ansible configuration testing:
      - Test playbook execution via workflow
      - Validate configuration management
      - Check inventory updates
      - Test role application
      - Verify idempotency
      - DOUBLE-CHECK: Configuration consistency
    - Multi-cloud deployment validation:
      - Test Azure deployments
      - Validate AWS provisioning (when implemented)
      - Check GCP resources (when implemented)
      - Test cross-cloud networking
      - Verify cloud-agnostic operations
      - FORBIDDEN: Cloud vendor lock-in

- Phase 5: Data Flow and Integration Testing

  - MANDATORY: Complete data flow validation:
    - Cross-service data consistency:
      - Track data through all services
      - Validate data transformations
      - Check data integrity at each step
      - Test transaction boundaries
      - Verify eventual consistency
      - MANDATORY: 100% data integrity
    - Event propagation testing:
      - Test webhook event flow
      - Validate message passing
      - Check event ordering
      - Test error propagation
      - Verify retry mechanisms
      - DOUBLE-CHECK: No event loss
    - Performance impact analysis:
      - Measure end-to-end latency
      - Test throughput limits
      - Validate resource utilization
      - Check bottleneck identification
      - Test scaling behaviors
      - FORBIDDEN: Performance regression

- Phase 6: Monitoring and Observability E2E Testing

  - MANDATORY: Complete observability validation:
    - Metrics collection validation:
      - Test Prometheus metric scraping
      - Validate custom metric generation
      - Check metric aggregation
      - Test alert rule evaluation
      - Verify metric persistence
      - MANDATORY: All metrics collected
    - Dashboard and visualization testing:
      - Test Grafana dashboard updates
      - Validate real-time visualization
      - Check dashboard performance
      - Test drill-down capabilities
      - Verify cross-dashboard linking
      - DOUBLE-CHECK: Accurate visualizations
    - Distributed tracing validation:
      - Test trace generation
      - Validate trace correlation
      - Check span relationships
      - Test trace sampling
      - Verify trace persistence
      - FORBIDDEN: Missing trace data

- Phase 7: Failure Recovery and Resilience Testing

  - MANDATORY: Complete resilience validation:
    - Service failure scenarios:
      - Test individual service failures
      - Validate failover mechanisms
      - Check circuit breaker behavior
      - Test recovery procedures
      - Verify data consistency post-recovery
      - MANDATORY: Graceful degradation
    - Network partition testing:
      - Simulate network splits
      - Test partition tolerance
      - Validate CAP theorem handling
      - Check reconciliation procedures
      - Verify split-brain prevention
      - DOUBLE-CHECK: Data consistency maintained
    - Cascade failure prevention:
      - Test failure isolation
      - Validate bulkhead patterns
      - Check timeout configurations
      - Test retry strategies
      - Verify backpressure handling
      - FORBIDDEN: Cascade failures

- Phase 8: User Journey and Experience Validation
  - MANDATORY: Complete user journey testing:
    - Business user workflows:
      - Test no-code workflow creation
      - Validate drag-and-drop interface
      - Check template usage
      - Test workflow sharing
      - Verify collaboration features
      - MANDATORY: User-friendly experience
    - Developer workflows:
      - Test API integration
      - Validate webhook handling
      - Check custom node creation
      - Test debugging capabilities
      - Verify version control integration
      - DOUBLE-CHECK: Developer productivity
    - Operations workflows:
      - Test infrastructure provisioning
      - Validate monitoring setup
      - Check alert configuration
      - Test backup procedures
      - Verify disaster recovery
      - FORBIDDEN: Operational blind spots

e2e_test_matrices:
service_integration_matrix: |
| Service A | Service B | Integration | Status | Latency | Data Flow | Issues |
|-----------|-----------|-------------|--------|---------|-----------|--------|
| n8n | PostgreSQL | State Persistence | ✓ | 45ms | Bidirectional | None |
| n8n | Neo4j | Knowledge Creation | ✓ | 120ms | Unidirectional | None |
| n8n | MinIO | File Storage | ✓ | 200ms | Bidirectional | None |
| LightRAG | Qdrant | Vector Storage | ✓ | 85ms | Bidirectional | None |
| All | Prometheus | Metrics | ✓ | 10ms | Unidirectional | None |

workflow_validation_matrix: |
| Workflow Type | Services Used | Execution Time | Data Processed | Status | Performance |
|---------------|---------------|----------------|----------------|--------|-------------|
| RAG Pipeline | 6 services | 4.2s | 100 documents | Pass | Optimal |
| IaC Deployment | 4 services | 45s | 5 resources | Pass | Acceptable |
| Data Integration | 8 services | 8.5s | 1000 records | Pass | Optimal |

user_journey_matrix: |
| Journey | Persona | Steps | Services | Duration | Success Rate | Issues |
|---------|---------|-------|----------|----------|--------------|--------|
| Create Automation | Business User | 5 | 3 | 2m 30s | 100% | None |
| Deploy Infrastructure | DevOps | 8 | 5 | 10m | 95% | Minor |
| Setup Monitoring | SRE | 6 | 4 | 5m | 100% | None |

data_consistency_matrix: |
| Data Type | Source | Destinations | Consistency Model | Validation | Status |
|-----------|--------|--------------|-------------------|------------|--------|
| Workflow State | n8n | PostgreSQL, Neo4j | Strong | Checksum | Valid |
| Embeddings | LightRAG | Qdrant | Eventual | Similarity | Valid |
| Metrics | All | Prometheus | Eventual | Timestamp | Valid |
| Files | n8n | MinIO | Strong | MD5 | Valid |

constraints:

- MANDATORY: ALL 10 services MUST be tested end-to-end
- MANDATORY: ALL service integrations MUST be validated
- MANDATORY: ALL user workflows MUST complete successfully
- MANDATORY: ALL data flows MUST maintain consistency
- MANDATORY: ALL performance benchmarks MUST be met
- MANDATORY: ALL failure scenarios MUST be tested
- MANDATORY: Documentation in markdown documents
- FORBIDDEN: Testing with mocked services
- FORBIDDEN: Incomplete workflow validation
- FORBIDDEN: Skipping service integration tests
- FORBIDDEN: Ignoring data consistency checks
- FORBIDDEN: Proceeding with degraded services

output_format:
jupyter_structure: - "01_E2E_Test_Overview.ipynb": - Test scope and objectives - Service architecture validation - Test environment status - Dependency verification - Test data preparation

    - "02_Workflow_Orchestration_Tests.ipynb":
        - n8n workflow lifecycle tests
        - PostgreSQL persistence validation
        - Neo4j knowledge graph tests
        - Workflow execution metrics
        - State management validation

    - "03_RAG_Pipeline_Tests.ipynb":
        - Document processing workflow
        - Vector embedding validation
        - Knowledge extraction tests
        - Similarity search validation
        - RAG query performance

    - "04_Infrastructure_Automation_Tests.ipynb":
        - Terraform execution tests
        - Ansible configuration validation
        - Multi-cloud deployment tests
        - Infrastructure state validation
        - Rollback procedure tests

    - "05_Data_Integration_Tests.ipynb":
        - Cross-service data flow
        - Data consistency validation
        - Transaction integrity tests
        - Event propagation validation
        - Performance impact analysis

    - "06_Monitoring_Observability_Tests.ipynb":
        - Metrics collection validation
        - Dashboard functionality tests
        - Alert rule validation
        - Distributed tracing tests
        - Observability coverage

    - "07_Resilience_Recovery_Tests.ipynb":
        - Service failure scenarios
        - Network partition tests
        - Recovery procedure validation
        - Data consistency recovery
        - Cascade failure prevention

    - "08_User_Journey_Validation.ipynb":
        - Business user workflows
        - Developer experience tests
        - Operations procedures
        - Collaboration features
        - User satisfaction metrics

    - "09_Performance_Benchmarks.ipynb":
        - End-to-end latency analysis
        - Throughput testing results
        - Resource utilization metrics
        - Bottleneck identification
        - Optimization recommendations

    - "10_E2E_Test_Certification.ipynb":
        - Overall test results summary
        - Service integration certification
        - Data consistency certification
        - Performance certification
        - Production readiness assessment

validation_criteria:
service_integration: "MANDATORY - All 10 services fully integrated"
workflow_completion: "MANDATORY - All workflows execute successfully"
data_consistency: "MANDATORY - 100% data consistency maintained"
performance_benchmarks: "MANDATORY - All benchmarks achieved"
failure_recovery: "MANDATORY - All failure scenarios handled"
user_experience: "MANDATORY - All user journeys successful"
monitoring_coverage: "MANDATORY - Complete observability achieved"

final_deliverables:

- E2E_Test_Complete_Report.ipynb (comprehensive results)
- Service_Integration_Matrix.xlsx (integration tracking)
- User_Journey_Validation.ipynb (user experience results)
- Performance_Benchmark_Report.ipynb (performance analysis)
- Data_Consistency_Report.ipynb (data validation)
- Resilience_Test_Report.ipynb (failure recovery)
- E2E_Test_Certification.pdf (production readiness)

# Execution Command

usage: |
test-end-to-end # Execute complete E2E test suite
test-end-to-end "workflow tests" # Test workflow orchestration
test-end-to-end "rag pipeline" # Test RAG pipeline E2E
test-end-to-end "infrastructure" # Test IaC automation E2E

execution_protocol: |
MANDATORY REQUIREMENTS:

- MUST test ALL 10 services end-to-end
- MUST validate ALL service integrations
- MUST track data through entire pipeline
- MUST verify ALL user workflows
- MUST benchmark complete operations
- MUST test failure recovery scenarios
- MUST document ALL test results
- MUST use MCP tools for automation
- MUST use sub-agents for execution

STRICTLY FORBIDDEN:

- NO testing with mocked services
- NO incomplete service coverage
- NO skipping integration tests
- NO ignoring data consistency
- NO incomplete user journeys
- NO missing performance metrics
- NO untested failure scenarios
- NO superficial testing

MCP TOOL REQUIREMENTS:

- USE memory to track E2E test progress
- USE sequential-thinking for test orchestration
- USE playwright for UI workflow testing
- USE context7 for best practices research
- USE grep for finding E2E test patterns
- USE fetch for API endpoint testing
- USE filesystem for file operation validation
- USE time for performance benchmarking

SUB-AGENT EXECUTION:

- ALL service tests via sub-agents
- ALL workflow validation via sub-agents
- ALL data validation via sub-agents
- ALL performance tests via sub-agents
- ALL documentation via sub-agents

REAL-TIME REQUIREMENTS:

- MUST monitor all services during testing
- MUST track data flow in real-time
- MUST detect issues immediately
- MUST update test matrices continuously
- MUST provide live test status

---
