# === FastAPI Implementation Planning: AI-Driven FastAPI Application Implementation Planning Protocol ===

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
   - Use web search for latest FastAPI documentation
   - Find official FastAPI docs and examples
   - Search GitHub for FastAPI production implementations
   - Review industry FastAPI best practices
   - Study similar successful FastAPI projects
   - Check Stack Overflow for common FastAPI patterns

**SEARCH PRIORITIES:**

- Official FastAPI documentation (latest version)
- GitHub repositories with high stars using FastAPI
- Industry standard FastAPI implementations
- Recent FastAPI blog posts/tutorials (< 1 year old)
- Community FastAPI best practices

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **FASTAPI IMPLEMENTATION PLANNING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI IMPLEMENTATION PLANNING ONLY:**

- **MUST:** Create exhaustive implementation planning for FastAPI applications
- **MUST:** Perform comprehensive reuse analysis of existing FastAPI code
- **MUST:** Create detailed task breakdown with FastAPI-specific dependencies
- **MUST:** Plan FastAPI quality gates and validation workflows
- **FORBIDDEN:** Creating implementation code or actual FastAPI modules
- **FORBIDDEN:** Creating external documentation files
- **FORBIDDEN:** Generating test planning or test specifications
- **MUST:** Output planning documentation in markdown documents only

**FASTAPI IMPLEMENTATION PLANNING FOCUS AREAS:**

- Comprehensive FastAPI application architecture planning and requirements
- Task decomposition and dependency mapping for FastAPI components
- Resource estimation and timeline planning for API development
- FastAPI-specific pattern implementation planning
- Database integration and ORM implementation planning
- Authentication/authorization middleware planning
- API endpoint and router implementation planning
- Performance optimization and caching planning
- Testing strategy and quality assurance planning

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-implementation-planning-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for api_name and complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the FastAPI planning protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive FastAPI planning documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% planning completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-implementation-planning-prompt"
arguments:
  api_name: "[name of the FastAPI application to plan]"
  api_complexity: "[simple-crud|complex-business|enterprise|high-performance]"
  architecture_context: "[clean-architecture|hexagonal|layered|microservice|monolithic]"
  planning_scope: "[optional: comprehensive|focused|mvp|full-feature]"
  database_requirements: "[optional: postgresql|mongodb|sqlite|multiple-db]"
  authentication_needs: "[optional: jwt|oauth2|api-key|rbac|multi-auth]"
  deployment_strategy: "[optional: container|kubernetes|serverless|traditional]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All FastAPI planning phases completed according to protocol with timestamp tracking
- [ ] 100% FastAPI application requirements analyzed and documented
- [ ] Complete task breakdown with FastAPI-specific dependencies created (timestamped)
- [ ] Resource estimation and timeline planning completed (timestamped)
- [ ] Risk assessment and mitigation strategies defined (timestamped)
- [ ] Quality gates and validation workflows planned (timestamped)
- [ ] Implementation roadmap with FastAPI milestones established (timestamped)
- [ ] Code reuse analysis and integration planning completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FASTAPI IMPLEMENTATION PLANNING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All planning deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All framework analysis documentation includes precise timestamps
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

### **FASTAPI IMPLEMENTATION PLANNING DELIVERABLES:**

**NO DOCUMENTATION DELIVERABLES - CODING ONLY COMMAND**

This command produces CODE ONLY:

- Source code files (.py, .ts, .js, etc.) in appropriate directories
- Configuration files as needed
- Test files for validation
- Build artifacts from compilation/bundling

**REMINDER**: This is a pure implementation command. NO Jupyter Notebooks, NO Markdown files, NO reports of any kind will be created. Documentation creation is STRICTLY FORBIDDEN per the protocol above.

**NEXT PHASE PREPARATION:**

```bash
# After planning approval, proceed to implementation with:
/fastapi-application-implement [api-name] [implementation-scope] [design-source]

# Examples:
/fastapi-application-implement user-api comprehensive design-specifications
/fastapi-application-implement order-service core-only architecture-documents
/fastapi-application-implement simple-crud mvp planning-requirements
```

## Command Integration

### Related Commands

- **Architecture Phase**: `/fastapi-architecture-design` - Overall application architecture design
- **API Design**: `/fastapi-api-endpoint-design` - RESTful API endpoint specifications
- **Service Patterns**: `/fastapi-service-dependency-patterns` - Service architecture patterns
- **Implementation**: `/fastapi-application-implement` - Full application implementation
- **Router Implementation**: `/fastapi-router-implement` - Router-specific implementation
- **Service Implementation**: `/fastapi-service-implement` - Service layer implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - Implementation quality validation

### Workflow Navigation

```
Architecture Design  Implementation Planning  API/Service Design  Implementation  Quality Review

   Domain Models      Task Breakdown      Detailed Design      Production Code   Validation
```

### Next Phase Commands

After completing implementation planning, proceed with:

1. `/fastapi-api-endpoint-design` - Design specific API endpoints
2. `/fastapi-service-dependency-patterns` - Define service patterns
3. `/fastapi-application-implement` - Begin full implementation
4. `/fastapi-router-implement` or `/fastapi-service-implement` - Focused implementations

---

**ENFORCEMENT:** This command performs FASTAPI IMPLEMENTATION PLANNING ONLY through the MCP prompt protocol. The comprehensive planning logic is defined in `fastapi-implementation-planning-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use implementation commands for actual FastAPI development after planning is complete and approved.

---
