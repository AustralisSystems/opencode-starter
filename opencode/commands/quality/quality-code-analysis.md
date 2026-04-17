# === Code Quality Analysis: Comprehensive Codebase Quality Assessment & Best Practices Analysis Protocol ===

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

### **CODE QUALITY ANALYSIS MANDATE - CRITICAL FOCUS**

**THIS COMMAND IS FOR COMPREHENSIVE CODE QUALITY ANALYSIS:**

- **MUST:** Perform comprehensive codebase quality assessment against industry standards
- **MUST:** Analyze SOLID principles compliance and design patterns usage
- **MUST:** Detect anti-patterns and code smells systematically
- **MUST:** Assess security best practices and performance patterns
- **FORBIDDEN:** Superficial or incomplete quality analysis
- **FORBIDDEN:** Missing critical quality issues or anti-patterns
- **FORBIDDEN:** Analysis without proper industry standard compliance
- **MUST:** Output analysis documentation in markdown documents with timestamps

**CODE QUALITY ANALYSIS FOCUS AREAS:**

- Comprehensive SOLID principles compliance assessment
- Design patterns usage and implementation analysis
- Anti-pattern detection and code smell identification
- Security best practices and vulnerability assessment
- Performance patterns and optimization opportunities
- Clean code principles and maintainability metrics

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `quality-code-analysis-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for codebase_path, analysis_scope, quality_framework
3. **FOLLOW PROTOCOL**: Execute all phases according to the quality analysis protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive analysis documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% code quality analysis completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "quality-code-analysis-prompt"
arguments:
  codebase_path: "[root directory of codebase to analyze]"
  analysis_scope: "[comprehensive|focused|security-focused|performance-focused|patterns-focused]"
  quality_framework: "[solid|clean-code|security-first|performance-first|comprehensive]"
  analysis_depth: "[optional: surface|detailed|comprehensive|enterprise]"
  pattern_analysis: "[optional: creational|structural|behavioral|all-patterns]"
  security_focus: "[optional: vulnerabilities|best-practices|compliance|comprehensive]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All code quality analysis phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive codebase quality assessment completed
- [ ] SOLID principles compliance analyzed for all components (timestamped)
- [ ] Design patterns usage and implementation assessed (timestamped)
- [ ] Anti-patterns and code smells detected systematically (timestamped)
- [ ] Security best practices and vulnerabilities analyzed (timestamped)
- [ ] Performance patterns and optimization opportunities identified (timestamped)
- [ ] Clean code principles and maintainability metrics calculated (timestamped)
- [ ] Quality metrics and scoring generated (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL CODE QUALITY ANALYSIS OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All analysis deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All quality assessment documentation includes precise timestamps
- [ ] All SOLID principles analysis includes timestamp documentation
- [ ] All design patterns analysis reports include proper date stamps
- [ ] All anti-pattern detection follows consistent date stamp format
- [ ] All security analysis documentation includes timestamps
- [ ] All performance assessment includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating analysis files without proper reverse date stamps
- Using inconsistent date formats within same analysis session
- Missing timestamps in analysis documentation

### **CODE QUALITY ANALYSIS DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/analysis/quality/Analysis_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive analysis report and findings
2. **`./project/docs/analysis/quality/Findings_Recommendations_{YYYYMMDD-HHMMSS}.ipynb`** - Findings Recommendations
3. **`./project/docs/analysis/quality/Action_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Action Plan with detailed breakdown and timeline

**NEXT PHASE PREPARATION:**

