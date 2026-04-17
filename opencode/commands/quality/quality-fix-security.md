# Security Issue Remediation Command

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

## Objective

Remediate security vulnerabilities and implement safety best practices throughout the codebase.

## Context

This command addresses security issues identified in quality analysis, focusing on eliminating vulnerabilities and strengthening security posture.

## Security Issue Categories

### 1. Input Validation Vulnerabilities

- SQL injection possibilities
- Command injection risks
- Path traversal vulnerabilities
- XSS attack vectors

### 2. Authentication/Authorization Issues

- Missing authentication checks
- Weak password policies
- Insufficient access controls
- Session management flaws

### 3. Data Protection Violations

- Hardcoded secrets and credentials
- Insecure data transmission
- Inadequate encryption
- Information disclosure

### 4. Dependency Vulnerabilities

- Packages with known CVEs
- Outdated security patches
- Vulnerable transitive dependencies
- Supply chain risks

## Security Remediation Protocol

### Phase 1: Critical Vulnerability Fixes

1. **Immediate Threat Mitigation**:

   - Remove hardcoded passwords, API keys, tokens
   - Fix SQL injection vulnerabilities
   - Eliminate command injection risks
   - Secure file upload mechanisms

2. **Input Sanitization**:

   - Implement input validation for all user data
   - Add parameterized queries for database operations
   - Sanitize file paths and names
   - Validate API input parameters

3. **Secret Management**:
   - Move secrets to environment variables
   - Implement secure credential storage
   - Add secret scanning prevention
   - Update .gitignore for sensitive files

### Phase 2: Authentication & Authorization

1. **Access Control Enhancement**:

   - Implement proper authentication mechanisms
   - Add role-based authorization
   - Secure API endpoints
   - Validate session management

2. **Security Headers**:
   - Add security-related HTTP headers
   - Implement CORS policies
   - Configure CSP headers
   - Enable HSTS where applicable

### Phase 3: Data Protection

1. **Encryption Implementation**:

   - Encrypt sensitive data at rest
   - Use TLS for data in transit
   - Implement proper key management
   - Secure communication channels

2. **Privacy Controls**:
   - Remove or mask PII in logs
   - Implement data retention policies
   - Add privacy consent mechanisms
   - Secure data backup procedures

### Phase 4: Dependency Security

1. **Vulnerability Scanning**:

   - Update packages with security fixes
   - Remove unused dependencies
   - Pin dependency versions
   - Monitor for new vulnerabilities

2. **Supply Chain Security**:
   - Verify package integrity
   - Use trusted package sources
   - Implement dependency approval process
   - Regular security audits

## Implementation Guidelines

### Security by Design Principles

- **Least Privilege**: Grant minimum required permissions
- **Defense in Depth**: Multiple security layers
- **Fail Secure**: Secure defaults and failure modes
- **Zero Trust**: Verify everything, trust nothing

### Code Security Patterns

- **Input Validation**: Validate all external input
- **Output Encoding**: Encode all output appropriately
- **Error Handling**: Avoid information disclosure
- **Logging**: Secure audit trails without sensitive data

## Execution Steps

1. **Security Assessment**:

   ```bash
   # Run security scanners
   bandit -r . -f json -o security-report.json
   safety check --json
   semgrep --config=p/security-audit .
   ```

2. **Vulnerability Remediation**:

   - Address each security issue by severity
   - Test security controls after implementation
   - Verify no new vulnerabilities introduced

3. **Security Validation**:
   - Re-run security scanners
   - Perform penetration testing
   - Validate security controls

## Security Fix Categories

### High Priority Fixes

- **SQL Injection**: Use parameterized queries
- **Command Injection**: Sanitize command inputs
- **XSS**: Implement output encoding
- **CSRF**: Add CSRF tokens
- **Authentication Bypass**: Strengthen auth checks

### Medium Priority Fixes

- **Information Disclosure**: Secure error messages
- **Session Fixation**: Implement session renewal
- **Weak Encryption**: Use strong algorithms
- **Missing Security Headers**: Add protective headers

### Low Priority Fixes

- **Rate Limiting**: Implement request throttling
- **Security Logging**: Enhance audit trails
- **Content Security**: Strengthen CSP policies
- **Cookie Security**: Secure cookie attributes

## Success Criteria

- All critical and high security vulnerabilities resolved
- No hardcoded secrets or credentials in codebase
- Input validation implemented for all user inputs
- Secure authentication and authorization mechanisms
- Security testing passes without critical findings
- Dependencies updated to secure versions

## Error Handling

### Security Fix Challenges

- **Breaking Changes**: Test thoroughly after security updates
- **Performance Impact**: Profile security controls
- **Compatibility Issues**: Validate with existing systems
- **User Experience**: Balance security with usability

### Escalation Scenarios

- **Zero-day vulnerabilities**: Immediate isolation and patching
- **Infrastructure security**: Coordinate with operations team
- **Compliance requirements**: Involve legal/compliance teams
- **Third-party integrations**: Work with vendor security teams

## Output Requirements

Generate comprehensive security remediation report:

```json
{
  "security_fixes_applied": {
    "vulnerabilities_patched": 0,
    "secrets_removed": 0,
    "authentication_enhanced": true,
    "input_validation_added": 0,
    "dependencies_updated": 0
  },
  "vulnerability_status": {
    "critical_remaining": 0,
    "high_remaining": 0,
    "medium_remaining": 0,
    "low_remaining": 0,
    "total_resolved": 0
  },
  "security_controls_implemented": [
    "input_validation",
    "output_encoding",
    "secure_headers",
    "authentication_checks"
  ],
  "compliance_status": {
    "owasp_top_10": "compliant",
    "security_scan_score": "A+",
    "penetration_test": "passed"
  },
  "recommendations": [
    "Implement regular security training",
    "Schedule quarterly security reviews",
    "Establish bug bounty program"
  ]
}
```

## MCP PROTOCOL COMPLIANCE REQUIREMENTS

**MANDATORY REQUIREMENTS FOR ALL SECURITY REMEDIATION OPERATIONS:**

1. ** ALWAYS use context7 BEFORE security fixes** - Get current, accurate documentation for security patterns
2. ** ALWAYS use grep to search GitHub** - Find real production examples of security fixes
3. ** ALWAYS record actions in neo4j-memory and memory AS YOU WORK** - Document everything
4. ** ALWAYS save to neo4j-memory and memory** - Preserve for future sessions
5. **NEVER skip the Context Load phase** - Always start by loading relevant context
6. **NEVER fix security without Research phase** - context7 + grep are MANDATORY
7. **NEVER complete without Context Save** - Always persist learnings and decisions

**THE GOLDEN RULE: context7 (docs) grep (examples) memory (record) fix memory (persist)**

## MANDATORY REVERSE DATE STAMP REQUIREMENTS

**ALL OUTPUT FILES AND DOCUMENTATION MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

Follow security-first development practices and maintain strong security posture throughout the remediation process.
