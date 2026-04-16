---
name: fastmcp-implement
description: Implement FastMCP servers with tool decorators, resources, prompts, and authentication using MCP Framework v6.0.0. Use when building MCP servers, creating tools, or implementing Model Context Protocol integrations. Orchestrates steps 1, 12-14, 18 (implement intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1, 2]
  safe_for_auto_approval: false
---

# FastMCP Implementation Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** implement | **Tech:** fastmcp

## Auto-Activation

I activate when you mention:
- "implement FastMCP [server/tool/resource]"
- "create MCP [integration/server]"
- "build FastMCP [application/service]"
- "write MCP tool decorator"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"
- "auto-approve Gate 2"

**Examples:**
> "Implement FASTMCP authentication service with auto-approval"
> "Implement FASTMCP user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate1 & Gate 2
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: Writes MCP server code. Recommend auto-approve Gate 1, review Gate 2

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

## ⚠️ MANDATORY: MCP Tools Workflow

**ALL FastMCP implementations MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load FastMCP project context
2. **MANDATORY RESEARCH**: Use `context7` + `grep` for FastMCP/MCP patterns BEFORE coding
3. **PLANNING**: Use `sequential-thinking` to design MCP tools/resources
4. **IMPLEMENTATION**: Use `filesystem` to write FastMCP code
5. **PROGRESS TRACKING**: Record to `neo4j-memory` during work
6. **CONTEXT SAVE**: Persist MCP patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Implementing FastMCP without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory

## ⚠️ MANDATORY: Enterprise Template Requirement

**BEFORE ANY CODE GENERATION:**

1. **READ**: `.claude/skills/MANDATORY-SCAFFOLD-TEMPLATE.md`
2. **COPY**: Enterprise template from `C:\github_development\projects\fastapi-enterprise-core-template`
   - Includes: FastMCP integration ready
   - Built-in: @mcp.tool(), @mcp.resource(), @mcp.prompt()
3. **ENABLE**: FEATURE_FLAG_MCP_ENABLED=true in `.env`
4. **ADD**: Your MCP tools in plugins/
5. **KEEP**: Core MCP framework intact

**❌ NEVER generate FastMCP code from scratch**
**✅ ALWAYS copy enterprise template first**

**FastMCP Template Location:**
- `fastmcp/` directory in template
- `services/mcp/` for MCP services
- `plugins/mcp/` for MCP plugins

**Template Features:**
- ✅ Factory patterns for MCP providers
- ✅ Plugin-based MCP tools architecture
- ✅ Hot-loading MCP tools support
- ✅ MCP protocol integration with FastAPI

## Execution

**READ**: `.mcp_prompts/platforms/fastmcp/run.fastmcp-implement.prompt.yaml`

**Steps**: 1, 12, 13, 14, 18 + Gate 2

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Platform: `.mcp_prompts/platforms/fastmcp/standards/*.yaml`
- Language: `.mcp_prompts/languages/python/standards/*.yaml`
- Domains: backend, integration, security

**Roles**:
- `code-implementer.role.yaml`
- `integration-test-generator.role.yaml`
- `refactoring-agent.role.yaml`

## Output

- FastMCP server (main.py)
- @mcp.tool() decorators
- @mcp.resource() handlers
- @mcp.prompt() templates
- Authentication config
- SSE transport setup
- MCP protocol tests
- Error handling

## Related

`fastmcp-design`, `fastmcp-quality-review`, `python-implement`
