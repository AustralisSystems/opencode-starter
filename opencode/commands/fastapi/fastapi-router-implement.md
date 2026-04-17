# FastAPI Router Implementation Command

## CRITICAL MCP PROMPT EXECUTION - MANDATORY

**THIS SECTION IS ABSOLUTELY MANDATORY - NON-COMPLIANCE FORBIDDEN**

**BEFORE ANY ROUTER IMPLEMENTATION, YOU MUST:**

1. **READ AND EXECUTE**: `fastapi-router-implement-prompt.yaml` - This is not optional
2. **FOLLOW MCP ORCHESTRATION**: Execute all MCP tool workflows as specified in the YAML
3. **ENFORCE NEO4J-MEMORY USAGE**: Load enduring memory context at session start, save at session end
4. **EXECUTE CONDITIONAL RESEARCH**: Follow intelligent research patterns based on authentication, dependencies, and CRUD requirements
5. **VALIDATE IMPLEMENTATION QUALITY**: Ensure >= 90% quality validation before completion

**MCP ORCHESTRATION REQUIREMENTS:**
-  Neo4j-memory (enduring memory) for router pattern persistence across projects
-  Memory (temporal memory) for session implementation progress tracking
-  Context7 + Grep for intelligent research based on detected requirements
-  Sequential-thinking for adaptive planning and Clean Architecture validation
-  Filesystem for code analysis and router implementation
-  Playwright for comprehensive API endpoint testing
-  Automated quality and security validation workflows

**NON-COMPLIANCE WITH MCP ORCHESTRATION IS ABSOLUTELY FORBIDDEN**

The YAML prompt contains sophisticated conditional research logic based on authentication requirements, dependency complexity, and CRUD operations that MUST be executed for optimal router implementations.

## STRICTLY FORBIDDEN - NO DOCUMENTATION CREATION

**THIS IS A CODING-ONLY COMMAND - DOCUMENTATION CREATION IS ABSOLUTELY FORBIDDEN**

**FORBIDDEN OUTPUTS:**
- **NO Jupyter Notebooks** (.ipynb files)
- **NO Markdown Documentation** (.md files)
- **NO Reports** of any kind
- **NO Analysis Documents**
- **NO Design Documents**
- **NO Planning Documents**
- **NO README files**
- **NO Architecture diagrams**
- **NO Technical specifications**
- **NO ANY FORM OF DOCUMENTATION WHATSOEVER**

**PERMITTED OUTPUTS:**
- **CODE ONLY** - Source code files (.py, .ts, .js, etc.)
- **CONFIGURATION FILES** - Config files required for code to function
- **TEST FILES** - Unit/integration tests for implemented code
- **BUILD ARTIFACTS** - Compiled/bundled code outputs

**VIOLATION CONSEQUENCES:**
Creating ANY documentation during this command execution will result in:
1. IMMEDIATE TASK TERMINATION
2. MANDATORY VIOLATION REPORT
3. COMPLETE ROLLBACK of all changes

**RATIONALE**: This is a pure implementation command focused exclusively on writing production code. Documentation should be created separately using dedicated documentation commands if needed.

## Command Overview
**Command**: `/fastapi-router-implement`
**Category**: FastAPI Development - Implementation
**Purpose**: Implement production-ready FastAPI routers with modern patterns, dependency injection, and Clean Architecture compliance

## Command Description
This command implements comprehensive FastAPI router modules following industry best practices, modern FastAPI 0.115+ patterns, and Clean Architecture principles. It creates production-ready router implementations with proper dependency injection, error handling, validation, and security.

## Key Features

### Modern FastAPI Router Patterns
- **APIRouter Configuration**: Proper router setup with prefixes, tags, and dependencies
- **Annotated Dependencies**: Modern dependency injection using `Annotated` types
- **Response Models**: Comprehensive Pydantic V2 response models with proper validation
- **HTTP Method Implementation**: Full REST API methods (GET, POST, PUT, PATCH, DELETE)
- **Status Code Management**: Proper HTTP status codes for all operations
- **Error Handling**: Comprehensive exception handling with custom error responses

