# CODE_IMPLEMENTATION_DIRECTIVES

```yaml
CODE_IMPLEMENTATION_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true
  intent: "Define mandatory production-implementation remediation, completeness, and blocking-gate reporting requirements."

  blocking_gate_reporting_policy: "Agents MUST report failures using gate_id and MUST halt on any blocking gate."

  incomplete_implementation_remediation_policy:
    enforcement: MANDATORY
    gate_id: incomplete_implementation_remediation_policy
    requires_immediate_action: true
    blocking: true

    full_remediation_definition: >
      “Full remediation” means implementing the missing/placeholder behavior to production standard.
      Merely deleting or rewording markers (e.g., removing the string “TODO”) without implementing
      the required logic, validation, and tests is NON-COMPLIANT.

    remediation_trigger_categories:
      - TODOs (ALL must be found and replaced with production code)
      - Mocks (ALL must be found and replaced with real implementation)
      - Stubs (ALL must be found and fully implemented)
      - '"PASS" passes (ALL must be found and replaced with real validation AND logging)'
      - Hacks (ALL must be found and replaced with proper solutions)
      - Notes that code needs to be implemented (ALL must be found and implemented)
      - Shims (ALL must be found, removed and the code replaced or updated to use the proper solutions)
      - Placeholder code (ALL must be found and replaced with production code)
      - Demo/test data in production paths (ALL must be found and replaced with real data retrieval)
      - Partial implementations (ALL must be found and completed)
      - Workarounds or temporary solutions (ALL must be found and replaced with proper solutions)

  production_implementation_requirements:
    enforcement: MANDATORY
    gate_id: production_implementation_requirements
    requires_immediate_action: true
    blocking: true

    baseline_requirements:
      - Production code MUST be implemented 100% correctly
      - Production code MUST meet the highest enterprise standards
      - Production code MUST have 0 errors
      - Production code MUST have 0 warnings
      - Production code MUST have 0 issues
      - Production code MUST be fully functional, not partial
      - Production code MUST NOT skip any required functionality
      - Production code MUST NOT use workarounds or temporary solutions
      - Production code MUST be production-ready, not development/test code
      - Production code MUST be dynamic, modular, extensible, resilient, and idempotent where applicable in accordance with SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES

    hard_coded_value_and_logic_restrictions:
      rule: "Production Code MUST NOT contain fixed hard-coded operational values or hard-coded runtime logic when those values or decisions should come from authoritative runtime inputs."
      forbidden_hard_coded_artifacts:
        - settings
        - props
        - property values
        - keys
        - constants
        - variables
        - configs
        - defaults
        - thresholds
        - feature flags
        - mappings
        - decision tables
        - branching logic
        - business rules
        - connection strings
        - connection uris
        - credentials
        - secrets
        - inputs

    dynamic_runtime_input_requirements:
      - Operational values, props, keys, constants, defaults, mappings, thresholds, and behavioral inputs in production code MUST be sourced from authoritative runtime inputs such as databases, config files, data files, validated runtime inputs, service responses, or other documented runtime sources.
      - Hard-coded logic that controls runtime behavior MUST be rewritten to evaluate authoritative runtime inputs unless the SPEC_DOC explicitly requires fixed behavior.
      - When a fixed literal is mandated by a protocol, language requirement, or SPEC_DOC, that literal MUST remain narrowly scoped to the documented requirement and MUST NOT be generalized into broader runtime logic.

    credential_and_connection_handling_requirements:
      - All default credentials MUST be set, stored and read from the .env files
      - All credentials, secrets, connection string or connection uris in the Production Code:
          - MUST be encrypted and persisted in the "settings" or "config" database(s)
          - MUST ALWAYS be persisted and read at runtime from the "settings" or "config" database(s)
          - SHOULD use .env files to set and store default credentials or connection uris and connection strings

    configuration_and_input_handling_requirements:
      - All settings, variables, constants, configs or inputs in the Production Code:
          - MUST ALWAYS use yaml and/or json files to set and store default settings, variables, constants, configs or inputs
          - MUST ALWAYS be stored in "settings" or "config" database(s)
          - MUST ALWAYS be persisted and read at runtime from the "settings" or "config" database(s)
          - MAY use environment variables to set and store default settings, variables, constants, configs or inputs
      - Runtime behavior inputs, business rules, mappings, and decision-driving data MUST be loaded from authoritative data sources instead of being embedded as fixed production logic unless the SPEC_DOC explicitly requires a fixed implementation.

  remediation_workflow_enforcement_policy:
    enforcement: MANDATORY
    gate_id: remediation_workflow_enforcement_policy
    requires_immediate_action: true
    blocking: true

    execution_stop_conditions:
      - Finding incomplete code = STOP current work immediately
      - Fully remediate incomplete code = MANDATORY, cannot proceed until complete
      - Implement production code = MANDATORY, cannot skip or defer
      - Verify implementation = MANDATORY, must achieve 0 errors, 0 warnings, 0 issues
      - Violations = BLOCKING ISSUE - execution MUST STOP until fixed

  implementation_completeness_policy:
    enforcement: MANDATORY
    gate_id: implementation_completeness_policy
    requires_immediate_action: true
    blocking: true

    completion_verification_questions:
      - Are there any remaining activities or tasks that require attention?
      - Has the production code been fully implemented to meet the standards of enterprise-class production quality with no future or planned tasks, items, or activities?
    completion_requirements:
      - If pending items exist, responsibilities are considered unfulfilled and work MUST continue until resolved.
      - Production codebase under /src MUST consist of a complete and fully implemented version of all modules, features, functions, utilities and content.
      - SPEC documents MUST be revised to reflect findings when incompleteness is discovered, and the treatment plan MUST be defined.

  section_default_requires_immediate_action: true

  GATE_CID_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - CODE_IMPLEMENTATION_DIRECTIVES
      - "I MUST immediately STOP and fully remediate any TODOs, mocks, stubs, shims, or placeholder code before proceeding."
      - "I MUST implement production code 100% correctly with 0 errors, 0 warnings, and 0 issues."
      - "I MUST NOT hard-code settings, props, keys, constants, credentials, secrets, connection strings, inputs, or runtime decision logic in production code when they should come from authoritative runtime inputs."
      - "I MUST rewrite hard-coded operational logic so production behavior is driven by databases, config files, data files, validated runtime inputs, service responses, or other documented runtime sources unless the SPEC_DOC explicitly requires a fixed literal."
      - "I MUST NOT skip or defer required functionality; all code MUST be production-ready and not partial."
    THEN: CONTINUE

# ------------------------------------------------------------
## Code Specification Documents Catalog Directives

```
