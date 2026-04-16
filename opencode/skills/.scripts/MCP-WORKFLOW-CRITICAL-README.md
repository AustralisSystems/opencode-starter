# 🔴 CRITICAL: MCP Tools Workflow is MANDATORY

**Date:** 2025-10-22
**Status:** ENFORCED ACROSS ALL DEVELOPMENT SKILLS
**Compliance:** ZERO EXCEPTIONS ALLOWED

---

## ⚠️ THIS IS NOT OPTIONAL - THIS IS MANDATORY

The MCP (Model Context Protocol) Tools workflow is **CRITICAL and MANDATORY** for EVERY development task. This is not a suggestion or best practice - it is a **STRICT REQUIREMENT** that MUST be followed.

### Why This Is CRITICAL

1. **🔴 Prevents AI Hallucinations**: Research phase (context7 + grep) ensures you use CURRENT, ACCURATE information
2. **🔴 Preserves Knowledge**: neo4j-memory saves learnings across ALL sessions
3. **🔴 Ensures Quality**: Following real-world patterns from grep guarantees production-ready code
4. **🔴 Maintains Consistency**: Every developer/AI follows the same workflow

**If you skip MCP tools, you WILL:**
- Generate code from outdated patterns
- Repeat mistakes already solved
- Create hallucinated solutions that don't work
- Waste time debugging preventable issues

---

## THE GOLDEN RULE (Memorize This)

```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

**Translation:**
1. Get CURRENT official documentation (context7)
2. Find REAL production examples (grep)
3. Record your work (neo4j-memory)
4. Write code **applying SOLID/DRY/KISS principles**
5. Save learnings for future (neo4j-memory)

---

## THE 6-PHASE MANDATORY SEQUENCE

**REQUIRED FOR EVERY SINGLE TASK:**

```
┌─────────────────────────────────────────────────────────────┐
│  START TASK                                                 │
│      ↓                                                      │
│  1. ✅ CONTEXT LOAD (neo4j-memory)                         │
│      ↓                                                      │
│  2. 🔴 MANDATORY RESEARCH (context7 + grep)                │
│      ↓                                                      │
│  3. ✅ PLANNING (sequential-thinking)                      │
│      ↓                                                      │
│  4. ✅ IMPLEMENTATION (filesystem + SOLID/DRY/KISS)        │
│      ↓                                                      │
│  5. ✅ PROGRESS TRACKING (neo4j-memory)                    │
│      ↓                                                      │
│  6. ✅ CONTEXT SAVE (neo4j-memory)                         │
│      ↓                                                      │
│  END TASK                                                   │
└─────────────────────────────────────────────────────────────┘
```

### Phase 1: CONTEXT LOAD (neo4j-memory)
**MANDATORY - Load previous work BEFORE starting anything**

```python
# Query for relevant context
neo4j-memory search_memories: "ai-agents FastAPI authentication last 14 days"

# Find specific entities
neo4j-memory find_memories_by_name: ["FastAPIServer_ai_agents", "LLMGateway_2025"]

# Load architectural decisions
neo4j-memory search_memories: "plugin framework architecture decisions"
```

**WHY:** Prevents repeating work, reusing solutions, maintaining consistency

### Phase 2: 🔴 MANDATORY RESEARCH (context7 + grep)
**THIS PHASE PREVENTS AI HALLUCINATIONS - NEVER SKIP**

```python
# Step 1: Get CURRENT official documentation
context7: "FastAPI JWT authentication security patterns 2025"
context7: "Python async SQLAlchemy patterns 2025"

# Step 2: Find REAL production examples
grep: "FastAPI jwt authentication middleware production"
grep: "async SQLAlchemy session factory pattern"

# Step 3: Validate understanding
# Only proceed when you understand CURRENT best practices
```

**WHY CRITICAL:**
- context7 ensures you use CURRENT API versions (not deprecated ones)
- grep shows you REAL code from production systems
- Prevents generating theoretical solutions that don't work

**REAL EXAMPLE:**
```
❌ WITHOUT RESEARCH: Generate JWT code from memory → uses deprecated library
✅ WITH RESEARCH: context7 shows python-jose[cryptography] is current standard
```

### Phase 3: PLANNING (sequential-thinking)
**Structure your approach BEFORE coding**

```python
sequential-thinking: Plan JWT authentication implementation
  Step 1: Create auth middleware based on context7 docs
  Step 2: Implement token validation using grep examples
  Step 3: Add dependency injection
  Checkpoint: Validate against plan after each step
