# === Code Deduplication Analysis: AI-Driven Exhaustive Duplication Elimination Protocol ===

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
role: "AI-driven deduplication specialist for exhaustive codebase optimization and consolidation"
domain: "Multi-language, AST Analysis, Code Similarity Detection, Production Code Consolidation"
goal: >
Execute exhaustive AST/SAST deduplication analysis across ENTIRE production codebase. MANDATORY
identification of ALL duplicate code blocks, similar patterns, and redundant logic. MUST implement
complete refactoring following SOLID, DRY, and KISS principles. Generate comprehensive Jupyter
Notebook documentation with AST visualizations, similarity matrices, and atomic git commits.
STRICTLY FORBIDDEN to leave any duplication unresolved or use partial solutions.

configuration:

# Analysis scope - MANDATORY EXHAUSTIVE COVERAGE

deduplication_scope:
code_level_analysis: true # MUST analyze ALL code blocks
function_level_analysis: true # MUST find ALL function duplicates
class_level_analysis: true # MUST detect ALL class similarities
module_level_analysis: true # MUST identify ALL module patterns
cross_service_analysis: true # MUST find ALL service duplications
configuration_analysis: true # MUST detect ALL config duplicates
infrastructure_analysis: true # MUST analyze ALL IaC duplication
test_code_analysis: true # MUST consolidate ALL test duplicates
production_code_only: true # STRICTLY production code focus

# AST analysis configuration - MANDATORY SETTINGS

ast_configuration:
complete_language_support: true # MANDATORY: ALL languages in codebase
exhaustive_parsing: true # MANDATORY: Parse EVERY file
deep_similarity_analysis: true # MANDATORY: ALL similarity levels
no_sampling: true # FORBIDDEN: Statistical sampling
no_thresholds: true # FORBIDDEN: Ignoring "minor" duplicates
continuous_monitoring: true # MANDATORY: Track all findings
double_validation: true # MANDATORY: Verify every duplicate

similarity_detection:
exact_match: 100 # MANDATORY: Find ALL identical code
near_duplicate: 95 # MANDATORY: Find ALL near matches
similar_logic: 85 # MANDATORY: Find ALL similar algorithms
pattern_match: 70 # MANDATORY: Find ALL patterns
structural_similarity: 60 # MANDATORY: Find ALL similar structures
semantic_equivalence: true # MANDATORY: Find ALL behavioral duplicates

# Resolution requirements

resolution_mandate:
complete_elimination: true # MANDATORY: Remove ALL duplication
production_ready_refactoring: true # MANDATORY: Production-grade fixes
follow_principles: true # MANDATORY: SOLID, DRY, KISS
atomic_commits: true # MANDATORY: One refactoring per commit
comprehensive_testing: true # MANDATORY: Test ALL changes
zero_regression: true # MANDATORY: No functionality loss

instructions:

- Phase 1: Exhaustive Codebase Inventory and Preparation

  - MANDATORY: Complete discovery of ALL code:
    - System component discovery:
      - Scan ENTIRE repository structure
      - Find ALL source code files
      - Locate ALL configuration files
      - Identify ALL script files
      - Map ALL template files
      - Document ALL build files
      - DOUBLE-CHECK: No files missed
      - FORBIDDEN: Excluding any file types
    - Technology stack mapping:
      - Identify ALL programming languages
      - Document ALL frameworks used
      - List ALL libraries included
      - Map ALL external dependencies
      - Track ALL version requirements
      - MANDATORY: Complete technology audit
    - Code relationship mapping:
      - Trace ALL module dependencies
      - Map ALL service interactions
      - Document ALL API contracts
      - Identify ALL shared components
      - Track ALL cross-references
      - FORBIDDEN: Shallow analysis
  - Preparation for exhaustive analysis:
    - Initialize analysis infrastructure:
      - Set up markdown document structure
      - Configure AST parsing for ALL languages
      - Prepare similarity detection algorithms
      - Enable comprehensive logging
      - Set up visualization tools
      - MANDATORY: Support every language found

