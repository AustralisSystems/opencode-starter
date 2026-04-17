---
name: MEMORY
description: Use MCP memory tools systematically to load prior context before work and persist important outcomes automatically during and after work. Use this skill whenever the task starts, resumes, fixes a bug, records a decision, discovers a reusable pattern, or reaches a natural completion point that should be remembered.
---

# MEMORY Skill

Use this skill to apply the repository memory protocol consistently.

## When to use

- A task is about to start and prior context may exist.
- A task is being resumed and relevant earlier work needs to be recalled.
- A bug fix, implementation outcome, or design decision should be stored.
- A reusable pattern or workflow insight has been discovered.
- A session or task is ending and important context should be persisted.

## Required startup behavior

1. Use MCP `memory` before starting substantive work.
2. Call `recall_memories` before any task.
3. Query by project, technology, or task type to narrow the retrieved context.
4. When detailed protocol semantics are needed, read `references/MEMORY_PROTOCOL.md` before proceeding.

## Automatic storage behavior

Store memory automatically when any of these occur:

- A git commit captures what changed.
- A bug fix resolves a concrete problem.
- A release summarizes a meaningful set of changes.
- An architecture decision establishes a choice and rationale.
- A reusable pattern or workflow is identified.
- An implementation, validation run, integration test, or end-to-end test produces a material outcome worth preserving.

## Preferred timing mode

- Default to `on-commit` behavior.
- Use `immediate` when an important decision or fix should not wait.
- Use `session-end` only when delayed persistence is explicitly appropriate.

## Required memory fields

- `Type`: choose a concrete type such as `solution`, `problem`, `code_pattern`, `fix`, `error`, `workflow`, `task`, `decision`, `release`, `test_result`, `snapshot`, or `rollup`.
- `Title`: make it specific and searchable, and include an identifier when possible.
- `Content`: capture context, what changed, why it mattered, and the outcome.
- `Tags`: include project, tech, category, repo identifier, date, and author where applicable.
- `Importance`: scale according to criticality.
- `Relationships`: connect related memories when available.
- `Metadata`: include traceability fields when available.

## Protocol coverage

This skill aligns with the authoritative repository memory protocol and covers:

- scoped recall before work
- automatic storage triggers
- timing mode guidance
- required schema fields
- relationship governance
- graph compaction and dedupe expectations
- pruning and rollup expectations
- mandatory session-end summaries

## Forbidden behavior

- Do not skip `recall_memories` before starting work.
- Do not wait for the user to ask before storing important memory.
- Do not create broad or weakly scoped recall queries when scoped ones are required.
- Do not create vague memory entries with weak titles or missing tags.
- Do not treat memory as optional housekeeping.

## Reference file

Read `references/MEMORY_PROTOCOL.md` when you need the full authoritative details for:

- tool contract and allowed operations
- scoped query windows and filters
- relationship edge types and canonical patterns
- compaction, dedupe, and pruning behavior
- mandatory session-end storage semantics

## Example situations

**Example 1:**
Input: You are starting work on a repo feature you have touched before.
Output: Call `recall_memories` using the project and feature area before making changes.

**Example 2:**
Input: You fix a bug and identify the root cause plus the remediation.
Output: Store a memory entry describing the bug, the fix, validation evidence, and relevant tags.

**Example 3:**
Input: You discover a reusable implementation pattern during a task.
Output: Persist the pattern as a memory entry and connect it to related nodes when applicable.
- Enables: Timeline reconstruction and progress tracking
- **Format:** ISO 8601 datetime string (YYYY-MM-DD HH:MM:SS)

### Session ID Generation

```python
# Method 1: Use terminal session (recommended)
import os
session_id = os.environ.get('TERM_SESSION_ID', f'session_{datetime.now().strftime("%Y%m%d_%H%M%S")}')

# Method 2: Generate from timestamp
from datetime import datetime
session_id = f'terminal_session_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

# Method 3: Use existing environment variable
session_id = os.environ.get('CLAUDE_SESSION_ID', 'default_session')
```

### Project Name Detection

