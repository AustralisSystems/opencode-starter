# AIDSL_INTERPRETATION_AND_EXECUTION_RULES

```yaml
AIDSL_INTERPRETATION_AND_EXECUTION_RULES:
  enforcement: MANDATORY
  blocking: true
  intent: >
    The full AiDSL (AI Domain Specific Language) verb dictionary and execution model
    is defined in the authoritative external file AGENTS_AI_DSL.yaml.
    Agents MUST NOT read that file wholesale. Instead, use on-demand targeted line search
    to resolve specific WORDS_WITH_UNDERSCORES_IN_CAPS encountered during execution.

  authoritative_aidsl_registry:
    verb_registry_file: "./AGENTS_AI_DSL.yaml"

  variable_interpolation_rules:
    rule: "Text wrapped in double curly braces (e.g., {{VARIABLE}}) indicates dynamic interpolation."
    resolution_order:
      - "Variables MUST be resolved against INPUTS (RUNTIME, STATIC, DEFAULTS) in that order."
      - "Variables using dot notation (e.g., {{INPUTS.STATIC.AUTHORITATIVE_DIRECTIVE_FILES}}) MUST traverse the structured definition."
      - "Variables MUST be fully resolved before the enclosing STEP executes."

  # ------------------------------------------------------------
  # ON-DEMAND AiDSL VERB RESOLUTION PROTOCOL
  # When you encounter a WORD_WITH_UNDERSCORES_IN_CAPS in any
  # instruction file, follow this 3-step lookup — do NOT read
  # the entire DSL file.
  # Use whatever line-search tool is available to you.
  # The tool MUST return complete, untruncated lines.
  # AiDSL definitions are ALWAYS on a single line —
  # one returned line = one complete definition.
  # ------------------------------------------------------------

  compound_verb_resolution_protocol:
    enforcement: MANDATORY
    blocking: true
    intent: >
      Resolve the meaning of any WORD_WITH_UNDERSCORES_IN_CAPS encountered in instruction
      files by targeted line search against AGENTS_AI_DSL.yaml. Never read the file whole.
      Use whatever line-search tool your environment provides. The tool MUST return complete,
      untruncated lines. AiDSL definitions are always on a single line — one line = one definition.
    lookup_order:
      - "1. AGENTS_AI_DSL.yaml — search for exact compound key"
      - "2. AGENTS_AI_DSL.yaml — token-by-token fallback if no compound match found"
      - "3. HALT if any token returns zero matches"

    step_1_split_compound_verb:
      action: "Split the compound verb on underscores to produce a token list."
      example:
        input: "READ_AND_UNDERSTAND"
        tokens: ["READ", "AND", "UNDERSTAND"]

    step_2_exact_verb_lookup:
      action: >
        Search AGENTS_AI_DSL.yaml for an exact compound verb key matching the full
        WORD_WITH_UNDERSCORES_IN_CAPS. All verbs are in the AiDSL_VERBS section.
        Use whatever line-search tool your environment provides. Tool MUST return complete lines.
      commands:
        bash: "grep -n 'READ_AND_UNDERSTAND:' ./AGENTS_AI_DSL.yaml"
        powershell: "Select-String -Path './AGENTS_AI_DSL.yaml' -Pattern 'READ_AND_UNDERSTAND:'"
        python: "[l.rstrip() for l in open('./AGENTS_AI_DSL.yaml') if 'READ_AND_UNDERSTAND:' in l]"
        generic: "Search for '<COMPOUND_VERB>:' in ./AGENTS_AI_DSL.yaml using any available line-search tool. Output MUST be complete lines."
      exact_verb_match_found:
        condition: "search returns ≥ 1 complete matching line"
        action: "Use that definition as the complete meaning. STOP."
        example_output: |
          234:  READ_AND_UNDERSTAND: "Load the specified targets into agent context prior to action. Do not modify files."
        interpretation: "READ_AND_UNDERSTAND = load into context without modifying files."

    step_3_token_lookup_fallback:
      condition: "STEP_2 returned zero matches."
      action: >
        Search AGENTS_AI_DSL.yaml for each individual token as a standalone key.
        Concatenate their definitions in token order to derive the compound meaning.
        Use whatever line-search tool your environment provides. Tool MUST return complete lines.
      commands:
        bash: |
          grep -n 'READ:' ./AGENTS_AI_DSL.yaml
          grep -n 'AND:' ./AGENTS_AI_DSL.yaml
          grep -n 'UNDERSTAND:' ./AGENTS_AI_DSL.yaml
        powershell: |
          Select-String -Path './AGENTS_AI_DSL.yaml' -Pattern 'READ:|AND:|UNDERSTAND:'
        python: |
          [l.rstrip() for l in open('./AGENTS_AI_DSL.yaml') if any(t in l for t in ['READ:', 'AND:', 'UNDERSTAND:'])]
        generic: "Search for each 'TOKEN:' separately in ./AGENTS_AI_DSL.yaml. Output MUST be complete lines."
      token_fallback_match_found:
        condition: "Individual token lines returned."
        concatenation_rule: "Apply all token definitions as a single unified instruction in token order."

    step_4_unresolvable_token_halt:
      condition: "Any token returns zero matches in AGENTS_AI_DSL.yaml."
      action: "HALT. Report the unresolvable token. Do NOT guess or infer its meaning."
      example: "PRESERVE_CHECKLIST_STATUS → PRESERVE not found → HALT and report."

    executable_colon_rule:
      enforcement: MANDATORY
      rule: "A COMPOUND_INSTRUCTION_VERB is ONLY an executable AiDSL directive when immediately followed by a colon ':'. Without a colon the word is a reference or mention — NOT an instruction to execute."
      examples:
        executable: "READ_AND_UNDERSTAND: ./file.yaml   → ✅ colon present — look up and execute"
        reference: "READ_AND_UNDERSTAND (no colon)    → ℹ️ reference only — do NOT execute"
      excluded_from_lookup:
        - "GATE_XXX: identifiers (e.g., GATE_IIL_001:) — checkpoint block labels, processed under Bootstrap Step 2"
        - "Lowercase-starting YAML keys (enforcement:, blocking:, condition:, action:, commands:) — structural schema fields"
        - "SCENARIO_X_ / STEP_N_ prefixed labels — documentation structure only"
        - "Named document section blocks (SESSION_BOOTSTRAP:, RFC2119_REQUIREMENTS_LANGUAGE:) — section labels, not instructions"

    nested_verb_execution_hierarchy:
      enforcement: MANDATORY
      rule: "When COMPOUND_INSTRUCTION_VERB: keys are nested inside other COMPOUND_INSTRUCTION_VERB: blocks, interpret the nesting as a parent-to-child execution hierarchy. The outer (parent) verb executes first and establishes scope. Inner (child) verbs execute within that scope in document order. Nesting depth equals execution scope depth."
      value_type_interpretation:
        scalar: "The primary argument or target for the parent verb."
        list: "Multiple operands, targets, or conditions for the parent verb."
        mapping: "Named parameters OR further nested child instruction verbs. Resolve each ALL_CAPS key via AiDSL."
      example: |
        READ_AND_UNDERSTAND:          # parent: load into context
          TARGET: ./AGENTS.md.yaml   # named parameter
          THEN:                       # child: runs after parent completes
            VALIDATE:                 # grandchild: runs within THEN scope
              - "condition one"

  FORBIDDEN:
    - "Reading AGENTS_AI_DSL.yaml in full — use targeted line search only."
    - "Guessing or inferring the meaning of an unresolvable token — HALT and report."
    - "Treating WORDS_WITH_UNDERSCORES_IN_CAPS as natural-language phrases — resolve via AiDSL line search protocol."

  GATE_IIL_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - AIDSL_INTERPRETATION_AND_EXECUTION_RULES
      - "I MUST treat ALL_CAPS words as specific, actionable intent markers mapped to AiDSL operational verbs."
      - "I MUST resolve all {{VARIABLE}} interpolations against INPUTS before executing any STEP."
      - "I MUST treat UNDERSTAND_AND_ACKNOWLEDGE as a formal commitment to apply loaded directives for the remainder of the session."
      - "I MUST treat READ_AND_UNDERSTAND as load-into-context; I MUST NOT modify files during READ_AND_UNDERSTAND."
      - "I MUST resolve WORDS_WITH_UNDERSCORES_IN_CAPS by targeted line search against ./AGENTS_AI_DSL.yaml — never reading the file in full. The tool used MUST return complete, untruncated lines."
      - "I MUST only treat a WORD_WITH_UNDERSCORES_IN_CAPS as an executable AiDSL verb when it is immediately followed by a colon ':' — without a colon it is a reference, not an instruction."
      - "I MUST NOT attempt AiDSL lookup for GATE_XXX identifiers, lowercase YAML structural keys, SCENARIO_/STEP_-prefixed labels, or named document section blocks."
      - "I MUST interpret nested COMPOUND_INSTRUCTION_VERB: blocks as a parent → child execution hierarchy — outer verb acts first and establishes scope; inner verbs execute within that scope in document order."
    THEN: CONTINUE

## App and Codebase Architecture Directives

```
