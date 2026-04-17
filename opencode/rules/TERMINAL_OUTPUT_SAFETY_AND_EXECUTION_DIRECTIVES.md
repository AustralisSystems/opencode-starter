# TERMINAL_OUTPUT_SAFETY_AND_EXECUTION_DIRECTIVES

```yaml
TERMINAL_OUTPUT_SAFETY_AND_EXECUTION_DIRECTIVES:
  enforcement: MANDATORY
  gate_id: terminal_output_safety_and_execution_directives
  requires_immediate_action: true
  blocking: true
  intent: "Prevent IDE terminal hangs and encoding crashes during command execution (Windows-focused)."

  execution_safety_summary: >
    To prevent IDE terminals/consoles from locking up when executing commands (especially when tools crash with heavy tracebacks
    or when output encoding is misconfigured), agents MUST follow these directives.

  YOU_MUST:
    - rule: "Redirect command output to a file."
      requirements:
        - "Redirect stdout and stderr to a text file for commands likely to produce large output or tracebacks."
        - "Bash example: append ` > /tmp/out_$(date +%Y%m%d%H%M%S)_<short_summary>.txt 2>&1`."
        - "Use `read_file` to review captured output."
    - rule: "Avoid heavy traces in the IDE terminal buffer."
      requirements:
        - "DO NOT print heavy traces directly to the IDE terminal buffer when it can be avoided; redirect them to a file instead."
    - rule: "Set Python import context explicitly for toolkit runs."
      requirements:
        - "Set `PYTHONPATH=.` (or the correct context path) before running scripts/tests that rely on repo-relative imports."
        - "Bash example: `export PYTHONPATH=.; <command>`."
        - 'PowerShell example: `$env:PYTHONPATH = "."; <command>`.'
    - rule: "Avoid non-ASCII terminal output on Windows."
      requirements:
        - "NEVER use emojis or advanced UTF-8 content in CLI output in this Windows environment to prevent `UnicodeEncodeError: charmap` failures."
    - rule: "Force UTF-8 stdout encoding in Python CLIs."
      requirements:
        - "Every Python script or CLI entrypoint MUST include the stdout reconfiguration snippet below to ensure predictable encoding."

  python_utf8_stdout_reconfiguration_snippet: |
    import sys
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

  safe_command_execution_examples:
    bash: "export PYTHONPATH=.; python src/services/web_toolkit/capabilities/csp_validator/cli.py > /tmp/out_$(date +%Y%m%d%H%M%S)_cli_out.txt 2>&1"
    powershell: '$env:PYTHONPATH = "."; python src/services/web_toolkit/capabilities/csp_validator/cli.py *> /tmp/out_$(Get-Date -Format "yyyyMMddHHmmss")_cli_out.txt'

  GATE_TED_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - SESSION_ENVIRONMENT_AND_RUNTIME_NOTES
      - TERMINAL_OUTPUT_SAFETY_AND_EXECUTION_DIRECTIVES
      - "I MUST redirect stdout and stderr to a text file for commands likely to produce large output or tracebacks."
      - "I MUST set PYTHONPATH=. (or the correct context path) before running scripts or tests that rely on repo-relative imports."
      - "I MUST NOT use emojis or advanced UTF-8 content in CLI output in this Windows environment."
      - "I MUST include the sys.stdout.reconfigure(encoding='utf-8') snippet in every Python CLI entrypoint."
      - "I MUST treat mirrored terminal output provided by the user as the absolute truth of what happened when the IDE terminal hung."
    THEN: CONTINUE

required_quality_gate_acknowledgement_sections:
  - QUALITY_GATE_AND_REMEDIATION_POLICY_DIRECTIVES
  - ACE_CAPABILITY_AND_GATE_EXECUTION_PROFILE

# ------------------------------------------------------------
# AI AGENTS ACKNOWLEDGEMENT (mandatory)
# All agents MUST read and formally acknowledge compliance with
# every directive listed below before proceeding with any task.
# ------------------------------------------------------------

```
