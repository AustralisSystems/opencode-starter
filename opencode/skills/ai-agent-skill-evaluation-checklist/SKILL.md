---
name: ai-agent-skill-evaluation-checklist
description: Create practical evaluation checklists for AI agent skills, including test prompts, measurable assertions, regression checks, and quality scoring for create/update cycles.
---

# AI Agent Skill Evaluation Checklist

## Goal
Ensure skills are verifiably correct, stable over time, and measurable during iteration.

## Use This Skill When
- Defining test coverage for a new skill.
- Adding regression checks after a skill update.
- Comparing baseline vs revised skill behavior.
- Requiring objective pass/fail criteria before rollout.

## Evaluation Framework
- Define representative test prompts.
- Specify expected outputs or observable outcomes.
- Add measurable assertions where objective validation is possible.
- Track regression risk between iterations.

## Minimum Checklist
- Trigger quality:
  - Skill activates when expected.
  - Skill does not over-trigger in unrelated contexts.
- Output quality:
  - Format is consistent with contract.
  - Critical constraints are honored.
- Safety quality:
  - Unsupported and risky requests are handled correctly.
- Compatibility quality:
  - Runtime-specific behavior is documented and validated.

## Scoring Dimensions
- clarity
- completeness
- correctness
- safety
- maintainability
- regression_resilience

## Output Contract
Return:
- `test_plan`
- `assertions`
- `quality_scores`
- `regression_findings`
- `recommendations`

## Anti-Patterns
- Subjective-only checks for objective requirements.
- No baseline comparison for major updates.
- Missing negative test cases.
- Declaring success without evidence.
