# Critical Issue Remediation Command

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ AND INDEX**: `C:\github_development\ai-agents\.claude\commands\ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

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

## MCP TOOLS REQUIREMENTS

**MANDATORY PROTOCOL REFERENCE**: You MUST use designated MCP tools for all operations:

### Core MCP Tools (MANDATORY)

**Core Memory & Thinking:**

- `neo4j-memory` - Enduring LLM Memory Knowledge Graph - MANDATORY
- `memory` - Temporal LLM Memory Knowledge Graph - MANDATORY
- `sequential-thinking` - Structured reasoning and planning - MANDATORY

**Documentation & Code Research (MANDATORY BEFORE FIXING):**

- `context7` - Up-to-date documentation from official sources - MANDATORY
- `grep` - GitHub code examples and implementations - MANDATORY

**File & Web Operations:**

- `filesystem` - File read/write operations - MANDATORY
- `fetch` - HTTP/HTTPS content retrieval - MANDATORY
- `time` - Timestamp and time operations - MANDATORY for reverse date stamp generation

### MCP EXECUTION SEQUENCE (REQUIRED)

```

  START CRITICAL FIXES

  1. CONTEXT LOAD (neo4j-memory + memory)

  2.  MANDATORY RESEARCH (context7 + grep)

  3. PLANNING (sequential-thinking)

  4. CRITICAL FIXES (filesystem + domain tools)

  5. PROGRESS TRACKING (neo4j-memory + memory)

  6. CONTEXT SAVE (neo4j-memory + memory)

  END CRITICAL FIXES

