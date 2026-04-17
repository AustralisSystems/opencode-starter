# === Universal Plugin Architecture Gap Analysis: AI-Driven Exhaustive Modular System Gap Assessment Protocol ===

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

### **PLUGIN GAP ANALYSIS-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR PLUGIN ARCHITECTURE GAP ANALYSIS ONLY:**

- **MUST:** Execute exhaustive gap analysis of ALL production code against plugin architecture requirements
- **MUST:** Identify ALL missing plugin components, incomplete implementations, and architectural gaps
- **MUST:** Analyze plugin isolation, hot-loading capabilities, registry integration, and extension points
- **MUST:** Generate comprehensive Jupyter Notebook documentation with actionable remediation plans
- **FORBIDDEN:** Analyzing test code or external documentation
- **FORBIDDEN:** Creating duplicate files or backups
- **MUST:** Analyze existing code in-place only

**PLUGIN GAP ANALYSIS FOCUS AREAS:**

- Plugin interface and contract completeness assessment
- Extension point and hook system gap identification
- Registry integration and discovery capability analysis
- Hot-loading and runtime management gap detection
- Plugin isolation and security boundary assessment
- Inter-plugin communication pattern analysis
- Plugin lifecycle and state management evaluation

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-plugin-gap-analysis-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply optional arguments for analysis focus and severity
3. **FOLLOW PROTOCOL**: Execute all phases according to the gap analysis protocol specifications
4. **VERIFY COMPLETION**: Ensure all gaps have been identified and documented
5. **DOCUMENT RESULTS**: Create comprehensive gap analysis documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% code coverage analysis achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with optional arguments:
prompt_name: "code-plugin-gap-analysis-prompt"
arguments:
  analysis_focus: "[optional: entire-codebase|specific-module|registry|hot-loading|interfaces]"
  severity_threshold: "[optional: all|critical|high|medium]"
  transformation_scope: "[optional: full-plugin|modular-only|interface-extraction]"
  effort_detail: "[optional: high-level|detailed|task-breakdown]"
  risk_assessment: "[optional: basic|comprehensive|impact-analysis]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All phases completed according to protocol with timestamp tracking
- [ ] 100% of production code analyzed for plugin architecture gaps
- [ ] All plugin interface and contract gaps identified (timestamped)
- [ ] Complete registry integration gaps documented (timestamped)
- [ ] Hot-loading capability gaps fully assessed (timestamped)
- [ ] Plugin isolation and security gaps identified (timestamped)
- [ ] Extension point gaps comprehensively mapped (timestamped)
- [ ] Transformation roadmap with effort estimates created (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL PLUGIN GAP ANALYSIS OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All gap analysis reports (.ipynb) have reverse date stamps in filenames
- [ ] All interface gap documentation includes precise timestamps
- [ ] All security gap assessments include timestamp documentation
- [ ] All registry gap reports include proper date stamps
- [ ] All extension point analyses follow consistent date stamp format
- [ ] All transformation roadmaps include timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating gap analysis files without proper reverse date stamps
- Using inconsistent date formats within same analysis session
- Missing timestamps in gap documentation

### **PLUGIN GAP ANALYSIS DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/analysis/plugin/Analysis_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive analysis report and findings
2. **`./project/docs/analysis/plugin/Findings_Recommendations_{YYYYMMDD-HHMMSS}.ipynb`** - Findings Recommendations
3. **`./project/docs/analysis/plugin/Action_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Action Plan with detailed breakdown and timeline

**NEXT PHASE PREPARATION:**

```bash
# After gap analysis completion, proceed to remediation with:
/code-plugin-framework-planning [plugin-name] [complexity] [context]

# Examples:
/code-plugin-framework-planning auth-plugin complex microservices
/code-plugin-framework-planning data-processor moderate monolithic
/code-plugin-framework-planning ui-extension simple event-driven
```

---

**ENFORCEMENT:** This command performs PLUGIN ARCHITECTURE GAP ANALYSIS ONLY through the MCP prompt protocol. The comprehensive gap analysis logic is defined in `code-plugin-gap-analysis-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use planning and implementation commands after gap analysis is complete.
