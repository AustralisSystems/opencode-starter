---
name: fastmcp-planning
description: Plan FastMCP server implementation, tool development, and MCP protocol integration using MCP Framework v6.0.0. Use when scoping MCP projects, breaking down tool development, or planning integration work. Orchestrates steps 1, 9-11 (planning intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1]
  safe_for_auto_approval: true
---

# FastMCP Planning Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** planning | **Tech:** fastmcp

## Auto-Activation

I activate when you mention:
- "plan FastMCP [implementation/development]"
- "scope MCP [server/tools/resources]"
- "estimate FastMCP [effort/timeline]"
- "MCP project roadmap"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"

**Examples:**
> "Plan FASTMCP authentication service with auto-approval"
> "Plan FASTMCP user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate 1
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Planning phase is safe for auto-approval (read-only task breakdown)

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 (https://datatracker.ietf.org/doc/html/rfc2119).

| Term | Meaning / Required Interpretation |
| ---- | ---- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions. |
| MUST NOT / SHALL NOT / NEVER | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions. |
| FORBIDDEN | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified. |
| SHOULD NOT / NOT RECOMMENDED | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented. |
| MAY / OPTIONAL | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance. |

### Special Notes

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)
- **FORBIDDEN** = a hard "MUST NOT" - MUST be detected, flagged, and immediately removed or refactored from the codebase with all references updated

**Enforcement:** All instructions using these words are enforceable protocol, not mere suggestions. No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.

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

**READ**: `.mcp_prompts/platforms/fastmcp/run.fastmcp-planning.prompt.yaml`

**Steps**: 1, 9, 10, 11 + Gate 1

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Platform: `.mcp_prompts/platforms/fastmcp/standards/*.yaml`
- Language: `.mcp_prompts/languages/python/standards/*.yaml`

**Roles**:
- `planning-analyst.role.yaml`
- `risk-assessor.role.yaml`

## Output

- MCP tool breakdown
- Resource implementation plan
- Integration timeline
- Testing strategy
- Risk assessment

## Related

`fastmcp-design`, `fastmcp-implement`, `python-planning`
