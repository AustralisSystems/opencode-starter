# === FastAPI Code Quality Review: AI-Driven FastAPI Code Quality Analysis and Architecture Review Protocol ===

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
- Skipping quality validation
- Ignoring architectural violations
- Proceeding without understanding
- Missing security analysis
- Overlooking performance issues

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO SUPERFICIAL REVIEWS** - perform deep architectural analysis
- **NO SKIPPED VALIDATIONS** - check ALL quality criteria
- **NO IGNORED VIOLATIONS** - identify and report ALL issues
- **NO INCOMPLETE ANALYSIS** - comprehensive review required
- **NO MISSING DOCUMENTATION** - document all findings
- **NO WORKAROUNDS** - identify root causes
- **NO PLACEHOLDER RECOMMENDATIONS** - provide specific fixes
- **NO INCOMPLETE REPORTS** - thorough analysis required

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
   - Use web search for latest FastAPI documentation
   - Find official FastAPI docs and examples
   - Search GitHub for FastAPI production implementations
   - Review industry FastAPI best practices
   - Study similar successful FastAPI projects
   - Check Stack Overflow for common FastAPI patterns

**SEARCH PRIORITIES:**

- Official FastAPI documentation (latest version)
- GitHub repositories with high stars using FastAPI
- Industry standard FastAPI implementations
- Recent FastAPI blog posts/tutorials (< 1 year old)
- Community FastAPI best practices

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **FASTAPI CODE QUALITY REVIEW-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI CODE QUALITY REVIEW ONLY:**

- **MUST:** Perform comprehensive FastAPI code quality analysis and architectural review
- **MUST:** Validate adherence to Clean Architecture, SOLID, and FastAPI best practices
- **MUST:** Analyze security, performance, and scalability aspects
- **MUST:** Review API design patterns, dependency injection, and async implementations
- **FORBIDDEN:** Making code changes or modifications
- **FORBIDDEN:** Creating new files or implementations
- **FORBIDDEN:** Modifying existing code during review
- **MUST:** Output analysis and recommendations in markdown documents only

**FASTAPI CODE QUALITY REVIEW FOCUS AREAS:**

- Clean Architecture and SOLID principles compliance analysis
- FastAPI-specific pattern adherence and best practices validation
- API design quality, RESTful principles, and OpenAPI compliance
- Dependency injection pattern implementation quality
- Database integration and repository pattern analysis
- Authentication/authorization security implementation review
- Pydantic model design and validation pattern analysis
- Async programming pattern implementation review
- Error handling and logging architecture analysis
- Performance optimization and caching strategy review
- Code organization, modularity, and maintainability assessment
- Security vulnerability and best practice compliance analysis

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-code-quality-review-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for review_scope and quality_focus
3. **FOLLOW PROTOCOL**: Execute all phases according to the quality review protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive quality analysis documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% review completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-code-quality-review-prompt"
arguments:
  review_scope: "[complete-application|specific-modules|api-endpoints|architecture-layers]"
  quality_focus: "[comprehensive|security-focused|performance-focused|architecture-focused]"
  analysis_depth: "[optional: surface|deep|architectural|enterprise]"
  compliance_standards: "[optional: clean-architecture|solid|fastapi-best-practices|all]"
  security_analysis: "[optional: basic|comprehensive|penetration-focused|compliance]"
  performance_analysis: "[optional: basic|comprehensive|load-testing|optimization]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All quality review phases completed according to protocol with timestamp tracking
- [ ] 100% FastAPI code quality analysis performed
- [ ] Complete architectural compliance assessment completed (timestamped)
- [ ] Security analysis and vulnerability assessment performed (timestamped)
- [ ] Performance analysis and optimization recommendations provided (timestamped)
- [ ] API design quality and RESTful compliance reviewed (timestamped)
- [ ] Code organization and maintainability assessment completed (timestamped)
- [ ] Dependency injection and service layer quality analyzed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FASTAPI CODE QUALITY REVIEW OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All review deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All quality analysis documentation includes precise timestamps
- [ ] All compliance reports include timestamp documentation
- [ ] All security analysis reports include proper date stamps
- [ ] All performance analysis reports follow consistent date stamp format
- [ ] All architecture review reports include timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating review files without proper reverse date stamps
- Using inconsistent date formats within same review session
- Missing timestamps in quality analysis documentation

### **FASTAPI CODE QUALITY REVIEW DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/analysis/python/Analysis_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive analysis report and findings
2. **`./project/docs/analysis/python/Findings_Recommendations_{YYYYMMDD-HHMMSS}.ipynb`** - Findings Recommendations
3. **`./project/docs/analysis/python/Action_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Action Plan with detailed breakdown and timeline

**NEXT PHASE PREPARATION:**

```bash
# After quality review completion, address issues with:
/fastapi-code-refactor [issue-category] [priority-level] [scope]

# Examples:
/fastapi-code-refactor security-issues high complete-application
/fastapi-code-refactor performance-optimization medium specific-modules
/fastapi-code-refactor architecture-compliance high core-services
```

## Command Integration

### Related Commands

- **Implementation Commands (Prerequisites)**:
  - `/fastapi-application-implement` - Full application implementation
  - `/fastapi-router-implement` - Router-specific implementation
  - `/fastapi-service-implement` - Service layer implementation
- **Design Commands (Reference)**:
  - `/fastapi-architecture-design` - Architecture compliance validation
  - `/fastapi-api-endpoint-design` - API design compliance
  - `/fastapi-service-dependency-patterns` - Service pattern compliance
- **Improvement Commands (Next Phase)**:
  - `/fastapi-code-refactor` - Code improvement and modernization

### Workflow Navigation

```
Implementation  Quality Review  Code Refactoring  Final Validation

  Production Code   Analysis     Optimization    Quality Assurance
```

### Usage Pattern

This command should be executed AFTER implementation commands to validate:

1. **Code Quality**: Architecture compliance, SOLID principles, best practices
2. **Security**: Vulnerability analysis and security pattern validation
3. **Performance**: Optimization opportunities and bottleneck identification
4. **Standards**: FastAPI patterns, Pydantic usage, async implementation

### Next Phase Commands

After completing quality review, proceed with improvements using:

1. `/fastapi-code-refactor` - Implement the review recommendations
2. Re-run `/fastapi-code-quality-review` - Validate improvements made

---

**ENFORCEMENT:** This command performs FASTAPI CODE QUALITY REVIEW ONLY through the MCP prompt protocol. The comprehensive review logic is defined in `fastapi-code-quality-review-prompt.yaml` and executed according to Model Context Protocol standards. No code modification allowed. Use refactoring commands for actual code improvements after review is complete and recommendations are provided.

---
