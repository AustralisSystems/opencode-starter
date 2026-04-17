# Security Protocol - Mandatory Security Instructions

### MANDATORY READING REQUIREMENT
**BEFORE ANY SECURITY ANALYSIS OR IMPLEMENTATION, YOU MUST:**
- **MUST READ AND INDEX:** `code-protocol-security-strategy.md` - Security philosophy, methods, and procedures

---

## SECURITY REQUIREMENTS - RFC 2119 COMPLIANCE

### INPUT VALIDATION - MANDATORY
- **MUST** validate all input parameters
- **MUST** sanitize user-provided data
- **MUST** implement proper type checking
- **MUST** use parameterized queries for database operations

### AUTHENTICATION & AUTHORIZATION - MANDATORY
- **MUST** implement proper authentication checks
- **MUST** follow least privilege principle
- **MUST** use secure session management
- **MUST** implement rate limiting where appropriate

### DATA PROTECTION - MANDATORY
- **MUST NOT** log sensitive information
- **MUST** use environment variables for secrets
- **MUST** implement proper encryption for sensitive data
- **MUST** follow OWASP security guidelines

### CODE SECURITY - MANDATORY
- **MUST** prevent injection attacks (SQL, XSS, Command)
- **MUST** implement CSRF protection
- **MUST** use secure headers
- **MUST** validate file uploads and paths

### ERROR HANDLING - MANDATORY
- **MUST NOT** expose system details in errors
- **MUST** log security events appropriately
- **MUST** implement proper exception handling
- **MUST** use secure defaults

---

## FORBIDDEN SECURITY PRACTICES

**NEVER:**
- Log secrets, keys, or sensitive data
- Use hardcoded credentials
- Trust user input without validation
- Expose internal system information in error messages
- Use deprecated or insecure cryptographic functions
- Bypass authentication or authorization checks

**ALWAYS:**
- Validate and sanitize all inputs
- Use secure communication protocols
- Implement proper access controls
- Follow security best practices
- Keep dependencies updated
- Use secure coding standards

---

**ENFORCEMENT:** All security requirements are MANDATORY and non-negotiable. Security violations will result in immediate remediation requirements.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>