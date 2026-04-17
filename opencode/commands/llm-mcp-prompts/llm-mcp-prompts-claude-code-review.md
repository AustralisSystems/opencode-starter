# === Claude Code CLI Commands and MCP Prompts Review: Anthropic Best Practices Validation ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance-prompt.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance-prompt.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring review errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns
- Ignoring Anthropic best practices
- Skipping MCP protocol compliance

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of data or services in production code
- **NO TODOs** - complete ALL work immediately
- **NO SHORTCUTS** - implement properly ALWAYS
- **NO STUBS** - write complete implementations
- **NO FIXED DATA** - use real, dynamic data
- **NO HARDCODED VALUES** - use configuration
- **NO WORKAROUNDS** - fix root causes
- **NO FAKE IMPLEMENTATIONS** - real code only
- **NO PLACEHOLDER CODE** - production-ready only
- **NO TEMPORARY SOLUTIONS** - permanent fixes only
- **NO REVIEW BYPASSES** - follow all review standards
- **NO COMPLIANCE VIOLATIONS** - respect all standards

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ ANTHROPIC DOCUMENTATION:**
   - Check official Anthropic documentation
   - Review Claude prompt engineering best practices
   - Study Anthropic safety guidelines
   - Understand Anthropic alignment principles

2. **READ PUBLIC PROMPT ENGINEERING RESOURCES:**
   - Check public prompt engineering best practices
   - Review prompt optimization techniques
   - Study effective prompt patterns
   - Understand prompt evaluation methods

3. **READ PROJECT DOCUMENTATION:**
   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review Claude Code CLI documentation
   - Study MCP protocol documentation

4. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest prompt engineering documentation
   - Find official Anthropic documentation
   - Search GitHub for prompt engineering examples
   - Review industry best practices
   - Study similar successful projects
   - Check Stack Overflow for common patterns

**SEARCH PRIORITIES:**

- Official Anthropic documentation (latest version)
- Public prompt engineering best practices
- MCP protocol documentation
- Claude Code CLI standards
- Review and validation methodologies

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to Anthropic best practices and public prompt engineering standards.

### **REVIEW-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR CLAUDE CODE CLI REVIEW ONLY:**

- **MUST:** Execute comprehensive review of Claude Code CLI commands and MCP prompts
- **MUST:** Validate against Anthropic best practices and public standards
- **MUST:** Assess structure, clarity, and effectiveness
- **MUST:** Provide actionable improvement recommendations
- **MUST:** Generate comprehensive review reports
- **FORBIDDEN:** Creating extensive planning documentation (use `/deployments-planning` first)
- **FORBIDDEN:** Performing comprehensive analysis without review
- **MUST:** Focus on review execution with Anthropic best practices

**REVIEW EXECUTION FOCUS:**

- Analyze Claude Code CLI commands against Anthropic best practices
- Validate MCP prompts against protocol compliance
- Assess documentation quality and completeness
- Evaluate structure and organization
- Generate improvement recommendations
- Create implementation roadmap

**IF REVIEW ISSUES OCCUR:**

- Follow debugging protocol in `./.claude/commands/code/code-debug.md`
- Use refactoring protocol in `./.claude/commands/code/code-refactor.md`
- Apply planning protocol if major changes needed
- Implement fixes per best practices
- Ensure compliance per standards

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-claude-code-review-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for target_commands, target_mcp_prompts, review_scope
3. **FOLLOW PROTOCOL**: Execute all phases according to the review protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive review documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% review success achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "claude-code-review-prompt"
arguments:
  target_commands: ["list of Claude Code CLI command files"]
  target_mcp_prompts: ["list of MCP prompt YAML files"]
  review_scope: "[comprehensive|structure_only|best_practices_only|compliance_only|documentation_only]"
  review_standards: ["anthropic_best_practices", "public_prompt_engineering", "mcp_protocol_compliance"]
  improvement_focus: "[structure_optimization|clarity_enhancement|compliance_fixes|documentation_improvement|best_practices_alignment]"
  output_format: "[detailed_report|summary_report|actionable_recommendations|compliance_checklist]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All review phases completed according to protocol with timestamp tracking
