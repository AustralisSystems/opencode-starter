# === Universal Code Refactoring: AI-Driven Exhaustive Production Code Improvement Protocol ===

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

### **REFACTORING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR CODE REFACTORING ONLY:**

- **MUST:** Execute exhaustive refactoring of ALL production code
- **MUST:** Apply SOLID, DRY, KISS principles throughout
- **MUST:** Fix ALL identified quality issues and gaps
- **MUST:** Improve ALL performance bottlenecks
- **MUST:** Refactor code in-place (no duplicates)
- **FORBIDDEN:** Creating test code or test scripts
- **FORBIDDEN:** Writing external documentation
- **FORBIDDEN:** Creating duplicate or backup files
- **MUST:** Document with docstrings and comments only

**REFACTORING FOCUS AREAS:**

- Code quality improvement and optimization
- Performance enhancement and optimization
- Security hardening and vulnerability fixes
- Clean code principles implementation
- Structure and organization improvements
- Transient code cleanup and hygiene
- In-code documentation updates only

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-refactor-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for refactoring_target and optional parameters
3. **FOLLOW PROTOCOL**: Execute all phases according to the refactoring protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive refactoring documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% refactoring success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-refactor-prompt"
arguments:
  refactoring_target: "[all-findings|performance|quality|security|structure]"
  refactoring_scope: "[optional: comprehensive|focused|specific-issues|critical-only]"
  improvement_focus: "[optional: solid|dry|kiss|performance|security|cleanup]"
  validation_level: "[optional: standard|comprehensive|strict|continuous]"
  change_strategy: "[optional: systematic|atomic|incremental|prioritized]"
  quality_enforcement: "[optional: standard|strict|enterprise|maximum]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All refactoring phases completed according to protocol with timestamp tracking
- [ ] 100% identified issues refactored
- [ ] All SOLID, DRY, KISS principles applied (timestamped)
- [ ] Complete functionality preservation validated (timestamped)
- [ ] Performance optimization completed (timestamped)
- [ ] Security hardening implemented (timestamped)
- [ ] Transient code cleanup executed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL REFACTORING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All refactoring reports (.ipynb) have reverse date stamps in filenames
- [ ] All quality improvement documentation includes precise timestamps
- [ ] All performance optimization reports include timestamp documentation
- [ ] All security enhancement reports include proper date stamps
- [ ] All cleanup certification reports follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating refactoring files without proper reverse date stamps
- Using inconsistent date formats within same refactoring session
- Missing timestamps in refactoring documentation

### **REFACTORING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/implementation/refactoring/Refactoring_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive refactoring report and findings
2. **`./project/docs/testing/regression-tests/Regression_Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/quality/code-quality/Quality_Improvement_{YYYYMMDD-HHMMSS}.ipynb`** - Code quality metrics, analysis, and compliance assessment

**NEXT PHASE PREPARATION:**

```bash
# After refactoring completion, execute validation with:
/code-quality-comprehensive [refactored-directory]

# Examples:
/code-quality-comprehensive ./src/refactored
/code-quality-comprehensive ./src/core
/code-quality-comprehensive ./src/services
```

---

**ENFORCEMENT:** This command performs CODE REFACTORING ONLY through the MCP prompt protocol. The comprehensive refactoring logic is defined in `code-refactor-prompt.yaml` and executed according to Model Context Protocol standards.
