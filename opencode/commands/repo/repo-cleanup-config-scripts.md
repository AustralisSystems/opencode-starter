# === Repository Configuration and Scripts Cleanup Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ AND INDEX**: `C:\github_development\ai-agents\.claude\commands\ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of data or services in production code
- **NO TODOs** - complete ALL work immediately
- **NO SHORTCUTS** - implement properly ALWAYS
- **NO STUBS** - write complete implementations
- **NO FIXED DATA** - use real, dynamic data
- **NO HARDCODED VALUES** - use configuration
- **NO WORKAROUNDS** - fix root causes
- **NO FAKE IMPLEMENTATIONS** - real code only
- **NO PLACEHOLDER CODE** - production-ready only
- **NO TEMPORARY SOLUTIONS** - permanent fixes only

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read implementation documents for context
   - Review analysis documents for insights
   - Study documentation documents for patterns

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest documentation
   - Find official framework/library docs
   - Search GitHub for example implementations
   - Review industry best practices
   - Study similar successful projects
   - Check Stack Overflow for common patterns

**SEARCH PRIORITIES:**

- Official documentation (latest version)
- GitHub repositories with high stars
- Industry standard implementations
- Recent blog posts/tutorials (< 1 year old)
- Community best practices

---

## INSTRUCTIONS

model_context:
role: "Repository configuration and script cleanup specialist"
domain: "Config files, Shell scripts, Batch files, Text files, JSON/YAML sprawl"
goal: >
Execute MANDATORY cleanup of ALL configuration sprawl and script chaos.
FORBIDDEN to keep duplicate configs, shell scripts, or scattered text files.
MUST consolidate configurations. MUST convert scripts to permitted languages.
MUST comply with CANONICAL PROTOCOL at all times.

configuration:

# Cleanup scope - MANDATORY EXHAUSTIVE COVERAGE

cleanup_scope:
config_files: true # MUST process ALL config files
shell_scripts: true # MUST convert ALL .sh files
batch_files: true # MUST convert ALL .bat/.cmd files
powershell_scripts: true # MUST convert ALL .ps1 files
text_files: true # MUST clean up .txt sprawl
json_yaml_duplicates: true # MUST consolidate configs

# Forbidden languages - MUST CONVERT OR DELETE

forbidden_scripts:
shell: ["*.sh", "*.bash", "*.zsh"]
batch: ["*.bat", "*.cmd"]
powershell: ["*.ps1", "*.psm1", "*.psd1"]
vbscript: ["*.vbs", "*.vbe"]

# Permitted conversions

permitted_languages:
python: ["Python 3.8+"]
nodejs: ["Node.js with child_process"]
typescript: ["TypeScript"]
go: ["Go"]
rust: ["Rust"]

instructions:

- Phase 1: Script Language Compliance Audit

  - MANDATORY: Find ALL non-compliant scripts:

    - Glob for \*.sh files
    - Glob for _.bat/_.cmd files
    - Glob for \*.ps1 files
    - Glob for \*.vbs files
    - Create conversion tasks
    - FORBIDDEN: Ignoring scripts

  - For each forbidden script:
    - Analyze functionality
    - Determine conversion target
    - Create MCP task for conversion
    - Plan Python/Node.js equivalent
    - Document conversion needs
    - MANDATORY: Full inventory

- Phase 2: Shell Script Conversion

  - MANDATORY: Convert ALL shell scripts:

    - Read each .sh file
    - Analyze bash commands
    - Convert to Python subprocess
    - Or use Node.js child_process
    - Test converted functionality
    - Delete original .sh file

  - Conversion patterns:
    - File operations → Python pathlib
    - Process execution → subprocess.run
    - Environment vars → os.environ
    - Conditionals → Python if/else
    - Loops → Python for/while
    - MANDATORY: Full conversion

