# Simple Quality Fix Command

## Objective
Fix specific code quality issues detected by the quality checker.

## Instructions
1. Run Black formatter on all Python files in the project
2. Fix any obvious linting issues (unused imports, etc.)
3. Address any hardcoded secrets by moving them to environment variables
4. Simplify overly complex functions if found

## Commands to Execute

```bash
# Format Python files
black --line-length 88 .

# Fix import sorting
isort --profile black .

# Basic linting fixes
ruff check --fix .
```

## Focus Areas
- Code formatting consistency
- Import organization
- Remove unused code
- Fix basic style violations
- Address security issues (hardcoded secrets)

## Expected Outcome
All Python files should be properly formatted and basic quality issues resolved.

## MCP PROTOCOL COMPLIANCE REQUIREMENTS

**MANDATORY REQUIREMENTS FOR ALL SIMPLE QUALITY FIX OPERATIONS:**

1. ** ALWAYS use context7 BEFORE fixing** - Get current, accurate documentation
2. ** ALWAYS use grep to search GitHub** - Find real production examples
3. ** ALWAYS record actions in neo4j-memory and memory AS YOU WORK** - Document everything
4. ** ALWAYS save to neo4j-memory and memory** - Preserve for future sessions

**THE GOLDEN RULE: context7 (docs)  grep (examples)  memory (record)  fix  memory (persist)**

## MANDATORY REVERSE DATE STAMP REQUIREMENTS

**ALL OUTPUT FILES AND DOCUMENTATION MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**