```

** CRITICAL: NEVER SKIP THE RESEARCH PHASE - IT PREVENTS AI HALLUCINATIONS**

### MCP MEMORY REQUIREMENTS

**ABSOLUTELY MANDATORY - ZERO EXCEPTIONS ALLOWED**

YOU MUST ALWAYS use **Neo4j Memory** (`neo4j-memory`) and **Memory** (`memory`) for ALL memory operations:

- **Enduring Memory**: `neo4j-memory` - MANDATORY for persistent knowledge storage with reverse date stamps
- **Session Memory**: `memory` - MANDATORY for temporal tracking with timestamps
- **Session Tracking**: Track all actions, outcomes, and decisions with timestamps
- **Knowledge Persistence**: Save all learnings and patterns with date stamps
- **Context Loading**: Load previous session context before starting (with date filtering)
- **Cross-Session Memory**: Maintain knowledge across all sessions with timestamp tracking

**MANDATORY DATE STAMP REQUIREMENTS:**

- "MANDATORY: All memory operations MUST include reverse date stamp YYYY-MM-DD-HHMMSS"
- "MANDATORY: Use UTC timestamps for all memory entries and operations"
- "MANDATORY: Include date stamps in all entity creation and relationship mapping"
- "FORBIDDEN: Memory operations without proper timestamp documentation"

**FAILURE TO USE MCP MEMORY WILL RESULT IN IMMEDIATE TASK TERMINATION**

## Objective

Immediately fix critical issues that prevent code compilation and execution.

## Context

This command addresses blocking issues identified in the quality analysis phase that must be resolved before any other remediation can proceed.

## Critical Issue Types

### 1. Syntax Errors

- Malformed f-strings
- Missing parentheses, brackets, braces
- Incorrect indentation
- Invalid character encoding

### 2. Import/Dependency Failures

- Missing required packages
- Circular import dependencies
- Incorrect module paths
- Version compatibility issues

### 3. Compilation Blockers

- Type annotation errors preventing static analysis
- Missing required files or resources
- Configuration file syntax errors
- Environment variable dependencies

## Remediation Protocol

### Phase 1: Syntax Error Resolution

1. **Scan for Syntax Issues**:

   - Run `python -m py_compile` on all Python files
   - Parse AST compilation errors
   - Identify specific line numbers and error types

2. **Apply Surgical Fixes**:

   - Fix malformed f-strings with proper closing braces
   - Correct indentation using consistent spacing
   - Add missing imports and remove unused ones
   - Resolve character encoding issues

3. **Validation**:
   - Verify each file compiles successfully
   - Ensure no new syntax errors introduced
   - Maintain original code functionality

### Phase 2: Dependency Resolution

1. **Dependency Analysis**:

   - Parse `requirements.txt`, `pyproject.toml`, `package.json`
   - Identify missing packages and version conflicts
   - Check for circular dependencies

2. **Package Management**:

   - Install missing required packages
   - Update packages with security vulnerabilities
   - Resolve version conflicts systematically

3. **Import Validation**:
   - Test all import statements
   - Fix relative import paths
   - Resolve module not found errors

### Phase 3: Configuration Fixes

1. **Environment Setup**:

   - Validate environment variable requirements
   - Check configuration file syntax
   - Ensure required directories exist

2. **Resource Verification**:
   - Confirm all referenced files exist
   - Validate database connections
   - Check external service dependencies

## Implementation Guidelines

### Code Safety Protocols

- **Atomic Changes**: Fix one issue at a time
- **Backup Strategy**: Create backup before each fix
- **Validation Testing**: Compile and test after each change
- **Rollback Capability**: Maintain ability to undo changes

### Quality Standards

- **Minimal Changes**: Make only necessary modifications
- **Preserve Functionality**: Maintain original code behavior
- **Follow Conventions**: Use existing project style patterns
- **Documentation**: Add comments for non-obvious fixes

## Execution Steps

1. **Critical Issue Assessment**:

   ```bash
   # Compile all Python files
   find . -name "*.py" -exec python -m py_compile {} \;

   # Check for missing dependencies
   pip check

   # Validate configuration files
   python -m json.tool config.json
   ```

2. **Surgical Remediation**:

   - Address each critical issue individually
   - Test compilation after each fix
   - Document changes for audit trail

3. **Validation Protocol**:
   - Run comprehensive compilation check
   - Verify application can start
   - Confirm no regressions introduced

## Success Criteria

- All Python files compile without syntax errors
- All required dependencies are installed and accessible
- Application can start without critical failures
- No new critical issues introduced during remediation
- All fixes documented and auditable

## Error Handling

### Fix Failure Scenarios

- **Syntax Fix Breaks Logic**: Rollback and flag for manual review
- **Dependency Conflicts**: Use virtual environment isolation
- **Configuration Errors**: Restore from backup configuration
- **Resource Missing**: Create minimal required resources

### Escalation Triggers

- Multiple syntax errors in same file
- Dependency conflicts requiring architectural changes
- Configuration requiring manual intervention
- Resource dependencies on external systems

## Output Requirements

Generate detailed remediation report:

```json
{
  "critical_fixes_applied": {
    "syntax_errors_fixed": 0,
    "dependencies_resolved": 0,
    "configuration_fixes": 0,
    "total_critical_fixes": 0
  },
  "compilation_status": {
    "files_checked": 0,
    "compilation_success": true,
    "remaining_errors": 0,
    "error_details": []
  },
  "fix_details": [
    {
      "file": "path/to/file.py",
      "issue_type": "syntax_error",
      "fix_applied": "corrected malformed f-string",
      "lines_modified": [669],
      "backup_created": true
    }
  ],
  "next_actions": [
    "Proceed to security issue remediation",
    "Run comprehensive test suite"
  ]
}
```

## MCP PROTOCOL COMPLIANCE REQUIREMENTS

**MANDATORY REQUIREMENTS FOR ALL CRITICAL FIX OPERATIONS:**

1. ** ALWAYS use context7 BEFORE fixing** - Get current, accurate documentation for critical issue patterns
2. ** ALWAYS use grep to search GitHub** - Find real production examples of critical issue fixes
3. ** ALWAYS record actions in neo4j-memory and memory AS YOU WORK** - Document everything
4. ** ALWAYS save to neo4j-memory and memory** - Preserve for future sessions
5. **NEVER skip the Context Load phase** - Always start by loading relevant context
6. **NEVER fix without Research phase** - context7 + grep are MANDATORY
7. **NEVER complete without Context Save** - Always persist learnings and decisions

**THE GOLDEN RULE: context7 (docs) grep (examples) memory (record) fix memory (persist)**

## MANDATORY REVERSE DATE STAMP REQUIREMENTS

**ALL OUTPUT FILES AND DOCUMENTATION MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

**MANDATORY REQUIREMENTS:**

- "MANDATORY: Use reverse date stamp format YYYY-MM-DD-HHMMSS for ALL output files"
- "MANDATORY: Include UTC timestamps in all documentation and deliverables"
- "MANDATORY: Apply consistent date stamp format across all session outputs"
- "MANDATORY: Use time MCP tool to generate proper timestamps"
- "MANDATORY: Include date stamps in all memory operations and file creation"

**FORBIDDEN:**

- "FORBIDDEN: Creating any output files without proper reverse date stamps"
- "FORBIDDEN: Using inconsistent date formats within same session"
- "FORBIDDEN: Missing timestamps in any documentation or deliverables"

# Execution Workflow

execution_steps: |

1. MANDATORY: Load context from neo4j-memory and memory before starting
2. MANDATORY: Research using context7 and grep for latest critical fix patterns
3. Scan for critical syntax errors and compilation blockers
4. Apply surgical fixes with atomic changes and validation
5. Resolve dependency conflicts and missing packages
6. Fix configuration and environment setup issues
7. Validate compilation success and functionality preservation
8. Generate comprehensive remediation report with timestamps
9. MANDATORY: Save all fixes and decisions to neo4j-memory and memory
10. MANDATORY: Use reverse date stamps for all output files

Follow canonical protocol compliance and maintain production-ready code quality throughout the remediation process.