```python
# Method 1: From git repository (recommended)
import subprocess
project_name = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip().split('/')[-1]

# Method 2: From environment variable
project_name = os.environ.get('PROJECT_NAME', 'unknown_project')

# Method 3: From current directory
import os
project_name = os.path.basename(os.getcwd())
```

---

## Memory Types

### 1. Persistent Memory (neo4j-memory)

**Purpose:** Cross-session knowledge graph that survives terminal restarts

**Characteristics:**

- ✅ Survives across sessions
- ✅ Stores entities and relationships
- ✅ Supports temporal queries
- ✅ Enables pattern recognition across time
- ✅ Single source of truth for project knowledge

**When to Use:**

- Session start: Load previous context and decisions
- During work: Record important decisions and patterns
- Session end: Save outcomes and learnings
- Any time: Query historical knowledge

**Storage:**

- **Location:** Neo4j knowledge graph database
- **Lifetime:** Permanent (until explicitly deleted)
- **Scope:** Global across all sessions for same project

### 2. Temporary Memory (session-only)

**Purpose:** Ephemeral working memory for current session only

**Characteristics:**

- ❌ Does NOT survive session restart
- ✅ Fast access during session
- ✅ Lightweight for temporary data
- ✅ Automatically cleared on session end

**When to Use:**

- Temporary calculations
- Intermediate results
- Session-specific notes
- Working variables

**Storage:**

- **Location:** In-memory (RAM)
- **Lifetime:** Current session only
- **Scope:** Single session

### Decision Matrix: Persistent vs Temporary

| Data Type                 | Persistent (neo4j-memory) | Temporary (session) |
| ------------------------- | ------------------------- | ------------------- |
| Design decisions          | ✅ YES                    | ❌ NO               |
| Implementation patterns   | ✅ YES                    | ❌ NO               |
| Code examples found       | ✅ YES                    | ❌ NO               |
| Learnings and insights    | ✅ YES                    | ❌ NO               |
| Project conventions       | ✅ YES                    | ❌ NO               |
| Intermediate calculations | ❌ NO                     | ✅ YES              |
| Temporary notes           | ❌ NO                     | ✅ YES              |
| Session progress          | ✅ YES (with session_id)  | ❌ NO               |

---

## Entity Types and Patterns

### Standard Entity Types

**1. Decision Entity:**

```python
{
    "entity_type": "Decision",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:30:00",
    "decision": "Use FastAPI for LLM gateway instead of Flask",
    "reasoning": "FastAPI provides async support, automatic OpenAPI docs, and better type safety",
    "alternatives_considered": ["Flask", "Django", "Starlette"],
    "impact": "All API endpoints will use async/await pattern"
}
```

**2. Implementation Entity:**

```python
{
    "entity_type": "Implementation",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:30:00",
    "component": "JWT Authentication Middleware",
    "file_path": "src/llm-gateway-plugin-framework/llm_gateway/api/middleware/auth.py",
    "pattern_used": "Dependency injection with FastAPI dependencies",
    "researched_from": "FastAPI docs via context7 + GitHub examples via grep",
    "solid_principles_applied": ["SRP", "DIP"]
}
```

**3. Pattern Entity:**

```python
{
    "entity_type": "Pattern",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:30:00",
    "pattern_name": "Result Pattern for Error Handling",
    "description": "Use Result[T] type for operations that can fail",
    "implementation": "from typing import Generic, TypeVar; T = TypeVar('T'); @dataclass class Result(Generic[T]): success: bool; data: T | None; error: str | None",
    "use_cases": ["API calls", "Database operations", "File I/O"],
    "source": "PowerShell Common.Core module pattern adapted for Python"
}
```

**4. Learning Entity:**

```python
{
    "entity_type": "Learning",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:30:00",
    "learning": "FastAPI dependency injection allows clean separation of concerns",
    "context": "Implementing authentication middleware",
    "application": "Use dependencies for logger, config, database connections",
    "related_solid_principle": "Dependency Inversion Principle (DIP)"
}
```

**5. Convention Entity:**

```python
{
    "entity_type": "Convention",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:30:00",
    "convention_type": "Naming",
    "rule": "All API route files use verb-based names: create_user.py, get_health.py",
    "rationale": "Clear intent, follows RESTful naming, easy to locate",
    "enforcement": "Code review checklist item"
}
```

