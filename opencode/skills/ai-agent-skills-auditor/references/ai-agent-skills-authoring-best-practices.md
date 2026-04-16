# AI Agent Skills Authoring Best Practices

Last updated: 2026-03-30
Owner skill: `ai-agent-skills-auditor`

## Purpose
This document is the authoritative baseline for auditing and updating in-scope AI agent skill packages.

## Canonical Sources
Refresh these before major audits:
- Anthropic Claude Code skills docs: https://code.claude.com/docs/en/skills
- Anthropic prompt engineering overview: https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/overview
- OpenAI skills guide: https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI evals guide: https://developers.openai.com/api/docs/guides/evals
- OpenAI structured outputs guide: https://developers.openai.com/api/docs/guides/structured-outputs
- OpenAI prompt engineering guide: https://developers.openai.com/api/docs/guides/prompt-engineering
- Google Gemini prompting strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
- Agent Skills standard overview: https://agentskills.io/

## Cross-Vendor Convergent Rules

### 1) Metadata and Triggering
- `name` and `description` are foundational and MUST be clear.
- Descriptions SHOULD front-load trigger language and use-case keywords.
- `description` SHOULD be concise and specific (avoid broad, noisy trigger text).

### 2) Invocation and Control Boundaries
- Use explicit invocation controls for side-effecting skills.
- Restrict tool access where runtime supports it.
- Separate manual-only operational workflows from passive knowledge skills.

### 3) Progressive Disclosure
- Keep `SKILL.md` concise and operational.
- Move deep detail to `references/`.
- Keep deterministic reusable logic in `scripts/`.
- Keep non-context output resources in `assets/`.

### 4) Deterministic Output and Validation
- Prefer explicit output contracts for review and automation workflows.
- Use structured and machine-checkable formats when practical.
- Include refusal/fallback behavior for unsupported or unsafe requests.

### 5) Evaluation and Regression Discipline
- Define objective quality criteria.
- Maintain representative prompt/test sets for high-impact skills.
- Re-validate after every material change.

### 6) Safety and Risk Management
- Treat skill content as privileged instructions.
- Assume prompt-injection risk where external context enters workflows.
- Require explicit approval for high-impact writes or external side effects.

### 7) Versioning and Packaging Hygiene
- Keep skill packages minimal and intentional.
- Exclude secrets, local caches, logs, temporary files, and large unrelated artifacts.
- Track compatibility notes when using runtime-specific fields.

## In-Scope Skill Audit Checklist
Apply to every in-scope skill package.

### A. SKILL.md
- Frontmatter parses cleanly.
- Name is runtime-compliant and stable.
- Description states what and when, not just what.
- Instructions are actionable and non-contradictory.
- Output contract exists for non-trivial workflows.
- Safety boundaries are explicit where needed.

### B. references/
- Contains useful deep material, not duplicated fluff.
- Files are discoverable from SKILL.md.
- Guidance is current, coherent, and source-traceable.

### C. scripts/
- Scripts are purposeful, deterministic, and scoped.
- Script intent and usage are discoverable from SKILL.md.
- Scripts avoid unsafe defaults.

### D. assets/
- Assets directly support intended outputs.
- Asset usage is discoverable from SKILL.md.
- No unrelated or stale assets.

### E. Package Hygiene
- No secrets or credentials.
- No local machine artifacts or transient files.
- No oversized unrelated payloads.

## Severity Model
- Critical: safety/policy risk, destructive workflow risk, severe contradiction.
- High: broken activation, missing required controls, invalid package behavior.
- Medium: maintainability, weak evaluation discipline, partial documentation gaps.
- Low: polish and clarity improvements.

## Scoring Model (Optional)
Use 0-5 per dimension:
- Metadata and triggering
- Safety and invocation controls
- Workflow determinism and output contract
- Reference quality
- Script quality
- Asset quality
- Evaluation readiness
- Packaging hygiene

Overall score = average dimension score x 20 (0-100).

## Remediation Rules
- Close Critical and High findings in the same cycle unless explicitly deferred.
- Keep changes minimal and behavior-preserving unless a behavior change is required.
- Record source-backed rationale for compatibility-impacting edits.

## Research Refresh Policy
- Refresh source review before broad audits or every 30 days, whichever comes first.
- If source guidance conflicts, prefer:
1. Official runtime docs for active target environment.
2. Cross-vendor common denominator for portability.
3. Local policy constraints for repository compliance.

## Audit Run Deliverables
Each run SHOULD produce:
- Scope inventory.
- Source refresh notes and date.
- Severity-ranked findings.
- Applied changes and rationale.
- Post-fix validation summary.
- Residual risk and follow-up recommendations.