- [ ] 100% successful review of all target files
- [ ] All standards validated and documented (timestamped)
- [ ] Comprehensive review documentation created with reverse date stamps
- [ ] All deliverables produced as specified with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL REVIEW OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All review reports (.md) have reverse date stamps in filenames
- [ ] All assessment reports include precise timestamps
- [ ] All improvement recommendations include timestamp documentation
- [ ] All compliance checklists include proper date stamps
- [ ] All implementation roadmaps follow consistent date stamp format
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating review files without proper reverse date stamps
- Using inconsistent date formats within same review session
- Missing timestamps in review documentation

### **ANTHROPIC BEST PRACTICES VALIDATION:**

**PROMPT STRUCTURE REQUIREMENTS:**

1. **Clear Role Definition:**
   - Explicit role and context setting
   - Specific task definition and objectives
   - Structured prompt organization
   - Appropriate prompt length and complexity
   - Clear output format specifications

2. **Prompt Clarity:**
   - Unambiguous instructions and requirements
   - Clear success criteria definition
   - Specific validation requirements
   - Explicit constraint definitions
   - Clear error handling instructions

3. **Prompt Safety:**
   - Appropriate safety guardrails
   - Ethical considerations and constraints
   - Responsible AI usage guidelines
   - Privacy and security considerations
   - Alignment with Anthropic's principles

### **PUBLIC PROMPT ENGINEERING STANDARDS:**

**PROMPT ENGINEERING PRINCIPLES:**

1. **Clear Instructions:**
   - Specific and actionable instructions
   - Appropriate context and background
   - Structured prompt organization
   - Effective use of examples and demonstrations
   - Clear output format specifications

2. **Prompt Effectiveness:**
   - Measurable success criteria
   - Clear validation requirements
   - Specific error handling
   - Appropriate complexity level
   - Effective constraint definitions

3. **Prompt Optimization:**
   - Optimal prompt length
   - Effective prompt structure
   - Clear prompt flow
   - Appropriate prompt complexity
   - Maintainable prompt design

### **MCP PROTOCOL COMPLIANCE:**

**MCP PROMPT STRUCTURE:**

1. **Proper Metadata:**
   - Complete MCP prompt metadata
   - Valid argument schema definitions
   - Compliant message structure
   - Clear execution phase definitions
   - Specific deliverable specifications

2. **Argument Validation:**
   - Complete argument schema definitions
   - Appropriate argument types and constraints
   - Clear argument descriptions
   - Valid argument validation rules
   - Proper argument requirements

3. **Message Structure:**
   - Appropriate message roles and content
   - Clear message organization
   - Effective message flow
   - Proper message formatting
   - Complete message content

### **CLAUDE CODE CLI STANDARDS:**

**COMMAND DOCUMENTATION:**

1. **Completeness:**
   - Complete command documentation
   - Clear command descriptions
   - Specific command usage examples
   - Detailed command parameters
   - Comprehensive command examples

2. **Structure:**
   - Logical command organization
   - Clear command flow
   - Appropriate command complexity
   - Effective command structure
   - Maintainable command design

3. **Effectiveness:**
   - Clear command objectives
   - Specific command requirements
   - Effective command validation
   - Appropriate command constraints
   - Clear command success criteria

### **DOCUMENTATION QUALITY ASSESSMENT:**

**DOCUMENTATION STANDARDS:**

1. **Completeness:**
   - Complete documentation coverage
   - Detailed documentation sections
   - Comprehensive documentation examples
   - Thorough documentation explanations
   - Complete documentation references

2. **Clarity:**
   - Clear documentation language
   - Unambiguous documentation instructions
   - Specific documentation examples
   - Clear documentation structure
   - Effective documentation organization

3. **Accuracy:**
   - Accurate documentation content
   - Current documentation information
   - Valid documentation examples
   - Correct documentation references
   - Precise documentation instructions

### **STRUCTURE AND ORGANIZATION ANALYSIS:**

**STRUCTURE STANDARDS:**

1. **Organization:**
   - Logical content organization
   - Clear content hierarchy
   - Appropriate content grouping
   - Effective content flow
   - Maintainable content structure

