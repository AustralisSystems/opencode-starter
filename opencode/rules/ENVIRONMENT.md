# Environment

This rule captures the concurrent development environment requirements from `AGENTS.md`.

## When to apply

- Apply this rule in shared repositories where multiple agents, humans, and automation may change files concurrently.
- Apply it before reading, editing, or validating files in a non-isolated workspace.

## Environment model

- This codebase operates in a parallel multi-agent, multi-developer environment.
- Active participants may include:
  - Other LLM agent instances.
  - Human developers editing files directly.
  - Automated ACE pipeline runs.
  - Background scripts, hooks, and orchestration tasks.
- These participants do not coordinate through isolated worktrees or branches.
- Shared directory activity is intentional and expected.

## Concurrent activity policy

- File changes, new files, timestamp shifts, and generated artifacts created by other actors are normal.
- Do not halt, abort, or pause a task because unrelated concurrent changes are present.
- Do not treat concurrent modifications as errors or anomalies by default.
- Do not undo, overwrite, revert, or remediate another actor's changes unless they directly and negatively affect the current task.
- If a concurrent change does not block or contradict the current task, ignore it and continue.

## Read-before-modify policy

- Re-read the physical file contents from disk immediately before modifying any file.
- Do not assume a previously read in-context version is still current.
- After re-reading, make only the minimal targeted change required by the current task.

## Scope boundary policy

- Strictly confine reads, writes, and edits to the current assigned task scope.
- Do not modify files outside the task scope, even if unrelated issues are noticed.
- Do not perform unsolicited cleanup or adjacent fixes.
- Do not expand task scope based on nearby findings unless explicitly instructed.
- You may note an out-of-scope issue in your response, but you must not act on it.

## Gate acknowledgement

- This rule reflects `GATE_CDE_001` from `AGENTS.md.yaml` and the corresponding loader content in `AGENTS.md`.
- Treat these commitments as active when this rule applies:
  - Do not halt or abort because of concurrent file changes made by other agents, humans, or automation.
  - Treat concurrent activity as normal unless it directly and negatively impacts the current task.
  - Re-read any file from disk immediately before modifying it.
  - Stay strictly within the assigned task scope.

## Key principle

- Shared-workspace concurrency is part of the operating model, not a special-case failure condition.
