---
name: ENVIRONMENT
description: Handle shared-workspace and concurrent-development conditions safely in repositories where multiple agents, humans, and automation edit the same files. Use this skill whenever the task involves unexpected file changes, dirty worktrees, concurrent edits, scope-boundary decisions, or deciding whether to continue work in a non-isolated environment.
---

# ENVIRONMENT Skill

Use this skill to behave correctly in a shared repository where concurrent changes are expected.

## When to use

- The repository is being edited by multiple agents, humans, or automation at the same time.
- You notice unexpected file changes, new files, or timestamps that you did not create.
- You need to decide whether a concurrent change should block the current task.
- You are about to modify files in a workspace that may have changed since your last read.
- You need to stay strictly in scope while working around nearby unrelated problems.

## Core operating model

- Assume concurrent activity is normal by design.
- Do not treat unrelated file changes as a failure condition.
- Continue work unless the concurrent change directly blocks, breaks, or contradicts the current task.

## Required behavior

1. Re-read any file from disk immediately before modifying it.
2. Apply only the minimal targeted change required for the current task.
3. Ignore unrelated concurrent edits instead of investigating or remediating them.
4. Stay within the assigned scope even when nearby issues are visible.
5. Mention out-of-scope issues only as notes; do not fix them without instruction.

## Forbidden behavior

- Do not halt or abort work just because the workspace is changing.
- Do not treat concurrent modifications as anomalies that automatically require investigation.
- Do not revert, overwrite, or clean up another actor's changes unless they directly and negatively impact the current task.
- Do not expand scope into adjacent fixes.

## Decision rule

- If a concurrent change does not block, break, or contradict the current task instructions, ignore it and continue.
- If it does directly impact the task, account for it narrowly and still keep changes limited to the assigned objective.

## Source alignment

- This skill is derived from the `Concurrent Development Environment` section in `AGENTS.md`.
- It aligns with `GATE_CDE_001` and the repository's shared-workspace operating model.

## Example situations

**Example 1:**
Input: A file you are not touching changes during your task.
Output: Ignore the unrelated change and continue your scoped work.

**Example 2:**
Input: You are about to patch a file that may have changed since your last read.
Output: Re-read the file from disk, then apply the smallest necessary edit.

**Example 3:**
Input: You notice an unrelated bug in a nearby module while fixing the current task.
Output: Leave it unchanged and optionally note it as out of scope.
