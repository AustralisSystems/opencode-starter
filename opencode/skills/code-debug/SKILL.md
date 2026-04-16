---
name: code-debug
description: Debug code issues, trace errors, analyze stack traces, and troubleshoot runtime problems. Use when debugging errors, investigating failures, or troubleshooting application issues.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: false
---

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>.

**Requirements Language Table**

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Note:** MUST/SHALL = absolute requirement, NEVER/FORBIDDEN = absolute prohibition. No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms. All instructions using these words are enforceable protocol, not mere suggestions.

# Code Debug Orchestrator

**Type:** SDLC Code | **Debug & Troubleshoot**

## Auto-Activation

I activate when you mention:
- "debug [code/error/issue]"
- "troubleshoot [problem/failure]"
- "investigate [bug/crash]"
- "analyze [stack trace/error]"
- "fix runtime error"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"


**Examples:**
> "Debug the authentication service with auto-approval"
> "Debug the user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: May modify code. Review proposed solutions

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL debugging work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → debug → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR DEBUGGING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous bug fixes and solutions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for debugging patterns BEFORE debugging
   - context7: Official documentation for error messages and APIs
   - grep: Search GitHub for similar bugs and fixes
3. **PLANNING**: Use `sequential-thinking` to plan debugging strategy
4. **DEBUGGING**: Apply fixes and test solutions
5. **PROGRESS TRACKING**: Record bug fixes to `neo4j-memory`
6. **CONTEXT SAVE**: Persist debugging solutions to `neo4j-memory`

**WHY CRITICAL FOR DEBUGGING:**
- grep shows you how OTHERS solved the same error
- context7 ensures you understand the CORRECT API usage
- neo4j-memory preserves bug fixes for future reference

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Debugging without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving solutions to neo4j-memory


## Execution

**READ**: `.mcp_prompts/sdlc/code/code-debug-prompt.yaml`

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- SDLC: `.mcp_prompts/sdlc/code/standards/*.yaml`

**Roles**:
- `code-analyzer.role.yaml`
- `debug-specialist.role.yaml`

## Output

- Root cause analysis
- Stack trace interpretation
- Error reproduction steps
- Debugging recommendations
- Fix implementation
- Test cases for bug
- Prevention strategies

## Related

`code-remediation`, `test-implementation`, `python-implement`
