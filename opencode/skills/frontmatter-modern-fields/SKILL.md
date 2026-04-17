---
name: ai-agent-skill-frontmatter-modern-fields
description: Design, validate, and modernize SKILL.md frontmatter for AI agent skills, including portable minimum fields and runtime-specific advanced fields with compatibility notes.
---

# AI Agent Skill Frontmatter Modern Fields

## Goal
Produce correct, trigger-effective, and runtime-compatible skill frontmatter.

## Use This Skill When
- Creating a new skill and defining frontmatter from scratch.
- Updating legacy skill metadata that only uses minimal fields.
- Normalizing frontmatter across multiple skills.
- Reviewing frontmatter for compatibility drift.

## Core Rules
- Always include portable minimum fields:
  - `name`
  - `description`
- Keep names lowercase hyphen-case.
- Keep descriptions explicit about what the skill does and when to use it.
- Prefer compatibility notes when using runtime-specific advanced fields.

## Advanced Field Policy
Use advanced fields only when runtime supports them. Common categories:
- Invocation controls.
- Tool restrictions.
- Argument hints.
- Context and agent selection.
- Path scoping.

When uncertain:
- Default to portable minimum.
- Add a short note documenting why advanced fields were omitted.

## Review Checklist
- Frontmatter parses cleanly.
- `name` is valid and stable.
- `description` is trigger-oriented and concise.
- Advanced fields are supported by the target runtime.
- No contradictory metadata.

## Output Contract
Return:
- `frontmatter_patch`
- `compatibility_notes`
- `validation_summary`

## Anti-Patterns
- Vague descriptions with no trigger cues.
- Overloading frontmatter with unsupported fields.
- Silent field removals without migration notes.
- Inconsistent naming conventions across skills.
