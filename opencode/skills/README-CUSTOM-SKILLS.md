# Custom MCP Framework Skills

**Created:** 2025-10-22
**Framework:** MCP v6.0.0
**Total Skills:** 21 (+ 12 Anthropic example skills)

## Overview

This skill set provides comprehensive development lifecycle support for Python/FastAPI/FastMCP stack with HTMX/Jinja2 templating. Each skill is a lightweight pointer to the MCP Framework v6.0.0 orchestrators in `.mcp_prompts/`.

### Architecture

```
User Request → Skill (Auto-Discovery) → Intent Orchestrator → Master Framework → Stepwise Prompts → Output
```

## Skills by Category

### 🐍 Python (Language Level) - 5 Skills

| Skill | Intent | Steps | Use When |
|-------|--------|-------|----------|
| **python-design** | design | 1, 3, 9-11 + Gate1 | Planning Python architecture, module structure |
| **python-planning** | planning | 1, 9-11 + Gate1 | Breaking down Python tasks, estimating effort |
| **python-implement** | implement | 1, 12-14, 18 + Gate2 | Writing Python code, creating modules |
| **python-quality-review** | quality-review | 5-8, 17 | Validating Python code quality, security |
| **python-refactor** | refactor | 5, 14-16 | Optimizing Python code, reducing tech debt |

**Orchestrators**: `.mcp_prompts/languages/python/run.python-*.prompt.yaml`

---

### ⚡ FastAPI (Platform Level) - 5 Skills

| Skill | Intent | Steps | Use When |
|-------|--------|-------|----------|
| **fastapi-design** | design | 1, 3, 9-11 + Gate1 | Designing FastAPI services, API architecture |
| **fastapi-planning** | planning | 1, 9-11 + Gate1 | Planning FastAPI endpoints, scoping APIs |
| **fastapi-implement** | implement | 1, 12-14, 18 + Gate2 | Building FastAPI routers, endpoints, services |
| **fastapi-quality-review** | quality-review | 5-8, 17 | Reviewing FastAPI quality, API standards |
| **fastapi-refactor** | refactor | 5, 14-16 | Optimizing FastAPI performance, structure |

**Orchestrators**: `.mcp_prompts/platforms/fastapi/run.fastapi-*.prompt.yaml`

**Includes Support For:**
- REST API design
- Pydantic models
- Dependency injection
- Middleware
- OpenAPI documentation
- HTMX/Jinja2 templates

---

### 🔌 FastMCP (Platform Level) - 5 Skills

| Skill | Intent | Steps | Use When |
|-------|--------|-------|----------|
| **fastmcp-design** | design | 1, 3, 9-11 + Gate1 | Designing MCP servers, tool architecture |
| **fastmcp-planning** | planning | 1, 9-11 + Gate1 | Planning MCP tool development |
| **fastmcp-implement** | implement | 1, 12-14, 18 + Gate2 | Building MCP servers with tools/resources |
| **fastmcp-quality-review** | quality-review | 5-8, 17 | Validating MCP protocol compliance |
| **fastmcp-refactor** | refactor | 5, 14-16 | Optimizing MCP server structure |

**Orchestrators**: `.mcp_prompts/platforms/fastmcp/run.fastmcp-*.prompt.yaml`

**MCP Features:**
- @mcp.tool() decorators
- @mcp.resource() handlers
- @mcp.prompt() templates
- SSE transport
- Authentication
- Protocol compliance

---

### ✅ Quality/Testing/Validation (Cross-Cutting) - 6 Skills

| Skill | Type | Use When |
|-------|------|----------|
| **quality-validation** | SDLC Quality | Linting, standards compliance, pre-commit checks |
| **quality-security** | SDLC Quality | Security analysis, vulnerability scanning, dependency audits |
| **test-implementation** | SDLC Testing | Creating unit/integration/E2E tests, test coverage |
| **code-remediation** | SDLC Code | Fixing quality issues, security vulnerabilities |
| **code-debug** | SDLC Code | Debugging errors, troubleshooting runtime issues |
| **python-typecheck** | Language Quality | mypy type checking, type hint validation |

**Orchestrators**: `.mcp_prompts/sdlc/{quality,test,code}/*.yaml`

---

## Standards Loading Hierarchy

Every skill loads standards in this order:

```yaml
1. Framework Core (MANDATORY - always loaded):
   - ai-agent-compliance-core.yaml
   - enterprise-code-quality-enforcement-core.yaml
   - rtfm-protocol-core.yaml
   - production-ready-checklist.yaml

2. Language Standards (python):
   - python-coding.standard.yaml
   - python-security.standard.yaml
   - python-optimization-best-practices.guide.yaml

3. Platform Standards (fastapi/fastmcp):
   - Platform-specific patterns and best practices

4. Domain Standards (context-based):
   - backend/* (API design, microservices)
   - security/* (authentication, encryption)
   - testing/* (unit, integration, E2E)
   - performance/* (caching, optimization)
   - And 8 more domains as needed...
```

---

## Role-Based Execution

Each skill loads specialized roles from `.mcp_prompts/roles/` (42 roles available):

**Design/Planning Roles:**
- planning-analyst.role.yaml
- risk-assessor.role.yaml
- architecture-compliance-reviewer.role.yaml

**Implementation Roles:**
- code-implementer.role.yaml
- refactoring-agent.role.yaml
- optimizer.role.yaml

**Quality Roles:**
- quality-validator.role.yaml
- python-type-checker.role.yaml
- python-security-scanner.role.yaml
- compliance-auditor.role.yaml

**Testing Roles:**
- unit-test-generator.role.yaml
- integration-test-runner.role.yaml
- api-test-generator.role.yaml
- test-validator.role.yaml

---

