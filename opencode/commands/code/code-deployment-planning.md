# === Deployment Planning: Comprehensive Deployment Strategy & Documentation Protocol ===

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

### **PLANNING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR PLANNING AND DOCUMENTATION ONLY:**

- **MUST:** Create comprehensive deployment plans and documentation
- **MUST:** Analyze system architecture and dependencies
- **MUST:** Design deployment strategies and rollback procedures
- **MUST:** Document infrastructure requirements and configurations
- **FORBIDDEN:** Execute ANY actual deployment commands
- **FORBIDDEN:** Make ANY changes to live systems
- **FORBIDDEN:** Deploy ANY code or infrastructure
- **MUST:** Output planning documentation in markdown documents

**PLANNING FOCUS AREAS:**

- Deployment strategy design (blue-green, canary, rolling)
- Infrastructure requirements and capacity planning
- Security considerations and compliance requirements
- Risk assessment and mitigation strategies
- Rollback procedures and disaster recovery plans
- Monitoring and observability requirements
- Performance baselines and SLA definitions

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-deployment-planning-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for target_system, environment_scope, platform_target
3. **FOLLOW PROTOCOL**: Execute all phases according to the planning protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive planning documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% planning completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-deployment-planning-prompt"
arguments:
  target_system: "[system or application name]"
  environment_scope: "[single|multi-environment|full-pipeline|development-only|staging-production|all-environments]"
  platform_target: "[docker|kubernetes|cloud-native|hybrid-cloud|multi-platform|on-premises]"
  complexity_level: "[optional: simple|moderate|complex|enterprise]"
  compliance_requirements: "[optional: SOC2, ISO27001, GDPR, etc.]"
  timeline: "[optional: deployment timeline and constraints]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All planning phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive deployment planning completed
- [ ] All system components analyzed and documented (timestamped)
- [ ] Deployment strategy selected with clear rationale (timestamped)
- [ ] Risk assessment completed with mitigation strategies (timestamped)
- [ ] Infrastructure requirements defined with capacity planning (timestamped)
- [ ] Security and compliance planning completed (timestamped)
- [ ] Monitoring and observability designed (timestamped)
- [ ] CI/CD pipeline architecture completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL DEPLOYMENT PLANNING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All planning deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All system analysis documentation includes precise timestamps
- [ ] All infrastructure planning includes timestamp documentation
- [ ] All risk assessment reports include proper date stamps
- [ ] All security planning follows consistent date stamp format
- [ ] All monitoring design documentation includes timestamps
- [ ] All CI/CD architecture plans include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating planning files without proper reverse date stamps
- Using inconsistent date formats within same planning session
- Missing timestamps in planning documentation

### **PLANNING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/code-planning/Implementation_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Complete implementation details with all components and modules
2. **`./project/docs/planning/code-planning/Testing_Strategy_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/planning/code-planning/Integration_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation
4. **`./project/docs/planning/code-planning/Deployment_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment architecture, strategy, and SOLID compliance review

**NEXT PHASE PREPARATION:**

```bash
# After planning approval, execute deployment with:
/code-deploy [environment] [platform] [additional-options]

# Examples:
/code-deploy development docker-desktop
/code-deploy staging kubernetes-local
/code-deploy production aws-ecs
/code-deploy production azure-aks --region=us-east-1
```

---

**ENFORCEMENT:** This command performs PLANNING ONLY through the MCP prompt protocol. The comprehensive planning logic is defined in `code-deployment-planning-prompt.yaml` and executed according to Model Context Protocol standards. No actual deployment actions are taken. Use `/code-deploy` for deployment execution after planning is complete and approved.