```

**WHY:** Structured approach prevents mistakes, enables rollback

### Phase 4: IMPLEMENTATION (filesystem + SOLID/DRY/KISS)
**Write code using researched patterns AND applying SOLID/DRY/KISS principles**

```python
# Use filesystem to write code
filesystem: Create auth/middleware.py with JWT validation

# Follow patterns from context7 + grep research
# NOT theoretical patterns from AI memory

# 🔴 MANDATORY: Apply SOLID/DRY/KISS principles
# - Single Responsibility: One class/function, one purpose
# - Open/Closed: Extend without modifying existing code
# - Liskov Substitution: Derived classes substitutable
# - Interface Segregation: Don't force unused methods
# - Dependency Inversion: Depend on abstractions
# - DRY: Don't repeat code
# - KISS: Keep it simple, don't over-engineer
```

**WHY:** Implementing researched patterns with SOLID/DRY/KISS guarantees production-ready, maintainable code

### Phase 5: PROGRESS TRACKING (neo4j-memory)
**Record decisions AS YOU WORK**

```python
neo4j-memory: "working on: auth middleware, current task: token validation"
neo4j-memory: "trying: JWT decode with python-jose[cryptography]"
neo4j-memory: "debugging: secret key validation"
```

**WHY:** Track progress, enable debugging, create audit trail

### Phase 6: CONTEXT SAVE (neo4j-memory)
**Persist learnings for FUTURE sessions**

```python
neo4j-memory: "project_id=ai-agents; solved: JWT validation → use python-jose[cryptography]"
neo4j-memory: "project_id=ai-agents; pattern: middleware before routes for CORS"
neo4j-memory: "project_id=ai-agents; next_session: implement refresh token rotation"
```

**WHY:** Knowledge preservation prevents repeating research, compounds learning

---

## ABSOLUTELY FORBIDDEN PRACTICES

**❌ NEVER DO THESE - ZERO EXCEPTIONS:**

1. **❌ Implementing without context7 + grep research**
   - Consequence: Hallucinated code, deprecated patterns, non-working solutions

2. **❌ Skipping neo4j-memory context load**
   - Consequence: Repeat solved problems, inconsistent decisions

3. **❌ Completing without saving to neo4j-memory**
   - Consequence: Lost knowledge, repeated work in future sessions

4. **❌ Using deprecated memory or extended-memory tools**
   - Consequence: Non-persistent memory, lost context

5. **❌ Generating code from scratch instead of researching**
   - Consequence: Reinventing wheels, missing best practices

6. **❌ Skipping sequential-thinking for complex tasks**
   - Consequence: Unstructured approach, difficult debugging

7. **❌ Violating SOLID/DRY/KISS principles**
   - Consequence: Technical debt, unmaintainable code, repeated bugs, production failures

---

## MCP Tools Inventory

### Core Tools (MANDATORY for ALL tasks)

**neo4j-memory** - Enduring Knowledge Graph
- Purpose: Persistent memory across ALL sessions
- When: Start of session (load), during work (record), end of session (save)
- Replaces: memory, extended-memory (deprecated)

**context7** - Official Documentation
- Purpose: Get CURRENT, accurate documentation
- When: BEFORE writing ANY code
- Critical: Prevents using outdated/deprecated patterns

**grep** - GitHub Code Search
- Purpose: Find REAL production examples
- When: BEFORE writing ANY code
- Critical: Shows you how OTHERS solved the same problem

**sequential-thinking** - Structured Reasoning
- Purpose: Plan approach before acting
- When: Complex tasks, multi-step work
- Critical: Enables systematic implementation

**filesystem** - File Operations
- Purpose: Read/write code files
- When: Implementation phase
- Usage: After research, following discovered patterns

**time** - Timestamps
- Purpose: Generate reverse date stamps (YYYY-MM-DD-HHMMSS)
- When: Creating output files, neo4j-memory operations
- Required: ALL file outputs must have timestamps

### Advanced Tools (Use when applicable)

- **fetch**: Web content retrieval
- **zen**: Multi-model AI orchestration
- **playwright**: Browser automation and testing
- **Frontend tools**: shadcn-ui, chakra-ui, lucide-icons

---

## Skills Enforcing MCP Workflow

**ALL 21 Python/FastAPI/FastMCP development skills now enforce MCP workflow:**

### Design Skills (3)
- ✅ python-design - Research patterns BEFORE designing
- ✅ fastapi-design - Research API patterns BEFORE designing
- ✅ fastmcp-design - Research MCP patterns BEFORE designing

### Planning Skills (3)
- ✅ python-planning - Research methodologies BEFORE planning
- ✅ fastapi-planning - Research API planning BEFORE planning
- ✅ fastmcp-planning - Research MCP planning BEFORE planning

### Implementation Skills (4)
- ✅ python-implement - Research + template BEFORE implementing
- ✅ fastapi-implement - Research + template BEFORE implementing
- ✅ fastmcp-implement - Research + template BEFORE implementing
- ✅ test-implementation - Research testing patterns BEFORE writing tests

### Refactor Skills (3)
- ✅ python-refactor - Research refactoring patterns BEFORE refactoring
- ✅ fastapi-refactor - Research API refactoring BEFORE refactoring
- ✅ fastmcp-refactor - Research MCP refactoring BEFORE refactoring

### Quality Review Skills (3)
- ✅ python-quality-review - Research quality standards BEFORE reviewing
- ✅ fastapi-quality-review - Research API quality BEFORE reviewing
- ✅ fastmcp-quality-review - Research MCP quality BEFORE reviewing

### Utility Skills (5)
- ✅ python-typecheck - Research typing patterns BEFORE typechecking
- ✅ quality-validation - Research validation standards BEFORE validating
- ✅ quality-security - Research security patterns BEFORE security review
- ✅ code-debug - Research error patterns BEFORE debugging
- ✅ code-remediation - Research fixes BEFORE remediating

---

## Real-World Example: JWT Authentication

### ❌ WITHOUT MCP Workflow (WRONG)
```python
# AI generates from memory (outdated)
import jwt  # Deprecated library!

