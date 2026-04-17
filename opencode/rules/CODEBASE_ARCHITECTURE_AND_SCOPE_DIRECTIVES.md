# CODEBASE_ARCHITECTURE_AND_SCOPE_DIRECTIVES

```yaml
CODEBASE_ARCHITECTURE_AND_SCOPE_DIRECTIVES:
  authoritative_codebase_paths:
    CODEBASE_DIR:
      windows: 'C:\github_development\projects\digital-angels-kit\agentic_code_engine'
    PRODUCTION_CODEBASE_DIR:
      windows: 'C:\github_development\projects\digital-angels-kit\agentic_code_engine'
      roots:
        - capabilities
        - core
        - config
        - scripts
        - storage
        - deployments
        - src
        - main.py
    AGENTIC_CODE_ENGINE_DIR:
      windows: 'C:\github_development\projects\digital-angels-kit\agentic_code_engine'

  path_scope_notes:
    - The placeholders {{PRODUCTION_CODEBASE_DIR}}, {{AGENTIC_CODE_ENGINE_DIR}}, and {{authoritative_architecture_documents}} refer to the values defined in this file.
    - PRODUCTION_CODEBASE_DIR.roots defines the production-authoritative in-scope roots for implementation and remediation.
    - Non-production areas (for example docs, tests, artifacts, .venv, build, logs, and backups) are out-of-scope unless explicitly requested.

  authoritative_architecture_documents:
    architecture_blueprint_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_Architecture_v2/architecture_bluprints/FSP_Reference_Architecture_Blueprint_v0.2.0.md"
    webapp_architecture_blueprint_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_Architecture_v2/architecture_bluprints/HTMX_Jinja2_Reference_Architecture_v0.1.0.md"
    approved_packages_sbom_reference: "{{AGENTIC_CODE_ENGINE_DIR}}/docs/ACE_Architecture_v2/architecture_bluprints/APPROVED_PACKAGES_SBOM.yaml"

  YOU_MUST:
    - rule: "Comply with architecture blueprint."
      requirements:
        - "All changes under authoritative_codebase_paths.PRODUCTION_CODEBASE_DIR MUST adhere to and comply with authoritative_architecture_documents."
    - rule: "Validate alignment for new artifacts."
      requirements:
        - "When introducing new modules, services, routers, or deployment artifacts, you MUST validate alignment with authoritative_architecture_documents before considering work complete."
    - rule: "Resolve conflicts in favor of blueprint."
      requirements:
        - "If a conflict exists between an ad-hoc pattern and authoritative_architecture_documents, you MUST follow authoritative_architecture_documents."
    - rule: "Comply with SBOM."
      requirements:
        - "All SOFTWARE PACKAGES and DEPENDENCIES MUST strictly adhere to and comply with authoritative_architecture_documents.approved_packages_sbom_reference."
    - rule: "Comply with Code Quality Toolkit."
      requirements:
        - "All code MUST strictly adhere to and comply with authoritative_architecture_documents.architecture_blueprint_reference."

  YOU_SHOULD:
    - rule: "Use the Agentic Code Engine."
      guidance:
        - "You SHOULD use the Agentic Code Engine {{AGENTIC_CODE_ENGINE_DIR}} capabilities to continuously validate architecture and enterprise production standards."
    - rule: "Keep decisions deterministic and traceable."
      guidance:
        - "You SHOULD keep architecture-related decisions deterministic and traceable to authoritative_architecture_documents."

  GATE_ARCH_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - CODEBASE_ARCHITECTURE_AND_SCOPE_DIRECTIVES
      - "I MUST ensure all changes under PRODUCTION_CODEBASE_DIR adhere to authoritative_architecture_documents."
      - "I MUST validate alignment with authoritative_architecture_documents before considering any new module, service, router, or deployment artifact complete."
      - "I MUST resolve any conflict between an ad-hoc pattern and authoritative_architecture_documents in favor of authoritative_architecture_documents."
      - "I MUST ensure all software packages and dependencies comply with approved_packages_sbom_reference."
    THEN: CONTINUE

## Python Runtime And Solution Selection Directives

```
