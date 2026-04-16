# AI Agent Skills Creator - Review and Research Dossier

Date: 2026-03-30
Scope: Review of the `skill-creator` skill package and research of updated best practices for skill/instruction authoring across Anthropic, OpenAI, Google, and GitHub ecosystem sources.

## 1. Executive Summary

This dossier captures:
- A code and content review of the current `skill-creator` package.
- High-confidence findings with severity and concrete evidence points.
- Current best-practice alignment research from official vendor docs and active cookbooks.
- Recommended updates to modernize local skill authoring, validation, packaging, and maintenance workflows.

Primary outcome:
- The current `skill-creator` package has strong foundational guidance, but contains validator and policy drift that now conflicts with updated platform capabilities and safety controls.

## 2. Artifacts Reviewed (Local)

Directory reviewed:
- `_ai_agent/.agents/skills/skill-creator`

Files reviewed directly:
- `_ai_agent/.agents/skills/skill-creator/SKILL.md`
- `_ai_agent/.agents/skills/skill-creator/references/output-patterns.md`
- `_ai_agent/.agents/skills/skill-creator/references/workflows.md`
- `_ai_agent/.agents/skills/skill-creator/scripts/init_skill.py`
- `_ai_agent/.agents/skills/skill-creator/scripts/package_skill.py`
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py`
- `_ai_agent/.agents/skills/skill-creator/LICENSE.txt`

## 3. Local Review Findings

### Finding A - Outdated frontmatter allowlist in validator
Severity: High

Evidence:
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py:42`
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py:45`

Observed behavior:
- Validator only permits a narrow set of frontmatter keys.
- Newer skill ecosystems now use additional frontmatter fields for invocation control, execution context, path scoping, and safety behavior.

Risk:
- Valid modern skills can fail local validation.
- Team may avoid using safer controls because local tooling rejects them.

### Finding B - Frontmatter parsing is brittle
Severity: High

Evidence:
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py:23`
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py:27`

Observed behavior:
- Parser assumes strict frontmatter placement and newline pattern.

Risk:
- Files with BOM/CRLF or common formatting variations may fail despite valid content.
- Creates avoidable friction in CI and packaging pipelines.

### Finding C - SKILL authoring policy drift in guidance text
Severity: Medium

Evidence:
- `_ai_agent/.agents/skills/skill-creator/SKILL.md:68`
- `_ai_agent/.agents/skills/skill-creator/SKILL.md:306`
- `_ai_agent/.agents/skills/skill-creator/SKILL.md:314`

Observed behavior:
- Guidance states only `name` and `description` should be used in frontmatter.

Risk:
- Direct conflict with updated capability fields in modern skill runtimes.
- Prevents authoring of intentionally manual-only skills and safer tool-bounded skills.

### Finding D - Name length policy inconsistency
Severity: Medium

Evidence:
- `_ai_agent/.agents/skills/skill-creator/scripts/init_skill.py:276`
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py` (name length check permits 64)

Observed behavior:
- Init script user guidance says max 40 chars.
- Validator uses max 64 chars.

Risk:
- User confusion and unnecessary naming constraints.

### Finding E - Packaging process has no content exclusion policy
Severity: Medium

Evidence:
- `_ai_agent/.agents/skills/skill-creator/scripts/package_skill.py:68`
- `_ai_agent/.agents/skills/skill-creator/scripts/package_skill.py:70`

Observed behavior:
- Packager recursively includes every file.

Risk:
- Could package unintended files (temporary outputs, caches, secrets, large artifacts).
- Increases distribution and security risk.

## 4. External Research Scope and Approach

Research objective:
- Identify updated best practices for reusable skill/instruction authoring and operationalization.

Vendors and source categories covered:
- Official documentation: Anthropic, OpenAI, Google
- Public ecosystem references: Agent Skills standard site
- Active GitHub cookbooks and repositories: OpenAI, Anthropic, Google

Topics emphasized:
- Skill structure and metadata
- Invocation controls and tool boundaries
- Validation and schema discipline
- Evaluation loops and regression testing
- Versioning and packaging
- Safety and operational governance

## 5. Research Synthesis by Vendor

### Anthropic (Claude Code Skills)

Key guidance identified:
- Skills are frontmatter plus markdown instructions, with optional supporting files.
- Description quality is critical for trigger behavior.
- Keep SKILL content concise and move heavy details to supporting docs.
- Expanded frontmatter supports invocation behavior, tool permissions, forked context, path scoping, argument handling, and shell configuration.

Notable implications:
- Local skill tooling should support a broader frontmatter model than legacy two-field assumptions.
- Skill docs should distinguish between automatic invocation and explicit/manual workflows.

### OpenAI (Skills + Prompting + Evals + Structured Outputs)

Key guidance identified:
- Skills are versioned bundles with upload, version pointers, and explicit limits.
- Skill safety model treats skill content as privileged instructions.
- Prompt engineering guidance emphasizes role hierarchy, structured prompts, examples, and context management.
- Evals guidance emphasizes iterative testing loops and objective criteria.
- Structured outputs guidance emphasizes schema discipline and strict machine-readable contracts.

Notable implications:
- Skill authoring should include explicit output contracts and evaluation pathways.
- Packaging and lifecycle tooling should support versioned workflows and safety checks.

### Google (Gemini prompt and agentic workflows)