def verify_token(token: str):
    return jwt.decode(token, "secret")  # Missing algorithm!
```

**Result:** Non-working code, security vulnerabilities, deprecated library

### ✅ WITH MCP Workflow (CORRECT)
```python
# Step 1: Context Load
neo4j-memory search: "ai-agents authentication patterns"
# Found: Previous JWT implementations

# Step 2: MANDATORY Research
context7: "FastAPI JWT authentication 2025"
# Learned: python-jose[cryptography] is current standard

grep: "FastAPI python-jose JWT middleware"
# Found: Real production examples with proper algorithm specification

# Step 3: Planning
sequential-thinking: Plan implementation
  1. Install python-jose[cryptography]
  2. Create middleware with algorithm specification
  3. Add proper error handling

# Step 4: Implementation (following researched patterns)
from jose import JWTError, jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]  # ✅ Algorithm specified
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Step 5: Progress Tracking
neo4j-memory: "implemented JWT with python-jose[cryptography], algorithm specified"

# Step 6: Context Save
neo4j-memory: "pattern: JWT validation requires algorithm specification"
neo4j-memory: "library: python-jose[cryptography] is current standard"
```

**Result:** Working code, current libraries, proper security, saved for future

---

## Integration with Enterprise Template

**MCP workflow integrates with the COPY-THEN-AUGMENT process:**

1. **CONTEXT LOAD**: Load previous template usage patterns
2. **MANDATORY RESEARCH**: Research current FastAPI/template best practices
3. **PLANNING**: Plan template customization approach
4. **COPY TEMPLATE**: Copy enterprise template
5. **CONFIGURE**: Set feature flags
6. **CUSTOMIZE**: Augment app/ directory
7. **TRACK**: Record customization decisions
8. **SAVE**: Persist template usage patterns

**See:** `.claude/skills/MANDATORY-SCAFFOLD-TEMPLATE.md`

---

## Database Factory Pattern Example

**From real project:** `C:\github_development\projects\agentic-intelligent-automation-azure`

The enterprise template uses MCP workflow to implement database factory patterns:

```python
# Factory pattern from template (researched via context7 + grep)
class DatabaseConfig:
    """Database configuration with auto-failover."""
    url: str
    fallback_url: str | None = None
    auto_fallback: bool = True

