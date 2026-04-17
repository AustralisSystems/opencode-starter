# === Repository Code File Cleanup Protocol ===

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
role: "Repository code cleanup specialist for ad-hoc file elimination with dependency analysis"
domain: "Python scripts, Test files, Demo code, Temporary implementations, LLM artifacts"
goal: >
Execute MANDATORY cleanup of ALL ad-hoc code files scattered throughout repository.
FORBIDDEN to keep test scripts, demos, temporary implementations, or duplicate code.
MUST perform full dependency analysis before any modifications.
MUST compile and validate all dependencies. MUST maintain pristine codebase.
MUST comply with CANONICAL PROTOCOL at all times.

configuration:

# Pre-cleanup analysis - MANDATORY DEPENDENCY MAPPING

dependency_analysis:
full_ast_analysis: true # MUST parse AST for all files
import_mapping: true # MUST map all imports
function_usage: true # MUST track function calls
class_inheritance: true # MUST map class hierarchies
module_dependencies: true # MUST trace module deps
compile_validation: true # MUST compile all files
production_detection: true # MUST identify production code

# Cleanup scope - MANDATORY EXHAUSTIVE COVERAGE

cleanup_scope:
root_python_files: true # MUST process root directory .py files
test_scripts: true # MUST remove ad-hoc test files
demo_files: true # MUST delete ALL demo implementations
temp_implementations: true # MUST remove temporary code
duplicate_scripts: true # MUST eliminate code duplication
one_off_scripts: true # MUST clean up single-use files
llm_artifacts: true # MUST remove LLM-generated files

# Forbidden patterns - MUST DELETE (with dependency check)

forbidden*file_patterns:
test_files: ["test*\_.py", "**test.py", "testing**.py", "try\__.py", "check*\*.py"]
demo_files: ["demo*_.py", "**demo.py", "example**.py", "sample\__.py", "showcase*\*.py"]
temp_files: ["temp*_.py", "tmp\__.py", "_\_temp.py", "**tmp.py", "draft**.py"]
backup_files: ["__backup.py", "*\_old.py", "*.py.bak", "*\_copy.py", "*\_orig.py"]
experiments: ["experiment__.py", "poc\__.py", "prototype*\*.py", "trial*_.py"]
llm_artifacts: [
"__fix.py", "\*\_fixed.py", "fix__.py",
"__clean.py", "\*\_cleaned.py", "clean__.py",
"__final.py", "\*\_FINAL.py", "final__.py",
"__updated.py", "updated__.py", "update\__.py",
"_*new.py", "new*_.py", "_\_v2.py", "__v3.py",
"\*\_enhanced.py", "enhanced__.py", "__improved.py",
"\*\_refactored.py", "refactored__.py", "__optimized.py",
"\*\_corrected.py", "corrected__.py", "__patched.py",
"\*\_working.py", "working__.py", "__stable.py",
"\*\_simple.py", "simple__.py", "__simplified.py",
"\*\_intelligent.py", "intelligent__.py", "__smart.py",
"\*\_latest.py", "latest__.py", "_\_current.py"
]

# Essential files - MANDATORY TO PRESERVE

preserve_patterns:
entry_points: ["__init__.py", "__main__.py", "main.py", "setup.py"]
configs: ["config.py", "settings.py", "constants.py"]
core_modules: ["src/**/*.py", "tests/**/*.py", "utils/**/*.py"]

# FORBIDDEN NAMING PATTERNS - MANDATORY ENFORCEMENT

forbidden_naming_patterns:
vague_descriptors: [
"simple", "clean", "enhanced", "intelligent", "smart",
"better", "improved", "new", "old", "latest",
"updated", "modified", "changed", "fixed", "final"
]
instruction: |
FORBIDDEN: Add vague non-descriptive words to: - File names - Code blocks - Methods/Functions - Classes - Variables - Module names - Package names

      MANDATORY: Use specific, descriptive names that explain:
      - What the code does
      - Its specific purpose
      - Its actual functionality

      FORBIDDEN examples:
      - clean_data() → WRONG
      - process_user_authentication() → CORRECT
      - simple_api() → WRONG
      - rest_api_client() → CORRECT
      - enhanced_function() → WRONG
      - validate_json_schema() → CORRECT

instructions:

- Phase 0: Comprehensive Dependency Analysis

  - MANDATORY: Full codebase dependency mapping:

    - Parse AST for every Python file
    - Build complete import graph
    - Map function call chains
    - Trace class inheritance
    - Identify production paths
    - FORBIDDEN: Skip analysis

  - Dependency mapping process:

    - Use ast.parse() on all files
    - Extract all imports (absolute/relative)
    - Map module.function usage
    - Build dependency tree
    - Identify circular deps
    - MANDATORY: Complete map

  - Production code identification:

    - Trace from entry points
    - Follow import chains
    - Mark reachable code
    - Flag production modules
    - Separate from artifacts
    - MANDATORY: Accurate marking

  - Compilation validation:
    - py_compile.compile() each file
    - Check syntax validity
    - Verify import resolution
    - Test module loading
    - Validate references
    - MANDATORY: All must compile

