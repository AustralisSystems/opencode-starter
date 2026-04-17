# Dependency Management & Security Command

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

**Documentation & Code Research (MANDATORY BEFORE DEPENDENCY MANAGEMENT):**

- `context7` - Up-to-date documentation from official sources - MANDATORY
- `grep` - GitHub code examples and implementations - MANDATORY

**File & Web Operations:**

- `filesystem` - File read/write operations - MANDATORY
- `fetch` - HTTP/HTTPS content retrieval - MANDATORY
- `time` - Timestamp and time operations - MANDATORY for reverse date stamp generation

### MCP EXECUTION SEQUENCE (REQUIRED)

```

  START DEPENDENCY MANAGEMENT

  1. CONTEXT LOAD (neo4j-memory + memory)

  2.  MANDATORY RESEARCH (context7 + grep)

  3. PLANNING (sequential-thinking)

  4. DEPENDENCY FIXES (filesystem + domain tools)

  5. PROGRESS TRACKING (neo4j-memory + memory)

  6. CONTEXT SAVE (neo4j-memory + memory)

  END DEPENDENCY MANAGEMENT

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

Update dependencies, resolve version conflicts, and address security advisories in project dependencies.

## Context

This command systematically manages project dependencies to ensure security, compatibility, and optimal performance.

## Dependency Management Areas

### 1. Security Updates

- **CVE Remediation**: Update packages with known vulnerabilities
- **Security Advisories**: Address GitHub/npm security alerts
- **Vulnerability Scanning**: Identify and patch security issues
- **Supply Chain Security**: Verify package integrity

### 2. Version Conflict Resolution

- **Dependency Hell**: Resolve conflicting version requirements
- **Transitive Dependencies**: Manage indirect dependency conflicts
- **Version Pinning**: Balance stability with security updates
- **Compatibility Testing**: Ensure updates don't break functionality

### 3. Dependency Optimization

- **Unused Dependencies**: Remove unnecessary packages
- **Bundle Size**: Optimize for production deployment
- **Performance**: Choose faster alternative packages
- **Licensing**: Ensure license compatibility

## Implementation Protocol

### Phase 1: Security Assessment

1. **Vulnerability Scanning**:

   ```bash
   # Python security scan
   safety check --json --output security-report.json
   pip-audit --format=json --output=audit-report.json

   # Node.js security scan
   npm audit --json > npm-security-report.json
   yarn audit --json > yarn-security-report.json
   ```

2. **Dependency Analysis**:

   ```bash
   # Python dependency tree
   pipdeptree --json > python-deps.json

   # Node.js dependency tree
   npm list --json > node-deps.json
   ```

### Phase 2: Security Updates

1. **Critical Vulnerability Fixes**:

   ```bash
   # Update packages with critical CVEs
   safety check --json | jq -r '.vulnerabilities[] | select(.vulnerability.severity == "high" or .vulnerability.severity == "critical") | .package_name' | xargs pip install --upgrade

   # Node.js security fixes
   npm audit fix --force
   ```

2. **Systematic Updates**:
   - Update packages with security advisories
   - Test functionality after each update
   - Document security improvements

### Phase 3: Conflict Resolution

1. **Version Conflict Detection**:

   ```bash
   # Check for conflicts
   pip check
   npm ls --depth=0 | grep UNMET
   ```

2. **Resolution Strategies**:
   - **Pin Compatible Versions**: Lock to specific working versions
   - **Update Dependencies**: Upgrade to resolve conflicts
   - **Alternative Packages**: Replace problematic dependencies
   - **Virtual Environments**: Isolate conflicting requirements

### Phase 4: Optimization

1. **Cleanup Unused Dependencies**:

   ```bash
   # Python unused packages
   pip-autoremove --list

   # Node.js unused packages
   depcheck --json
   ```

2. **Performance Optimization**:
   - Choose lightweight alternatives
   - Remove development dependencies from production
   - Bundle optimization for deployment

## Dependency Categories

### Critical Dependencies

- **Core Framework**: Essential runtime dependencies
- **Security Libraries**: Authentication, encryption, validation
- **Database Drivers**: Data persistence layers
- **Communication**: API clients, networking libraries

### Development Dependencies

- **Testing Frameworks**: Unit testing, integration testing
- **Build Tools**: Compilation, bundling, optimization
- **Quality Tools**: Linting, formatting, analysis
- **Documentation**: API docs, static site generators

### Optional Dependencies

- **Monitoring**: Logging, metrics, tracing
- **Utilities**: Helper libraries, convenience functions
- **UI Components**: Frontend components, styling
- **Development Aids**: Debugging, profiling tools

## Security Priorities

### High Priority Updates

- **Critical CVEs**: CVSS score 9.0
- **Remote Code Execution**: Any RCE vulnerabilities
- **Authentication Bypass**: Auth-related vulnerabilities
- **Data Exposure**: Information disclosure issues

### Medium Priority Updates

- **High CVEs**: CVSS score 7.0-8.9
- **Privilege Escalation**: Local privilege issues
- **Denial of Service**: DoS vulnerabilities
- **Cross-Site Scripting**: XSS vulnerabilities

### Low Priority Updates

- **Medium CVEs**: CVSS score 4.0-6.9
- **Information Disclosure**: Minor info leaks
- **Configuration Issues**: Misconfiguration vulnerabilities
- **Legacy Warnings**: Deprecated API usage

## Success Criteria

- All critical and high severity vulnerabilities resolved
- No version conflicts in dependency tree
- All dependencies updated to secure versions
- Unused dependencies removed
- License compatibility verified
- Application functionality maintained after updates

## Error Handling

### Update Failure Scenarios

- **Breaking API Changes**: Test and adapt to new APIs
- **Version Incompatibilities**: Use compatible version ranges
- **Build Failures**: Resolve compilation/build issues
- **Runtime Errors**: Fix code that depends on changed behavior

### Rollback Procedures

- **Dependency Snapshots**: Maintain pre-update state
- **Version Locking**: Pin working versions
- **Environment Isolation**: Use virtual environments
- **Incremental Updates**: Update one dependency at a time

## Execution Steps

1. **Pre-Update Assessment**:

   ```bash
   # Create dependency snapshots
   pip freeze > requirements-backup.txt
   npm shrinkwrap  # or yarn.lock backup

   # Run test suite
   pytest --tb=short
   npm test
   ```

2. **Security-First Updates**:

   - Address critical vulnerabilities first
   - Test thoroughly after each security update
   - Document security improvements

3. **Systematic Dependency Updates**:

   - Update dependencies by category
   - Resolve conflicts systematically
   - Maintain functionality throughout

4. **Post-Update Validation**:

   ```bash
   # Verify no vulnerabilities remain
   safety check
   npm audit

   # Run comprehensive tests
   pytest --cov=. --cov-report=html
   npm test -- --coverage
   ```

## Output Requirements

Generate comprehensive dependency management report:

```json
{
  "dependency_updates": {
    "security_updates": 0,
    "version_upgrades": 0,
    "packages_removed": 0,
    "conflicts_resolved": 0
  },
  "security_improvements": {
    "vulnerabilities_fixed": 0,
    "severity_breakdown": {
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0
    },
    "security_score_improvement": "+15%"
  },
  "conflict_resolutions": [
    {
      "package": "package-name",
      "issue": "version conflict",
      "resolution": "upgraded to compatible version",
      "version_before": "1.0.0",
      "version_after": "2.1.0"
    }
  ],
  "optimization_results": {
    "bundle_size_reduction": "2.3MB",
    "unused_packages_removed": 8,
    "performance_improvement": "+12%"
  }
}
```

## MCP PROTOCOL COMPLIANCE REQUIREMENTS

**MANDATORY REQUIREMENTS FOR ALL DEPENDENCY MANAGEMENT OPERATIONS:**

1. ** ALWAYS use context7 BEFORE dependency management** - Get current, accurate documentation for dependency patterns
2. ** ALWAYS use grep to search GitHub** - Find real production examples of dependency management
3. ** ALWAYS record actions in neo4j-memory and memory AS YOU WORK** - Document everything
4. ** ALWAYS save to neo4j-memory and memory** - Preserve for future sessions
5. **NEVER skip the Context Load phase** - Always start by loading relevant context
6. **NEVER manage dependencies without Research phase** - context7 + grep are MANDATORY
7. **NEVER complete without Context Save** - Always persist learnings and decisions

**THE GOLDEN RULE: context7 (docs) grep (examples) memory (record) manage memory (persist)**

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
2. MANDATORY: Research using context7 and grep for latest dependency management patterns
3. Perform security vulnerability scanning and assessment
4. Execute security-first updates for critical vulnerabilities
5. Resolve version conflicts and dependency incompatibilities
6. Optimize dependencies and remove unused packages
7. Validate functionality preservation and performance
8. Generate comprehensive dependency management report with timestamps
9. MANDATORY: Save all management actions and decisions to neo4j-memory and memory
10. MANDATORY: Use reverse date stamps for all output files

Follow secure dependency management practices and maintain application stability throughout the update process.
