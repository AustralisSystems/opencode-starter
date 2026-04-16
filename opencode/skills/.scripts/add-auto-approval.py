#!/usr/bin/env python3
"""
Add auto-approval capability to all custom skills
"""

from pathlib import Path

# Skill configuration: (skill_name, gates, safety_level, safety_note)
SKILL_CONFIGS = {
    # Python skills
    "python-design": (
        [1],
        "safe",
        "Design phase is safe for auto-approval (read-only analysis/planning)",
    ),
    "python-planning": (
        [1],
        "safe",
        "Planning phase is safe for auto-approval (read-only task breakdown)",
    ),
    "python-implement": (
        [1, 2],
        "caution",
        "CAUTION: Writes code. Recommend auto-approve Gate 1, review Gate 2",
    ),
    "python-quality-review": (
        [],
        "safe",
        "Quality review is safe for auto-approval (read-only validation)",
    ),
    "python-refactor": (
        [],
        "caution",
        "CAUTION: Modifies code. Review changes before accepting",
    ),
    "python-typecheck": (
        [],
        "safe",
        "Type checking is safe for auto-approval (validation only)",
    ),
    # FastAPI skills
    "fastapi-design": (
        [1],
        "safe",
        "Design phase is safe for auto-approval (read-only analysis/planning)",
    ),
    "fastapi-planning": (
        [1],
        "safe",
        "Planning phase is safe for auto-approval (read-only task breakdown)",
    ),
    "fastapi-implement": (
        [1, 2],
        "caution",
        "CAUTION: Writes code. Recommend auto-approve Gate 1, review Gate 2",
    ),
    "fastapi-quality-review": (
        [],
        "safe",
        "Quality review is safe for auto-approval (read-only validation)",
    ),
    "fastapi-refactor": (
        [],
        "caution",
        "CAUTION: Modifies code. Review changes before accepting",
    ),
    # FastMCP skills
    "fastmcp-design": (
        [1],
        "safe",
        "Design phase is safe for auto-approval (read-only analysis/planning)",
    ),
    "fastmcp-planning": (
        [1],
        "safe",
        "Planning phase is safe for auto-approval (read-only task breakdown)",
    ),
    "fastmcp-implement": (
        [1, 2],
        "caution",
        "CAUTION: Writes MCP server code. Recommend auto-approve Gate 1, review Gate 2",
    ),
    "fastmcp-quality-review": (
        [],
        "safe",
        "Quality review is safe for auto-approval (read-only validation)",
    ),
    "fastmcp-refactor": (
        [],
        "caution",
        "CAUTION: Modifies code. Review changes before accepting",
    ),
    # Quality/Testing skills
    "quality-validation": (
        [],
        "safe",
        "Validation is safe for auto-approval (read-only analysis)",
    ),
    "quality-security": (
        [],
        "safe",
        "Security analysis is safe for auto-approval (read-only scanning)",
    ),
    "test-implementation": (
        [1, 2],
        "caution",
        "CAUTION: Creates tests. Review test coverage and quality",
    ),
    "code-remediation": (
        [],
        "caution",
        "CAUTION: Fixes code issues. Review fixes before accepting",
    ),
    "code-debug": (
        [],
        "caution",
        "CAUTION: May modify code. Review proposed solutions",
    ),
}

AUTO_APPROVAL_SECTION_TEMPLATE = """
## Auto-Approval Mode

**Enable auto-approval by adding any of these phrases:**
- "with auto-approval"
- "auto-approve"
- "skip approval gates"
- "autonomous mode"
{gate_specific}

**Examples:**
{examples}

**What happens:**
- I execute all steps without pausing{gate_list}
- I make decisions autonomously based on best practices
- I proceed directly to deliverables
- State is still saved for review/rollback

**Safety:** {safety_note}
"""


def get_metadata_block(gates, safety_level):
    """Generate metadata YAML block"""
    safe_bool = "true" if safety_level == "safe" else "false"
    gates_str = str(gates) if gates else "[]"

    return f"""metadata:
  auto_approval_supported: true
  auto_approval_gates: {gates_str}
  safe_for_auto_approval: {safe_bool}"""


