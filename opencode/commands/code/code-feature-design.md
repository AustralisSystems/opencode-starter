# === Universal Code Feature Design: AI-Driven Exhaustive Feature Architecture and Technical Specification Protocol ===

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

### **FEATURE DESIGN-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FEATURE DESIGN AND ARCHITECTURE ONLY:**

- **MUST:** Create comprehensive feature architecture and technical specifications
- **MUST:** Apply SOLID, DRY, KISS principles to all designs
- **MUST:** Address all cross-cutting concerns and production readiness
- **MUST:** Design integration patterns and operational architecture
- **FORBIDDEN:** Create implementation details or actual code
- **FORBIDDEN:** Design test cases or test specifications
- **FORBIDDEN:** Execute any implementation commands
- **MUST:** Output design documentation in markdown documents

**FEATURE DESIGN FOCUS AREAS:**

- Feature architecture and component design
- Technical specifications and API contracts
- Security and performance architecture
- Integration patterns and fault tolerance
- Observability and operational design
- SOLID/DRY/KISS principle application

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-feature-design-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for feature_name, feature_scope, domain_context
3. **FOLLOW PROTOCOL**: Execute all phases according to the design protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive design documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% design completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-feature-design-prompt"
arguments:
  feature_name: "[name of the feature to design]"
  feature_scope: "[simple|moderate|complex|enterprise|microservice|full-stack]"
  domain_context: "[business domain context for the feature]"
  integration_requirements: "[optional: integration requirements and dependencies]"
  performance_requirements: "[optional: performance and scalability requirements]"
  security_requirements: "[optional: security and compliance requirements]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All design phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive feature architecture designed
- [ ] All functional requirements analyzed and documented (timestamped)
- [ ] Complete technical specifications created (timestamped)
- [ ] SOLID/DRY/KISS principles applied to all designs (timestamped)
- [ ] Security architecture designed from start (timestamped)
- [ ] Performance and scalability architecture completed (timestamped)
- [ ] Integration patterns and fault tolerance designed (timestamped)
- [ ] Observability and operational architecture completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FEATURE DESIGN OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All design deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All feature architecture documentation includes precise timestamps
- [ ] All technical specifications include timestamp documentation
- [ ] All API design documents include proper date stamps
- [ ] All security architecture follows consistent date stamp format
- [ ] All performance design documentation includes timestamps
- [ ] All integration patterns include proper date stamps
- [ ] All observability design includes timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating design files without proper reverse date stamps
- Using inconsistent date formats within same design session
- Missing timestamps in design documentation

### **FEATURE DESIGN DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/code-design/Architecture_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Architecture Design with technical specifications and implementation details
2. **`./project/docs/planning/code-design/Security_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Security Design with technical specifications and implementation details
3. **`./docs/design-patterns/Integration_Patterns_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation (enduring)
4. **`./project/docs/planning/code-design/Performance_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Performance Design with technical specifications and implementation details
5. **`./project/docs/planning/code-design/Deployment_Architecture_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment Architecture with technical specifications and implementation details

**NEXT PHASE PREPARATION:**

```bash
# After design approval, proceed to planning with:
/code-feature-planning [feature-name] [complexity] [domain-context]

# Examples:
/code-feature-planning user-authentication moderate security-domain
/code-feature-planning payment-processing complex fintech-domain
/code-feature-planning dashboard-widgets simple analytics-domain
```

---

**ENFORCEMENT:** This command performs FEATURE DESIGN ONLY through the MCP prompt protocol. The comprehensive design logic is defined in `code-feature-design-prompt.yaml` and executed according to Model Context Protocol standards. No implementation details or actual code are created. Use planning commands for implementation planning after design is complete and approved.
