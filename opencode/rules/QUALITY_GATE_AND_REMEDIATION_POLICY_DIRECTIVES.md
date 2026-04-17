# QUALITY_GATE_AND_REMEDIATION_POLICY_DIRECTIVES

```yaml
QUALITY_GATE_AND_REMEDIATION_POLICY_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true
  intent: "Enforce mandatory quality gate execution, remediation behavior, and completion criteria for all in-scope production artifacts."
  authoritative_scope: "This mandate is authoritative for in-scope production artifacts and defines target-state gate behavior."

  YOU_MUST:
    - Achieve 0 errors, 0 warnings, and 0 issues across the in-scope codebase AND production artifacts before completion.
    - Apply this mandate to Python modules/scripts, Jinja2 templates, HTML, and related production assets.
    - After each file change, run ace pipeline run gate-a <scope> before moving to next file.
    - At end of each task, run ace pipeline run gate-a <scope> then ace pipeline run gate-b <scope>.
    - Treat failed gates as blocking and re-run until clean.
    - Use remediation mode by default; scan-only and dry-run are opt-in.
    - Use stage-local findings and deterministic convergence criteria.
    - Escalate non-convergence to ai_automation and perform post-AI revalidation.
    - Run ripgrep and semgrep in applicable quality gate executions.
    - Remediate findings; do not mask with broad ignores or suppressions.
    - Remediate sequentially and revalidate after each fix.

  FORBIDDEN:
    - Running native quality/security tools directly outside ACE CLI orchestration.
    - Using non-ACE namespaces for production quality/security/compliance execution.
    - Skipping mandatory gate-a per-file and gate-a/gate-b task-end sequence.

  GATE_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - QUALITY_GATE_AND_REMEDIATION_POLICY_DIRECTIVES
      - "I MUST achieve 0 errors, 0 warnings, and 0 issues across the in-scope codebase AND production artifacts."
      - "I MUST run `ace pipeline run gate-a <scope>` followed by `ace pipeline run gate-b <scope>` at the end of each task."
    THEN: CONTINUE

# ------------------------------------------------------------
## Skill Discovery and Execution Directives

```
