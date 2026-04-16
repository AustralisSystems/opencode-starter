---
name: swarm-orchestrator
description: Unified skill for PRIME protocol activation and universal agent spawn template. Provides single-word activation for THE SWARM hierarchy and standardized spawn template for all 7 swarm orchestrators. Consolidates orchestrator entry point and spawn template functionality into one portable skill.
allowed-tools: [*]
version: 4.0.0
created: 2025-11-02
updated: 2025-11-02
architecture: 2-tier
role: PRIME Protocol Entry Point + Universal Agent Spawn Template
---

# Swarm Orchestrator - PRIME Protocol & Universal Spawn Template

**Version**: 4.0.0 (November 2025)
**Created**: 2025-11-02
**Updated**: 2025-11-02
**Type**: Dual-Purpose Skill (Entry Point + Template Provider)
**Architecture**: 2-TIER (PRIME → ORCHESTRATORS → AGENTS)

---

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

**Enforcement Statement**: All instructions using these terms are enforceable protocol, not mere suggestions.

---

## 🎯 Dual Purpose

This skill serves TWO critical functions:

### 1. PRIME Protocol Activation (Entry Point)

**Quick activation** when you say:

- "orchestrator"
- "swarm-orchestrator"
- "act as orchestrator"
- "/prime"

Routes to **PRIME protocol** (`.claude/commands/prime.md`)

### 2. Universal Agent Spawn Template (For Orchestrators)

**Provides standardized spawn template** used by all 7 swarm orchestrators:

- codex-swarm-orchestrator
- gemini-swarm-orchestrator
- grok-swarm-orchestrator
- kimi-swarm-orchestrator
- haiku-swarm-orchestrator
- qwen-swarm-orchestrator
- sonnet-swarm-orchestrator

---

## PART 1: PRIME Protocol Entry Point

### What This Does

Activates PRIME protocol which provides access to 7 specialized swarm orchestrators (November 2025):

**ALL orchestrators enforce THE GOLDEN RULE + SOLID/DRY/KISS principles:**

#### 1. **sonnet-swarm-orchestrator**

- Model: Claude 4.5 Sonnet (anthropic/claude-4.5-sonnet)
- Use: Complex reasoning, architectural design, strategic planning
- Capacity: 5 concurrent agents
- GOLDEN RULE: ALWAYS MANDATORY | SOLID/DRY/KISS: ALWAYS

#### 2. **haiku-swarm-orchestrator**

- Model: Claude 4.5 Haiku (anthropic/claude-4.5-haiku)
- Use: Fast code generation, rapid execution
- Capacity: 15 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

#### 3. **codex-swarm-orchestrator**

- Model: GPT-5.1/GPT-5-codex (openai/gpt-5.1 or openai/gpt-5-codex)
- Use: Simple code generation, CRUD, rapid prototyping
- Capacity: 10 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

#### 4. **gemini-swarm-orchestrator**

- Model: Google Gemini 2.5 Pro (google/gemini-2.5-pro)
- CLI: DUAL ROUTING - PRIMARY: native gemini CLI (direct), FALLBACK: qwen CLI → LiteLLM:47821
- Use: Strategic/complex analysis, 1M token context
- Capacity: 10 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

#### 5. **grok-swarm-orchestrator**

- Model: Grok 1 (x-ai/grok-code-fast-1, 92 tok/s) or Grok 4 Fast (xAI Grok 4 Fast (grok cli model = grok-4-latest or openrouter model = x-ai/grok-4-fast), 2M context)
- CLI: DUAL ROUTING - PRIMARY: native grok CLI (direct), FALLBACK: qwen CLI → LiteLLM:47821
- Use: Fast execution (Grok 1) or complex tasks (Grok 4)
- Capacity: 15 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

#### 6. **kimi-swarm-orchestrator**

- Model: Kimi K2 (moonshotai/kimi-k2, 128K context) or Kimi K2 Thinking (moonshotai/kimi-k2-thinking, 256K context, reasoning)
- Use: Fast code analysis (Kimi K2) or complex reasoning (Kimi K2 Thinking)
- Capacity: 15 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

#### 7. **qwen-swarm-orchestrator**

