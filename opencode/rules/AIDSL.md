# AiDSL Verb Resolution

This rule captures the AiDSL verb resolution protocol from `AGENTS.md` and `AGENTS.md.yaml`.

## When to apply

- Apply this rule when processing instruction files in YAML, JSON, or Markdown.
- A `WORD_WITH_UNDERSCORES_IN_CAPS` followed immediately by a colon `:` is a candidate **compound instruction verb**.
- Only treat it as an executable AiDSL directive when the colon is present.

## What counts as a directive

- `READ_AND_UNDERSTAND:` → executable AiDSL verb, look up and perform.
- `READ_AND_UNDERSTAND` (no colon) → reference only, not executable.

## What is NOT an AiDSL lookup

Do NOT attempt AiDSL lookup for:

- `GATE_XXX:` prefix labels, such as `GATE_IIL_001:`. These are checkpoint block labels processed by Bootstrap Step 2.
- Lowercase-starting YAML keys such as `enforcement:`, `blocking:`, `condition:`, `action:`.
- `SCENARIO_X_...:` or `STEP_N_...:` labels.
- Named document section blocks such as `SESSION_BOOTSTRAP:`, `RFC2119_REQUIREMENTS_LANGUAGE:`.

## Decision rule

1. If the token matches a `GATE_` prefix, do NOT look it up in AiDSL.
2. If the token is a lowercase or structural YAML key, treat it structurally.
3. Otherwise, if the token is ALL_CAPS_WITH_UNDERSCORES and followed by `:`, look it up in `AGENTS_AI_DSL.yaml`.

## Lookup order

1. Search `AGENTS_AI_DSL.yaml` for the exact compound verb key (e.g. `READ_AND_UNDERSTAND:`).
2. If no exact match is found, search for each token separately and concatenate their definitions in token order.
3. If any token returns zero matches, halt and report the unresolvable token. Do NOT guess.

## Search requirements

- Do NOT read `AGENTS_AI_DSL.yaml` in full.
- Use targeted line search only.
- The search tool must return complete, untruncated lines.
- AiDSL definitions are always on a single line.

## Formal acknowledgement

- When applying AiDSL resolution in this repo, the agent should also internalize the Bootstrap Step 4 acknowledgements from `AGENTS.md`.
- The agent must treat the following commitments as active for the remainder of the session:
  - It has loaded and understood `./AGENTS.md` and `./AGENTS.md.yaml`.
  - It has processed all `GATE_XXX` checkpoints from `AGENTS.md.yaml` in document order.
  - It will apply all directives, gates, and constraints for the remainder of this session.
  - It will resolve all `WORD_WITH_UNDERSCORES_IN_CAPS` using targeted line search — never by reading the AiDSL file whole.
  - It will not weaken requirement levels.
  - If `AGENTS.md` or `AGENTS.md.yaml` cannot be loaded, it must halt.

## Nested verb hierarchy

- When a compound instruction verb is nested inside another, interpret it as a parent → child execution hierarchy.
- The outer verb establishes scope first; inner verbs execute in document order within that scope.
- Use the value type under the verb to interpret intent:
  - Scalar = primary argument/target.
  - List = multiple operands or conditions.
  - Mapping = named parameters or nested child verbs.

## Key principle

- Never infer or invent the meaning of an AiDSL verb.
- Always resolve via the explicit line-search protocol against `AGENTS_AI_DSL.yaml`.

## Authoritative files and forbidden behaviors

- `./AGENTS.md` is the bootstrap loader and shim.
- `./AGENTS.md.yaml` is the authoritative directives source for gates, rules, and enforcement.
- `./AGENTS_AI_DSL.yaml` is the canonical AiDSL verb registry; use it only via targeted line search.

**Forbidden when using this rule:**

- Proceeding with any task before completing BOOTSTRAP STEPS 1–4.
- Reading `AGENTS_AI_DSL.yaml` in full.
- Treating `WORDS_WITH_UNDERSCORES_IN_CAPS` as plain English instead of resolving them via AiDSL line search.
- Weakening any requirement level from `AGENTS.md.yaml`.
