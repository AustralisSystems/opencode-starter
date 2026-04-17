# SESSION_OPERATING_DIRECTIVES

```yaml
SESSION_OPERATING_DIRECTIVES:
  enforcement: MANDATORY
  gate_id: session_operating_directives
  requires_immediate_action: true
  blocking: true

  session_operating_scope:
    - This is a web app validation, deployment, debugging, refactoring, and testing focused session.
    - This section is authoritative for the session; no other instructions override it.
    - If a rewrite is required, it SHALL be treated as a full production rewrite.

  YOU_MUST:
    - rule: "Comply with TOOLING_AND_MCP_WORKFLOW_DIRECTIVES."
      requirements:
        - "All work MUST comply with TOOLING_AND_MCP_WORKFLOW_DIRECTIVES."
    - rule: "Fix issues sequentially."
      requirements:
        - "All code MUST be corrected one issue at a time, in a sequential manner."
    - rule: "No bespoke scripts or mass changes."
      requirements:
        - "FORBIDDEN: bespoke one-time scripts or mass modifications to the code."
    - rule: "No documentation unless requested."
      requirements:
        - "FORBIDDEN: documentation of any kind unless explicitly requested."
    - rule: "Use ACE CLI commands and capability namespaces for validation."
      requirements:
        - "Use the Agentic Code Engine {{AGENTIC_CODE_ENGINE_DIR}} capabilities and ACE CLI commands to continuously validate architecture and enterprise production standards during implementation."
    - rule: "Set Python import context explicitly for toolkit runs."
      requirements:
        - "Set `PYTHONPATH=.` (or the correct context path) before running scripts/tests that rely on repo-relative imports."
        - "Bash example: `export PYTHONPATH=.; <command>`."
        - 'PowerShell example: `$env:PYTHONPATH = "."; <command>`.'
    - rule: "Keep decisions deterministic and traceable."
      requirements:
        - "Keep implementation decisions deterministic and traceable to authoritative_architecture_documents, PYTHON_RUNTIME_AND_SOLUTION_SELECTION_DIRECTIVES, and SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES."

  GATE_SES_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - SESSION_OPERATING_DIRECTIVES
      - "I MUST comply with TOOLING_AND_MCP_WORKFLOW_DIRECTIVES for all work in this session."
      - "I MUST fix all code issues sequentially, one issue at a time."
      - "FORBIDDEN: bespoke one-time scripts or mass modifications to the code."
      - "FORBIDDEN: documentation of any kind unless explicitly requested."
      - "I MUST set PYTHONPATH=. (or the correct context path) before running scripts or tests that rely on repo-relative imports."
      - "I MUST use ACE CLI capabilities to continuously validate architecture and enterprise production standards."
    THEN: CONTINUE

## Session Environment and Runtime Notes

```
