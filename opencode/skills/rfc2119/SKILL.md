# RFC 2119 Requirements Language - Compliance Protocol Skill

**Skill ID**: `rfc2119`
**Version**: 1.0.0
**Created**: 2025-11-01
**Updated**: 2025-11-01
**Type**: Compliance Protocol
**Enforcement**: MANDATORY for all protocol documentation and API specifications

---

## Overview

RFC 2119 defines the standard for requirements language used in protocol specifications, API documentation, and compliance frameworks. This skill ensures consistent interpretation and enforcement of requirement levels across all documentation and code.

**Purpose**: Provide clear, unambiguous requirements language that cannot be misinterpreted by AI agents, LLMs, developers, or automated systems.

**Source**: [RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels](https://datatracker.ietf.org/doc/html/rfc2119)

---

## Activation

This skill applies to:

- ✅ Protocol documentation creation and review
- ✅ API specification writing
- ✅ Compliance framework development
- ✅ Requirements definition and validation
- ✅ Architecture decision records (ADRs)
- ✅ Security policy documentation

Can be manually invoked via:

```bash
Skill(command="rfc2119")
```

---

## Requirements Language Table

All requirements language in instructions, protocols, and documentation SHALL be interpreted as defined in RFC 2119.

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

---

## Special Interpretations

### ALWAYS and NEVER

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)

All instructions containing "ALWAYS" or "NEVER" SHALL be interpreted and enforced as strictly as "MUST" and "MUST NOT".

### FORBIDDEN

- **FORBIDDEN** = a hard "MUST NOT" with immediate enforcement
- Any artefact, word, file, or pattern labelled as FORBIDDEN (e.g. file/module/function name "enhanced", or other banned logic or artefacts):
  - MUST be detected, flagged, and immediately removed or refactored from the codebase
  - All references MUST be updated and corrected
  - Remediation MUST be logged as a protocol enforcement action
  - No exceptions and no warnings--immediate correction is REQUIRED

---

## Enforcement Protocol

### Non-Negotiable Rules

1. **No Relaxation**: No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.
2. **Protocol Status**: All instructions using these words are enforceable protocol, not mere suggestions.
3. **Immediate Action**: MUST and MUST NOT violations require immediate remediation.
4. **Zero Tolerance**: FORBIDDEN items require detection and immediate removal without exception.

### Compliance Validation

**When reviewing requirements language:**

1. Verify correct term usage for requirement level
2. Ensure no ambiguous language that could be misinterpreted
3. Validate that enforcement level matches actual requirement importance
4. Check for consistent usage throughout documentation

---

## Compliance Workflow

### Step 1: Analyze Requirement Criticality

Determine the appropriate requirement level:

```yaml
Critical (MUST/MUST NOT):
  - Security requirements
  - Data integrity requirements
  - Legal/regulatory compliance
  - API contract guarantees
  - System stability requirements

Strong Recommendation (SHOULD/SHOULD NOT):
  - Best practices
  - Performance optimization
  - User experience guidelines
  - Code quality standards

Optional (MAY):
  - Enhancement features
  - Alternative implementations
  - Configurable behaviors
  - Optional integrations
```

### Step 2: Select Correct Term

**Decision Tree**:

```
Is this requirement...

├─ Absolutely required with no exceptions?
│  └─ Use: MUST / SHALL / REQUIRED / ALWAYS
│
├─ Absolutely prohibited with no exceptions?
│  └─ Use: MUST NOT / SHALL NOT / NEVER
│
├─ Prohibited and must be detected/removed immediately?
│  └─ Use: FORBIDDEN
│
├─ Strongly recommended but may have valid exceptions?
│  └─ Use: SHOULD / RECOMMENDED
│
├─ Strongly discouraged but may have valid use cases?
│  └─ Use: SHOULD NOT / NOT RECOMMENDED
│
└─ Truly optional without impact on compliance?
   └─ Use: MAY / OPTIONAL
```

### Step 3: Document Enforcement

For MUST/MUST NOT requirements, document:

- Enforcement mechanism
- Validation procedure
- Remediation process
- Consequences of non-compliance

### Step 4: Validate Compliance

Use compliance checking tools to verify:

- All MUST requirements are implemented
- No MUST NOT violations exist
- No FORBIDDEN items are present
- SHOULD recommendations are followed or deviations documented

---

## Practical Examples

### Example 1: API Authentication

**Correct**:

```markdown
## Authentication

- API requests MUST include a valid authentication token in the Authorization header
- Authentication tokens MUST NOT be transmitted in URL query parameters
- Expired tokens MUST be rejected with HTTP 401 status
- Token refresh SHOULD occur automatically before expiration
- Clients MAY cache tokens for the duration of their validity period
```

**Incorrect**:

```markdown
## Authentication

- API requests should probably have authentication
- Don't put tokens in URLs
- Try to reject expired tokens
- It would be nice if token refresh was automatic
```

### Example 2: Code Quality Standards

**Correct**:

```markdown
## Code Quality

- All code MUST pass type checking with zero errors
- Code MUST NOT contain security vulnerabilities
- Functions SHOULD have comprehensive docstrings
- Code SHOULD follow PEP 8 style guidelines
- Developers MAY use alternative formatters if team-approved
```

**Incorrect**:

```markdown
## Code Quality

- Try to make code pass type checking
- Avoid security vulnerabilities when possible
- Docstrings are recommended
- Follow PEP 8 if you can
```

### Example 3: FORBIDDEN Pattern

**Correct**:

```markdown
## Naming Conventions

- Module names MUST use snake_case
- Class names MUST use PascalCase
- The term "enhanced" is FORBIDDEN in all file names and module names
- Any existing usage MUST be immediately refactored
```

**Implementation**:

