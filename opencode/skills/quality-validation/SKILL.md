---
name: quality-validation
description: Comprehensive code quality validation including linting, standards compliance, metrics, and best practices. Use when validating code quality across any codebase before commits or deployments. Cross-platform and multi-language.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: true
---

# Quality Validation Orchestrator

**Type:** SDLC Quality | **Cross-Platform**

## Auto-Activation

I activate when you mention:
- "validate [code/quality]"
- "quality check/validation"
- "lint and check code"
- "standards compliance check"
- "pre-commit validation"


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

**Safety:** Validation is safe for auto-approval (read-only analysis)

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

**READ**: `.mcp_prompts/sdlc/quality/quality-code-validation-prompt.yaml`

**Also reads**:
- `.mcp_prompts/sdlc/quality/quality-code-lint-and-quality-check-prompt.yaml`

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- SDLC: `.mcp_prompts/sdlc/quality/standards/*.yaml`
- Language-specific: Python, Node, etc. (context-based)

**Roles**:
- `quality-validator.role.yaml`
- `compliance-auditor.role.yaml`
- `python-formatter.role.yaml` (if Python)
- `python-type-checker.role.yaml` (if Python)

## Output

- Linting results (ruff, black, mypy for Python)
- Code quality metrics
- Standards compliance report
- Cyclomatic complexity
- Code duplication analysis
- Security issues (basic)
- Recommendations

## Related

`python-quality-review`, `fastapi-quality-review`, `quality-security`
