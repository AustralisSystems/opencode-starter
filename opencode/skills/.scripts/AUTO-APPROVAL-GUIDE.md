# Auto-Approval Mode Guide

**Version:** 1.0.0
**Framework:** MCP v6.0.0

## Overview

Auto-approval allows Claude to bypass approval gates and proceed autonomously through multi-step workflows. This accelerates development but requires understanding of safety implications.

## How to Enable Auto-Approval

Add any of these phrases to your request:
- `with auto-approval`
- `auto-approve`
- `skip approval gates`
- `autonomous mode`
- `auto-approve Gate [N]` (specific gate)
- `auto-approve all gates`

## Examples

```
✅ "Design a FastAPI authentication service with auto-approval"
✅ "Implement Python data parser, auto-approve all gates"
✅ "Refactor FastAPI code with auto-approval"
✅ "Auto-approve: quality check the Python code"
```

## Approval Gates Explained

### Gate 1 - Planning Approval
- **After:** Steps 1-11 (design/planning phase)
- **Before:** Core implementation
- **Decision:** Approve architecture/plan

### Gate 2 - Implementation Review
- **After:** Steps 12-16 (implementation phase)
- **Before:** Quality enhancement
- **Decision:** Approve code changes

### Gate 3 - Deployment Approval
- **After:** Step 24 (final validation)
- **Before:** Production deployment
- **Decision:** Approve deployment

## Safety Ratings by Skill Type

### ✅ SAFE - Auto-Approval Recommended

**Design Skills** (Read-only analysis):
- `python-design`, `fastapi-design`, `fastmcp-design`
- Gates: [1]
- Risk: **LOW** - No code changes, just planning

**Planning Skills** (Read-only planning):
- `python-planning`, `fastapi-planning`, `fastmcp-planning`
- Gates: [1]
- Risk: **LOW** - Task breakdown only

**Quality Review Skills** (Read-only validation):
- `python-quality-review`, `fastapi-quality-review`, `fastmcp-quality-review`
- `quality-validation`, `quality-security`
- Gates: None (no gates in review workflows)
- Risk: **LOW** - Analysis only, no changes

**Type Check** (Validation):
- `python-typecheck`
- Gates: None
- Risk: **LOW** - Type validation only

### ⚠️ USE CAUTION - Review Recommended

**Implementation Skills** (Writes new code):
- `python-implement`, `fastapi-implement`, `fastmcp-implement`
- Gates: [1, 2]
- Risk: **MEDIUM** - Creates new code
- **Recommendation:** Auto-approve Gate 1 (plan), review Gate 2 (code)

**Test Implementation** (Writes tests):
- `test-implementation`
- Gates: [1, 2]
- Risk: **MEDIUM** - Creates test code
- **Recommendation:** Auto-approve Gate 1, review test coverage

**Refactor Skills** (Modifies existing code):
- `python-refactor`, `fastapi-refactor`, `fastmcp-refactor`
- Gates: None (direct execution)
- Risk: **MEDIUM** - Modifies working code
- **Recommendation:** Review changes before applying

**Code Remediation** (Fixes code issues):
- `code-remediation`
- Gates: None
- Risk: **MEDIUM** - Modifies code to fix issues
- **Recommendation:** Review fixes before applying

**Code Debug** (Investigates and fixes):
- `code-debug`
- Gates: None
- Risk: **MEDIUM** - May modify code
- **Recommendation:** Review proposed fixes

### 🔴 HIGH RISK - Manual Review Strongly Recommended

**Full Framework Execution** (24 steps):
- Running complete framework with Gates 1, 2, 3
- Risk: **HIGH** - Full lifecycle changes
- **Recommendation:** Only auto-approve Gate 1, review 2 & 3

**Deployment Skills** (Production changes):
- Any deployment-related workflows
- Gates: [3]
- Risk: **HIGH** - Production impact
- **Recommendation:** NEVER auto-approve Gate 3

## Selective Gate Auto-Approval

You can approve specific gates only:

```
# Auto-approve planning, review implementation
"Implement FastAPI service, auto-approve Gate 1"

# Review design, auto-approve implementation
[After reviewing Gate 1]
"APPROVE Gate 1, then auto-approve Gate 2"
```

## Auto-Approval Behavior

**When auto-approval is enabled:**

1. **Execution continues** without pausing at specified gates
2. **I make decisions** based on best practices and standards
3. **State is saved** after each step for rollback capability
4. **You receive reports** at each gate (non-blocking)
5. **You can interrupt** anytime with "STOP" or "PAUSE"

**What still happens:**

✅ All validation and quality checks
✅ Standards compliance enforcement
✅ Error handling and recovery
✅ State preservation
✅ Progress reporting

**What doesn't happen:**

❌ No pause for user input
❌ No manual approval required
❌ No waiting at gates

## Rollback Capability

Even with auto-approval, you can rollback:

```python
# State file: project/state/stepwise-execution.json
{
  "current_step": 14,
  "steps_completed": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
  "gates_auto_approved": [1, 2],
  "artifacts_generated": ["design.md", "implementation/"]
}
```

