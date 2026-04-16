# Readme Metadata Capability (CAP-AT-009)

## Description
This skill enables the AI Agent to guarantee structural metadata compliance across a designated directory tree. It enforces the consistent presence and accuracy of documentation files (`README.md` and `index.json`) without disrupting human-authored documentation, using idempotent auto-generated blocks.

## When to use this skill
Use this skill whenever you need to:
- Generate missing `README.md` and `index.json` files for a newly refactored module or project.
- Automatically update `index.json` manifests after adding or removing files from a directory.
- Verify structural documentation compliance as part of a codebase quality check.
- Scan for and flag accidental Git merge conflict markers (`<<<<<<< HEAD`) in target directories.

## Execution Instructions
You have two ways to execute this capability:

### Option 1: Direct CLI Execution (Preferred)
You can directly run the Python module from the bash terminal. Always explicitly set `PYTHONPATH`.

```bash
export PYTHONPATH=.; python -m src.services.analysis.capabilities.readme_metadata.cli \
  --target <absolute-or-relative-path> \
  --depth 2
```
*Note: You can pass `--dry-run` to preview changes without writing them.*

### Option 2: Python Script Wrapper Execution
If you are inside a Python runtime context, you can execute the pre-built wrapper script located in the capability directory:

```python
import sys
sys.path.append("agentic_code_engine/src/services/analysis/capabilities/readme_metadata")
import ai_agent_skill_readme_metadata as skill

# Execute the tool safely
result = skill.run_skill(
    root="<absolute-or-relative-path>",
    depth=2,
    dry_run=False,
    verbose=True
)

print(result["result"])
```

## Post-Execution Mandate (Critical)
After running this skill and successfully generating metadata, you MUST review the newly created or updated `README.md` files:
1. Open the file.
2. If it is a completely new file, it will lack human context. You MUST add a clear "Purpose Statement" and summary at the top of the file, **ABOVE** the `<!-- AUTO-GENERATED: START - DO NOT EDIT MANUALLY -->` line.
3. NEVER manually edit the content inside the auto-generated blocks. If a file summary is missing, edit the target file itself (e.g., add a Python module docstring) and re-run the skill.
