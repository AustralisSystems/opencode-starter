# === FastAPI API Endpoint Design: AI-Driven RESTful API Endpoint Design and Implementation Protocol ===

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

## FASTAPI API ENDPOINT DESIGN PRINCIPLES

**INDUSTRY-STANDARD API DESIGN PRINCIPLES:**

### RESTful Design Principles

- **Resource-Based URLs**: Design URLs around resources, not actions
- **HTTP Methods**: Use appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE)
- **Status Codes**: Return meaningful HTTP status codes
- **Stateless Operations**: Each request should be independent
- **HATEOAS**: Hypermedia as the Engine of Application State when applicable

### FastAPI-Specific Best Practices

- **Type Safety**: Use comprehensive type annotations with Annotated types
- **Pydantic Models**: Leverage Pydantic for request/response validation
- **Dependency Injection**: Use FastAPI's DI system for clean separation
- **Async Operations**: Implement async/await patterns for I/O operations
- **OpenAPI Integration**: Ensure proper OpenAPI documentation generation

### Security-First Design

- **Authentication**: Implement proper authentication mechanisms
- **Authorization**: Apply fine-grained access controls
- **Input Validation**: Validate all inputs comprehensively
- **Rate Limiting**: Implement appropriate rate limiting
- **CORS Configuration**: Configure CORS policies properly

### Performance Optimization

- **Caching Strategies**: Implement intelligent response caching
- **Pagination**: Use cursor-based or offset pagination
- **Filtering**: Support efficient query filtering and sorting
- **Compression**: Enable response compression for large payloads
- **Connection Pooling**: Optimize database connections

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **FASTAPI API ENDPOINT DESIGN-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI API ENDPOINT DESIGN ONLY:**

- **MUST:** Create comprehensive RESTful API endpoint designs and specifications
- **MUST:** Design complete FastAPI router architectures and URL patterns
- **MUST:** Apply industry-standard API design principles and RESTful conventions
- **MUST:** Design Pydantic models for request/response validation
- **FORBIDDEN:** Creating implementation code or actual FastAPI modules
- **FORBIDDEN:** Creating test specifications or test designs
- **FORBIDDEN:** Generating incomplete or placeholder designs
- **MUST:** Output design documentation in markdown documents only

**FASTAPI API ENDPOINT DESIGN FOCUS AREAS:**

- RESTful API endpoint architecture and URL design patterns
- HTTP method selection and status code standardization
- Request/response schema design with Pydantic models
- API versioning strategies and backward compatibility
- Authentication and authorization endpoint design
- Error response standardization and exception handling
- Pagination, filtering, and sorting endpoint patterns
- File upload/download endpoint design
- Bulk operations and batch processing endpoints
- Real-time API patterns with WebSockets (if applicable)

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-api-endpoint-design-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for api_domain and endpoint_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the API design protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive API endpoint design documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% design completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-api-endpoint-design-prompt"
arguments:
  api_domain: "[user-management|order-processing|content-management|data-analytics]"
  endpoint_complexity: "[simple-crud|complex-business|enterprise-integration|real-time]"
  resource_model: "[optional: single-resource|related-resources|hierarchical|graph-based]"
  authentication_requirements: "[optional: public|authenticated|role-based|resource-based]"
  versioning_strategy: "[optional: url-versioning|header-versioning|content-negotiation]"
  response_formats: "[optional: json-only|multiple-formats|streaming|file-downloads]"
