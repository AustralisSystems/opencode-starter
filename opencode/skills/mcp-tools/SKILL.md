---
name: mcp-tools
description: MANDATORY MCP tools workflow enforcement for ALL tasks. Ensures proper use of neo4j-memory, context7, grep, sequential-thinking, and other MCP tools following THE GOLDEN RULE workflow. Use this to validate MCP tool usage compliance.
allowed-tools: [*]
metadata:
  auto_approval_supported: true
  auto_approval_gates: [1]
  safe_for_auto_approval: true
---

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

### Special Note on "ALWAYS" and "NEVER"

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)

All instructions containing "ALWAYS" or "NEVER" SHALL be interpreted and enforced as strictly as "MUST" and "MUST NOT".

### Special Note on "FORBIDDEN"

- **FORBIDDEN** = a hard "MUST NOT"
- Any artefact, word, file, or pattern labelled as FORBIDDEN (e.g. file/module/function name "enhanced", or other banned logic or artefacts):
  - MUST be detected, flagged, and immediately removed or refactored from the codebase
  - All references MUST be updated and corrected
  - Remediation MUST be logged as a protocol enforcement action
  - No exceptions and no warnings--immediate correction is REQUIRED

### Enforcement

- No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.
- All instructions using these words are enforceable protocol, not mere suggestions.
- MUST/SHALL = absolute requirement, NEVER/FORBIDDEN = absolute prohibition

---

# MCP Tools Workflow Orchestrator

**Type:** MANDATORY | **Compliance Enforcement** | **Framework Integration**

## Auto-Activation

I activate AUTOMATICALLY for EVERY task to ensure MCP tool compliance.

This skill is FOUNDATIONAL and runs alongside all other skills.

## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**

- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
- "auto-approve Gate 1"

**What happens:**

- I validate MCP tool usage without pausing
- I ensure compliance with THE GOLDEN RULE
- I verify all 6 phases are followed
- State is tracked for review/rollback

**Safety:** SAFE - This is a compliance validation skill (read-only verification)

## ⚠️ CRITICAL: THE GOLDEN RULE - AUTONOMOUS STEPWISE EXECUTION

**MANDATORY WORKFLOW FOR EVERY TASK:**

```
context7 (docs) → grep (examples) → neo4j-memory (record) → code → neo4j-memory (persist)
```

**ZERO EXCEPTIONS ALLOWED**

**AUTONOMOUS EXECUTION MODE (2025 UPDATE):**

- Execute ALL steps WITHOUT manual intervention
- Use `alwaysThinkingEnabled` for complex reasoning
- Operate in `bypassPermissions` mode (fully autonomous)
- Follow stepwise approach: PLAN → EXECUTE → VALIDATE → COMMIT
- Use parallelism for independent operations (max 3 concurrent tasks)
- Apply progressive thinking triggers ("think" → "think hard" → "ultrathink")
- Never pause for approval - AUTO-APPROVE mode is MANDATORY

## THE 6-PHASE MANDATORY SEQUENCE - FULL AUTONOMOUS STEPWISE EXECUTION

**REQUIRED FOR EVERY TASK (FULLY AUTONOMOUS):**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  START TASK (AUTO-APPROVE MODE)                                            │
│      ↓                                                                      │
│  1. ✅ CONTEXT LOAD (neo4j-memory) - Execute autonomously                  │
│      ↓                                                                      │
│  2. 🔴 MANDATORY RESEARCH (context7 + grep) - NO EXCEPTIONS                │
│      ↓                                                                      │
│  3. ✅ PLANNING (sequential-thinking) - Use "think hard" for complexity    │
│      ↓                                                                      │
│  4. ✅ IMPLEMENTATION (filesystem + domain tools) - Parallel when possible │
│      ↓                                                                      │
│  5. ✅ PROGRESS TRACKING (neo4j-memory) - Real-time updates                │
│      ↓                                                                      │
│  6. ✅ CONTEXT SAVE (neo4j-memory) - Persist all learnings                 │
│      ↓                                                                      │
│  END TASK → VALIDATE → COMMIT (if 100% successful)                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

**🔴 CRITICAL: NEVER SKIP THE RESEARCH PHASE - IT PREVENTS AI HALLUCINATIONS**

**🚀 AUTONOMOUS STEPWISE EXECUTION REQUIREMENTS:**

