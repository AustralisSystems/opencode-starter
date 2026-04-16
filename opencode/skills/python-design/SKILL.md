---
name: python-design
description: Design Python application architecture, module structure, and API contracts using MCP Framework v6.0.0. Use when planning Python applications, designing modules, or structuring codebases before implementation. Orchestrates steps 1, 3, 9-11 (design intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1]
  safe_for_auto_approval: true
---

# Python Design Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** design | **Tech:** python

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
- "design Python [application/module/API/architecture]"
- "plan Python [structure/organization]"
- "Python architecture/design before implementation"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"

**Examples:**
> "Design a PYTHON authentication service with auto-approval"
> "Design a PYTHON user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate 1
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Design phase is safe for auto-approval (read-only analysis/planning)

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL design work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → design → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR DESIGN)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous architectural decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for design patterns BEFORE designing
   - context7: Latest Python/framework architecture patterns
   - grep: Real-world architecture examples from GitHub
3. **PLANNING**: Use `sequential-thinking` to structure design approach
4. **DESIGN**: Create architecture/module design
5. **PROGRESS TRACKING**: Record design decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist design patterns and decisions to `neo4j-memory`

**WHY THIS IS CRITICAL FOR DESIGN:**
- context7 ensures you use CURRENT best practices, not outdated patterns
- grep shows you REAL production architectures, not theoretical ones
- neo4j-memory preserves design decisions for future reference

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Designing without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing design without saving decisions to neo4j-memory

## Execution

**READ**: `.mcp_prompts/languages/python/run.python-design.prompt.yaml`

**Steps**: 1, 3, 9, 10, 11 + Gate 1

**Standards (Hierarchical)**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`

**Tier 1 - Core Checklist (ALWAYS LOAD):**
- Read: `.mcp_prompts/languages/python/python-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during design):**
- Read: `.mcp_prompts/languages/python/standards/python-coding.detailed.yaml`
- Read: `.mcp_prompts/languages/python/standards/python-security.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- (None currently - placeholder for future Python examples)

**Domains**: backend, security (context-based)

**Roles**:
- `planning-analyst.role.yaml`
- `risk-assessor.role.yaml`
- `architecture-compliance-reviewer.role.yaml`

## Output

- Architecture design
- Module structure plan
- API contracts
- Risk assessment
- Implementation plan
- State: `project/state/stepwise-execution.json`

## Related

`python-planning`, `python-implement`, `python-quality-review`, `python-refactor`
