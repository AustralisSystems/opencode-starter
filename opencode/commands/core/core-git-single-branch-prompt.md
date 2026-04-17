# Code Protocol: Single Branch Development - Mandatory Instructions

### PROTOCOL HIERARCHY
This protocol must be read and applied AFTER:
1. `code-protocol-compliance-prompt.md` - Base compliance requirements and requirements language
2. `documentation-protocol-prompt.md` - Documentation standards

### MANDATORY READING REQUIREMENT
**BEFORE ANY GIT OPERATIONS, YOU MUST:**
- **MUST READ AND INDEX:** `code-protocol-single-branch-strategy.md` - Git workflow philosophy, methods, and procedures

---

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS PROTOCOL IS MANDATORY FOR ALL AI INSTANCES WORKING ON THIS CODEBASE**

### MULTI-AI DEVELOPMENT MANDATE - RFC 2119 COMPLIANCE

**FOR ALL AI INSTANCES (Claude, GPT, Gemini, Ollama, etc.), YOU MUST:**
- **MUST:** Use single development branch strategy EXCLUSIVELY
- **MUST NOT:** Create feature branches without explicit permission
- **SHALL:** Tag all commits with AI instance identification
- **MUST:** Maintain atomic commits with clear descriptions
- **SHALL:** Coordinate through commit messages and frequent pushes

---

## ENTERPRISE PRODUCTION CODE MANDATE - RFC 2119 COMPLIANCE

**FOR ALL GIT BRANCH OPERATIONS, YOU MUST:**
- **MUST:** Focus EXCLUSIVELY on production code development
- **MUST NOT:** Create branches for test, demo, or experimental code
- **SHALL:** Use professional commit messages with clear purpose
- **MUST:** Apply SOLID/DRY/KISS principles to git workflow
- **SHALL:** Ensure all commits support immediate production deployment

---

## [CRITICAL] SIMPLIFIED SINGLE-BRANCH DEVELOPMENT STRATEGY

### RFC 2119 COMPLIANCE - DEVELOPMENT-FIRST APPROACH

**PRIMARY RULE - DEVELOPMENT BRANCH ONLY:**

- **development** - THE ONLY ACTIVE WORKING BRANCH
- **MUST:** Work directly on development branch for ALL coding activities
- **MUST NOT:** Create automatic feature branches for simple changes
- **SHALL:** Use backup branches ONLY for significant checkpoints

**SACRED BRANCHES - ABSOLUTELY FORBIDDEN FOR DIRECT WORK:**

- **main** - Production release branch - NEVER TOUCH
- **master** - Legacy production branch - NEVER TOUCH  
- **production** - Production deployment branch - NEVER TOUCH

---

## MANDATORY WORKING PROTOCOL

### VIOLATION RESPONSE PROTOCOL
```bash
# If accidentally on sacred branch, immediately switch to development
CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" == "main" || "$CURRENT_BRANCH" == "master" || "$CURRENT_BRANCH" == "production" ]]; then
    echo "ERROR: On sacred branch $CURRENT_BRANCH - switching to development"
    git checkout development
fi
```

### ATOMIC COMMIT MESSAGE FORMAT - MANDATORY

**COMMIT MESSAGE STRUCTURE:**
```
type(scope): clear one-line description

- Bullet point describing specific change
- Another bullet point for additional change
- Third bullet point if needed

[AI-Instance-ID-Timestamp]
```

**COMMIT TYPES:**
- **feat**: New feature implementation
- **fix**: Bug fix or correction
- **refactor**: Code improvement without changing functionality
- **docs**: Documentation updates
- **chore**: Maintenance tasks, dependency updates
- **security**: Security improvements or fixes

---

## FORBIDDEN ACTIONS

**NEVER DO:**
- Create automatic feature branches for simple changes
- Work on main/master/production branches
- Leave uncommitted changes without proper commits
- Force push without explicit permission
- Delete development branch
- Create complex branch hierarchies

**ALWAYS DO:**
- Work on development branch only
- Commit frequently with clear messages
- Track all files before committing
- Push after each commit for backup
- Use backup branches for major checkpoints only

---

## COMPLIANCE VERIFICATION

**MANDATORY CHECKS BEFORE ANY GIT OPERATION:**
- Current branch is development
- All files are tracked (git add .)
- Commit messages follow format requirements
- Working directory is clean after commits
- Remote backup is up to date

**AUDIT TRAIL:**
- All commits tagged with instance identifier
- All actions logged with timestamps
- All backup branches documented with purpose
- All recovery actions recorded

---

**ENFORCEMENT:** This simplified branch strategy eliminates complex multi-instance protocols while maintaining code safety through frequent atomic commits and manual backup branching only when needed.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>