# === FastAPI Code Refactor: AI-Driven Production-Ready FastAPI Code Refactoring Protocol ===

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

## CRITICAL MCP PROMPT EXECUTION - MANDATORY

**THIS SECTION IS ABSOLUTELY MANDATORY - NON-COMPLIANCE FORBIDDEN**

**BEFORE ANY REFACTORING OPERATIONS, YOU MUST:**

1. **READ AND EXECUTE**: `fastapi-code-refactor-prompt.yaml` - This is not optional
2. **FOLLOW MCP ORCHESTRATION**: Execute all MCP tool workflows as specified in the YAML
3. **ENFORCE NEO4J-MEMORY USAGE**: Load enduring memory context at session start, save at session end
4. **EXECUTE INTELLIGENT WORKFLOWS**: Follow conditional research and validation patterns
5. **VALIDATE QUALITY THRESHOLDS**: Ensure >= 85% quality validation before completion

**MCP ORCHESTRATION REQUIREMENTS:**

- Neo4j-memory (enduring memory) for context persistence across sessions
- Memory (temporal memory) for session progress tracking
- Context7 + Grep for intelligent research based on detected patterns
- Sequential-thinking for adaptive planning and validation
- Filesystem for code analysis and transformation
- Playwright for API endpoint validation
- Automated quality validation workflows

**NON-COMPLIANCE WITH MCP ORCHESTRATION IS ABSOLUTELY FORBIDDEN**

The YAML prompt contains sophisticated conditional logic and intelligent tool chaining that MUST be executed for proper refactoring outcomes.

## FORBIDDEN PRACTICES

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO DOCUMENTATION CREATION** - This is an implementation command
- **NO TEST CODE GENERATION** - Implementation only, no testing
- **NO README OR MD FILES** - Code changes only
- **NO BACKUP FILES** - Direct refactoring without duplicates
- **NO PLACEHOLDER CODE** - Production-ready refactored code only
- **NO TEMPORARY SOLUTIONS** - Permanent refactoring fixes only
- **NO INCOMPLETE REFACTORING** - Complete all improvements immediately
- **NO BREAKING CHANGES** - Maintain API compatibility unless explicitly required

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read quality review reports for refactoring guidance
   - Review performance analysis for optimization targets
   - Study security analysis for vulnerability fixes

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Review architecture documentation
   - Study API documentation for compatibility requirements

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest FastAPI refactoring patterns
   - Find FastAPI 0.115+ optimization techniques
   - Search for Pydantic V2 migration best practices
   - Review security hardening techniques
   - Study performance optimization patterns

**SEARCH PRIORITIES:**

- FastAPI 0.115+ refactoring guides
- Pydantic V2 migration patterns
- SQLModel optimization techniques
- Async/await performance improvements
- Security vulnerability remediation

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **FASTAPI CODE REFACTOR IMPLEMENTATION-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI CODE REFACTORING IMPLEMENTATION ONLY:**

- **MUST:** Implement production-ready FastAPI code refactoring and optimization
- **MUST:** Apply modern FastAPI 0.115+ patterns and Pydantic V2 optimizations
- **MUST:** Implement security vulnerability fixes and performance improvements
- **MUST:** Refactor to Clean Architecture and SOLID compliance
- **FORBIDDEN:** Creating documentation, analysis reports, or external files
- **FORBIDDEN:** Creating test code or test modifications
- **FORBIDDEN:** Creating backup files or temporary solutions
- **MUST:** Make direct code improvements with atomic commits

**FASTAPI CODE REFACTOR IMPLEMENTATION FOCUS AREAS:**

- Legacy FastAPI pattern modernization to 0.115+ standards
- Pydantic V1 to V2 migration and optimization
- Async/await pattern improvements and performance optimization
- Security vulnerability remediation and hardening
- Database query optimization and connection pooling
- Code organization and Clean Architecture compliance
- Dependency injection modernization with Annotated types
- Error handling and logging improvements
- Performance bottleneck resolution and caching implementation

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-code-refactor-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for refactor_scope and improvement_focus
3. **FOLLOW PROTOCOL**: Execute all phases according to the refactor protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **VALIDATE IMPROVEMENTS**: Confirm code quality and performance improvements
6. **COMMIT CHANGES**: Atomic commits with descriptive messages

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-code-refactor-prompt"
arguments:
  refactor_scope: "[complete-codebase|specific-modules|performance-critical|security-focused]"
  improvement_focus: "[modernization|performance|security|architecture|compatibility]"
  refactor_priority: "[optional: high-impact|quick-wins|comprehensive|targeted]"
  fastapi_version_target: "[optional: 0.115|0.116|latest-stable|backward-compatible]"
  migration_strategy: "[optional: incremental|complete|selective|safety-first]"
  optimization_level: "[optional: basic|aggressive|enterprise|production-ready]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and validation
- [ ] All targeted code successfully refactored and improved
- [ ] FastAPI patterns modernized to 0.115+ standards
- [ ] Pydantic V2 patterns implemented where applicable
- [ ] Security vulnerabilities addressed and resolved
- [ ] Performance optimizations implemented and validated
- [ ] Clean Architecture compliance achieved
- [ ] Dependency injection patterns modernized
- [ ] Error handling and logging improvements applied
- [ ] All code builds and runs without errors
- [ ] API compatibility maintained (unless breaking changes approved)
- [ ] Atomic commits with descriptive messages completed

### **FASTAPI CODE REFACTOR FOCUS AREAS:**

#### **1. FastAPI 0.115+ Modernization**

```python
# OLD Pattern (Legacy)
from fastapi import Depends, FastAPI

def get_current_user(token: str = Depends(oauth2_scheme)):
    return validate_token(token)

# NEW Pattern (Modern 0.115+)
from typing import Annotated
from fastapi import Depends, FastAPI

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
) -> User:
    return validate_token(token)
```

#### **2. Pydantic V2 Migration**

```python
# OLD Pattern (V1)
from pydantic import BaseSettings

class Settings(BaseSettings):
    class Config:
        env_file = ".env"

# NEW Pattern (V2)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }
```

#### **3. Performance Optimization**

```python
# OLD Pattern (Synchronous)
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()

# NEW Pattern (Async Optimized)
@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_async_db)]
) -> UserResponse:
    result = await db.execute(select(User).where(User.id == user_id))
    if user := result.scalar_one_or_none():
        return UserResponse.model_validate(user)
    raise HTTPException(404, "User not found")
```

### **NEXT PHASE PREPARATION:**

```bash
# After refactoring completion, validate improvements with:
/fastapi-code-quality-review complete-application comprehensive

# Examples based on refactor scope:
/fastapi-code-quality-review specific-modules performance-focused
/fastapi-code-quality-review complete-codebase security-focused
```

---

**ENFORCEMENT:** This command performs FASTAPI CODE REFACTORING IMPLEMENTATION ONLY through the MCP prompt protocol. The comprehensive refactoring logic is defined in `fastapi-code-refactor-prompt.yaml` and executed according to Model Context Protocol standards. No documentation or analysis creation allowed. Use quality review commands after refactoring is complete to validate improvements.

---