1. **NO PAUSING**: Execute all steps continuously without manual approval
2. **STEPWISE APPROACH**: Complete each phase before moving to next
3. **PARALLEL EXECUTION**: Run independent tasks concurrently (max 3)
4. **PROGRESSIVE THINKING**: Use appropriate thinking intensity per task complexity
5. **AUTO-VALIDATION**: Validate each step completion before proceeding
6. **AUTO-COMMIT**: Commit successful changes automatically with proper message

## Phase 1: Context Load (MANDATORY)

**Tools:** `neo4j-memory`

**Iterative Context Retrieval Strategy:**

1. **Query for relevant past knowledge** (progressive expansion)

   - Focus on recent past with entries relating to current project or repository
   - **Start narrow**: Query last 5 minutes for immediate context
   - **Expand to 30 minutes** if insufficient context found
   - **Expand to 1 hour** if still insufficient
   - **Broaden timeframe** to 4-48 hours as needed
   - **Broaden query terms** if timeline expansion doesn't help
2. **Create entities for new strategic objectives**

   - Document task goals and requirements
   - Track decisions and rationale
   - Record interim results and progress
3. **Build relationship graph for task dependencies**

   - Map dependencies between entities
   - Track execution flow and relationships
   - Document context for future sessions

**Progressive Query Pattern:**

```markdown
Step 1: START NARROW (last 5 minutes, specific to current task)
→ search_memories: "{project} {specific_task} last 5 minutes"

Step 2: EXPAND TIME (if insufficient, try 30 minutes)
→ search_memories: "{project} {broader_context} last 30 minutes"

Step 3: EXPAND FURTHER (if still insufficient, try 1 hour)
→ search_memories: "{project} {related_work} last 1 hour"

Step 4: BROADEN SCOPE (if needed, expand to 4-48 hours)
→ search_memories: "{project} {domain} last 24 hours"
→ find_memories_by_name: ["{EntityName}", "{ProjectName}"]

Step 5: VERIFY COMPLETENESS
→ Ensure sufficient context before proceeding
```

**Example Queries:**

```
# Start narrow
search_memories: "saw-automation-projects PowerShell script updates last 5 minutes"

# Expand as needed
search_memories: "windows-drive-analysis-cleanup refactoring last 30 minutes"
search_memories: "automation script portability changes last 1 hour"

# Broaden scope if needed
find_memories_by_name: ["DriveCleanup", "TestData Reorganization"]
```

**❌ FORBIDDEN:**

```
neo4j-memory read_graph  # NEVER at session start - too broad
```

## Phase 2: 🔴 MANDATORY RESEARCH (PREVENTS HALLUCINATIONS)

**Tools:** `context7` + `grep` (BOTH REQUIRED)

**RTFM Protocol Integration:**

**Step 1: Smart Codebase Exploration (MAX 20 files)**

- Use `filesystem` to index structure only
- Read max 10 high-priority files
- Achieve 90% codebase understanding

**Step 2: Documentation Research (MANDATORY)**

- `context7`: Get current, accurate, version-specific documentation
- `fetch`: Additional documentation with credibility validation
- Achieve 85% documentation comprehension

**Step 3: Online Research (MANDATORY)**

- `grep`: Find real production code examples on GitHub
- Validate sources using tier-based credibility
- Achieve 95% implementation readiness

**Step 4: Quality Gate Validation**

- Codebase Understanding: ≥90%
- Documentation Comprehension: ≥85%
- Implementation Readiness: ≥95%

**Example Research Sequence:**

```
1. context7: "FastAPI JWT authentication security patterns 2025"
2. grep: "FastAPI jwt authentication middleware production"
3. Validate understanding against codebase
4. Proceed only when all thresholds met
```

**THE GOLDEN RULE STARTS HERE:**

```
context7 (get official docs) → grep (find real examples) → proceed to planning
```

## Phase 3: Planning (REQUIRED)

**Tools:** `sequential-thinking`, `neo4j-memory`

**Actions:**

- Create structured plan using research findings
- Generate numbered steps with checkpoints
- Track every planning decision
- Save complete plan with rationale

**Example Planning:**

```
sequential-thinking: Plan JWT middleware implementation
  Step 1: Create auth middleware based on context7 docs
  Step 2: Implement token validation using grep examples
  Step 3: Add dependency injection
  Checkpoint: Validate against plan after each step

neo4j-memory: "plan_step_1: create middleware, reason: separation of concerns"
neo4j-memory: "project_id=ai-agents; save plan with research sources"
```

