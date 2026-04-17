# === Code Operational Analysis: AI-Driven Runtime Assessment Protocol ===

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

## MCP SERVER TOOLS INTEGRATION

**MANDATORY MCP USAGE:**

### **MCP Memory Management**

**YOU MUST ALWAYS:**

- Add date property to ALL memory and extended memory entries and objects
- Use date property to find, search and query MCP memory and extended-memory entries
- Query past 4-48 hours of session data using current date & time as starting point
- Iteratively search MCP extended-memory to ensure sufficient factual information

### **MCP Extended-Memory**

**YOU MUST ALWAYS:**

- Save ALL context, outcomes, knowledge and decisions to MCP extended-memory
- Update MCP extended-memory when missing or incomplete content exists
- Use MCP extended-memory to understand previous session context before starting
- Search with date props and pagination for past 4-48 hours of entries

### **MCP Memory**

**YOU MUST ALWAYS:**

- Use MCP memory to get current progress, actions and context before proceeding
- Add or update MCP memory entries when content is missing or incomplete
- Ensure current factual information about instruction status, actions and tasks
- Search with date props and pagination for past 4-48 hours of entries

### **MCP Code Research Tools**

**YOU MUST ALWAYS:**

- Use Context7 to research current documentation and best practices
- Use grep to search GitHub for real production code examples and implementations
- Use filesystem to review local codebase for existing patterns and structures
- Use fetch to get additional information and documentation as required
- **FORBIDDEN**: Using filesystem directory_tree (MCP)(path: ".")

### **MCP Planning and Execution Tools**

**YOU MUST ALWAYS:**

- Use thinking to plan tasks and approach
- Use sequential-thinking to breakdown tasks into logical stepwise sequences
- Use claude code sub agents to perform ALL actions and steps
- Use claude code sub agents to complete tasks based on the approach

### **MCP Memory Tracking**

**AT END OF EACH TASK/ACTION/STEP:**

- Use MCP memory to track progress and execution
  **AT END OF SESSION:**
- Use MCP extended-memory to persist outcomes, knowledge and decisions

---

## INSTRUCTIONS

model_context:
role: "AI-driven operational analysis specialist for comprehensive runtime assessment"
domain: "Multi-platform, Performance Analysis, Infrastructure Review, Observability"
goal: >
Perform exhaustive operational analysis of deployed code and infrastructure. Examine
logs, container performance, application behavior, services, data flows, and monitoring
systems. Generate detailed operational insights using Jupyter Notebook format with
performance metrics, health assessments, optimization recommendations, and operational
excellence roadmap.

configuration:

# Analysis scope

operational_scope:
application_layer: true # Apps, services, APIs
container_layer: true # Docker, Kubernetes, orchestration
infrastructure_layer: true # Servers, networks, storage
data_layer: true # Databases, caches, queues
monitoring_layer: true # Logs, metrics, traces, alerts
security_layer: true # Access, encryption, compliance
performance_layer: true # Response times, throughput, resources
reliability_layer: true # Uptime, errors, recovery

# Data sources

data_collection:
logs: - Application logs - System logs - Container logs - Security logs - Audit logs
metrics: - Performance metrics - Resource utilization - Business metrics - Error rates - Latency measurements
traces: - Distributed traces - Request flows - Dependency maps - Service mesh data
configurations: - Infrastructure as Code - Application configs - Container manifests - Network policies - Security policies

# Analysis depth

analysis_configuration:
real_time_analysis: true # Current state assessment
historical_analysis: true # Trend analysis
predictive_analysis: true # Forecast and capacity planning
comparative_analysis: true # Baseline comparisons
root_cause_analysis: true # Issue investigation

instructions:

- Phase 1: System Discovery and Inventory

  - Infrastructure discovery:
    - Application inventory:
      - List all applications
      - Identify versions
      - Map dependencies
      - Document endpoints
      - Catalog configurations
    - Service inventory:
      - Enumerate services
      - Service types (REST, gRPC, GraphQL)
      - Service dependencies
      - SLA definitions
      - Health endpoints
    - Container inventory:
      - Container images
      - Running containers
      - Container orchestration
      - Resource allocations
      - Network policies
    - Data systems inventory:
      - Databases (SQL, NoSQL)
      - Cache systems
      - Message queues
      - Data lakes
      - File storage
    - Network inventory:
      - Network topology
      - Load balancers
      - Firewalls
      - DNS configuration
      - CDN setup
  - Monitoring infrastructure:
    - Logging systems
    - Metrics collection
    - Tracing systems
    - Alerting rules
    - Dashboards

- Phase 2: Performance Analysis

  - Application performance:
    - Response time analysis:
      - API response times
      - Page load times
      - Transaction times
      - Query performance
      - Batch job duration
    - Throughput analysis:
      - Requests per second
      - Concurrent users
      - Data processing rates
      - Message queue throughput
      - Batch processing speed
    - Error rate analysis:
      - HTTP error rates
      - Application errors
      - Timeout frequencies
      - Retry patterns
      - Circuit breaker trips
  - Infrastructure performance:
    - Resource utilization:
      - CPU usage patterns
      - Memory consumption
      - Disk I/O rates
      - Network bandwidth
      - Container resource limits
    - Scalability analysis:
      - Auto-scaling behavior
      - Load distribution
      - Bottleneck identification
      - Capacity planning
      - Growth projections

