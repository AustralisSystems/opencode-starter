# CONCURRENT_DEVELOPMENT_ENVIRONMENT_DIRECTIVES

```yaml
CONCURRENT_DEVELOPMENT_ENVIRONMENT_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true
  intent: >
    This codebase operates in a parallel multi-agent, multi-developer environment.
    Multiple LLM instances, human developers, and automated pipelines work on the
    same directory structures simultaneously — without worktrees or branch isolation.
    This is intentional and by design. Agents MUST NOT treat concurrent activity
    as an error condition requiring investigation, remediation, or halting.

  shared_workspace_operating_model:
    participants:
      - "Other LLM agent instances (Antigravity, Codex, Gemini, Sonnet, Haiku, Qwen, etc.)"
      - "Human developers committing and editing files directly"
      - "Automated ACE pipeline runs (quality gates, lint, format, analysis, remediation)"
      - "Scripted background tasks (CI/CD hooks, watchdogs, scaffolding, orchestration scripts)"
    coordination_model: "No worktrees or isolated branches. Shared directory structure. Intentional."

  concurrent_change_nonblocking_policy:
    enforcement: MANDATORY
    rule: >
      Observing file changes, new files, modified timestamps, or artifacts that the agent
      did not create is expected and normal. Agents MUST NOT halt, abort, or pause their
      task because of unrelated concurrent changes in the codebase.
    YOU_MUST_NOT:
      - "Halt or abort a task because unrelated files were changed by another agent, human, or automation."
      - "Treat concurrent modifications as errors, conflicts, or anomalies requiring investigation."
      - "Undo, overwrite, revert, or remediate concurrent changes unless they directly and negatively impact the current assigned task."
    decision_rule: "If a concurrent change does not block, break, or contradict your current task instructions — ignore it and continue."

  live_file_reread_policy:
    enforcement: MANDATORY
    rule: >
      Because other agents or automation may have modified a file since it was last read,
      agents MUST re-read the physical file from disk immediately before modifying it.
    YOU_MUST:
      - "Re-read the physical file contents from disk immediately before modifying any file."
      - "Never assume the in-context (cached) version of a file reflects its current on-disk state."
      - "After re-reading, apply only the minimal targeted change required by the current task scope."

  task_scope_boundary_policy:
    enforcement: MANDATORY
    rule: >
      Agents MUST strictly confine all reads, writes, and changes to the scope of their
      current instruction. Unsolicited fixes, clean-ups, or scope extensions are FORBIDDEN.
    YOU_MUST_NOT:
      - "Modify files outside the assigned task scope, even if issues are observed in them."
      - "Perform unsolicited clean-up or fixes on unrelated code encountered during a task."
      - "Extend task scope based on adjacent findings unless explicitly instructed to do so."
    YOU_MAY:
      - "Note an out-of-scope issue in your response — but MUST NOT act on it."

  GATE_CDE_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - CONCURRENT_DEVELOPMENT_ENVIRONMENT_DIRECTIVES
      - "I MUST NOT halt or abort my task because I observe concurrent file changes made by other agents, humans, or automation."
      - "Concurrent activity by other LLMs, AI agents, human developers, and automated scripts is by design — I MUST treat it as normal and ignore it unless it directly and negatively impacts my current task."
      - "I MUST re-read any file from disk immediately before modifying it — I MUST NOT assume my in-context version is current."
      - "I MUST strictly confine all changes to my assigned task scope — I MUST NOT modify, revert, or investigate files outside my instruction scope."
    THEN: CONTINUE

## Code Implementation Directives

```