## Phase 4: Implementation (WITH TRACKING)

**Primary Tools:** `filesystem` + domain-specific tools

**Smart Recording Division:**

**Use `neo4j-memory` for ACTIVE WORK:**

- Current task tracking
- Debugging notes
- Immediate next steps
- Trial approaches

**Example Active Tracking:**

```
neo4j-memory: "working on: auth middleware, current task: token validation"
neo4j-memory: "trying: JWT decode with python-jose"
neo4j-memory: "debugging: secret key validation"
```

**Use `neo4j-memory` for SIGNIFICANT FINDINGS:**

- Successful patterns discovered
- Problems solved
- Important decisions made
- Reusable approaches

**Example Knowledge Persistence:**

```
neo4j-memory: "project_id=ai-agents; solved: JWT validation → use python-jose[cryptography]"
neo4j-memory: "project_id=ai-agents; pattern: middleware before routes for CORS"
```

**Domain-Specific Tools:**

- Frontend: `shadcn-ui`, `chakra-ui`, `lucide-icons`
- Testing: `playwright`
- AI Workflows: `zen`
- Time Operations: `time` (for reverse date stamps)

## Phase 5: Progress Tracking (LIGHTWEIGHT)

**Tools:** `neo4j-memory`, `sequential-thinking`

**Smart Recording:**

- Track current state only
- Record significant milestones
- Document blockers immediately
- Validate against plan

**Example Progress:**

```
neo4j-memory: "progress: step 3 of 7"
neo4j-memory: "blocked_by: missing API configuration"
neo4j-memory: "project_id=ai-agents; milestone: authentication complete"
sequential-thinking: Validate checkpoint - all steps passing
```

## Phase 6: Context Save (CURATED KNOWLEDGE)

**Tools:** `neo4j-memory`

**Final Knowledge Extraction:**

1. Review session notes for important outcomes
2. Transfer high-value learnings to neo4j-memory
3. Persist curated knowledge with reverse date stamps

**Example Context Save:**

```
neo4j-memory: "project_id=ai-agents; session_outcome: JWT auth implemented successfully"
neo4j-memory: "project_id=ai-agents; key_learning: always use python-jose[cryptography] not just python-jose"
neo4j-memory: "project_id=ai-agents; resolved_issue: CORS → add middleware before routes"
neo4j-memory: "project_id=ai-agents; next_session: implement refresh token rotation"
```

## Task-to-Tool Mapping Matrix

| Task Type                   | Primary MCP Tools                                | Secondary Tools     |
| --------------------------- | ------------------------------------------------ | ------------------- |
| **Starting Session**  | neo4j-memory (load context)                      | N/A                 |
| **Before ANY Code**   | context7 + grep                                  | fetch, filesystem   |
| **Planning Features** | sequential-thinking                              | neo4j-memory        |
| **Debugging Issues**  | grep (search errors), context7 (docs)            | sequential-thinking |
| **Writing Code**      | context7 (FIRST), grep (SECOND), filesystem      | neo4j-memory        |
| **Refactoring**       | context7 (patterns), grep (examples)             | sequential-thinking |
| **Frontend Dev**      | context7 (framework docs), shadcn-ui, chakra-ui  | lucide-icons        |
| **API Testing**       | playwright, fetch                                | context7 (API docs) |
| **Documentation**     | context7 (specs), filesystem                     | neo4j-memory        |
| **Security**          | grep (vulnerabilities), context7 (security docs) | sequential-thinking |

## Common Tool Combination Patterns

**Pattern 1: Feature Implementation (CORRECT ORDER)**

```
neo4j-memory (load) → context7 (docs) → grep (examples) →
sequential-thinking (plan) → filesystem (code) →
neo4j-memory (track) → neo4j-memory (save)
```

**Pattern 2: Bug Investigation**

```
neo4j-memory (context) → grep (error patterns) →
context7 (API docs) → sequential-thinking (analyze) →
filesystem (fix) → neo4j-memory (document)
```

**Pattern 3: Frontend Component**

```
context7 (framework docs) → grep (examples) →
shadcn-ui (component) → filesystem (integrate) →
playwright (test) → neo4j-memory (save)
```

**Pattern 4: API Development**

```
context7 (framework docs) → grep (patterns) →
sequential-thinking (design) → filesystem (implement) →
fetch (test) → neo4j-memory (persist)
```

