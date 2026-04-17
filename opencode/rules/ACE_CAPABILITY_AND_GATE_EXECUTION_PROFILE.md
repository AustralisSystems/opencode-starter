# ACE_CAPABILITY_AND_GATE_EXECUTION_PROFILE

```yaml
ACE_CAPABILITY_AND_GATE_EXECUTION_PROFILE:
  enforcement: MANDATORY
  blocking: true
  intent: "Define the authoritative ACE gate execution sequence, AST/LibCST application policy, and remediation escalation model."

  minimum_required_gate_command_sequence:
    - ace pipeline run gate-a <target>
    - ace pipeline run gate-b <target>

  gate_execution_notes:
    - gate-a is mandatory after file-level modifications.
    - gate-a then gate-b is mandatory at task completion.
    - Direct native tool invocation is prohibited for gate execution.
    - ace ai_automation capability escalation is mandatory on deterministic non-convergence.

  ace_ast_and_libcst_application_policy:
    ast_engine_required_application_stages:
      - pre-remediation discovery for python source changes
      - architectural/static contract checks
      - post-remediation semantic validation
      - release-gate structural verification

    libcst_required_application_stages:
      - stage-local codemod/remediation for eligible adapters
      - mapped import rewrites and deterministic API migrations
      - stage remediation loops after stage findings

    combined_application_order:
      - AST and stage-tool rule targeting
      - Tool-native fix for eligible adapters in remediation mode
      - Stage-local LibCST codemod/refactor execution
      - Mandatory secondary validation rerun
      - ace ai_automation capability escalation on non-convergence and post-AI revalidation

  GATE_002:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - ACE_CAPABILITY_AND_GATE_EXECUTION_PROFILE
      - ace_ast_and_libcst_application_policy
      - "I MUST use ACE CLI commands for all gate executions."
      - "I MUST run the minimum required ACE gate command sequence for gate execution as defined in ACE_CAPABILITY_AND_GATE_EXECUTION_PROFILE."
      - "I MUST NOT invoke native tools directly for gate execution."
    THEN: CONTINUE

# ------------------------------------------------------------
## Session Operating Directives

```
