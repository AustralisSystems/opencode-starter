# THE GOLDEN RULE - Mandatory MCP Workflow Skill

**Skill ID**: `golden-rule`
**Version**: 1.0.0
**Created**: 2025-10-26
**Updated**: 2025-10-26
**Type**: Workflow Protocol
**Enforcement**: MANDATORY for Sonnet agents, RECOMMENDED for all levels

---

## Overview

THE GOLDEN RULE defines the mandatory MCP tool workflow that MUST be followed before any implementation work. This protocol prevents AI hallucinations, ensures research-backed decisions, and promotes knowledge persistence across sessions.

**The Rule**:

```
context7 → grep → neo4j-memory → code → neo4j-memory
```

**Expanded**:

```
RTFM → context7 (docs) → grep (examples) → neo4j-memory (record) → code → neo4j-memory (persist)
```

---

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

---

## Activation

This skill is automatically enforced for:

- ✅ ALL Sonnet agent spawns (MANDATORY)
- ✅ Complex implementation tasks
- ✅ High-stakes code changes
- ✅ Production deployments

Can be manually invoked via:

```bash
Skill(command="golden-rule")
```

---

## The 7-Step Mandatory Workflow

### Step 1: Load Patterns from Neo4j-Memory

**Purpose**: Retrieve relevant knowledge and patterns from previous sessions

**Tool**: `mcp__neo4j-memory__search_memories`

**Iterative Context Retrieval Strategy:**

1. **Query for relevant past knowledge** (progressive expansion)

   - Focus on recent past with entries relating to current project or repository
   - **Start narrow**: Query last 5 minutes for immediate context
   - **Expand to 30 minutes** if insufficient context found
   - **Expand to 1 hour** if still insufficient
   - **Broaden timeframe** to 4-48 hours as needed
   - **Broaden query terms** if timeline expansion doesn't help

2. **Analyze retrieved patterns**

   - Review implementation patterns
   - Identify relevant approaches
   - Note architectural decisions
   - Extract successful solutions

3. **Build on existing knowledge**
   - Use found patterns as foundation
   - Avoid reinventing solved problems
   - Maintain consistency with project conventions

**Progressive Query Pattern**:

```python
# Step 1: Get current time
current_time = mcp__time__get_current_time(timezone="UTC")

# Step 2: START NARROW (last 5 minutes)
results_1 = mcp__neo4j-memory__search_memories(
    query="implementation pattern for {task_type} last 5 minutes"
)

# Step 3: Expand to 30 minutes if insufficient
if insufficient_context(results_1):
    results_2 = mcp__neo4j-memory__search_memories(
        query="implementation pattern for {task_type} last 30 minutes"
    )

# Step 4: Expand to 1 hour if still insufficient
if insufficient_context(results_2):
    results_3 = mcp__neo4j-memory__search_memories(
        query="implementation patterns and decisions for {domain} last 1 hour"
    )

# Step 5: Broaden to 4-48 hours if needed
if insufficient_context(results_3):
    results_4 = mcp__neo4j-memory__search_memories(
        query="architectural patterns and solutions for {domain} last 24 hours"
    )
    # Or use specific entity lookups
    results_5 = mcp__neo4j-memory__find_memories_by_name(
        names=["ProjectPattern", "ImplementationDecision"]
    )

# Step 6: Analyze retrieved patterns
if results:
    review_patterns(results)
    identify_relevant_approaches(results)
    extract_reusable_solutions(results)
```

**What to Query**:

- Previous fix patterns for similar issues
- Architectural decisions related to current task
- Known pitfalls and solutions
- Successful implementation approaches
- Project conventions and standards

**Example Queries**:

```
# Start narrow
search_memories: "saw-automation-projects PowerShell refactoring last 5 minutes"

# Expand as needed
search_memories: "windows-drive-analysis-cleanup implementation patterns last 30 minutes"
search_memories: "automation project architectural decisions last 1 hour"

# Broaden scope if needed
find_memories_by_name: ["DriveCleanup Pattern", "PowerShell Module Architecture"]
```

---

### Step 2: Get Documentation via Context7

**Purpose**: Fetch up-to-date official documentation for libraries/frameworks

**Tool**: `mcp__upstash-context7__resolve-library-id` + `mcp__upstash-context7__get-library-docs`

**Pattern**:

```python
# Step 2a: Resolve library ID
library_id = mcp__upstash-context7__resolve-library-id(
    libraryName="library-name"
)

# Step 2b: Get documentation for specific topic
docs = mcp__upstash-context7__get-library-docs(
    context7CompatibleLibraryID=library_id,
    topic="specific-feature-or-api",
    tokens=5000
)

# Step 2c: Analyze documentation
understand_api_signatures(docs)
identify_best_practices(docs)
note_deprecations_and_warnings(docs)
```

