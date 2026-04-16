"""
Batch update all remaining skills with MCP workflow requirements.
This ensures CRITICAL and MANDATORY MCP tools usage is enforced everywhere.
"""

import re
from pathlib import Path

# MCP workflow templates for each skill type
MCP_TEMPLATES = {
    "planning": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL planning work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  plan  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR PLANNING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous planning decisions
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for planning patterns BEFORE creating plan
3. **PLANNING**: Use `sequential-thinking` to structure approach
4. **PLAN CREATION**: Create roadmap and task breakdown
5. **PROGRESS TRACKING**: Record decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist planning patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Planning without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving to neo4j-memory

""",
    "refactor": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL refactoring work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  refactor  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR REFACTORING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous refactoring decisions
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for refactoring patterns BEFORE refactoring
   - context7: Latest refactoring techniques and best practices
   - grep: Real-world refactoring examples from high-quality repos
3. **PLANNING**: Use `sequential-thinking` to plan refactoring strategy
4. **REFACTORING**: Apply refactoring transformations
5. **PROGRESS TRACKING**: Record refactoring decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist refactoring patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Refactoring without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving to neo4j-memory

""",
    "quality-review": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL quality review work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  review  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR QUALITY REVIEW)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous quality standards and decisions
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for quality patterns BEFORE reviewing
   - context7: Latest quality standards and best practices
   - grep: Real-world quality review criteria from top projects
3. **PLANNING**: Use `sequential-thinking` to structure review approach
4. **QUALITY REVIEW**: Perform comprehensive quality analysis
5. **PROGRESS TRACKING**: Record quality findings to `neo4j-memory`
6. **CONTEXT SAVE**: Persist quality patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Reviewing without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving to neo4j-memory

""",
    "debug": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL debugging work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  debug  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR DEBUGGING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous bug fixes and solutions
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for debugging patterns BEFORE debugging
   - context7: Official documentation for error messages and APIs
   - grep: Search GitHub for similar bugs and fixes
3. **PLANNING**: Use `sequential-thinking` to plan debugging strategy
4. **DEBUGGING**: Apply fixes and test solutions
5. **PROGRESS TRACKING**: Record bug fixes to `neo4j-memory`
6. **CONTEXT SAVE**: Persist debugging solutions to `neo4j-memory`

**WHY CRITICAL FOR DEBUGGING:**
- grep shows you how OTHERS solved the same error
- context7 ensures you understand the CORRECT API usage
- neo4j-memory preserves bug fixes for future reference

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Debugging without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving solutions to neo4j-memory

""",
    "typecheck": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL typechecking work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  typecheck  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR TYPECHECKING)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous type annotations
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for typing patterns BEFORE typechecking
   - context7: Latest Python typing standards (mypy, Pydantic)
   - grep: Real-world type annotation examples
3. **PLANNING**: Use `sequential-thinking` to plan type improvements
4. **TYPECHECKING**: Add/fix type annotations
5. **PROGRESS TRACKING**: Record typing decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist typing patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Typechecking without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving to neo4j-memory

""",
    "validation": """
##  CRITICAL: MCP Tools Workflow - MANDATORY

**ALL validation work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs)  grep (examples)  neo4j-memory (record)  validate  neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED FOR VALIDATION)
1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous validation standards
2. ** MANDATORY RESEARCH**: Use `context7` + `grep` for validation patterns BEFORE validating
   - context7: Latest validation standards and tools
   - grep: Real-world validation implementations
3. **PLANNING**: Use `sequential-thinking` to structure validation
4. **VALIDATION**: Perform comprehensive validation
5. **PROGRESS TRACKING**: Record validation results to `neo4j-memory`
6. **CONTEXT SAVE**: Persist validation patterns to `neo4j-memory`

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md`

**ABSOLUTELY FORBIDDEN:**
-  Validating without context7 + grep research
-  Skipping neo4j-memory context load
-  Completing without saving to neo4j-memory

""",
}

# Skills to update with their types
SKILLS_TO_UPDATE = {
    "fastapi-planning": "planning",
    "fastmcp-planning": "planning",
    "python-refactor": "refactor",
    "fastapi-refactor": "refactor",
    "fastmcp-refactor": "refactor",
    "python-quality-review": "quality-review",
    "fastapi-quality-review": "quality-review",
    "fastmcp-quality-review": "quality-review",
    "python-typecheck": "typecheck",
    "quality-validation": "validation",
    "quality-security": "validation",
    "code-debug": "debug",
    "code-remediation": "debug",
}


def update_skill(skill_path: Path, template_type: str) -> bool:
    """Update a skill file with MCP workflow section."""
    try:
        content = skill_path.read_text(encoding="utf-8")

        # Find the Safety line
        safety_pattern = r"(\*\*Safety:\*\*[^\n]+)\n\n## "

        # Check if already has MCP workflow
        if " CRITICAL: MCP Tools Workflow" in content:
            print(f"  [OK] {skill_path.parent.name} already has MCP workflow")
            return True

        # Insert MCP workflow after Safety line
        template = MCP_TEMPLATES[template_type]
        replacement = r"\1\n" + template + "\n## "

        new_content = re.sub(safety_pattern, replacement, content)

        if new_content != content:
            skill_path.write_text(new_content, encoding="utf-8")
            print(f"  [OK] Updated {skill_path.parent.name}")
            return True
        print(f"  [FAIL] Could not find insertion point in {skill_path.parent.name}")
        return False

    except Exception as e:
        print(f"  [FAIL] Error updating {skill_path.parent.name}: {e}")
        return False


def main():
    """Update all skills with MCP workflow requirements."""
    skills_dir = Path(__file__).parent

    print("=" * 70)
    print("BATCH UPDATE: Adding CRITICAL MCP Workflow to ALL Skills")
    print("=" * 70)

    updated = 0
    failed = 0

    for skill_name, template_type in SKILLS_TO_UPDATE.items():
        skill_file = skills_dir / skill_name / "SKILL.md"

        if not skill_file.exists():
            print(f"  [FAIL] {skill_name} - File not found")
            failed += 1
            continue

        if update_skill(skill_file, template_type):
            updated += 1
        else:
            failed += 1

    print()
    print("=" * 70)
    print(f"COMPLETE: {updated} skills updated, {failed} failed")
    print("=" * 70)
    print()
    print("MCP Tools workflow is now MANDATORY and CRITICAL across:")
    print(f"  - {updated} skills successfully updated")
    print("  - ALL Python/FastAPI/FastMCP development skills")
    print("  - Design, Planning, Implementation, Refactor, Quality, Debug skills")
    print()
    print("THE GOLDEN RULE is now enforced everywhere:")
    print("  context7 -> grep -> neo4j-memory -> code -> neo4j-memory")
    print()


if __name__ == "__main__":
    main()