- Model: Qwen3-Coder (qwen/qwen-3-coder)
- Use: Agentic AI coding (handles BOTH complex AND simple tasks)
- Capacity: 10 concurrent agents
- GOLDEN RULE: MANDATORY | SOLID/DRY/KISS: MANDATORY

### The 2-Tier Hierarchy

```
PRIME (Claude 4.5 Sonnet - You)
  │
  ├── Strategic decomposition
  ├── Task classification
  ├── Resource allocation
  └── Quality validation
      │
      └─> ORCHESTRATORS (via Task tool)
          │
          ├─> sonnet-swarm-orchestrator → Sonnet agents (complex reasoning)
          ├─> haiku-swarm-orchestrator → Haiku agents (fast execution)
          ├─> codex-swarm-orchestrator → Codex agents (simple code)
          ├─> gemini-swarm-orchestrator → Gemini agents (strategic analysis)
          ├─> grok-swarm-orchestrator → Grok agents (fast/complex analysis)
          ├─> kimi-swarm-orchestrator → Kimi agents (fast/reasoning analysis)
          └─> qwen-swarm-orchestrator → Qwen agents (agentic coding)
              │
              └─> AGENTS (Level 2 - Peer execution units)
```

### Usage

**Invoke PRIME protocol:**

```
/prime
```

**PRIME then spawns appropriate orchestrators:**

```python
Task(subagent_type='codex-swarm-orchestrator', prompt='...')
Task(subagent_type='gemini-swarm-orchestrator', prompt='...')
# etc.
```

---

## PART 2: Universal Agent Spawn Template

### Template Location

**File**: `prompt-template.yaml` (in this directory)

**Path**: `.claude/skills/swarm-orchestrator/prompt-template.yaml`

### Used By (All 7 Swarm Orchestrators)

All orchestrator agents in `.claude/agents/` use this template:

1. **codex-swarm-orchestrator.md** (spawns GPT-5.1/GPT-5-codex agents)
2. **gemini-swarm-orchestrator.md** (spawns Gemini 2.5 Pro agents)
3. **grok-swarm-orchestrator.md** (spawns Grok 1/4 Fast agents)
4. **kimi-swarm-orchestrator.md** (spawns Kimi K2/Thinking agents)
5. **haiku-swarm-orchestrator.md** (spawns Claude 4.5 Haiku agents)
6. **qwen-swarm-orchestrator.md** (spawns Qwen3-Coder agents)
7. **sonnet-swarm-orchestrator.md** (spawns Claude 4.5 Sonnet agents)

### What the Template Provides

The `prompt-template.yaml` ensures consistent agent spawning:

✅ **RFC 2119 compliance** in all spawned agents
✅ **GOLDEN RULE workflow** (8-step mandatory process)
✅ **SOLID/DRY/KISS principles** (7 design standards)
✅ **Standardized reporting format**
✅ **Model-specific CLI commands**
✅ **Variable replacement guide**

### How Orchestrators Use the Template

#### Step 1: Reference the Template

```markdown
**Template Location**: `.claude/skills/swarm-orchestrator/prompt-template.yaml`
```

#### Step 2: Replace Variables

```python
agent_prompt = f"""You are {identity} from .claude/skills/{model}-agent/SKILL.md.

MODEL: {model_name} ({model_identifier})
CLI: {cli_command}
HIERARCHY: Level 2 - {agent_type} Agent
REPORTS_TO: PRIME

RFC 2119 COMPLIANCE: ...
GOLDEN RULE (MANDATORY): ...
SOLID/DRY/KISS (MANDATORY): ...
TASK: {task}
SUCCESS CRITERIA: ...
REPORT FORMAT: ...
"""
```

#### Step 3: Spawn Agent

```python
Bash(run_in_background=True,
     command=f"""{cli_command} "{agent_prompt}" > /tmp/{model}_agent_{id}.txt 2>&1""")
```

### CLI Command Reference