# SQLite ↔ PostgreSQL auto-switching
# MongoDB Community ↔ Atlas auto-switching
# TinyDB ↔ MongoDB failover
# Local-to-remote sync
```

**This pattern came from:**
1. context7: Research database failover patterns
2. grep: Find production database factory implementations
3. neo4j-memory: Save factory pattern for reuse

---

## Compliance Enforcement

### For All Development Skills

**Each skill now includes:**
- 🔴 CRITICAL: MCP Tools Workflow - MANDATORY section
- THE GOLDEN RULE enforcement
- THE 6-PHASE SEQUENCE requirement
- ABSOLUTELY FORBIDDEN practices

### Violation Response

**If MCP workflow is skipped:**
1. **HALT**: Stop current operation immediately
2. **DECLARE**: "PROTOCOL VIOLATION DETECTED - HALTING OPERATIONS"
3. **ANALYZE**: Why was the workflow skipped?
4. **CORRECT**: Execute proper MCP workflow
5. **REINFORCE**: Re-read protocol requirements
6. **RESUME**: Only after compliance restored

---

## Success Metrics

**After full enforcement:**

✅ **21/21 Python/FastAPI/FastMCP skills** enforce MCP workflow
✅ **100% compliance** with THE GOLDEN RULE
✅ **0 code generation from scratch** (all researched first)
✅ **100% knowledge preservation** (all saved to neo4j-memory)
✅ **0 AI hallucinations** (research prevents them)

---

## Quick Reference Card

**Print this and keep it visible:**

```
==========================================
    MCP WORKFLOW - MANDATORY FOR ALL
==========================================

THE GOLDEN RULE:
context7 → grep → neo4j-memory → code → neo4j-memory

THE 6 PHASES:
1. LOAD (neo4j-memory)
2. RESEARCH (context7 + grep) ← PREVENTS HALLUCINATIONS
3. PLAN (sequential-thinking)
4. CODE (filesystem)
5. TRACK (neo4j-memory)
6. SAVE (neo4j-memory)

FORBIDDEN:
❌ Code without research
❌ Skip context load
❌ Skip context save

==========================================
```

---

## Summary

**MCP Tools workflow is:**
- ✅ MANDATORY for ALL development tasks
- ✅ CRITICAL for preventing AI hallucinations
- ✅ ENFORCED across 21 development skills
- ✅ INTEGRATED with enterprise template
- ✅ NON-NEGOTIABLE - ZERO EXCEPTIONS

**THE GOLDEN RULE prevents:**
- ❌ Outdated/deprecated patterns
- ❌ Theoretical solutions that don't work
- ❌ Repeated research
- ❌ Lost knowledge
- ❌ Inconsistent implementations

**Follow THE GOLDEN RULE. Every time. No exceptions.**

```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

---

## Advanced MCP Tool Usage

### Context7: Two-Step Documentation Process

**Context7 is NOT a simple search - it's a two-step process:**

**Step 1: Resolve Library ID**
```python
# Find the correct library/documentation identifier
context7 resolve-library-id: "FastAPI"
# Returns: library_id = "fastapi-official-docs"

context7 resolve-library-id: "SQLAlchemy async patterns"
# Returns: library_id = "sqlalchemy-async-docs"
```

**Step 2: Get Library Documentation**
```python
# Fetch specific documentation using library_id
context7 get-library-docs: library_id="fastapi-official-docs" query="JWT authentication security"
# Returns: Current FastAPI JWT authentication documentation

context7 get-library-docs: library_id="sqlalchemy-async-docs" query="session factory pattern"
# Returns: Current async SQLAlchemy session factory patterns
```

**Why Two Steps?**
- **Step 1** ensures you're querying the CORRECT, CURRENT documentation source
- **Step 2** retrieves ACCURATE, version-specific information
- Prevents mixing documentation from different versions or libraries

**Best Practices:**
```python
# ✅ CORRECT - Two-step process
context7 resolve-library-id: "FastAPI middleware patterns"
context7 get-library-docs: library_id="<resolved-id>" query="CORS middleware configuration"

# ❌ WRONG - Single generic query (less accurate)
context7: "FastAPI CORS middleware"
```

**Common Library IDs to Resolve:**
- FastAPI: Authentication, middleware, dependencies, WebSockets, testing
- SQLAlchemy: Async patterns, relationship loading, migrations, query optimization
- Pydantic: Validators, custom types, serialization, settings management
- Python: Asyncio patterns, type hints, dataclasses, context managers

### Grep: Advanced Search Patterns

**Grep searches GitHub code - use specific patterns for better results:**

**1. Basic Searches:**
```python
# Find implementations
grep: "FastAPI JWT authentication middleware production"

# Find specific patterns
grep: "async def authenticate_user FastAPI"

# Find configuration examples
grep: "uvicorn.run host port workers"
```

