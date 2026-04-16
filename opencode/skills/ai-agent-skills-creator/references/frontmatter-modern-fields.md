# Frontmatter Modern Fields Reference

Date: 2026-03-30
Applies to: ai-agent-skills-creator

This reference catalogs the full set of frontmatter fields used across major skill runtimes.
Use it when authoring, reviewing, or validating skill packages.

---

## Portable Minimum (All Runtimes)

These two fields are required and supported everywhere.

```yaml
name: my-skill-name
description: One or two sentences describing what this skill does and when to invoke it.
```

**Rules for `name`:**
- Lowercase hyphen-case only (e.g. `code-debug`, `fastapi-implement`)
- Maximum 64 characters (canonical limit; keep under 40 for readability)
- Must be unique within the skill library
- No underscores, spaces, or uppercase

**Rules for `description`:**
- Lead with trigger phrases and use-case context
- Must be specific enough to distinguish this skill from similar ones
- Avoid vague openers like "A skill that..." — state the action directly
- Recommended length: 1–3 sentences

---

## Anthropic (Claude Code / Cowork) Extended Fields

These fields are supported in Anthropic skill runtimes and enable invocation control,
context scoping, and execution behavior.

### Invocation Control

```yaml
# Controls whether the skill is triggered automatically by Claude
# or requires explicit user invocation (e.g. /skill-name)
invoke: auto | manual
```

- `auto` (default): Claude triggers the skill when the description matches
- `manual`: Skill only activates when explicitly called by name
- Use `manual` for high-impact, destructive, or confirmation-required workflows

```yaml
# Hide the skill from skill discovery and listings
# Useful for internal/scaffolding skills not intended for end users
hidden: true | false
```

### Tool and Permission Scoping

```yaml
# Restrict which tools this skill may use
# Reduces blast radius for skills that don't need broad access
tools:
  - read
  - edit
  - bash
  - web_search
```

```yaml
# Deny specific tools even if globally permitted
tools_deny:
  - write
  - bash
```

### Path Scoping

```yaml
# Limit skill activation to specific file paths or directories
# Claude will only apply the skill when context matches these paths
path_scope:
  - src/
  - tests/
```

### Agent and Context Mode

```yaml
# Request a specific agent or model tier for execution
agent: default | code | reasoning

# Control context window behavior
context_mode: focused | full
```

### Argument Hints

```yaml
# Declare expected arguments when skill is invoked manually
# Helps Claude understand required inputs without prompting
args:
  - name: target_file
    description: Path to the file to process
    required: true
  - name: output_format
    description: Output format (json or markdown)
    required: false
    default: markdown
```

### Shell and Environment

```yaml
# Set environment variables available during skill execution
env:
  LOG_LEVEL: info
  OUTPUT_DIR: ./outputs

# Override shell for bash-based skills
shell: bash | powershell | zsh
```

---

## OpenAI (Responses API / Hosted Skills) Fields

OpenAI skills use a versioned upload model with structured metadata.

```yaml
name: my-skill-name
description: What this skill does and when to use it.

# Versioning — critical for lifecycle management
version: "1.0.0"

# Explicit author attribution
author: team-name or email

# Safety classification for content policy enforcement
safety_level: standard | elevated | restricted
```

**Invocation:**
OpenAI hosted skills activate based on description match. There is no `invoke: manual` equivalent
in the current public API — manual invocation must be controlled via instruction framing in the skill body.

**Versioning discipline:**
- Increment `version` on every published change
- Use semantic versioning: MAJOR.MINOR.PATCH
- MAJOR: breaking changes to behavior or outputs
- MINOR: additive improvements
- PATCH: fixes and clarifications

---

## Google (Gemini Extensions / System Instructions)

Google Gemini does not use frontmatter-based skill packaging in the same sense.
Gemini skills are typically structured as system instruction blocks or extension configs.

When targeting Gemini or portable multi-vendor deployment, use only the portable minimum fields
and rely on the skill body for all behavioral guidance.

```yaml
# Portable minimum only for Gemini-targeted skills
name: my-skill-name
description: Clear trigger description for the skill.
```

---

## Compatibility Mode Guidance

| Field | Anthropic | OpenAI | Google | Portable |
|---|---|---|---|---|
| `name` | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| `description` | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| `version` | Optional | ✅ Recommended | Optional | Optional |
| `invoke` | ✅ Supported | ❌ Not supported | ❌ Not supported | ❌ Omit |
| `hidden` | ✅ Supported | ❌ Not supported | ❌ Not supported | ❌ Omit |
| `tools` / `tools_deny` | ✅ Supported | ❌ Not supported | ❌ Not supported | ❌ Omit |
| `path_scope` | ✅ Supported | ❌ Not supported | ❌ Not supported | ❌ Omit |
| `agent` | ✅ Supported | ❌ Not supported | ❌ Not supported | ❌ Omit |
| `args` | ✅ Supported | Partial | ❌ Not supported | ❌ Omit |
| `safety_level` | ❌ Not supported | ✅ Supported | ❌ Not supported | ❌ Omit |

**When runtime is unknown:** Use portable minimum only. Add a compatibility note in the skill body
indicating which extended fields should be applied per runtime.

---

## Validator Schema (Canonical)

The local `quick_validate.py` script uses this schema as its allowed field set.
Fields outside this list trigger a warning, not a hard failure, in permissive mode.

**Required fields:**
- `name`
- `description`

**Known optional fields (all runtimes combined):**
- `version`
- `author`
- `invoke`
- `hidden`
- `tools`
- `tools_deny`
- `path_scope`
- `agent`
- `context_mode`
- `args`
- `env`
- `shell`
- `safety_level`

**Unknown fields:** Warn in permissive mode. Fail in strict mode.

---

## Full Example: Anthropic Production Skill Frontmatter

```yaml
name: fastapi-implement
description: >
  Implement FastAPI endpoints, routers, and middleware following project conventions.
  Use when adding new routes, request/response models, or dependency injection patterns.
  Triggers on: "implement endpoint", "add route", "create FastAPI", "add middleware".
version: "2.1.0"
invoke: auto
tools:
  - read
  - edit
  - bash
path_scope:
  - src/api/
  - tests/api/
args:
  - name: endpoint_spec
    description: Natural language description or OpenAPI snippet for the endpoint to implement
    required: false
```

---

## Full Example: Portable Multi-Vendor Frontmatter

```yaml
name: code-debug
description: >
  Debug failing code by analyzing error messages, stack traces, and runtime behavior.
  Use when code throws exceptions, produces incorrect output, or fails tests.
  Triggers on: "debug", "fix error", "stack trace", "why is this failing".
version: "1.0.0"
author: digital-angels-team
# Note: add invoke: manual and tools scoping when deploying to Anthropic runtime.
# Note: add safety_level when deploying to OpenAI hosted skills.
```
