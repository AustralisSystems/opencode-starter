# === FastAPI Architecture Design: AI-Driven Modern FastAPI Application Design Protocol ===

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

### **FASTAPI ARCHITECTURE DESIGN-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI ARCHITECTURE DESIGN ONLY:**

- **MUST:** Create comprehensive FastAPI application architecture and design specifications
- **MUST:** Design complete modern FastAPI patterns and architectural structures
- **MUST:** Apply Clean Architecture, Hexagonal, and DDD principles to FastAPI designs
- **MUST:** Design FastAPI-specific patterns (dependency injection, middleware, routers)
- **FORBIDDEN:** Creating implementation code or actual FastAPI modules
- **FORBIDDEN:** Creating test specifications or test designs
- **FORBIDDEN:** Generating incomplete or placeholder designs
- **MUST:** Output design documentation in markdown documents only

**FASTAPI ARCHITECTURE DESIGN FOCUS AREAS:**

- FastAPI application structure and layered architecture design
- API router organization and endpoint design patterns
- FastAPI dependency injection and service layer architecture
- Database integration with SQLModel/SQLAlchemy design
- Authentication/authorization middleware design
- Request/response schema design with Pydantic models
- Async programming patterns for FastAPI
- Performance optimization and caching strategies design
- OpenAPI/Swagger documentation architecture
- Testing strategy design for FastAPI applications

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-architecture-design-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for design_scope and api_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the FastAPI design protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive FastAPI architecture design documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% design completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-architecture-design-prompt"
arguments:
  design_scope: "[api-application|microservice|monolithic|distributed-system]"
  api_complexity: "[simple-crud|complex-business|enterprise|high-performance]"
  architecture_pattern: "[optional: clean-architecture|hexagonal|layered|event-driven]"
  database_integration: "[optional: postgresql|mongodb|sqlite|multiple]"
  authentication_type: "[optional: jwt|oauth2|api-key|session-based]"
  deployment_target: "[optional: container|serverless|traditional|kubernetes]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All FastAPI design phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive FastAPI architecture designed
- [ ] Complete API router and endpoint specifications created (timestamped)
- [ ] FastAPI dependency injection patterns fully designed (timestamped)
- [ ] Database integration architecture completely specified (timestamped)
- [ ] Authentication/authorization middleware designed (timestamped)
- [ ] Pydantic schema and validation architecture documented (timestamped)
- [ ] Async programming patterns specified (timestamped)
- [ ] Performance and caching strategies designed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FASTAPI ARCHITECTURE DESIGN OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All design deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All architecture documentation includes precise timestamps
- [ ] All technical specifications include timestamp documentation
- [ ] All API design documents include proper date stamps
- [ ] All FastAPI pattern implementations follow consistent date stamp format
- [ ] All database integration designs include timestamps
- [ ] All authentication designs include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating design files without proper reverse date stamps
- Using inconsistent date formats within same design session
- Missing timestamps in design documentation

### **FASTAPI ARCHITECTURE DESIGN DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/python-design/Architecture_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Architecture Design with technical specifications and implementation details
2. **`./project/docs/planning/python-design/Security_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Security Design with technical specifications and implementation details
3. **`./docs/design-patterns/Integration_Patterns_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation (enduring)
4. **`./project/docs/planning/python-design/Performance_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Performance Design with technical specifications and implementation details
5. **`./project/docs/planning/python-design/Deployment_Architecture_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment Architecture with technical specifications and implementation details

**NEXT PHASE PREPARATION:**

```bash
# After design approval, proceed to planning with:
/fastapi-implementation-planning [api-name] [complexity] [architecture-context]

# Examples:
/fastapi-implementation-planning user-api enterprise clean-architecture
/fastapi-implementation-planning order-service complex hexagonal
/fastapi-implementation-planning simple-crud simple layered
```

## Command Integration

### Related Commands

- **Planning Phase**: `/fastapi-implementation-planning` - Implementation roadmap and task breakdown
- **API Design**: `/fastapi-api-endpoint-design` - RESTful API endpoint specifications
- **Service Patterns**: `/fastapi-service-dependency-patterns` - Service architecture patterns
- **Implementation**: `/fastapi-application-implement` - Full application implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - Architecture compliance validation

### Workflow Navigation

```
Architecture Design  Implementation Planning  API Design  Implementation  Quality Review

   Domain Models      Task Breakdown      API Contracts    Production Code   Validation
```

### Next Phase Commands

After completing architecture design, proceed with:

1. `/fastapi-implementation-planning` - Create detailed implementation roadmap
2. `/fastapi-api-endpoint-design` - Design specific API endpoints
3. `/fastapi-service-dependency-patterns` - Define service patterns

---

**ENFORCEMENT:** This command performs FASTAPI ARCHITECTURE DESIGN ONLY through the MCP prompt protocol. The comprehensive design logic is defined in `fastapi-architecture-design-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use planning commands for implementation planning after design is complete and approved.

---
