# === Code Feature Planning ===

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

### **FEATURE PLANNING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FEATURE PLANNING ONLY:**

- **MUST:** Create exhaustive, production-ready implementation plans
- **MUST:** Perform comprehensive reuse analysis of existing codebase
- **MUST:** Create detailed task breakdown with dependencies
- **MUST:** Plan quality gates and validation workflows
- **FORBIDDEN:** Create actual implementation code
- **FORBIDDEN:** Create external documentation files
- **FORBIDDEN:** Generate test planning or test specifications
- **MUST:** Output planning documentation in markdown documents

**FEATURE PLANNING FOCUS AREAS:**

- Comprehensive feature analysis and requirements breakdown
- Task decomposition and dependency mapping
- Resource estimation and timeline planning
- Risk assessment and mitigation strategies
- Quality assurance and validation planning
- Implementation roadmap and milestone definition

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-feature-planning-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for feature_name and optional parameters
3. **FOLLOW PROTOCOL**: Execute all phases according to the feature planning protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive feature planning documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% planning completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-feature-planning-prompt"
arguments:
  feature_name: "[name of the feature to plan]"
  feature_complexity: "[simple|moderate|complex|enterprise]"
  domain_context: "[business domain and context]"
  planning_scope: "[optional: comprehensive|focused|mvp|full-feature]"
  integration_requirements: "[optional: integration and dependency requirements]"
  timeline_constraints: "[optional: timeline and milestone constraints]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All planning phases completed according to protocol with timestamp tracking
- [ ] 100% feature requirements analyzed and documented
- [ ] Complete task breakdown with dependencies created (timestamped)
- [ ] Resource estimation and timeline planning completed (timestamped)
- [ ] Risk assessment and mitigation strategies defined (timestamped)
- [ ] Quality gates and validation workflows planned (timestamped)
- [ ] Implementation roadmap with milestones established (timestamped)
- [ ] Code reuse analysis and integration planning completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FEATURE PLANNING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All planning deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All feature analysis documentation includes precise timestamps
- [ ] All task breakdown documentation includes timestamp documentation
- [ ] All resource estimation reports include proper date stamps
- [ ] All risk assessment follows consistent date stamp format
- [ ] All quality planning documentation includes timestamps
- [ ] All roadmap and milestone plans include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating planning files without proper reverse date stamps
- Using inconsistent date formats within same planning session
- Missing timestamps in planning documentation

### **FEATURE PLANNING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/code-planning/Implementation_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Complete implementation details with all components and modules
2. **`./project/docs/planning/code-planning/Testing_Strategy_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/planning/code-planning/Integration_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation
4. **`./project/docs/planning/code-planning/Deployment_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment architecture, strategy, and SOLID compliance review

**NEXT PHASE PREPARATION:**

```bash
# After planning approval, proceed to implementation with:
/code-feature-implement [feature-name] [implementation-scope] [design-source]

# Examples:
/code-feature-implement user-authentication comprehensive design-specifications
/code-feature-implement payment-processing core-only architecture-documents
/code-feature-implement dashboard-widgets mvp planning-requirements
```

---

**ENFORCEMENT:** This command performs FEATURE PLANNING ONLY through the MCP prompt protocol. The comprehensive planning logic is defined in `code-feature-planning-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use implementation commands for actual feature development after planning is complete and approved.
