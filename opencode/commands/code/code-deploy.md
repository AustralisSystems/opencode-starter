# === Code Deployment Execution: Environment-Specific Deployment Orchestration ===

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

### **DEPLOYMENT-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR DEPLOYMENT EXECUTION ONLY:**

- **MUST:** Execute actual deployment to specified environment and platform
- **MUST:** Build, deploy, and validate the application
- **MUST:** Perform health checks and verification
- **FORBIDDEN:** Create extensive planning documentation
- **FORBIDDEN:** Perform comprehensive analysis (use `/code-deployment-planning` first)
- **MUST:** Focus on deployment execution and validation

**DEPLOYMENT EXECUTION FOCUS:**

- Build and deploy application components
- Execute deployment strategy (blue-green, canary, rolling)
- Validate deployment success through health checks
- Monitor deployment progress and handle failures
- Perform post-deployment verification
- Execute rollback if deployment fails

**IF BUILD/DEPLOY ISSUES OCCUR:**

- Follow debugging protocol in `./.claude/commands/code/code-debug.md`
- Use refactoring protocol in `./.claude/commands/code/code-refactor.md`
- Apply planning protocol in `./.claude/commands/code/code-planning.md`
- Implement fixes per `./.claude/commands/code/code-implement.md`
- Ensure security compliance per `./.claude/commands/code/code-security-analysis.md`

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-deploy-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for environment, platform, additional_options
3. **FOLLOW PROTOCOL**: Execute all phases according to the deployment protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive deployment documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% deployment success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-deploy-prompt"
arguments:
  environment: "[dev|development|test|testing|stage|staging|prod|production]"
  platform: "[docker-desktop|docker|kubernetes|k8s|aws|azure|gcp|local]"
  additional_options: "[optional: region, cluster, etc.]"
  build_tag: "[optional: custom build tag]"
  rollback_enabled: "[optional: true/false]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All deployment phases completed according to protocol with timestamp tracking
- [ ] 100% successful deployment to target environment and platform
- [ ] All health checks passed and services are running (timestamped)
- [ ] Comprehensive deployment documentation created with reverse date stamps
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL DEPLOYMENT OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All deployment reports (.md) have reverse date stamps in filenames
- [ ] All build artifact logs include precise timestamps
- [ ] All health check results include timestamp documentation
- [ ] All deployment validation reports include proper date stamps
- [ ] All monitoring setup guides follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating deployment files without proper reverse date stamps
- Using inconsistent date formats within same deployment session
- Missing timestamps in deployment documentation

---

**ENFORCEMENT:** This command performs DEPLOYMENT EXECUTION ONLY through the MCP prompt protocol. The comprehensive deployment logic is defined in `code-deploy-prompt.yaml` and executed according to Model Context Protocol standards. Use `/code-deployment-planning` for planning and comprehensive documentation. Focus on build, deploy, validate cycle with proper timestamp documentation and reverse date stamp requirements.
