# SKILL_DISCOVERY_AND_EXECUTION_DIRECTIVES

```yaml
SKILL_DISCOVERY_AND_EXECUTION_DIRECTIVES:
  enforcement: MANDATORY
  gate_id: skill_discovery_and_execution_directives
  requires_immediate_action: true
  blocking: true

  intent: "Define mandatory skill discovery, precedence resolution, and SKILL.md execution behavior for agents operating in this repo."

  authoritative_scope: "This section governs skill discovery, precedence, and mandatory execution behavior for agents operating in this repo."

  skill_definition_notes:
    - Skills are instruction bundles stored as folders containing a SKILL.md file.
    - A skill "exists" only if the file <skill-name>/SKILL.md exists at the expected location.

  skill_lookup_location_precedence:
    - location_id: PROJECT_LOCAL
      windows_lookup_path: '{{CODEBASE_DIR}}\.claude\skills\<skill-name>\SKILL.md'
    - location_id: EXTRA_ROOTS
      description: For each directory listed in AGENT_SKILLS_EXTRA_ROOTS, look for <root>/<skill-name>/SKILL.md
      required_when_environment_variable_is_set: true
    - location_id: GLOBAL_USER
      windows_lookup_path: '%USERPROFILE%\.agents\skills\<skill-name>\SKILL.md'
      linux_macos_lookup_path: "$HOME/.agents/skills/<skill-name>/SKILL.md"

  extra_skill_root_configuration:
    environment_variable_name: AGENT_SKILLS_EXTRA_ROOTS
    path_list_separators:
      windows: ";"
      linux_macos: ":"
    lookup_order: in_order_provided

  extra_skill_root_config_file:
    config_file_path: '{{CODEBASE_DIR}}\.claude\skills.extra_roots'
    file_format: one_absolute_path_per_line
    ignore_blank_lines: true
    comment_prefix: "#"
    precedence_insertion_point: between_PROJECT_LOCAL_and_GLOBAL_USER
    combine_with_environment_variable: true
    combined_lookup_order:
      - config_file_top_to_bottom
      - environment_variable_left_to_right

  skill_resolution_rules:
    precedence_rule: Highest-precedence location wins (PROJECT-LOCAL, then EXTRA ROOTS, then GLOBAL/USER).
    applicability_rule: A skill applies when the user's request matches the skill's described domain.
    execution_rule: For each applicable skill, locate/read/comply with SKILL.md BEFORE taking action; if multiple skills apply, load/follow ALL of them.

  YOU_MUST:
    - rule: "Skill Inventory Scan is mandatory."
      requirements:
        - "Agents MUST perform a Skill Inventory Scan as the FIRST operational step at the start of each task/session BEFORE any other operations (including research, planning, coding, testing, or substantive response generation)."
        - 'Skill Inventory Scan MUST enumerate and review ALL available SKILLS in all default and nominated locations: PROJECT_LOCAL, EXTRA_ROOTS (AGENT_SKILLS_EXTRA_ROOTS and/or {{CODEBASE_DIR}}\.claude\skills.extra_roots), and GLOBAL/USER.'
    - rule: "Applicable skills MUST be identified and followed."
      requirements:
        - "Agents MUST determine whether one or more skills apply BEFORE generating a substantive response or making code changes."
        - "When skills apply, agents MUST locate SKILL.md using the precedence order (PROJECT-LOCAL, then EXTRA ROOTS, then GLOBAL/USER) and use the first match."
        - "Agents MUST read and comply with each applicable skill's SKILL.md BEFORE proceeding; if multiple skills apply, agents MUST load and follow ALL of them."
    - rule: "Skill existence and precedence MUST be enforced."
      requirements:
        - "Agents MUST treat a skill as available only when <skill-name>/SKILL.md is present; agents MUST NOT assume a skill exists based on folder name alone."
        - "If a skill exists in multiple locations, agents MUST use the highest-precedence version; agents MUST NOT mix instructions from lower-precedence duplicates."
    - rule: "Skill discovery fallback MUST be deterministic."
      requirements:
        - "If skill discovery is not supported by the host runtime (IDE/CLI), agents MUST implement discovery manually by checking the locations in precedence order."
    - rule: "Skill guidance MUST NOT be invented."
      requirements:
        - 'Agents MUST NOT invent, assume, or "freehand" skill guidance; when an applicable skill exists, its SKILL.md instructions MUST be treated as authoritative and MUST be followed.'
        - "If no applicable skill exists, agents MUST proceed without inventing skill guidance."

  YOU_SHOULD:
    - rule: "Prefer higher-signal skill sources."
      guidance:
        - "Agents SHOULD prefer PROJECT-LOCAL skills for repo-specific conventions."
        - "Agents SHOULD treat GLOBAL/USER skills as general-purpose defaults."
    - rule: "Keep skill roots deterministic."
      guidance:
        - "Agents SHOULD keep AGENT_SKILLS_EXTRA_ROOTS and skills.extra_roots deterministic and minimal to reduce ambiguity and conflicting skill definitions."
    - rule: "Improve auditability and reuse."
      guidance:
        - "Agents SHOULD state (briefly) which skills were loaded when helpful for auditability or handover."
        - "Agents SHOULD update or create a PROJECT-LOCAL skill when repeated work reveals missing guidance that would benefit future agents."

  GATE_SKL_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - SKILL_DISCOVERY_AND_EXECUTION_DIRECTIVES
      - "I MUST perform a Skill Inventory Scan as the FIRST operational step before any research, planning, coding, testing, or substantive response generation."
      - "I MUST scan ALL available SKILLS across PROJECT_LOCAL, EXTRA_ROOTS, and GLOBAL/USER locations."
      - "I MUST read and comply with each applicable skill's SKILL.md BEFORE proceeding; if multiple skills apply, I MUST load and follow ALL of them."
      - "I MUST NOT invent, assume, or freehand skill guidance; when an applicable SKILL.md exists, it is authoritative."
    THEN: CONTINUE

# ------------------------------------------------------------
## ACE Capability and Gate Execution Profile

```