- Phase 3: Batch/PowerShell Conversion

  - MANDATORY: Convert ALL Windows scripts:

    - Read .bat/.cmd/.ps1 files
    - Extract core functionality
    - Rewrite in Python
    - Handle Windows-specific ops
    - Ensure cross-platform
    - Delete original files

  - Common conversions:
    - Directory ops → os/pathlib
    - Registry → Python winreg
    - Services → subprocess/psutil
    - File manipulation → shutil
    - Network ops → requests
    - FORBIDDEN: Keep originals

- Phase 4: Configuration Consolidation

  - MANDATORY: Consolidate ALL configs:

    - Find duplicate JSON files
    - Identify redundant YAML
    - Merge similar configs
    - Create single source
    - Update references
    - Delete duplicates

  - Consolidation rules:
    - One config per purpose
    - Environment-specific sections
    - Clear naming conventions
    - Proper directory structure
    - Version control friendly
    - MANDATORY: No duplicates

- Phase 5: Text File Cleanup

  - MANDATORY: Clean ALL .txt files:

    - Inventory all .txt files
    - Categorize by content
    - Convert docs to .md
    - Move data to proper format
    - Delete temporary notes
    - FORBIDDEN: Scattered .txt

  - Cleanup criteria:
    - TODO lists → Issue tracker
    - Notes → Documentation
    - Data files → JSON/CSV
    - Logs → Proper log files
    - Instructions → README
    - MANDATORY: Proper formats

- Phase 6: Directory Structure Enforcement

  - MANDATORY: Organize ALL configs:

    - Create config/ structure
    - Move all configs there
    - Create subdirectories
    - Update all references
    - Document structure
    - DOUBLE-CHECK: Clean root

  - Final structure:
    - config/
      - environments/
      - services/
      - credentials/
      - schemas/
    - MANDATORY: Organized

conversion_patterns:
shell_to_python:
from: "#!/bin/bash scripts"
to: "Python with subprocess"
example: | # Shell: git status # Python: subprocess.run(['git', 'status'], capture_output=True)

batch_to_python:
from: "Windows batch files"
to: "Cross-platform Python"
example: | # Batch: dir /s # Python: Path('.').rglob('\*')

powershell_to_python:
from: "PowerShell scripts"
to: "Python equivalents"
example: | # PS: Get-ChildItem # Python: os.listdir() or Path.iterdir()

validation_criteria:
script_compliance: "MANDATORY - Only permitted languages"
no_shell_scripts: "MANDATORY - Zero .sh files"
no_batch_files: "MANDATORY - Zero .bat/.cmd files"
no_powershell: "MANDATORY - Zero .ps1 files"
config_consolidation: "MANDATORY - No duplicate configs"
proper_organization: "MANDATORY - Clean directory structure"

constraints:

- MANDATORY: Convert ALL shell scripts
- MANDATORY: Convert ALL batch files
- MANDATORY: Convert ALL PowerShell
- MANDATORY: Delete ALL originals
- MANDATORY: Consolidate configs
- FORBIDDEN: Shell/Batch/PS scripts
- FORBIDDEN: Duplicate configs
- FORBIDDEN: Scattered .txt files
- FORBIDDEN: Config sprawl
- FORBIDDEN: Using vague non-descriptive names (simple, clean, enhanced, intelligent, etc.)

# Execution Command

usage: |
/repo-cleanup-config-scripts # Full cleanup
/repo-cleanup-config-scripts shell # Focus on shell scripts
/repo-cleanup-config-scripts configs # Focus on config files
/repo-cleanup-config-scripts convert # Focus on conversions

execution_protocol: |
MANDATORY CONVERSION REQUIREMENTS:

- MUST convert all scripts
- MUST use permitted languages
- MUST test conversions
- MUST delete originals
- MUST update references

STRICTLY FORBIDDEN:

- NO shell scripts (.sh)
- NO batch files (.bat/.cmd)
- NO PowerShell (.ps1)
- NO VBScript (.vbs)
- NO script language mixing
