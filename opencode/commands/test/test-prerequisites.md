# === Universal Test Prerequisites: AI-Driven Test Environment Setup and Validation Protocol ===

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
3. **READ AND INDEX**: `.claude/commands/test/test-protocol-prerequisites.md`
4. **VERIFY**: User has given explicit permission to proceed
5. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Setting up test environments without validation
- Skipping prerequisite verification steps
- Ignoring dependency requirements
- Proceeding without understanding service architecture
- Creating incomplete test environments
- Using outdated test configurations

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of critical infrastructure in test setup
- **NO SHORTCUTS** - complete ALL prerequisite validation
- **NO STUBS** - implement complete test environment setup
- **NO FIXED DATA** - use configurable test data sources
- **NO HARDCODED VALUES** - use environment-specific configuration
- **NO WORKAROUNDS** - fix root infrastructure issues
- **NO FAKE IMPLEMENTATIONS** - real test environment only
- **NO PLACEHOLDER CODE** - production-ready test setup only
- **NO TEMPORARY SOLUTIONS** - permanent test infrastructure

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ TEST FRAMEWORK DOCUMENTATION:**

   - Read `TEST_PLAN_FRAMEWORK.md` for testing methodology
   - Review `PLATFORM_TEST_PLAN.md` for platform-specific requirements
   - Study `TEST_PLAN_PREREQUISITES.md` for prerequisite validation
   - Check `PLATFORM_TEST_PLAN_DETAILED.md` for detailed procedures

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Review architecture documentation
   - Study service deployment guides
   - Understand configuration requirements

3. **RESEARCH ONLINE TEST PRACTICES:**
   - Use web search for latest testing frameworks
   - Find official testing documentation
   - Search GitHub for test configuration examples
   - Review industry testing best practices
   - Study similar platform test setups

**SEARCH PRIORITIES:**

- Official testing framework documentation
- Platform-specific testing guides
- GitHub repositories with comprehensive test setups
- Recent testing tutorials and best practices
- Community testing standards

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **TEST-PREREQUISITES-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR TEST PREREQUISITES VALIDATION ONLY:**

- **MUST:** Execute comprehensive test environment validation and setup
- **MUST:** Validate all service dependencies and infrastructure requirements
- **MUST:** Prepare complete test data sources and configurations
- **MUST:** Generate detailed prerequisite validation reports with evidence
- **FORBIDDEN:** Execute ANY actual deployment or system changes
- **FORBIDDEN:** Modify ANY production systems or configurations
- **FORBIDDEN:** Deploy ANY code or infrastructure components
- **MUST:** Output validation results in markdown documents with timestamp tracking

**TEST PREREQUISITES FOCUS AREAS:**

- Test environment readiness validation
- Service dependency verification and health checks
- Infrastructure requirements validation
- Test data preparation and validation
- Security configuration verification
- Monitoring and observability setup validation
- Network connectivity and performance testing

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-prerequisites-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for validation_scope, environment_target, setup_focus
3. **FOLLOW PROTOCOL**: Execute all phases according to the prerequisites validation protocol
4. **VERIFY COMPLETION**: Ensure all validation objectives and readiness criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive prerequisite validation reports with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% prerequisite validation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-prerequisites-prompt"
arguments:
  validation_scope: "[complete|infrastructure|services|data|security|monitoring|network]"
  environment_target: "[local|development|staging|production|multi-environment|all-environments]"
  setup_focus: "[validation-only|setup-and-validation|configuration|dependency-check|readiness-assessment]"
  complexity_level: "[optional: basic|standard|comprehensive|enterprise]"
  infrastructure_requirements: "[optional: hardware, software, network requirements]"
  compliance_validation: "[optional: security, regulatory compliance requirements]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All prerequisite validation phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive prerequisite validation completed across all targeted areas