### Relationship Patterns

**1. Decision → Implementation:**

```python
neo4j-memory: Create relationship
{
    "from_entity": "Decision: Use FastAPI for gateway",
    "relationship_type": "LEADS_TO",
    "to_entity": "Implementation: JWT Authentication Middleware",
    "created_in_session": "terminal_session_20251022_143000"
}
```

**2. Pattern → Implementation:**

```python
neo4j-memory: Create relationship
{
    "from_entity": "Pattern: Result Pattern",
    "relationship_type": "APPLIED_IN",
    "to_entity": "Implementation: Database query functions",
    "created_in_session": "terminal_session_20251022_143000"
}
```

**3. Learning → Decision:**

```python
neo4j-memory: Create relationship
{
    "from_entity": "Learning: Dependency injection benefits",
    "relationship_type": "INFLUENCED",
    "to_entity": "Decision: Use DI pattern for all services",
    "created_in_session": "terminal_session_20251022_143000"
}
```

---

## Temporal Query Patterns

### Query by Time Range

**Last 4 Hours (Current Session):**

```
neo4j-memory: Query entities created in past 4 hours for project "ai-agents"
Filter: date >= "2025-10-22 10:30:00" AND project_name = "ai-agents"
```

**Past 48 Hours (Recent Work):**

```
neo4j-memory: Query entities created in past 48 hours for project "ai-agents"
Filter: date >= "2025-10-20 14:30:00" AND project_name = "ai-agents"
```

**This Week:**

```
neo4j-memory: Query entities created this week for project "ai-agents"
Filter: date >= "2025-10-16 00:00:00" AND project_name = "ai-agents"
```

### Query by Session

**All Entities from Specific Session:**

```
neo4j-memory: Get all entities where session_id = "terminal_session_20251022_143000"
Returns: All decisions, implementations, patterns, learnings from that session
```

**All Sessions for Project:**

```
neo4j-memory: Get distinct session_ids where project_name = "ai-agents"
Returns: List of all sessions that worked on this project
```

**Session Timeline:**

```
neo4j-memory: Get entities for session "terminal_session_20251022_143000" ordered by date
Returns: Chronological timeline of session activities
```

### Query by Project

**All Entities for Project:**

```
neo4j-memory: Get all entities where project_name = "ai-agents"
Returns: Complete knowledge graph for the project
```

**Project Decisions:**

```
neo4j-memory: Get entities where project_name = "ai-agents" AND entity_type = "Decision"
Returns: All architectural and design decisions for project
```

**Project Patterns:**

```
neo4j-memory: Get entities where project_name = "ai-agents" AND entity_type = "Pattern"
Returns: All established patterns and conventions
```

### Combined Queries

**Recent Decisions for Project:**

```
neo4j-memory: Query entities where:
- project_name = "ai-agents"
- entity_type = "Decision"
- date >= "2025-10-20 00:00:00"
Returns: Recent architectural decisions
```

**Session Learnings for Project:**

```
neo4j-memory: Query entities where:
- project_name = "ai-agents"
- session_id = "terminal_session_20251022_143000"
- entity_type = "Learning"
Returns: What was learned in specific session
```

---

## The 6-Phase Memory Workflow

### Phase 1: CONTEXT LOAD (Session Start)

**When:** FIRST action of every session - MANDATORY

**Iterative Context Retrieval Strategy:**

1. **Query for relevant past knowledge** (progressive expansion)

   - Focus on recent past with entries relating to current project or repository
   - **Start narrow**: Query last 5 minutes for immediate context
   - **Expand to 30 minutes** if insufficient context found
   - **Expand to 1 hour** if still insufficient
   - **Broaden timeframe** to 4-48 hours as needed
   - **Broaden query terms** if timeline expansion doesn't help

2. **Create entities for new work**

   - Document decisions and goals
   - Track implementation progress
   - Record patterns and learnings

3. **Build relationship graph**
   - Link related decisions and implementations
   - Track dependencies between entities
   - Document knowledge flow

**Progressive Query Pattern:**

