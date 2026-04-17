# === Universal Enterprise Architecture Documentation: AI-Driven Comprehensive Architecture Design Documentation Protocol ===

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

### **ENTERPRISE ARCHITECTURE DOCUMENTATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR ENTERPRISE ARCHITECTURE DOCUMENTATION ONLY:**

- **MUST:** Create comprehensive enterprise-class professional architecture documentation
- **MUST:** Follow Diataxis principles for documentation structure and content
- **MUST:** Apply enterprise architecture best practices throughout
- **MUST:** Document complete system architecture and design patterns
- **FORBIDDEN:** Creating implementation code or executing changes
- **FORBIDDEN:** Creating test documentation or test specifications
- **FORBIDDEN:** Generating incomplete or placeholder documentation
- **MUST:** Output documentation in markdown documents only

**ENTERPRISE ARCHITECTURE DOCUMENTATION FOCUS AREAS:**

- High-level architecture design and system landscape
- Component architecture and dependency matrices
- Service-level architecture and microservices patterns
- Network topology and data flow documentation
- Security architecture and compliance frameworks
- Performance and scalability architecture design
- Detailed technical implementation specifications

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `docs-enterprise-architecture-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for architecture_scope and system_context
3. **FOLLOW PROTOCOL**: Execute all phases according to the documentation protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive architecture documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% documentation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "docs-enterprise-architecture-prompt"
arguments:
  architecture_scope: "[system-level|enterprise-level|microservices|full-stack|cloud-native]"
  system_context: "[business domain and system context]"
  documentation_type: "[optional: tutorial|how-to|reference|explanation]"
  technical_depth: "[optional: executive|technical|developer|operations]"
  compliance_requirements: "[optional: SOC2|ISO27001|GDPR|industry-specific]"
  architecture_patterns: "[optional: microservices|event-driven|layered|hexagonal]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All documentation phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive enterprise architecture documented
- [ ] All system components analyzed and documented (timestamped)
- [ ] Complete technical specifications created (timestamped)
- [ ] Dependency matrices and relationship diagrams completed (timestamped)
- [ ] Security architecture designed and documented (timestamped)
- [ ] Performance and scalability considerations addressed (timestamped)
- [ ] Network topology and data flows documented (timestamped)
- [ ] Diataxis principles applied throughout documentation (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL ENTERPRISE ARCHITECTURE DOCUMENTATION OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All architecture documentation (.ipynb) have reverse date stamps in filenames
- [ ] All system analysis documentation includes precise timestamps
- [ ] All component design includes timestamp documentation
- [ ] All technical specifications include proper date stamps
- [ ] All dependency analysis follows consistent date stamp format
- [ ] All security architecture documentation includes timestamps
- [ ] All performance design includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating architecture documentation without proper reverse date stamps
- Using inconsistent date formats within same documentation session
- Missing timestamps in architecture documentation

### **ENTERPRISE ARCHITECTURE DOCUMENTATION DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./docs/documentation/Documentation_Complete_{YYYYMMDD-HHMMSS}.ipynb`** - Documentation Complete
2. **`./docs/api/API_Documentation_{YYYYMMDD-HHMMSS}.md`** - API Documentation
3. **`./docs/guides/User_Guide_{YYYYMMDD-HHMMSS}.md`** - User Guide

**NEXT PHASE PREPARATION:**

```bash
# After architecture documentation completion, proceed to implementation planning with:
/code-feature-planning [architecture-component] [complexity] [domain-context]

# Examples:
/code-feature-planning user-service-architecture enterprise security-domain
/code-feature-planning data-pipeline-architecture complex analytics-domain
/code-feature-planning api-gateway-architecture moderate integration-domain
```

---

**ENFORCEMENT:** This command performs ENTERPRISE ARCHITECTURE DOCUMENTATION ONLY through the MCP prompt protocol. The comprehensive documentation logic is defined in `docs-enterprise-architecture-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use implementation commands for actual development after architecture documentation is complete and approved.
