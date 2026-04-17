# AGENTIC_CODE_ENGINE_USAGE_DIRECTIVES

```yaml
AGENTIC_CODE_ENGINE_USAGE_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true
  intent: "Define mandatory ACE usage, documentation discovery, reference-library usage, and CLI execution behavior for the session."

  documentation_reference_registry:
    documentation_root_directory: "{{AGENTIC_CODE_ENGINE_DIR}}/docs"
    repository_readme_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/README.md"
    architecture_docs_directory: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_Architecture_v2/architecture_bluprints"
    ace_cli_readme_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_CLI_Docs/README.md"
    ace_cli_docs_directory: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_CLI_Docs"
    ace_tools_docs_directory: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_Tools_Docs"
    code_capability_readme_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/capabilities/code/README.md"

  reference_library_usage_policy:
    intent: "Provide an authoritative reference library for scaffolding, reusable code patterns, and deterministic implementation guidance."
    scope: "This library is authoritative for reference implementations, reusable code patterns, and supporting documentation aligned with authoritative_architecture_documents, PYTHON_RUNTIME_AND_SOLUTION_SELECTION_DIRECTIVES, and SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES."
    authoritative_reference_library_paths:
      repository_root: "{{AGENTIC_CODE_ENGINE_DIR}}/_reference_lib"
      documentation_root: "{{AGENTIC_CODE_ENGINE_DIR}}/_reference_lib/docs"

    YOU_MUST:
      use_for_scaffolding_and_pattern_lookup: "Use {{reference_library_usage_policy.authoritative_reference_library_paths.repository_root}} for scaffolding and to locate reusable code examples and patterns."
      use_for_documentation_lookup: "Use {{reference_library_usage_policy.authoritative_reference_library_paths.documentation_root}} for documentation and implementation guidance."

  ace_cli_execution_policy:
    required_cli_behaviors:
      use_ace_cli_for_quality_validation_and_remediation: "Use ACE CLI commands for quality checks, validation, and remediation."
      use_ace_cli_namespaces_for_command_execution: "Use the ACE CLI command namespace for ACE command execution."
      understand_capability_specific_command_usage: "Understand the ACE CLI commands for any ACE capability or service before using them."

    ace_cli_usage_requirements:
      - All quality checks, validation, and remediation MUST be performed using ACE CLI commands.
      - Direct invocation of native tools for quality/security/compliance checks is strictly prohibited.
      - ACE CLI namespaces MUST be used for all production quality/security/compliance execution.

    execution_prerequisites:
      shell_environment_requirements:
        - Run ACE from a shell where the project environment is active.
        - If ace is not found, install project in editable mode.
      bootstrap_commands:
        - python -m pip install -e {{AGENTIC_CODE_ENGINE_DIR}}
      troubleshooting_steps:
        - Open a new terminal if PATH entry points are stale after installation.
        - Confirm python -m pip --version targets the active environment.

    command_reference:
      cli_executable_name: ace
      namespace_usage_rule: USE ONLY ACE CLI COMMANDS AND NAMESPACES.
      base_command_examples:
        - ace --help
        - ace info
        - ace list
        - ace pipeline run <config> <target>
        - ace <capability_name> <target> -- <native tool options>

  GATE_000:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - AGENTIC_CODE_ENGINE_USAGE_DIRECTIVES
      - "I MUST use ACE CLI commands for all quality checks, validation, and remediation."
      - "I MUST NOT invoke native tools directly for quality/security/compliance checks."
      - "I MUST use ACE CLI namespaces for all production quality/security/compliance execution."
      - "I MUST read relevant README files before using any ACE capability or service."
    THEN: CONTINUE

# ------------------------------------------------------------
## Quality Gate and Remediation Policy Directives

```
