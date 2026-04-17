# Repository Documentation Cleanup Protocol (SAFE VERSION)

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

## SAFE CLEANUP PHASES

### Phase 1: Inventory and Preview

```bash
# First, create an inventory of potential cleanup candidates
echo "=== DOCUMENTATION CLEANUP PREVIEW ==="
echo "The following files are candidates for cleanup:"
echo ""

# Find temporal reports (with safe patterns)
echo "1. TEMPORAL REPORTS (safe patterns):"
find . -name "*-report-[0-9]*.md" -o -name "*-analysis-[0-9]*.md" -o -name "*-summary-[0-9]*.md" | grep -v "/docs/architecture/" | sort

# Find obvious duplicates
echo ""
echo "2. OBVIOUS DUPLICATES:"
find . -name "README_*.md" -o -name "README-old.md" -o -name "README-backup.md" -o -name "*.backup.md" | sort

# Find AI session artifacts (specific patterns only)
echo ""
echo "3. AI SESSION ARTIFACTS:"
find . -name "claude-session-*.md" -o -name "gpt-output-*.md" -o -name "ai-conversation-*.md" | sort

# Find temporary documentation
echo ""
echo "4. TEMPORARY DOCUMENTATION:"
find . -name "TODO.md" -o -name "NOTES.md" -o -name "temp-*.md" -o -name "draft-*.md" | grep -v "/docs/" | sort
```

### Phase 2: User Review and Confirmation

**MANDATORY USER INTERACTION:**

```
Please review the files listed above.
- Files marked for deletion should be reviewed
- Any file you want to keep should be noted
- Confirm you want to proceed with cleanup

Type 'CONFIRM' to proceed or 'CANCEL' to abort:
```

### Phase 3: Safe Deletion with Logging

**FOR EACH FILE TO DELETE:**

1. Log the deletion to `cleanup-log-[timestamp].txt`
2. Show file path and first 5 lines of content
3. Get individual confirmation for files > 1000 lines
4. Delete only after confirmation

### Phase 4: Documentation Consolidation (NOT Deletion)

**INSTEAD OF DELETING, CONSOLIDATE:**

- Multiple READMEs → Merge into single README.md
- Scattered docs → Organize into `/docs/` structure
- Temporal reports → Archive to `/docs/archive/[year]/`

### Phase 5: Jupyter Notebook Conversion

**SAFE CONVERSION PROCESS:**

1. Copy .md file to .ipynb (don't delete original yet)
2. Verify document renders correctly
3. Get user confirmation
4. Only then remove original .md

---

## SAFE PATTERNS FOR CLEANUP

### SAFE TO DELETE (with confirmation):

```yaml
safe_patterns:
  temporal_with_dates:
    - "*-report-2024-*.md" # Reports with specific dates
    - "*-analysis-2024-*.md" # Analysis with specific dates
    - "meeting-notes-*.md" # Meeting notes with dates

  obvious_temps:
    - "temp-*.md" # Clearly temporary
    - "test-*.md" # Test documentation
    - "draft-*.md" # Draft documents

  clear_duplicates:
    - "*.backup.md" # Explicit backups
    - "*-old.md" # Explicit old versions
    - "*-copy.md" # Explicit copies
```

### REQUIRES REVIEW (never auto-delete):

```yaml
review_required:
  - Files containing "analysis" without dates
  - Files containing "report" without dates
  - Files containing "summary" without dates
  - Any file > 1000 lines
  - Any file in /docs/ directory
  - Any file with diagrams or images
```

---

## ENHANCED SAFETY COMMANDS

### Interactive Cleanup Mode:

```bash
# Start interactive cleanup session
/repo-cleanup-documentation --interactive

# Preview only (no deletions)
/repo-cleanup-documentation --preview

# Create backup before cleanup
/repo-cleanup-documentation --backup

# Archive instead of delete
/repo-cleanup-documentation --archive
```

### Safety Options:

- `--interactive` - Confirm each file individually
- `--preview` - Show what would be deleted without deleting
- `--backup` - Create backup branch first
- `--archive` - Move to archive instead of deleting
- `--dry-run` - Simulate the entire process

---

## CRITICAL SAFETY RULES

1. **NEVER** use wildcard patterns like `*analysis*.md`
2. **ALWAYS** preview before deleting
3. **REQUIRE** user confirmation for deletions
4. **PRESERVE** all architectural documentation
5. **BACKUP** before major operations
6. **LOG** all deletions for recovery
7. **ARCHIVE** instead of delete when unsure

---

## ERROR PREVENTION

**FORBIDDEN PRACTICES:**

- Deleting without preview
- Using overly broad patterns
- Ignoring user concerns
- Deleting architectural docs
- Removing files without reading them
- Batch deleting without review

**MANDATORY PRACTICES:**

- Read file content before deletion
- Check file importance
- Verify not referenced elsewhere
- Ensure proper backups exist
- Document why file was removed
- Provide recovery instructions

---

## RECOVERY PROCEDURES

**IF ACCIDENTAL DELETION OCCURS:**

```bash
# Check cleanup log
cat cleanup-log-*.txt

# Recover from git
git checkout HEAD~1 -- [deleted-file]

# Restore from backup branch
git checkout backup-cleanup-[date] -- [deleted-file]
```

---

## Usage Examples

### Safe Preview:

```bash
/repo-cleanup-documentation-safe --preview
# Shows what would be cleaned up without deleting anything
```

### Interactive Cleanup:

```bash
/repo-cleanup-documentation-safe --interactive
# Asks for confirmation on each file
```

### Archive Old Docs:

```bash
/repo-cleanup-documentation-safe --archive
# Moves old docs to /docs/archive/ instead of deleting
```

---

**REMEMBER:** The goal is a clean repository WITHOUT losing important documentation. When in doubt, preserve the file!
