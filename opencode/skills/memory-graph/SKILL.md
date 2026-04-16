# MemoryGraph Tools Reference

Complete guide to all MCP tools in MemoryGraph, including usage patterns and configuration.

**Last Updated**: December 2025
**Version**: v0.10.0

---

## Memory Protocol

### REQUIRED: Before Starting Work
You MUST use `recall_memories` before any task. Query by project, tech, or task type.

### REQUIRED: Automatic Storage Triggers
Store memories on ANY of:
- **Git commit** → what was fixed/added
- **Bug fix** → problem + solution
- **Version release** → summarize changes
- **Architecture decision** → choice + rationale
- **Pattern discovered** → reusable approach

### Timing Mode (default: on-commit)
`memory_mode: immediate | on-commit | session-end`

### Memory Fields
- **Type**: solution | problem | code_pattern | fix | error | workflow
- **Title**: Specific, searchable (not generic)
- **Content**: Accomplishment, decisions, patterns
- **Tags**: project, tech, category (REQUIRED)
- **Importance**: 0.8+ critical, 0.5-0.7 standard, 0.3-0.4 minor
- **Relationships**: Link related memories when they exist

### Common Relationship Patterns
- Solutions SOLVE problems
- Fixes ADDRESS errors
- Patterns APPLY_TO projects
- Decisions IMPROVE previous approaches
- Errors TRIGGER problems
- Changes CAUSE issues

### Session Management
At the end of each session:
1. Use `store_memory` with type=task to summarize what was accomplished
2. Include what's next in the content
3. Tag with project name and date

Do NOT wait to be asked. Memory storage is automatic.

## Team Memory Protocol

### Shared Memory Guidelines
This team uses MemoryGraph for collective knowledge. Follow these practices:

#### Storage Standards
- **Be descriptive**: Others will search for your memories
- **Include context**: Why decisions were made, not just what
- **Tag consistently**: Use agreed-upon tags (see below)
- **Link everything**: Create relationships between related memories

#### Team Tagging Convention
Required tags for all team memories:
- `team:[team-name]` - Which team stored this
- `project:[project-name]` - Which project it applies to
- `component:[component-name]` - Which part of the system
- Technology tags: `python`, `fastapi`, `postgresql`, `react`, etc.

#### Memory Ownership
- Add your name or initials in tags: `author:[yourname]`
- Update existing memories if you discover new information
- Leave a comment in the content explaining changes

#### Session Routine
**Start of day**:
- "What did the team work on yesterday?"
- "Recall any issues in [component] I should know about"

**During work**:
- Store solutions to non-trivial problems
- Link to existing problems when you solve them
- Update memories if approach changes

**End of day**:
- "Store a summary of what I accomplished today"
- Tag with `daily-summary` and current date

#### Common Memory Flows
**Bug fixing**:
1. Check: "Have we seen [error] before?"
2. Store: Problem (if new) + Solution
3. Link: solution SOLVES problem
4. Tag: `bug-fix`, component, technologies

**Feature development**:
1. Check: "What patterns have we used for [use case]?"
2. Store: Implementation as code_pattern
3. Link: pattern APPLIES_TO project
4. Tag: `feature`, component, pattern-name

**Architecture decisions**:
1. Store: Decision with full rationale
2. Link: decision IMPROVES previous_approach (if applicable)
3. Tag: `architecture`, `decision`, affected components

### Sprint Workflows
**Sprint planning**:
- "Recall problems from last sprint"
- "What technical debt did we identify?"

**Sprint retro**:
- "What solutions worked well this sprint?"
- Store top improvements as decision memories

**Onboarding**:
- New team members: "Catch me up on [project/component]"
- Returns: Decisions, patterns, known issues

## Memory Protocol - Web Development

### Store These Patterns
- **API Design**: Endpoint structure, error handling, validation
- **Authentication**: JWT flows, session management, OAuth patterns
- **Database**: Query optimization, migration patterns, schema decisions
- **Frontend**: Component patterns, state management, performance tricks
- **Deployment**: CI/CD configs, environment setup, rollback procedures

### Common Relationships
- API endpoint patterns APPLY_TO projects
- Performance optimizations IMPROVE slow_queries
- Security fixes ADDRESS vulnerabilities
- New patterns REPLACE deprecated_patterns

