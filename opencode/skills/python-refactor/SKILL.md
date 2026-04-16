---
name: python-refactor
description: Refactor Python code for optimization, maintainability, and performance using MCP Framework v6.0.0. Use when improving existing Python code, optimizing performance, or reducing technical debt. Orchestrates steps 5, 14-16 (refactor intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: false
---

# Python Refactor Orchestrator

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 (https://datatracker.ietf.org/doc/html/rfc2119). The requirements language table below defines the mandatory interpretation of compliance terms used throughout this skill.

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Statement:** No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms. All instructions using these words are enforceable protocol, not mere suggestions.

**Special Note:** MUST/SHALL/ALWAYS = absolute requirement; NEVER/MUST NOT/SHALL NOT = absolute prohibition; FORBIDDEN = hard MUST NOT requiring immediate correction with no exceptions.

**Framework:** MCP v6.0.0 | **Intent:** refactor | **Tech:** python

## Auto-Activation

I activate when you mention:
- "refactor Python [code/module/function]"
- "optimize Python [performance/memory]"
- "improve Python [code/structure]"
- "clean up Python code"
- "Python technical debt"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"


**Examples:**
> "Refactor PYTHON authentication service with auto-approval"
> "Refactor PYTHON user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: Modifies code. Review changes before accepting

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL refactoring work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → refactor → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR REFACTORING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous refactoring decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for refactoring patterns BEFORE refactoring
   - context7: Latest refactoring techniques and best practices
   - grep: Real-world refactoring examples from high-quality repos
3. **PLANNING**: Use `sequential-thinking` to plan refactoring strategy
4. **REFACTORING**: Apply refactoring transformations
5. **PROGRESS TRACKING**: Record refactoring decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist refactoring patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Refactoring without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory


## Execution

**READ**: `.mcp_prompts/languages/python/run.python-refactor.prompt.yaml`

**Steps**: 5, 14, 15, 16

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`

**Tier 1 - Core Checklist (ALWAYS LOAD):**
- Read: `.mcp_prompts/languages/python/python-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during refactoring):**
- Read: `.mcp_prompts/languages/python/standards/python-coding.detailed.yaml`
- Read: `.mcp_prompts/languages/python/standards/python-optimization-best-practices.detailed.yaml`
- Read: `.mcp_prompts/languages/python/standards/python-optimization-implementation.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- (None currently - placeholder for future Python examples)

**Domains**: performance, backend

**Roles**:
- `refactoring-agent.role.yaml`
- `optimizer.role.yaml`
- `python-formatter.role.yaml`
- `duplication-detector.role.yaml`

## Output

- Refactored code
- Optimization report
- Dependency updates
- Performance improvements
- Code quality metrics
- State: `project/state/stepwise-execution.json`

## Related

`python-implement`, `python-quality-review`, `python-design`