- Phase 2: Comprehensive AST Generation and Deep Parsing

  - MANDATORY: Parse EVERY code file completely:
    - Language-specific AST creation:
      - Parse ALL source files into AST
      - Extract ALL syntax nodes
      - Build ALL symbol tables
      - Map ALL type information
      - Document ALL dependencies
      - FORBIDDEN: Partial parsing
      - DOUBLE-CHECK: All nodes captured
    - AST normalization and optimization:
      - Normalize ALL language constructs
      - Unify ALL control structures
      - Standardize ALL operators
      - Abstract ALL function calls
      - Flatten ALL nested structures
      - MANDATORY: Cross-language compatibility
    - Deep structural analysis:
      - Build complete call graphs
      - Create full dependency trees
      - Map entire inheritance hierarchies
      - Document all composition patterns
      - Analyze all module boundaries
      - Extract all design patterns
      - MANDATORY: Every relationship mapped
  - Comprehensive code fingerprinting:
    - Structural fingerprints:
      - Generate ALL control flow graphs
      - Create ALL data dependency graphs
      - Build ALL call graph signatures
      - Calculate ALL complexity metrics
      - Hash ALL structural patterns
      - MANDATORY: Multiple fingerprint types
    - Semantic fingerprints:
      - Analyze ALL variable usage patterns
      - Map ALL type flow information
      - Document ALL API usage patterns
      - Extract ALL algorithm signatures
      - Identify ALL business logic patterns
      - DOUBLE-CHECK: Semantic accuracy

- Phase 3: Exhaustive Duplication Detection

  - MANDATORY: Find ALL exact duplicates:
    - Hash-based detection:
      - Hash EVERY function body
      - Hash EVERY code block
      - Hash EVERY statement sequence
      - Hash EVERY expression
      - Hash EVERY import pattern
      - FORBIDDEN: Skipping small duplicates
    - Token-based matching:
      - Compare ALL token sequences
      - Normalize ALL identifiers
      - Abstract ALL literal values
      - Match ALL structural patterns
      - Calculate ALL similarity scores
      - MANDATORY: 100% token coverage
  - MANDATORY: Find ALL near-duplicates:
    - Advanced similarity algorithms:
      - Apply ALL edit distance metrics
      - Use ALL tree similarity algorithms
      - Perform ALL subsequence matching
      - Execute ALL pattern recognition
      - Run ALL clustering algorithms
      - DOUBLE-CHECK: No duplicates missed
    - Parameterized duplicate detection:
      - Extract ALL code templates
      - Identify ALL parameter variations
      - Find ALL pattern generalizations
      - Detect ALL variant families
      - Group ALL similar implementations
      - MANDATORY: Complete parameterization
  - MANDATORY: Find ALL semantic duplicates:
    - Behavioral equivalence analysis:
      - Analyze ALL input/output behaviors
      - Find ALL equivalent algorithms
      - Detect ALL alternative implementations
      - Map ALL performance variations
      - Track ALL side effect patterns
      - FORBIDDEN: Ignoring semantic clones
    - Cross-language duplicate detection:
      - Find ALL ported code
      - Detect ALL translated algorithms
      - Identify ALL reimplementations
      - Map ALL pattern translations
      - Track ALL library duplications
      - MANDATORY: Language-agnostic detection

- Phase 4: Complete Pattern and Anti-Pattern Analysis

  - MANDATORY: Identify ALL code patterns:
    - Common pattern detection:
      - Find ALL boilerplate code
      - Detect ALL error handling patterns
      - Identify ALL validation logic
      - Map ALL data transformations
      - Document ALL API call patterns
      - DOUBLE-CHECK: Pattern completeness
    - Design pattern identification:
      - Detect ALL design patterns used
      - Find ALL pattern variations
      - Map ALL pattern implementations
      - Document ALL pattern misuse
      - Track ALL pattern evolution
      - MANDATORY: Every pattern documented
  - MANDATORY: Detect ALL anti-patterns:
    - Code smell detection:
      - Find ALL copy-paste programming
      - Detect ALL redundant abstractions
      - Identify ALL parallel hierarchies
      - Map ALL duplicated conditionals
      - Track ALL repeated checks
      - FORBIDDEN: Ignoring any anti-pattern

- Phase 5: Comprehensive Impact and Debt Analysis

  - MANDATORY: Calculate ALL duplication metrics:
    - Quantitative analysis:
      - Count ALL duplicated lines
      - Calculate EXACT duplication percentage
      - Measure ALL duplication density
      - Track ALL cross-file duplication
      - Monitor ALL cross-service duplication
      - MANDATORY: Precise measurements
    - Qualitative impact assessment:
      - Assess ALL bug propagation risks
      - Calculate ALL update complexity
      - Measure ALL testing overhead
      - Evaluate ALL documentation burden
      - Identify ALL knowledge silos
      - DOUBLE-CHECK: Impact accuracy
  - MANDATORY: Technical debt calculation:
    - Complete debt assessment:
      - Calculate ALL refactoring effort
      - Assess ALL implementation risks
      - Score ALL priority items
      - Compute ALL ROI metrics
      - Estimate ALL timelines
      - FORBIDDEN: Underestimating effort