**What to Research**:

- Current API signatures and parameters
- Best practices and recommendations
- Common patterns and idioms
- Security considerations
- Performance implications

---

### Step 3: Find Examples via Grep

**Purpose**: Locate real-world implementation examples from GitHub repositories

**Tool**: `mcp__grep__searchGitHub`

**Pattern**:

```python
# Search for implementation patterns
examples = mcp__grep__searchGitHub(
    query="actual code pattern",  # NOT keywords
    language=["Python"],  # or TypeScript, JavaScript, etc.
    useRegexp=False
)

# Analyze examples
review_implementation_approaches(examples)
identify_common_patterns(examples)
note_edge_case_handling(examples)
extract_best_practices(examples)
```

**Search Strategy**:

- ✅ Search for LITERAL code patterns (e.g., "useState(", "async def")
- ✅ Use actual code that would appear in files
- ❌ Do NOT search for keywords or questions
- ❌ Do NOT search for "best practices" or "tutorial"

**Examples**:

- Good: `'class FastAPI('`, `'@app.route('`, `'useEffect(() =>'`
- Bad: `'fastapi tutorial'`, `'react best practices'`

---

### Step 4: Plan Solution with Sequential-Thinking

**Purpose**: Break down implementation into structured reasoning steps

**Tool**: `mcp__sequential-thinking__sequentialthinking`

**Pattern**:

```python
# Start thinking process
mcp__sequential-thinking__sequentialthinking(
    thought="Analyzing task requirements and constraints",
    thought_number=1,
    total_thoughts=10,
    next_thought_needed=True
)

# Continue through planning
# - Understand requirements
# - Identify constraints
# - Design approach
# - Plan implementation steps
# - Consider edge cases
# - Plan validation strategy
# - Estimate complexity
```

**Planning Checklist**:

- [ ] Requirements clearly understood
- [ ] Constraints identified
- [ ] Approach designed based on docs + examples
- [ ] Implementation steps outlined
- [ ] Edge cases considered
- [ ] Validation strategy planned
- [ ] Rollback plan if needed

---

### Step 5: Implement Changes (SOLID/DRY/KISS)

**Purpose**: Execute the planned implementation following best practices

**Tools**: `mcp__filesystem__*` tools (read, write, edit)

**Principles**:

- **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **DRY**: Don't Repeat Yourself - extract common patterns
- **KISS**: Keep It Simple, Stupid - prefer simplicity over cleverness

**Pattern**:

```python
# Read existing code
current_code = mcp__filesystem__read_text_file(
    path="path/to/file.py"
)

# Implement changes
mcp__filesystem__edit_file(
    path="path/to/file.py",
    edits=[{
        "oldText": "existing code",
        "newText": "improved code"
    }]
)

# Verify changes applied
verify_implementation()
```

**Implementation Checklist**:

- [ ] Follow patterns from documentation
- [ ] Apply best practices from examples
- [ ] Implement error handling
- [ ] Add input validation
- [ ] Include type hints (Python)
- [ ] Write clear comments
- [ ] Maintain consistent style

---

### Step 6: Run Comprehensive Validation

**Purpose**: Ensure implementation meets all quality standards

**Tools**: Various quality and security tools

**Required Checks**:

```yaml
type_checking:
  tool: mypy
  requirement: 0 errors, 0 warnings
  command: "python -m mypy ."

linting:
  tool: ruff
  requirement: 0 errors, 0 warnings
  command: "python -m ruff check ."

formatting:
  tool: black
  requirement: 0 issues
  command: "python -m black --check ."

security:
  tool: bandit
  requirement: 0 vulnerabilities
  command: "python -m bandit -r ."

imports:
  tool: isort
  requirement: 0 issues
  command: "python -m isort --check-only ."
```

**Pattern**:

```python
# Run validation suite
validation_results = {
    "mypy": run_mypy(),
    "ruff": run_ruff(),
    "black": run_black(),
    "bandit": run_bandit(),
    "isort": run_isort()
}

# Analyze results
if not all_checks_pass(validation_results):
    identify_failures(validation_results)
    fix_issues()
    rerun_validation()
```

**Validation Threshold**: 100% - All checks must pass

---

### Step 7: Save Pattern to Extended-Memory

**Purpose**: Persist successful patterns and learnings for future sessions

**Tool**: `mcp__neo4j-memory__create_entities` + `mcp__neo4j-memory__create_relations`

**Pattern**:

