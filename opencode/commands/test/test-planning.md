# === Universal Test Planning: AI-Driven Comprehensive Test Strategy and Framework Creation Protocol ===

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
3. **READ AND INDEX**: `.claude/commands/test/test-protocol-planning-framework.md`
4. **READ AND INDEX**: `.claude/commands/test/test-protocol-service-examples.md`
5. **VERIFY**: User has given explicit permission to proceed
6. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Creating incomplete test plans
- Skipping comprehensive feature analysis
- Ignoring performance testing requirements
- Proceeding without understanding system architecture
- Creating plans without measurable success criteria
- Using generic test templates without customization

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of critical system components in test planning
- **NO SHORTCUTS** - plan ALL testing scenarios comprehensively
- **NO STUBS** - create complete test planning frameworks
- **NO FIXED DATA** - plan for dynamic test data scenarios
- **NO HARDCODED VALUES** - use configurable test parameters
- **NO WORKAROUNDS** - plan proper testing methodologies
- **NO FAKE IMPLEMENTATIONS** - plan real system testing only
- **NO PLACEHOLDER CODE** - production-ready test planning only
- **NO TEMPORARY SOLUTIONS** - permanent test strategy planning

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ TEST FRAMEWORK DOCUMENTATION:**

   - Read `TEST_PLAN_FRAMEWORK.md` for comprehensive methodology
   - Review `PLATFORM_TEST_PLAN.md` for platform requirements
   - Study `PLATFORM_TEST_PLAN_DETAILED.md` for detailed procedures
   - Check `TEST_PLAN_PREREQUISITES.md` for prerequisite validation

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Review architecture documentation
   - Study API documentation
   - Understand service interactions
   - Review deployment guides

3. **RESEARCH ONLINE TEST PLANNING:**
   - Use web search for latest test planning methodologies
   - Find official testing framework documentation
   - Search GitHub for comprehensive test plans
   - Review industry testing best practices
   - Study similar platform test strategies

**SEARCH PRIORITIES:**

- Official testing methodology documentation
- Comprehensive test planning frameworks
- GitHub repositories with detailed test strategies
- Recent testing tutorials and methodologies
- Community testing standards and practices

---

## INSTRUCTIONS

model_context:
role: "AI-driven test planning specialist for comprehensive platform test strategy creation"
domain: "Test Strategy, Test Framework Design, Test Case Planning, Quality Assurance Planning"
goal: >
Create exhaustive and comprehensive test plans for ALL platform features, functions, API endpoints,
and application components. MANDATORY planning of complete test coverage including functional,
performance, security, integration, and end-to-end testing strategies. Generate detailed test
planning documentation using Jupyter Notebook format with comprehensive test matrices, expected
vs actual tracking, and deviation analysis procedures.

configuration:

# Test planning scope - MANDATORY EXHAUSTIVE COVERAGE

planning_scope:
all_features_inventory: true # MUST list ALL features and functions
all_endpoints_mapping: true # MUST map ALL API endpoints
all_app_endpoints: true # MUST document ALL app endpoints
data_requirements: true # MUST document ALL data requirements
network_requirements: true # MUST document ALL network requirements
storage_requirements: true # MUST document ALL storage requirements
performance_requirements: true # MUST define ALL performance criteria
security_requirements: true # MUST define ALL security test requirements
integration_requirements: true # MUST plan ALL integration scenarios

# Test planning requirements - MANDATORY SETTINGS

planning_requirements:
comprehensive_feature_analysis: true # MANDATORY: Analyze every feature
endpoint_functionality_mapping: true # MANDATORY: Map all endpoint functions
test_case_specification: true # MANDATORY: Specify all test cases
expected_vs_actual_tracking: true # MANDATORY: Define tracking framework
deviation_analysis_procedures: true # MANDATORY: Plan deviation analysis
test_data_strategy: true # MANDATORY: Plan test data approach
test_environment_strategy: true # MANDATORY: Plan environment approach
test_automation_strategy: true # MANDATORY: Plan automation approach

# Framework integration

framework_integration:
existing_test_documents: true # MANDATORY: Integrate existing framework
platform_specific_requirements: true # MANDATORY: Use platform requirements
service_specific_testing: true # MANDATORY: Plan service-specific tests
end_to_end_scenarios: true # MANDATORY: Plan E2E test scenarios

