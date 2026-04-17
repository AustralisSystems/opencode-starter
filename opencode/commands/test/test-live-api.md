# === Universal Code Live API Testing: AI-Driven Production Testing Protocol ===

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

### **LIVE-API-TESTING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR LIVE API TESTING EXECUTION ONLY:**

- **MUST:** Execute comprehensive live API testing against production endpoints
- **MUST:** Validate real API responses and system behavior
- **MUST:** Test complete user workflows and API integration chains
- **MUST:** Generate detailed API testing reports with evidence collection
- **FORBIDDEN:** Execute ANY actual deployment or system changes
- **FORBIDDEN:** Modify ANY production systems or configurations
- **FORBIDDEN:** Create ANY new API endpoints or services
- **MUST:** Output test results in markdown documents with timestamp tracking

**API TESTING FOCUS AREAS:**

- Live production API endpoint validation
- End-to-end workflow testing across API chains
- Performance benchmarking and load testing
- Security boundary and authentication testing
- Integration testing between services
- Error handling and recovery validation
- Data consistency and state management testing

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-live-api-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for api_scope, environment_target, testing_focus
3. **FOLLOW PROTOCOL**: Execute all phases according to the API testing protocol specifications
4. **VERIFY COMPLETION**: Ensure all API testing objectives and validation criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive API testing reports with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% API testing coverage and validation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-live-api-prompt"
arguments:
  api_scope: "[all-apis|core-apis|specific-endpoints|integration-focus|performance-critical|security-focus]"
  environment_target: "[local|development|staging|production|multi-environment|all-environments]"
  testing_focus: "[functional|performance|security|integration|end-to-end|comprehensive]"
  complexity_level: "[optional: basic|standard|comprehensive|enterprise]"
  performance_requirements: "[optional: baseline, performance SLA requirements]"
  security_validation: "[optional: authentication, authorization, security compliance]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All API testing phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive live API testing completed across all targeted endpoints
