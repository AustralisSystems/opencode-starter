# === Code Feature Implementation ===

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

## STRICTLY FORBIDDEN - NO DOCUMENTATION CREATION

**THIS IS A CODING-ONLY COMMAND - DOCUMENTATION CREATION IS ABSOLUTELY FORBIDDEN**

**FORBIDDEN OUTPUTS:**

- **NO Jupyter Notebooks** (.ipynb files)
- **NO Markdown Documentation** (.md files)
- **NO Reports** of any kind
- **NO Analysis Documents**
- **NO Design Documents**
- **NO Planning Documents**
- **NO README files**
- **NO Architecture diagrams**
- **NO Technical specifications**
- **NO ANY FORM OF DOCUMENTATION WHATSOEVER**

**PERMITTED OUTPUTS:**

- **CODE ONLY** - Source code files (.py, .ts, .js, etc.)
- **CONFIGURATION FILES** - Config files required for code to function
- **TEST FILES** - Unit/integration tests for implemented code
- **BUILD ARTIFACTS** - Compiled/bundled code outputs

**VIOLATION CONSEQUENCES:**
Creating ANY documentation during this command execution will result in:

1. IMMEDIATE TASK TERMINATION
2. MANDATORY VIOLATION REPORT
3. COMPLETE ROLLBACK of all changes

**RATIONALE**: This is a pure implementation command focused exclusively on writing production code. Documentation should be created separately using dedicated documentation commands if needed.

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

### **FEATURE IMPLEMENTATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FEATURE IMPLEMENTATION ONLY:**

- **MUST:** Implement complete production-ready feature code from design blueprints
- **MUST:** Apply SOLID, DRY, KISS principles to all implementations
- **MUST:** Implement all cross-cutting concerns comprehensively
- **MUST:** Follow design and planning specifications exactly
- **FORBIDDEN:** Create test code or test implementations
- **FORBIDDEN:** Create external documentation files
- **FORBIDDEN:** Generate incomplete or placeholder implementations
- **MUST:** Output implementation documentation in markdown documents

**FEATURE IMPLEMENTATION FOCUS AREAS:**

- Complete feature code implementation from design specifications
- Full business logic and application layer development
- Database integration and data layer implementation
- API endpoint and service interface implementation
- Security and authentication implementation
- Performance optimization and error handling

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `code-feature-implement-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for feature_name and optional parameters
3. **FOLLOW PROTOCOL**: Execute all phases according to the implementation protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive implementation documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% implementation success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "code-feature-implement-prompt"
arguments:
  feature_name: "[name of the feature to implement]"
  implementation_scope: "[comprehensive|core-only|mvp|full-featured]"
  design_source: "[source of feature design specifications]"
  technology_stack: "[optional: specific technology stack requirements]"
  integration_context: "[optional: integration and dependency context]"
  quality_requirements: "[optional: quality and performance requirements]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All implementation phases completed according to protocol with timestamp tracking
- [ ] 100% feature functionality implemented from design specifications
- [ ] All business logic completely implemented and validated (timestamped)
- [ ] Complete data layer integration and database implementation (timestamped)
- [ ] All API endpoints and service interfaces implemented (timestamped)
- [ ] Security and authentication measures fully implemented (timestamped)
- [ ] Performance optimization and error handling completed (timestamped)
- [ ] Cross-cutting concerns and operational features implemented (timestamped)
- [ ] Production readiness validation completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**CODE FILES ONLY - NO DOCUMENTATION TIMESTAMPS NEEDED**

Since this is a coding-only command with NO documentation deliverables:

- Source code files follow project naming conventions
- Configuration files use standard formats
- Test files integrate with existing test suites
- Build artifacts follow build system conventions

**NO .ipynb files will be created** - therefore no timestamp requirements for documentation deliverables.

**FORBIDDEN:**

- Creating any documentation files (as per NO DOCUMENTATION mandate)
- Generating .ipynb or .md files during implementation
- Producing reports or analysis documents of any kind

### **FEATURE IMPLEMENTATION DELIVERABLES:**

**NO DOCUMENTATION DELIVERABLES - CODING ONLY COMMAND**

This command produces CODE ONLY:

- Source code files (.py, .ts, .js, etc.) in appropriate directories
- Configuration files as needed
- Test files for validation
- Build artifacts from compilation/bundling

**REMINDER**: This is a pure implementation command. NO Jupyter Notebooks, NO Markdown files, NO reports of any kind will be created. Documentation creation is STRICTLY FORBIDDEN per the protocol above.

**NEXT PHASE PREPARATION:**

```bash
# After implementation completion, proceed to validation with:
/code-quality-comprehensive [implementation-directory]

# Examples:
/code-quality-comprehensive ./src/features/user-auth
/code-quality-comprehensive ./src/features/payment-system
/code-quality-comprehensive ./src/features/dashboard
```

---

**ENFORCEMENT:** This command performs FEATURE IMPLEMENTATION ONLY through the MCP prompt protocol. The comprehensive implementation logic is defined in `code-feature-implement-prompt.yaml` and executed according to Model Context Protocol standards. No test code creation allowed. Use quality validation commands for code verification after implementation is complete and functional.