```python
# Step 1: Get current time
current_time = mcp__time__get_current_time(timezone="UTC")

# Step 2: START NARROW (last 5 minutes)
results_1 = mcp__neo4j-memory__search_memories(
    query="ai-agents implementation progress last 5 minutes"
)

# Step 3: Expand to 30 minutes if insufficient
if insufficient_context(results_1):
    results_2 = mcp__neo4j-memory__search_memories(
        query="ai-agents development work last 30 minutes"
    )

# Step 4: Expand to 1 hour if still insufficient
if insufficient_context(results_2):
    results_3 = mcp__neo4j-memory__search_memories(
        query="ai-agents decisions and patterns last 1 hour"
    )

# Step 5: Broaden to 4-48 hours if needed
if insufficient_context(results_3):
    results_4 = mcp__neo4j-memory__search_memories(
        query="ai-agents project work last 24 hours"
    )
    # Or use entity lookup
    results_5 = mcp__neo4j-memory__find_memories_by_name(
        names=["ai-agents", "LLM Gateway", "FastAPI Implementation"]
    )
```

**What to Load:**

- Recent decisions (progressive: 5 min → 30 min → 1 hr → 48 hr)
- Established patterns and conventions
- In-progress implementations
- Previous session outcomes

**Example:**

```
Session Start: 2025-10-22 14:30:00

# Progressive retrieval starting narrow
neo4j-memory search_memories: "ai-agents last 5 minutes"
→ No results, expand timeframe

neo4j-memory search_memories: "ai-agents last 30 minutes"
→ No results, expand further

neo4j-memory search_memories: "ai-agents last 1 hour"
→ Found 2 entities, expand to get full context

neo4j-memory search_memories: "ai-agents last 24 hours"
→ Retrieved full context:
  - Decision: Use FastAPI for gateway (2025-10-21)
  - Pattern: Result pattern for error handling (2025-10-21)
  - Implementation: JWT middleware (2025-10-22)
  - Learning: Dependency injection benefits (2025-10-22)

Context loaded successfully - ready to continue work
```

### Phase 2: MANDATORY RESEARCH

**When:** Before writing ANY code

**Commands:**

```
context7: "FastAPI dependency injection best practices"
grep: "FastAPI JWT authentication middleware github"
```

**NOT** memory commands - research is EXTERNAL to memory

### Phase 3: PLANNING

**When:** Complex features or multi-step tasks

**Commands:**

```
sequential-thinking: Plan implementation of authentication system
```

**Record to Memory:**

```
neo4j-memory: Create entity
{
    "entity_type": "Decision",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:35:00",
    "decision": "Authentication will use JWT with refresh tokens",
    "reasoning": "Better security than API keys, supports expiration"
}
```

### Phase 4: IMPLEMENTATION

**When:** Writing code following researched patterns

**Apply:** SOLID/DRY/KISS principles

**Record to Memory:**

```
neo4j-memory: Create entity
{
    "entity_type": "Implementation",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:45:00",
    "component": "JWT Authentication Middleware",
    "file_path": "src/llm-gateway-plugin-framework/llm_gateway/api/middleware/auth.py",
    "pattern_used": "Dependency injection",
    "researched_from": "context7: FastAPI docs, grep: GitHub examples"
}
```

### Phase 5: PROGRESS TRACKING

**When:** During implementation (not just at end)

**Commands:**

```
neo4j-memory: Record progress for session "terminal_session_20251022_143000"
- Completed: JWT middleware implementation
- In progress: Integration with FastAPI app
- Next: Unit tests for authentication
```

**Track Learnings:**

```
neo4j-memory: Create entity
{
    "entity_type": "Learning",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 15:00:00",
    "learning": "FastAPI dependencies are resolved before route handler runs",
    "application": "Use dependencies for authentication checks"
}
```

### Phase 6: CONTEXT SAVE (Session End)

**When:** End of session - MANDATORY

**Commands:**

```
neo4j-memory: Save session outcomes for "terminal_session_20251022_143000"
- Completed: JWT authentication middleware
- Decisions made: Use refresh token pattern
- Patterns established: Dependency injection for auth
- Next session: Implement unit tests
```

**What to Save:**

- Completed work
- Decisions made during session
- Patterns discovered or established
- Learnings and insights
- Next steps for future sessions

---

## Best Practices

