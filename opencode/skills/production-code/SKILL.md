# Production Code Quality & Validation Skill

**Purpose:** Ensure 100% production-ready code through comprehensive validation and quality standards

**When to use:** ALWAYS before committing code - validation is MANDATORY for ALL production code

**Critical Importance:** 100% production ready is the ONLY acceptable state - NO EXCEPTIONS

---

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL validation work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → memory (record) → code (SOLID/DRY/KISS) → memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)

1. **CONTEXT LOAD**: Use `memory` to load previous validation decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `github-grep` BEFORE validating
   Examples of mandatory research queries:
   - `context7`: "Python code quality tools best practices 2026"
   - `context7`: "flake8 mypy configuration standards"
   - `github-grep`: "pyproject.toml configuration examples for ruff, bandit, safety"
3. **PLANNING**: Use `sequential-thinking` to plan validation approach
4. **VALIDATION**: Run validation tools, fix issues with SOLID/DRY/KISS
5. **PROGRESS TRACKING**: Record validation results to `memory`
6. **CONTEXT SAVE**: Persist quality standards to `memory`

**ABSOLUTELY FORBIDDEN:**
- ❌ Validating without context7 + grep research
- ❌ Skipping memory context load
- ❌ Completing without saving results to memory
- ❌ **Creating custom fix scripts to remediate code** (USE STANDARD TOOLS ONLY)
- ❌ Accepting partial success (99% = FAILURE)
- ❌ Using workarounds (# type: ignore, # noqa) to suppress issues

---

## ⚠️ ABSOLUTELY FORBIDDEN: CUSTOM FIX SCRIPTS

**🔴 YOU ARE ABSOLUTELY FORBIDDEN FROM CREATING CUSTOM SCRIPTS TO FIX OR REMEDIATE THE CODEBASE**

**WHY THIS IS FORBIDDEN:**
- Custom fix scripts have CONTINUOUSLY corrupted the codebase
- You have PROVEN INCAPABLE of writing reliable fix scripts
- Custom scripts introduce MORE bugs than they fix
- Standard tools are TESTED and RELIABLE

**YOU MUST USE STANDARD INDUSTRY TOOLS ONLY:**
- ✅ `black` for formatting
- ✅ `isort` for import organization
- ✅ `autoflake` for unused code removal (standard tool)
- ✅ Sub-agents for refactoring complex functions
- ✅ Manual refactoring following SOLID/DRY/KISS principles

**❌ NO CUSTOM SCRIPTS - EVER - ZERO EXCEPTIONS**

**If you violate this rule:**
1. STOP immediately
2. DELETE the custom script
3. Use standard tools instead
4. Re-run validation

---

## 100% Production Ready Definition

**PRODUCTION READY = ABSOLUTE PERFECTION ACROSS ALL METRICS**

**Anything less than 100% = UNACCEPTABLE FAILURE**

### The 12 Mandatory Metrics

| # | Metric | Tool | PASS Criteria | FAIL Criteria |
|---|--------|------|---------------|---------------|
| 1 | AST Compilation | py_compile | 0 errors | ≥1 error |
| 2 | Type Safety | mypy | 0 errors, 0 warnings | ≥1 error OR ≥1 warning |
| 3 | Linting | flake8 | 0 errors, 0 warnings | ≥1 error OR ≥1 warning |
| 4 | Security | bandit | 0 high, 0 medium | ≥1 high OR ≥1 medium |
| 5 | Dependencies | safety | 0 CVE issues | ≥1 vulnerability |
| 6 | Formatting | black | 0 files to format | ≥1 file needs formatting |
| 7 | Import Order | isort | 0 files to fix | ≥1 file incorrect |
| 8 | Complexity | radon cc | ALL ≤15 | ≥1 function >15 |
| 9 | Maintainability | radon mi | ALL MI ≥20 (Grade A) | ≥1 file <Grade A |
| 10 | Violations | xenon | 0 violations | ≥1 violation |
| 11 | Line Length | flake8, black | ALL ≤120 | ≥1 line >120 |
| 12 | Deduplication | pylint | ≤10% duplicate | >10% duplicate |

**ABSOLUTE REQUIREMENT: ALL 12 METRICS MUST ACHIEVE 100% PASS STATUS**

**EVEN ONE FAIL = ENTIRE CODEBASE FAILS**

---

## Configuration Standards (MANDATORY)

### Python Configuration Files

**pyproject.toml** (REQUIRED):
```toml
[tool.black]
line-length = 120
target-version = ['py310', 'py311', 'py312', 'py313']

[tool.isort]
profile = "black"
line_length = 120

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.ruff]
line-length = 120
target-version = "py310"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
source = ["."]
omit = ["tests/*", ".venv/*"]

[tool.bandit]
exclude_dirs = [".venv", "tests"]
```

**.flake8** (REQUIRED):
```ini
[flake8]
max-line-length = 120
max-complexity = 15
exclude =
    .git,
    __pycache__,
    .venv,
    venv,
    build,
    dist,
    *.egg-info,
    submodules
count = True
statistics = True
```

**mypy.ini** (REQUIRED):
```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
exclude = (?x)(
    \.venv/
    | node_modules/
    | __pycache__/
    | \.git/
    | submodules/
)
```

**BEFORE STARTING ANY WORK:**
1. Verify these files exist
2. Verify configurations are correct (line-length=120, max-complexity=15)
3. If missing or incorrect, CREATE/FIX them immediately

---

## Python Validation Commands (10 MANDATORY Commands)

### 1. AST Compilation Validation

```bash
python -m py_compile $(find . -name "*.py" -not -path "*/test*" -not -path "*/.venv/*")
```

**PASS:** 0 errors
**FAIL:** ≥1 compilation error
**Validates:** Python syntax correctness, valid Abstract Syntax Tree

**When to run:** BEFORE any other validation

---

### 2. Type Checking (MyPy)

```bash
python -m mypy . --exclude '(\.venv|node_modules|__pycache__|\.git|submodules)'
```

**PASS:** 0 errors, 0 warnings
**FAIL:** ≥1 error OR ≥1 warning
**Validates:** Type safety, no `Any` types, complete type annotations

**Configuration:** mypy.ini with strict mode
**Requirement:** 100% type coverage on all functions

**Common Issues:**
- Missing type hints → Add proper type annotations
- `Any` types → Replace with specific types
- `# type: ignore` → Fix the root cause, don't suppress

---

### 3. Linting (Flake8)

```bash
python -m flake8 . --max-line-length=120 --max-complexity=15 \
  --exclude=.git,__pycache__,.venv,venv,build,dist,*.egg-info,submodules \
  --count --statistics
```

**PASS:** 0 errors, 0 warnings
**FAIL:** ≥1 error OR ≥1 warning
**Validates:** PEP 8 compliance, code style, cyclomatic complexity

**Critical Settings:**
- `--max-line-length=120` (NOT 79 or 88)
- `--max-complexity=15` (functions must be ≤15)

**Common Violations:**
- E501: Line too long → Refactor or use Black
- C901: Function too complex → Refactor to reduce complexity
- F401: Imported but unused → Remove or use autoflake

---

### 4. Security Analysis (Bandit)

```bash
python -m bandit -r . -x ./.venv,./node_modules,./submodules \
  --skip B101,B601 -f json
```

**PASS:** 0 high severity, 0 medium severity
**FAIL:** ≥1 high OR ≥1 medium severity issue
**Validates:** SQL injection, hardcoded passwords, insecure functions, shell injection

**Skipped Checks:**
- B101: assert statements (allowed in tests)
- B601: shell injection (only if parameterized)

**NEVER skip:**
- SQL injection checks
- Hardcoded password checks
- Insecure hash function checks

**If security issues found:**
1. Fix at source (don't suppress with # nosec)
2. Use parameterized queries for SQL
3. Use environment variables for secrets
4. Use secure hash functions (SHA256+, bcrypt, argon2)

---

### 5. Dependency Security (Safety)

```bash
python -m safety check --json
```

**PASS:** 0 known vulnerabilities
**FAIL:** ≥1 CVE vulnerability in dependencies
**Validates:** CVE vulnerabilities, outdated packages with security issues

**If vulnerabilities found:**
1. Update affected package: `pip install --upgrade package_name`
2. Check if breaking changes exist
3. Run all tests after update
4. Re-run safety check to verify fix

---

### 6. Code Formatting (Black)

```bash
python -m black --check . --line-length=120 \
  --exclude='(\.venv|node_modules|__pycache__|\.git|submodules)'
```

**PASS:** 0 files needing reformatting
**FAIL:** ≥1 file needs formatting
**Validates:** Consistent code formatting across codebase

**To fix:**
```bash
python -m black . --line-length=120 \
  --exclude='(\.venv|node_modules|__pycache__|\.git|submodules)'
```

**Settings:**
- `--line-length=120` (MANDATORY, not default 88)

---

### 7. Import Organization (Isort)

```bash
python -m isort --check-only . --line-length=120 --profile=black \
  --skip .venv --skip node_modules --skip submodules
```

**PASS:** 0 files with incorrect import sorting
**FAIL:** ≥1 file has incorrect imports
**Validates:** Alphabetical imports, proper grouping (stdlib, third-party, local)

**To fix:**
```bash
python -m isort . --line-length=120 --profile=black \
  --skip .venv --skip node_modules --skip submodules
```

**Import order:**
1. Standard library imports
2. Third-party imports
3. Local application imports

---

### 8. Cyclomatic Complexity (Radon CC)

```bash
python -m radon cc . -a --min=C --exclude="*.venv/*,*node_modules/*,*submodules/*"
```

**PASS:** ALL functions ≤15 complexity (Grade A or B)
**FAIL:** ≥1 function >15 complexity
**Validates:** Code maintainability, function complexity

**Complexity Grades:**
- A: 1-5 (simple)
- B: 6-10 (well-structured)
- C: 11-15 (complex, acceptable limit)
- D: 16-20 (too complex, FAIL)
- E: 21-30 (very complex, FAIL)
- F: 31+ (extremely complex, FAIL)

**If complexity >15:**
1. Extract helper functions
2. Simplify conditional logic
3. Use early returns
4. Apply SOLID principles (especially SRP)
5. Use sub-agents for refactoring if needed

**DO NOT:**
- Use `# noqa: C901` to suppress
- Accept complexity >15 "just this once"
- Create workarounds

---

### 9. Maintainability Index (Radon MI)

```bash
python -m radon mi . -a --exclude="*.venv/*,*node_modules/*,*submodules/*"
```

**PASS:** ALL files Grade A (MI ≥20)
**FAIL:** ≥1 file <Grade A
**Validates:** Overall code maintainability

**Maintainability Index Grades:**
- A: 20-100 (highly maintainable)
- B: 10-19 (moderately maintainable)
- C: 0-9 (difficult to maintain)

**If MI <20:**
1. Reduce complexity (see radon cc)
2. Add documentation
3. Improve code structure
4. Reduce code duplication

---

### 10. Complexity Violations (Xenon)

```bash
python -m xenon . --max-absolute B --max-modules A --max-average A \
  --exclude ".venv" --exclude "node_modules" --exclude "submodules"
```

**PASS:** 0 violations (all code Grade A/B)
**FAIL:** ≥1 violation
**Validates:** No functions exceed complexity threshold

**Settings:**
- `--max-absolute B`: Individual functions ≤15 (Grade B)
- `--max-modules A`: Module average ≤10 (Grade A)
- `--max-average A`: Overall average ≤10 (Grade A)

---

## Node.js Validation Commands (6 MANDATORY Commands)

### Node.js Configuration Files

**tsconfig.json** (REQUIRED):
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictPropertyInitialization": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

**.eslintrc** (REQUIRED):
```json
{
  "rules": {
    "max-len": ["error", { "code": 120 }],
    "complexity": ["error", 15],
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

**.prettierrc** (REQUIRED):
```json
{
  "printWidth": 120,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5"
}
```

### 1. Type Checking (TypeScript)

```bash
npm run type-check
# OR: npx tsc --noEmit --strict
```

**PASS:** 0 type errors
**FAIL:** ≥1 type error
**Validates:** Complete type coverage, no `any` types

---

### 2. Linting (ESLint)

```bash
npm run lint
# OR: npx eslint . --ext .ts,.tsx,.js,.jsx --max-warnings 0
```

**PASS:** 0 errors, 0 warnings
**FAIL:** ≥1 error OR ≥1 warning
**Validates:** Code quality, complexity ≤15

---

### 3. Quality Checks

```bash
npm run quality:check
```

**PASS:** ALL checks pass
**FAIL:** ≥1 check fails
**Validates:** Combined linting, type checking, complexity

---

### 4. Development Server

```bash
npm run dev
```

**PASS:** Starts without errors
**FAIL:** Runtime exceptions or startup errors
**Validates:** Development environment, dependencies

---

### 5. Production Build

```bash
npm run build
```

**PASS:** Completes with 0 errors, 0 warnings
**FAIL:** ≥1 error OR ≥1 warning
**Validates:** Production bundle, tree shaking, optimization

---

### 6. Production Server

```bash
npm run start
```

**PASS:** Starts and serves correctly
**FAIL:** Startup errors or runtime issues
**Validates:** Production deployment readiness

---

## Validation Workflow (4 Phases)

### Phase 1: Pre-Implementation Validation

**BEFORE writing ANY code:**

```bash
# Python
python -m py_compile $(find . -name "*.py" -not -path "*/test*" -not -path "*/.venv/*")
python -m mypy . --exclude '(\.venv|node_modules|__pycache__|\.git|submodules)'
python -m flake8 . --max-line-length=120 --max-complexity=15

# Node.js
npm run type-check
npm run lint
```

**REQUIRED:** ALL commands pass with 0 errors, 0 warnings

**Purpose:** Establish baseline - ensure starting point is clean

---

### Phase 2: During Implementation Validation

**AFTER every file save:**

```bash
# Single file validation (faster)
python -m flake8 modified_file.py --max-line-length=120 --max-complexity=15
python -m mypy modified_file.py
python -m black --check modified_file.py --line-length=120
```

**REQUIRED:** Immediate fixes if ANY issues detected

**Purpose:** Catch issues early, prevent accumulation

---

### Phase 3: Pre-Commit Validation

**BEFORE every commit - ALL 10 Python OR 6 Node.js commands:**

**Python (ALL 10 commands):**
```bash
python -m py_compile $(find . -name "*.py" -not -path "*/test*" -not -path "*/.venv/*")
python -m mypy . --exclude '(\.venv|node_modules|__pycache__|\.git|submodules)'
python -m flake8 . --max-line-length=120 --max-complexity=15 --count --statistics
python -m bandit -r . -x ./.venv,./node_modules,./submodules --skip B101,B601 -f json
python -m safety check --json
python -m black --check . --line-length=120
python -m isort --check-only . --line-length=120 --profile=black
python -m radon cc . -a --min=C
python -m radon mi . -a
python -m xenon . --max-absolute B --max-modules A --max-average A
```

**Node.js (ALL 6 commands):**
```bash
npm run type-check
npm run lint
npm run quality:check
npm run dev  # Verify starts
npm run build  # Verify builds
npm run start  # Verify production serves
```

**REQUIRED:** 100% PASS on ALL commands. Fix ALL issues before committing.

**Purpose:** Ensure production ready before committing

---

### Phase 4: Continuous Validation

**AFTER pushing to remote:**

- Verify CI/CD pipeline shows all green
- Check deployment status
- Monitor for any issues

**Purpose:** Continuous monitoring, immediate remediation

---

## Remediation Strategies (STANDARD TOOLS ONLY)

### ✅ CORRECT: Use Standard Tools

**For formatting issues:**
```bash
python -m black . --line-length=120
```

**For import order:**
```bash
python -m isort . --line-length=120 --profile=black
```

**For unused imports:**
```bash
python -m autoflake --remove-all-unused-imports --in-place --recursive .
```

**For complexity >15:**
1. Use sub-agents: `Task(subagent_type="code-planner-implementer", prompt="Refactor function X to reduce complexity from 18 to ≤15")`
2. Manual refactoring following SOLID/DRY/KISS:
   - Extract helper functions (SRP)
   - Simplify conditional logic (KISS)
   - Use early returns
   - Apply design patterns

**For type coverage:**
- Add proper type hints manually
- Use specific types (NOT `Any`)
- Follow mypy suggestions

---

### ❌ FORBIDDEN: Custom Fix Scripts

**DO NOT create scripts like:**
- `fix_all_issues.py`
- `auto_remediate.py`
- `quick_fix.sh`
- `format_and_fix.py`

**WHY FORBIDDEN:**
- Custom scripts have corrupted the codebase repeatedly
- You are INCAPABLE of writing reliable fix scripts
- Standard tools are TESTED and SAFE
- Custom scripts introduce MORE problems

**If you create a custom fix script:**
1. STOP immediately
2. DELETE the script
3. Use standard tools instead
4. Apologize and re-run validation

---

## Production Ready Scope

### ✅ INCLUDED in Production Ready Requirements

- All Python source code (`*.py`)
- All TypeScript/JavaScript source code (`*.ts`, `*.tsx`, `*.js`, `*.jsx`)
- All configuration files (pyproject.toml, .flake8, mypy.ini, tsconfig.json, etc.)
- All production routes, services, utilities, helpers
- All database models, schemas, migrations
- All API endpoints and handlers
- All templates and frontend code
- All documentation (`*.md` files)

### ❌ EXCLUDED from Production Ready Requirements

- Git submodules (`./submodules/*`)
- Virtual environments (`.venv/`, `venv/`)
- Node modules (`node_modules/`)
- Build artifacts (`dist/`, `build/`, `*.egg-info/`)
- Cache directories (`__pycache__/`, `.pytest_cache/`)
- Test files (`test_*.py`, `*_test.py`) - **BUT they still should be high quality**

**Note:** Even excluded files should maintain reasonable quality, but don't block production ready status

---

## Quick Reference Checklists

### Before Claiming 100% Production Ready

**Verify ALL of the following:**

#### Code Quality (ALL MUST BE TRUE)
- [ ] py_compile: 0 errors
- [ ] mypy: 0 errors, 0 warnings, 100% type coverage
- [ ] flake8: 0 errors, 0 warnings
- [ ] bandit: 0 high, 0 medium severity
- [ ] safety: 0 vulnerabilities
- [ ] black: 0 files need formatting
- [ ] isort: 0 files incorrect
- [ ] radon cc: ALL ≤15 complexity
- [ ] radon mi: ALL Grade A
- [ ] xenon: 0 violations

#### Code Structure (ALL MUST BE TRUE)
- [ ] 0 functions with complexity >15
- [ ] 0 lines >120 characters
- [ ] ≤10% code deduplication
- [ ] 100% type hints
- [ ] 0 `Any` types (except unavoidable)
- [ ] 0 `# type: ignore`
- [ ] 0 `# noqa` (except documented exceptions)

#### Functionality (ALL MUST BE TRUE)
- [ ] 0 TODO comments
- [ ] 0 FIXME comments
- [ ] 0 mock implementations in production
- [ ] 0 stub functions in production
- [ ] 0 placeholder code
- [ ] 0 workarounds or hacks
- [ ] 0 commented-out code
- [ ] 100% fully implemented functionality

#### Configuration (ALL MUST BE TRUE)
- [ ] pyproject.toml exists (line-length=120, max-complexity=15)
- [ ] .flake8 exists (max-line-length=120, max-complexity=15)
- [ ] mypy.ini exists (strict configuration)
- [ ] All tools installed and accessible

---

## Integration with MCP Workflow

**When validating code:**

1. **Load Context**: `memory` - "Load previous validation results for project"
2. **Research**: `context7` - "Python code quality tools configuration 2025"
3. **Research**: `grep` - "pyproject.toml configuration examples github"
4. **Plan**: `sequential-thinking` - "Plan validation sequence and remediation strategy"
5. **Validate**: Run all 10 (Python) or 6 (Node.js) commands
6. **Fix**: Use ONLY standard tools (black, isort, autoflake, sub-agents)
7. **Track**: `memory` - "Record: All 10 validation commands passed"
8. **Save**: `memory` - "Persist: 100% production ready achieved"

---

## Summary: The Only Acceptable Outcome

**100% PRODUCTION READY = ABSOLUTE PERFECTION**

- ✅ 0 errors across ALL tools
- ✅ 0 warnings across ALL tools
- ✅ 0 security issues
- ✅ 0 vulnerabilities
- ✅ ALL complexity ≤15
- ✅ ALL maintainability Grade A
- ✅ ≤10% deduplication
- ✅ 100% type coverage
- ✅ 0 TODOs/FIXMEs/workarounds
- ✅ Line length ≤120
- ✅ Perfect formatting
- ✅ Perfect import order

**ANYTHING LESS THAN 100% = UNACCEPTABLE FAILURE**

**NO EXCEPTIONS. NO COMPROMISES. NO EXCUSES.**

**🔴 NEVER CREATE CUSTOM FIX SCRIPTS - USE STANDARD TOOLS ONLY**

---

**Skill Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** MANDATORY FOR ALL PRODUCTION CODE
**Compliance:** 100% PRODUCTION READY REQUIRED

**Follow THE GOLDEN RULE. Use standard tools. Achieve 100% production ready. Always.**
