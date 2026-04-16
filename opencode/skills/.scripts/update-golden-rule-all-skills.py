#!/usr/bin/env python3
"""
Batch update script to correct THE GOLDEN RULE in all development skills.

THE GOLDEN RULE MUST include SOLID/DRY/KISS principles:
OLD: context7 (docs)  grep (examples)  neo4j-memory (record)  code  neo4j-memory (persist)
NEW: context7 (docs)  grep (examples)  neo4j-memory (record)  code (SOLID/DRY/KISS)  neo4j-memory (persist)

This is CRITICAL - SOLID/DRY/KISS are not optional, they are MANDATORY.
"""

from pathlib import Path

# Skills to update
SKILLS_TO_UPDATE = [
    # Design Skills
    "python-design",
    "fastapi-design",
    "fastmcp-design",
    # Planning Skills
    "python-planning",
    "fastapi-planning",
    "fastmcp-planning",
    # Implementation Skills
    "python-implement",
    "fastapi-implement",
    "fastmcp-implement",
    "test-implementation",
    # Refactor Skills
    "python-refactor",
    "fastapi-refactor",
    "fastmcp-refactor",
    # Quality Review Skills
    "python-quality-review",
    "fastapi-quality-review",
    "fastmcp-quality-review",
    # Utility Skills
    "python-typecheck",
    "quality-validation",
    "quality-security",
    "code-debug",
    "code-remediation",
]

# Replacement patterns
REPLACEMENTS = [
    (
        "context7 (docs)  grep (examples)  neo4j-memory (record)  code  neo4j-memory (persist)",
        "context7 (docs)  grep (examples)  neo4j-memory (record)  code (SOLID/DRY/KISS)  neo4j-memory (persist)",
    ),
    (
        "context7  grep  neo4j-memory  code  neo4j-memory",
        "context7  grep  neo4j-memory  code (SOLID/DRY/KISS)  neo4j-memory",
    ),
    (
        "│  4.  IMPLEMENTATION (filesystem + domain tools)          │",
        "│  4.  IMPLEMENTATION (filesystem + SOLID/DRY/KISS)        │",
    ),
    (
        "4. **IMPLEMENTATION**: Use `filesystem` to write code",
        "4. **IMPLEMENTATION**: Use `filesystem` to write code applying SOLID/DRY/KISS",
    ),
]

# Add forbidden practice if missing
FORBIDDEN_PRACTICE = """
7. ** Violating SOLID/DRY/KISS principles**
   - Consequence: Technical debt, unmaintainable code, repeated bugs, production failures
"""


def update_skill_file(skill_path: Path) -> tuple[bool, str]:
    """
    Update a single skill file with corrected Golden Rule.

    Returns:
        (success, message) tuple
    """
    try:
        # Read file
        with open(skill_path, encoding="utf-8") as f:
            content = f.read()

        original_content = content
        replacements_made = 0

        # Apply replacements
        for old_text, new_text in REPLACEMENTS:
            if old_text in content:
                content = content.replace(old_text, new_text)
                replacements_made += 1

        # Check if forbidden practices section needs update
        if "ABSOLUTELY FORBIDDEN" in content and "Violating SOLID/DRY/KISS" not in content:
            # Find the forbidden practices section and add new item
            if "6. ** Skipping sequential-thinking for complex tasks**" in content:
                insertion_point = content.find("6. ** Skipping sequential-thinking for complex tasks**")
                # Find end of item 6
                next_section_start = content.find("\n\n---", insertion_point)
                if next_section_start > insertion_point:
                    content = content[:next_section_start] + "\n" + FORBIDDEN_PRACTICE + content[next_section_start:]
                    replacements_made += 1

        # Write back if changes were made
        if content != original_content:
            with open(skill_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True, f"Updated with {replacements_made} changes"
        return True, "No changes needed (already correct)"

    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Main execution function."""
    print("=" * 80)
    print("GOLDEN RULE CORRECTION - Batch Update Script")
    print("=" * 80)
    print()
    print("CRITICAL UPDATE:")
    print("THE GOLDEN RULE must include SOLID/DRY/KISS principles")
    print()
    print("OLD: context7 -> grep -> neo4j-memory -> code -> neo4j-memory")
    print("NEW: context7 -> grep -> neo4j-memory -> code (SOLID/DRY/KISS) -> neo4j-memory")
    print()
    print("=" * 80)
    print()

    # Find skills directory
    script_dir = Path(__file__).parent
    skills_base = script_dir

    # Statistics
    total_skills = len(SKILLS_TO_UPDATE)
    updated_count = 0
    failed_count = 0
    no_change_count = 0

    print(f"Updating {total_skills} skills...")
    print()

    # Update each skill
    for skill_name in SKILLS_TO_UPDATE:
        skill_path = skills_base / skill_name / "SKILL.md"

        if not skill_path.exists():
            print(f"[SKIP] {skill_name:30s} - File not found")
            continue

        success, message = update_skill_file(skill_path)

        if success:
            if "No changes needed" in message:
                status = "[OK]"
                no_change_count += 1
            else:
                status = "[UPDATED]"
                updated_count += 1
        else:
            status = "[FAIL]"
            failed_count += 1

        print(f"{status:10s} {skill_name:30s} - {message}")

    # Summary
    print()
    print("=" * 80)
    print("UPDATE SUMMARY")
    print("=" * 80)
    print(f"Total skills processed: {total_skills}")
    print(f"Successfully updated:   {updated_count}")
    print(f"Already correct:        {no_change_count}")
    print(f"Failed:                 {failed_count}")
    print()

    if failed_count == 0:
        print("[SUCCESS] All skills have been updated with SOLID/DRY/KISS Golden Rule!")
    else:
        print(f"[WARNING] {failed_count} skills failed to update")

    print()
    print("CRITICAL REMINDER:")
    print("THE GOLDEN RULE now MANDATES SOLID/DRY/KISS principles during code phase")
    print()
    print("context7  grep  neo4j-memory  code (SOLID/DRY/KISS)  neo4j-memory")
    print()
    print("These principles are NON-NEGOTIABLE for ALL development work.")
    print("=" * 80)


if __name__ == "__main__":
    main()