### Clean Architecture Integration
- **Controller Layer**: Router acts as controller in Clean Architecture
- **Service Integration**: Proper service layer dependency injection
- **Repository Pattern**: Clean separation of data access concerns
- **Domain Models**: Integration with domain entities and value objects
- **Use Cases**: Implementation of business use cases through service calls

### Production-Grade Features
- **Authentication & Authorization**: JWT integration with role-based access control
- **Input Validation**: Comprehensive request validation with custom validators
- **Rate Limiting**: Per-endpoint rate limiting configuration
- **Caching**: Response caching with Redis integration
- **Logging**: Structured logging with correlation IDs
- **Monitoring**: Metrics collection and health checks

### Performance Optimization
- **Async Operations**: Full async/await pattern implementation
- **Connection Pooling**: Efficient database connection management
- **Query Optimization**: Efficient data fetching patterns
- **Response Streaming**: Large data streaming capabilities
- **Background Tasks**: Asynchronous task processing

## Technical Implementation

### Router Structure
```python
# Modern FastAPI router with Annotated dependencies
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field, ConfigDict

router = APIRouter(
    prefix="/api/v1/resources",
    tags=["resources"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)
```

### Dependency Injection Patterns
```python
# Clean Architecture service injection
ServiceDep = Annotated[ResourceService, Depends(get_resource_service)]
UserDep = Annotated[User, Depends(get_current_user)]
ValidatorDep = Annotated[ResourceValidator, Depends(get_validator)]
```

### Error Handling Implementation
```python
# Comprehensive error handling
@router.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "type": "validation_error"}
    )
```

## Architecture Compliance

### SOLID Principles
- **Single Responsibility**: Each router handles one resource type
- **Open/Closed**: Extensible through middleware and dependencies
- **Liskov Substitution**: Service interfaces are properly abstracted
- **Interface Segregation**: Focused interfaces for specific operations
- **Dependency Inversion**: Depends on abstractions, not concretions

### Clean Architecture Layers
- **Presentation Layer**: Router endpoints handle HTTP concerns
- **Application Layer**: Service calls orchestrate business logic
- **Domain Layer**: Business rules and entities remain pure
- **Infrastructure Layer**: Repository implementations handle data access

### Design Patterns
- **Repository Pattern**: Clean data access abstraction
- **Unit of Work**: Transaction management across multiple operations
- **Factory Pattern**: Service creation and configuration
- **Observer Pattern**: Event-driven architecture integration
- **Strategy Pattern**: Algorithm selection for different operations

## Security Implementation

### Authentication & Authorization
```python
# JWT authentication with role-based access
@router.get("/admin-only")
async def admin_endpoint(
    user: UserDep,
    _: Annotated[None, Depends(require_role("admin"))]
):
    return {"message": "Admin access granted"}
```

### Input Validation & Sanitization
```python
# Comprehensive input validation
class CreateResourceRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    category: ResourceCategory
    metadata: Dict[str, Any] = Field(default_factory=dict)
```

## Performance Features

### Caching Integration
```python
# Redis caching with TTL
@router.get("/resources/{id}")
@cache(expire=300, key_builder=resource_cache_key)
async def get_resource(id: int, service: ServiceDep):
    return await service.get_by_id(id)
```

### Background Tasks
```python
# Asynchronous processing
@router.post("/resources/bulk")
async def create_bulk_resources(
    requests: List[CreateResourceRequest],
    background_tasks: BackgroundTasks,
    service: ServiceDep
):
    background_tasks.add_task(service.process_bulk_creation, requests)
    return {"message": "Bulk creation initiated"}
```

## Monitoring & Observability

### Metrics Collection
```python
# Prometheus metrics integration
from prometheus_client import Counter, Histogram

request_count = Counter('api_requests_total', 'Total API requests')
request_duration = Histogram('api_request_duration_seconds', 'Request duration')
```

