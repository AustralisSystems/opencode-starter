# === Universal Code Gap Analysis: AI-Driven Exhaustive Production Code Gap Assessment Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance-prompt.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance-prompt.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

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

### **GAP ANALYSIS-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR GAP ANALYSIS ONLY:**

- **MUST:** Execute exhaustive gap analysis of ALL production code
- **MUST:** Identify ALL missing components and incomplete implementations
- **MUST:** Create actionable remediation plans with priorities
- **MUST:** Analyze against requirements, best practices, and standards
- **FORBIDDEN:** Analyze test code or external documentation
- **FORBIDDEN:** Create duplicate files or backup copies
- **FORBIDDEN:** Execute any remediation or implementation
- **MUST:** Output analysis documentation in markdown documents

**GAP ANALYSIS FOCUS AREAS:**

- Production code completeness assessment
- Functional and feature gap identification
- Technical and architecture gap analysis
- Security and performance gap assessment
- Debug logging and monitoring gap analysis
- Code reuse and validation gap analysis

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-gap-analysis-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for analysis_target, analysis_scope, gap_categories
3. **FOLLOW PROTOCOL**: Execute all phases according to the gap analysis protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive gap analysis documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% analysis completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-gap-analysis-prompt"
arguments:
  analysis_target: "[entire codebase|specific module|focus area]"
  analysis_scope: "[comprehensive|functional-only|technical-only|security-focused|performance-focused|quality-focused]"
  gap_categories: "[optional: all-gaps|functional-gaps|technical-gaps|security-gaps|performance-gaps|logging-gaps|validation-gaps]"
  priority_focus: "[optional: critical-only|high-priority|all-priorities|quick-wins]"
  remediation_planning: "[optional: true|false]"
  compliance_standards: "[optional: SOLID, DRY, KISS, OWASP, etc.]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All gap analysis phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive production code gap analysis completed
