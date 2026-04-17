# N8N WORKFLOW COMMAND REWRITE PLAN

**Generated:** 2025-10-02-110029 UTC

## Executive Summary

This document provides the comprehensive plan for rewriting all 8 n8n workflow development command pairs from their current Node.js framework focus to a complete n8n workflow lifecycle management focus.

## Current State Analysis

### Existing Commands (Node.js Focus)

1. **n8n-workflow-planning.md** - Node.js framework selection and planning
2. **n8n-workflow-design.md** - Backend architecture design
3. **n8n-workflow-implementation.md** - Node.js implementation
4. **n8n-workflow-lint-quality-check.md** - Code linting and quality
5. **n8n-workflow-quality-analysis.md** - Code quality analysis
6. **n8n-workflow-review.md** - Code review
7. **n8n-workflow-refactor.md** - Code refactoring
8. **n8n-workflow-gap-analysis.md** - Requirements gap analysis

### Target State (n8n Workflow Focus)

All commands will be transformed to focus on the complete n8n workflow development lifecycle, from planning through deployment and maintenance.

## N8N Workflow Lifecycle Mapping

### Phase 1: Planning & Discovery

**Command:** n8n-workflow-planning.md

- Template discovery (2,500+ templates)
- Requirements analysis
- Node selection strategy
- Architecture planning

### Phase 2: Design & Configuration

**Command:** n8n-workflow-design.md

- Node configuration design
- Connection architecture
- Expression planning
- Error handling design

### Phase 3: Implementation & Deployment

**Command:** n8n-workflow-implementation.md

- Workflow building
- Validation execution
- Deployment to n8n
- Post-deployment testing

### Phase 4: Quality Assurance

**Commands:** n8n-workflow-lint-quality-check.md + n8n-workflow-quality-analysis.md

- Expression validation
- Connection validation
- Complexity analysis
- Performance analysis

### Phase 5: Review & Optimization

**Commands:** n8n-workflow-review.md + n8n-workflow-refactor.md

- Structure review
- Security review
- Performance optimization
- Refactoring execution

### Phase 6: Assessment & Maintenance

**Command:** n8n-workflow-gap-analysis.md

- Requirements coverage
- Testing gaps
- Production readiness

## Standard File Structure

### .MD File Template Structure

```markdown
# [Command Name]

**YAML Prompt**: `[yaml-file-name].yaml`

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

[Standard compliance section]

## Purpose

[n8n workflow-specific purpose]

## MCP Tool Requirements

- context7 - Latest n8n documentation
- grep - Real-world workflow examples
- sequential-thinking - Structured approach
- filesystem - Workflow file operations
- memory - Progress tracking
- time - Timestamp operations
- [n8n-specific MCP tools]

## [Phase-Specific Sections]

[Content specific to workflow lifecycle phase]

### Template-First Workflow Strategy

[Template discovery and usage patterns]

### Node Discovery Strategy

[Progressive node discovery approach]

### Validation Strategy

[Validate early and often patterns]

### MCP Workflow Integration

[How to use n8n MCP tools]

## Deliverables

[Specific deliverables with YYYY-MM-DD-HHMMSS timestamps]

## Success Criteria

- [ ] Checklist items

## Command Integration

- **Previous Phase**: [previous-command]
- **Next Phase**: [next-command]

## Next Phase Preparation

[Command examples for next phase]
```

### .YAML File Template Structure

```yaml
name: "[Command Name]"
description: "[n8n workflow description]"
version: "2.1.0"
category: "[lifecycle-phase]"

mcp_requirements:
  mandatory_tools:
    - context7
    - grep
    - sequential-thinking
    - filesystem
    - memory
    - time
    - [n8n-specific tools]

n8n_context:
  workflow_types:
    [automation|integration|data-processing|webhook|scheduled|event-driven]
  complexity_levels: [simple|intermediate|advanced|enterprise]
  template_usage: [template-first|hybrid|custom-build]

execution_phases:
  1_phase_name:
    description: ""
    tools: []
    required_actions: []
    success_criteria: []

n8n_parameters:
  template_discovery: {}
  node_selection: {}
  validation_strategy: {}

deliverables:
  document_count: N
  document_types: []

success_criteria:
  category: []

related_commands:
  previous: ""
  next_phase: ""
```

