# === Python Code Design: AI-Driven SOLID Principles and Architectural Pattern Implementation Protocol ===

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

### **PYTHON CODE DESIGN-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR PYTHON CODE DESIGN ONLY:**

- **MUST:** Create comprehensive Python architecture and design specifications
- **MUST:** Design complete SOLID principle implementations
- **MUST:** Apply SOLID, DRY, KISS principles to all Python designs
- **MUST:** Design modern Python patterns and architectural structures
- **FORBIDDEN:** Creating implementation code or actual Python modules
- **FORBIDDEN:** Creating test specifications or test designs
- **FORBIDDEN:** Generating incomplete or placeholder designs
- **MUST:** Output design documentation in markdown documents only

**PYTHON CODE DESIGN FOCUS AREAS:**

- Python class architecture and component design
- Abstract base class and interface specifications
- Design pattern implementations (Factory, Strategy, Observer, etc.)
- Dataclass and modern Python feature architecture
- Type hint and static analysis design
- Error handling and exception architecture
- Async programming pattern design

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `python-code-design-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for design_scope and architecture_type
3. **FOLLOW PROTOCOL**: Execute all phases according to the design protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive Python code design documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% design completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "python-code-design-prompt"
arguments:
  design_scope: "[application-wide|module-specific|class-hierarchy|interface-design]"
  architecture_type: "[layered|hexagonal|clean-architecture|mvc|mvp]"
  pattern_focus: "[optional: creational|structural|behavioral|architectural]"
  python_features: "[optional: dataclasses|abc|typing|async|decorators]"
  complexity_level: "[optional: simple|moderate|complex|enterprise]"
  domain_focus: "[optional: web-api|data-processing|cli-tool|library]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All design phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive Python architecture designed
- [ ] Complete Python class and interface specifications created (timestamped)
- [ ] SOLID principles implementation patterns fully designed (timestamped)
- [ ] Design patterns architecture completely specified (timestamped)
- [ ] Modern Python features architecture documented (timestamped)
- [ ] Type system and static analysis designed (timestamped)
- [ ] Error handling and async patterns specified (timestamped)
- [ ] SOLID/DRY/KISS principles applied throughout (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL PYTHON CODE DESIGN OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All design deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All architecture documentation includes precise timestamps
- [ ] All technical specifications include timestamp documentation
- [ ] All class design documents include proper date stamps
- [ ] All SOLID principle implementations follow consistent date stamp format
- [ ] All design pattern implementations include timestamps
- [ ] All Python feature designs include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating design files without proper reverse date stamps
- Using inconsistent date formats within same design session
- Missing timestamps in design documentation

### **PYTHON CODE DESIGN DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/python-design/Architecture_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Architecture Design with technical specifications and implementation details
2. **`./project/docs/planning/python-design/Security_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Security Design with technical specifications and implementation details
3. **`./docs/design-patterns/Integration_Patterns_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation (enduring)
4. **`./project/docs/planning/python-design/Performance_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Performance Design with technical specifications and implementation details
5. **`./project/docs/planning/python-design/Deployment_Architecture_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment Architecture with technical specifications and implementation details

**NEXT PHASE PREPARATION:**

```bash
# After design approval, proceed to planning with:
/python-code-implementation-planning [component-name] [complexity] [architecture-context]

# Examples:
/python-code-implementation-planning user-service enterprise clean-architecture
/python-code-implementation-planning data-processor moderate layered
/python-code-implementation-planning api-client simple mvc
```

---

**ENFORCEMENT:** This command performs PYTHON CODE DESIGN ONLY through the MCP prompt protocol. The comprehensive design logic is defined in `python-code-design-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use planning commands for implementation planning after design is complete and approved.