### ✅ DO:

1. **Always include mandatory properties:**

   ```python
   {
       "session_id": "...",
       "project_name": "...",
       "date": "..."
   }
   ```

2. **Load context at session start:**

   ```
   neo4j-memory: Get recent context for project "ai-agents"
   ```

3. **Record during work, not just at end:**

   ```
   # After making decision
   neo4j-memory: Create Decision entity

   # After implementation
   neo4j-memory: Create Implementation entity
   ```

4. **Save outcomes at session end:**

   ```
   neo4j-memory: Save session summary
   ```

5. **Use temporal queries:**

   ```
   neo4j-memory: Get entities from past 48 hours
   ```

6. **Track relationships:**

   ```
   neo4j-memory: Link Decision to Implementation
   ```

7. **Record learnings:**
   ```
   neo4j-memory: Create Learning entity when discovering insights
   ```

### ❌ DON'T:

1. **Skip session_id or project_name:**

   ```python
   # ❌ WRONG - missing mandatory properties
   {
       "decision": "Use FastAPI",
       "date": "2025-10-22"
   }

   # ✅ CORRECT
   {
       "session_id": "terminal_session_20251022_143000",
       "project_name": "ai-agents",
       "date": "2025-10-22 14:30:00",
       "decision": "Use FastAPI"
   }
   ```

2. **Skip context load at session start:**

   ```
   # ❌ WRONG - starting work without context
   Start coding immediately

   # ✅ CORRECT
   neo4j-memory: Load context → Then start work
   ```

3. **Wait until end of session to record:**

   ```
   # ❌ WRONG - recording everything at end
   # (might forget details)

   # ✅ CORRECT - record as you go
   Make decision → Record to memory
   Implement → Record to memory
   Learn something → Record to memory
   ```

4. **Use deprecated tools:**

   ```
   # ❌ WRONG
   memory: ... (old tool)
   extended-memory: ... (deprecated)

   # ✅ CORRECT
   neo4j-memory: ... (current tool)
   ```

5. **Create entities without date:**

   ```python
   # ❌ WRONG
   {
       "session_id": "...",
       "project_name": "...",
       "decision": "..."
   }

   # ✅ CORRECT
   {
       "session_id": "...",
       "project_name": "...",
       "date": "2025-10-22 14:30:00",
       "decision": "..."
   }
   ```

---

## Real-World Usage Examples

### Example 1: Session Start Workflow

```
# Session starts at 2025-10-22 14:30:00
session_id = "terminal_session_20251022_143000"
project_name = "ai-agents"

# 1. Load context from past 48 hours
neo4j-memory: Query entities where:
- project_name = "ai-agents"
- date >= "2025-10-20 14:30:00"

Retrieved:
- 3 decisions
- 5 implementations
- 2 patterns
- 4 learnings

# 2. Review what was done in last session
neo4j-memory: Get entities where:
- project_name = "ai-agents"
- session_id = "terminal_session_20251021_090000"

Last session completed:
- Implemented Docker Compose setup
- Decided to use Prometheus for metrics
- Established pattern: Health check endpoints

# 3. Ready to continue work with full context
```

### Example 2: During Implementation

```
# Task: Implement JWT authentication

# 1. Research (MANDATORY)
context7: "FastAPI JWT authentication best practices 2025"
grep: "FastAPI JWT middleware github"

# 2. Record decision
neo4j-memory: Create entity
{
    "entity_type": "Decision",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:35:00",
    "decision": "Use python-jose for JWT encoding/decoding",
    "reasoning": "Most popular, well-maintained, FastAPI documentation uses it",
    "alternatives_considered": ["PyJWT", "authlib"],
    "researched_from": "context7: FastAPI security docs"
}

# 3. Implement code (SOLID/DRY/KISS)
filesystem: Create auth.py with JWT middleware

# 4. Record implementation
neo4j-memory: Create entity
{
    "entity_type": "Implementation",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:45:00",
    "component": "JWT Authentication Middleware",
    "file_path": "src/llm-gateway-plugin-framework/llm_gateway/api/middleware/auth.py",
    "pattern_used": "FastAPI dependency injection",
    "solid_principles_applied": ["SRP", "DIP"]
}

# 5. Record learning
neo4j-memory: Create entity
{
    "entity_type": "Learning",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 14:50:00",
    "learning": "FastAPI dependencies execute before route handler, perfect for auth",
    "application": "Use Depends() for all authentication checks"
}

# 6. Create relationship
neo4j-memory: Create relationship
{
    "from_entity": "Decision: Use python-jose",
    "relationship_type": "IMPLEMENTED_AS",
    "to_entity": "Implementation: JWT Authentication Middleware"
}
```