## Detailed Command Specifications

### 1. N8N-WORKFLOW-PLANNING

**Purpose:** Strategic planning for n8n workflow development

**Key Sections:**

- Workflow Requirements Analysis
- Template Discovery Strategy (search_templates_by_metadata, get_templates_for_task)
- Node Selection Matrix
- Architecture Planning
- Implementation Roadmap

**MCP Tools:**

- search_templates / search_templates_by_metadata / get_templates_for_task
- search_nodes / list_nodes / list_ai_tools
- tools_documentation
- Standard tools (context7, grep, sequential-thinking, filesystem, memory, time)

**Deliverables:**

1. Workflow_Requirements_Analysis_YYYY-MM-DD-HHMMSS.ipynb
2. Template_and_Node_Selection_YYYY-MM-DD-HHMMSS.ipynb
3. Workflow_Architecture_Plan_YYYY-MM-DD-HHMMSS.ipynb
4. Implementation_Roadmap_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Requirements clearly documented
- [ ] Templates evaluated and selected
- [ ] Nodes mapped to requirements
- [ ] Architecture design complete
- [ ] Implementation phases defined

---

### 2. N8N-WORKFLOW-DESIGN

**Purpose:** Detailed workflow architecture design

**Key Sections:**

- Node Configuration Design (get_node_essentials for each node)
- Connection Architecture (data flow mapping)
- Expression Planning (data transformation)
- Error Handling Design
- Pre-Validation (validate_node_minimal)

**MCP Tools:**

- get_node_essentials / get_node_for_task / search_node_properties
- get_property_dependencies / get_node_documentation
- validate_node_minimal / validate_node_operation
- Standard tools

**Deliverables:**

1. Node_Configuration_Design_YYYY-MM-DD-HHMMSS.ipynb
2. Connection_Architecture_YYYY-MM-DD-HHMMSS.ipynb
3. Expression_and_Data_Mapping_YYYY-MM-DD-HHMMSS.ipynb
4. Error_Handling_Strategy_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] All nodes configured with validated parameters
- [ ] Connection map complete and validated
- [ ] Expressions designed and syntax-checked
- [ ] Error handling strategy defined
- [ ] Pre-validation passed

---

### 3. N8N-WORKFLOW-IMPLEMENTATION

**Purpose:** Build and deploy workflows using n8n MCP tools

**Key Sections:**

- Template Customization (get_template if using template)
- Workflow Building (construct nodes and connections)
- Validation Execution (validate_workflow, validate_workflow_connections, validate_workflow_expressions)
- Deployment (n8n_create_workflow, n8n_validate_workflow)
- Post-Deployment Testing

**MCP Tools:**

- get_template
- validate_workflow / validate_workflow_connections / validate_workflow_expressions
- n8n_create_workflow / n8n_validate_workflow / n8n_update_partial_workflow
- n8n_trigger_webhook_workflow / n8n_list_executions
- Standard tools

**Deliverables:**

1. Workflow_Build_Log_YYYY-MM-DD-HHMMSS.ipynb
2. Validation_Results_YYYY-MM-DD-HHMMSS.ipynb
3. Deployment_Report_YYYY-MM-DD-HHMMSS.ipynb
4. Testing_Results_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Workflow built successfully
- [ ] All validations passed
- [ ] Deployed to n8n instance (if configured)
- [ ] Post-deployment validation successful
- [ ] Test executions completed

---

### 4. N8N-WORKFLOW-LINT-QUALITY-CHECK

**Purpose:** Workflow linting and validation

**Key Sections:**

- Expression Validation (validate_workflow_expressions)
- Connection Validation (validate_workflow_connections)
- Node Configuration Lint (validate_node_operation)
- Workflow Structure Lint (validate_workflow)
- System Diagnostics (n8n_diagnostic)

**MCP Tools:**

- validate_workflow_expressions / validate_workflow_connections / validate_workflow
- validate_node_operation
- n8n_diagnostic / n8n_health_check
- Standard tools

**Deliverables:**