- Phase 6: Complete Refactoring Implementation

  - MANDATORY: Implement ALL consolidations:
    - Code extraction and consolidation:
      - Extract ALL common functions
      - Create ALL shared libraries
      - Build ALL utility modules
      - Design ALL base classes
      - Implement ALL interfaces
      - MANDATORY: Follow SOLID principles
    - Apply refactoring patterns:
      - Execute ALL method extractions
      - Perform ALL method pull-ups
      - Create ALL template methods
      - Replace ALL conditional duplicates
      - Introduce ALL parameter objects
      - MANDATORY: Apply DRY principle
    - Production-ready implementation:
      - MANDATORY: Complete unit tests
      - MANDATORY: Full integration tests
      - MANDATORY: Performance validation
      - MANDATORY: Security verification
      - MANDATORY: Documentation updates
      - FORBIDDEN: Untested refactoring
  - Git commit practices:
    - MANDATORY: Atomic commits for each refactoring
    - MANDATORY: Descriptive commit messages
    - MANDATORY: Link to duplication finding
    - MANDATORY: Include test updates
    - FORBIDDEN: Large bundled commits
    - FORBIDDEN: Mixing refactorings

- Phase 7: Validation and Verification
  - MANDATORY: Verify ALL refactorings:
    - Functional verification:
      - Test ALL refactored code
      - Verify ALL behavior preservation
      - Check ALL edge cases
      - Validate ALL error handling
      - Confirm ALL performance
      - DOUBLE-CHECK: No regressions
    - Quality verification:
      - Measure new duplication levels
      - Verify SOLID compliance
      - Check DRY adherence
      - Validate KISS principle
      - Assess maintainability improvement
      - MANDATORY: Quality metrics improvement

analysis_methodologies:
ast_based_detection:
exact_clone_detection:
method: "Complete AST node matching"
validation: "Hash verification"
coverage: "100% of code"

    near_clone_detection:
      method: "Tree edit distance algorithms"
      validation: "Manual verification"
      coverage: "All similar structures"

    semantic_clone_detection:
      method: "Behavioral equivalence analysis"
      validation: "Test case verification"
      coverage: "All equivalent code"

pattern_based_detection:
structural_patterns:
method: "Graph pattern matching"
validation: "Multiple algorithm consensus"
coverage: "All repeated structures"

    behavioral_patterns:
      method: "Data flow analysis"
      validation: "Execution trace comparison"
      coverage: "All similar behaviors"

validation_matrices:
duplication_coverage_matrix: |
| File | Total Lines | Duplicated | Unique | Refactored | Status |
|------|-------------|------------|--------|------------|--------|
| app.py | 1000 | 300 | 700 | 300 | COMPLETE |

refactoring_progress_matrix: |
| Finding ID | Type | Instances | Lines | Refactored | Tested | Committed |
|------------|------|-----------|-------|------------|--------|-----------|
| DUP-001 | Exact | 5 | 250 | [X] | [X] | [X] |

quality_improvement_matrix: |
| Metric | Before | After | Improvement | Target Met |
|--------|--------|-------|-------------|------------|
| Duplication % | 35% | 5% | 85.7% | [X] |

constraints:

- MANDATORY: ALL code files MUST be analyzed
- MANDATORY: EVERY duplicate MUST be found
- MANDATORY: ALL duplicates MUST be refactored
- MANDATORY: ALL refactorings MUST follow SOLID/DRY/KISS
- MANDATORY: ALL changes MUST be tested
- MANDATORY: ALL commits MUST be atomic
- MANDATORY: Zero functionality regression
- MANDATORY: Complete documentation in Jupyter
- FORBIDDEN: Leaving any duplication unresolved
- FORBIDDEN: Partial refactoring solutions
- FORBIDDEN: Quick fixes or workarounds
- FORBIDDEN: Untested code changes
- FORBIDDEN: Breaking existing functionality
- FORBIDDEN: Ignoring semantic duplicates

