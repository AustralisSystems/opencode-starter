---
name: ai-agent-skill-cross-vendor-compatibility
description: Align AI agent skills across Anthropic, OpenAI, Google, and open skill standards by defining portable core fields, runtime-specific extensions, and migration-safe compatibility notes.
---

# AI Agent Skill Cross Vendor Compatibility

## Goal
Keep skills portable while preserving runtime-specific strengths safely.

## Use This Skill When
- Porting skills between agent runtimes.
- Updating skills that rely on vendor-specific fields or behavior.
- Defining compatibility notes for mixed-runtime environments.
- Preventing schema and behavior drift across platforms.

## Compatibility Model
- Portable core:
  - Keep universally safe baseline in frontmatter and instructions.
- Runtime extensions:
  - Add platform-specific controls only behind explicit compatibility notes.
- Migration safety:
  - Preserve behavior intent and document any breaking differences.

## Mapping Checklist
- Core fields are present and portable.
- Runtime-specific fields are annotated.
- Unsupported fields have fallback behavior.
- Trigger semantics remain equivalent after migration.
- Validation strategy covers each runtime target.

## Output Contract
Return:
- `portability_assessment`
- `runtime_matrix`
- `migration_notes`
- `fallback_rules`

## Anti-Patterns
- Assuming one runtime's advanced fields are universally supported.
- Silent semantic changes during migration.
- Missing fallback behavior for unsupported controls.
- No runtime matrix for multi-platform skills.
