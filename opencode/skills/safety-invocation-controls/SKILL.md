---
name: ai-agent-skill-safety-invocation-controls
description: Define and harden AI agent skill invocation and safety controls, including auto/manual trigger strategy, permission boundaries, tool restrictions, and high-impact action safeguards.
---

# AI Agent Skill Safety Invocation Controls

## Goal
Make skill behavior safe, predictable, and governed by explicit invocation boundaries.

## Use This Skill When
- A skill triggers too often or not often enough.
- You need manual-only execution for risky workflows.
- You need tool-boundary enforcement.
- You are hardening skills that can perform write or high-impact actions.

## Safety Principles
- Treat skill instructions as privileged.
- Require explicit approval for sensitive actions.
- Minimize default capability exposure.
- Prefer deterministic and auditable behavior.

## Invocation Strategy
- Auto invocation:
  - Use for low-risk guidance and background conventions.
- Manual-only invocation:
  - Use for deployment, mutation-heavy tasks, or operations with blast radius.
- Hidden/background invocation:
  - Use only when user command discoverability is not desired and behavior remains safe.

## Control Checklist
- Trigger scope is explicit.
- Tool permissions are least-privilege.
- Write actions require explicit confirmation where applicable.
- Unsupported actions have clear refusal/redirection behavior.
- Behavior does not bypass policy constraints.

## Output Contract
Return:
- `invocation_policy`
- `safety_controls`
- `risk_notes`
- `recommended_changes`

## Anti-Patterns
- Open-ended auto invocation on destructive workflows.
- No approval gates for high-impact actions.
- Implicit tool access assumptions.
- Safety constraints that conflict with required mission behavior.
