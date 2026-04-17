# === Universal Code Debugging: AI-Driven Exhaustive Issue Resolution Protocol ===

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

## **FORBIDDEN PRACTICES**

**FORBIDDEN**
YOU ARE FORBIDDEN from creating custom scripts to fix or remediate the code base, YOU HAVE CONTINUIOUSLY corrupted the code base through poor "fix" scripts
YOU MUST NEVER EVER EVER create custom scripts to fix or remediate the code base

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

## **RTFM (READ THE FUCKING MANUAL) - MANDATORY PROTOCOL**

**YOU MUST ALWAYS:**

1. **FIND AND READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read implementation documents for context
   - Review analysis documents for insights
   - Study documentation documents for patterns

2. **READ FIND AND PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **PERFOMR RESEARCH ONLINE FOR BEST PRACTICES:**
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

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-debug-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for issue_type, severity, codebase_path
3. **FOLLOW PROTOCOL**: Execute all phases according to the debugging protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive markdown document documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% production ready status achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "comprehensive-debug"
arguments:
  issue_type: "[runtime|logic|performance|security|concurrency|integration|all]"
  severity: "[critical|high|medium|low]"
  codebase_path: "[path to codebase or component]"
  error_logs: "[optional: error logs or stack traces]"
  reproduction_steps: "[optional: steps to reproduce]"
  affected_components: "[optional: list of affected components]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All debugging phases completed according to protocol with timestamp tracking
- [ ] 100% of issues resolved with production-ready fixes (timestamped)
- [ ] Zero technical debt remaining (timestamp validation)
- [ ] Comprehensive documentation created with reverse date stamps
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All markdown documents (.ipynb) have reverse date stamps in filenames
- [ ] All investigation logs include precise timestamps
- [ ] All git commits include timestamp documentation
- [ ] All memory entries include proper date stamps
- [ ] All deliverables follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating files without proper reverse date stamps
- Using inconsistent date formats within same session
- Missing timestamps in investigation documentation