```python
# Create entities for the pattern
mcp__neo4j-memory__create_entities(
    entities=[{
        "name": f"Implementation Pattern: {task_name} {timestamp}",
        "type": "pattern",
        "observations": [
            f"Task: {task_description}",
            f"Approach: {approach_used}",
            f"Libraries: {libraries_used}",
            f"Key Decisions: {key_decisions}",
            f"Edge Cases: {edge_cases_handled}",
            f"Validation: All checks passed",
            f"Timestamp: {timestamp}"
        ]
    }]
)

# Create relationships
mcp__neo4j-memory__create_relations(
    relations=[{
        "source": f"Implementation Pattern: {task_name} {timestamp}",
        "target": "AI Agents Platform",
        "relationType": "APPLIED_TO"
    }]
)
```

**What to Save**:

- Implementation approach and reasoning
- Key decisions and trade-offs
- Libraries and versions used
- Edge cases identified and handled
- Validation results
- Lessons learned
- Future improvement notes

**Timestamp Format**: YYYY-MM-DD-HHMMSS (reverse date stamp, UTC)

---

## Quality Thresholds

### Analysis Phase (85% Confidence)

- ✅ Understanding of requirements and constraints
- ✅ Identification of existing patterns and dependencies
- ✅ Risk assessment and mitigation strategies
- ✅ Clear implementation approach planned

### Implementation Phase (90% Confidence)

- ✅ Code follows established patterns and conventions
- ✅ All dependencies properly integrated
- ✅ Error handling and edge cases addressed
- ✅ Tests implemented and passing

### Deployment Phase (95% Confidence)

- ✅ All validation commands pass with 0 errors
- ✅ Security scanning shows 0 vulnerabilities
- ✅ Performance requirements met
- ✅ Documentation complete and accurate

---

## Integration with Swarm Orchestration

### Sonnet Agent Spawning (MANDATORY)

When sonnet-swarm-orchestrator spawns Sonnet agents, it MUST include golden rule enforcement:

```python
# Sonnet agent spawn command
Bash(run_in_background=true):
  command: |
    claude --model sonnet --print << 'EOF'
    You are sonnet-agent-task-001

    MANDATORY: Follow THE GOLDEN RULE workflow

    1. extended-memory: Load previous fix patterns
    2. context7: Get library documentation
    3. grep: Find real-world examples
    4. sequential-thinking: Plan solution
    5. filesystem: Implement fix
    6. Validate: Run mypy, ruff, black, bandit
    7. extended-memory: Save pattern

    DO NOT skip any step. This is REQUIRED.

    TASK: {task_description}

    Execute following golden rule sequence.
    EOF
```

### Haiku Agent Usage (RECOMMENDED)

Haiku agents SHOULD follow simplified workflow:

- Skip context7/grep for simple, well-defined tasks
- ALWAYS use sequential-thinking
- ALWAYS validate implementation
- Save patterns for significant learnings

---

## Anti-Patterns (What NOT to Do)

### ❌ Skipping Research Phase

```python
# WRONG - Jumping straight to implementation
def fix_issue():
    # Just guessing at the solution
    implement_without_research()
```

```python
# RIGHT - Following golden rule
def fix_issue():
    # Step 1: Load patterns
    patterns = load_from_memory()

    # Step 2: Get docs
    docs = get_documentation()

    # Step 3: Find examples
    examples = search_github()

    # Step 4: Plan
    plan = sequential_thinking()

    # Step 5: Implement
    implement_solution()
```

### ❌ Skipping Validation

```python
# WRONG - Not validating changes
implement_changes()
return "Done!"
```

```python
# RIGHT - Comprehensive validation
implement_changes()
validation = run_all_checks()
if not validation.all_pass():
    fix_issues()
    revalidate()
```

### ❌ Not Persisting Knowledge

```python
# WRONG - Lost knowledge
successfully_implement()
# Knowledge dies with session
```

```python
# RIGHT - Persistent learning
successfully_implement()
save_pattern_to_memory()  # Available for future sessions
```

---

## Enforcement Levels

### Level 1: PRIME

- **Requirement**: ONLY IF WARRANTED
- **Use When**: Strategic decisions need technical understanding
- **Skip When**: Pure orchestration and coordination

### Level 2: AGENTS (All Execution Units)

- **Requirement**: MANDATORY FOR ALL CODING TASKS
- **Use When**: Any directive involving code or file operations, implementation, debugging, or code modification
- **Skip When**: Pure coordination without coding
- **Note**: This includes both Tier 1 (complex: Sonnet, Codex, Kimi Thinking, Grok 4) and Tier 2 (simple: Haiku, Grok 1, Kimi K2) agents

### Sonnet Instances

