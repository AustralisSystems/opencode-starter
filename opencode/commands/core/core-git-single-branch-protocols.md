# Code Protocol: Single Branch Development Strategy - Philosophy, Methods & Procedures

### STRATEGIC OVERVIEW

This file contains the philosophy, methodology, and detailed procedures for single branch development. This strategy must be read and indexed before any git operations per the mandatory protocol instructions in `code-protocol-single-branch-prompt.md`.

---

## GIT WORKFLOW PHILOSOPHY

### SIMPLICITY PRINCIPLE

Single branch development eliminates complexity while maintaining safety:

- **One Branch:** No confusion about where to work
- **Clear History:** All changes tracked in linear progression
- **Instance Coordination:** Multiple AI instances can work safely
- **Atomic Safety:** Frequent commits prevent work loss

### MULTI-AI COLLABORATION APPROACH

When multiple AI instances work on the same codebase:

- Each AI follows identical protocols
- Instance identification prevents confusion
- Atomic commits enable safe coordination
- Simple workflow reduces conflicts

---

## DETAILED WORKING PROCEDURES

### PHASE 1: ENSURE DEVELOPMENT BRANCH IS ACTIVE

```bash
# Always ensure on development branch
git checkout development

# Pull latest changes if working with remote
git pull origin development 2>/dev/null || echo "No remote configured"

# Verify we're on development
CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" != "development" ]]; then
    echo "CRITICAL: Not on development branch. Current: $CURRENT_BRANCH"
    exit 1
fi
```

### PHASE 2: TRACK ALL FILES AND COMMIT ATOMICALLY

```bash
# Track all new and modified files
git add .

# Verify what will be committed
git status

# Create atomic commit with descriptive message
git commit -m "type(scope): clear description of changes

- Specific change 1 implemented
- Specific change 2 fixed
- Specific change 3 enhanced

[AI-Type-Model-$(date -u +%Y-%m-%dT%H:%M:%SZ)]"

# Push to remote immediately for backup
git push origin development
```

### COMMIT MESSAGE EXAMPLES

```
feat(cli): implement user authentication validation

- Added password strength validation
- Implemented session timeout handling
- Enhanced error messaging for failed login

[Claude-Sonnet-4-2025-08-08T15:24:00Z]
```

```
fix(api): resolve connection timeout issues

- Increased default timeout from 30s to 60s
- Added retry logic for failed connections
- Fixed memory leak in connection pooling

[Claude-Sonnet-4-2025-08-08T15:24:00Z]
```

---

## BACKUP BRANCH METHODOLOGY

### WHEN TO CREATE BACKUP BRANCHES

- Before major refactoring operations
- Before risky architectural changes
- Before updating critical dependencies
- At significant development milestones

### BACKUP CREATION PROTOCOL

```bash
# Create backup branch with descriptive name using reverse date stamp format
BACKUP_NAME="backup/$(date -u +%Y-%m-%d-%H%M%S)-before-major-refactor"
git checkout -b "$BACKUP_NAME"

# Push backup to remote
git push origin "$BACKUP_NAME"

# Return to development branch immediately
git checkout development

echo "✅ BACKUP CREATED: $BACKUP_NAME"
echo "✅ RETURNED TO DEVELOPMENT BRANCH"
```

### BACKUP NAMING CONVENTIONS WITH REVERSE DATE STAMP FORMAT

```
backup/YYYY-MM-DD-HHMMSS-description
backup/2025-09-22-142155-before-framework-update
backup/2025-09-22-142155-before-security-refactor
backup/2025-09-22-142155-milestone-v1-complete
```

**MANDATORY DATE STAMP REQUIREMENTS FOR BACKUPS:**

- "MANDATORY: Use reverse date stamp format YYYY-MM-DD-HHMMSS for backup branches"
- "MANDATORY: Include UTC timestamp with time precision for unique identification"
- "MANDATORY: Ensure chronological sorting of backup branches"
- "FORBIDDEN: Using date-only format without time precision"

---

## RECOVERY PROCEDURES

### IF DEVELOPMENT BRANCH BECOMES CORRUPTED

```bash
# Option 1: Reset to last good commit
git log --oneline -10  # Find last good commit
git reset --hard <commit-hash>

# Option 2: Restore from backup branch (using reverse date stamp format)
git checkout backup/YYYY-MM-DD-HHMMSS-description
git checkout -b development-recovery
git checkout development
git reset --hard development-recovery
git branch -D development-recovery

# Option 3: Use git reflog to find lost commits
git reflog
git checkout <commit-hash>
git checkout -b development-temp
git checkout development
git reset --hard development-temp
git branch -D development-temp
```

---

## DAILY WORKFLOW PROCEDURES

### BEFORE STARTING WORK

- [ ] Verify on development branch: `git branch --show-current`
- [ ] Pull latest changes: `git pull origin development`
- [ ] Check working directory status: `git status`

