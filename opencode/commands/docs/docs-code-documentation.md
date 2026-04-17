# === Universal Code Documentation: AI-Driven Comprehensive Production Code Documentation Protocol ===

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

### **CODE DOCUMENTATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR CODE DOCUMENTATION ONLY:**

- **MUST:** Create comprehensive code documentation and API references
- **MUST:** Generate developer guides and technical specifications
- **MUST:** Document all functions, classes, modules, and services
- **MUST:** Create operational runbooks and maintenance documentation
- **FORBIDDEN:** Creating implementation code or executing changes
- **FORBIDDEN:** Creating test documentation or test specifications
- **FORBIDDEN:** Generating incomplete or placeholder documentation
- **MUST:** Output documentation in markdown documents only

**CODE DOCUMENTATION FOCUS AREAS:**

- Complete API documentation and function references
- System component discovery and service topology
- Developer documentation and implementation guides
- Operations documentation and runbooks
- Security documentation and compliance guides
- Module structure and dependency documentation
- Performance and maintenance documentation

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `docs-code-documentation-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for documentation_scope and codebase_target
3. **FOLLOW PROTOCOL**: Execute all phases according to the documentation protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive code documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% documentation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "docs-code-documentation-prompt"
arguments:
  documentation_scope: "[comprehensive|api-focused|developer-guide|operations|security]"
  codebase_target: "[entire-codebase|specific-modules|services|components]"
  documentation_depth: "[optional: summary|detailed|comprehensive|technical-reference]"
  audience_focus: "[optional: developers|operations|architects|end-users]"
  framework_type: "[optional: api-reference|user-guide|technical-specs|runbooks]"
  compliance_standards: "[optional: internal|industry|regulatory|enterprise]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All documentation phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive code documentation completed
- [ ] All system components discovered and documented (timestamped)
- [ ] Complete API documentation with examples created (timestamped)
- [ ] Developer guides and implementation documentation completed (timestamped)
- [ ] Operations runbooks and maintenance procedures documented (timestamped)
- [ ] Security documentation and compliance guides created (timestamped)
- [ ] Module dependency analysis and documentation completed (timestamped)
- [ ] Performance and troubleshooting documentation generated (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL CODE DOCUMENTATION OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All code documentation (.ipynb) have reverse date stamps in filenames
- [ ] All API reference documentation includes precise timestamps
- [ ] All developer guide documentation includes timestamp documentation
- [ ] All operations documentation includes proper date stamps
- [ ] All security documentation follows consistent date stamp format
- [ ] All module documentation includes timestamps
- [ ] All troubleshooting guides include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating code documentation without proper reverse date stamps
- Using inconsistent date formats within same documentation session
- Missing timestamps in code documentation

### **CODE DOCUMENTATION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./docs/documentation/Documentation_Complete_{YYYYMMDD-HHMMSS}.ipynb`** - Documentation Complete
2. **`./docs/api/API_Documentation_{YYYYMMDD-HHMMSS}.md`** - API Documentation
3. **`./docs/guides/User_Guide_{YYYYMMDD-HHMMSS}.md`** - User Guide

**NEXT PHASE PREPARATION:**

```bash
# After code documentation completion, proceed to architecture documentation with:
/docs-enterprise-architecture [architecture-scope] [system-context]

# Examples:
/docs-enterprise-architecture system-level n8n-automation-platform
/docs-enterprise-architecture microservices api-orchestration-system
/docs-enterprise-architecture full-stack cloud-native-platform
```

---

**ENFORCEMENT:** This command performs CODE DOCUMENTATION ONLY through the MCP prompt protocol. The comprehensive documentation logic is defined in `docs-code-documentation-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use architecture documentation commands for system design documentation after code documentation is complete and approved.