- [ ] All production code inventoried and analyzed (timestamped)
- [ ] All functional gaps identified and documented (timestamped)
- [ ] All technical and architecture gaps assessed (timestamped)
- [ ] All security vulnerabilities and gaps documented (timestamped)
- [ ] All performance bottlenecks and inefficiencies identified (timestamped)
- [ ] All debug logging and monitoring gaps analyzed (timestamped)
- [ ] All code reuse opportunities and validation gaps documented (timestamped)
- [ ] Comprehensive remediation roadmap created (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL GAP ANALYSIS OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All gap analysis deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All gap inventory documentation includes precise timestamps
- [ ] All functional gap analysis includes timestamp documentation
- [ ] All technical gap analysis includes proper date stamps
- [ ] All security gap assessment follows consistent date stamp format
- [ ] All performance gap reports include timestamps
- [ ] All logging gap analysis includes proper date stamps
- [ ] All remediation roadmaps include timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating gap analysis files without proper reverse date stamps
- Using inconsistent date formats within same analysis session
- Missing timestamps in gap analysis documentation

instructions:

- Phase 1: Complete Production Code Inventory and Analysis

  - MANDATORY: Exhaustive code discovery:
    - Production code inventory:
      - Scan ALL source files
      - Map ALL modules
      - List ALL components
      - Track ALL dependencies
      - Document ALL interfaces
      - DOUBLE-CHECK: Nothing missed
    - Architecture analysis:
      - Map component relationships
      - Document data flows
      - Identify integration points
      - Track service boundaries
      - Map API contracts
      - MANDATORY: Complete picture
    - Code quality baseline:
      - Measure complexity
      - Check duplication
      - Assess coupling
      - Evaluate cohesion
      - Track tech debt
      - FORBIDDEN: Ignoring issues
  - Requirements mapping:
    - Functional requirements:
      - Map ALL features
      - Track implementation status
      - Identify missing pieces
      - Document partial implementations
      - List edge cases
      - MANDATORY: Full traceability
    - Technical requirements:
      - Performance targets
      - Scalability needs
      - Security requirements
      - Reliability goals
      - Maintainability standards
      - DOUBLE-CHECK: All covered

- Phase 2: Functional and Feature Gap Analysis

  - MANDATORY: Find ALL functional gaps:
    - Missing features:
      - Unimplemented requirements
      - Partial implementations
      - Stubbed functions
      - TODO comments
      - Placeholder code
      - FORBIDDEN: Accepting stubs
    - Business logic gaps:
      - Incorrect calculations
      - Missing validations
      - Incomplete workflows
      - Edge case handling
      - Error scenarios
      - MANDATORY: Complete logic
    - Integration gaps:
      - Missing API endpoints
      - Incomplete contracts
      - Broken integrations
      - Missing adaptors
      - Protocol mismatches
      - DOUBLE-CHECK: All connected
  - User experience gaps:
    - Missing functionality:
      - Incomplete features
      - Broken workflows
      - Missing feedback
      - Error handling
      - Help systems
      - MANDATORY: Full UX

- Phase 3: Technical and Architecture Gap Analysis

  - MANDATORY: Identify ALL technical gaps:
    - SOLID principle violations:
      - Single Responsibility gaps
      - Open/Closed violations
      - Liskov Substitution issues
      - Interface Segregation problems
      - Dependency Inversion gaps
      - MANDATORY: Full compliance
    - Code quality gaps:
      - DRY violations (duplication)
      - KISS violations (complexity)
      - Poor naming
      - Magic numbers
      - Long methods
      - FORBIDDEN: Poor quality
    - Architecture gaps:
      - Missing layers
      - Tight coupling
      - Poor cohesion
      - Circular dependencies
      - Missing patterns
      - DOUBLE-CHECK: Clean architecture
  - Infrastructure gaps:
    - Scalability issues:
      - Missing caching
      - No load balancing
      - Connection limits
      - Memory leaks
      - Resource waste
      - MANDATORY: Production ready

- Phase 4: Security and Performance Gap Analysis

  - MANDATORY: Find ALL security gaps:
    - Authentication gaps:
      - Weak mechanisms
      - Missing MFA
      - Token issues
      - Session problems
      - Password policies
      - MANDATORY: Strong auth
    - Authorization gaps:
      - Missing checks
      - Broken access control
      - Privilege escalation
      - Data exposure
      - API vulnerabilities
      - FORBIDDEN: Open access
    - Data security gaps:
      - Missing encryption
      - Weak algorithms
      - Key management
      - Data leakage
      - Injection points
      - DOUBLE-CHECK: Secure data
  - Performance gap analysis:
    - Algorithm efficiency:
      - O(n) operations
      - Missing indexes
      - N+1 queries
      - Synchronous I/O
      - Memory waste
      - MANDATORY: Optimized
    - Resource utilization:
      - Connection pooling
      - Caching strategy
      - Batch processing
      - Async operations
      - Stream processing
      - MANDATORY: Efficient

- Phase 5: Debug Logging and Monitoring Gap Analysis

  - MANDATORY: Analyze ALL logging gaps:
    - Debug logging coverage:
      - Entry/exit logging
      - Parameter logging
      - State changes
      - Decision points
      - Error details
      - MANDATORY: Full coverage
    - Structured logging:
      - Consistent format
      - Correlation IDs
      - Context inclusion
      - Performance metrics
      - Security events
      - FORBIDDEN: Silent failures
    - Monitoring gaps:
      - Missing metrics
      - No health checks
      - Absent alerts
      - No dashboards
      - Missing traces
      - DOUBLE-CHECK: Observable
  - Operational gaps:
    - Deployment readiness:
      - Missing configs
      - No rollback plan
      - Absent runbooks
      - No monitoring
      - Missing alerts
      - MANDATORY: Prod ready

- Phase 6: Code Reuse and Validation Gap Analysis
  - MANDATORY: Find ALL reuse opportunities:
    - Duplication analysis:
      - Identical code blocks
      - Similar patterns
      - Common utilities
      - Shared logic
      - Repeated structures
      - MANDATORY: DRY compliance
    - Consolidation opportunities:
      - Extract methods
      - Create utilities
      - Build libraries
      - Share components
      - Unify patterns
      - FORBIDDEN: Duplication
  - Validation workflow gaps:
    - Pre-commit gaps:
      - No linting
      - Missing type checks
      - No complexity checks
      - Missing dedup scan
      - No security scan
      - MANDATORY: Quality gates
    - CI/CD gaps:
      - No auto-build
      - Missing deploy
      - No log checking
      - Missing rollback
      - No monitoring
      - DOUBLE-CHECK: Full pipeline

gap_analysis_methodologies:
static_analysis:
code_quality:
tools: "Language-specific analyzers"
metrics: "Complexity, duplication, coupling"
thresholds: "Industry standards"

    security_scanning:
      tools: "SAST, dependency scanners"
      rules: "OWASP, CWE standards"
      severity: "Critical, High, Medium, Low"

    compliance_checking:
      standards: "SOLID, DRY, KISS"
      patterns: "Best practices"
      violations: "Anti-patterns"

dynamic_analysis:
runtime_behavior:
monitoring: "Performance profiling"
tracing: "Execution paths"
logging: "Debug output analysis"

    integration_testing:
      api_validation: "Contract testing"
      data_flow: "End-to-end verification"
      error_scenarios: "Failure mode testing"

validation_matrices:
gap_inventory_matrix: |
| Gap ID | Category | Severity | Component | Impact | Effort | Status |
|--------|----------|----------|-----------|---------|---------|--------|
| GAP-001 | Security | CRITICAL | Auth API | High | 2d | OPEN |

compliance_gap_matrix: |
| Principle | Component | Violation | Remediation | Priority | Status |
|-----------|-----------|-----------|-------------|----------|--------|
| SOLID-SRP | UserService | Mixed concerns | Extract | HIGH | OPEN |

logging_gap_matrix: |
| Component | Entry/Exit | Params | Errors | State | Security | Coverage |
|-----------|------------|---------|---------|--------|----------|----------|
| AuthAPI | Missing | Partial | Yes | No | Partial | 40% |

constraints:

- MANDATORY: ALL production code MUST be analyzed
- MANDATORY: EVERY gap MUST be documented
- MANDATORY: ALL findings MUST be actionable
- MANDATORY: Priorities MUST be assigned
- MANDATORY: Effort MUST be estimated
- MANDATORY: Remediation MUST be planned
- MANDATORY: Documentation in Jupyter only
- MANDATORY: Analyze existing code in-place
- MANDATORY: NEVER create duplicate files or copies
- FORBIDDEN: Analyzing test code
- FORBIDDEN: External doc analysis
- FORBIDDEN: Accepting placeholders
- FORBIDDEN: Ignoring security gaps
- FORBIDDEN: Allowing duplication
- FORBIDDEN: Missing debug logs
- FORBIDDEN: Creating duplicate analysis files
- FORBIDDEN: Making backup copies for analysis
- FORBIDDEN: Creating alternative code versions

output_format:
jupyter_structure: - "01_Gap_Analysis_Overview.ipynb": - Analysis scope and methodology - Production code inventory - Requirements mapping - Gap categories summary - Executive summary

    - "02_Functional_Gaps.ipynb":
        - Missing features inventory
        - Incomplete implementations
        - Business logic gaps
        - Integration gaps
        - Remediation priorities

    - "03_Technical_Gaps.ipynb":
        - SOLID violations
        - DRY/KISS violations
        - Architecture gaps
        - Code quality issues
        - Refactoring needs

    - "04_Security_Gaps.ipynb":
        - Authentication gaps
        - Authorization issues
        - Data security gaps
        - Vulnerability inventory
        - Security roadmap

    - "05_Performance_Gaps.ipynb":
        - Algorithm inefficiencies
        - Resource waste
        - Scaling issues
        - Optimization opportunities
        - Performance targets

    - "06_Logging_Monitoring_Gaps.ipynb":
        - Debug logging gaps
        - Monitoring coverage
        - Observability issues
        - Alert gaps
        - Remediation plan

    - "07_Remediation_Roadmap.ipynb":
        - Prioritized gap list
        - Effort estimates
        - Quick wins
        - Dependencies
        - Timeline

validation_criteria:
analysis_completeness: "MANDATORY - 100% code analyzed"
gap_identification: "MANDATORY - All gaps found"
priority_assignment: "MANDATORY - All gaps prioritized"
effort_estimation: "MANDATORY - Hours/days estimated"
remediation_planning: "MANDATORY - Action plans created"
risk_assessment: "MANDATORY - Impact evaluated"
documentation_quality: "MANDATORY - markdown documents complete"
actionable_findings: "MANDATORY - Can be implemented"

final_deliverables:

- Complete_Gap_Inventory.ipynb (all gaps cataloged)
- Functional_Gap_Analysis.ipynb (feature gaps)
- Technical_Gap_Analysis.ipynb (quality gaps)
- Security_Gap_Assessment.ipynb (vulnerabilities)
- Performance_Gap_Report.ipynb (optimizations)
- Logging_Gap_Analysis.ipynb (observability)
- Remediation_Roadmap.ipynb (action plan)
- Executive_Summary.ipynb (key findings)

# Execution Command

usage: |
/code-gap-analysis # Analyze entire codebase
/code-gap-analysis "user module" # Focus on specific module
/code-gap-analysis "security" # Security-focused analysis

execution_protocol: |
MANDATORY REQUIREMENTS:

- MUST analyze ALL production code
- MUST find ALL gaps
- MUST prioritize findings
- MUST estimate effort
- MUST plan remediation
- MUST assess risk
- MUST track duplication
- MUST check logging
- MUST analyze existing code only
- MUST maintain pristine codebase

STRICTLY FORBIDDEN:

- NO test code analysis
- NO external doc gaps
- NO accepting stubs
- NO ignoring issues
- NO vague findings
- NO missing priorities
- NO skipped components
- NO incomplete analysis
- NO duplicate files EVER
- NO backup copies EVER
- NO alternative versions EVER
- NO gap_analysis_copy.py files

CODEBASE HYGIENE RULES:

- ALWAYS analyze existing code
- FORBIDDEN: create duplicates
- FORBIDDEN: create backups
- FORBIDDEN: create alternatives
- ANALYZE in-place ONLY
- DELETE transient files
- MAINTAIN clean repository