### Typical Session Flow
1. Start: "Recall API patterns for [feature]"
2. Develop: [Implementation]
3. Store: "Store this error handling pattern"
4. Link: pattern APPLIES_TO this_project
5. End: "Store feature completion summary"


## Quick Start: Tool Selection

Follow this decision tree when working with memories:

```
User Request
│
├─ Recall/Search Query? → START WITH recall_memories
│  ├─ Results found? → Use get_memory or get_related_memories for details
│  └─ No results? → Try search_memories with different parameters
│
├─ Store New Information? → START WITH store_memory
│  └─ After storing? → Use create_relationship to link related memories
│
├─ Explore Connections? → START WITH get_related_memories
│
├─ Update/Delete? → get_memory first, then update_memory or delete_memory
│
└─ Overview/Stats? → get_recent_activity or get_memory_statistics
```

---

## Profile Overview

| Profile | Tool Count | Description | Use Case |
|---------|------------|-------------|----------|
| **core** | 9 | Essential memory operations | Default for 95% of users |
| **extended** | 12 | Core + analytics + contextual search | Power users |

**Note**: As of v0.10.0+, 29 unimplemented tools were removed, saving ~40-45k context tokens. See [ADR-017](adr/017-context-budget-constraint.md).

### Quick Comparison

| Feature | Core (Default) | Extended |
|---------|----------------|----------|
| Memory CRUD | ✅ 5 tools | ✅ 5 tools |
| Relationships | ✅ 2 tools | ✅ 2 tools |
| Discovery | ✅ 2 tools | ✅ 2 tools |
| Database Stats | ❌ | ✅ 1 tool |
| Complex Queries | ❌ | ✅ 1 tool |
| Contextual Search | ❌ | ✅ 1 tool |

---

## Core Profile (9 tools) - DEFAULT

### Primary Tools (Use First)

#### 1. recall_memories 🎯 RECOMMENDED FIRST CHOICE

**Use for**:
- Any recall or search query from user
- "What did we learn about X?"
- "Show me solutions for Y"
- "Catch me up on this project"

**Why first**:
- Optimized defaults (fuzzy matching, relationships included)
- Simpler interface for natural language queries
- Best results for common use cases

**When to skip**:
- Need exact match only → use `search_memories` with `search_tolerance="strict"`
- Need advanced boolean queries → use `search_memories`

#### 2. store_memory

**Use for**:
- Capturing new solutions, problems, errors, decisions
- Recording patterns or learnings
- Documenting technology choices

**Always follow with**:
- `create_relationship` to link to related memories

#### 3. create_relationship

**Use for**:
- After storing a solution → link to problem it solves
- After documenting an error → link to its fix
- Connecting decisions to what they improve

**Common patterns**:
- solution SOLVES problem
- fix ADDRESSES error
- decision IMPROVES previous_approach
- pattern APPLIES_TO project

**35+ relationship types** across categories: Causation, Solution, Context, Dependency, Knowledge, Comparison, Workflow.

### Secondary Tools (Drill-Down)

#### 4. search_memories

**Use when recall_memories isn't suitable**:
- Need strict exact matching (`search_tolerance="strict"`)
- Need to search with specific tags
- Need to filter by importance threshold
- Advanced queries requiring fine control
- Need pagination for large result sets

**Pagination**:
```python
# First page (results 0-49)
search_memories(query="authentication", limit=50, offset=0)

# Second page (results 50-99)
search_memories(query="authentication", limit=50, offset=50)
```

#### 5. get_memory

**Use for**:
- Getting full details when you have a specific ID
- Verifying memory before update/delete
- Drilling down from search results

#### 6. get_related_memories

**Use for**:
- After finding a memory, explore what connects to it
- "What caused this problem?"
- "What solutions exist for this?"
- Following chains of reasoning

**Filter by relationship types**:
- `relationship_types=["SOLVES"]` → Find solutions
- `relationship_types=["CAUSES", "TRIGGERS"]` → Find causes
- `relationship_types=["USED_IN"]` → Find where pattern applies

### Utility Tools

#### 7. update_memory

**Use for**: Corrections, adding tags, updating importance.
**Always**: Use `get_memory` first to verify contents.

#### 8. delete_memory

**Use for**: Removing obsolete or incorrect memories.
**Warning**: Deletes all relationships too (cascade). Irreversible.