### DURING DEVELOPMENT

- [ ] Track all files: `git add .`
- [ ] Create atomic commits with clear messages
- [ ] Push after each logical change: `git push origin development`

### BEFORE ENDING SESSION

- [ ] Commit all current work
- [ ] Push final state to remote
- [ ] Verify clean working directory: `git status`

---

## MULTI-INSTANCE COORDINATION PROCEDURES

### SIMPLE INSTANCE SAFETY

```bash
# Before starting work, check for uncommitted changes from other instances
git status
if ! git diff-index --quiet HEAD --; then
    echo "WARNING: Uncommitted changes detected"
    echo "Review changes before proceeding:"
    git diff --name-only
fi

# Pull latest changes from other instances
git pull origin development
```

### HANDOFF PROTOCOL

```bash
# Before ending session, ensure all work is committed and pushed
git add .
git commit -m "chore(session): end of development session

- All current work committed
- Ready for next instance handoff

[AI-Type-Model-$(date -u +%Y-%m-%dT%H:%M:%SZ)]"

git push origin development
echo "✅ SESSION COMPLETE - WORK SAFELY COMMITTED"
```

---

## FILE PROTECTION PROCEDURES

### BEFORE ANY BRANCH OPERATION

```bash
# 1. CHECK FOR UNTRACKED FILES
git ls-files --others --exclude-standard  # List untracked files

# 2. VERIFY .gitignore COMPLIANCE
# If untracked files should be ignored: Add to .gitignore
# If untracked files are work files: Add and commit or stash

# 3. MANDATORY STASH BEFORE BRANCH SWITCH
git stash push -u -m "WIP: [description]"  # Include untracked files

# 4. VERIFY CLEAN STATE
git status  # MUST show "nothing to commit, working tree clean"
```

---

## MERGE AND SYNC PROCEDURES

### COMPLETING A FEATURE

```bash
# 1. FINAL COMMIT ON FEATURE BRANCH
git add .
git commit -m "feat(scope): complete [feature description]"
git push origin [feature-branch]

# 2. SYNC WITH DEVELOPMENT
git checkout development
git pull origin development
git checkout [feature-branch]
git rebase development               # Resolve conflicts if any
git push origin [feature-branch] --force-with-lease

# 3. MERGE TO DEVELOPMENT
git checkout development
git merge [feature-branch] --no-ff  # Preserve feature branch history
git push origin development

# 4. CLEANUP
git branch -d [feature-branch]      # Delete local branch
git push origin --delete [feature-branch]  # Delete remote branch
```

---

## EMERGENCY WORK RECOVERY

### IF WORK IS LOST OR BRANCH CORRUPTED

```bash
# 1. CHECK STASH
git stash list                       # List all stashes
git stash show -p stash@{0}         # Preview stash content
git stash apply stash@{0}           # Recover from stash

# 2. CHECK REFLOG
git reflog                          # Show all recent commits
git checkout [commit-hash]          # Recover from specific commit

# 3. CHECK REMOTE BRANCHES
git fetch --all                     # Fetch all remote branches
git branch -r                       # List remote branches
git checkout origin/[branch-name]   # Recover from remote
```

---

## SAFETY CHECKLISTS

### BEFORE EVERY SESSION

- [ ] Current branch identified and clean
- [ ] No uncommitted changes without stash
- [ ] Remote origin synchronized
- [ ] .gitignore properly configured

### BEFORE EVERY BRANCH SWITCH

- [ ] `git status` shows clean working tree
- [ ] All work stashed or committed
- [ ] Current branch pushed to origin
- [ ] Target branch verified exists

### BEFORE EVERY COMMIT

- [ ] Code compiles and runs
- [ ] Tests pass (if applicable)
- [ ] Linting passes
- [ ] Commit message follows format
- [ ] Changes are logical atomic unit

### AFTER EVERY COMMIT

- [ ] Pushed to origin immediately
- [ ] Branch status verified
- [ ] Working tree remains clean

---

## WHY THIS STRATEGY WORKS FOR MULTI-AI DEVELOPMENT

### The Problem It Solves

When multiple AI instances (Claude, GPT, Gemini, Ollama) work on the same codebase:

- Each AI might create different branch names for the same task
- Branch switching causes confusion and mixed purposes
- Complex branching strategies lead to conflicts

### The Solution

- **One branch** = No confusion possible
- **Clear commits** = Full traceability without branches
- **Instance tagging** = Know who did what
- **Atomic commits** = Easy to revert specific changes
- **Frequent pushes** = Automatic backup and coordination

### Perfect for AI Collaboration

- AIs follow protocols precisely
- No human ego or preferences
- Consistent execution every time
- Simple enough for any AI to understand
- Powerful enough for complex development

**PREVENTION IS BETTER THAN RECOVERY - FOLLOW THE PROTOCOL RELIGIOUSLY**

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