1. Expression_Validation_Report_YYYY-MM-DD-HHMMSS.ipynb
2. Connection_Validation_Report_YYYY-MM-DD-HHMMSS.ipynb
3. Node_Lint_Results_YYYY-MM-DD-HHMMSS.ipynb
4. System_Diagnostic_Report_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] All expressions validated (no syntax errors)
- [ ] All connections validated
- [ ] All nodes pass configuration validation
- [ ] Workflow passes comprehensive validation
- [ ] System health check passed

---

### 5. N8N-WORKFLOW-QUALITY-ANALYSIS

**Purpose:** Comprehensive quality analysis

**Key Sections:**

- Complexity Analysis (node count, connection depth, branching)
- Performance Analysis (execution patterns, bottlenecks)
- Best Practices Compliance (template attribution, error handling)
- Execution History Analysis (n8n_list_executions)
- Database Statistics (get_database_statistics)

**MCP Tools:**

- get_database_statistics
- n8n_list_executions
- n8n_get_workflow_structure
- Standard tools

**Deliverables:**

1. Complexity_Analysis_Report_YYYY-MM-DD-HHMMSS.ipynb
2. Performance_Analysis_Report_YYYY-MM-DD-HHMMSS.ipynb
3. Best_Practices_Compliance_YYYY-MM-DD-HHMMSS.ipynb
4. Quality_Metrics_Dashboard_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Complexity metrics calculated
- [ ] Performance analysis complete
- [ ] Best practices compliance verified
- [ ] Execution history analyzed
- [ ] Quality recommendations provided

---

### 6. N8N-WORKFLOW-REVIEW

**Purpose:** Workflow code review

**Key Sections:**

- Structure Review (organization, naming, clarity)
- Security Review (credentials, secrets, input validation)
- Expression Review (logic, error handling)
- Best Practices Review (attribution, documentation)
- Optimization Opportunities

**MCP Tools:**

- n8n_get_workflow / n8n_get_workflow_structure
- validate_workflow
- n8n_list_executions
- Standard tools (context7 for best practices, grep for examples)

**Deliverables:**

1. Structure_Review_Report_YYYY-MM-DD-HHMMSS.ipynb
2. Security_Review_Report_YYYY-MM-DD-HHMMSS.ipynb
3. Expression_Review_Report_YYYY-MM-DD-HHMMSS.ipynb
4. Optimization_Recommendations_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Structure review complete
- [ ] Security review complete
- [ ] Expressions reviewed
- [ ] Best practices assessed
- [ ] Optimization opportunities identified

---

### 7. N8N-WORKFLOW-REFACTOR

**Purpose:** Workflow optimization and refactoring

**Key Sections:**

- Refactoring Strategy (based on review)
- Performance Optimization (node consolidation, expression optimization)
- Simplification Opportunities
- Incremental Updates (n8n_update_partial_workflow with diffs)
- Validation After Refactor

**MCP Tools:**

- n8n_get_workflow
- n8n_update_partial_workflow (80-90% token savings with diffs)
- validate_workflow / validate_workflow_connections / validate_workflow_expressions
- n8n_validate_workflow
- Standard tools

**Deliverables:**

1. Refactoring_Plan_YYYY-MM-DD-HHMMSS.ipynb
2. Performance_Optimization_Report_YYYY-MM-DD-HHMMSS.ipynb
3. Refactoring_Changes_Log_YYYY-MM-DD-HHMMSS.ipynb
4. Post_Refactor_Validation_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Refactoring plan executed
- [ ] Performance improvements measured
- [ ] Complexity reduced
- [ ] All validations passed
- [ ] Documentation updated

---

### 8. N8N-WORKFLOW-GAP-ANALYSIS

**Purpose:** Requirements vs implementation gap analysis

**Key Sections:**

- Requirements Coverage Analysis
- Feature Completeness Assessment
- Testing Coverage Analysis (Vitest framework)
- Documentation Gap Analysis
- Deployment Readiness Assessment

**MCP Tools:**

- n8n_list_workflows
- n8n_get_workflow_structure
- n8n_list_executions
- get_database_statistics
- Standard tools

**Deliverables:**