```

### **COMPREHENSIVE API ENDPOINT DESIGN GUIDELINES:**

#### 1. URL Design Patterns

**Resource-Based URL Structure:**

```
/api/v1/{resource}                    # Collection operations
/api/v1/{resource}/{id}               # Individual resource operations
/api/v1/{resource}/{id}/{sub-resource} # Sub-resource operations
/api/v1/{resource}/{id}/relationships/{relationship} # Relationship operations
```

**Examples:**

```
GET    /api/v1/users                  # List users
POST   /api/v1/users                  # Create user
GET    /api/v1/users/123              # Get user by ID
PUT    /api/v1/users/123              # Update user completely
PATCH  /api/v1/users/123              # Update user partially
DELETE /api/v1/users/123              # Delete user
GET    /api/v1/users/123/orders       # Get user's orders
POST   /api/v1/users/123/orders       # Create order for user
```

#### 2. HTTP Method Selection Guidelines

| Method  | Purpose                   | Request Body | Response Body | Idempotent | Safe |
| ------- | ------------------------- | ------------ | ------------- | ---------- | ---- |
| GET     | Retrieve resource(s)      | No           | Yes           | Yes        | Yes  |
| POST    | Create new resource       | Yes          | Yes           | No         | No   |
| PUT     | Replace entire resource   | Yes          | Yes           | Yes        | No   |
| PATCH   | Update resource partially | Yes          | Yes           | No         | No   |
| DELETE  | Remove resource           | No           | Optional      | Yes        | No   |
| HEAD    | Get metadata only         | No           | No            | Yes        | Yes  |
| OPTIONS | Get allowed methods       | No           | Yes           | Yes        | Yes  |

#### 3. HTTP Status Code Standards

**Success Codes:**

- `200 OK` - Successful GET, PUT, PATCH, or DELETE
- `201 Created` - Successful POST with resource creation
- `202 Accepted` - Request accepted for async processing
- `204 No Content` - Successful DELETE or PUT with no response body

**Client Error Codes:**

- `400 Bad Request` - Invalid request syntax or validation errors
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Authenticated but not authorized
- `404 Not Found` - Resource does not exist
- `405 Method Not Allowed` - HTTP method not supported
- `409 Conflict` - Resource conflict (duplicate, state conflict)
- `422 Unprocessable Entity` - Valid syntax but semantic errors
- `429 Too Many Requests` - Rate limit exceeded

**Server Error Codes:**

- `500 Internal Server Error` - Generic server error
- `502 Bad Gateway` - Invalid response from upstream server
- `503 Service Unavailable` - Server temporarily unavailable
- `504 Gateway Timeout` - Upstream server timeout

#### 4. Request/Response Schema Design

**Pydantic Model Design Patterns:**

```python
# Base model for common fields
class BaseModel(BaseModel):
    created_at: datetime
    updated_at: datetime

# Request models (input validation)
class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None

# Response models (output serialization)
class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

# List response with metadata
class UserListResponse(BaseModel):
    users: List[UserResponse]
    total_count: int
    page: int
    page_size: int
    has_next: bool
```

#### 5. Error Response Standardization

**Standard Error Response Format:**

```python
class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime
    path: str

class ValidationErrorResponse(BaseModel):
    error: str = "validation_error"
    message: str
    field_errors: List[Dict[str, str]]
    timestamp: datetime
    path: str
```

#### 6. Pagination Patterns

**Cursor-Based Pagination (Recommended):**

```python
class PaginationParams(BaseModel):
    cursor: Optional[str] = None
    limit: int = Field(default=20, ge=1, le=100)

class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    pagination: Dict[str, Any]  # next_cursor, has_next, etc.
```

**Offset-Based Pagination:**

```python
class OffsetPaginationParams(BaseModel):
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
```

#### 7. Filtering and Sorting

**Query Parameter Patterns:**

```
GET /api/v1/users?status=active&role=admin&sort=created_at:desc&search=john
GET /api/v1/orders?created_after=2023-01-01&amount_gte=100.00&status=in:pending,processing
```

**Filter Model Design:**

```python
class UserFilters(BaseModel):
    status: Optional[str] = None
    role: Optional[str] = None
    created_after: Optional[datetime] = None
    search: Optional[str] = None
    sort: Optional[str] = Field(default="created_at:desc")
```

#### 8. File Upload/Download Patterns

**File Upload Endpoint:**

```python
@router.post("/users/{user_id}/avatar")
async def upload_avatar(
    user_id: UUID,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
) -> FileUploadResponse:
    pass
```

**File Download Endpoint:**

```python
@router.get("/files/{file_id}/download")
async def download_file(
    file_id: UUID,
    current_user: User = Depends(get_current_user)
) -> FileResponse:
    pass
