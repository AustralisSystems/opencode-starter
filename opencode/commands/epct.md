# EPCT Development Workflow Command

# === MANDATORY CANONICAL COMPLIANCE REQUIREMENTS ===

<!--
TEMPLATE VARIABLES TO REPLACE:
{{PROJECT_ID}} - Project identifier for extended-memory (e.g., "ai-agents")
{{PROJECT_NAME}} - Display name of the project
{{WORKING_BRANCH}} - Development branch name (e.g., "development")
{{SACRED_BRANCHES}} - Protected branches (e.g., "main/master/production")
{{DB_PATH}} - Extended memory database path (e.g., "sqlite:///./extended-memory/extended-memory.db")
{{FRAMEWORK_EXAMPLES}} - Your tech stack examples (e.g., "React, Next.js, FastAPI")
-->

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**IT IS MANDATORY TO ALWAYS USE YOUR AWESOME AGENTS AND SUB AGENTS FOR ALL INSTRUCTIONS AND OPERATIONS**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ, INDEX AND EXECUTE**: `C:\github_development\ai-agents\.claude\commands\ai-agent-compliance.md`
2. **VERIFY**: User has given explicit permission to proceed
3. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns

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

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read implementation documents for context
   - Review analysis documents for insights
   - Study documentation documents for patterns

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest documentation
   - Find official framework/library docs
   - Search GitHub for example implementations
   - Review industry best practices
   - Study similar successful projects
   - Check Stack Overflow for common patterns

**SEARCH PRIORITIES:**

- Official documentation (latest version)
- GitHub repositories with high stars
- Industry standard implementations
- Recent blog posts/tutorials (< 1 year old)
- Community best practices

---

## INSTRUCTIONS

**REMEMBER:** Professional enterprise development requires discipline, planning, and systematic execution. NO SHORTCUTS.

Please follow this structured development approach for: $argument

## Phase 1: Explore [SEARCH]

Conduct comprehensive research and analysis before any implementation.

### Codebase Discovery

- Search for existing implementations and patterns
- Identify reusable components and utilities
- Understand architectural decisions and constraints
- Document relevant file locations and dependencies

### Technical Research

- Review framework/library documentation
- Analyze best practices and anti-patterns
- Research performance implications
- Identify potential security concerns

### Requirements Analysis

- Clarify ambiguous requirements
- Define acceptance criteria
- Identify edge cases and error scenarios
- Document assumptions and decisions

### Key Findings

Document all discoveries with file references (e.g., `src/utils/helper.ts:42`)

## Phase 2: Plan

Design a comprehensive implementation strategy.

### Architecture Design

- Define component structure and relationships
- Create interface contracts and APIs
- Design data flow and state management
- Plan integration points

### Task Breakdown

Create atomic, independently testable tasks:

1. **Task Name**: Clear description
   - Estimated time: X hours
   - Dependencies: [list]
   - Success criteria: [measurable outcomes]

### Risk Assessment

- Technical challenges and mitigation strategies
- Performance bottlenecks and optimizations
- Security vulnerabilities and protections
- Scalability concerns and solutions

### Implementation Timeline

- Priority order of tasks
- Parallel work opportunities
- Critical path identification
- Testing checkpoints

## Phase 3: Code [CODE]

Implement the solution following strict quality standards.

### Development Protocol

- Work directly on development branch (single branch strategy)
- Follow existing code patterns and conventions
- Write self-documenting, clean code
- Implement comprehensive error handling

### Quality Gates

After each component:

- [ ] AST analysis passes
- [ ] Linting succeeds (0 errors, 0 warnings)
- [ ] Type checking passes
- [ ] Code compiles successfully
- [ ] No duplicate functionality

### Documentation Requirements

- Inline comments for complex logic only
- JSDoc/TSDoc for all public APIs
- Update relevant README sections
- Add usage examples where appropriate

### Security Checklist

- [ ] Input validation implemented
- [ ] No hardcoded secrets
- [ ] Proper authentication checks
- [ ] SQL injection prevention
- [ ] XSS protection in place

## Phase 4: Test [TEST]

Ensure comprehensive quality through rigorous testing.

### Unit Testing

- Test each function/method in isolation
- Cover happy path and error cases
- Aim for >90% code coverage
- Mock external dependencies appropriately

### Integration Testing

- Test component interactions
- Verify API contracts
- Test database operations
- Validate external service integrations

### Edge Case Testing

- Null/undefined inputs
- Empty collections
- Boundary values
- Concurrent operations
- Network failures

### Performance Testing

- Measure response times
- Check memory usage
- Identify bottlenecks
- Optimize critical paths

### Final Validation

- [ ] All tests passing
- [ ] No regression in existing features
- [ ] Performance metrics acceptable
- [ ] Security scan completed
- [ ] Code review approved

## Deliverables Checklist

- [ ] Working, tested code
- [ ] Comprehensive test suite
- [ ] Updated documentation
- [ ] No TODOs or tech debt
- [ ] Clean git history

Provide detailed output for each phase before proceeding to the next.
