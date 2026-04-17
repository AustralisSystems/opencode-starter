# === Code AST/SAST Analysis: Comprehensive Abstract Syntax Tree & Static Security Analysis Protocol ===

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

### **AST/SAST ANALYSIS MANDATE - CRITICAL FOCUS**

**THIS COMMAND IS FOR COMPREHENSIVE AST AND SAST ANALYSIS:**

- **MUST:** Execute exhaustive Abstract Syntax Tree and Static Application Security Testing analysis
- **MUST:** Analyze ALL code structures, security vulnerabilities, and architectural patterns
- **MUST:** Generate complete visual AST representations and security findings
- **MUST:** Create comprehensive compliance matrices and analysis documentation
- **FORBIDDEN:** Superficial or incomplete AST/SAST analysis
- **FORBIDDEN:** Skipping any code paths or using simplified analysis tools
- **FORBIDDEN:** Missing critical security vulnerabilities or structural issues
- **MUST:** Output analysis documentation in markdown documents with timestamps

**AST/SAST ANALYSIS FOCUS AREAS:**

- Exhaustive Abstract Syntax Tree parsing and analysis
- Comprehensive Static Application Security Testing
- Complete dependency and data flow analysis
- Control flow analysis and complexity measurement
- Pattern detection and dead code identification
- Security vulnerability assessment and compliance validation

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `quality-code-ast-analysis-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for codebase_path, analysis_scope, security_focus
3. **FOLLOW PROTOCOL**: Execute all phases according to the AST/SAST analysis protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive analysis documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% AST/SAST analysis completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "quality-code-ast-analysis-prompt"
arguments:
  codebase_path: "[root directory of codebase to analyze]"
  analysis_scope: "[comprehensive|security-focused|structure-focused|compliance-focused]"
  security_focus: "[vulnerabilities|best-practices|compliance|all-security]"
  ast_depth: "[optional: surface|detailed|comprehensive|exhaustive]"
  sast_coverage: "[optional: basic|standard|comprehensive|enterprise]"
  output_format: "[optional: jupyter|visual|matrices|comprehensive]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All AST/SAST analysis phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive codebase AST analysis completed
- [ ] All code structures parsed and analyzed systematically (timestamped)
- [ ] Complete SAST security analysis performed (timestamped)
- [ ] All dependencies and data flows mapped (timestamped)
- [ ] Control flow analysis and complexity measurement completed (timestamped)
- [ ] Pattern detection and dead code identification performed (timestamped)
- [ ] Visual AST representations and compliance matrices generated (timestamped)
- [ ] Security vulnerability assessment completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL AST/SAST ANALYSIS OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All analysis deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All AST analysis documentation includes precise timestamps
- [ ] All SAST security analysis includes timestamp documentation
- [ ] All dependency analysis reports include proper date stamps
- [ ] All complexity analysis follows consistent date stamp format
- [ ] All pattern detection documentation includes timestamps
- [ ] All compliance matrices include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating analysis files without proper reverse date stamps
- Using inconsistent date formats within same analysis session
- Missing timestamps in analysis documentation

### **AST/SAST ANALYSIS DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/analysis/quality/Analysis_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive analysis report and findings
2. **`./project/docs/analysis/quality/Findings_Recommendations_{YYYYMMDD-HHMMSS}.ipynb`** - Findings Recommendations
3. **`./project/docs/analysis/quality/Action_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Action Plan with detailed breakdown and timeline

**NEXT PHASE PREPARATION:**

```bash
# After analysis completion, execute improvements with:
/quality-fix-security [analysis-results] [security-vulnerabilities]
/quality-fix-critical [analysis-results] [critical-issues]
/quality-improve-code [analysis-results] [structural-improvements]

# Examples:
/quality-fix-security AST_Analysis-2025-09-22-085549.ipynb vulnerabilities
/quality-fix-critical AST_Analysis-2025-09-22-085549.ipynb complexity-violations
/quality-improve-code AST_Analysis-2025-09-22-085549.ipynb structural-patterns
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE AST/SAST ANALYSIS through the MCP prompt protocol. The comprehensive analysis logic is defined in `quality-code-ast-analysis-prompt.yaml` and executed according to Model Context Protocol standards. Use subsequent quality fix commands for remediation execution after analysis is complete and approved.