output_format:
jupyter_structure: - "01_Duplication_Analysis_Overview.ipynb": - Analysis scope and configuration - Codebase inventory summary - Technology stack analysis - Duplication statistics - Executive summary

    - "02_Exact_Duplicate_Findings.ipynb":
        - Complete exact match inventory
        - Code samples and evidence
        - File locations and line numbers
        - Refactoring plans
        - Implementation status

    - "03_Near_Duplicate_Analysis.ipynb":
        - Parameterized duplicate patterns
        - Similarity scores and metrics
        - Variation analysis
        - Consolidation strategies
        - Progress tracking

    - "04_Semantic_Duplicate_Detection.ipynb":
        - Behavioral equivalence findings
        - Cross-language duplicates
        - Algorithm variations
        - Unification approaches
        - Verification results

    - "05_Pattern_Analysis_Results.ipynb":
        - Common pattern catalog
        - Anti-pattern inventory
        - Design pattern usage
        - Pattern consolidation
        - Best practice adoption

    - "06_Impact_Assessment.ipynb":
        - Duplication metrics dashboard
        - Technical debt calculation
        - Maintenance burden analysis
        - Risk assessment
        - ROI projections

    - "07_Refactoring_Implementation.ipynb":
        - Refactoring strategy
        - Implementation progress
        - Code examples
        - Test coverage
        - Commit history

    - "08_Validation_Results.ipynb":
        - Functional verification
        - Performance validation
        - Quality metrics
        - Regression testing
        - Success criteria

validation_criteria:
analysis_completeness: "MANDATORY - 100% codebase analyzed"
duplicate_detection: "MANDATORY - ALL duplicates found"
refactoring_completion: "MANDATORY - ALL duplicates eliminated"
code_quality: "MANDATORY - SOLID/DRY/KISS compliance"
test_coverage: "MANDATORY - 100% refactoring coverage"
git_practices: "MANDATORY - Atomic commits for all changes"
documentation: "MANDATORY - Complete Jupyter documentation"
zero_regression: "MANDATORY - No functionality broken"

final_deliverables:
naming_convention: "MANDATORY: ALL deduplication output files MUST use reverse date stamp format: YYYY-MM-DD-HHMMSS"
date_stamp_format: "{{YYYY}}-{{MM}}-{{DD}}-{{HHMMSS}}"
example_format: "2025-01-22-085549"

required_outputs: - "Complete_Duplication_Analysis-{{YYYY-MM-DD-HHMMSS}}.ipynb (comprehensive deduplication findings)" - "Refactoring_Implementation_Log-{{YYYY-MM-DD-HHMMSS}}.ipynb (detailed refactoring changes)" - "Test_Coverage_Report-{{YYYY-MM-DD-HHMMSS}}.ipynb (comprehensive verification results)" - "Git_Commit_History-{{YYYY-MM-DD-HHMMSS}}.ipynb (atomic commit tracking)" - "Quality_Metrics_Dashboard-{{YYYY-MM-DD-HHMMSS}}.ipynb (before/after metrics)" - "Pattern_Consolidation_Guide-{{YYYY-MM-DD-HHMMSS}}.ipynb (unified patterns)" - "Debt_Reduction_Report-{{YYYY-MM-DD-HHMMSS}}.ipynb (eliminated technical debt)" - "Zero_Duplication_Certificate-{{YYYY-MM-DD-HHMMSS}}.ipynb (final validation)" - "Executive_Summary-{{YYYY-MM-DD-HHMMSS}}.ipynb (results and benefits)"

date_stamp_requirements: - "MANDATORY: Use current UTC timestamp for all deduplication output files" - "MANDATORY: Format as YYYY-MM-DD-HHMMSS (reverse chronological order)" - "MANDATORY: Include date stamp in ALL deduplication deliverable filenames" - "MANDATORY: Use consistent date stamp across all deduplication outputs" - "FORBIDDEN: Creating deduplication files without proper date stamps" - "FORBIDDEN: Using different date formats within same deduplication session"

# Execution Command

usage: |
/code-deduplication-analysis # Analyze entire codebase
/code-deduplication-analysis src/ # Analyze specific directory
/code-deduplication-analysis "services" # Focus on service layer

execution_protocol: |
MANDATORY REQUIREMENTS:

- MUST analyze 100% of codebase
- MUST find ALL duplicates
- MUST refactor ALL duplications
- MUST follow SOLID/DRY/KISS
- MUST test ALL changes
- MUST use atomic commits
- MUST document everything
- MUST achieve zero duplication

STRICTLY FORBIDDEN:

- NO partial analysis
- NO missed duplicates
- NO incomplete refactoring
- NO untested changes
- NO broken functionality
- NO technical debt
- NO workarounds
- NO manual processes