1. Requirements_Coverage_Report_YYYY-MM-DD-HHMMSS.ipynb
2. Feature_Completeness_Analysis_YYYY-MM-DD-HHMMSS.ipynb
3. Testing_Gap_Analysis_YYYY-MM-DD-HHMMSS.ipynb
4. Production_Readiness_Assessment_YYYY-MM-DD-HHMMSS.ipynb

**Success Criteria:**

- [ ] Requirements mapped to implementations
- [ ] Feature gaps identified
- [ ] Testing coverage assessed
- [ ] Documentation completeness verified
- [ ] Production readiness complete

---

## Common N8N Patterns (To Include Across All Commands)

### 1. Template-First Approach Pattern

```markdown
### Template-First Workflow Strategy

**ALWAYS CHECK FOR EXISTING TEMPLATES FIRST (2,500+ available):**

1. **Search by metadata** (97.5% have metadata):

   - Complexity: `simple|intermediate|advanced`
   - Audience: `marketers|developers|analysts|business-users`
   - Setup time: `maxSetupMinutes: 15|30|60`
   - Service: `openai|slack|google|etc`

2. **Search by task** (curated):

   - `get_templates_for_task('webhook_processing')`
   - Common: webhook_processing, slack_integration, data_transformation

3. **Search by text** (keyword):

   - `search_templates('slack notification webhook')`

4. **Search by nodes** (specific nodes):
   - `list_node_templates(['n8n-nodes-base.webhook'])`

**Best Practices:**

- Templates save 70-90% development time
- ALWAYS attribute: "Based on template by **[Author]** (@username) - [URL]"
- Validate before use
- Customize to requirements
```

### 2. Node Discovery Pattern

```markdown
### Node Discovery Strategy

1. **Broad search**: `search_nodes({query: 'database'})`
2. **Get essentials**: `get_node_essentials('nodeType')` (10-20 essential properties)
3. **Targeted search**: `search_node_properties('nodeType', 'auth')`
4. **Task templates**: `get_node_for_task('send_email')`
5. **Full docs**: `get_node_documentation('nodeType')` (when needed)
```

### 3. Validation Strategy Pattern

```markdown
### Validation Strategy (Validate Early and Often)

**Pre-Build:**

1. `validate_node_minimal()` - Quick required fields
2. `validate_node_operation()` - Full config with profile

**During Build:**

1. Validate each node
2. Check dependencies
3. Validate expressions

**Post-Build:**

1. `validate_workflow()` - Complete validation
2. `validate_workflow_connections()` - Structure
3. `validate_workflow_expressions()` - All expressions

**Post-Deployment:**

1. `n8n_validate_workflow({id})` - Validate in n8n
2. `n8n_list_executions()` - Monitor status
3. `n8n_update_partial_workflow()` - Fix with diffs
```

### 4. Testing Strategy Pattern

```markdown
### Testing Strategy for n8n Workflows

**Framework: Vitest**

- Unit tests: Node configuration validation
- Integration: Workflow execution
- E2E: Real n8n instance (Docker)

**Test Levels:**

1. Unit (70%): Node configurations
2. Integration (20%): Workflow validation
3. E2E (10%): Full workflow with API

**Patterns:**

- Mock n8n API for unit tests
- In-memory n8n for integration
- Docker Compose for E2E
- Test data factories
```

### 5. Deployment Pattern

```markdown
### n8n Deployment Strategies

**Local Development:**

- Docker Compose with n8n
- API configuration (URL, KEY)
- Local testing

**Production:**

- n8n cloud or self-hosted
- Environment configs
- CI/CD integration
- Versioning strategies

**Process:**

1. Validate locally
2. Deploy: `n8n_create_workflow()`
3. Validate: `n8n_validate_workflow({id})`
4. Activate workflow
5. Monitor: `n8n_list_executions()`
6. Update: `n8n_update_partial_workflow()` (80-90% token savings)
```

### 6. MCP Tool Best Practices