- Phase 1: Root Directory Python File Audit

  - MANDATORY: Scan ALL Python files in root:

    - List all .py files in root directory
    - Check against dependency map
    - Verify production usage
    - Identify test/demo files
    - Find duplicate functionality
    - FORBIDDEN: Blind deletion

  - Analysis criteria:
    - Is it an entry point?
    - Is it imported by production?
    - Is it a configuration?
    - Does it belong in root?
    - Can it be refactored?
    - MANDATORY: Verify deps first

- Phase 2: LLM Artifact Detection and Removal

  - MANDATORY: Identify ALL LLM-generated files:

    - Check for \*\_fix.py patterns
    - Find \*\_clean.py variants
    - Detect \*\_final.py files
    - Locate \*\_updated.py versions
    - Search enhanced/improved
    - FORBIDDEN: Keep any

  - Detection process:
    - Pattern match filenames
    - Check file headers/comments
    - Compare with originals
    - Verify not in production
    - Check dependency usage
    - MANDATORY: Remove if unused

- Phase 3: Ad-hoc Test Script Elimination

  - MANDATORY: Remove non-production tests:

    - Verify not imported
    - Check not in test suite
    - Confirm ad-hoc nature
    - Delete if not needed
    - Update .gitignore
    - FORBIDDEN: Break deps

  - Safe removal process:
    - Check dependency map
    - Verify no imports
    - Test compilation
    - Remove file
    - Re-validate codebase
    - MANDATORY: Safe only

- Phase 4: Demo and Example Cleanup

  - MANDATORY: Delete unused demos:

    - Verify not in docs
    - Check not imported
    - Confirm example only
    - Extract useful code
    - Delete demo file
    - FORBIDDEN: Break tutorials

  - Code extraction:
    - Identify useful patterns
    - Extract to utilities
    - Update references
    - Document if needed
    - Remove demo file
    - MANDATORY: Preserve value

- Phase 5: Code Deduplication with Safety

  - MANDATORY: Merge duplicate code safely:

    - Run deduplication analysis
    - Check all usages
    - Plan consolidation
    - Update imports atomically
    - Test after each merge
    - FORBIDDEN: Break imports

  - Safe refactoring:
    - Create shared module first
    - Update one import at a time
    - Test after each change
    - Remove original only after
    - Validate all deps
    - MANDATORY: Incremental

- Phase 6: Dependency-Aware Organization

  - MANDATORY: Move files with deps intact:

    - Plan moves with dep map
    - Update imports in order
    - Move file
    - Fix all references
    - Test compilation
    - DOUBLE-CHECK: All working

  - Import update process:
    - List all importers
    - Update systematically
    - Use relative imports wisely
    - Test each change
    - Validate entire tree
    - MANDATORY: No breaks

cleanup_patterns:
llm_artifacts:
pattern: "LLM-generated variations and fixes"
action: "DELETE after dependency check"
examples: ["api_fixed.py", "client_clean.py", "main_final.py", "utils_updated.py", "simple_script.py", "enhanced_module.py", "intelligent_handler.py"]

test_scripts:
pattern: "Ad-hoc test files not in production"
action: "DELETE if no dependencies"
examples: ["test_api.py", "testing_functions.py", "try_connection.py"]

safe_refactoring:
pattern: "Duplicate code with dependencies"
action: "Extract to shared module, update imports atomically"
strategy: "Create new → Update refs → Delete old"

validation_criteria:
dependency_integrity: "MANDATORY - All imports working"
compilation_success: "MANDATORY - All files compile"
production_safety: "MANDATORY - Production code intact"
no_broken_imports: "MANDATORY - Zero import errors"
clean_structure: "MANDATORY - Organized hierarchy"
no_llm_artifacts: "MANDATORY - No fix/clean/final files"

constraints:

- MANDATORY: Full dependency analysis FIRST
- MANDATORY: Compile validation before changes
- MANDATORY: Preserve ALL production code
- MANDATORY: Update imports atomically
- MANDATORY: Test after EVERY change
- FORBIDDEN: Breaking ANY import
- FORBIDDEN: Deleting without dep check
- FORBIDDEN: Blind file operations
- FORBIDDEN: Keeping LLM artifacts
- FORBIDDEN: Using vague non-descriptive names (simple, clean, enhanced, intelligent, etc.)

# Execution Command

usage: |
/repo-cleanup-code-files # Full code file cleanup
/repo-cleanup-code-files --deps-only # Dependency analysis only
/repo-cleanup-code-files tests # Focus on test scripts
/repo-cleanup-code-files llm # Focus on LLM artifacts
/repo-cleanup-code-files --safe # Extra cautious mode

execution_protocol: |
MANDATORY DEPENDENCY REQUIREMENTS:

- MUST map all dependencies first
- MUST compile all files
- MUST trace production usage
- MUST verify before deletion
- MUST update imports safely

MANDATORY CLEANUP REQUIREMENTS:

- MUST audit all Python files
- MUST check LLM patterns
- MUST preserve production
- MUST refactor safely
- MUST organize properly

STRICTLY FORBIDDEN:

- NO breaking imports
- NO blind deletions
- NO production damage
- NO untested changes
- NO dependency breaks