| Model      | CLI Command                                                                           | Routing                     |
| ---------- | ------------------------------------------------------------------------------------- | --------------------------- |
| **Codex**  | `codex exec -s danger-full-access --skip-git-repo-check`                              | Direct                      |
| **Haiku**  | `claude --model haiku --print`                                                        | Direct                      |
| **Sonnet** | `claude --model sonnet --print`                                                       | Direct                      |
| **Gemini** | `qwen --openai-base-url http://localhost:47821/v1 -m google/gemini-2.5-pro --yolo -p` | qwen → LiteLLM → OpenRouter |
| **Grok**   | `qwen --openai-base-url http://localhost:47821/v1 -m x-ai/grok-code-fast-1 --yolo -p` | qwen → LiteLLM → OpenRouter |
| **Kimi**   | `qwen --openai-base-url http://localhost:47821/v1 -m moonshotai/kimi-k2 --yolo -p`    | qwen → LiteLLM → OpenRouter |
| **Qwen**   | `qwen --openai-base-url http://localhost:47821/v1 -m qwen/qwen-3-coder --yolo -p`     | qwen → LiteLLM              |

---

## Mandatory Frameworks (Universal Enforcement)

Every spawned agent receives:

### 1. RFC 2119 Compliance

- Mandatory requirements language interpretation
- MUST/SHALL/NEVER enforcement

### 2. THE GOLDEN RULE (8-Step Workflow)

1. Load patterns from neo4j-memory (progressive: 5min → 48hrs)
2. RTFM (Read The F\*\*\*ing Manual - project documentation)
3. Get library docs via context7
4. Find examples via grep (GitHub search)
5. Plan with sequential-thinking
6. Implement with SOLID/DRY/KISS principles
7. Delegate to specialized sub-agents
8. Save pattern to neo4j-memory

### 3. SOLID/DRY/KISS Principles

- SRP: Single Responsibility
- OCP: Open/Closed
- LSP: Liskov Substitution
- ISP: Interface Segregation
- DIP: Dependency Inversion
- DRY: Don't Repeat Yourself
- KISS: Keep It Simple

---

## Benefits of Consolidation

### ✅ DRY (Don't Repeat Yourself)

- **Before**: 3 separate directories with overlapping purposes
- **After**: 1 unified directory with clear dual purpose
- **Eliminated**: ~1,500 lines of redundant/deprecated content

### ✅ KISS (Keep It Simple, Stupid)

- **Single directory** for all orchestrator-related functionality
- **Clear naming**: "swarm-orchestrator" - exactly what it does
- **Two files**: SKILL.md (docs) + prompt-template.yaml (template)
- **One purpose**: Orchestration entry point + spawn template

### ✅ Portability

- Entire `.claude/skills/swarm-orchestrator/` moves as one unit
- All references use consistent path
- Self-contained and complete

### ✅ Maintainability

- Update once, affects entire system
- Single source of truth for orchestration
- Clear versioning (v4.0.0)
- Easy to understand and modify

---

## Directory Structure

```
.claude/skills/swarm-orchestrator/
  ├── SKILL.md (this file)
  │   ├─> Part 1: PRIME protocol activation
  │   ├─> Part 2: Universal agent spawn template docs
  │   └─> RFC 2119 + GOLDEN RULE + SOLID/DRY/KISS
  │
  └── prompt-template.yaml
      ├─> Variable replacement guide
      ├─> CLI commands for all 7 models
      ├─> Complete agent prompt structure
      └─> RFC 2119 + GOLDEN RULE + SOLID/DRY/KISS enforcement
```

**Portable**: This entire directory is copied/moved with `.claude/skills/` for deployment consistency.

---

## Replaces (Deprecated/Consolidated)

This skill **consolidates and replaces**:

1. **orchestrator** (`.claude/skills/orchestrator/`)

   - Purpose: PRIME protocol entry point
   - Status: Consolidated into this skill (Part 1)

2. **swarm-orchestrator-spawn-template** (`.claude/skills/swarm-orchestrator-spawn-template/`)

   - Purpose: Universal agent spawn template
   - Status: Consolidated into this skill (Part 2)

3. **swarm-leader** (`.claude/skills/swarm-leader/`)
   - Purpose: 3-tier SWARM-LEADER (deprecated architecture)
   - Status: DEPRECATED (replaced by 2-tier PRIME → AGENTS)

---

## How to Activate (Entry Point)

Say any of:

- "orchestrator"
- "swarm-orchestrator"
- "act as orchestrator"
- "/prime"

This activates PRIME protocol from `.claude/commands/prime.md`

---

## How Orchestrators Use This (Spawn Template)

### Reference in Orchestrator Files

```markdown
**Template Location**: `.claude/skills/swarm-orchestrator/prompt-template.yaml`
```

### Variable Replacement

See `prompt-template.yaml` for complete variable list and replacement guide.

### Example Usage in Orchestrator

```python
# Read template structure (reference only - inline spawn for simplicity)
# Replace variables with actual values
# Construct spawn command with frameworks enforced

agent_prompt = f"""You are {identity} from {skill_reference}.

MODEL: {model_name}
CLI: {cli_command}
HIERARCHY: Level 2
REPORTS_TO: PRIME

RFC 2119 COMPLIANCE: MANDATORY
GOLDEN RULE: 8-step workflow
SOLID/DRY/KISS: 7 principles

TASK: {task}
"""

Bash(run_in_background=True, command=f"{cli_command} '{agent_prompt}' ...")
```

---

## System Architecture (November 2025)

| Orchestrator | Model             | Capacity | Use Case           | Speed            |
| ------------ | ----------------- | -------- | ------------------ | ---------------- |
| sonnet-swarm | Claude 4.5 Sonnet | 5        | Complex reasoning  | 60-120s          |
| haiku-swarm  | Claude 4.5 Haiku  | 15       | Fast execution     | 10-30s           |
| codex-swarm  | GPT-5.1/GPT-5-codex    | 10       | Simple code        | Fast             |
| gemini-swarm | Gemini 2.5 Pro    | 10       | Strategic analysis | Fast             |
| grok-swarm   | Grok 1/4 Fast     | 15       | Fast/complex       | 10-60s (Grok 1)  |
| kimi-swarm   | Kimi K2/Thinking  | 15       | Fast/reasoning     | 10-60s (Kimi K2) |
| qwen-swarm   | Qwen3-Coder       | 10       | Agentic coding     | Variable         |

**Total Capacity**: 200+ concurrent agents

---

## Template Variables (For Orchestrators)

When using `prompt-template.yaml`, replace these:

```yaml
{identity}           # Agent unique ID (e.g., "codex-agent-001")
{model_name}         # Human-readable model name
{model_identifier}   # Technical identifier
{cli_command}        # CLI command to spawn
{skill_reference}    # Path to agent SKILL.md
{agent_type}         # Agent specialization
{task}               # Specific task from PRIME
{router_info}        # Routing information
{release_date}       # Model release date
{orchestrator_name}  # Which orchestrator spawned agent
```

---

## Frameworks Enforced (Universal)

Every spawned agent receives:

### RFC 2119 Compliance ✅

- MUST/SHALL = mandatory
- NEVER/FORBIDDEN = prohibited
- Full requirements language

### THE GOLDEN RULE ✅

8-step workflow (mandatory before coding)

### SOLID/DRY/KISS ✅

7 design principles (mandatory for all code)

---

## Summary

**Swarm Orchestrator** skill is your:

1. **Entry point** to THE SWARM → Activates PRIME protocol
2. **Template provider** for consistent agent spawning → Ensures quality

**Say "orchestrator"** → Activates PRIME → Access to 7 specialized orchestrators → Each enforces GOLDEN RULE + SOLID/DRY/KISS + RFC 2119

**Template in this directory** → Used by all 7 orchestrators → Guarantees consistent agent spawning

**Total parallel capacity**: 200+ agents across all 7 orchestrators

---

## Version History

| Version | Date       | Changes                                                                                                                                                                                                                        |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4.0.0   | 2025-11-02 | **CONSOLIDATION**: Merged orchestrator/, swarm-orchestrator-spawn-template/, and deprecated swarm-leader/ into single unified skill. Dual-purpose: PRIME entry point + universal spawn template. DRY/KISS principles enforced. |

---

_Version: 4.0.0 (November 2025)_
_Consolidates: orchestrator + swarm-orchestrator-spawn-template_
_Replaces: swarm-leader (deprecated)_
_See: .claude/commands/prime.md for complete PRIME protocol_