#### 9. get_recent_activity

**Use for**:
- Session briefing and progress tracking
- Summary of recent memories (last N days)
- Unresolved problems highlighted
- "Catch me up" functionality

---

## Extended Profile (12 tools)

All Core tools plus:

### 10. get_memory_statistics

**Use for**:
- Database overview and metrics
- Total memories and relationships
- Breakdown by memory type
- Average importance scores

### 11. search_relationships_by_context

**Use for**:
- Complex relationship queries
- Search by structured context fields (scope, conditions, evidence)
- Filter by implementation scope (partial/full/conditional)
- Advanced relationship analytics

### 12. contextual_search

**Use for**:
- Scoped search within related memories
- Two-phase search: find related memories, then search within that set
- Search within a specific problem context
- No leakage outside context boundary

---

## Common Usage Patterns

### Pattern: "What did we learn about X?"

```
Step 1: recall_memories(query="X")
Step 2: [Present results]
Step 3 (if user asks): get_memory(memory_id="...")
Step 4 (if user wants connections): get_related_memories(memory_id="...")
```

### Pattern: User Solves a Problem

```python
# Step 1: Store the solution
store_memory(
    type="solution",
    title="Fixed Redis timeout with 5s connection timeout",
    content="...",
    tags=["redis", "timeout"]
)
# → Returns memory_id: "sol-123"

# Step 2: Find related problem
recall_memories(query="Redis timeout", memory_types=["problem", "error"])
# → Finds memory_id: "prob-456"

# Step 3: Create link
create_relationship(
    from_memory_id="sol-123",
    to_memory_id="prob-456",
    relationship_type="SOLVES"
)
```

### Pattern: "Catch me up"

```
Step 1: get_recent_activity(days=7, project="/current/project")
Step 2: Present summary with unresolved problems highlighted
```

---

## Tool Categories Summary

| Category | Tools | Profile |
|----------|-------|---------|
| Memory CRUD | store_memory, get_memory, search_memories, update_memory, delete_memory | core |
| Relationships | create_relationship, get_related_memories | core |
| Discovery | recall_memories, get_recent_activity | core |
| Statistics | get_memory_statistics | extended |
| Advanced Queries | search_relationships_by_context | extended |
| Contextual Search | contextual_search | extended |

---

## Profile Configuration

### Environment Variable

```bash
# Core (default)
export MEMORY_TOOL_PROFILE=core

# Extended
export MEMORY_TOOL_PROFILE=extended
```

### CLI Flag

```bash
# Core (default)
memorygraph

# Extended
memorygraph --profile extended
```

### MCP Configuration

```json
{
  "mcpServers": {
    "memorygraph": {
      "command": "memorygraph",
      "args": ["--profile", "extended"],
      "env": {
        "MEMORY_BACKEND": "sqlite"
      }
    }
  }
}
```

---

## Choosing Your Profile

### Use Core Profile If:
- ✅ You're getting started
- ✅ You need basic memory storage and retrieval
- ✅ You want zero configuration
- ✅ You're a typical user (95% of use cases)

### Use Extended Profile If:
- ✅ You need database statistics
- ✅ You want advanced relationship queries
- ✅ You're analyzing patterns across large memory sets
- ✅ You need contextual/scoped search

---

## Backend Compatibility

All 12 tools work with all backends:
- **SQLite** - Default, zero configuration
- **Neo4j** - Requires setup, optimal for large graphs
- **Memgraph** - Requires setup, fastest analytics
- **FalkorDB** - Redis-based graph database
- **Cloud** - memorygraph.dev cloud backend

---

## Anti-Patterns to Avoid

**❌ Don't**:
- Use search_memories when recall_memories would work
- Call get_memory without an ID
- Create memory without considering relationships
- Use exact match search as default

**✅ Do**:
- Start with recall_memories for all searches
- Use create_relationship after storing related memories
- Filter by memory_types for precision
- Use get_related_memories to explore context

---

## Related Documentation

- [CONFIGURATION.md](CONFIGURATION.md) - Full configuration options
- [TEMPORAL_MEMORY.md](temporal-memory.md) - Temporal memory concepts and usage
- [CLAUDE_MD_EXAMPLES.md](CLAUDE_MD_EXAMPLES.md) - Example usage with Claude
- [SCHEMA.md](schema.md) - Memory graph schema and structure
