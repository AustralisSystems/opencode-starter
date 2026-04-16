---
name: fastmcp-quality-review
description: Review FastMCP server quality, MCP protocol compliance, and tool implementation using MCP Framework v6.0.0. Use when validating MCP servers, checking protocol adherence, or auditing tool security. Orchestrates steps 5-8, 17 (quality-review intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: []
  safe_for_auto_approval: true
---

# FastMCP Quality Review Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** quality-review | **Tech:** fastmcp

## Auto-Activation

I activate when you mention:
- "review FastMCP [server/quality]"
- "validate MCP [protocol/compliance]"
- "check FastMCP [security/standards]"
- "audit MCP server"
- "MCP protocol validation"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"


**Examples:**
> "Review FASTMCP authentication service with auto-approval"
> "Review FASTMCP user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** Quality review is safe for auto-approval (read-only validation)

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 (<https://datatracker.ietf.org/doc/html/rfc2119>).

### Requirements Language

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Statement**: All instructions in this skill MUST be interpreted according to RFC 2119. MUST/SHALL/ALWAYS = absolute requirement. NEVER/MUST NOT/SHALL NOT = absolute prohibition. No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL quality review work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → review → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR QUALITY REVIEW)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous quality standards and decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` for quality patterns BEFORE reviewing
   - context7: Latest quality standards and best practices
   - grep: Real-world quality review criteria from top projects
3. **PLANNING**: Use `sequential-thinking` to structure review approach
4. **QUALITY REVIEW**: Perform comprehensive quality analysis
5. **PROGRESS TRACKING**: Record quality findings to `neo4j-memory`
6. **CONTEXT SAVE**: Persist quality patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
- ❌ Reviewing without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory


## Execution

**READ**: `.mcp_prompts/platforms/fastmcp/run.fastmcp-quality-review.prompt.yaml`

**Steps**: 5, 6, 7, 8, 17

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Platform: `.mcp_prompts/platforms/fastmcp/standards/*.yaml`
- Language: `.mcp_prompts/languages/python/standards/*.yaml`
- Domains: integration, security, testing

**Roles**:
- `quality-validator.role.yaml`
- `security-analyst.role.yaml`
- `integration-test-validator.role.yaml`
- `compliance-auditor.role.yaml`

## Output

- MCP protocol compliance
- Tool decorator validation
- Resource handler review
- Security assessment
- Authentication audit
- Error handling review
- Test coverage analysis

## Related

`fastmcp-implement`, `fastmcp-refactor`, `python-quality-review`