```python
# FORBIDDEN - Immediate removal required
# enhanced_processor.py

# CORRECT - Refactored name
# advanced_processor.py
# optimized_processor.py
# improved_processor.py
```

### Example 4: Configuration Requirements

**Correct**:

```markdown
## Configuration

- Production environments MUST use TLS 1.3 or higher
- Development environments SHOULD use TLS for consistency
- Local testing environments MAY use HTTP for debugging
- SSLv3 and TLS 1.0 are FORBIDDEN and MUST NOT be enabled
```

---

## Validation Checklist

Before publishing requirements documentation, verify:

- [ ] All critical requirements use MUST or MUST NOT
- [ ] No ambiguous terms like "should probably" or "try to"
- [ ] SHOULD statements have documented deviation processes
- [ ] FORBIDDEN items have detection and remediation procedures
- [ ] MAY statements are truly optional without compliance impact
- [ ] Consistent terminology throughout document
- [ ] Enforcement mechanisms defined for all MUST requirements
- [ ] No weakening language like "generally" or "usually"

---

## Anti-Patterns (Incorrect Usage)

### ❌ Ambiguous Language

**Wrong**:

```markdown
- Authentication is important and should be implemented
- Try to validate all inputs
- It's recommended to use HTTPS
```

**Right**:

```markdown
- Authentication MUST be implemented for all API endpoints
- All user inputs MUST be validated before processing
- Production deployments MUST use HTTPS
```

### ❌ Weak Enforcement

**Wrong**:

```markdown
- Code must generally pass all tests
- Security scanning is usually required
- Production code should normally be reviewed
```

**Right**:

```markdown
- Code MUST pass all tests before merging
- Security scanning MUST be performed on all releases
- Production code MUST undergo peer review
```

### ❌ Incorrect Term Selection

**Wrong**:

```markdown
- Critical security patches SHOULD be applied immediately
- SQL injection vulnerabilities MAY be fixed
- Production databases SHOULD NOT be exposed to internet
```

**Right**:

```markdown
- Critical security patches MUST be applied within 24 hours
- SQL injection vulnerabilities MUST be fixed immediately
- Production databases MUST NOT be directly exposed to internet
```

### ❌ Missing FORBIDDEN Enforcement

**Wrong**:

```markdown
- The term "legacy" should not be used in new code
```

**Right**:

```markdown
- The term "legacy" is FORBIDDEN in all new module names
- Any usage MUST be detected and immediately refactored
- Automated scanning MUST flag all violations
```

---

## Integration with Development Workflows

### Protocol Documentation

When writing protocol documentation:

1. Use sequential-thinking to analyze requirement levels
2. Select appropriate RFC 2119 terms
3. Document enforcement mechanisms
4. Validate with compliance checklist

### Code Review

When reviewing code or documentation:

1. Verify RFC 2119 compliance
2. Check for weak or ambiguous language
3. Ensure MUST requirements are enforced
4. Validate no FORBIDDEN items exist

### Automated Validation

Implement automated checks for:

```yaml
rfc2119_validation:
  checks:
    - ambiguous_terms:
        forbidden: ["should probably", "try to", "generally", "usually"]
        action: reject_pr

    - weak_language:
        pattern: "MUST.*generally|normally|typically"
        action: flag_for_review

    - forbidden_items:
        scan: codebase
        action: immediate_remediation
        log: protocol_enforcement

    - requirement_consistency:
        verify: all_must_have_enforcement
        action: require_documentation
```

---

## Quality Thresholds

### Documentation Phase (95% Confidence)

- ✅ All critical requirements use MUST/MUST NOT
- ✅ No ambiguous or weak language
- ✅ Enforcement mechanisms documented
- ✅ FORBIDDEN items identified with remediation process

### Review Phase (98% Confidence)

- ✅ RFC 2119 compliance verified
- ✅ Consistent terminology throughout
- ✅ All deviations from SHOULD justified and documented
- ✅ Automated validation rules in place

### Enforcement Phase (100% Compliance)

- ✅ All MUST requirements implemented
- ✅ Zero MUST NOT violations
- ✅ All FORBIDDEN items removed
- ✅ Continuous monitoring active

---

## Success Metrics

### Clarity

- Requirements are unambiguous and precise
- No room for misinterpretation
- Clear enforcement mechanisms defined

### Consistency

- RFC 2119 terms used correctly throughout
- No mixing of informal and formal language
- Uniform interpretation across all documents

### Enforceability

- All MUST requirements are testable
- Automated validation possible
- Clear remediation procedures

### Compliance

- 100% adherence to RFC 2119 definitions
- Zero tolerance for ambiguous language
- Immediate correction of violations

---

## Remember

**RFC 2119 exists to**:

- ✅ Eliminate ambiguity in requirements
- ✅ Ensure consistent interpretation across systems
- ✅ Enable automated compliance validation
- ✅ Provide clear enforcement boundaries
- ✅ Support legal and regulatory compliance

**Always use RFC 2119 for**:

- Protocol specifications
- API documentation
- Security policies
- Compliance frameworks
- Architecture decisions
- Quality standards

**Never compromise on**:

- Precise terminology
- Clear enforcement
- Unambiguous requirements
- Immediate FORBIDDEN remediation

---

## Version History

| Version | Date       | Changes                                                   |
| ------- | ---------- | --------------------------------------------------------- |
| 1.0.0   | 2025-11-01 | Initial RFC 2119 skill definition with full requirements table |

---

**Skill Created By**: Claude Code (Sonnet 4.5)
**Based On**: RFC 2119, Core Compliance Prompt, Requirements Language Protocol
**Enforcement**: MANDATORY for protocol and compliance documentation
**Purpose**: Ensure unambiguous, enforceable requirements language across all documentation
