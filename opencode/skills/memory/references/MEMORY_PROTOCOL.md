# Memory Protocol Reference

This file carries the full authoritative content from the repository-level `MEMORY.md`.

```markdown
# ------------------------------------------------------------

# Memory Protocol (Authoritative: 2024-06)

# ------------------------------------------------------------

MEMORY_MCP_PROTOCOL:
enforcement: MANDATORY
gate_id: memory_mcp_protocol_root
requires_immediate_action: true
blocking: true
authoritative_scope: >
Governs memory recall/store/relationship/compaction/pruning behaviors for all agents.
This protocol MUST be referenced by repo instructions and AGENTS.md.

# ------------------------------------------------------------

# Gate interpretation rule (aligns with repo standard)

# ------------------------------------------------------------

gate_interpretation_rule:
enforcement: MANDATORY
gate_id: memory_gate_interpretation_rule
requires_immediate_action: true
blocking: true
rule: "Agents MUST report failures using gate_id and MUST halt on any blocking gate."

# ------------------------------------------------------------

# Tool contract

# ------------------------------------------------------------

tools:
enforcement: MANDATORY
gate_id: memory_tools_contract
requires_immediate_action: true
blocking: true
required: - recall_memories - search_memories - store_memory - edit_memory - traverse_memories - generate_mermaid_graph - list_domains - select_domain
rules: - "Memory operations MUST use MemoryGraph MCP (server id: memory)." - "Do NOT rely on broad context. Use memory tools and scoped queries."

# ------------------------------------------------------------

# Query Scoping Policy (NARROW-FIRST)

# ------------------------------------------------------------

query_policy:
enforcement: MANDATORY
gate_id: memory_query_scope_gate
requires_immediate_action: true
blocking: true

    intent: "Minimize tokens and maximize relevance. Do NOT do broad queries."
    hard_rules:
      - "FORBIDDEN: broad/unscoped queries"
      - "MUST filter by repo_id (or repo_name) + project + task_type/category"
      - "MUST use time windows: last_24_hours then last_48_hours"
      - "MAY expand beyond 48h ONLY if results are empty AND justification is recorded"

    time_windows:
      initial:
        - last_24_hours
        - last_48_hours
      expansion_sequence:
        - last_7_days
        - last_30_days

    required_filters:
      - repo_id_or_repo_name
      - project
      - task_type_or_category

    example_templates:
      recall_before_task:
        tool: recall_memories
        params:
          time_window: last_24_hours
          filters:
            repo_id: "{repo_id}"
            project: "{project}"
            task_type: "{task_type}"
      recall_before_task_fallback:
        tool: recall_memories
        params:
          time_window: last_48_hours
          filters:
            repo_id: "{repo_id}"
            project: "{project}"
            task_type: "{task_type}"

# ------------------------------------------------------------

# Mandatory Pre-Work Recall

# ------------------------------------------------------------

preflight_recall:
enforcement: MANDATORY
gate_id: memory_preflight_recall_gate
requires_immediate_action: true
blocking: true

    rule: "Before starting ANY task, you MUST run recall_memories using the scoped query policy."
    stop_conditions:
      - "If recall_memories was not run: execution MUST STOP."
      - "If filters are missing (repo/project/task_type): execution MUST STOP and correct the query."

# ------------------------------------------------------------

# Memory Storage Triggers (Individual + Team)

# ------------------------------------------------------------

storage_policy:
enforcement: MANDATORY
gate_id: memory_storage_policy_gate
requires_immediate_action: true
blocking: true

    intent: >
      Store concise, detailed, traceable entries and link them with relationships to form a navigable graph.
      Entries must be token-efficient but action-oriented.

    timing_modes:
      memory_mode:
        allowed: [immediate, on-commit, session-end]
        default: on-commit

    triggers:
      - event: git_commit
        requirement: "MUST store what was fixed/added + outcome + refs"
      - event: bug_fix
        requirement: "MUST store problem + solution + validation"
      - event: version_release
        requirement: "MUST store release summary + impact"
      - event: architecture_decision
        requirement: "MUST store decision + rationale + tradeoffs"
      - event: pattern_discovered
        requirement: "MUST store reusable pattern + where it applies"
      - event: implementation
        requirement: "MUST store capability/service/feature/function + purpose + outcome"
      - event: validation
        requirement: "MUST store status + synopsis + outcome + evidence"
      - event: integration_testing
        requirement: "MUST store status + synopsis + outcome + evidence"
      - event: end_to_end_testing
        requirement: "MUST store status + synopsis + outcome + evidence"

# ------------------------------------------------------------

# Memory Node Schema (metadata-heavy for queryability)

# ------------------------------------------------------------

memory_schema:
enforcement: MANDATORY
gate_id: memory_schema_gate
requires_immediate_action: true
blocking: true

    required_fields:
      type:
        allowed: [solution, problem, code_pattern, fix, error, workflow, task, decision, release, test_result, snapshot, rollup]
      title:
        rules:
          - "MUST be specific and searchable"
          - "MUST include an identifier when possible (error signature, endpoint, module, PR/issue)"
      content:
        rules:
          - "MUST be concise but detailed"
          - "MUST include: context + what + why + outcome"
          - "MUST include actionable steps when relevant"
      tags:
        rules:
          - "REQUIRED: project, tech, category"
          - "REQUIRED: repo_id (or repo_name) + date"
          - "REQUIRED: author for team entries"
      metadata:
        required:
          - created_at   # ISO-8601
          - updated_at   # ISO-8601
          - repo_id
          - repo_name
          - timezone
        optional_traceability:
          - commit_sha
          - pr_number
          - issue_id
          - incident_id
          - release_version
          - environment
          - services
          - components
          - technologies
          - verification_signals

# ------------------------------------------------------------

# Relationship / Edge Governance (mind-map quality)

# ------------------------------------------------------------

relationships:
enforcement: MANDATORY
gate_id: memory_relationships_gate
requires_immediate_action: true
blocking: true

    intent: "Convert memory entries into a navigable mind map with consistent edge semantics."
    edge_types:
      - SOLVES
      - ADDRESSES
      - TRIGGERS
      - CAUSES
      - APPLIES_TO
      - IMPROVES
      - REPLACES
      - VALIDATES
      - SUPERSEDED_BY
      - RELATED_TO

    canonical_patterns:
      - pattern: "solution SOLVES problem"
      - pattern: "fix ADDRESSES error"
      - pattern: "error TRIGGERS problem"
      - pattern: "code_pattern APPLIES_TO project/component/service"
      - pattern: "decision IMPROVES previous_approach"
      - pattern: "test_result VALIDATES fix/solution"

    enforcement_rules:
      - "If a related node exists, you MUST create the edge (no orphan solutions)."
      - "Use RELATED_TO sparingly; prefer specific edges."
      - "Edges MUST include edge_metadata: created_at, author, repo_id, evidence(if any)."

# ------------------------------------------------------------

# Graph Compaction Mode (dedupe + canonical IDs + snapshots)

# ------------------------------------------------------------

graph_compaction_mode:
enforcement: MANDATORY
gate_id: memory_graph_compaction_gate
requires_immediate_action: true
blocking: true

    enabled: true
    trigger_modes: [on_store, on_commit, session_end, scheduled]
    canonical_id:
      rule: "MUST assign canonical ids for dedupe and stable linking."
      format: "mem:{repo_id}:{type}:{primary_key}:{date_bucket}"

    dedupe_rules:
      - "MUST check duplicates using scoped queries (24h then 48h) before creating new nodes."
      - "If duplicate found, MUST edit/merge rather than create new."
      - "MUST preserve evidence and rewire edges to canonical node."
      - "Default is archive merged nodes; prune only under pruning policy."

    snapshots:
      rule: "At session_end, MUST create daily snapshot nodes linking to touched nodes."
      types: [daily, weekly, monthly, release]

# ------------------------------------------------------------

# Pruning + Long-Horizon Merging (time + relevance)

# ------------------------------------------------------------

pruning_and_merging_mode:
enforcement: MANDATORY
gate_id: memory_pruning_merging_gate
requires_immediate_action: true
blocking: true

    enabled: true
    non_destructive_preference: true
    default_to_archive_over_delete: true

    relevance_model:
      rule: "Pruning MUST be based on time + relevance, not time alone."
      features:
        - recency
        - access_frequency
        - importance
        - link_density
        - verification_strength
        - critical_type_bonus
      thresholds:
        retain: 0.70
        merge: 0.40
        prune_candidate: 0.25

    never_prune_if:
      - "importance >= 0.8"
      - "node_type in [decision, code_pattern, incident, release, security_fix, validated_fix]"
      - "edge_degree >= 3"
      - "has_verification_signals == true"

    prune_only_if_all_true:
      - "relevance_score <= 0.25"
      - "edge_degree <= 1"
      - "represented_in_rollup == true"
      - "no_open_incident_or_active_issue_links == true"

    rollups:
      rule: "Older low/medium relevance nodes MUST be merged into rollups before prune."
      scopes: [repo, project, component, service, release_version]
      periods: [weekly, monthly, release]

# ------------------------------------------------------------

# Session-end Summary (mandatory)

# ------------------------------------------------------------

session_end:
enforcement: MANDATORY
gate_id: session_end_memory_summary_gate
requires_immediate_action: true
blocking: true

    requirement: "At end of session, MUST store a task summary with what's next and correct tags."
    store_action:
      tool: store_memory
      params:
        type: task
        tags_required:
          - project:{project}
          - repo_id:{repo_id}
          - date:{YYYY-MM-DD}
          - author:{author}
        content_must_include:
          - accomplishments
          - next_steps
          - verification_signals_if_any
          - refs_commit_pr_issue_if_any
```
