---
name: fastapi-implement
description: Implement FastAPI services, routers, endpoints, and middleware using MCP Framework v6.0.0. Use when building FastAPI applications, creating REST APIs, or implementing backend services. Orchestrates steps 1, 12-14, 18 (implement intent).
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1, 2]
  safe_for_auto_approval: false
---

# FastAPI Implementation Orchestrator

**Framework:** MCP v6.0.0 | **Intent:** implement | **Tech:** fastapi

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

## Auto-Activation

I activate when you mention:
- "implement FastAPI [service/router/endpoint]"
- "create FastAPI [API/application]"
- "build FastAPI [backend/microservice]"
- "write FastAPI code"


## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"
- "auto-approve Gate 2"

**Examples:**
> "Implement FASTAPI authentication service with auto-approval"
> "Implement FASTAPI user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate1 & Gate 2
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: Writes code. Recommend auto-approve Gate 1, review Gate 2

## ⚠️ MANDATORY: MCP Tools Workflow

**ALL FastAPI implementations MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load FastAPI project context
2. **MANDATORY RESEARCH**: Use `context7` + `grep` for FastAPI patterns BEFORE coding
3. **PLANNING**: Use `sequential-thinking` to structure API design
4. **IMPLEMENTATION**: Use `filesystem` to write FastAPI code
5. **PROGRESS TRACKING**: Record to `neo4j-memory` during work
6. **CONTEXT SAVE**: Persist API patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Implementing FastAPI without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory

## ⚠️ MANDATORY: Enterprise Template Requirement

**BEFORE ANY CODE GENERATION:**

1. **READ**: `.claude/skills/MANDATORY-SCAFFOLD-TEMPLATE.md`
2. **COPY**: Enterprise template from `C:\github_development\projects\fastapi-enterprise-core-template`
   - Includes: FastAPI + HTMX + Jinja2 + TailwindCSS
   - Built-in: Auth, MCP, Plugin system
3. **CONFIGURE**: Feature flags for this specific app
4. **CUSTOMIZE**: app/routes/ and app/models/ only
5. **KEEP**: src/core/ framework intact

**❌ NEVER generate FastAPI code from scratch**
**✅ ALWAYS copy enterprise template first**

**Template Features:**
- ✅ Factory patterns throughout
- ✅ Database auto-switching (SQLite/PostgreSQL, MongoDB/TinyDB)
- ✅ 54+ plugin provider capabilities
- ✅ Hot-loading and state preservation
- ✅ Multi-auth support (FastAPI Users, OAuth, Auth0)

## Execution

**READ**: `.mcp_prompts/platforms/fastapi/run.fastapi-implement.prompt.yaml`

**Steps**: 1, 12, 13, 14, 18 + Gate 2

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Platform: `.mcp_prompts/platforms/fastapi/standards/*.yaml`
- Language: `.mcp_prompts/languages/python/standards/*.yaml`

**Tier 1 - Core Checklists (ALWAYS LOAD):**
- Read: `.mcp_prompts/domains/backend/rest-core.checklist.yaml`
- Read: `.mcp_prompts/domains/backend/api-design-core.checklist.yaml`
- Read: `.mcp_prompts/domains/security/auth-core.checklist.yaml`

**Tier 2 - Detailed Standards (CONDITIONAL - Load during implementation):**
- Read: `.mcp_prompts/domains/backend/rest-standards.detailed.yaml`
- Read: `.mcp_prompts/domains/backend/api-design.detailed.yaml`
- Read: `.mcp_prompts/domains/security/auth-standards.detailed.yaml`

**Tier 3 - Examples Library (ON-DEMAND - When validation fails or requested):**
- Search: `.mcp_prompts/examples/backend/rest-*.example.yaml`
- Search: `.mcp_prompts/anti-patterns/backend/rest-*.anti-pattern.yaml`

**Roles**:
- `code-implementer.role.yaml`
- `api-test-generator.role.yaml`
- `refactoring-agent.role.yaml`

## Output

- FastAPI routers/endpoints
- Request/Response models (Pydantic)
- Dependency injection
- Middleware implementation
- API tests
- OpenAPI documentation
- Error handling

## Related

`fastapi-design`, `fastapi-quality-review`, `python-implement`