- [ ] All service dependencies validated and documented (timestamped)
- [ ] Complete infrastructure requirements verified (timestamped)
- [ ] Test data preparation completed and validated (timestamped)
- [ ] Security configuration verified and documented (timestamped)
- [ ] Network connectivity validated across all services (timestamped)
- [ ] Monitoring and observability setup validated (timestamped)
- [ ] Environment readiness certification completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL TEST PREREQUISITES OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All prerequisite validation deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All validation result documentation includes precise timestamps
- [ ] All service dependency reports include timestamp documentation
- [ ] All infrastructure validation reports include proper date stamps
- [ ] All security validation follows consistent date stamp format
- [ ] All monitoring setup documentation includes timestamps
- [ ] All readiness certification includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating prerequisite validation files without proper reverse date stamps
- Using inconsistent date formats within same validation session
- Missing timestamps in validation result documentation

### **TEST PREREQUISITES DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After prerequisites validation completion, proceed with testing using:
/test-execution [test-type] [environment] [additional-options]

# Examples:
/test-execution end-to-end local
/test-execution performance staging
/test-execution security production
```

---

**ENFORCEMENT:** This command performs TEST PREREQUISITES VALIDATION ONLY through the MCP prompt protocol. The comprehensive validation logic is defined in `test-prerequisites-prompt.yaml` and executed according to Model Context Protocol standards. No actual system changes or deployments are performed. Use `/test-execution` for actual testing after prerequisites are validated.

model_context:
role: "AI-driven test prerequisites specialist for comprehensive test environment validation"
domain: "Test Infrastructure, Environment Setup, Dependency Validation, Service Architecture"
goal: >
Execute exhaustive validation and setup of ALL test prerequisites for comprehensive platform testing.
MANDATORY verification of test environment readiness, service dependencies, data requirements,
and infrastructure prerequisites. Generate detailed prerequisite validation reports using
Jupyter Notebook format with validation matrices and readiness certification.

configuration:

# Test prerequisite scope - MANDATORY EXHAUSTIVE COVERAGE

prerequisite_scope:
infrastructure_validation: true # MUST validate all infrastructure
service_dependency_check: true # MUST verify all service dependencies
environment_setup: true # MUST setup complete test environment
data_preparation: true # MUST prepare all test data sources
network_validation: true # MUST validate network connectivity
security_setup: true # MUST configure security for testing
monitoring_preparation: true # MUST setup test monitoring
backup_preparation: true # MUST prepare backup procedures

# Validation requirements - MANDATORY SETTINGS

validation_requirements:
verify_all_services: true # MANDATORY: Check all service status
validate_configurations: true # MANDATORY: Verify all configurations
test_connectivity: true # MANDATORY: Test all connections
verify_permissions: true # MANDATORY: Check access permissions
validate_data_sources: true # MANDATORY: Verify data availability
check_resource_limits: true # MANDATORY: Validate resource capacity
verify_monitoring: true # MANDATORY: Check monitoring setup

# MCP tool integration

mcp_tool_usage:
neo4j_memory_tracking: true # MANDATORY: Track all prerequisite status
sequential_thinking: true # MANDATORY: Structure prerequisite validation
context7_research: true # MANDATORY: Research current best practices
grep_examples: true # MANDATORY: Find test setup examples
filesystem_validation: true # MANDATORY: Validate file system setup
fetch_documentation: true # MANDATORY: Get latest documentation

instructions:

- Phase 1: Comprehensive Prerequisites Discovery and Analysis

  - MANDATORY: Complete environment analysis:
    - Service inventory and analysis:
      - Identify ALL platform services
      - Document ALL service dependencies
      - Map ALL service interactions
      - Verify ALL service configurations
      - Check ALL service health endpoints
      - DOUBLE-CHECK: No services missed
    - Infrastructure requirements analysis:
      - Document ALL hardware requirements
      - Identify ALL software dependencies
      - Map ALL network requirements
      - Verify ALL storage requirements
      - Check ALL security requirements
      - MANDATORY: Complete infrastructure map
    - Test data requirements analysis:
      - Identify ALL test data sources
      - Document ALL data dependencies
      - Map ALL data transformation needs
      - Verify ALL data access requirements
      - Check ALL data privacy requirements
      - FORBIDDEN: Using production data unsafely
  - Environment prerequisite planning:
    - Test environment design:
      - Plan isolated test environment
      - Design data isolation strategy
      - Plan network segmentation
      - Design security isolation
      - Plan resource allocation
      - MANDATORY: Complete environment isolation

- Phase 2: Service Dependency Validation and Setup

  - MANDATORY: Complete service validation:
    - Core service validation:
      - Validate n8n service setup
      - Verify PostgreSQL configuration
      - Check Neo4j graph database
      - Validate Qdrant vector database
      - Verify LightRAG service
      - MANDATORY: All core services operational
    - Supporting service validation:
      - Check monitoring services
      - Verify logging infrastructure
      - Validate backup services
      - Check security services
      - Verify network services
      - DOUBLE-CHECK: All dependencies met
    - External service integration:
      - Validate API endpoints
      - Check authentication services
      - Verify external data sources
      - Test third-party integrations
      - Check service mesh connectivity
      - FORBIDDEN: Unverified external dependencies

- Phase 3: Test Environment Configuration and Validation

  - MANDATORY: Complete environment setup:
    - Container environment setup:
      - Configure Docker containers
      - Setup container networking
      - Verify container storage
      - Configure container security
      - Setup container monitoring
      - MANDATORY: Production-like environment
    - Network configuration validation:
      - Verify internal networking
      - Test external connectivity
      - Validate security groups
      - Check firewall configurations
      - Test load balancing
      - DOUBLE-CHECK: All connections working
    - Data persistence validation:
      - Verify database connections
      - Test data persistence
      - Check backup procedures
      - Validate data recovery
      - Test data migration
      - FORBIDDEN: Data loss scenarios

- Phase 4: Test Data Preparation and Validation

  - MANDATORY: Complete test data setup:
    - Test data generation:
      - Create comprehensive test datasets
      - Generate edge case data
      - Prepare performance test data
      - Create security test data
      - Generate integration test data
      - MANDATORY: Cover all test scenarios
    - Data validation procedures:
      - Verify data integrity
      - Check data consistency
      - Validate data formats
      - Test data transformations
      - Verify data access controls
      - DOUBLE-CHECK: Data quality assured
    - Data backup and recovery:
      - Setup test data backups
      - Test data restoration
      - Verify backup procedures
      - Test disaster recovery
      - Validate data migration
      - FORBIDDEN: Unrecoverable data loss

- Phase 5: Security and Access Control Setup

  - MANDATORY: Complete security validation:
    - Authentication setup:
      - Configure test authentication
      - Setup test user accounts
      - Verify access controls
      - Test permission systems
      - Configure API authentication
      - MANDATORY: Secure test environment
    - Network security validation:
      - Test network isolation
      - Verify encryption setup
      - Check security monitoring
      - Test intrusion detection
      - Validate security logging
      - DOUBLE-CHECK: Security measures active
    - Data security validation:
      - Test data encryption
      - Verify access controls
      - Check data masking
      - Test audit logging
      - Validate compliance controls
      - FORBIDDEN: Security vulnerabilities

- Phase 6: Monitoring and Observability Setup
  - MANDATORY: Complete monitoring validation:
    - Test monitoring setup:
      - Configure test metrics collection
      - Setup test alerting
      - Verify log aggregation
      - Test performance monitoring
      - Configure health checks
      - MANDATORY: Full observability
    - Validation dashboard setup:
      - Create test result dashboards
      - Setup real-time monitoring
      - Configure alert notifications
      - Test monitoring workflows
      - Verify data visualization
      - DOUBLE-CHECK: All metrics visible

validation_matrices:
prerequisite_readiness_matrix: |
| Prerequisite Category | Component | Status | Validation Method | Issues | Ready |
|----------------------|-----------|--------|-------------------|--------|-------|
| Core Services | n8n | ✓ | Health check | None | Yes |
| Databases | PostgreSQL | ✓ | Connection test | None | Yes |
| Monitoring | Prometheus | ✓ | Metrics check | None | Yes |

service_dependency_matrix: |
| Service | Dependencies | Status | Health Check | Configuration | Ready |
|---------|--------------|--------|--------------|---------------|-------|
| n8n | PostgreSQL, API | ✓ | 200 OK | Valid | Yes |
| LightRAG | Qdrant, API | ✓ | 200 OK | Valid | Yes |

environment_validation_matrix: |
| Environment Aspect | Requirement | Current Status | Validation Result | Action Needed |
|-------------------|-------------|----------------|-------------------|---------------|
| Network Connectivity | All services reachable | ✓ Verified | Pass | None |
| Storage Access | All volumes mounted | ✓ Verified | Pass | None |
| Security | All controls active | ✓ Verified | Pass | None |

constraints:

- MANDATORY: ALL prerequisites MUST be validated before testing
- MANDATORY: ALL services MUST be operational
- MANDATORY: ALL configurations MUST be verified
- MANDATORY: ALL security measures MUST be active
- MANDATORY: ALL monitoring MUST be functional
- MANDATORY: ALL data sources MUST be accessible
- MANDATORY: Documentation in markdown documents
- FORBIDDEN: Proceeding with incomplete prerequisites
- FORBIDDEN: Skipping validation steps
- FORBIDDEN: Using unverified configurations
- FORBIDDEN: Ignoring security requirements
- FORBIDDEN: Proceeding with service failures

output_format:
jupyter_structure: - "01_Prerequisites_Analysis.ipynb": - Service inventory and dependencies - Infrastructure requirements - Test data requirements - Environment prerequisites - Security requirements

    - "02_Service_Validation.ipynb":
        - Core service validation results
        - Supporting service checks
        - External service integration
        - Dependency verification
        - Health check results

    - "03_Environment_Setup.ipynb":
        - Container environment configuration
        - Network setup and validation
        - Storage configuration
        - Security setup results
        - Monitoring configuration

    - "04_Test_Data_Preparation.ipynb":
        - Test data generation procedures
        - Data validation results
        - Backup and recovery setup
        - Data access control validation
        - Data quality verification

    - "05_Security_Validation.ipynb":
        - Authentication setup results
        - Access control validation
        - Network security verification
        - Data security validation
        - Compliance verification

    - "06_Monitoring_Setup.ipynb":
        - Monitoring configuration
        - Dashboard setup
        - Alert configuration
        - Performance monitoring
        - Health check validation

validation_criteria:
infrastructure_ready: "MANDATORY - All infrastructure validated and operational"
services_operational: "MANDATORY - All services running and healthy"
environment_configured: "MANDATORY - Test environment properly configured"
data_prepared: "MANDATORY - All test data prepared and validated"
security_active: "MANDATORY - All security measures operational"
monitoring_functional: "MANDATORY - All monitoring systems active"
prerequisites_complete: "MANDATORY - 100% prerequisite validation complete"

final_deliverables:

- Prerequisites_Validation_Report.ipynb (complete validation)
- Service_Readiness_Matrix.xlsx (service status tracking)
- Environment_Configuration_Guide.ipynb (setup procedures)
- Test_Data_Inventory.ipynb (data preparation results)
- Security_Validation_Report.ipynb (security verification)
- Monitoring_Setup_Guide.ipynb (monitoring configuration)
- Prerequisites_Certification.pdf (readiness certification)

# Execution Command

usage: |
test-prerequisites # Validate all prerequisites
test-prerequisites "service setup" # Validate specific service setup
test-prerequisites "data prep" # Focus on data preparation

execution_protocol: |
MANDATORY REQUIREMENTS:

- MUST validate ALL test prerequisites
- MUST verify ALL service dependencies
- MUST setup complete test environment
- MUST prepare ALL test data sources
- MUST configure ALL security measures
- MUST setup ALL monitoring systems
- MUST document ALL validation results
- MUST use MCP tools for tracking
- MUST use sub-agents for execution

STRICTLY FORBIDDEN:

- NO incomplete prerequisite validation
- NO unverified service dependencies
- NO incomplete environment setup
- NO unverified test data
- NO missing security measures
- NO incomplete monitoring setup
- NO proceeding without validation
- NO shortcuts in prerequisite setup

MCP TOOL REQUIREMENTS:

- USE memory to track validation progress
- USE sequential-thinking for structured validation
- USE context7 for latest testing best practices
- USE grep for test setup examples
- USE filesystem for configuration validation
- USE fetch for documentation retrieval

SUB-AGENT EXECUTION:

- ALL validation tasks via sub-agents
- ALL setup procedures via sub-agents
- ALL verification steps via sub-agents
- ALL documentation via sub-agents

---