**2. Regex Patterns (Advanced):**
```python
# Find function definitions
grep: "def (authenticate|verify)_token.*JWT"

# Find class patterns
grep: "class.*Middleware.*FastAPI"

# Find imports
grep: "from fastapi.security import.*JWT"
```

**3. File Type Filters:**
```python
# Python files only
grep: "FastAPI authentication" --type=py

# Configuration files
grep: "docker-compose" --type=yaml

# Documentation
grep: "JWT best practices" --type=md
```

**4. Repository Filters:**
```python
# High-quality repositories (>1000 stars)
grep: "FastAPI production deployment" stars:>1000

# Recently updated (within 6 months)
grep: "async SQLAlchemy patterns" pushed:>2024-07-01

# Specific organization
grep: "authentication middleware" org:fastapi
```

**5. Exclude Patterns:**
```python
# Exclude test files
grep: "authentication middleware" -path:tests

# Exclude examples/demos
grep: "production config" -path:examples -path:demo

# Exclude archived repositories
grep: "FastAPI patterns" archived:false
```

**Best Practice Workflow:**
```python
# 1. Broad search to understand landscape
grep: "FastAPI JWT authentication"

# 2. Narrow to production code
grep: "FastAPI JWT authentication" stars:>500 -path:tests -path:examples

# 3. Find specific implementation
grep: "async def verify_jwt_token" --type=py archived:false

# 4. Study multiple examples
grep: "class JWTBearer FastAPI" stars:>100
```

**What to Look For in Grep Results:**
- ✅ Production code (not tutorials/examples)
- ✅ Recently updated repositories
- ✅ High star count (community validation)
- ✅ Complete implementations (not snippets)
- ✅ Proper error handling
- ✅ Type hints and documentation

### Filesystem: Best Practices

**Filesystem performs file read/write operations - use strategically:**

**1. When to Read:**
```python
# Before editing - ALWAYS read first
filesystem read: "src/api/routes/auth.py"
# Then make informed edits

# Understanding structure
filesystem read: "pyproject.toml"
filesystem read: "docker-compose.yml"

# Reviewing existing patterns
filesystem read: "src/core/middleware/base.py"
# Learn existing patterns before implementing new ones
```

**2. When to Write:**
```python
# After research (context7 + grep)
context7: "FastAPI middleware best practices"
grep: "FastAPI custom middleware examples"
# NOW write using researched patterns
filesystem write: "src/api/middleware/custom.py"

# Following templates
filesystem read: "templates/fastapi_route_template.py"
# Use template as base
filesystem write: "src/api/routes/new_endpoint.py"
```

**3. File Organization Patterns:**
```python
# Read project structure first
filesystem list: "src/"
# Understand organization before adding files

# Follow existing conventions
# If project uses:
#   src/api/routes/
#   src/api/middleware/
#   src/api/dependencies/
# MATCH THIS STRUCTURE when adding new files
```

**4. Atomic Operations:**
```python
# ✅ GOOD - One logical change at a time
filesystem write: "src/models/user.py"  # Add User model
filesystem write: "src/api/routes/users.py"  # Add user routes
filesystem write: "tests/test_users.py"  # Add tests

# ❌ BAD - Multiple unrelated changes
filesystem write: "src/everything.py"  # DON'T dump everything in one file
```

**5. Validation After Write:**
```python
# Always validate after writing
filesystem write: "src/api/auth.py"

# Immediate validation
filesystem read: "src/api/auth.py"  # Verify what was written
# Run linting: ruff check src/api/auth.py
# Run type check: mypy src/api/auth.py
```

**Best Practices:**
```python
# 1. Read before edit (understand context)
filesystem read: "existing_file.py"

# 2. Research patterns (context7 + grep)
context7 resolve-library-id: "FastAPI patterns"
grep: "similar implementation examples"

# 3. Write following researched patterns
filesystem write: "new_file.py"

# 4. Validate immediately
filesystem read: "new_file.py"  # Verify
# Run quality checks

# 5. Record to memory
neo4j-memory: "implemented X following Y pattern from grep results"
```

### Sub-Agent Selection and Usage

**When to use Task tool with specialized sub-agents:**