## MCP Tools Inventory

**Core Memory & Thinking (MANDATORY):**

- `neo4j-memory` - Enduring knowledge graph - MANDATORY for ALL persistence
- `sequential-thinking` - Structured reasoning - MANDATORY for planning

**Research Tools (MANDATORY BEFORE CODING):**

- `context7` - Official documentation - MANDATORY
- `grep` - GitHub code examples - MANDATORY

**File & Web Operations:**

- `filesystem` - File read/write
- `fetch` - HTTP content retrieval
- `time` - Timestamps (MANDATORY for reverse date stamps YYYY-MM-DD-HHMMSS)

**Advanced Tools:**

- `zen` - Multi-model AI orchestration
- `playwright` - Browser automation and testing

**Frontend Development:**

- `shadcn-ui` - shadcn/ui components
- `chakra-ui` - Chakra UI components
- `lucide-icons` - Icon library
- `vite-plugin` - Vite build tool

**DEPRECATED (DO NOT USE):**

- `memory` - Replaced by neo4j-memory
- `extended-memory` - Replaced by neo4j-memory

## Mandatory Compliance Rules

1. **🔴 ALWAYS use context7 BEFORE writing code** - Get current docs
2. **🔴 ALWAYS use grep to search GitHub** - Find real examples
3. **🔴 ALWAYS record in neo4j-memory AS YOU WORK** - Track everything
4. **🔴 ALWAYS save to neo4j-memory** - Persist for future sessions
5. **NEVER skip Context Load** - Start by querying relevant context
6. **NEVER implement without Research** - context7 + grep MANDATORY
7. **NEVER complete without Context Save** - Persist learnings
8. **ALWAYS use sequential-thinking for complex tasks** - Structure approach
9. **ALWAYS use time for reverse date stamps** - YYYY-MM-DD-HHMMSS format

## ABSOLUTELY FORBIDDEN

**❌ FORBIDDEN PRACTICES:**

- Proceeding without context7 research
- Coding without grep examples
- Skipping neo4j-memory context load
- Implementing without sequential-thinking plan
- Completing without saving to neo4j-memory
- Using deprecated memory or extended-memory tools
- Skipping any of the 6 mandatory phases

**VIOLATION RESPONSE:**
Any violation triggers immediate halt and mandatory correction:

1. HALT current operation
2. DECLARE violation
3. ANALYZE root cause
4. CORRECT immediately
5. REINFORCE protocol understanding
6. RESUME with compliance

## Date Stamp Requirements

**ALL neo4j-memory operations and file outputs MUST include reverse date stamps:**

**Format:** `YYYY-MM-DD-HHMMSS` (UTC)

**Example:**

```
time: Generate current UTC timestamp in format YYYY-MM-DD-HHMMSS
neo4j-memory: "project_id=ai-agents; timestamp=2025-01-22-143000; session_complete"
```

**MANDATORY:**

- Use UTC timestamps for all operations
- Include date stamps in all entity creation
- Apply to all memory operations
- Use for all file naming

**FORBIDDEN:**

- Operations without timestamps
- Inconsistent date formats
- Missing timestamps in documentation

## Execution

**This skill enforces compliance through:**

1. **Pre-task validation** - Verify context loaded
2. **Research gate** - Ensure context7 + grep completed
3. **Planning verification** - Confirm sequential-thinking used
4. **Implementation tracking** - Monitor neo4j-memory usage
5. **Progress validation** - Check tracking maintained
6. **Save verification** - Ensure knowledge persisted

**READ:** `.claude/commands/ai-agent-compliance.md`
**READ:** `.claude/commands/ai-agent-compliance-protocols.md`

**Standards:**

- Core: MCP Framework v6.0.0 compliance
- Tools: All MCP server specifications
- Quality: RTFM protocol integration
- Memory: Neo4j knowledge graph standards

## Output

- MCP tool usage validation
- Compliance verification reports
- Protocol violation alerts
- Workflow adherence confirmation
- Knowledge persistence validation
- Research completeness verification

## Related

**ALL skills must follow this workflow:**

- `python-implement`
- `fastapi-implement`
- `fastmcp-implement`
- `test-implementation`
- All design, planning, quality, and refactor skills

**Integration with:**

- RTFM protocol enforcement
- Enterprise template scaffolding
- Auto-approval workflow
- Quality validation