### Example 3: Session End Workflow

```
# Session ends at 2025-10-22 17:00:00

# 1. Save session summary
neo4j-memory: Create entity
{
    "entity_type": "SessionSummary",
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "date": "2025-10-22 17:00:00",
    "completed": [
        "JWT authentication middleware",
        "Integration with FastAPI app",
        "Unit tests for auth"
    ],
    "decisions_made": [
        "Use python-jose library",
        "Use refresh token pattern",
        "Store tokens in HTTP-only cookies"
    ],
    "patterns_established": [
        "Dependency injection for authentication",
        "Separate auth logic from business logic"
    ],
    "next_session": [
        "Implement rate limiting",
        "Add API key authentication",
        "Integration tests for auth flow"
    ]
}

# 2. Verify all work recorded
neo4j-memory: Count entities where:
- session_id = "terminal_session_20251022_143000"
- project_name = "ai-agents"

Result: 12 entities created this session
- 3 Decisions
- 4 Implementations
- 2 Patterns
- 3 Learnings

# Session end complete - all work persisted
```

### Example 4: Multi-Project Tracking

```
# Working on multiple projects

# Project 1: ai-agents
neo4j-memory: Create entity
{
    "session_id": "terminal_session_20251022_143000",
    "project_name": "ai-agents",
    "entity_type": "Implementation",
    "component": "LLM Gateway"
}

# Project 2: saw-automation-projects
neo4j-memory: Create entity
{
    "session_id": "terminal_session_20251022_143000",
    "project_name": "saw-automation-projects",
    "entity_type": "Implementation",
    "component": "Storage Analysis Module"
}

# Query specific project
neo4j-memory: Get all entities where project_name = "ai-agents"
Returns: Only ai-agents entities

neo4j-memory: Get all entities where project_name = "saw-automation-projects"
Returns: Only saw-automation-projects entities

# Query across projects for session
neo4j-memory: Get all entities where session_id = "terminal_session_20251022_143000"
Returns: All entities from this session across all projects
```

---

## Quick Reference

### Mandatory Entity Template

```python
{
    # MANDATORY - ALWAYS INCLUDE
    "session_id": "terminal_session_YYYYMMDD_HHMMSS",
    "project_name": "project-or-repo-name",
    "date": "YYYY-MM-DD HH:MM:SS",
    "entity_type": "Decision|Implementation|Pattern|Learning|Convention",

    # Entity-specific properties
    # ...
}
```

### Common Query Patterns

```
# Session start
neo4j-memory: Get entities for project "X" from past 48 hours

# During work
neo4j-memory: Create Decision/Implementation/Pattern/Learning entity

# Session end
neo4j-memory: Create SessionSummary entity

# Search by session
neo4j-memory: Get all entities where session_id = "Y"

# Search by project
neo4j-memory: Get all entities where project_name = "X"

# Temporal query
neo4j-memory: Get entities where project_name = "X" AND date >= "YYYY-MM-DD"
```

### Memory Type Selection

| Need                     | Use                       |
| ------------------------ | ------------------------- |
| Save for future sessions | Persistent (neo4j-memory) |
| Temporary calculation    | Temporary (session-only)  |
| Project knowledge        | Persistent (neo4j-memory) |
| Working notes            | Temporary (session-only)  |

---

**Skill Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** PRODUCTION READY

**CRITICAL REMINDER:**

- EVERY entity MUST include: session_id, project_name, date
- Load context at session start (MANDATORY)
- Record during work, not just at end
- Save outcomes at session end (MANDATORY)
- Follow THE GOLDEN RULE for all development work

**Follow THE GOLDEN RULE. Research before coding. Track progress. Save learnings.**
