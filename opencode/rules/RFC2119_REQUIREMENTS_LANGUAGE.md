# RFC2119_REQUIREMENTS_LANGUAGE

```yaml
RFC2119_REQUIREMENTS_LANGUAGE:
  enforcement: MANDATORY
  blocking: true
  source_protocol: "{{AGENTIC_CODE_ENGINE_DIR}}/_ai_agent/instructions/002/code/002_1000_protocols/006-PROTOCOL-RFC2119_Requirements_Language-v2.0.0.yaml"
  authoritative_scope: "This section governs interpretation of requirement language in this file and related repo instruction/protocol files."

  bcp14_keyword_definitions:
    MUST: "Absolute requirement (RFC 2119). Violations require immediate remediation; execution SHALL STOP."
    MUST_NOT: "Absolute prohibition (RFC 2119). Violations require immediate remediation; execution SHALL STOP."
    REQUIRED: "Equivalent to MUST. Use when a requirement is absolute and non-negotiable."
    SHALL: "Equivalent to MUST. Use when the specification defines mandatory behavior."
    SHALL_NOT: "Equivalent to MUST_NOT. Use when the specification defines an absolute prohibition."
    SHOULD: "Strong recommendation (RFC 2119). Deviations are permitted only with explicit justification."
    SHOULD_NOT: "Strong discouragement (RFC 2119). Use requires explicit justification."
    RECOMMENDED: "Equivalent to SHOULD. Use when a practice is strongly advised but not universally mandatory."
    NOT_RECOMMENDED: "Equivalent to SHOULD_NOT. Use when a practice is strongly discouraged but may be acceptable with explicit justification."
    MAY: "Truly optional (RFC 2119). Implementation choice permitted without compliance impact."
    OPTIONAL: "Equivalent to MAY. Use when inclusion is left to implementation choice."

  bcp14_applicability_statement:
    rule: 'The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.'

  repository_enforcement_labels:
    FORBIDDEN: "Hard MUST NOT with active enforcement: detect and prevent; if found, execution SHALL STOP and remediation is REQUIRED."
    PROHIBITED: "Active scanning required: locate, document, and eradicate all instances; verify zero remain before continuation."

  uppercase_keyword_rule:
    rule: "Per RFC 8174, key words have special meaning when ALL CAPS. In this repo, capitalized RFC terms and the labels FORBIDDEN/PROHIBITED are enforceable requirements."

  normative_document_conventions:
    - "In this file, list headers are normative: items under YOU_MUST are MUST-level; items under YOU_SHOULD are SHOULD-level."
    - "Agents MUST NOT weaken requirement levels by rewording (e.g., MUST -> should) without explicit owner approval."

  GATE_RFC_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - RFC2119_REQUIREMENTS_LANGUAGE
      - "I MUST interpret the BCP 14 keywords only when they appear in all capitals."
      - "I MUST interpret MUST as an absolute requirement; violations require immediate remediation and execution SHALL STOP."
      - "I MUST interpret MUST_NOT as an absolute prohibition; violations require immediate remediation and execution SHALL STOP."
      - "I MUST interpret REQUIRED and SHALL as equivalent to MUST, SHALL_NOT as equivalent to MUST_NOT, RECOMMENDED as equivalent to SHOULD, NOT_RECOMMENDED as equivalent to SHOULD_NOT, and OPTIONAL as equivalent to MAY."
      - "I MUST interpret FORBIDDEN as a hard MUST_NOT with active enforcement; if found, execution SHALL STOP."
      - "I MUST interpret PROHIBITED as a mandatory locate-and-eradicate label that requires zero remaining instances before continuation."
      - "I MUST NOT weaken requirement levels by rewording (e.g., MUST to should) without explicit owner approval."
    THEN: CONTINUE

## AiDSL — AI DOMAIN SPECIFIC LANGUAGE

```
