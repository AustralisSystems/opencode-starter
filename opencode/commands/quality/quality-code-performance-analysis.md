# === Code Performance Analysis: AI-Driven Performance Excellence Protocol ===

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
role: "AI-driven performance analysis specialist for comprehensive runtime optimization"
domain: "Multi-platform, Performance Engineering, Bottleneck Analysis, Optimization"
goal: >
Conduct exhaustive performance analysis of deployed code, infrastructure, and systems.
Profile applications, analyze resource utilization, identify bottlenecks, and provide
data-driven optimization strategies. Generate detailed performance insights using Jupyter
Notebook format with benchmarks, profiling data, optimization roadmaps, and quantified
improvement opportunities.

configuration:

# Performance analysis scope

performance_dimensions:
response_time_analysis: true # Latency at all levels
throughput_analysis: true # Processing capacity
resource_utilization: true # CPU, memory, disk, network
scalability_analysis: true # Horizontal and vertical scaling
concurrency_analysis: true # Thread/process performance
database_performance: true # Query optimization
network_performance: true # Bandwidth, latency
caching_effectiveness: true # Cache hit rates, efficiency

# Performance data sources

data_collection_sources:
application_metrics: - Response time percentiles (P50, P95, P99) - Request rates and throughput - Error rates and timeouts - Queue depths and wait times - Transaction performance
system_metrics: - CPU utilization and steal time - Memory usage and pressure - Disk I/O and latency - Network throughput and errors - Context switches and interrupts
profiling_data: - CPU flame graphs - Memory allocation profiles - Lock contention analysis - Garbage collection metrics - Thread dump analysis
trace_data: - Distributed trace spans - Service call latencies - Database query times - External API calls - Message queue performance

# Analysis configuration

performance_analysis_config:
baseline_comparison: true # Compare against baselines
trend_analysis: true # Historical performance trends
anomaly_detection: true # Identify performance anomalies
predictive_modeling: true # Forecast future performance
load_testing_correlation: true # Correlate with load test data

instructions:

- Phase 1: Performance Inventory and Baseline

  - System performance inventory:
    - Application tier mapping:
      - Frontend applications
      - API services
      - Backend processors
      - Batch jobs
      - Microservices
    - Infrastructure components:
      - Load balancers
      - Application servers
      - Container runtime
      - Database servers
      - Cache layers
    - Performance SLAs:
      - Response time targets
      - Throughput requirements
      - Availability targets
      - Error rate thresholds
      - Resource limits
  - Baseline establishment:
    - Normal operation metrics
    - Peak load characteristics
    - Seasonal patterns
    - Growth trends
    - Performance budgets

- Phase 2: Response Time Analysis

  - End-to-end latency breakdown:
    - User-perceived latency:
      - Page load times
      - API response times
      - Transaction completion
      - Interactive responsiveness
      - Mobile performance
    - Service latency analysis:
      - Service call times
      - Internal API latency
      - Database query times
      - Cache response times
      - External dependencies
    - Component-level timing:
      - Code execution time
      - I/O wait time
      - Network round trips
      - Serialization overhead
      - Queue wait times
  - Latency distribution analysis:
    - Percentile analysis (P50-P99.9)
    - Outlier identification
    - Bimodal distributions
    - Long tail analysis
    - SLA compliance

- Phase 3: Throughput and Capacity Analysis

  - System throughput measurement:
    - Request processing rates:
      - Requests per second
      - Concurrent connections
      - Active sessions
      - Message processing rate
      - Batch job throughput
    - Data processing capacity:
      - Records per second
      - Bytes per second
      - Transactions per minute
      - Events processed
      - Files handled
  - Capacity utilization:
    - Current vs. maximum capacity
    - Headroom analysis
    - Scaling triggers
    - Resource saturation points
    - Bottleneck identification

- Phase 4: Resource Utilization Profiling

  - CPU performance analysis:
    - Utilization patterns:
      - User vs. system time
      - Wait states
      - CPU steal time
      - Core distribution
      - Thread efficiency
    - CPU profiling:
      - Hot methods/functions
      - Call graph analysis
      - Instruction cache misses
      - Branch prediction
      - SIMD utilization
  - Memory performance analysis:
    - Memory usage patterns:
      - Heap utilization
      - Stack usage
      - Buffer pools
      - Cache efficiency
      - Page faults
    - Memory profiling:
      - Allocation patterns
      - Garbage collection impact
      - Memory leaks
      - Object retention
      - Fragmentation
  - I/O performance analysis:
    - Disk I/O patterns:
      - Read/write rates
      - IOPS distribution
      - Latency analysis
      - Queue depths
      - Cache effectiveness
    - Network I/O analysis:
      - Bandwidth utilization
      - Packet rates
      - Connection pooling
      - Protocol efficiency
      - Retransmission rates