```markdown
### n8n MCP Tool Best Practices

**Token Efficiency:**

- `get_node_essentials()` vs full docs (80-90% savings)
- `n8n_update_partial_workflow()` with diffs (80-90% savings)
- `validate_node_minimal()` for quick checks
- Filter template searches with metadata

**Workflow Best Practices:**

- Start with `tools_documentation()`
- Template-first approach
- Pre-validate before building
- Use Code node ONLY when necessary
- Validate before deployment
- Test locally AND after deployment

**AI Tool Integration:**

- ANY node can be AI tool
- `list_ai_tools()` for discovery
- `get_node_as_tool_info()` for AI config
```

## Implementation Approach

### Phase 1: Read Current Files

Read all existing .md and .yaml files to understand current structure

### Phase 2: Transform Content

For each command pair:

1. Read current Node.js-focused content
2. Map to n8n workflow lifecycle phase
3. Replace Node.js concepts with n8n workflow concepts
4. Integrate n8n MCP tools and patterns
5. Add n8n-specific validation and best practices
6. Update deliverables with proper timestamps
7. Add success criteria specific to n8n workflows

### Phase 3: Validate Consistency

- Ensure all commands reference each other correctly
- Verify MCP tool usage is accurate
- Check that n8n patterns are consistently applied
- Validate deliverable naming conventions
- Ensure proper timestamp formats

### Phase 4: Integration Testing

- Verify command flow (planning design implementation validation review refactor gap-analysis)
- Check that each command produces expected deliverables
- Validate that MCP tools are properly specified

## Success Criteria for Complete Rewrite

### Content Transformation

- [ ] All Node.js framework concepts replaced with n8n workflow concepts
- [ ] Framework selection Template/node selection
- [ ] Code implementation Workflow building
- [ ] Testing patterns Workflow validation and testing
- [ ] Deployment n8n API deployment

### n8n Integration

- [ ] n8n-mcp-prompt.md practices integrated
- [ ] n8n API patterns included
- [ ] Workflow validation requirements specified
- [ ] Testing strategies from n8n_workflow_manager docs included
- [ ] Template-first approach emphasized

### Consistency

- [ ] RFC 2119 language (MUST, SHALL, MAY) used
- [ ] Deployment command structure followed
- [ ] MCP tool requirements comprehensive
- [ ] Success criteria specific and measurable
- [ ] Deliverables use YYYY-MM-DD-HHMMSS format

### Integration

- [ ] Commands reference each other appropriately
- [ ] Workflow progresses logically through lifecycle
- [ ] No gaps in coverage
- [ ] MCP tools properly specified for each phase

### Production Readiness

- [ ] All commands ready for production use
- [ ] Integration with n8n_workflow_manager repo validated
- [ ] Documentation complete and accurate
- [ ] Examples relevant and helpful

## References

### Key Documents

- `n8n-mcp-prompt.md` - n8n MCP workflow process and best practices
- `n8n_workflow_manager/docs/testing-strategy.md` - Testing approach and Vitest framework
- `n8n_workflow_manager/docs/testing-architecture.md` - Test infrastructure details
- `.claude/commands/deployments/deployments-planning.md` - Structure template

### n8n MCP Tools Reference

- **Template Discovery**: search_templates, search_templates_by_metadata, get_templates_for_task, list_node_templates, get_template
- **Node Discovery**: search_nodes, list_nodes, list_ai_tools, get_node_essentials, get_node_for_task, search_node_properties, get_property_dependencies, get_node_documentation, get_node_as_tool_info
- **Validation**: validate_node_minimal, validate_node_operation, validate_workflow, validate_workflow_connections, validate_workflow_expressions, get_property_dependencies
- **n8n Management**: n8n_create_workflow, n8n_get_workflow, n8n_get_workflow_structure, n8n_list_workflows, n8n_update_partial_workflow, n8n_validate_workflow, n8n_trigger_webhook_workflow, n8n_list_executions
- **System**: n8n_health_check, n8n_diagnostic, tools_documentation, get_database_statistics

## Next Steps

1. Proceed to PHASE 2: IMPLEMENTATION
2. Rewrite each .md file following the plan
3. Rewrite each .yaml file following the plan
4. Validate all changes
5. Create summary of changes document

---

**Plan Status:** COMPLETE
**Next Action:** Begin PHASE 2 - Implementation
**Estimated Implementation Time:** 2-3 hours for all 16 files