- Phase 3: Reliability and Availability Analysis

  - System reliability:
    - Uptime metrics:
      - Service availability
      - Component uptime
      - Planned maintenance impact
      - Unplanned outages
      - Recovery times
    - Failure analysis:
      - Failure patterns
      - Root cause identification
      - Cascade failures
      - Recovery mechanisms
      - Resilience testing
  - Data integrity:
    - Backup verification
    - Replication status
    - Data consistency
    - Recovery testing
    - Archive integrity

- Phase 4: Security Operational Analysis

  - Access control review:
    - Authentication mechanisms
    - Authorization policies
    - API key management
    - Certificate status
    - Privilege escalation risks
  - Security monitoring:
    - Intrusion detection
    - Vulnerability scanning
    - Compliance monitoring
    - Audit log analysis
    - Incident response readiness
  - Data protection:
    - Encryption status
    - Data classification
    - PII handling
    - Compliance verification
    - Data retention policies

- Phase 5: Log and Trace Analysis

  - Log analysis:
    - Error pattern detection:
      - Recurring errors
      - Error clustering
      - Stack trace analysis
      - Error correlation
      - Root cause patterns
    - Performance patterns:
      - Slow query logs
      - Long-running transactions
      - Resource contention
      - Deadlock detection
      - Memory leak indicators
  - Distributed tracing:
    - Request flow analysis
    - Service latency breakdown
    - Dependency performance
    - Bottleneck identification
    - Cross-service optimization

- Phase 6: Cost and Efficiency Analysis
  - Resource optimization:
    - Right-sizing recommendations
    - Idle resource identification
    - Reserved capacity analysis
    - Spot instance opportunities
    - Storage optimization
  - Cost analysis:
    - Service cost breakdown
    - Cost trends
    - Budget compliance
    - Cost optimization opportunities
    - ROI analysis

operational_patterns:

# Common operational patterns to analyze

performance_patterns:
latency_spikes:
indicators: "P95 > 2x baseline"
investigation: "Trace analysis, resource correlation"
remediation: "Caching, query optimization, scaling"

    memory_leaks:
      indicators: "Gradual memory increase"
      investigation: "Heap dumps, allocation tracking"
      remediation: "Code fixes, container restarts"

    cascading_failures:
      indicators: "Multiple service failures"
      investigation: "Dependency analysis, timeout review"
      remediation: "Circuit breakers, retry policies"

reliability_patterns:
single_points_of_failure:
detection: "Dependency mapping"
impact: "Service availability risk"
mitigation: "Redundancy, load balancing"

    insufficient_monitoring:
      detection: "Coverage analysis"
      impact: "Blind spots in operations"
      mitigation: "Enhanced instrumentation"

analysis_methodologies:

# Systematic analysis approaches

top_down_analysis:
start: "User-facing metrics"
drill_down: "Component performance"
end: "Infrastructure metrics"

bottom_up_analysis:
start: "Infrastructure health"
build_up: "Service performance"
end: "User experience metrics"

comparative_analysis:
baseline: "Normal operation metrics"
comparison: "Current state"
identification: "Anomalies and degradation"

constraints:

- Analysis MUST be based on actual operational data
- Findings MUST be actionable and prioritized
- Performance impacts MUST be quantified
- Security risks MUST be assessed
- Cost implications MUST be calculated
- Recommendations MUST be feasible
- Documentation MUST reflect current state

output_format:
jupyter_structure: - Section 1: Executive Operational Summary - Section 2: System Inventory and Architecture - Section 3: Application Performance Analysis - Section 4: Container and Orchestration Analysis - Section 5: Infrastructure Performance Review - Section 6: Data Systems Operational Health - Section 7: Network Performance and Security - Section 8: Monitoring and Observability Assessment - Section 9: Log Analysis and Error Patterns - Section 10: Security Operational Review - Section 11: Reliability and Availability Metrics - Section 12: Cost and Efficiency Analysis - Section 13: Operational Risk Assessment - Section 14: Performance Optimization Opportunities - Section 15: Capacity Planning Recommendations - Section 16: Operational Excellence Roadmap - Section 17: Critical Issues and Remediation - Section 18: Continuous Improvement Plan

component_analysis_format: |
For each operational component:

````
Component ID: <OPS-CATEGORY-001>
Type: Application|Service|Container|Database|Network
Criticality: Critical|High|Medium|Low

    Component Details:
      Name: [Component name]
      Version: [Current version]
      Dependencies: [List of dependencies]
      Resources: [CPU, Memory, Storage]

    Performance Metrics:
      - Availability: 99.9% (30-day)
      - Response Time: P50: Xms, P95: Yms, P99: Zms
      - Throughput: X requests/second
      - Error Rate: X% (4xx: Y%, 5xx: Z%)
      - Resource Usage: CPU: X%, Memory: Y%, Disk: Z%

    Health Status:
      Overall: Healthy|Degraded|Critical
      Issues:
        - Issue 1: [Description, Impact, Started]
        - Issue 2: [Description, Impact, Started]

    Log Analysis:
      - Error Patterns: [Common errors]
      - Warning Trends: [Increasing/Stable/Decreasing]
      - Notable Events: [Recent incidents]

    Optimization Opportunities:
      - Opportunity 1: [Description, Expected Impact]
      - Opportunity 2: [Description, Expected Impact]

    Risks:
      - Risk 1: [Description, Probability, Impact]
      - Risk 2: [Description, Probability, Impact]

    Recommendations:
      Immediate: [Critical actions needed]
      Short-term: [1-2 week improvements]
      Long-term: [Strategic improvements]
    ```

operational_dashboard_format: | - System health overview heatmap - Performance trends (7d, 30d, 90d) - Error rate visualization - Resource utilization charts - Cost breakdown pie charts - Dependency network diagram - Alert frequency histogram

validation_criteria:
data_quality: "10 - Comprehensive operational data collected"
analysis_depth: "10 - All layers thoroughly analyzed"
issue_identification: "10 - All operational issues found"
root_cause_accuracy: "10 - True causes identified"
recommendation_quality: "10 - Actionable and prioritized"
risk_assessment: "10 - All risks identified and quantified"
optimization_value: "10 - High-impact opportunities found"

final_deliverables:
naming_convention: "MANDATORY: ALL operational analysis output files MUST use reverse date stamp format: YYYY-MM-DD-HHMMSS"
date_stamp_format: "{{YYYY}}-{{MM}}-{{DD}}-{{HHMMSS}}"
example_format: "2025-01-22-085549"

required_outputs: - "Operational_Analysis_Report-{{YYYY-MM-DD-HHMMSS}}.ipynb (comprehensive operational analysis)" - "System_Inventory-{{YYYY-MM-DD-HHMMSS}}.xlsx (complete component list)" - "Performance_Dashboard-{{YYYY-MM-DD-HHMMSS}}.html (interactive metrics)" - "Error_Pattern_Analysis-{{YYYY-MM-DD-HHMMSS}}.md (log insights and patterns)" - "Optimization_Roadmap-{{YYYY-MM-DD-HHMMSS}}.md (improvement plan)" - "Risk_Register-{{YYYY-MM-DD-HHMMSS}}.md (operational risks assessment)" - "Cost_Analysis_Report-{{YYYY-MM-DD-HHMMSS}}.pdf (financial insights)" - "Monitoring_Gaps-{{YYYY-MM-DD-HHMMSS}}.md (observability improvements)" - "Incident_Playbooks-{{YYYY-MM-DD-HHMMSS}}.md (operational procedures)" - "Executive_Summary-{{YYYY-MM-DD-HHMMSS}}.pdf (key findings)"

date_stamp_requirements: - "MANDATORY: Use current UTC timestamp for all operational analysis output files" - "MANDATORY: Format as YYYY-MM-DD-HHMMSS (reverse chronological order)" - "MANDATORY: Include date stamp in ALL operational analysis deliverable filenames" - "MANDATORY: Use consistent date stamp across all operational analysis outputs" - "FORBIDDEN: Creating operational analysis files without proper date stamps" - "FORBIDDEN: Using different date formats within same operational analysis session"

# Operational Health Scoring

health_scoring:
performance_score:
excellent: "> 95% SLA compliance"
good: "90-95% SLA compliance"
fair: "80-90% SLA compliance"
poor: "< 80% SLA compliance"

reliability_score:
calculation: "(Uptime % _ MTTR score _ Error rate score) / 3"
weights:
uptime: 0.5
mttr: 0.3
errors: 0.2

efficiency_score:
factors: - Resource utilization - Cost per transaction - Scaling efficiency - Waste reduction

# Operational Patterns Recognition

pattern_detection:
performance_patterns: - Peak load patterns - Seasonal variations - Growth trends - Degradation patterns

failure_patterns: - Recurring incidents - Cascade failures - Recovery patterns - Root cause clusters

cost_patterns: - Spending trends - Waste patterns - Optimization opportunities - Budget variances

# Continuous Monitoring Setup

monitoring_recommendations:
metrics_to_add: - Business KPIs - User experience metrics - Cost metrics - Security metrics

alerts_to_configure: - SLA breaches - Error rate spikes - Resource exhaustion - Security events

dashboards_to_create: - Executive overview - Operations center - Developer insights - Cost management

# Execution Workflow

execution_steps: |

1. Discover and inventory all operational components
2. Collect logs, metrics, and traces
3. Analyze application performance
4. Review infrastructure health
5. Assess reliability and availability
6. Examine security operations
7. Analyze logs for patterns
8. Calculate costs and efficiency
9. Identify optimization opportunities
10. Generate comprehensive operational report
````