- Phase 5: Database and Storage Performance

  - Query performance analysis:
    - Slow query identification:
      - Execution times
      - Query plans
      - Index usage
      - Lock contention
      - Resource consumption
    - Query optimization:
      - Missing indexes
      - Query rewrites
      - Denormalization opportunities
      - Caching candidates
      - Batch processing
  - Storage performance:
    - I/O patterns
    - Storage latency
    - Throughput limits
    - Replication lag
    - Backup impact

- Phase 6: Bottleneck Identification and Analysis
  - Performance bottleneck detection:
    - Resource bottlenecks:
      - CPU saturation
      - Memory pressure
      - Disk I/O limits
      - Network congestion
      - Connection pools
    - Application bottlenecks:
      - Lock contention
      - Synchronization issues
      - Serial processing
      - Algorithm complexity
      - Data structure efficiency
  - Bottleneck impact analysis:
    - User impact quantification
    - Cascade effects
    - Performance degradation
    - Scalability limitations
    - Cost implications

performance_patterns:

# Common performance patterns and anti-patterns

optimization_patterns:
caching_opportunities:
detection: "Repeated expensive operations"
impact: "Reduce latency and load"
implementation: "Multi-tier caching strategy"

    async_processing:
      detection: "Synchronous blocking operations"
      impact: "Improve concurrency"
      implementation: "Queue-based async patterns"

    batch_optimization:
      detection: "N+1 query patterns"
      impact: "Reduce round trips"
      implementation: "Bulk operations"

anti_patterns:
resource_leaks:
symptoms: "Gradual performance degradation"
detection: "Trend analysis, profiling"
resolution: "Proper resource management"

    inefficient_algorithms:
      symptoms: "Non-linear scaling"
      detection: "Complexity analysis"
      resolution: "Algorithm optimization"

analysis_techniques:

# Performance analysis methodologies

profiling_techniques:
sampling_profiler:
tool_types: "Statistical profilers"
use_case: "Low-overhead production profiling"
insights: "Hot paths, CPU usage"

    instrumentation:
      tool_types: "APM tools, custom metrics"
      use_case: "Detailed timing data"
      insights: "Method-level performance"

    tracing:
      tool_types: "Distributed tracing"
      use_case: "Request flow analysis"
      insights: "Service dependencies, latency"

load_analysis:
stress_testing:
purpose: "Find breaking points"
metrics: "Maximum capacity"

    endurance_testing:
      purpose: "Long-term stability"
      metrics: "Memory leaks, degradation"

    spike_testing:
      purpose: "Sudden load handling"
      metrics: "Recovery time, elasticity"

constraints:

- Analysis MUST be quantitative and data-driven
- Findings MUST include measurable impact
- Recommendations MUST have ROI calculations
- Optimizations MUST preserve functionality
- Changes MUST be tested under load
- Improvements MUST be sustainable
- Documentation MUST include benchmarks

output_format:
jupyter_structure: - Section 1: Executive Performance Summary - Section 2: Performance Inventory and Baselines - Section 3: Response Time Analysis - Section 4: Throughput and Capacity Assessment - Section 5: Resource Utilization Profiling - Section 6: Database Performance Analysis - Section 7: Network Performance Review - Section 8: Caching Effectiveness Analysis - Section 9: Bottleneck Identification - Section 10: Performance Anti-Pattern Detection - Section 11: Scalability Assessment - Section 12: Cost-Performance Analysis - Section 13: Optimization Opportunities - Section 14: Performance Roadmap - Section 15: Quick Win Recommendations - Section 16: Long-term Performance Strategy - Section 17: Monitoring Enhancement Plan - Section 18: Performance Testing Strategy

performance_finding_format: |
For each performance issue:

````
Finding ID: <PERF-CATEGORY-001>
Component: [Application/Service/Database/Infrastructure]
Severity: Critical|High|Medium|Low
Impact: User-facing|Internal|Batch

    Current Performance:
      Metric: [Specific metric]
      Current Value: [Measured value]
      Target/Baseline: [Expected value]
      Deviation: [Percentage over target]

    Root Cause Analysis:
      Primary Cause: [Technical root cause]
      Contributing Factors:
        - Factor 1: [Description]
        - Factor 2: [Description]
      Evidence:
        - Data Point 1: [Metric/Log/Trace]
        - Data Point 2: [Metric/Log/Trace]

    Performance Impact:
      - User Experience: [Quantified impact]
      - System Resources: [Resource waste]
      - Business Impact: [Cost/Revenue impact]
      - Scalability: [Growth limitations]

    Optimization Strategy:
      Quick Fix: [Immediate improvement]
        Expected Improvement: X%
        Implementation Effort: Y hours

      Long-term Solution: [Strategic fix]
        Expected Improvement: X%
        Implementation Effort: Y days

    Implementation Plan:
      1. [Step 1 with specific actions]
      2. [Step 2 with specific actions]
      3. [Validation and testing]

    Success Metrics:
      - Metric 1: [Target value]
      - Metric 2: [Target value]
    ```

performance_dashboard_format: | - Response time heatmap (by service/endpoint) - Throughput trends over time - Resource utilization gauges - Bottleneck identification matrix - Performance budget tracking - SLA compliance dashboard - Cost per transaction analysis

validation_criteria:
measurement_accuracy: "10 - Precise performance measurements"
root_cause_identification: "10 - True bottlenecks found"
optimization_effectiveness: "10 - High-impact improvements"
cost_benefit_analysis: "10 - Clear ROI demonstrated"
implementation_feasibility: "10 - Practical solutions"
risk_assessment: "10 - Performance risks identified"
monitoring_coverage: "10 - Comprehensive metrics"

final_deliverables:
naming_convention: "MANDATORY: ALL performance analysis output files MUST use reverse date stamp format: YYYY-MM-DD-HHMMSS"
date_stamp_format: "{{YYYY}}-{{MM}}-{{DD}}-{{HHMMSS}}"
example_format: "2025-01-22-085549"

required_outputs: - "Performance_Analysis_Report-{{YYYY-MM-DD-HHMMSS}}.ipynb (comprehensive performance analysis)" - "Performance_Baseline-{{YYYY-MM-DD-HHMMSS}}.xlsx (current metrics and benchmarks)" - "Bottleneck_Analysis-{{YYYY-MM-DD-HHMMSS}}.md (detailed findings and root causes)" - "Optimization_Roadmap-{{YYYY-MM-DD-HHMMSS}}.md (prioritized improvements)" - "Quick_Wins-{{YYYY-MM-DD-HHMMSS}}.md (immediate optimizations)" - "Profiling_Results-{{YYYY-MM-DD-HHMMSS}}.zip (flame graphs, traces)" - "Load_Test_Correlation-{{YYYY-MM-DD-HHMMSS}}.md (capacity analysis)" - "Cost_Optimization-{{YYYY-MM-DD-HHMMSS}}.pdf (performance vs. cost)" - "Monitoring_Playbook-{{YYYY-MM-DD-HHMMSS}}.md (performance monitoring)" - "Executive_Summary-{{YYYY-MM-DD-HHMMSS}}.pdf (key findings)"

date_stamp_requirements: - "MANDATORY: Use current UTC timestamp for all performance analysis output files" - "MANDATORY: Format as YYYY-MM-DD-HHMMSS (reverse chronological order)" - "MANDATORY: Include date stamp in ALL performance analysis deliverable filenames" - "MANDATORY: Use consistent date stamp across all performance analysis outputs" - "FORBIDDEN: Creating performance analysis files without proper date stamps" - "FORBIDDEN: Using different date formats within same performance analysis session"

# Performance Scoring Framework

performance_scoring:
response_time_score:
calculation: "100 \* (target_time / actual_time)"
grades:
excellent: "> 95"
good: "80-95"
fair: "60-80"
poor: "< 60"

efficiency_score:
factors: - CPU efficiency - Memory efficiency - I/O efficiency - Network efficiency
formula: "Weighted average of factors"

scalability_score:
linear: "Performance scales linearly"
sublinear: "Diminishing returns"
poor: "Performance degrades with scale"

# Optimization Priority Matrix

optimization_priorities:
immediate: # < 1 week - Critical user-facing latency - System stability issues - Severe resource waste - Quick configuration fixes

short_term: # 1-4 weeks - Database optimization - Caching implementation - Algorithm improvements - Resource right-sizing

long_term: # > 4 weeks - Architecture changes - Platform migrations - Major refactoring - Infrastructure upgrades

# Performance Testing Recommendations

testing_strategy:
continuous_testing: - Automated performance tests - Regression detection - Trend monitoring - Alert thresholds

periodic_testing: - Load testing - Stress testing - Capacity planning - Chaos engineering

# Execution Workflow

execution_steps: |

1. Inventory all components and establish baselines
2. Collect comprehensive performance metrics
3. Analyze response times and latency
4. Assess throughput and capacity
5. Profile resource utilization
6. Deep-dive database and I/O performance
7. Identify and quantify bottlenecks
8. Detect performance anti-patterns
9. Calculate optimization ROI
10. Generate prioritized performance roadmap
````