# MCP tool integration

mcp_tool_usage:
neo4j_memory_tracking: true # MANDATORY: Track planning progress
sequential_thinking: true # MANDATORY: Structure planning approach
context7_research: true # MANDATORY: Research testing best practices
grep_examples: true # MANDATORY: Find test planning examples
filesystem_analysis: true # MANDATORY: Analyze project structure
fetch_documentation: true # MANDATORY: Get latest documentation

instructions:

- Phase 1: Comprehensive Platform Feature Analysis and Inventory

  - MANDATORY: Complete feature discovery and documentation:
    - Platform feature inventory:
      - List ALL user-facing features
      - Document ALL administrative features
      - Map ALL automation features
      - Identify ALL workflow features
      - Catalog ALL integration features
      - DOUBLE-CHECK: No features missed
    - API endpoint comprehensive mapping:
      - Document ALL REST API endpoints
      - Map ALL GraphQL endpoints (if applicable)
      - List ALL WebSocket endpoints
      - Catalog ALL webhook endpoints
      - Document ALL internal API endpoints
      - MANDATORY: Complete endpoint coverage
    - Application endpoint documentation:
      - Map ALL web application routes
      - Document ALL single-page application routes
      - List ALL mobile application endpoints
      - Catalog ALL admin interface endpoints
      - Map ALL configuration endpoints
      - FORBIDDEN: Missing any application endpoints
  - System architecture analysis:
    - Component interaction mapping:
      - Map ALL service interactions
      - Document ALL data flows
      - Identify ALL integration points
      - Map ALL external dependencies
      - Document ALL internal dependencies
      - MANDATORY: Complete architecture understanding

- Phase 2: Test Requirements Analysis and Documentation

  - MANDATORY: Comprehensive requirements documentation:
    - Data requirements analysis:
      - Document ALL test data sources
      - Identify ALL data transformation needs
      - Map ALL data validation requirements
      - Plan ALL data backup requirements
      - Define ALL data privacy requirements
      - MANDATORY: Complete data strategy
    - Network requirements documentation:
      - Document ALL network connectivity needs
      - Map ALL external service dependencies
      - Identify ALL internal network requirements
      - Plan ALL network security testing
      - Define ALL network performance requirements
      - DOUBLE-CHECK: All network aspects covered
    - Storage requirements analysis:
      - Document ALL database testing requirements
      - Map ALL file storage testing needs
      - Identify ALL cache testing requirements
      - Plan ALL backup storage testing
      - Define ALL storage performance requirements
      - FORBIDDEN: Incomplete storage planning
  - Performance criteria definition:
    - Response time requirements:
      - Define ALL API response time limits
      - Set ALL page load time requirements
      - Plan ALL database query time limits
      - Define ALL file transfer time limits
      - Set ALL workflow execution time limits
      - MANDATORY: Measurable performance criteria

- Phase 3: Test Case Specification and Framework Design

  - MANDATORY: Comprehensive test case planning:
    - Functional test case specification:
      - Design ALL positive test cases
      - Plan ALL negative test cases
      - Create ALL boundary test cases
      - Design ALL error handling test cases
      - Plan ALL edge case scenarios
      - MANDATORY: Complete functional coverage
    - Integration test case design:
      - Plan ALL service integration tests
      - Design ALL API integration tests
      - Create ALL database integration tests
      - Plan ALL external service integration tests
      - Design ALL workflow integration tests
      - DOUBLE-CHECK: All integrations tested
    - Performance test case planning:
      - Design ALL load testing scenarios
      - Plan ALL stress testing scenarios
      - Create ALL volume testing scenarios
      - Design ALL scalability testing scenarios
      - Plan ALL endurance testing scenarios
      - FORBIDDEN: Missing performance scenarios
  - Security test case specification:
    - Authentication testing:
      - Plan ALL login scenario tests
      - Design ALL access control tests
      - Create ALL permission testing scenarios
      - Plan ALL session management tests
      - Design ALL logout scenario tests
      - MANDATORY: Complete security coverage

