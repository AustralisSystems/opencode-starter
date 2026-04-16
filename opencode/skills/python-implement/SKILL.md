---
name: python-implement
description: Implement Python code with optimization, testing, and error handling using MCP Framework v6.0.0. Use when writing Python code, creating modules, or implementing features. Orchestrates steps 1, 12-14, 18 (implement intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1, 2]
  safe_for_auto_approval: false
---

# Python Implementation Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** implement | **Tech:** python

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 as defined in <https://datatracker.ietf.org/doc/html/rfc2119>.

**Requirements Language Table:**

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Statement:** All instructions using MUST/SHALL/ALWAYS are enforceable protocol requirements, not mere suggestions. MUST/SHALL = absolute requirement, NEVER/FORBIDDEN = absolute prohibition.

**Special Note:** ALWAYS and NEVER are equivalent to MUST and MUST NOT respectively - see RFC 2119 for complete protocol interpretation.

## Auto-Activation

I activate when you mention:
- "implement Python [feature/module/function]"
- "write Python [code/class/service]"
- "create Python [application/library]"
- "Python development/coding"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"
- "auto-approve Gate 2"

**Examples:**
> "Implement PYTHON authentication service with auto-approval"
> "Implement PYTHON user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate1 & Gate 2
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: Writes code. Recommend auto-approve Gate 1, review Gate 2

## ⚠️ MANDATORY: MCP Tools Workflow

**ALL Python implementations MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load project context
2. **MANDATORY RESEARCH**: Use `context7` + `grep` BEFORE coding
3. **PLANNING**: Use `sequential-thinking` to structure approach
4. **IMPLEMENTATION**: Use `filesystem` to write code applying SOLID/DRY/KISS
5. **PROGRESS TRACKING**: Record to `neo4j-memory` during work
6. **CONTEXT SAVE**: Persist learnings to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Implementing without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory

## ⚠️ MANDATORY: Enterprise Template Requirement

**BEFORE ANY CODE GENERATION:**

1. **READ**: `.claude/skills/MANDATORY-SCAFFOLD-TEMPLATE.md`
2. **COPY**: Enterprise template from `C:\github_development\projects\fastapi-enterprise-core-template`
3. **CONFIGURE**: Feature flags in `.env`
4. **THEN**: Augment/customize for specific use case

**❌ NEVER generate Python code from scratch**
**✅ ALWAYS copy enterprise template first**

**Template Features:**
- ✅ Factory patterns throughout
- ✅ Database auto-switching (SQLite/PostgreSQL, MongoDB/TinyDB)
- ✅ 54+ plugin provider capabilities
- ✅ Hot-loading and state preservation

## Execution

**READ**: `.mcp_prompts/languages/python/run.python-implement.prompt.yaml`

**Steps**: 1, 12, 13, 14, 18 + Gate 2

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`

**Tier 1 - Core Checklist (ALWAYS LOAD):**
- Read: `.mcp_prompts/languages/python/python-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during implementation):**
- Read: `.mcp_prompts/languages/python/standards/python-coding.detailed.yaml`
- Read: `.mcp_prompts/languages/python/standards/python-security.detailed.yaml`
- Read: `.mcp_prompts/languages/python/standards/python-optimization-best-practices.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- (None currently - placeholder for future Python examples)

**Domains**: backend, security, testing (context-based)

**Roles**:
- `code-implementer.role.yaml`
- `unit-test-generator.role.yaml`
- `refactoring-agent.role.yaml`
- `python-formatter.role.yaml`

## Output

- Optimized Python code
- Comprehensive test suite
- Refactored structure
- Error handling
- Documentation
- State: `project/state/stepwise-execution.json`

## Related

`python-design`, `python-quality-review`, `python-refactor`, `python-typecheck`