Key guidance identified:
- High-value patterns: clear instructions, explicit constraints, fixed response format, and consistent examples.
- Strong recommendation for iterative refinement and decomposition for complex tasks.
- Agentic workflows benefit from explicit planning, validation, and robust control over output requirements.

Notable implications:
- Skill templates should embed decomposition and validation by default.
- Reference patterns should prefer deterministic format guarantees where possible.

### Agent Skills Open Standard

Key guidance identified:
- Skills as portable, reusable capability bundles for agent ecosystems.

Notable implications:
- Local implementation should remain interoperable and avoid unnecessary proprietary lock-in in core authoring conventions.

## 6. GitHub Ecosystem Signals

Active repositories reviewed:
- OpenAI Cookbook (`openai/openai-cookbook`)
- Anthropic Claude Cookbooks (`anthropics/claude-cookbooks`)
- Google Gemini Cookbook (`google-gemini/cookbook`)

Signal:
- All three ecosystems show active maintenance and rapid evolution.

Implication:
- Skill creation references should include periodic refresh rules to avoid stale guidance.

## 7. Consolidated Best Practices (Cross-Vendor)

1. Metadata and triggering
- Front-load trigger phrases in description.
- Keep description concise but specific.
- Treat metadata as operational configuration, not just labels.

2. Invocation and control boundaries
- Distinguish auto-triggered skills from manual-only workflows.
- Scope permissions and tool access explicitly.
- Use path/context scoping for targeted activation.

3. Structure and progressive disclosure
- Keep SKILL.md focused.
- Move deep references into `references/` and scripts into `scripts/`.
- Provide explicit navigation cues for when to load each reference file.

4. Deterministic output and safety
- Prefer structured output contracts for machine-readable workflows.
- Require refusal/fallback behavior for unsupported or unsafe requests.
- Avoid ambiguous terms without acceptance criteria.

5. Evaluation and iteration
- Build test prompts and objective checks early.
- Run regression-style checks after edits.
- Track prompt/skill performance over revisions.

6. Packaging and lifecycle
- Enforce safe packaging filters.
- Use versioning discipline and clear changelogs.
- Validate before packaging and distribution.

## 8. Gap Analysis - skill-creator vs Current Best Practice

Strengths already present:
- Strong progressive disclosure concept.
- Good emphasis on concise skill body and references.
- Helpful output and workflow patterns.

Gaps to address:
- Validator frontmatter model is too narrow.
- Parser robustness needs BOM/CRLF tolerance.
- Guidance text is inconsistent with modern frontmatter controls.
- Packaging requires explicit include/exclude policy.
- Naming constraints are inconsistent.

## 9. Recommended Update Plan (Actionable)

### Phase 1 - Correctness and compatibility
1. Expand frontmatter schema in validator.
2. Replace brittle frontmatter regex parsing with robust extraction.
3. Align name length policy to one canonical limit.

### Phase 2 - Safety and packaging hardening
1. Add packaging exclusion defaults.
2. Add optional package manifest allowlist.
3. Add size and file-count preflight checks for bundles.

### Phase 3 - Documentation refresh
1. Update SKILL.md policy from "only name/description" to "required + optional advanced fields".
2. Add explicit section on invocation control and safety.
3. Add cross-vendor compatibility note and update cadence.

### Phase 4 - Evaluation discipline
1. Add reusable eval checklist template for skills.
2. Add regression test recipe for trigger quality and output structure.

## 10. Proposed Additions to skill-creator References

Recommended new reference files:
- `references/frontmatter-modern-fields.md`
- `references/safety-and-invocation-controls.md`
- `references/skill-evaluation-checklist.md`
- `references/cross-vendor-compatibility-notes.md`

Recommended script enhancements:
- `scripts/quick_validate.py`: robust parser + expanded schema + strict/permissive modes
- `scripts/package_skill.py`: safe excludes + manifest support + preflight guardrails
- `scripts/init_skill.py`: synchronized naming rules and modern frontmatter template examples

## 11. Full Source References (Research)

### Anthropic
- https://code.claude.com/docs/en/skills

### OpenAI
- https://developers.openai.com/api/docs/guides/tools-skills
- https://developers.openai.com/api/docs/guides/prompt-engineering
- https://developers.openai.com/api/docs/guides/evals
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://developers.openai.com/api/docs/guides/production-best-practices

### Google
- https://ai.google.dev/gemini-api/docs/prompting-strategies

### Open Skill Standard
- https://agentskills.io/

### GitHub Repositories
- https://github.com/openai/openai-cookbook
- https://github.com/anthropics/claude-cookbooks
- https://github.com/google-gemini/cookbook

## 12. Local Evidence References

- `_ai_agent/.agents/skills/skill-creator/SKILL.md`
- `_ai_agent/.agents/skills/skill-creator/references/output-patterns.md`
- `_ai_agent/.agents/skills/skill-creator/references/workflows.md`
- `_ai_agent/.agents/skills/skill-creator/scripts/init_skill.py`
- `_ai_agent/.agents/skills/skill-creator/scripts/package_skill.py`
- `_ai_agent/.agents/skills/skill-creator/scripts/quick_validate.py`

## 13. Optional Next Step

If requested, this dossier can be converted into:
- A concrete patch plan with exact diffs for `skill-creator` files.
- A companion `SKILL.md` for this new `ai-agent-skills-author` directory.
- A minimal conformance test set to validate future updates.
