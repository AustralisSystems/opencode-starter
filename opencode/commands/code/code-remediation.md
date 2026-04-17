# === Universal Code Remediation: AI-Driven Exhaustive Production Code Fix Protocol ===

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

### **REMEDIATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR CODE REMEDIATION ONLY:**

- **MUST:** Execute exhaustive remediation of ALL identified code issues
- **MUST:** Fix critical bugs, security vulnerabilities, and performance issues
- **MUST:** Apply SOLID, DRY, KISS principles to all fixes
- **MUST:** Remediate ALL quality violations and technical debt
- **MUST:** Fix code in-place (no duplicates)
- **FORBIDDEN:** Creating test code or test scripts
- **FORBIDDEN:** Writing external documentation
- **FORBIDDEN:** Creating duplicate or backup files
- **MUST:** Document with docstrings and comments only

**REMEDIATION FOCUS AREAS:**

- Critical bug fixes and stability improvements
- Security vulnerability remediation
- Performance bottleneck elimination
- Code quality violations correction
- Technical debt reduction
- Compliance and standards adherence
- In-code documentation updates only

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-remediation-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for remediation_target and optional parameters
3. **FOLLOW PROTOCOL**: Execute all phases according to the remediation protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive remediation documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% remediation success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-remediation-prompt"
arguments:
  remediation_target: "[all-critical|security|performance|quality|specific-component]"
  remediation_scope: "[optional: comprehensive|critical-only|security-focused|performance-focused]"
  issue_source: "[optional: source of issues to remediate]"
  validation_level: "[optional: standard|comprehensive|continuous|strict]"
  deployment_strategy: "[optional: atomic|incremental|batch|emergency]"
  logging_level: "[optional: standard|debug|verbose|trace]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All remediation phases completed according to protocol with timestamp tracking
- [ ] 100% critical issues and vulnerabilities remediated
- [ ] All security vulnerabilities fixed (timestamped)
- [ ] Complete performance optimization implemented (timestamped)
- [ ] All code quality violations corrected (timestamped)
- [ ] Technical debt reduction completed (timestamped)
- [ ] Compliance and standards adherence validated (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL REMEDIATION OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All remediation reports (.ipynb) have reverse date stamps in filenames
- [ ] All bug fix documentation includes precise timestamps
- [ ] All security remediation includes timestamp documentation
- [ ] All performance optimization reports include proper date stamps
- [ ] All quality improvement follows consistent date stamp format
- [ ] All technical debt reduction documentation includes timestamps
- [ ] All compliance validation includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating remediation files without proper reverse date stamps
- Using inconsistent date formats within same remediation session
- Missing timestamps in remediation documentation

### **REMEDIATION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/code/Implementation_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Complete implementation details with all components and modules
2. **`./project/docs/testing/code/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/quality/code/Quality_Assessment_{YYYYMMDD-HHMMSS}.ipynb`** - Code quality metrics, analysis, and compliance assessment

**NEXT PHASE PREPARATION:**

```bash
# After remediation completion, execute validation with:
/code-quality-comprehensive [remediated-directory]

# Examples:
/code-quality-comprehensive ./src/core
/code-quality-comprehensive ./src/services
/code-quality-comprehensive ./src/api
```

---

**ENFORCEMENT:** This command performs CODE REMEDIATION ONLY through the MCP prompt protocol. The comprehensive remediation logic is defined in `code-remediation-prompt.yaml` and executed according to Model Context Protocol standards.