**Rollback commands:**
- "Rollback to step 10"
- "Undo changes from step 12"
- "Restore to Gate 1"
- "Reset to before implementation"

## Best Practices

### ✅ DO Use Auto-Approval For:
- **Design and planning** phases (always safe)
- **Quality analysis** and validation (read-only)
- **Type checking** and linting (validation only)
- **Well-understood workflows** you've run before
- **Rapid prototyping** iterations
- **Non-critical environments** (dev, staging)

### ❌ DON'T Use Auto-Approval For:
- **Production deployments** (Gate 3)
- **First time workflows** (learn the process first)
- **Critical/sensitive code** changes
- **Large refactorings** without review
- **Security-sensitive** implementations
- **When learning** new patterns

### 🎯 Strategic Auto-Approval:
- **Design → Review → Implement**: Auto-approve design, review architecture, then auto-approve implementation
- **Iterative Development**: Auto-approve for iterations 2+, review iteration 1
- **Trusted Patterns**: Auto-approve when repeating known-good patterns

## Safety Mechanisms

Even with auto-approval enabled:

1. **RFC 2119 Compliance**: All MUST/SHALL requirements enforced
2. **Standards Validation**: All standards checked automatically
3. **Security Scanning**: Security issues flagged (even if not blocking)
4. **Quality Gates**: Quality metrics still calculated
5. **Error Recovery**: Automatic retry/recovery on errors
6. **State Preservation**: Full rollback capability maintained

## Example Workflows

### Workflow 1: Rapid Design → Implement → Validate

```bash
# Step 1: Auto-approve design (safe)
"Design FastAPI user management API with auto-approval"
→ Claude designs autonomously, delivers architecture

# Step 2: Review architecture, then auto-approve implementation
"Implement the user management API, auto-approve Gate 2"
→ Claude implements, you review code changes

# Step 3: Auto-approve quality validation (safe)
"Run quality validation with auto-approval"
→ Claude validates autonomously, reports issues
```

### Workflow 2: Cautious Implementation

```bash
# Step 1: Auto-approve planning
"Plan Python data pipeline implementation with auto-approval"
→ Claude creates task breakdown

# Step 2: Manual review gates
"Implement Python data pipeline"
→ Pause at Gate 1: Review plan → APPROVE
→ Pause at Gate 2: Review code → APPROVE

# Step 3: Auto-approve validation
"Quality check with auto-approval"
→ Claude validates autonomously
```

### Workflow 3: Iterative Development

```bash
# Iteration 1: Manual approval (learning)
"Design FastAPI authentication"
→ Gate 1: Review design → APPROVE

"Implement authentication"
→ Gate 2: Review code → APPROVE

# Iterations 2+: Auto-approval (trusted pattern)
"Add OAuth support to authentication with auto-approval for all gates"
→ Claude extends implementation autonomously
```

## Interrupting Auto-Approval

**Stop execution:**
- "STOP"
- "PAUSE"
- "HALT"

**What happens:**
- Current step completes
- Execution pauses
- State saved
- You can review and decide to continue or rollback

## Resuming After Auto-Approval

Even with auto-approval, state is preserved:

```bash
# Resume from saved state
"Continue the FastAPI implementation from step 15"

# Resume with different approval mode
"Continue, but pause at Gate 2 for review"
```

## Configuration Override

You can override auto-approval settings:

```bash
# Force manual approval even if auto-approval requested
"Implement FastAPI service, but require manual approval at Gate 2"

# Mix auto and manual
"Auto-approve Gate 1, manual approval for Gate 2"
```

## Monitoring Auto-Approval

Track auto-approved executions:

```bash
# Check what was auto-approved
cat project/state/stepwise-execution.json | jq '.gates_auto_approved'

# Review auto-approved changes
git diff HEAD~1..HEAD

# Check quality metrics from auto-approved run
cat optimization_output/metrics/quality-report.json
```

## When Things Go Wrong

**If auto-approval produces unexpected results:**

1. **STOP** execution immediately
2. **Review** state file and generated artifacts
3. **Rollback** to last known good state
4. **Analyze** what went wrong
5. **Re-run** with manual approval
6. **Report** issues for framework improvement

## Summary Table

| Skill Category | Auto-Approval Safety | Gates | Recommendation |
|---------------|---------------------|-------|----------------|
| Design | ✅ SAFE | 1 | Always safe |
| Planning | ✅ SAFE | 1 | Always safe |
| Quality Review | ✅ SAFE | None | Always safe |
| Type Check | ✅ SAFE | None | Always safe |
| Implementation | ⚠️ CAUTION | 1, 2 | Auto Gate 1, review Gate 2 |
| Testing | ⚠️ CAUTION | 1, 2 | Review test coverage |
| Refactor | ⚠️ CAUTION | None | Review changes |
| Remediation | ⚠️ CAUTION | None | Review fixes |
| Debug | ⚠️ CAUTION | None | Review solutions |
| Deployment | 🔴 HIGH RISK | 3 | NEVER auto-approve |

---

**Remember:** Auto-approval is a power feature. Use wisely! 🚀
