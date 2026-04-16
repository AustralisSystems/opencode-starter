---
name: fastapi-design
description: Design FastAPI architecture and API structure using MCP Framework v6.0.0. Use when planning FastAPI services, designing endpoints, or structuring applications before implementation. Orchestrates framework steps 1, 3, 9-11 (design intent) with approval gate.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1]
  safe_for_auto_approval: true
---

# FastAPI Design Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** design | **Tech:** fastapi

## RFC 2119 COMPLIANCE

**All instructions in this skill MUST be interpreted according to RFC 2119** <https://datatracker.ietf.org/doc/html/rfc2119>

**MUST/SHALL/REQUIRED/ALWAYS** = absolute requirement, NEVER/SHALL NOT/MUST NOT/FORBIDDEN = absolute prohibition

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

## Auto-Activation Triggers

I activate when you mention:
- "design FastAPI [service/API/endpoint/architecture]"
- "plan FastAPI [application/structure]"
- "FastAPI architecture/design/structure"

## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"

**Examples:**
> "Design a FastAPI authentication service with auto-approval"
> "Design FastAPI user management API, auto-approve all gates"

**What happens:**
- I execute all steps without pausing at Gate 1
- I make design decisions autonomously
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Design phase is safe for auto-approval (read-only analysis/planning)

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL FastAPI design work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → design → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR DESIGN)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous API architectural decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for FastAPI patterns BEFORE designing
   - context7: Latest FastAPI architecture patterns, endpoint design, middleware patterns
   - grep: Real-world FastAPI applications from GitHub (high-star repos)
3. **PLANNING**: Use `sequential-thinking` to structure API design approach
4. **DESIGN**: Create FastAPI architecture/endpoint design
5. **PROGRESS TRACKING**: Record API design decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist FastAPI patterns and decisions to `neo4j-memory`

**WHY THIS IS CRITICAL FOR FASTAPI DESIGN:**
- context7 ensures you use CURRENT FastAPI best practices (not deprecated patterns)
- grep shows you REAL production FastAPI architectures
- neo4j-memory preserves API design decisions across sessions

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Designing FastAPI without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing design without saving API decisions to neo4j-memory

## Execution Process

### 1. Load Intent Orchestrator
**READ**: `.mcp_prompts/platforms/fastapi/run.fastapi-design.prompt.yaml`

This orchestrator:
- References master framework
- Enables steps: 1, 3, 9, 10, 11 + Gate 1
- Loads standards hierarchy
- Specifies required roles

### 2. Framework Execution Flow

```
Step 1  → Project initialization
Step 3  → Project structure setup
Step 9  → Optimization scope definition
Step 10 → Task planning
Step 11 → Risk assessment
Gate 1  → ⏸️ APPROVAL (wait for your input: APPROVE/MODIFY/REJECT/INFO)
```

### 3. Standards Loading (Hierarchical)

**Core (MANDATORY):**
- Read: `.mcp_prompts/framework/standards/ai-agent/*.yaml` (4 files)

**Platform:**
- Read: `.mcp_prompts/platforms/fastapi/standards/*.yaml`

**Language:**
- Read: `.mcp_prompts/languages/python/standards/*.yaml`

**Tier 1 - Core Checklists (ALWAYS LOAD):**
- Read: `.mcp_prompts/domains/backend/rest-core.checklist.yaml`
- Read: `.mcp_prompts/domains/backend/api-design-core.checklist.yaml`
- Read: `.mcp_prompts/domains/security/auth-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during design phase):**
- Read: `.mcp_prompts/domains/backend/rest-standards.detailed.yaml`
- Read: `.mcp_prompts/domains/backend/api-design.detailed.yaml`
- Read: `.mcp_prompts/domains/security/auth-standards.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- Search: `.mcp_prompts/examples/backend/rest-*.example.yaml`
- Search: `.mcp_prompts/anti-patterns/backend/rest-*.anti-pattern.yaml`

### 4. Roles to Assume

Load from `.mcp_prompts/roles/`:
- `planning-analyst.role.yaml`
- `risk-assessor.role.yaml`
- `architecture-compliance-reviewer.role.yaml`

## Output Deliverables

At Approval Gate 1:
- Architecture design document
- API endpoint specifications
- Module structure plan
- Risk assessment
- Implementation task breakdown
- State: `project/state/stepwise-execution.json`

## Resume Capability

State saved after each step. Resume with:
> "Continue the FastAPI design from where we left off"

## Approval Gate 1 Responses

- **APPROVE** → Continue to implementation (use `fastapi-implement` skill)
- **MODIFY** → Request design changes
- **REJECT** → Return to planning
- **INFO** → Request more information

## Related Skills

- `fastapi-implement` - Implement designed architecture
- `fastapi-quality-review` - Code quality review
- `fastapi-refactor` - Refactor existing code
- `python-design` - Generic Python design

---

**Note:** This skill uses progressive disclosure - framework files are only read when executing steps, minimizing context usage.