- Phase 4: Expected vs Actual Tracking Framework Design

  - MANDATORY: Comprehensive tracking system design:
    - Expected results definition:
      - Define ALL expected functional outcomes
      - Set ALL expected performance metrics
      - Specify ALL expected security behaviors
      - Define ALL expected integration results
      - Set ALL expected error handling behaviors
      - MANDATORY: Measurable expected results
    - Actual results tracking framework:
      - Design result capture mechanisms
      - Plan automated result collection
      - Create manual verification procedures
      - Design result storage systems
      - Plan result analysis workflows
      - DOUBLE-CHECK: Complete tracking coverage
    - Deviation detection procedures:
      - Plan automated deviation detection
      - Design threshold-based alerting
      - Create variance analysis procedures
      - Plan trend analysis methods
      - Design anomaly detection systems
      - FORBIDDEN: Undetected deviations

- Phase 5: Test Automation Strategy and Implementation Planning

  - MANDATORY: Complete automation strategy:
    - Test automation framework selection:
      - Evaluate automation tools
      - Select appropriate frameworks
      - Plan tool integration
      - Design automation architecture
      - Plan maintenance procedures
      - MANDATORY: Scalable automation strategy
    - Automation implementation planning:
      - Plan test script development
      - Design test data automation
      - Plan environment automation
      - Design result automation
      - Plan reporting automation
      - DOUBLE-CHECK: Complete automation coverage
    - Continuous testing integration:
      - Plan CI/CD integration
      - Design automated trigger systems
      - Plan automated reporting
      - Design feedback loops
      - Plan continuous improvement
      - FORBIDDEN: Manual-only testing approach

- Phase 6: Test Execution Strategy and Resource Planning
  - MANDATORY: Complete execution planning:
    - Test execution sequencing:
      - Plan test execution order
      - Design dependency management
      - Plan parallel execution
      - Design resource optimization
      - Plan execution monitoring
      - MANDATORY: Efficient execution strategy
    - Resource allocation planning:
      - Plan human resource allocation
      - Design infrastructure resource planning
      - Plan tool resource allocation
      - Design time allocation
      - Plan budget allocation
      - DOUBLE-CHECK: Adequate resources planned

test_planning_matrices:
feature_coverage_matrix: |
| Feature Category | Feature Name | Test Type | Priority | Coverage % | Test Cases | Status |
|------------------|--------------|-----------|----------|------------|------------|--------|
| User Management | User Login | Functional | High | 100% | 15 | Planned |
| API Services | User API | Integration | High | 100% | 25 | Planned |
| Workflows | n8n Automation | E2E | High | 100% | 30 | Planned |

endpoint_testing_matrix: |
| Endpoint | Method | Function | Test Scenarios | Expected Results | Performance Target |
|----------|--------|----------|----------------|------------------|-------------------|
| /api/users | GET | List users | 10 scenarios | User list JSON | < 200ms |
| /api/auth/login | POST | User login | 8 scenarios | Auth token | < 500ms |
| /api/workflows | GET | List workflows | 12 scenarios | Workflow list | < 300ms |

test_requirements_matrix: |
| Requirement Type | Component | Specification | Test Method | Success Criteria | Priority |
|------------------|-----------|---------------|-------------|------------------|----------|
| Performance | API Response | < 200ms | Automated | 95% under limit | High |
| Security | Authentication | OAuth2 | Manual + Auto | All access controlled | Critical |
| Integration | Database | CRUD operations | Automated | All operations work | High |

expected_vs_actual_tracking: |
| Test Case ID | Expected Result | Actual Result | Deviation | Severity | Action Required |
|--------------|----------------|---------------|-----------|----------|-----------------|
| TC001 | 200ms response | TBD | TBD | TBD | TBD |
| TC002 | Valid JSON | TBD | TBD | TBD | TBD |
| TC003 | Access denied | TBD | TBD | TBD | TBD |

constraints:

- MANDATORY: ALL features MUST be inventoried and planned
- MANDATORY: ALL endpoints MUST be mapped and tested
- MANDATORY: ALL requirements MUST be documented
- MANDATORY: ALL test cases MUST have expected results
- MANDATORY: ALL tracking MUST be automated where possible
- MANDATORY: ALL deviations MUST have analysis procedures
- MANDATORY: Documentation in markdown documents
- FORBIDDEN: Incomplete feature analysis
- FORBIDDEN: Missing endpoint documentation
- FORBIDDEN: Undefined expected results
- FORBIDDEN: Manual-only tracking systems
- FORBIDDEN: Unplanned deviation handling

output_format:
jupyter_structure: - "01_Platform_Feature_Inventory.ipynb": - Complete feature listing - API endpoint mapping - Application endpoint documentation - System architecture analysis - Integration point mapping

    - "02_Test_Requirements_Analysis.ipynb":
        - Data requirements documentation
        - Network requirements analysis
        - Storage requirements planning
        - Performance criteria definition
        - Security requirements specification

    - "03_Test_Case_Specification.ipynb":
        - Functional test case design
        - Integration test planning
        - Performance test scenarios
        - Security test specifications
        - End-to-end test planning

    - "04_Expected_Vs_Actual_Framework.ipynb":
        - Expected results definition
        - Tracking framework design
        - Deviation analysis procedures
        - Automated detection systems
        - Reporting mechanisms

    - "05_Test_Automation_Strategy.ipynb":
        - Automation framework selection
        - Implementation planning
        - Tool integration design
        - Continuous testing strategy
        - Maintenance procedures

    - "06_Test_Execution_Planning.ipynb":
        - Execution sequencing
        - Resource allocation
        - Timeline planning
        - Risk mitigation
        - Success criteria definition

validation_criteria:
feature_completeness: "MANDATORY - 100% of features inventoried and planned"
endpoint_coverage: "MANDATORY - All endpoints mapped and test planned"
requirements_documented: "MANDATORY - All requirements fully documented"
test_cases_specified: "MANDATORY - All test cases with expected results"
tracking_framework: "MANDATORY - Complete expected vs actual tracking"
automation_strategy: "MANDATORY - Comprehensive automation planning"
execution_planning: "MANDATORY - Complete execution strategy defined"

final_deliverables:

- Comprehensive_Test_Plan.ipynb (complete test strategy)
- Feature_Test_Matrix.xlsx (feature coverage tracking)
- Endpoint_Testing_Guide.ipynb (API testing procedures)
- Expected_Vs_Actual_Framework.ipynb (tracking methodology)
- Test_Automation_Strategy.ipynb (automation planning)
- Test_Execution_Plan.ipynb (execution procedures)
- Deviation_Analysis_Procedures.ipynb (analysis methodology)

# Execution Command

usage: |
code:test-planning # Create comprehensive test plan
code:test-planning "api testing" # Focus on API test planning
code:test-planning "performance tests" # Focus on performance planning

execution_protocol: |
MANDATORY REQUIREMENTS:

- MUST inventory ALL features and functions
- MUST map ALL API and application endpoints
- MUST document ALL test requirements comprehensively
- MUST specify ALL test cases with expected results
- MUST design expected vs actual tracking framework
- MUST plan comprehensive automation strategy
- MUST create detailed execution planning
- MUST use MCP tools for research and tracking
- MUST use sub-agents for all planning tasks

STRICTLY FORBIDDEN:

- NO incomplete feature analysis
- NO missing endpoint documentation
- NO undefined test requirements
- NO test cases without expected results
- NO manual-only tracking approaches
- NO incomplete automation planning
- NO undefined execution strategies
- NO planning without research

MCP TOOL REQUIREMENTS:

- USE neo4j-memory to track planning progress
- USE sequential-thinking for structured planning
- USE context7 for latest testing methodologies
- USE grep for test planning examples
- USE filesystem for project structure analysis
- USE fetch for testing documentation

SUB-AGENT EXECUTION:

- ALL analysis tasks via sub-agents
- ALL planning procedures via sub-agents
- ALL documentation via sub-agents
- ALL framework design via sub-agents

INTEGRATION REQUIREMENTS:

- MUST integrate with existing TEST_PLAN_FRAMEWORK.md
- MUST use PLATFORM_TEST_PLAN.md specifications
- MUST reference PLATFORM_TEST_PLAN_DETAILED.md
- MUST align with TEST_PLAN_PREREQUISITES.md

---
