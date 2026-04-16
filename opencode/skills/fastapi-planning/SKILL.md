---
name: fastapi-planning
description: Plan FastAPI implementation tasks, API design, and service architecture using MCP Framework v6.0.0. Use when planning FastAPI services, estimating API development, or scoping REST endpoints. Orchestrates steps 1, 9-11 (planning intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1]
  safe_for_auto_approval: true
---

# FastAPI Planning Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** planning | **Tech:** fastapi

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>.

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

### Enforcement Notes

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)
- **MUST/SHALL** = Absolute requirement; NEVER/FORBIDDEN = Absolute prohibition
- All instructions using these terms are enforceable protocol, not mere suggestions.

## Auto-Activation

I activate when you mention:
- "plan FastAPI [implementation/service/API]"
- "scope FastAPI [endpoints/routes]"
- "estimate FastAPI [development/effort]"
- "FastAPI roadmap/breakdown"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"

**Examples:**
> "Plan FASTAPI authentication service with auto-approval"
> "Plan FASTAPI user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate 1
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Planning phase is safe for auto-approval (read-only task breakdown)

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL planning work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → plan → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR PLANNING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous planning decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for planning patterns BEFORE creating plan
3. **PLANNING**: Use `sequential-thinking` to structure approach
4. **PLAN CREATION**: Create roadmap and task breakdown
5. **PROGRESS TRACKING**: Record decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist planning patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Planning without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory


## Execution

**READ**: `.mcp_prompts/platforms/fastapi/run.fastapi-planning.prompt.yaml`

**Steps**: 1, 9, 10, 11 + Gate 1

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Platform: `.mcp_prompts/platforms/fastapi/standards/*.yaml`
- Language: `.mcp_prompts/languages/python/standards/*.yaml`

**Tier 1 - Core Checklists (ALWAYS LOAD):**
- Read: `.mcp_prompts/domains/backend/rest-core.checklist.yaml`
- Read: `.mcp_prompts/domains/backend/api-design-core.checklist.yaml`
- Read: `.mcp_prompts/domains/security/auth-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during planning):**
- Read: `.mcp_prompts/domains/backend/rest-standards.detailed.yaml`
- Read: `.mcp_prompts/domains/backend/api-design.detailed.yaml`
- Read: `.mcp_prompts/domains/security/auth-standards.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- Search: `.mcp_prompts/examples/backend/rest-*.example.yaml`
- Search: `.mcp_prompts/anti-patterns/backend/rest-*.anti-pattern.yaml`

**Roles**:
- `planning-analyst.role.yaml`
- `risk-assessor.role.yaml`

## Output

- API endpoint breakdown
- Service scope
- Implementation timeline
- Resource requirements
- Risk assessment

## Related

`fastapi-design`, `fastapi-implement`, `python-planning`