## Approval Gates

Skills pause at approval gates for user input:

**Gate 1 (After Planning):**
- Design and planning complete
- User reviews architecture/plan
- Responses: APPROVE, MODIFY, REJECT, INFO

**Gate 2 (After Implementation):**
- Core implementation complete
- User reviews code changes
- Responses: APPROVE, MODIFY, REJECT

**Gate 3 (After Validation):**
- Full validation complete
- User approves deployment
- Responses: DEPLOY, HOLD, REJECT

---

## State Management & Resume

All skills save progress to: `project/state/stepwise-execution.json`

**Resume any skill with:**
> "Continue the [skill-name] from where we left off"

Example:
> "Continue the FastAPI implementation from where we left off"

---

## Usage Examples

### Example 1: Design → Implement → Validate Workflow

```
You: "Design a FastAPI authentication service"
Claude: [Activates fastapi-design skill]
        → Executes steps 1, 3, 9-11
        → Presents architecture at Gate 1

You: "APPROVE"

You: "Implement the FastAPI authentication service"
Claude: [Activates fastapi-implement skill]
        → Executes steps 1, 12-14, 18
        → Creates routers, models, tests
        → Presents at Gate 2

You: "APPROVE"

You: "Validate the FastAPI code quality"
Claude: [Activates fastapi-quality-review skill]
        → Runs quality checks, security scan
        → Reports metrics and issues
```

### Example 2: Python Development Lifecycle

```
You: "Plan Python data processing module implementation"
Claude: [Activates python-planning skill]
        → Creates task breakdown, estimates

You: "Implement the Python data parser"
Claude: [Activates python-implement skill]
        → Writes code with tests

You: "Type check the Python code"
Claude: [Activates python-typecheck skill]
        → Runs mypy, fixes type hints

You: "Review Python code quality"
Claude: [Activates python-quality-review skill]
        → Quality metrics, security scan

You: "Fix the quality issues"
Claude: [Activates code-remediation skill]
        → Remediates all issues
```

### Example 3: MCP Server Development

```
You: "Design a FastMCP server for GitHub integration"
Claude: [Activates fastmcp-design skill]
        → Tool architecture, resource design

You: "Implement the MCP GitHub tools"
Claude: [Activates fastmcp-implement skill]
        → @mcp.tool() decorators
        → @mcp.resource() handlers
        → Authentication config

You: "Validate MCP protocol compliance"
Claude: [Activates fastmcp-quality-review skill]
        → Protocol validation
        → Security audit
```

---

## Integration with Existing Commands

These skills **complement** the existing `.claude/commands/` structure:

- **Commands**: User-invoked with `/command` syntax
- **Skills**: Auto-invoked based on intent detection

Both reference the same `.mcp_prompts/` framework orchestrators.

---

## Integration with Existing Agents

These skills **replace** the need for `.claude/agents/` in many cases:

- **Old**: Manually invoke agent via Task tool
- **New**: Skills auto-activate based on natural language

However, agents remain useful for:
- Complex multi-agent orchestration
- Background processing
- Specialized workflows

---

## Context Efficiency

**Design Philosophy:** Progressive Disclosure

- Skills are small (~50-80 lines)
- Framework files loaded just-in-time
- Standards loaded only when needed
- Roles loaded per-step

**Estimated Context Usage:**
- Skill discovery: ~3K tokens
- Orchestrator load: ~10-15K tokens
- Framework execution: ~20-30K tokens per step
- Standards (JIT): ~5-10K per standard

**Total per skill activation:** ~30-60K tokens (well within limits)

---

## Future Enhancements

**Potential Additional Skills:**
- `fastapi-endpoint-design` - Specific endpoint design
- `fastapi-router-implement` - Router implementation
- `htmx-integration` - HTMX/Jinja2 templating
- `deployment-orchestrate` - Full deployment workflow
- `monitoring-setup` - Observability configuration

**Skill Generator:**
Create script to auto-generate skills from orchestrators:
```python
python .mcp_prompts/tools/generate-skills.py --platform fastapi --all
```

---

## Troubleshooting

**Skill not activating?**
- Check description triggers in SKILL.md frontmatter
- Restart Claude Code to reload skills
- Verify orchestrator file exists in `.mcp_prompts/`

**Too much context usage?**
- Skills use progressive disclosure (only load what's needed)
- If hitting limits, reduce number of active skills
- Consider using commands instead for simple tasks

**Want custom behavior?**
- Edit SKILL.md description to change triggers
- Modify orchestrator YAML to change steps/standards
- Add custom roles in `.mcp_prompts/roles/`

---

## Maintenance

**Updating Skills:**
1. Update orchestrator YAML in `.mcp_prompts/`
2. Skills automatically reference latest version
3. No need to modify skill files

**Adding New Skills:**
1. Create orchestrator in `.mcp_prompts/{lang|platform}/`
2. Create skill directory in `.claude/skills/`
3. Copy template from existing skill
4. Customize description and orchestrator path

**Version Management:**
- All skills reference MCP Framework v6.0.0
- Framework version tracked in `.mcp_prompts/VERSION_MANIFEST.json`
- Update all skills when framework version changes

---

## License & Attribution

**Skills:** Created for ai-agents repository
**Framework:** MCP Framework v6.0.0
**Based on:** Anthropic Agent Skills specification

**References:**
- `.mcp_prompts/README.md` - Framework documentation
- `.mcp_prompts/STRUCTURE_GUIDE_v6.0.0.md` - Architecture guide
- `.claude/docs/agent-skills.md` - Skills documentation

---

**Total Development Time:** ~3 days
**Total Framework Files:** 219 YAML files
**Total Skills:** 21 custom skills
**Lines of Framework Code:** 64,752+ lines
