# === Repository Unicode and Emoji Elimination Protocol ===

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
role: "Repository Unicode/Emoji elimination specialist"
domain: "Source code, Comments, Documentation, Commit messages, File names"
goal: >
Execute MANDATORY removal of ALL Unicode symbols and emoji from entire codebase.
FORBIDDEN to use or retain any non-ASCII characters in any context.
MUST maintain pure ASCII codebase. MUST fix all violations immediately.
MUST comply with CANONICAL PROTOCOL at all times.

configuration:

# Cleanup scope - MANDATORY EXHAUSTIVE COVERAGE

cleanup_scope:
source_code: true # MUST clean ALL code files
comments: true # MUST clean ALL comments
documentation: true # MUST clean ALL docs
commit_messages: true # MUST clean git history
file_names: true # MUST clean ALL filenames
string_literals: true # MUST clean ALL strings

# Forbidden characters - MUST REMOVE

forbidden_patterns:
emoji: ["[\U0001F600-\U0001F64F]", "[\U0001F300-\U0001F5FF]", "[\U0001F680-\U0001F6FF]"]
symbols: ["[\U00002702-\U000027B0]", "[\U0001F900-\U0001F9FF]"]
decorative: ["★", "☆", "♥", "♦", "♠", "♣", "•", "◦", "▸", "▪", "▫"]
arrows: ["→", "←", "↑", "↓", "⇒", "⇐", "⇑", "⇓"]
checkmarks: ["[OK]", "✔", "[ERROR]", "✘", "☑", "☒"]

# ASCII replacements

ascii*replacements:
arrows: {"→": "->", "←": "<-", "⇒": "=>", "⇐": "<="}
checkmarks: {"[OK]": "[OK]", "✔": "[YES]", "[ERROR]": "[NO]", "✘": "[FAIL]"}
bullets: {"•": "*", "◦": "-", "▸": ">", "▪": "-", "▫": "-"}
symbols: {"★": "\_", "☆": "\*", "♥": "[HEART]", "♦": "[DIAMOND]"}

instructions:

- Phase 1: Unicode Detection Scan

  - MANDATORY: Scan ALL files for Unicode:

    - Use regex patterns for emoji
    - Detect non-ASCII characters
    - Find Unicode in comments
    - Check string literals
    - Scan documentation
    - FORBIDDEN: Missing any

  - File types to scan:
    - Python files (\*.py)
    - JavaScript (_.js, _.ts)
    - Markdown (\*.md)
    - JSON/YAML configs
    - Text files (\*.txt)
    - MANDATORY: All types

- Phase 2: Source Code Cleaning

  - MANDATORY: Remove ALL Unicode from code:

    - Clean inline comments
    - Fix string literals
    - Update docstrings
    - Replace with ASCII
    - Maintain functionality
    - FORBIDDEN: Unicode remains

  - Replacement strategy:
    - Emoji → descriptive text
    - Arrows → ASCII equivalents
    - Symbols → text markers
    - Decorative → plain text
    - Special chars → escaped
    - MANDATORY: Pure ASCII

- Phase 3: Comment and Documentation Cleaning

  - MANDATORY: Clean ALL documentation:

    - Process all .md files
    - Clean code comments
    - Fix README files
    - Update docstrings
    - Clean inline docs
    - FORBIDDEN: Any Unicode

  - Documentation rules:
    - No emoji in headers
    - No Unicode bullets
    - No decorative symbols
    - Plain ASCII only
    - Clear formatting
    - MANDATORY: Readable

- Phase 4: File Name Sanitization

  - MANDATORY: Fix ALL file names:

    - Find Unicode in names
    - Rename to ASCII only
    - Update all references
    - Fix import statements
    - Update documentation
    - FORBIDDEN: Unicode names

  - Naming rules:
    - Letters, numbers, underscore
    - Hyphens allowed
    - No spaces or Unicode
    - Lowercase preferred
    - Descriptive names
    - MANDATORY: ASCII only

- Phase 5: Git History Cleaning

  - MANDATORY: Clean commit messages:

    - Scan recent commits
    - Identify Unicode usage
    - Plan cleanup strategy
    - Document violations
    - Prevent future use
    - FORBIDDEN: Emoji commits

  - Prevention measures:
    - Add pre-commit hooks
    - Update contributing guide
    - Document standards
    - Enforce in CI/CD
    - Regular scanning
    - MANDATORY: Enforcement

- Phase 6: Validation and Prevention

  - MANDATORY: Verify complete cleanup:

    - Run Unicode detection
    - Check all file types
    - Validate replacements
    - Test functionality
    - Document changes
    - DOUBLE-CHECK: All clean

  - Future prevention:
    - Pre-commit hooks
    - CI/CD checks
    - Code review rules
    - Documentation updates
    - Team training
    - MANDATORY: No regression

cleanup_patterns:
emoji_in_code:
pattern: "Emoji characters in source code"
action: "Replace with descriptive text"
example: "# 🚀 Deploy → # [DEPLOY] Deploy"

unicode_arrows:
pattern: "Unicode arrows and symbols"
action: "Replace with ASCII equivalent"
example: "→ becomes ->, ⇒ becomes =>"

decorative_bullets:
pattern: "Unicode bullets in lists"
action: "Replace with ASCII markers"
example: "• Item → \* Item, ▸ Sub → > Sub"

validation_criteria:
pure_ascii: "MANDATORY - 100% ASCII codebase"
no_emoji: "MANDATORY - Zero emoji characters"
no_unicode_symbols: "MANDATORY - No Unicode symbols"
clean_comments: "MANDATORY - ASCII-only comments"
ascii_filenames: "MANDATORY - ASCII-only file names"
prevention_enabled: "MANDATORY - Hooks configured"

constraints:

- MANDATORY: Remove ALL emoji
- MANDATORY: Remove ALL Unicode
- MANDATORY: Use ASCII only
- MANDATORY: Fix ALL files
- MANDATORY: Update references
- FORBIDDEN: Any non-ASCII
- FORBIDDEN: Emoji in code
- FORBIDDEN: Unicode symbols
- FORBIDDEN: Special characters
- FORBIDDEN: Using vague non-descriptive names (simple, clean, enhanced, intelligent, etc.)

# Execution Command

usage: |
/repo-cleanup-unicode-emoji # Full Unicode cleanup
/repo-cleanup-unicode-emoji code # Focus on source code
/repo-cleanup-unicode-emoji docs # Focus on documentation
/repo-cleanup-unicode-emoji strict # Most aggressive cleanup

execution_protocol: |
MANDATORY CLEANUP REQUIREMENTS:

- MUST scan entire codebase
- MUST remove ALL Unicode
- MUST remove ALL emoji
- MUST use ASCII only
- MUST fix all violations

STRICTLY FORBIDDEN:

- NO emoji characters
- NO Unicode symbols
- NO special characters
- NO decorative text
- NO non-ASCII anywhere