```

#### 9. Bulk Operations

**Bulk Create:**

```python
class BulkCreateRequest(BaseModel):
    items: List[UserCreateRequest] = Field(..., min_items=1, max_items=100)

class BulkCreateResponse(BaseModel):
    created: List[UserResponse]
    errors: List[Dict[str, Any]]
```

**Bulk Update:**

```python
class BulkUpdateRequest(BaseModel):
    updates: List[Dict[str, Any]] = Field(..., min_items=1, max_items=100)
```

#### 10. API Versioning Strategies

**URL Versioning (Recommended):**

```
/api/v1/users
/api/v2/users
```

**Header Versioning:**

```
GET /api/users
Accept: application/vnd.api+json;version=1
```

**Content Negotiation:**

```
GET /api/users
Accept: application/vnd.company.v1+json
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All API design phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive API endpoint architecture designed
- [ ] Complete RESTful URL patterns and HTTP method selection documented (timestamped)
- [ ] Request/response schema designs with Pydantic models created (timestamped)
- [ ] Authentication and authorization patterns designed (timestamped)
- [ ] Error response standardization implemented (timestamped)
- [ ] Pagination and filtering strategies designed (timestamped)
- [ ] File handling and bulk operation patterns specified (timestamped)
- [ ] API versioning and backward compatibility strategies defined (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FASTAPI API ENDPOINT DESIGN OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All design deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All API specification documentation includes precise timestamps
- [ ] All schema design documents include timestamp documentation
- [ ] All endpoint design documents include proper date stamps
- [ ] All authentication design documents follow consistent date stamp format
- [ ] All versioning strategy documents include timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating design files without proper reverse date stamps
- Using inconsistent date formats within same design session
- Missing timestamps in API design documentation

### **FASTAPI API ENDPOINT DESIGN DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/python-design/Architecture_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Architecture Design with technical specifications and implementation details
2. **`./project/docs/planning/python-design/Security_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Security Design with technical specifications and implementation details
3. **`./docs/design-patterns/Integration_Patterns_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation (enduring)
4. **`./project/docs/planning/python-design/Performance_Design_{YYYYMMDD-HHMMSS}.ipynb`** - Performance Design with technical specifications and implementation details
5. **`./project/docs/planning/python-design/Deployment_Architecture_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment Architecture with technical specifications and implementation details

**NEXT PHASE PREPARATION:**

```bash
# After endpoint design approval, proceed to implementation with:
/fastapi-router-implement [api-domain] [endpoint-scope] [design-source]

# Examples:
/fastapi-router-implement user-management comprehensive endpoint-designs
/fastapi-router-implement order-processing core-only api-specifications
/fastapi-router-implement content-management mvp design-documents
```

## Command Integration

### Related Commands

- **Architecture Phase**: `/fastapi-architecture-design` - Overall application architecture design
- **Planning Phase**: `/fastapi-implementation-planning` - Implementation roadmap and task breakdown
- **Service Patterns**: `/fastapi-service-dependency-patterns` - Service architecture patterns
- **Router Implementation**: `/fastapi-router-implement` - Router-specific implementation
- **Application Implementation**: `/fastapi-application-implement` - Full application implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - API design validation

### Workflow Navigation

```
Architecture Design  Implementation Planning  API Endpoint Design  Router Implementation  Quality Review

   Domain Models      Task Breakdown         API Contracts         Controllers         Validation
```

### Next Phase Commands

After completing API endpoint design, proceed with:

1. `/fastapi-router-implement` - Implement the designed API endpoints
2. `/fastapi-service-dependency-patterns` - Define service layer patterns
3. `/fastapi-application-implement` - Full application implementation

---

**ENFORCEMENT:** This command performs FASTAPI API ENDPOINT DESIGN ONLY through the MCP prompt protocol. The comprehensive design logic is defined in `fastapi-api-endpoint-design-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use implementation commands for actual FastAPI development after design is complete and approved.

---