2. **Consistency:**
   - Consistent formatting and style
   - Uniform terminology and language
   - Coherent content presentation
   - Aligned content standards
   - Consistent content quality

3. **Maintainability:**
   - Maintainable content structure
   - Scalable content design
   - Extensible content framework
   - Flexible content organization
   - Adaptable content structure

### **IMPROVEMENT RECOMMENDATIONS FRAMEWORK:**

**CRITICAL IMPROVEMENTS (HIGH PRIORITY):**
- Address critical compliance violations
- Fix structural issues and gaps
- Resolve documentation completeness issues
- Correct best practices violations
- Implement essential functionality

**HIGH PRIORITY IMPROVEMENTS:**
- Enhance clarity and effectiveness
- Improve structure and organization
- Optimize performance and efficiency
- Strengthen validation and error handling
- Enhance user experience

**MEDIUM PRIORITY IMPROVEMENTS:**
- Refine documentation and examples
- Improve maintainability and scalability
- Enhance flexibility and adaptability
- Optimize resource usage
- Improve user experience

**LOW PRIORITY IMPROVEMENTS:**
- Polish formatting and presentation
- Enhance aesthetic and visual appeal
- Improve minor usability issues
- Optimize performance details
- Enhance documentation polish

### **REVIEW DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY REVIEW OUTPUT FILES:**

1. **`Claude_Code_Review_Report-YYYY-MM-DD-HHMMSS.md`** - Comprehensive review report
2. **`Anthropic_Best_Practices_Assessment-YYYY-MM-DD-HHMMSS.md`** - Anthropic standards validation
3. **`Public_Standards_Assessment-YYYY-MM-DD-HHMMSS.md`** - Public prompt engineering validation
4. **`MCP_Compliance_Assessment-YYYY-MM-DD-HHMMSS.md`** - MCP protocol compliance validation
5. **`Documentation_Quality_Assessment-YYYY-MM-DD-HHMMSS.md`** - Documentation quality analysis
6. **`Structure_Analysis_Report-YYYY-MM-DD-HHMMSS.md`** - Structure and organization analysis
7. **`Improvement_Recommendations-YYYY-MM-DD-HHMMSS.md`** - Actionable improvement recommendations
8. **`Implementation_Roadmap-YYYY-MM-DD-HHMMSS.md`** - Implementation roadmap and timeline
9. **`Compliance_Checklist-YYYY-MM-DD-HHMMSS.md`** - Compliance validation checklist

### **REVIEW QUALITY GATES:**

**PRE-REVIEW:**
- All required parameters provided and validated
- Target files accessible and readable
- Review scope and standards confirmed
- Output format specified and supported

**REVIEW PHASE:**
- All review phases completed successfully
- No critical errors during review process
- All standards validated appropriately
- All assessments completed thoroughly

**POST-REVIEW:**
- Comprehensive review report generated
- All findings documented with timestamps
- Improvement recommendations provided
- Implementation roadmap created

### **REVIEW TROUBLESHOOTING:**

**BASIC REVIEW DEBUGGING:**

```bash
# Check review status
kubectl get deployments
kubectl describe deployment {app-name}

# Check review logs
kubectl logs -l app={app-name}
kubectl describe pod {pod-name}

# Check review events
kubectl get events --sort-by='.lastTimestamp'
```

### **NEXT PHASE IMPLEMENTATION:**

After successful review, implement improvements:

```bash
# Basic implementation commands
kubectl apply -f improved-commands/
kubectl rollout status deployment/{app-name}

# Simple validation
kubectl get pods -l app={app-name}
kubectl logs -l app={app-name}
```

---

**ENFORCEMENT:** This command performs CLAUDE CODE CLI REVIEW ONLY through the MCP prompt protocol with STRICT adherence to Anthropic best practices and public prompt engineering standards. The comprehensive review logic is defined in `deployments-claude-code-review-prompt.yaml` and executed according to Model Context Protocol standards. All reviews must follow Anthropic best practices, public standards, and established patterns. Use `/deployments-planning` for comprehensive planning before review implementation. Focus on production-ready review execution with proper timestamp documentation and reverse date stamp requirements.