```bash
# After analysis completion, execute improvements with:
/quality-improve-code [analysis-results] [improvement-scope]
/quality-fix-critical [analysis-results] [critical-issues]
/quality-fix-security [analysis-results] [security-vulnerabilities]

# Examples:
/quality-improve-code Code_Quality_Analysis-2025-09-22-085549.ipynb comprehensive
/quality-fix-critical Code_Quality_Analysis-2025-09-22-085549.ipynb solid-violations
/quality-fix-security Code_Quality_Analysis-2025-09-22-085549.ipynb vulnerabilities
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE CODE QUALITY ANALYSIS through the MCP prompt protocol. The comprehensive analysis logic is defined in `quality-code-analysis-prompt.yaml` and executed according to Model Context Protocol standards. Use subsequent quality improvement commands for remediation execution after analysis is complete and approved.

## Analysis Framework

### Phase 1: Component Inventory

Create a complete inventory of all system components:

1. **Applications & Entry Points**

   - Enumerate all executable scripts
   - Identify all CLI tools in `/tools/`
   - Map all test executables in `/tests/`
   - Document all utility scripts

2. **Service Architecture**

   - List all services in `/src/services/`
   - Map service dependencies
   - Document service interfaces
   - Identify service contracts

3. **Modules & Libraries**

   - Catalog all PowerShell modules (.psm1)
   - Map module exports and imports
   - Document helper functions
   - Identify shared libraries

4. **Data & Configuration**

   - List all configuration files
   - Map data schemas
   - Document credential stores
   - Identify environment configs

5. **Infrastructure Components**
   - Document API integrations
   - Map network communication
   - List external dependencies
   - Identify monitoring hooks

### Phase 2: SOLID Principles Analysis

1. **Single Responsibility Principle**

   ```
   For each class/module:
   - Count responsibilities
   - Measure cohesion
   - Identify violation patterns
   - Suggest refactoring opportunities
   ```

2. **Open/Closed Principle**

   ```
   Analyze extensibility:
   - Check for hardcoded logic
   - Evaluate configuration flexibility
   - Identify extension points
   - Review modification risks
   ```

3. **Liskov Substitution Principle**

   ```
   Review inheritance/interfaces:
   - Verify contract compliance
   - Check behavioral consistency
   - Identify type violations
   - Analyze polymorphism usage
   ```

4. **Interface Segregation Principle**

   ```
   Examine interfaces:
   - Check interface granularity
   - Identify fat interfaces
   - Review client dependencies
   - Suggest interface splitting
   ```

5. **Dependency Inversion Principle**
   ```
   Analyze dependencies:
   - Map concrete dependencies
   - Check abstraction usage
   - Identify tight coupling
   - Review injection patterns
   ```

### Phase 3: Design Patterns Analysis

1. **Creational Patterns**

   - Factory pattern usage
   - Singleton implementation review
   - Builder pattern identification
   - Prototype pattern analysis

2. **Structural Patterns**

   - Adapter pattern usage
   - Facade pattern implementation
   - Decorator pattern review
   - Proxy pattern analysis

3. **Behavioral Patterns**
   - Strategy pattern usage
   - Observer pattern implementation
   - Command pattern review
   - Template method analysis

### Phase 4: Anti-Pattern Detection

1. **Code Smells**

   - Long methods (>50 lines)
   - Large classes (>500 lines)
   - Feature envy
   - Data clumps
   - Primitive obsession
   - Switch statements abuse
   - Parallel inheritance hierarchies
   - Lazy classes
   - Middle man
   - Message chains

2. **Design Anti-Patterns**

   - God objects/classes
   - Spaghetti code
   - Copy-paste programming
   - Magic numbers/strings
   - Hard coding
   - Premature optimization
   - Over-engineering
   - Under-abstraction
   - Circular dependencies
   - Tight coupling

3. **PowerShell-Specific Anti-Patterns**
   - Pipeline abuse
   - Inefficient filtering
   - Missing error handling
   - Improper scope usage
   - Synchronous-only operations
   - Missing parameter validation
   - Unsafe type conversions
   - Global variable pollution

### Phase 5: Clean Code Principles

1. **Naming Conventions**

   - Function naming clarity
   - Variable naming consistency
   - Parameter naming standards
   - Constant naming patterns

2. **Function Quality**

   - Function length analysis
   - Parameter count review
   - Side effect detection
   - Return type consistency

3. **Code Organization**

   - Module cohesion
   - Logical grouping
   - Dependency organization
   - File structure standards

4. **Comments & Documentation**
   - Comment quality
   - Documentation completeness
   - Code self-documentation
   - Outdated comment detection

### Phase 6: Security Best Practices

1. **Input Validation**

   - Parameter validation coverage
   - Type checking implementation
   - Boundary condition handling
   - Injection prevention

2. **Authentication & Authorization**

   - Credential handling review
   - Permission checking
   - Session management
   - Access control patterns

3. **Cryptography**

   - Encryption usage
   - Key management
   - Hash function selection
   - Random number generation

4. **Error Handling**
   - Exception management
   - Error message exposure
   - Logging practices
   - Fail-safe defaults

### Phase 7: Performance Patterns

1. **Resource Management**

   - Memory usage patterns
   - Connection pooling
   - Object disposal
   - Cache implementation

2. **Algorithmic Efficiency**
   - Time complexity analysis
   - Space complexity review
   - Optimization opportunities
   - Bottleneck identification

### Phase 8: Testing & Maintainability

1. **Testability**

   - Test coverage analysis
   - Mockability assessment
   - Dependency injection usage
   - Test isolation review

2. **Maintainability Metrics**
   - Cyclomatic complexity
   - Coupling metrics
   - Cohesion analysis
   - Change risk assessment

## Quality Metrics & Scoring

### Code Quality Score (0-100)

```
Components:
- SOLID Compliance: 20%
- Pattern Usage: 15%
- Anti-Pattern Absence: 20%
- Clean Code: 15%
- Security: 15%
- Performance: 10%
- Maintainability: 5%
```

### Severity Classification

- **Critical**: Security vulnerabilities, data loss risks
- **High**: Major anti-patterns, SOLID violations
- **Medium**: Code smells, minor pattern issues
- **Low**: Style inconsistencies, optimization opportunities

## Output Deliverables

1. **Executive Dashboard**

   - Overall quality score
   - Critical issue count
   - Trend analysis
   - Improvement roadmap

2. **Detailed Report**

   - Issue catalog by component
   - Best practice violations
   - Pattern analysis results
   - Remediation guidelines

3. **Code Metrics**

   - Complexity measurements
   - Coupling/cohesion metrics
   - Test coverage statistics
   - Technical debt estimation

4. **Visual Analysis**
   - Dependency graphs
   - Complexity heat maps
   - Pattern distribution charts
   - Anti-pattern clustering

## Execution Command

```powershell
# Perform comprehensive code quality analysis
.\tools\PerformCodeQualityAnalysis.ps1 `
    -Scope "Full" `
    -AnalysisDepth "Comprehensive" `
    -IncludePatterns `
    -IncludeAntiPatterns `
    -IncludeSecurity `
    -IncludePerformance `
    -GenerateVisuals `
    -OutputFormat @("HTML", "JSON", "PDF")
```

## Quality Checkpoints

Ensure complete analysis coverage:

- [ ] All functions analyzed for SOLID compliance
- [ ] All modules checked for patterns
- [ ] All code blocks scanned for anti-patterns
- [ ] All inputs validated for security
- [ ] All algorithms reviewed for efficiency
- [ ] All dependencies mapped
- [ ] All complexity calculated
- [ ] All test coverage measured
- [ ] All documentation reviewed
- [ ] All metrics generated