**1. General-Purpose Agent:**
```python
# Use for: Complex multi-step research tasks
Task: subagent_type="general-purpose"
  prompt="Research FastAPI authentication patterns, find 5 production examples,
          analyze their approaches, and recommend best pattern for our use case"

# Use for: Deep codebase exploration
Task: subagent_type="general-purpose"
  prompt="Explore the authentication module, understand the middleware chain,
          and identify where JWT validation should be added"
```

**2. Explore Agent:**
```python
# Use for: Quick codebase navigation (fast, focused)
Task: subagent_type="Explore" thoroughness="quick"
  prompt="Find all authentication-related files in src/"

# Use for: Medium exploration
Task: subagent_type="Explore" thoroughness="medium"
  prompt="Locate JWT token validation implementation across the codebase"

# Use for: Comprehensive analysis
Task: subagent_type="Explore" thoroughness="very thorough"
  prompt="Analyze complete authentication flow from request to response,
          including all middleware, dependencies, and database interactions"
```

**3. Code-Planner-Implementer Agent:**
```python
# Use for: Planning AND implementing in one flow
Task: subagent_type="code-planner-implementer"
  prompt="Plan and implement JWT refresh token rotation feature.
          Phase 1: Analyze requirements and create implementation plan.
          Phase 2: Implement following the plan with validation at each step."

# Perfect for: Feature development with clear scope
Task: subagent_type="code-planner-implementer"
  prompt="Design and implement rate limiting middleware for FastAPI.
          Include configuration, storage, and error handling."
```

**4. Code-Debugger Agent:**
```python
# Use for: Systematic debugging
Task: subagent_type="code-debugger"
  prompt="The /api/v1/auth/login endpoint is returning 500 errors.
          Debug the issue: analyze error logs, trace execution flow,
          identify root cause, and provide fix."

# Use for: Test failures
Task: subagent_type="code-debugger"
  prompt="test_jwt_validation is failing with 'Invalid signature' error.
          Investigate test setup, JWT generation, and validation logic."
```

**5. Code-Quality-Enforcer Agent:**
```python
# Use for: Pre-commit quality validation
Task: subagent_type="code-quality-enforcer"
  prompt="Perform comprehensive quality checks on src/api/auth.py:
          - Linting (ruff, flake8)
          - Type checking (mypy)
          - Security (bandit)
          - Complexity (radon)
          Report all issues with severity levels."
```

**6. Test-Preparation-Planner + Test-Executor-Analyzer:**
```python
# Step 1: Prepare tests
Task: subagent_type="test-preparation-planner"
  prompt="Prepare comprehensive test plan for JWT authentication module.
          Validate prerequisites, analyze code coverage gaps,
          create test plan with expected vs actual tracking."

# Step 2: Execute and fix until 100%
Task: subagent_type="test-executor-analyzer"
  prompt="Execute the authentication test plan.
          Run all tests, analyze failures, automatically remediate issues,
          continue until 100% tests pass."
```

**7. Architecture-Compliance-Reviewer Agent:**
```python
# Use for: Architecture validation
Task: subagent_type="architecture-compliance-reviewer"
  prompt="Review the authentication service implementation for:
          - Microservices architecture compliance
          - Deployment protocol adherence
          - Documentation standards
          - SOLID/DRY/KISS principles"
```

**Sub-Agent Decision Matrix:**

| Task Type | Sub-Agent | Thoroughness/Mode |
|-----------|-----------|-------------------|
| Quick file search | Explore | quick |
| Understand auth flow | Explore | medium |
| Complete architecture analysis | Explore | very thorough |
| Feature planning + implementation | code-planner-implementer | N/A |
| Debug 500 error | code-debugger | N/A |
| Pre-commit quality check | code-quality-enforcer | N/A |
| Test planning | test-preparation-planner | N/A |
| Test execution with fixes | test-executor-analyzer | N/A |
| Architecture review | architecture-compliance-reviewer | N/A |
| Complex multi-step research | general-purpose | N/A |

**Best Practices for Sub-Agents:**
```python
# ✅ GOOD - Specific, actionable prompt
Task: subagent_type="code-debugger"
  prompt="The JWT validation is failing for tokens generated by our mobile app.
          Debug: Check token format, signature algorithm, secret key usage.
          Expected: Valid tokens should authenticate successfully."

# ❌ BAD - Vague prompt
Task: subagent_type="code-debugger"
  prompt="Fix authentication"  # Too vague, no context

# ✅ GOOD - Clear success criteria
Task: subagent_type="test-executor-analyzer"
  prompt="Execute authentication tests. Success criteria: 100% pass rate,
          all edge cases covered, no flaky tests."

# ❌ BAD - No success criteria
Task: subagent_type="test-executor-analyzer"
  prompt="Run tests"  # What's success? When to stop?
```

