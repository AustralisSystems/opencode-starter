---
name: python-typecheck
description: Python type checking with mypy, type hint validation, and type annotation improvements. Use when checking Python types, fixing mypy errors, or adding/improving type hints.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: true
---

# Python Type Check Orchestrator

**Type:** Language Quality | **Python Typing**

## Auto-Activation

I activate when you mention:
- "check Python types"
- "run mypy"
- "type check Python"
- "fix type [hints/errors]"
- "add type annotations"
- "validate Python typing"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"


**Examples:**
> "Type check PYTHON authentication service with auto-approval"
> "Type check PYTHON user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Type checking is safe for auto-approval (validation only)

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

**ALL typechecking work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → typecheck → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR TYPECHECKING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous type annotations
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for typing patterns BEFORE typechecking
   - context7: Latest Python typing standards (mypy, Pydantic)
   - grep: Real-world type annotation examples
3. **PLANNING**: Use `sequential-thinking` to plan type improvements
4. **TYPECHECKING**: Add/fix type annotations
5. **PROGRESS TRACKING**: Record typing decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist typing patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Typechecking without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory


## Execution

**READ**: `.mcp_prompts/languages/python/python-code-lint-and-quality-check-prompt.yaml`

Focus on mypy and type checking sections.

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`

**Tier 1 - Core Checklist (ALWAYS LOAD):**
- Read: `.mcp_prompts/languages/python/python-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during type checking):**
- Read: `.mcp_prompts/languages/python/standards/python-coding.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- (None currently - placeholder for future Python examples)

**Roles**:
- `python-type-checker.role.yaml`
- `python-formatter.role.yaml`

## Commands Executed

```bash
# Type checking
mypy . --strict
mypy . --config-file pyproject.toml

# Type coverage
mypy . --html-report mypy-report
```

## Output

- mypy error report
- Type hint additions
- Type annotation fixes
- Generic type improvements
- Protocol/TypedDict implementations
- Type coverage metrics
- Strict mode compliance

## Related

`python-quality-review`, `quality-validation`, `python-implement`
