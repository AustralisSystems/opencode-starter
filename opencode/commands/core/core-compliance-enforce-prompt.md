# Protocol Enforcement Command


Apply the canonical coding protocol for: $argument

## Canonical Protocol Requirements

### Core Philosophy
- KISS (Keep It Simple, Stupid)
- SOLID principles (Single Responsibility, Open/Closed, Liskov, Interface, Dependency)
- DRY (Don't Repeat Yourself)
- Clean Code principles

### Mandatory Behaviors
1. **RTFM First**: Read all relevant documentation before any code changes
2. **One Change at a Time**: Atomic commits with comprehensive testing
3. **No Shortcuts**: Complete all TODOs, no stubs, no placeholders
4. **Security First**: Never expose secrets, always validate inputs
5. **Git Discipline**: Follow single-branch development strategy from code-protocol-single-branch-strategy.md

### Code Quality Gates
- [ ] AST analysis passes
- [ ] Linting succeeds
- [ ] Type checking passes
- [ ] Unit tests complete
- [ ] Integration tests pass
- [ ] No duplicate code
- [ ] All functions documented

### Forbidden Patterns
- Creating "enhanced", "updated", "fixed" versions of files
- Hardcoded data, mocks, or stubs in production code
- Working directly on main/master branch
- Bundling multiple changes in single commits
- External documentation files during active development

Apply these protocols strictly to the specified task.