**Parallel vs Sequential Sub-Agents:**
```python
# PARALLEL - Independent tasks (use multiple Task calls in single message)
Task: subagent_type="Explore" prompt="Find all middleware files"
Task: subagent_type="Explore" prompt="Find all route handlers"
Task: subagent_type="Explore" prompt="Find all database models"
# All three run simultaneously

# SEQUENTIAL - Dependent tasks (one Task call, wait, then next)
Task: subagent_type="test-preparation-planner" prompt="Create test plan"
# Wait for completion, review plan
Task: subagent_type="test-executor-analyzer" prompt="Execute the test plan"
# Second depends on first completing
```

---

## Complete Workflow Example: Implementing Feature

**Task:** Add JWT refresh token rotation to FastAPI application

**Step 1: Context Load**
```python
neo4j-memory: Get entities where project_name="ai-agents" AND entity_type="Decision" AND date>="2025-10-20"
# Load recent authentication decisions
```

**Step 2: Research (MANDATORY)**
```python
# Context7 - Two-step process
context7 resolve-library-id: "FastAPI JWT authentication"
context7 get-library-docs: library_id="<resolved>" query="refresh token rotation patterns"

# Grep - Production examples with filters
grep: "JWT refresh token rotation FastAPI" stars:>500 -path:tests -path:examples
grep: "async def refresh_access_token" --type=py archived:false
grep: "class RefreshTokenBearer FastAPI" stars:>100
```

**Step 3: Planning**
```python
sequential-thinking: Plan JWT refresh token implementation
  Step 1: Design token storage (Redis for blacklisting)
  Step 2: Implement refresh endpoint
  Step 3: Add rotation logic
  Step 4: Update authentication middleware
  Checkpoint: Validate each step against researched patterns
```

**Step 4: Implementation (Filesystem)**
```python
# Read existing code first
filesystem read: "src/api/auth.py"
filesystem read: "src/core/security.py"

# Implement following researched patterns
filesystem write: "src/api/routes/token_refresh.py"  # New endpoint
filesystem write: "src/core/security/token_rotation.py"  # Rotation logic
filesystem write: "src/core/cache/redis_token_store.py"  # Token blacklist

# Validate immediately
filesystem read: "src/api/routes/token_refresh.py"  # Verify
```

**Step 5: Quality Check (Sub-Agent)**
```python
Task: subagent_type="code-quality-enforcer"
  prompt="Perform comprehensive quality checks on token refresh implementation:
          src/api/routes/token_refresh.py
          src/core/security/token_rotation.py
          src/core/cache/redis_token_store.py"
```

**Step 6: Testing (Sub-Agents)**
```python
# Prepare tests
Task: subagent_type="test-preparation-planner"
  prompt="Create comprehensive test plan for JWT refresh token rotation.
          Include unit tests, integration tests, security tests.
          Validate prerequisites (Redis running, test DB configured)."

# Execute and fix
Task: subagent_type="test-executor-analyzer"
  prompt="Execute token refresh test plan.
          Run all tests, analyze failures, remediate issues.
          Success criteria: 100% test pass rate."
```

**Step 7: Progress Tracking**
```python
neo4j-memory: Create entity
{
    "entity_type": "Implementation",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 15:30:00",
    "component": "JWT Refresh Token Rotation",
    "files": ["token_refresh.py", "token_rotation.py", "redis_token_store.py"],
    "pattern_used": "Token rotation with Redis blacklist",
    "researched_from": "context7: FastAPI JWT docs, grep: production examples"
}
```

**Step 8: Context Save**
```python
neo4j-memory: Create entity
{
    "entity_type": "Learning",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 16:00:00",
    "learning": "JWT refresh tokens should be rotated on each use for security",
    "pattern": "Store invalidated tokens in Redis with expiration",
    "application": "All future token implementations should use rotation"
}
```

---

**Document Version:** 2.0.0
**Last Updated:** 2025-10-22
**Status:** ENFORCED
**Compliance:** MANDATORY - ZERO EXCEPTIONS ALLOWED

**For complete workflow details, see:** `.claude/skills/mcp-tools-workflow/SKILL.md`