- [ ] All API integrations validated and documented (timestamped)
- [ ] Complete API workflows tested with validation matrices (timestamped)
- [ ] Performance benchmarks executed and analyzed (timestamped)
- [ ] Security testing completed with vulnerability assessment (timestamped)
- [ ] Error handling and recovery scenarios tested (timestamped)
- [ ] Data consistency validated across API operations (timestamped)
- [ ] User journey API workflows validated (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL API TESTING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All API testing deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All API test result documentation includes precise timestamps
- [ ] All endpoint validation reports include timestamp documentation
- [ ] All performance benchmark reports include proper date stamps
- [ ] All security testing follows consistent date stamp format
- [ ] All integration testing documentation includes timestamps
- [ ] All workflow testing includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating API testing files without proper reverse date stamps
- Using inconsistent date formats within same testing session
- Missing timestamps in API test result documentation

### **API TESTING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After API testing completion, analyze results with:
/test-api-analysis [api-scope] [environment] [additional-options]

# Examples:
/test-api-analysis all-apis production
/test-api-analysis core-apis staging
/test-api-analysis performance-critical local
```

---

**ENFORCEMENT:** This command performs LIVE API TESTING EXECUTION ONLY through the MCP prompt protocol. The comprehensive API testing logic is defined in `test-live-api-prompt.yaml` and executed according to Model Context Protocol standards. No actual system changes or deployments are performed. Use `/test-api-analysis` for result analysis after testing is complete.

model_context:
role: "AI-driven live API testing specialist for production environment validation"
domain: "Multi-platform, API Testing, Live Systems, Integration Testing, Performance Monitoring"
goal: >
Execute comprehensive live testing of all REST API endpoints in production environments.
Discover and document all APIs, create detailed test plans, execute real tests against
live endpoints, monitor system behavior, and generate comprehensive test reports using
Jupyter Notebook format with evidence, logs, performance metrics, and business logic
documentation including Mermaid diagrams.

configuration:

# Testing scope

test_environment:
environment_type: "PRODUCTION" # Live production testing
test_mode: "REAL" # No mocks, stubs, or fakes
safety_checks: true # Prevent destructive operations
rate_limiting: true # Respect API rate limits
monitoring_enabled: true # Full system monitoring

# Discovery configuration

discovery_scope:
api_endpoints: true # REST API endpoints
graphql_endpoints: true # GraphQL schemas
websocket_endpoints: true # WebSocket connections
grpc_services: true # gRPC service definitions
internal_apis: true # Internal service APIs
third_party_apis: true # External integrations
health_endpoints: true # Health check APIs
admin_endpoints: true # Administrative APIs

# Test configuration

test_configuration:
functional_testing: true # API functionality
integration_testing: true # Cross-service flows
end_to_end_workflow_testing: true # MANDATORY - Complete user journeys
performance_testing: true # Response times, throughput
security_testing: true # Auth, permissions, vulnerabilities
error_handling_testing: true # Error scenarios
boundary_testing: true # Edge cases, limits
concurrent_testing: true # Parallel requests
data_validation_testing: true # Input/output validation

## MANDATORY END-TO-END WORKFLOW TESTING REQUIREMENTS

**CRITICAL PROTOCOL CHANGE**: End-to-End Workflow Testing is now MANDATORY for all API testing.

### Why E2E Workflow Testing is Critical

**Individual endpoint testing alone is INSUFFICIENT** because:

- APIs work in isolation but fail in business workflows
- State management issues only appear across multiple operations
- Session handling problems emerge during complete user journeys
- Business logic gaps manifest in end-to-end scenarios
- Performance degradation compounds over workflow sequences
- Security vulnerabilities appear in workflow transitions

### Mandatory E2E Workflow Categories

**CATEGORY 1: User Journey Workflows**

```
New User Complete Journey:
Registration → Email verification → First login → Profile setup →
First data operation → Data management → Feature usage → Account settings → Logout

Returning User Journey:
Login → Dashboard access → Data operations → Collaboration →
File management → Settings update → Session management → Logout

Power User Journey:
Login → Advanced features → Bulk operations → API integrations →
Admin functions → System monitoring → Configuration → Logout
```

**CATEGORY 2: Data Lifecycle Workflows**

```
Complete Data Management:
Create resource → Validate creation → Modify resource →
Share/collaborate → Version control → Archive → Delete → Verify cleanup

Bulk Operations Workflow:
Bulk create → Validation → Bulk modify → Error handling →
Recovery → Completion verification → Audit trail check
```

**CATEGORY 3: Error Recovery Workflows**

```
Failure Recovery Journey:
Normal operation → Induced failure → Error detection →
User notification → Retry mechanism → Success validation → Audit logging

Authentication Expiry Workflow:
Long operation start → Token near expiry → Automatic refresh →
Operation continuation → Completion → Session validation
```

**CATEGORY 4: Multi-User Collaboration Workflows**

```
Collaboration Workflow:
User A creates resource → User B gains access → Concurrent modifications →
Conflict detection → Resolution mechanism → State synchronization → Audit trail

Permission Management Workflow:
Admin grants permissions → User accesses resource → Permission change →
Access re-validation → Operation authorization → Audit logging
```

### E2E Testing Success Criteria

- **State Consistency**: Data remains consistent throughout complete workflows
- **Session Integrity**: User sessions maintained properly across all operations
- **Business Rules**: All business logic enforced throughout journeys
- **Performance**: Complete workflows meet acceptable time limits
- **Error Handling**: Graceful failure and recovery at any workflow step
- **Security**: Authentication and authorization maintained throughout
- **Audit Trail**: Complete workflow tracking and logging
- **User Experience**: Workflows provide acceptable user experience

### E2E Testing Failure Conditions

- ANY step in workflow fails
- Data inconsistency detected at any point
- Session management fails during workflow
- Business rules bypassed or violated
- Performance degradation beyond acceptable limits
- Security breach at any workflow step
- Missing or incomplete audit trail
- Poor user experience due to workflow friction

instructions:

- Phase 1: System Discovery and Documentation

  - Infrastructure discovery:

    - Application inventory:
      - List all applications with versions
      - Document deployment locations
      - Identify application dependencies
      - Map application architectures
      - Document configuration details
    - Service inventory:
      - Enumerate all services
      - Document service types
      - Map service dependencies
      - Identify service contracts
      - Document SLA requirements
    - Container inventory:
      - List all running containers
      - Document container images
      - Map container networking
      - Identify resource allocations
      - Document orchestration details
    - Data systems inventory:
      - List all databases
      - Document data schemas
      - Map data relationships
      - Identify data flows
      - Document backup strategies
    - Network infrastructure:
      - Document network topology
      - List load balancers
      - Map API gateways
      - Identify firewalls
      - Document DNS entries
    - Monitoring systems:
      - List monitoring tools
      - Document metric collection
      - Map alerting rules
      - Identify log aggregation
      - Document dashboards

  - API discovery and documentation:
    - Production codebase APIs:
      - Scan codebase for API definitions
      - Extract OpenAPI/Swagger specs
      - Document API versions
      - Map API dependencies
      - Identify authentication methods
    - Service-specific APIs:
      - For each application/service:
        - List all API endpoints
        - Document request methods
        - Extract parameter schemas
        - Document response formats
        - Identify error codes
    - Infrastructure APIs:
      - Container orchestration APIs
      - Monitoring system APIs
      - Database admin APIs
      - Network management APIs
      - Security service APIs

- Phase 2: Test Plan Preparation

  - For each discovered API endpoint:
    - Test case design:
      - Test case ID and name
      - API endpoint details
      - Test objectives
      - Test prerequisites
      - Test data requirements
    - Test scenarios:
      - Happy path testing:
        - Valid inputs
        - Expected outputs
        - Success criteria
      - Error path testing:
        - Invalid inputs
        - Error handling
        - Recovery behavior
      - Boundary testing:
        - Minimum values
        - Maximum values
        - Edge cases
      - Security testing:
        - Authentication tests
        - Authorization tests
        - Injection attempts
      - Performance testing:
        - Response time targets
        - Throughput limits
        - Concurrent user loads
    - Test execution plan:
      - Execution sequence
      - Dependencies between tests
      - Rate limiting considerations
      - Rollback procedures
      - Monitoring requirements

- Phase 3: Test Execution and Evidence Collection

  - Pre-test preparation:

    - System health check:
      - Verify all services running
      - Check resource availability
      - Confirm monitoring active
      - Validate test environment
      - Create baseline metrics
    - Test data setup:
      - Generate test data
      - Configure test accounts
      - Set up test scenarios
      - Prepare cleanup scripts
      - Document initial state

  - Test execution process (MANDATORY PHASES):

    **PHASE 3A: Individual Endpoint Testing**

    - For each API endpoint individually:
      - Execute isolated endpoint tests:
        - Prepare request data
        - Execute API call
        - Capture response
        - Validate results
        - Record timings
      - Evidence collection:
        - Request details (headers, body)
        - Response details (status, headers, body)
        - Response time metrics
        - System resource usage
        - Error messages
      - Log collection:
        - Application logs
        - Container logs
        - Service logs
        - System logs
        - Security logs
      - Performance monitoring:
        - CPU utilization
        - Memory usage
        - Network traffic
        - Database queries
        - Cache performance
      - Test result recording:
        - Pass/fail status
        - Actual vs. expected
        - Deviations noted
        - Issues discovered
        - Follow-up required

    **PHASE 3B: End-to-End Workflow Testing (MANDATORY)**

    - Complete business workflow validation:
      - User journey workflows:
        - New user registration → Profile setup → First operation → Data management → Account cleanup
        - Returning user login → Data operations → Collaboration → Session management → Logout
        - Admin operations → User management → System monitoring → Configuration changes
      - Data lifecycle workflows:
        - Create resource → Modify resource → Share/collaborate → Archive → Delete → Verify cleanup
        - Bulk operations → Validation → Error handling → Recovery → Completion
      - Error recovery workflows:
        - Failed operation → Error detection → User notification → Retry mechanism → Success validation
        - Authentication expiry → Token refresh → Operation continuation → Completion
      - Multi-user collaboration workflows:
        - User A creates resource → User B accesses → Concurrent modifications → Conflict resolution
        - Permission changes → Access validation → Operation authorization → Audit trail
      - State consistency validation:
        - Verify data consistency across all workflow steps
        - Validate session state maintenance
        - Confirm business rule enforcement
        - Check audit trail completeness
      - Performance validation:
        - Measure complete workflow duration
        - Identify bottlenecks in user journeys
        - Validate acceptable user experience
        - Monitor resource usage during workflows

    **PHASE 3C: Integration Testing (Service-to-Service)**

    - Cross-service communication validation:
      - API Gateway → Authentication Service integration
      - Data Service → Database → Cache integration
      - MCP Server → External Service integration
      - Monitoring → Alerting → Notification integration
    - Failure scenario testing:
      - Service dependency failures
      - Circuit breaker activation
      - Failover mechanisms
      - Recovery procedures

- Phase 4: System Behavior Analysis

  - Performance impact analysis:
    - Response time analysis:
      - Baseline comparison
      - Percentile distribution
      - Outlier identification
      - Trend analysis
      - SLA compliance
    - Resource utilization:
      - CPU impact
      - Memory consumption
      - I/O patterns
      - Network usage
      - Database load
  - System stability:
    - Error rate changes
    - Service degradation
    - Recovery behavior
    - Cascade effects
    - Circuit breaker triggers
  - Integration behavior:
    - Cross-service impacts
    - Data consistency
    - Transaction integrity
    - Event propagation
    - Cache coherence

- Phase 5: Test Results Compilation
  - Test summary generation:
    - Overall pass/fail rates
    - Category-wise results
    - Critical findings
    - Performance metrics
    - Security issues
  - Evidence compilation:
    - Request/response pairs
    - Log excerpts
    - Performance graphs
    - Error traces
    - System metrics
  - Business logic documentation:
    - API workflow diagrams
    - Data flow representations
    - Integration patterns
    - Error handling flows
    - Security boundaries

test_plan_template:

# Template for each API test

api_test_specification:
test_id: "TEST-API-{category}-{number}"
api_details:
endpoint: "Full URL path"
method: "GET|POST|PUT|DELETE|PATCH"
authentication: "Type and requirements"
rate_limits: "Requests per minute"

    test_description:
      objective: "What this test validates"
      business_logic: "Business process tested"
      dependencies: "Required preconditions"

    test_steps:
      - step: 1
        action: "Specific action"
        data: "Input data"
        validation: "What to check"

    expected_results:
      response_code: "Expected HTTP status"
      response_body: "Expected structure/values"
      response_time: "Maximum acceptable time"
      side_effects: "Expected system changes"

    actual_results:
      response_code: "Actual HTTP status"
      response_body: "Actual response"
      response_time: "Measured time"
      side_effects: "Observed changes"

    test_verdict:
      status: "PASS|FAIL|PARTIAL"
      issues: "List of problems"
      impact: "Business impact"

evidence_collection:

# Evidence to collect for each test

request_evidence: - Full URL with parameters - Request headers - Request body - Authentication tokens - Timestamp

response_evidence: - Response status code - Response headers - Response body - Response time - Response size

system_evidence: - Application logs (with correlation ID) - Container logs - Service mesh traces - Database query logs - Performance metrics

monitoring_evidence: - CPU usage during test - Memory consumption - Network throughput - Error rates - Active connections

constraints:

- Tests MUST NOT corrupt production data
- Tests MUST respect rate limits
- Tests MUST NOT cause service disruption
- Tests MUST capture all evidence
- Tests MUST be repeatable
- Tests MUST document all findings
- Tests MUST include rollback procedures

output_format:
jupyter_structure: - Section 1: Executive Test Summary - Section 2: System Inventory Documentation - Section 3: API Discovery Results - Section 4: Test Plan Overview - Section 5: Individual Endpoint Test Results - Section 6: End-to-End Workflow Test Results (MANDATORY) - Section 7: Integration Test Results (Service-to-Service) - Section 8: Performance Test Results - Section 9: Security Test Results - Section 10: Error Handling Test Results - Section 11: System Behavior Analysis - Section 12: Evidence Collection - Section 13: Log Analysis - Section 14: Performance Impact Assessment - Section 15: Workflow Analysis and User Journey Validation - Section 16: Issues and Findings - Section 17: Business Logic Diagrams - Section 18: Recommendations - Section 19: Test Artifacts Archive

test_result_format: |
For each API test:

````
Test ID: <TEST-API-XXX-001>
Endpoint: [Full API URL]
Method: [HTTP Method]
Test Type: Functional|Integration|Performance|Security

    Test Description:
      Objective: [What is being tested]
      Business Logic: [Business process validated]

    Test Execution:
      Start Time: [Timestamp]
      End Time: [Timestamp]
      Duration: [Milliseconds]

    Request Details:
      Headers: [Key headers]
      Body: [Request payload]

    Response Details:
      Status Code: [HTTP status]
      Headers: [Response headers]
      Body: [Response payload]
      Response Time: [Milliseconds]

    Expected vs Actual:
      Expected: [What should happen]
      Actual: [What actually happened]
      Match: YES|NO|PARTIAL

    System Behavior:
      CPU Impact: [% increase]
      Memory Impact: [MB consumed]
      Database Queries: [Count and duration]

    Logs Collected:
      Application: [Log excerpts]
      Container: [Relevant entries]

    Test Result: PASS|FAIL

    Issues Found:
      - Issue 1: [Description]
      - Issue 2: [Description]

    Evidence Links:
      - Request capture: [Link]
      - Response capture: [Link]
      - Performance graph: [Link]
    ```

mermaid_diagram_format: |
Business Logic Flow:
`mermaid
    flowchart TD
      A[Client Request] --> B[API Gateway]
      B --> C{Authentication}
      C -->|Valid| D[Service Logic]
      C -->|Invalid| E[401 Error]
      D --> F[Database Query]
      F --> G[Response Formation]
      G --> H[Client Response]
    `

    Test Execution Flow:
    ```mermaid
    sequenceDiagram
      participant Test as Test Runner
      participant API as API Endpoint
      participant DB as Database
      participant Log as Logging System

      Test->>API: HTTP Request
      API->>Log: Log Request
      API->>DB: Query Data
      DB-->>API: Return Data
      API-->>Test: HTTP Response
      API->>Log: Log Response
    ```

validation_criteria:
test_coverage: "10 - All APIs tested comprehensively"
evidence_quality: "10 - Complete evidence captured"
documentation_completeness: "10 - Full documentation"
test_reliability: "10 - Consistent, repeatable results"
system_safety: "10 - No production impact"
finding_accuracy: "10 - All issues identified"
performance_monitoring: "10 - Complete metrics captured"

final_deliverables:

- Live_API_Test_Report.ipynb (comprehensive test results)
- API_Inventory.xlsx (all discovered APIs)
- Test_Plan_Document.md (detailed test plans)
- Test_Evidence_Archive.zip (all captured evidence)
- Performance_Impact_Report.pdf (system behavior)
- Security_Findings.md (security issues found)
- Integration_Test_Results.md (cross-service tests)
- Business_Logic_Diagrams.md (Mermaid diagrams)
- Issue_Tracker.csv (all findings with priority)
- Executive_Summary.pdf (key results and risks)

# Test Safety Framework

safety_measures:
pre_test_checks: - Verify non-destructive operations - Check rate limit compliance - Validate test data isolation - Confirm rollback procedures - Alert operations team

during_test_monitoring: - Watch error rates - Monitor system health - Check resource usage - Verify data integrity - Track user impact

post_test_validation: - Confirm system stability - Verify data consistency - Check no side effects - Validate cleanup complete - Document any issues

# Test Prioritization

test_priorities:
critical: # Must test - Authentication/authorization - Core business functions - Payment processing - Data integrity operations

high: # Should test - User-facing features - Integration points - Performance-critical paths - Error handling

medium: # Good to test - Administrative functions - Reporting features - Background processes - Utility endpoints

low: # Optional - Deprecated endpoints - Rarely used features - Internal tools - Debug endpoints

# Execution Workflow

execution_steps: |

1. Discover and document all system components
2. Identify and catalog all API endpoints
3. Create comprehensive test plans
4. Create end-to-end workflow test plans (complete user journeys)
5. Establish baseline system metrics
6. Execute individual endpoint tests with evidence collection
7. Execute end-to-end workflow tests (MANDATORY)
8. Execute integration tests (service-to-service)
9. Monitor system behavior during all test phases
10. Collect and analyze all logs
11. Document test results and findings
12. Create business logic diagrams
13. Generate comprehensive test report

constraints:

- NO mock implementations allowed - production code only
- NO stub services permitted - real integrations only
- NO demo data allowed - realistic test data only
- NO simplified tests - comprehensive validation only
- ALL tests must have debug logging enabled
- ALL results must be documented in markdown documents
- ALL test artifacts must be in dedicated test directory
- NO markdown documentation outside of code blocks
- MANDATORY: Test existing production code only
- MANDATORY: NEVER create duplicate files or copies
- FORBIDDEN: Creating duplicate test files
- FORBIDDEN: Making backup copies of code
- FORBIDDEN: Creating alternative test implementations
- FORBIDDEN: Test file copies like api_test_v2.py

validation_criteria:
api_completeness: "100% of production endpoints tested individually"
workflow_completeness: "100% of critical user journeys tested end-to-end"
integration_completeness: "100% of service dependencies validated"
spec_accuracy: "100% alignment between code and specification"
test_coverage: "100% of documented APIs have individual AND workflow tests"
performance_compliance: "All endpoints and workflows meet SLA targets"
security_validation: "All security requirements verified in isolation AND workflows"
error_handling: "All error scenarios properly handled in endpoints AND workflows"
data_integrity: "All CRUD operations maintain consistency in isolation AND workflows"
business_logic_validation: "All business rules enforced throughout complete workflows"
state_consistency: "System state remains consistent throughout all user journeys"
user_experience_validation: "All workflows provide acceptable user experience"
````
