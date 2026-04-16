---
name: test-implementation
description: Comprehensive test suite creation including unit tests, integration tests, API tests, and E2E validation. Use when creating tests, improving coverage, or implementing test strategies.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1, 2]
  safe_for_auto_approval: false
---

# Test Implementation Orchestrator

**Type:** SDLC Testing | **Comprehensive Testing**

## Auto-Activation

I activate when you mention:
- "create/write [tests/test suite]"
- "implement [unit/integration/E2E] tests"
- "test [implementation/creation]"
- "improve test coverage"
- "generate tests"


## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119. The following requirements language is binding and non-negotiable:

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Statement**: All instructions using these terms are enforceable protocol, not mere suggestions. No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.

**Special Note**: MUST/SHALL = absolute requirement, NEVER/FORBIDDEN = absolute prohibition. ALWAYS = MUST (non-negotiable requirement). No exceptions permitted.

---

## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"
- "auto-approve Gate 2"

**Examples:**
> "Implement the authentication service with auto-approval"
> "Implement the user management, auto-approve all gates" 

**What happens:**
- I execute all steps without pausing at Gate1 & Gate 2
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** CAUTION: Creates tests. Review test coverage and quality

## ⚠️ MANDATORY: MCP Tools Workflow

**ALL test implementations MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load test context and patterns
2. **MANDATORY RESEARCH**: Use `context7` + `grep` for pytest/testing patterns BEFORE coding
3. **PLANNING**: Use `sequential-thinking` to design test strategy
4. **IMPLEMENTATION**: Use `filesystem` to write test code
5. **PROGRESS TRACKING**: Record to `neo4j-memory` during work
6. **CONTEXT SAVE**: Persist test patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

**ABSOLUTELY FORBIDDEN:**
- ❌ Writing tests without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving test patterns to neo4j-memory

## ⚠️ MANDATORY: Enterprise Template Requirement

**FOR FASTAPI/PYTHON PROJECTS:**

1. **READ**: `.claude/skills/MANDATORY-SCAFFOLD-TEMPLATE.md`
2. **USE**: Test framework from enterprise template
   - `tests/` directory structure
   - `pytest.ini` configuration
   - Test fixtures in `tests/fixtures/`
3. **ADD**: Your tests following template patterns
4. **RUN**: `make test` for validation

**Template test structure:**
- `tests/fixtures/` - Shared test fixtures
- `tests/integration/` - Integration tests
- `tests/security/` - Security tests
- `tests/plans/` - Test plans

**Template Features:**
- ✅ Pytest configuration with markers
- ✅ 80% coverage minimum enforced
- ✅ Security test framework
- ✅ Plugin testing support

## Execution

**READ**: `.mcp_prompts/sdlc/test/*.yaml`

Key orchestrators:
- `test-prerequisites-prompt.yaml`
- `test-end-to-end-prompt.yaml`
- `test-live-api-prompt.yaml`

**Standards**:
- Core: `.mcp_prompts/framework/standards/ai-agent/*.yaml`
- Domains: `.mcp_prompts/domains/testing/*.yaml`
- Language: Python testing standards (pytest)

**Roles**:
- `unit-test-generator.role.yaml`
- `integration-test-runner.role.yaml`
- `api-test-generator.role.yaml`
- `test-validator.role.yaml`

## Output

- Unit tests (pytest)
- Integration tests
- API tests (FastAPI TestClient)
- E2E validation scripts
- Test fixtures
- Mock configurations
- Coverage reports
- CI/CD test integration

## Related

`python-implement`, `fastapi-implement`, `quality-validation`