- **Requirement**: ALWAYS MANDATORY
- **Enforcement**: Orchestrator must include in spawn command
- **Validation**: No exceptions allowed

---

## Validation Checklist

Before completing ANY implementation task, verify:

- [ ] **Step 1**: Loaded relevant patterns from extended-memory
- [ ] **Step 2**: Retrieved up-to-date documentation via context7
- [ ] **Step 3**: Found real-world examples via grep
- [ ] **Step 4**: Planned approach using sequential-thinking
- [ ] **Step 5**: Implemented following SOLID/DRY/KISS principles
- [ ] **Step 6**: Ran and passed ALL validation checks (100%)
- [ ] **Step 7**: Saved successful pattern to extended-memory

**If ANY step is incomplete**: STOP and complete it before proceeding.

---

## Success Metrics

### Research Quality

- Documentation retrieved is current and official
- Examples found are relevant and production-quality
- Patterns loaded provide valuable context

### Implementation Quality

- Code follows documented best practices
- Examples' patterns properly adapted
- All validation checks pass (100%)

### Knowledge Persistence

- Patterns saved with complete context
- Timestamp properly formatted (YYYY-MM-DD-HHMMSS)
- Future sessions can benefit from learnings

---

## Example Workflow

### Scenario: Fix Type Error in auth.py

```python
# Step 1: Load Patterns
patterns = mcp__neo4j-memory__search_memories(
    query="type error fix patterns FastAPI authentication last 7 days"
)
# Result: Found 3 previous similar fixes

# Step 2: Get Documentation
library_id = mcp__upstash-context7__resolve-library-id(
    libraryName="FastAPI"
)
docs = mcp__upstash-context7__get-library-docs(
    context7CompatibleLibraryID=library_id,
    topic="type hints and validation"
)
# Result: Retrieved FastAPI type hint best practices

# Step 3: Find Examples
examples = mcp__grep__searchGitHub(
    query="from fastapi import FastAPI\nfrom typing import",
    language=["Python"]
)
# Result: Found 50+ examples of proper FastAPI typing

# Step 4: Plan Solution
mcp__sequential-thinking__sequentialthinking(
    thought="Type error in auth.py requires Pydantic model validation",
    thought_number=1,
    total_thoughts=5,
    next_thought_needed=True
)
# Result: Plan to use Pydantic BaseModel with proper type hints

# Step 5: Implement
mcp__filesystem__edit_file(
    path="src/auth/auth.py",
    edits=[{
        "oldText": "def authenticate(username, password):",
        "newText": "def authenticate(username: str, password: str) -> AuthResult:"
    }]
)
# Result: Type hints added

# Step 6: Validate
validation = {
    "mypy": run_command("python -m mypy src/auth/"),
    "ruff": run_command("python -m ruff check src/auth/")
}
# Result: All checks pass ✓

# Step 7: Save Pattern
mcp__neo4j-memory__create_entities(
    entities=[{
        "name": "Fix: Type Error FastAPI Auth 2025-10-26-143022",
        "type": "pattern",
        "observations": [
            "Task: Fix type error in authentication function",
            "Approach: Added explicit type hints using Pydantic",
            "Library: FastAPI 0.104.1, Pydantic 2.5.0",
            "Pattern: Use AuthResult return type for auth functions",
            "Validation: mypy and ruff checks passed",
            "Timestamp: 2025-10-26-143022"
        ]
    }]
)
# Result: Pattern saved for future reference
```

---

## Remember

**The Golden Rule exists to**:

- ✅ Prevent AI hallucinations by grounding in real documentation
- ✅ Ensure high-quality implementations based on proven patterns
- ✅ Build persistent knowledge that improves over time
- ✅ Maintain consistency across sessions and agents
- ✅ Reduce errors and increase confidence

**Never skip the golden rule for**:

- Production code changes
- Complex implementations
- High-stakes modifications
- Sonnet agent work (MANDATORY)

**You may simplify for**:

- Trivial fixes with high confidence
- Well-understood patterns
- Haiku agent simple tasks
- BUT: Always maintain quality standards

---

## Version History

| Version | Date       | Changes                                                             |
| ------- | ---------- | ------------------------------------------------------------------- |
| 1.0.0   | 2025-10-26 | Initial golden rule skill definition based on MCP workflow protocol |

---

**Skill Created By**: Claude Code (Sonnet 4.5)
**Based On**: MCP Tool Workflow Protocol, AI Agent Compliance Core, Swarm Orchestration Protocol
**Enforcement**: MANDATORY for Sonnet, RECOMMENDED for all
**Purpose**: Ensure research-backed, high-quality, persistent implementations
