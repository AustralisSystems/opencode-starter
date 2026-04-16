---
name: quality-security
description: Security analysis including vulnerability scanning, dependency audits, authentication review, and threat assessment. Use when checking security, auditing dependencies, or validating auth implementations.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: true
---

# Security Quality Orchestrator

**Type:** SDLC Quality | **Security Focus**

## Auto-Activation

I activate when you mention:
- "security [analysis/audit/check]"
- "vulnerability [scan/assessment]"
- "dependency audit"
- "security validation"
- "threat assessment"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"


**Examples:**
> "Review the authentication service with auto-approval"
> "Review the user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Security analysis is safe for auto-approval (read-only scanning)

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>.

### Requirements Language

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

### Enforcement

**MUST/SHALL = absolute requirement, NEVER/FORBIDDEN = absolute prohibition**

- ALWAYS = MUST (absolute, non-negotiable requirement)
- NEVER = MUST NOT (absolute, non-negotiable prohibition)
- No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms
- All instructions using these words are enforceable protocol, not mere suggestions

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL validation work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → validate → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR VALIDATION)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous validation standards
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for validation patterns BEFORE validating
   - context7: Latest validation standards and tools
   - grep: Real-world validation implementations
3. **PLANNING**: Use `sequential-thinking` to structure validation
4. **VALIDATION**: Perform comprehensive validation
5. **PROGRESS TRACKING**: Record validation results to `neo4j-memory`
6. **CONTEXT SAVE**: Persist validation patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Validating without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory


## Execution

**READ**: `.mcp_prompts/sdlc/quality/quality-code-security-analysis-prompt.yaml`

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Domains: `.mcp_prompts/domains/security/*.yaml`
- Language: Python security standards

**Roles**:
- `security-analyst.role.yaml`
- `python-security-scanner.role.yaml`
- `compliance-auditor.role.yaml`

## Output

- Vulnerability scan results
- Dependency security audit (safety, pip-audit)
- Authentication/authorization review
- Secrets detection
- SQL injection risks
- XSS vulnerabilities
- Security best practices compliance
- Remediation recommendations

## Related

`quality-validation`, `python-quality-review`, `code-remediation`
