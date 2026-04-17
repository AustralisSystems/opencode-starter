# === Python Code Lint and Quality Check: Automated Quality Validation & Compliance Protocol ===

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

### **PYTHON LINT AND QUALITY CHECK-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR AUTOMATED PYTHON QUALITY CHECKING ONLY:**

- **MUST:** Run comprehensive Python quality tools (ruff, black, mypy, bandit, pytest)
- **MUST:** Enforce PEP 8 compliance and Python best practices
- **MUST:** Fix safe quality issues WITHOUT changing functionality
- **MUST:** Preserve ALL existing functionality during improvements
- **FORBIDDEN:** Altering business logic or algorithms
- **FORBIDDEN:** Changing API signatures or contracts
- **MUST:** Flag complex issues for follow-up remediation

**PYTHON QUALITY CHECK FOCUS AREAS:**

- PEP 8 style compliance and formatting (black, ruff)
- Type safety and annotation coverage (mypy)
- Security vulnerability detection (bandit, safety)
- Test coverage and quality (pytest, coverage)
- Code complexity and maintainability (radon, mccabe)
- Import organization and optimization (isort)
- Documentation completeness (pydocstyle)

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `python-code-lint-and-quality-check-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply target area for Python quality analysis
3. **FOLLOW PROTOCOL**: Execute all phases according to the quality check protocol specifications
4. **VERIFY COMPLETION**: Ensure all Python quality checks have been performed
5. **DOCUMENT RESULTS**: Create comprehensive quality report documentation
6. **VALIDATE COMPLIANCE**: Confirm no functionality has been altered

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "python-code-lint-and-quality-check-prompt"
arguments:
  target_area: "[directory or file path for Python quality analysis]"
  check_focus: "[optional: all|style|types|security|tests|complexity|imports]"
  fix_level: "[optional: safe-only|moderate|aggressive]"
  validation_depth: "[optional: basic|comprehensive|exhaustive]"
  reporting_detail: "[optional: summary|detailed|verbose]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All phases completed according to protocol with timestamp tracking
- [ ] PEP 8 compliance verified with ruff/black (timestamped)
- [ ] Type safety validated with mypy (timestamped)
- [ ] Security vulnerabilities scanned with bandit (timestamped)
- [ ] Test coverage measured with pytest (timestamped)
- [ ] Code complexity assessed with radon (timestamped)
- [ ] Safe quality fixes applied (timestamped)
- [ ] Complex issues flagged for remediation (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL PLUGIN QUALITY CHECK OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All quality reports (.ipynb) have reverse date stamps in filenames
- [ ] All validation logs include precise timestamps
- [ ] All fix documentation includes timestamp documentation
- [ ] All issue tracking reports include proper date stamps
- [ ] All remediation plans follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating quality check files without proper reverse date stamps
- Using inconsistent date formats within same check session
- Missing timestamps in quality documentation

### **PYTHON QUALITY CHECK DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/quality/python/Quality_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Code quality metrics, analysis, and compliance assessment
2. **`./project/docs/quality/python/Issues_Identified_{YYYYMMDD-HHMMSS}.ipynb`** - Issues Identified
3. **`./project/docs/quality/python/Remediation_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Remediation Plan with detailed breakdown and timeline

**NEXT PHASE PREPARATION:**

```bash
# After quality check completion, if complex issues found:
/python-code-remediation [target-area] [issue-severity]

# Examples:
/python-code-remediation ./src/services critical
/python-code-remediation ./lib/utils high
/python-code-remediation ./app/models medium
```

---

**ENFORCEMENT:** This command performs PYTHON QUALITY CHECKING ONLY through the MCP prompt protocol. The comprehensive quality check logic is defined in `python-code-lint-and-quality-check-prompt.yaml` and executed according to Model Context Protocol standards. No functionality changes allowed. Use remediation commands for complex fixes.
