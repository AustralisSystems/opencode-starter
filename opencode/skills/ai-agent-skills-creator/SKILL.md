---
name: ai-agent-skills-creator
description: Create, review, refactor, and update AI agent skill packages (SKILL.md plus references/scripts/assets) using cross-vendor best practices, trigger-focused metadata, safety controls, evaluation discipline, and packaging hygiene. Use when building new skills or modernizing existing skills.
---

# AI Agent Skills Creator

## Goal
Create and maintain production-grade AI agent skills that are reliable, safe, and easy to evolve.

## Use This Skill When
- Creating a new skill from scratch.
- Reviewing an existing skill for quality, drift, or safety gaps.
- Updating a skill to align with current Anthropic/OpenAI/Google best practices.
- Hardening skill packaging and validation workflows.

## Role Boundary
- Engineer the skill package and its instructions.
- Do not execute the target business workflow unless the user explicitly asks for simulation/testing.

## Non-Goals
- Do not invent tools, runtime capabilities, or APIs.
- Do not silently remove constraints or safeguards.
- Do not make broad rewrites that hide semantic diffs unless requested.
- Do not claim validation or tests that were not run.

## Core Principles
- Metadata drives invocation:
Put trigger context in `description` clearly and early.
- Progressive disclosure:
Keep `SKILL.md` focused; move details to `references/` and execution logic to `scripts/`.
- Deterministic structure:
Use explicit sections, stable ordering, and clear output contracts.
- Safety first:
Treat skill content as privileged instructions with potential side effects.
- Evidence over assumption:
When runtime behavior is uncertain, verify against current docs or local config.

## Standard Workflow
1. Intake and classify
- Identify request mode: create, review, or update.
- Identify runtime target: Anthropic-style, OpenAI hosted/local shell skills, or portable baseline.

2. Define intent and triggering
- Capture what the skill does.
- Capture exact trigger phrases and contexts.
- Define expected outputs and success criteria.

3. Design package layout
- Required: `SKILL.md`.
- Optional: `references/`, `scripts/`, `assets/`.
- Keep files minimal and purposeful.

4. Author or patch `SKILL.md`
- Write clear frontmatter.
- Keep instructions actionable and concise.
- Add explicit create/review/update flows when appropriate.

5. Add supporting files
- `references/`: deep guidance and schemas.
- `scripts/`: deterministic helpers/validators.
- `assets/`: templates and non-context resources.

6. Validate and harden
- Frontmatter parse and schema checks.
- Naming and trigger quality checks.
- Packaging safety checks.

7. Deliver
- Provide updated files.
- Provide findings and change summary.
- Provide follow-up recommendations.

## Frontmatter Policy
Portable minimum:
- `name`
- `description`

Use portable minimum when runtime is unknown.

Advanced fields may be used when runtime supports them, such as:
- Invocation controls (for example manual-only or hidden skills).
- Tool restrictions.
- Argument hints.
- Context mode and agent selection.
- Path scoping.

When using advanced fields:
- Prefer explicit compatibility notes.
- Avoid fields that are unsupported by the active runtime.

## Create Mode Contract
Always produce:
- `SKILL.md` with clear trigger metadata.
- A concise package structure recommendation.
- Optional starter files in `references/` and `scripts/` when warranted.

Output sections:
- `skill_summary`
- `package_layout`
- `skill_markdown`
- `validation_notes`
- `next_steps`

## Review Mode Contract
Report findings first, ordered by severity.

Severity:
- Critical: safety/policy risk, destructive behavior risk, invalid packaging, or severe invocation risk.
- High: trigger drift, schema/validator mismatch, missing safeguards, contradictory instructions.
- Medium: maintainability, clarity, and compatibility gaps.
- Low: style and polish issues.

For each finding include:
- Location
- Issue
- Impact
- Recommended fix

Output sections:
- `summary`
- `findings`
- `quality_scores`
- `recommended_patch`
- `regression_risks`

## Update Mode Rules
- Preserve intent and behavior unless change is requested.
- Keep diffs minimal and explain renamed/removed fields.
- Add migration notes for compatibility-impacting changes.
- Re-validate after edits.

Output sections:
- `updated_content`
- `change_summary`
- `compatibility_notes`
- `validation_results`

## Validation Checklist
- Frontmatter parses cleanly.
- `name` uses lowercase hyphen-case and is runtime-compliant.
- `description` clearly states what the skill does and when to use it.
- Instructions are explicit and non-contradictory.
- Safety boundaries and refusal/fallback behavior are clear where needed.
- Supporting files are referenced from `SKILL.md`.
- No unnecessary files are included.

## Packaging and Security Rules
- Exclude secrets and local artifacts from skill bundles (for example `.env`, caches, temporary outputs).
- Avoid packaging unrelated large files.
- Prefer deterministic scripts over repeated ad hoc prompt logic when behavior must be reliable.
- Require explicit user confirmation for high-impact write workflows.

## Anti-Patterns
- Vague descriptions that under-trigger or over-trigger indiscriminately.
- Monolithic `SKILL.md` with no supporting file strategy.
- Conflicting instructions across sections.
- Validator logic that rejects legitimate modern frontmatter without compatibility mode.
- Packaging everything recursively without exclusions.

## Acceptance Criteria
- Skill metadata is clear, actionable, and trigger-ready.
- Skill body is concise, structured, and operational.
- Validation and packaging guidance is explicit.
- Findings/changes are evidence-based and reproducible.
- Outputs are suitable for source control review.

## References
Use this local dossier as the baseline for this skill:
- `README.md`

Specialist sibling skills created for focused workflows:
- `../ai-agent-skill-frontmatter-modern-fields/SKILL.md`
- `../ai-agent-skill-safety-invocation-controls/SKILL.md`
- `../ai-agent-skill-evaluation-checklist/SKILL.md`
- `../ai-agent-skill-cross-vendor-compatibility/SKILL.md`

Primary external references used to shape this skill:
- Anthropic skills docs
- OpenAI skills, prompting, evals, and structured output docs
- Google Gemini prompting strategies docs
- Agent Skills open standard
