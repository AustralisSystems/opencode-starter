# Code Quality Improvement Command

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ AND INDEX**: `C:\github_development\ai-agents\.claude\commands\ai-agent-compliance.md`
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

## Objective

Apply comprehensive code quality improvements for formatting, linting, complexity, and maintainability issues.

## Context

This command systematically improves code quality across the entire codebase using industry-standard tools and best practices.

## Quality Improvement Areas

### 1. Code Formatting

- **Black**: Python code formatting
- **Prettier**: JavaScript/TypeScript/JSON/CSS formatting
- **isort**: Python import sorting
- **EditorConfig**: Consistent line endings and indentation

### 2. Linting & Style

- **Ruff**: Fast Python linting
- **ESLint**: JavaScript/TypeScript linting
- **Flake8**: Python style guide enforcement
- **Pylint**: Comprehensive Python analysis

### 3. Complexity Reduction

- **Cyclomatic Complexity**: Simplify complex functions
- **Cognitive Complexity**: Improve code readability
- **Nested Depth**: Reduce excessive nesting
- **Function Length**: Break down large functions

### 4. Code Maintainability

- **Dead Code Removal**: Eliminate unused code
- **Duplicate Code**: Refactor repeated patterns
- **Documentation**: Add missing docstrings
- **Type Annotations**: Improve type safety

## Implementation Protocol

### Phase 1: Automated Formatting

1. **Python Formatting**:

   ```bash
   # Format all Python files
   black --line-length 88 --target-version py311 .

   # Sort imports
   isort --profile black .

   # Fix common issues
   autopep8 --in-place --aggressive --aggressive .
   ```

2. **JavaScript/TypeScript Formatting**:

   ```bash
   # Format web assets
   prettier --write "**/*.{js,ts,jsx,tsx,json,css,md}"

   # Fix ESLint issues
   eslint --fix "**/*.{js,ts,jsx,tsx}"
   ```

3. **Configuration Files**:

   ```bash
   # Format JSON files
   find . -name "*.json" -exec python -m json.tool {} {} \;

   # Format YAML files
   yamllint --format auto .
   ```

### Phase 2: Linting & Style Enforcement

1. **Python Linting**:

   ```bash
   # Fast linting with Ruff
   ruff check --fix .

   # Comprehensive analysis
   flake8 --max-line-length=88 --extend-ignore=E203,W503 .

   # Advanced static analysis
   pylint --rcfile=.pylintrc .
   ```

2. **Type Checking**:

   ```bash
   # Static type checking
   mypy --strict --ignore-missing-imports .

   # Runtime type checking
   python -m pytest --mypy .
   ```

### Phase 3: Complexity Reduction

1. **Identify Complex Functions**:

   ```bash
   # Complexity analysis
   radon cc . --min C
   radon mi . --min B
   xenon . --max-absolute B --max-modules A
   ```

2. **Refactoring Strategies**:
   - **Extract Methods**: Break down large functions
   - **Simplify Conditionals**: Reduce nested if/else
   - **Remove Duplication**: Create reusable functions
   - **Early Returns**: Reduce nesting depth

### Phase 4: Documentation & Maintainability

1. **Documentation Enhancement**:

   - Add missing docstrings
   - Improve existing documentation
   - Add type annotations
   - Update inline comments

2. **Code Cleanup**:
   - Remove unused imports
   - Delete dead code
   - Consolidate duplicate logic
   - Improve variable naming

## Quality Metrics Tracking

### Before/After Comparison

- **Complexity Score**: Track cyclomatic complexity reduction
- **Maintainability Index**: Measure code maintainability improvement
- **Test Coverage**: Ensure coverage maintained or improved
- **Performance**: Verify no performance degradation

### Quality Gates

- **Complexity**: All functions below complexity threshold (15)
- **Style**: 100% compliance with style guides
- **Documentation**: All public APIs documented
- **Type Safety**: Complete type annotation coverage

## Implementation Guidelines

### Code Quality Standards

- **SOLID Principles**: Ensure adherence throughout
- **DRY Principle**: Eliminate code duplication
- **KISS Principle**: Prefer simple solutions
- **Clean Code**: Follow established patterns

### Refactoring Safety

- **Small Changes**: Make incremental improvements
- **Test Coverage**: Maintain or improve test coverage
- **Functionality**: Preserve original behavior
- **Performance**: Monitor for regressions

## Execution Steps

1. **Quality Assessment**:

   ```bash
   # Baseline measurements
   radon cc . -a > complexity-before.txt
   radon mi . -a > maintainability-before.txt
   coverage run --source=. -m pytest
   coverage report > coverage-before.txt
   ```

2. **Automated Improvements**:

   - Run formatting tools systematically
   - Apply automated linting fixes
   - Address simple complexity issues

3. **Manual Refactoring**:

   - Tackle complex refactoring tasks
   - Improve documentation quality
   - Optimize performance bottlenecks

4. **Validation**:
   ```bash
   # Post-improvement measurements
   radon cc . -a > complexity-after.txt
   radon mi . -a > maintainability-after.txt
   coverage run --source=. -m pytest
   coverage report > coverage-after.txt
   ```

## Success Criteria

- All code formatted consistently across the project
- Zero linting errors or warnings remaining
- All functions below complexity threshold (15)
- Maintainability index improved by 20%
- Test coverage maintained or improved
- Documentation coverage 90% for public APIs

## Error Handling

### Quality Improvement Challenges

- **Formatting Conflicts**: Resolve tool configuration conflicts
- **Breaking Changes**: Ensure refactoring doesn't break functionality
- **Performance Impact**: Monitor for performance regressions
- **Test Failures**: Fix tests broken by refactoring

### Rollback Scenarios

- **Functionality Loss**: Revert changes that break features
- **Performance Degradation**: Rollback performance-impacting changes
- **Test Breakage**: Fix or revert changes causing test failures
- **Integration Issues**: Address compatibility problems

## Output Requirements

Generate comprehensive improvement report:

```json
{
  "quality_improvements_applied": {
    "files_formatted": 0,
    "linting_issues_fixed": 0,
    "complexity_reductions": 0,
    "documentation_added": 0,
    "dead_code_removed": 0
  },
  "code_metrics": {
    "complexity_before": 15.2,
    "complexity_after": 8.7,
    "maintainability_before": "B",
    "maintainability_after": "A",
    "coverage_before": 85.5,
    "coverage_after": 87.2
  },
  "quality_improvements": [
    "Reduced cyclomatic complexity by 43%",
    "Improved maintainability index from B to A",
    "Added 150+ missing docstrings",
    "Eliminated 25 duplicate code blocks"
  ],
  "tools_used": {
    "formatters": ["black", "prettier", "isort"],
    "linters": ["ruff", "eslint", "flake8"],
    "analyzers": ["radon", "mypy", "pylint"]
  }
}
```

## MCP PROTOCOL COMPLIANCE REQUIREMENTS

**MANDATORY REQUIREMENTS FOR ALL CODE IMPROVEMENT OPERATIONS:**

1. ** ALWAYS use context7 BEFORE improving code** - Get current best practices
2. ** ALWAYS use grep to search GitHub** - Find real production examples
3. ** ALWAYS record actions in neo4j-memory and memory AS YOU WORK** - Document everything
4. ** ALWAYS save to neo4j-memory and memory** - Preserve for future sessions

**THE GOLDEN RULE: context7 (docs) grep (examples) memory (record) improve memory (persist)**

## MANDATORY REVERSE DATE STAMP REQUIREMENTS

**ALL OUTPUT FILES AND DOCUMENTATION MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

Follow canonical quality standards and ensure all improvements enhance code maintainability and readability.
