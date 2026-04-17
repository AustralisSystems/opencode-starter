# TOOLING_AND_MCP_WORKFLOW_DIRECTIVES

```yaml
TOOLING_AND_MCP_WORKFLOW_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true
  authoritative_source_protocol_reference: "agentic_code_engine/_ai_agent/instructions/002/code/002_1000_protocols/007-PROTOCOL-MCP_Tools_Workflow-v2.0.0.yaml"
  intent: "Defines how MCP tools and related validation tools MUST be used in this repo and during sessions."

  tool_research_and_execution_workflow:
    workflow_sequence: "context7 (docs) → grep (MCP GitHub code search tool; real-world examples) → memorygraph (record) → code → memorygraph (persist)"
    purpose: "Prevent hallucinations, ensure research-backed decisions, and promote knowledge persistence."
    adaptation_policy: "Workflow SHOULD be followed, but MAY be adapted based on task complexity and context."

    memory_store_policy:
      rule: "Agent persistent memory MUST use Memory (mcp server id: memory) as a memory backend."

    session_preflight_requirements:
      - "MUST retrieve the current time and timezone at the start of the task/session (prefer MCP time tools if available; otherwise use host time)."
      - "MUST treat model knowledge as time-bounded; if the model knowledge cutoff date is unknown OR the current date is > 30 days after the model knowledge cutoff, agents MUST perform the mandatory research step BEFORE writing or modifying production code."

    required_workflow_stages:
      - "Time Sync (time): Retrieve the current time and timezone (prefer MCP time tools; otherwise use host time)."
      - "Skill Inventory Scan (filesystem + read_file): Enumerate and review ALL available SKILLS across default and nominated locations (PROJECT_LOCAL, EXTRA_ROOTS, GLOBAL/USER) as the FIRST operational step BEFORE any other operations (including research, planning, coding, testing, or substantive response generation); then load/follow all applicable SKILL.md instructions."
      - "MUST use sequential-thinking to break tasks down into logical steps for non-trivial changes."
      - "MUST use a TODO list to plan and track progress for multi-step work."
      - "Context Load (memory): Retrieve relevant knowledge and patterns from previous sessions when appropriate."
      - "Knowledge Freshness Check (time): Compare current date/time against the model knowledge cutoff; if cutoff is unknown OR current date is > 30 days after cutoff, mandatory research MUST be performed BEFORE writing or modifying production code."
      - "Research (context7 + grep (MCP GitHub code search tool) + fetch/browser (MCP fetch + web search tools)): Fetch up-to-date official docs/release notes and real-world examples before implementation when appropriate."
      - "Planning (sequential-thinking): Break down implementation into structured reasoning steps."
      - "Implementation (filesystem + domain tools): Execute planned changes using dedicated file/editor operations."
      - "Progress Tracking (TODO list + memory): Track current state, milestones, and blockers."
      - "Context Save (memory): Persist significant learnings for future sessions."

  tool_usage_compliance_policies:
    required_practices:
      required_mcp_tool_usage:
        - "MUST retrieve the current time and timezone at the start of the task/session (prefer MCP time tools if available; otherwise use host time)."
        - "MUST use sequential-thinking to break tasks down into logical steps for non-trivial changes."
        - "MUST use MCP research tools (context7 + grep (MCP GitHub code search tool) + fetch/browser (MCP fetch + web search tools)) to validate assumptions against up-to-date sources BEFORE writing or modifying production code; this requirement is STRICT for security-sensitive work."
        - "MUST use browser automation tooling (e.g., Playwright and/or approved MCP browser automation tools) to validate web app behavior and ALL user flows when changes impact the Web App, UX or UI behavior."

      required_workflow_behaviors:
        - "MUST use a TODO list to plan and track progress for multi-step work."
        - "MUST NOT skip the research phase for security-sensitive code."
        - "MUST treat LLM knowledge as potentially stale; when implementing code that depends on external libraries/APIs/language features/best practices, agents MUST validate against up-to-date authoritative sources (e.g., official docs, release notes, vendor references) as of the execution date."

      file_editing_requirements:
        - "MUST NOT create/update files via terminal commands or ad-hoc scripts."
        - "MUST use dedicated file/editor operations for any action that creates new files or updates existing file content."

      skill_loading_requirements:
        - "Agents MUST perform a Skill Inventory Scan as the FIRST operational step at the start of each task/session BEFORE any other operations (including research, planning, coding, testing, or substantive response generation)."
        - 'Skill Inventory Scan MUST enumerate and review ALL available SKILLS in all default and nominated locations: PROJECT_LOCAL, EXTRA_ROOTS (AGENT_SKILLS_EXTRA_ROOTS and/or {{CODEBASE_DIR}}\.claude\skills.extra_roots), and GLOBAL/USER.'
        - "After the scan, when one or more skills apply to the current task, agents MUST load and follow each applicable skill's SKILL.md instructions BEFORE generating a substantive response or making code changes."
        - 'Agents MUST NOT invent, assume, or "freehand" skill guidance; when an applicable skill exists, its SKILL.md instructions MUST be treated as authoritative and MUST be followed.'

    recommended_workflow_behaviors:
      - "SHOULD load prior context at session start when resuming work or doing complex changes."
      - "SHOULD record significant decisions and findings as you work, and persist them at the end of the session."
      - "SHOULD validate understanding before implementation (codebase, docs, and examples) for complex changes."

    prohibited_workflow_behaviors:
      - "FORBIDDEN: starting any task/session without first capturing the current time and timezone (prefer MCP time tools if available; otherwise use host time)."
      - "FORBIDDEN: writing or modifying production code without completing the required Knowledge Freshness Check and mandatory research when cutoff is unknown or current date is > 30 days after cutoff."
      - "FORBIDDEN: skipping research for unfamiliar APIs (MUST research using context7 + grep (MCP GitHub code search tool))."
      - "FORBIDDEN: broad root-level scans that create unnecessary noise (e.g., directory trees over the entire repo) when a targeted search will do."
      - "FORBIDDEN: proceeding with research, planning, coding, testing, or substantive responses without first performing the Skill Inventory Scan when the skills system is available."
      - 'FORBIDDEN: inventing, assuming, or "freehand" skill guidance; when an applicable skill exists, its SKILL.md instructions are authoritative and MUST be followed.'
      - "FORBIDDEN: skipping sequential-thinking for non-trivial changes or skipping a TODO list for multi-step work."
      - "FORBIDDEN: creating/updating files via terminal commands, ad-hoc scripts, or manual shell redirection instead of dedicated file/editor operations."
      - "FORBIDDEN: using shell grep as a substitute for the MCP GitHub code search tool when real-world examples are required by this workflow."
      - "FORBIDDEN: skipping browser automation validation when changes impact the Web App, UX, or UI behavior."

  task_stage_tool_mapping:
    session_startup_stage:
      primary_tools: "time (get current time/timezone) + filesystem (skills inventory scan) + read_file (review SKILL.md) + memory (load context)"
      tool_selection_guidance: "MUST capture current time/timezone first; MUST scan/review all available SKILLS across configured locations before research/planning/coding; SHOULD load context from previous sessions when relevant."
    pre_implementation_stage:
      primary_tools: "time (knowledge freshness check) + context7 + grep (MCP GitHub code search tool) + fetch/browser (MCP fetch + web search tools)"
      tool_selection_guidance: "MUST validate assumptions against up-to-date authoritative sources before coding; MUST do mandatory research when cutoff is unknown or current date is > 30 days after cutoff."
    planning_stage:
      primary_tools: "sequential-thinking + TODO list"
      tool_selection_guidance: "MUST plan multi-step work with a TODO list; SHOULD plan complex features and refactors."
    skill_instruction_stage:
      primary_tools: "read_file (load applicable SKILL.md)"
      tool_selection_guidance: "When a skill applies, agents MUST load and follow SKILL.md instructions before substantive responses or code changes."
    implementation_stage:
      primary_tools: "filesystem (dedicated file/editor operations)"
      tool_selection_guidance: "MUST use dedicated file/editor operations (e.g., apply_patch / create_file / edit_notebook_file) for any file changes; MUST NOT modify files via terminal commands."
    web_validation_stage:
      primary_tools: "browser automation tools (e.g., Playwright and/or approved MCP browser automation tools)"
      tool_selection_guidance: "MUST validate web app behavior and impacted user flows end-to-end when changes affect the Web App, UX, or UI."

  GATE_MCP_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - TOOLING_AND_MCP_WORKFLOW_DIRECTIVES
      - "I MUST capture the current time and timezone at the start of every task or session."
      - "I MUST perform a Skill Inventory Scan as the FIRST operational step before any research, planning, coding, testing, or response generation."
      - "I MUST use sequential-thinking to break down non-trivial tasks into logical steps."
      - "I MUST use MCP research tools (context7 + grep + fetch/browser) to validate assumptions before writing or modifying production code."
      - "I MUST NOT create or update files via terminal commands or ad-hoc scripts."
      - "I MUST NOT invent or freehand skill guidance when an applicable SKILL.md exists."
      - "FORBIDDEN: skipping browser automation validation when changes impact the Web App, UX, or UI."
    THEN: CONTINUE

# ------------------------------------------------------------
## Agentic Code Engine Usage Directives

```
