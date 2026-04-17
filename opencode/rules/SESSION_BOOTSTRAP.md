# SESSION_BOOTSTRAP

```yaml
SESSION_BOOTSTRAP:
  enforcement: MANDATORY
  blocking: true
  intent: "Ensure agents explicitly load and commit to AGENTS.md and AGENTS.md.yaml before any task execution."

  INPUTS:
    STATIC:
      AUTHORITATIVE_DIRECTIVE_FILES:
        - ./AGENTS.md
        - ./AGENTS.md.yaml

  INSTRUCTIONS:
    READ_AND_UNDERSTAND:
      - "{{INPUTS.STATIC.AUTHORITATIVE_DIRECTIVE_FILES}}"
    UNDERSTAND_AND_ACKNOWLEDGE:
      - "{{INPUTS.STATIC.AUTHORITATIVE_DIRECTIVE_FILES}}"

  GATE_LOAD_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - SESSION_BOOTSTRAP
      - "I MUST read and understand the authoritative directive files, AGENTS.md and AGENTS.md.yaml, before proceeding with any task."
      - "I have read and understood the authoritative directives in AGENTS.md and AGENTS.md.yaml and will comply with them during this session."
      - "I MUST apply all directives, gates, and constraints defined in the authoritative directive files for the remainder of the session."
    THEN: CONTINUE

## Requirements language (RFC 2119 / RFC 8174)

```