### Health Checks
```python
# Router health check endpoint
@router.get("/health", tags=["health"])
async def health_check(service: ServiceDep):
    return await service.health_check()
```

## Expected Deliverables

This command produces the following implementation artifacts:

### Core Router Implementation
1. **Main Router Module**: Complete FastAPI router with all endpoints
2. **Request Models**: Pydantic V2 models for all input validation
3. **Response Models**: Comprehensive response schemas with examples
4. **Exception Handlers**: Custom error handling for all scenarios

### Architecture Components
5. **Service Integration**: Clean service layer integration
6. **Dependency Configuration**: Modern dependency injection setup
7. **Middleware Implementation**: Authentication, logging, rate limiting
8. **Validation Rules**: Custom validators for business logic

### Production Features
9. **Security Configuration**: JWT, RBAC, input sanitization
10. **Performance Optimization**: Caching, async patterns, connection pooling
11. **Monitoring Integration**: Metrics, logging, health checks
12. **API Documentation**: OpenAPI schema with comprehensive examples

### Testing Infrastructure
13. **Unit Tests**: Comprehensive router endpoint testing
14. **Integration Tests**: Service layer integration validation
15. **Performance Tests**: Load testing and benchmarking
16. **Security Tests**: Authentication and authorization validation

## Usage Examples

### Basic Router Implementation
```python
# Create a new resource router
/fastapi-router-implement --resource users --operations crud --auth jwt

# Advanced router with caching and validation
/fastapi-router-implement --resource products --operations full --cache redis --validation strict

# Microservice router with event integration
/fastapi-router-implement --resource orders --pattern microservice --events rabbitmq
```

### Integration with Existing Architecture
```python
# Router with custom service integration
/fastapi-router-implement --resource inventory --service existing --repository custom

# Multi-tenant router implementation
/fastapi-router-implement --resource data --tenant multi --isolation strict
```

## Quality Standards

### Code Quality Metrics
- **Test Coverage**: Minimum 95% line coverage required
- **Type Safety**: Full type annotations with mypy validation
- **Code Style**: Black formatting and Ruff linting compliance
- **Security**: Bandit security scanning and OWASP compliance

### Performance Benchmarks
- **Response Time**: < 100ms for simple operations, < 500ms for complex
- **Throughput**: Support 1000+ concurrent requests
- **Memory Usage**: Efficient memory management with connection pooling
- **Error Rate**: < 0.1% error rate under normal load

### Architecture Compliance
- **Clean Architecture**: Proper layer separation and dependency flow
- **SOLID Principles**: Full compliance with all five principles
- **Design Patterns**: Appropriate pattern usage for scalability
- **API Standards**: RESTful design with proper HTTP semantics

## Command Integration

### Related Commands
- **Design Phase**: `/fastapi-architecture-design` - Overall application architecture
- **Planning Phase**: `/fastapi-implementation-planning` - Implementation roadmap
- **Service Creation**: `/fastapi-service-implement` - Service layer implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - Code review and validation
- **Refactoring**: `/fastapi-code-refactor` - Code improvement and modernization

### Workflow Navigation
```
Design  Planning  Router Implementation  Service Implementation  Quality Review  Refactoring
                                                                             
Architecture  Roadmap    Controllers        Business Logic      Validation   Optimization
```

## MCP Integration

This command requires the following MCP tools for comprehensive implementation:

### Core Development Tools
- **filesystem**: Read existing code, create router implementations
- **context7**: Get latest FastAPI and Pydantic documentation
- **grep**: Find implementation patterns from GitHub repositories
- **sequential-thinking**: Plan complex router architecture

### Quality Assurance Tools
- **memory**: Track implementation decisions and patterns
- **extended-memory**: Persist architectural decisions across sessions
- **playwright**: Test API endpoints and authentication flows

### Research and Validation Tools
- **fetch**: Get latest security and performance best practices
- **time**: Generate timestamps for logging and monitoring

This command ensures production-ready FastAPI router implementations that follow modern patterns, maintain architectural integrity, and deliver enterprise-grade performance and security.