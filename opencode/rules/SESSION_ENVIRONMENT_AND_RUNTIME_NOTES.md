# SESSION_ENVIRONMENT_AND_RUNTIME_NOTES

```yaml
SESSION_ENVIRONMENT_AND_RUNTIME_NOTES:
  enforcement: MANDATORY
  gate_id: session_environment_and_runtime_notes
  requires_immediate_action: true
  blocking: true

  terminal_failure_recovery_protocol: >
    **IMPORTANT: ANTIGRAVITY IDE TERMINAL HANG WORKAROUND**
    When YOU execute a terminal command (like `pytest` or a script) and it fails, the pseudo-terminal in the Antigravity IDE often locks up and hangs indefinitely. This occurs because the terminal buffer cannot process the sudden heavy volume of error tracebacks or unhandled Unicode characters (like emojis) without crashing the UI.

        Because of this IDE limitation, if your command hangs:
        1. I (the human user) will manually cancel the hanging process you spawned.
        2. I will then copy the exact command you tried to run and execute it myself in an isolated, external terminal.
        3. I will paste the mirrored results (the actual output/errors from outside the IDE) back into our chat.

        **YOUR MANDATE WHEN THIS HAPPENS:**
        When I provide you with a mirrored output, YOU MUST immediately understand that your previous command hung the IDE and failed. You must treat my pasted output as the absolute truth of what happened. You must consider these error tracebacks when evaluating, planning, and taking your next actions, and immediately adjust your execution strategy (such as using output redirection `> out.txt 2>&1`) to avoid triggering another IDE hang on subsequent attempts.

```