def get_auto_approval_section(skill_name, gates, safety_level, safety_note):
    """Generate auto-approval section"""
    # Gate-specific text
    if gates:
        gate_list_str = f" at Gate{' & Gate '.join(map(str, gates)) if len(gates) > 1 else f' {gates[0]}'}"
        gate_specific = "\n".join([f'- "auto-approve Gate {g}"' for g in gates])
    else:
        gate_list_str = ""
        gate_specific = ""

    # Example commands
    skill_display = skill_name.replace("-", " ").title()
    if "design" in skill_name:
        action = "Design a"
    elif "planning" in skill_name or "plan" in skill_name:
        action = "Plan"
    elif "implement" in skill_name:
        action = "Implement"
    elif "quality" in skill_name or "review" in skill_name:
        action = "Review"
    elif "refactor" in skill_name:
        action = "Refactor"
    elif "test" in skill_name:
        action = "Create tests for"
    elif "debug" in skill_name:
        action = "Debug"
    elif "remediation" in skill_name:
        action = "Fix issues in"
    elif "typecheck" in skill_name:
        action = "Type check"
    else:
        action = "Process"

    tech = skill_name.split("-")[0].upper() if skill_name.split("-")[0] in ["python", "fastapi", "fastmcp"] else "the"

    examples = f"""> "{action} {tech} authentication service with auto-approval"
> "{action} {tech} user management, auto-approve all gates" """

    return AUTO_APPROVAL_SECTION_TEMPLATE.format(
        gate_specific=gate_specific,
        gate_list=gate_list_str,
        examples=examples,
        safety_note=safety_note,
    )


def update_skill_file(skill_path, skill_name, gates, safety_level, safety_note):
    """Update a single skill file"""
    with open(skill_path, encoding="utf-8") as f:
        content = f.read()

    # Check if already updated
    if "metadata:" in content and "auto_approval_supported" in content:
        print(f"  SKIP {skill_name} - Already has auto-approval")
        return False

    # Add metadata to frontmatter
    lines = content.split("\n")
    frontmatter_end = None
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == "---":
            frontmatter_end = i
            break

    if frontmatter_end:
        # Insert metadata before closing ---
        metadata_block = get_metadata_block(gates, safety_level)
        lines.insert(frontmatter_end, metadata_block)

        # Find where to insert auto-approval section (after Auto-Activation Triggers)
        content_with_metadata = "\n".join(lines)

        # Insert auto-approval section
        trigger_section_end = content_with_metadata.find("## Execution")
        if trigger_section_end == -1:
            trigger_section_end = content_with_metadata.find("## Commands")
        if trigger_section_end == -1:
            trigger_section_end = content_with_metadata.find("## Output")

        if trigger_section_end != -1:
            auto_approval_section = get_auto_approval_section(skill_name, gates, safety_level, safety_note)
            new_content = (
                content_with_metadata[:trigger_section_end]
                + auto_approval_section
                + "\n"
                + content_with_metadata[trigger_section_end:]
            )

            with open(skill_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"  OK   {skill_name} - Updated with auto-approval")
            return True
        print(f"  WARN {skill_name} - Could not find insertion point")
        return False
    print(f"  ERR  {skill_name} - Could not find frontmatter")
    return False


def main():
    """Main execution"""
    skills_dir = Path(__file__).parent
    print(f"\nAdding auto-approval capability to skills in: {skills_dir}\n")

    updated_count = 0
    skipped_count = 0

    for skill_name, (gates, safety_level, safety_note) in SKILL_CONFIGS.items():
        skill_path = skills_dir / skill_name / "SKILL.md"

        if not skill_path.exists():
            print(f"  WARN {skill_name} - SKILL.md not found")
            continue

        if update_skill_file(skill_path, skill_name, gates, safety_level, safety_note):
            updated_count += 1
        else:
            skipped_count += 1

    print("\nSummary:")
    print(f"   Updated: {updated_count}")
    print(f"   Skipped: {skipped_count}")
    print(f"   Total:   {updated_count + skipped_count}")
    print("\nAuto-approval capability added!\n")
    print("See AUTO-APPROVAL-GUIDE.md for usage documentation\n")


if __name__ == "__main__":
    main()
