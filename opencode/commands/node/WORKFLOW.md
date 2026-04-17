# Node.js Backend Development Workflow

## Command Flow Diagram

```

                    Node.js Backend Workflow


                      START: New Project or Analysis



                         nodejs-framework-planning
                        Framework selection
                        Architecture planning
                        Technology stack decision




                    nodejs-backend-architecture-design
                   System architecture design
                   Database design
                   API structure planning




                     nodejs-backend-implementation
                   Code implementation
                   API endpoints development
                   Database integration




           nodejs-code-review              nodejs-code-quality-
          Security analysis               analysis
          Performance review               Metrics collection
          Architecture audit               Tool recommendations




                        nodejs-gap-analysis
                   Current vs best practices
                   Improvement roadmap
                   Investment prioritization



                            END: Production Ready
```

## Command Categories

### Planning Commands

- **`nodejs-framework-planning`** - Strategic framework selection and roadmap
  - **Output**: Planning documentation
  - **Next**: `nodejs-backend-architecture-design`

### Design Commands

- **`nodejs-backend-architecture-design`** - System and API architecture
  - **Output**: Design documentation and diagrams
  - **Next**: `nodejs-backend-implementation`

### Implementation Commands

- **`nodejs-backend-implementation`** - Production-ready code development
  - **Output**: markdown documents with executable code
  - **Next**: `nodejs-code-review` + `nodejs-code-quality-analysis`

### Analysis Commands

- **`nodejs-code-review`** - Comprehensive code review and audit

  - **Output**: Review reports with findings and recommendations
  - **Parallel**: `nodejs-code-quality-analysis`

- **`nodejs-code-quality-analysis`** - Quality metrics and tooling analysis

  - **Output**: Quality dashboards and improvement guides
  - **Parallel**: `nodejs-code-review`

- **`nodejs-gap-analysis`** - Strategic improvement planning
  - **Output**: Gap assessment and roadmap
  - **Prerequisites**: Both review and quality analysis

## Navigation Paths

### New Project Path

```
Planning  Design  Implementation  Review & Quality  Gap Analysis
```

### Existing Project Path

```
Review & Quality Analysis  Gap Analysis  Planning (next iteration)
```

### Continuous Improvement Path

```
Gap Analysis  Planning  Design  Implementation  Review & Quality
```

## Command Integration Matrix

| Command                              | Prerequisites            | Outputs                    | Follow-up Commands                   |
| ------------------------------------ | ------------------------ | -------------------------- | ------------------------------------ |
| `nodejs-framework-planning`          | Project requirements     | 2 planning documents       | `nodejs-backend-architecture-design` |
| `nodejs-backend-architecture-design` | Framework selection      | 2 design documents         | `nodejs-backend-implementation`      |
| `nodejs-backend-implementation`      | Architecture design      | 2 implementation documents | Review + Quality commands            |
| `nodejs-code-review`                 | Implementation code      | 2 analysis documents       | `nodejs-gap-analysis`                |
| `nodejs-code-quality-analysis`       | Implementation code      | 3 quality documents        | `nodejs-gap-analysis`                |
| `nodejs-gap-analysis`                | Review + Quality results | 3 strategic documents      | Next iteration planning              |

## YAML Prompt Files

Each command has a corresponding YAML prompt file for MCP execution:

- `nodejs-framework-planning-prompt.yaml`
- `nodejs-backend-architecture-design-prompt.yaml`
- `nodejs-backend-implementation-prompt.yaml`
- `nodejs-code-review-prompt.yaml`
- `nodejs-code-quality-analysis-prompt.yaml`
- `nodejs-gap-analysis-prompt.yaml`

## Command Execution Notes

### Command Purpose Distinction

- **Planning/Design Commands**: Generate documentation and specifications
- **Implementation Commands**: Generate working code and configurations
- **Analysis Commands**: Generate reports and improvement recommendations

### MCP Tool Requirements

All commands require these mandatory MCP tools:

- `context7` - Latest documentation and best practices
- `grep` - Real-world GitHub implementation examples
- `sequential-thinking` - Structured approach planning
- `filesystem` - File operations and code analysis
- `memory` - Session progress tracking
- `time` - Activity timestamping

### Success Criteria

- All commands produce 2-3 markdown documents as specified
- Implementation commands focus on code generation only
- Analysis commands focus on reporting and recommendations
- Design commands focus on architecture and planning documentation
