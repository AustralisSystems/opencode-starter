# === Universal Plugin Architecture Refactoring: AI-Driven Exhaustive Modular System Transformation Protocol ===

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

### **PLUGIN REFACTORING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR PLUGIN ARCHITECTURE REFACTORING ONLY:**

- **MUST:** Transform monolithic code TO plugin architecture
- **MUST:** Extract plugin interfaces and contracts
- **MUST:** Implement plugin registry and discovery
- **MUST:** Add hot-loading and lifecycle management
- **FORBIDDEN:** Creating test code
- **FORBIDDEN:** Creating duplicate files or backups
- **MUST:** Transform existing code in-place only

**PLUGIN REFACTORING FOCUS AREAS:**

- Monolith decomposition into plugin modules
- Interface extraction and contract definition
- Registry integration and discovery implementation
- Hot-loading and runtime management addition
- Plugin isolation and security boundary creation
- Extension point and hook system implementation
- Inter-plugin communication establishment

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-plugin-refactor-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for refactoring target and approach
3. **FOLLOW PROTOCOL**: Execute all phases according to the refactoring protocol specifications
4. **VERIFY COMPLETION**: Ensure all refactoring objectives have been met
5. **DOCUMENT RESULTS**: Create comprehensive refactoring documentation
6. **VALIDATE COMPLIANCE**: Confirm functionality preservation and quality improvement

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-plugin-refactor-prompt"
arguments:
  refactoring_target: "[target component or module to refactor]"
  transformation_approach: "[gradual|aggressive|conservative]"
  plugin_granularity: "[optional: fine|medium|coarse]"
  isolation_level: "[optional: strict|moderate|minimal]"
  hot_loading_strategy: "[optional: full|partial|none]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All phases completed according to protocol with timestamp tracking
- [ ] Monolithic components transformed to plugins (timestamped)
- [ ] Plugin interfaces extracted and defined (timestamped)
- [ ] Registry integration implemented (timestamped)
- [ ] Hot-loading capabilities added (timestamped)
- [ ] Plugin isolation established (timestamped)
- [ ] Extension points created (timestamped)
- [ ] Functionality fully preserved (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL PLUGIN REFACTORING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All refactoring reports (.ipynb) have reverse date stamps in filenames
- [ ] All transformation logs include precise timestamps
- [ ] All validation reports include timestamp documentation
- [ ] All quality assessments include proper date stamps
- [ ] All implementation tracking follows consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating refactoring files without proper reverse date stamps
- Using inconsistent date formats within same refactoring session
- Missing timestamps in transformation documentation

### **PLUGIN REFACTORING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/implementation/refactoring/Refactoring_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive refactoring report and findings
2. **`./project/docs/testing/regression-tests/Regression_Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/quality/code-quality/Quality_Improvement_{YYYYMMDD-HHMMSS}.ipynb`** - Code quality metrics, analysis, and compliance assessment

**NEXT PHASE PREPARATION:**

```bash
# After refactoring completion, validate quality with:
/code-plugin-quality-analysis [refactored-area]

# Examples:
/code-plugin-quality-analysis ./src/plugins
/code-plugin-quality-analysis ./lib/plugin-framework
/code-plugin-quality-analysis ./modules/extensions
```

---

**ENFORCEMENT:** This command performs PLUGIN ARCHITECTURE REFACTORING ONLY through the MCP prompt protocol. The comprehensive refactoring logic is defined in `code-plugin-refactor-prompt.yaml` and executed according to Model Context Protocol standards. No test creation allowed. Transform existing code in-place only.
