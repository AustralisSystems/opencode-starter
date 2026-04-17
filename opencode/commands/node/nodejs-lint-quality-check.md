# === Node.js Code Lint and Quality Check: Automated Quality Validation & Compliance Protocol ===

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

### **NODE.JS LINT AND QUALITY CHECK-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR AUTOMATED NODE.JS QUALITY CHECKING ONLY:**

- **MUST:** Run comprehensive Node.js quality tools (ESLint, Prettier, TypeScript, npm audit, Jest)
- **MUST:** Enforce JavaScript/TypeScript standards and Node.js best practices
- **MUST:** Fix safe quality issues WITHOUT changing functionality
- **MUST:** Preserve ALL existing functionality during improvements
- **FORBIDDEN:** Altering business logic or algorithms
- **FORBIDDEN:** Changing API signatures or contracts
- **MUST:** Flag complex issues for follow-up remediation

**NODE.JS QUALITY CHECK FOCUS AREAS:**

- JavaScript/TypeScript style compliance and formatting (ESLint, Prettier)
- Type safety and annotation coverage (TypeScript)
- Security vulnerability detection (npm audit, ESLint security plugins)
- Test coverage and quality (Jest, Node.js test runner)
- Code complexity and maintainability (ESLint complexity rules)
- Import organization and optimization (ESLint import rules)
- Documentation completeness (JSDoc)

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `nodejs-lint-quality-check-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply target area for Node.js quality analysis
3. **FOLLOW PROTOCOL**: Execute all phases according to the quality check protocol specifications
4. **VERIFY COMPLETION**: Ensure all Node.js quality checks have been performed
5. **DOCUMENT RESULTS**: Create comprehensive quality report documentation
6. **VALIDATE COMPLIANCE**: Confirm no functionality has been altered

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "nodejs-lint-quality-check-prompt"
arguments:
  target_area: "[directory or file path for Node.js quality analysis]"
  check_focus: "[optional: all|style|types|security|tests|complexity|imports]"
  fix_level: "[optional: safe-only|moderate|aggressive]"
  validation_depth: "[optional: basic|comprehensive|exhaustive]"
  reporting_detail: "[optional: summary|detailed|verbose]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All phases completed according to protocol with timestamp tracking
- [ ] JavaScript/TypeScript style compliance verified with ESLint/Prettier (timestamped)
- [ ] Type safety validated with TypeScript (timestamped)
- [ ] Security vulnerabilities scanned with npm audit (timestamped)
- [ ] Test coverage measured with Jest (timestamped)
- [ ] Code complexity assessed with ESLint (timestamped)
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

### **NODE.JS QUALITY CHECK DELIVERABLES - FIXES APPLIED ONLY:**

**MANDATORY QUALITY IMPROVEMENTS - NO EXTENSIVE DOCUMENTATION:**

1. **Code Formatting Applied** - Prettier formatting and import sorting completed
2. **Linting Issues Resolved** - ESLint violations fixed automatically
3. **Type Safety Improvements** - Missing TypeScript types added where safe
4. **Security Vulnerabilities Fixed** - npm audit security issues resolved automatically
5. **Style Compliance Achieved** - JavaScript/TypeScript style violations corrected
6. **Import Organization** - Import statements optimized and organized
7. **Documentation Standards Applied** - Missing JSDoc comments added where required
8. **Performance Optimizations** - Safe performance improvements applied

**LIMITED DOCUMENTATION DELIVERABLES (Execution Summary Only):**

- **`Quality_Fixes_Applied-YYYY-MM-DD-HHMMSS.ipynb`** - Summary of automatic fixes applied
- **`Manual_Review_Required-YYYY-MM-DD-HHMMSS.ipynb`** - Complex issues flagged for manual review (only if critical issues found)

**FORBIDDEN DELIVERABLES:**

- No comprehensive quality assessment reports (analysis commands handle this)
- No style compliance reports (analysis commands provide these)
- No type safety reports (analysis commands create these)
- No security scan documentation (analysis commands handle this)
- No test coverage analysis (analysis commands provide this)
- No executive quality summaries (analysis commands create these)

**NEXT PHASE PREPARATION:**

```bash
# After quality check completion, if complex issues found:
/nodejs-code-remediation [target-area] [issue-severity]

# Examples:
/nodejs-code-remediation ./src/services critical
/nodejs-code-remediation ./lib/utils high
/nodejs-code-remediation ./app/models medium
```

---

**ENFORCEMENT:** This command performs NODE.JS QUALITY CHECKING ONLY through the MCP prompt protocol. The comprehensive quality check logic is defined in `nodejs-lint-quality-check-prompt.yaml` and executed according to Model Context Protocol standards. No functionality changes allowed. Use remediation commands for complex fixes.
