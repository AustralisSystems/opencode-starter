---
name: AIDSL
description: Resolve AiDSL compound instruction verbs in YAML, JSON, or Markdown by using targeted line search against AGENTS_AI_DSL.yaml. Use this skill whenever the task involves interpreting or executing instruction-file directives expressed as all-caps verbs followed by a colon.
---

# AIDSL Skill

Use this skill to interpret `COMPOUND_INSTRUCTION_VERB`s in instruction files.

## When to use

- The user asks about AiDSL verb resolution, instruction-file execution, or parsing `ALL_CAPS` directives.
- The content contains `WORD_WITH_UNDERSCORES_IN_CAPS:` in YAML, JSON, or Markdown.
- You need to decide whether a token is an executable AiDSL verb or a structural label.

## Resolution rules

1. Only treat a token as an executable AiDSL verb when it is immediately followed by a colon `:`.
2. If the token has a `GATE_` prefix, do NOT resolve it via AiDSL; it is a checkpoint label.
3. If the token is a lowercase or structural YAML key, treat it as schema metadata, not an AiDSL verb.
4. If it is ALL_CAPS_WITH_UNDERSCORES and not one of the excluded structural cases, resolve it via `AGENTS_AI_DSL.yaml`.

## Search protocol

- Search `AGENTS_AI_DSL.yaml` for the exact compound key first.
- If the exact key is missing, search for each token separately and concatenate definitions in token order.
- If any token has zero matches, stop and report the missing token.
- Do NOT read `AGENTS_AI_DSL.yaml` in full; use targeted line search only.
- Ensure the search output is complete and untruncated.

## Structural exceptions

Do NOT perform AiDSL lookup for:

- `GATE_XXX:` identifiers (checkpoint block labels)
- `enforcement:`, `blocking:`, `condition:`, `action:`, and similar schema keys
- `SCENARIO_X_...:` or `STEP_N_...:` labels
- Named document section blocks like `SESSION_BOOTSTRAP:` or `RFC2119_REQUIREMENTS_LANGUAGE:`

## Nested instruction handling

- Treat nested compound verbs as parent → child hierarchy.
- The outer verb defines the scope.
- Inner verbs execute within that scope, in document order.
- Interpret scalar values as arguments, lists as operand collections, and mappings as named parameters or nested child verbs.

## Formal acknowledgement

- This skill also reflects the Bootstrap Step 4 formal acknowledgement from `AGENTS.md`.
- When the AIDSL skill is active, the model should hold these commitments as part of its session behavior:
  - It has loaded and understood `./AGENTS.md` and `./AGENTS.md.yaml`.
  - It has processed all `GATE_XXX` checkpoints from `AGENTS.md.yaml` in document order.
  - It will apply all directives, gates, and constraints for the remainder of the session.
  - It will resolve all `WORD_WITH_UNDERSCORES_IN_CAPS` using targeted line search only.
  - It will not weaken requirement levels.
  - If either authoritative directive file cannot be loaded, it must halt.

## Authoritative file map

- `./AGENTS.md` is the bootstrap loader and shim.
- `./AGENTS.md.yaml` is the authoritative directives source for gates, rules, and enforcement.
- `./AGENTS_AI_DSL.yaml` is the canonical AiDSL verb registry that must only be used via targeted line search.

## Forbidden behaviors

- Do NOT proceed with any task before completing BOOTSTRAP STEPS 1–4.
- Do NOT read `AGENTS_AI_DSL.yaml` in full.
- Do NOT treat `WORDS_WITH_UNDERSCORES_IN_CAPS` as plain English; resolve them through AiDSL line search.
- Do NOT weaken any requirement level from `AGENTS.md.yaml`.

## Example

Use this skill when processing instructions like:

```yaml
READ_AND_UNDERSTAND:
  TARGET: ./AGENTS.md.yaml
  THEN:
    VALIDATE:
      - "All GATE_XXX blocks have UNDERSTAND_AND_ACKNOWLEDGE"
```

In this example:

- `READ_AND_UNDERSTAND:` is an executable AiDSL verb.
- `TARGET:` is a named parameter.
- `THEN:` is a sequencing child verb.
- `VALIDATE:` is a nested AiDSL verb resolved within the parent scope.
