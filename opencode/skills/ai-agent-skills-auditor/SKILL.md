---
name: ai-agent-skills-auditor
description: Perform deep research on current AI agent skill best practices, maintain an authoritative best-practices reference, then audit and update every in-scope skill package (SKILL.md plus references/scripts/assets) to close quality, safety, and capability gaps.
---

# AI Agent Skills Auditor

## Goal
Run a repeatable, evidence-backed audit and remediation workflow for skill packages.

## Use This Skill When
- You need to harden or modernize a portfolio of skill packages.
- You need to verify that in-scope skills align with current cross-vendor best practices.
- You need to identify and close metadata, safety, evaluation, and packaging gaps.
- You need one authoritative reference that drives continuous skill quality updates.

## Mandatory Artifacts
Maintain this file as the audit source of truth:
- `references/ai-agent-skills-authoring-best-practices.md`

Use this template for each audit run output:
- `assets/skill-audit-report-template.md`

Use this helper for deterministic portfolio scans:
- `scripts/audit_skill_packages.py`

## In-Scope Definition
Default in-scope roots:
- `_ai_agent/.agents/skills/`
- `.claude/skills/` (if present)

A folder is considered a skill package when it contains `SKILL.md` (case-insensitive).

For each in-scope skill package, audit and remediate:
- `SKILL.md`
- `references/` contents (if present)
- `scripts/` contents (if present)
- `assets/` contents (if present)

## Required Workflow
1. Deep research first
- Refresh knowledge from current official sources before making changes.
- Prioritize: Anthropic Claude Code skills docs, OpenAI skills/evals/structured-output docs, Google Gemini prompting docs, and Agent Skills standard docs.
- Capture source URLs and update date in `references/ai-agent-skills-authoring-best-practices.md`.

2. Update the best-practices reference
- Reconcile findings into concrete rules and checklists.
- Keep rules implementation-oriented and testable.
- Remove or mark stale guidance.

3. Inventory in-scope skills
- Discover all in-scope skill packages.
- Record package paths and scope boundaries.

4. Audit each skill package comprehensively
- Validate metadata quality and trigger clarity.
- Validate invocation controls and safety boundaries.
- Validate workflow clarity, determinism, and output contracts.
- Validate references/scripts/assets usefulness, consistency, and completeness.
- Validate packaging hygiene and absence of risky artifacts.

5. Report findings by severity
Severity levels:
- Critical: safety or policy violation, destructive workflow risk, or severe instruction conflict.
- High: broken triggering, missing required controls, invalid structure, or major behavior ambiguity.
- Medium: maintainability gaps, weak evaluation guidance, incomplete supporting files.
- Low: style and clarity improvements.

6. Remediate and close gaps
- Patch in-scope skill packages directly where required.
- Add or update missing `references/`, `scripts/`, or `assets/` content when needed.
- Keep edits minimal, explicit, and behavior-preserving unless a change is required.

7. Validate after remediation
- Re-run deterministic checks with `scripts/audit_skill_packages.py`.
- Confirm critical/high findings are closed unless explicitly deferred.
- Document any accepted residual risk.

8. Deliver audit outputs
- Provide a severity-ordered findings list.
- Provide changed files and rationale.
- Provide final quality status per skill package.

## Audit Dimensions (Apply To Every In-Scope Skill)
- Metadata and triggering quality.
- Safety and invocation controls.
- Instruction quality and contradiction checks.
- Progressive disclosure and reference navigation quality.
- Script determinism and operational utility.
- Asset relevance and output support.
- Evaluation and regression readiness.
- Portability and cross-runtime compatibility notes.

## Output Contract
Return sections in this order:
1. `scope`
2. `research_updates`
3. `findings`
4. `remediation_changes`
5. `post_fix_validation`
6. `residual_risks`
7. `next_cycle_recommendations`

## Operating Rules
- Do not claim research, tests, or validations that were not performed.
- Do not invent runtime capabilities or unsupported frontmatter fields.
- Require explicit confirmation for high-impact actions.
- Keep evidence and recommendations traceable to sources.

## Quick Commands
Portfolio audit (report only):
```bash
python scripts/audit_skill_packages.py --skills-root _ai_agent/.agents/skills --output-dir _ai_agent/.agents/skills/ai-agent-skills-auditor/.reports
```

Portfolio audit with directory scaffolding fixes:
```bash
python scripts/audit_skill_packages.py --skills-root _ai_agent/.agents/skills --fix --output-dir _ai_agent/.agents/skills/ai-agent-skills-auditor/.reports
```

## References
- `references/ai-agent-skills-authoring-best-practices.md`
- `assets/skill-audit-report-template.md`
