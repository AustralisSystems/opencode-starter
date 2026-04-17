# FastAPI Service Implementation Command

<command_context>
  <role>FastAPI Service Implementation Specialist</role>
  <goal>Implement production-ready FastAPI service layer with Clean Architecture</goal>
  <expertise_level>enterprise</expertise_level>
</command_context>

<tone_context>
  <communication_style>Technical precision with professional directness</communication_style>
  <interaction_approach>Solution-focused with structured implementation guidance</interaction_approach>
  <technical_level>Expert-level technical communication with detailed explanations</technical_level>
  <response_format>Step-by-step implementation with code examples and architectural reasoning</response_format>
  <audience_considerations>Senior developers and technical leads requiring enterprise-grade solutions</audience_considerations>
</tone_context>

## CRITICAL MCP PROMPT EXECUTION - MANDATORY

<mcp_requirements>
  <mandatory_actions>
    <action priority="critical">READ AND EXECUTE: `fastapi-service-implement-prompt.yaml` - This is not optional</action>
    <action>FOLLOW MCP ORCHESTRATION: Execute all MCP tool workflows as specified in the YAML</action>
    <action>ENFORCE NEO4J-MEMORY USAGE: Load enduring memory context at session start, save at session end</action>
    <action>EXECUTE CONDITIONAL RESEARCH: Follow intelligent research patterns based on service complexity, domain rules, and integration requirements</action>
    <action>VALIDATE IMPLEMENTATION QUALITY: Ensure >= 90% quality validation before completion</action>
  </mandatory_actions>

  <mcp_orchestration>
    <sequence>neo4j-memory  memory  context7 + grep  sequential-thinking  filesystem  validation</sequence>
    <tools_required>["neo4j-memory", "memory", "context7", "grep", "sequential-thinking", "filesystem"]</tools_required>
    <quality_threshold>90% validation required</quality_threshold>
  </mcp_orchestration>

  <enforcement>NON-COMPLIANCE WITH MCP ORCHESTRATION IS ABSOLUTELY FORBIDDEN</enforcement>
</mcp_requirements>

The YAML prompt contains sophisticated conditional research logic based on domain complexity, business rule requirements, and integration patterns that MUST be executed for optimal service implementations.

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

<examples>
  <ideal_service_implementation>
    <user_query>Implement a user management service with authentication and role-based access control</user_query>
    <ai_response>
      I'll implement the user management service following our comprehensive MCP workflow:
      
      1. **Context Query**: Loading any previous user management work from neo4j-memory
      2. **Research Phase**: Using context7 for latest FastAPI security patterns and grep for RBAC implementations
      3. **Planning**: Using sequential-thinking to design Clean Architecture service layers
      4. **Implementation**: Creating UserService with dependency injection and proper abstractions
      5. **Progress Tracking**: Recording architectural decisions and patterns used
      6. **Context Save**: Persisting service patterns and security considerations
      
      Deliverables include:
      - UserService with CRUD operations and business logic
      - AuthenticationService with JWT token management
      - AuthorizationService with role-based permission checking
      - UserRepository with async database operations
      - Comprehensive test suite with 95%+ coverage
      
      All following Clean Architecture principles with proper dependency inversion.
    </ai_response>
  </ideal_service_implementation>

  <complex_business_logic_example>
    <scenario>Implementing order processing service with complex business rules</scenario>
    <ai_behavior>
      **Phase 1 - Research and Context**
      - Load previous e-commerce patterns from neo4j-memory
      - Research latest order processing patterns with context7
      - Find real-world order management implementations with grep
      
      **Phase 2 - Business Logic Design**
      - Use sequential-thinking to model complex order workflows:
        * Order validation and inventory checking
        * Payment processing with multiple providers
        * Shipping calculation and fulfillment
        * Order status transitions and notifications
      
      **Phase 3 - Clean Architecture Implementation**
      - OrderService: Orchestrate high-level business operations
      - OrderDomainService: Complex business rule validation
      - PaymentService: External payment provider integration
      - InventoryService: Stock management and reservation
      - NotificationService: Event-driven customer communications
      
      **Phase 4 - Quality Assurance**
      - Unit tests for all business logic with edge cases
      - Integration tests with external payment services
      - Performance tests for order processing throughput
      - Security tests for payment and personal data handling
    </ai_behavior>
  </complex_business_logic_example>

  <error_handling_example>
    <error_scenario>Service implementation fails during database integration</error_scenario>
    <proper_response>
      **Error Detection**: "Database connection failing in UserService integration tests"
      
      **Immediate Response**:
      1. **Halt and Analyze**: Stop implementation to diagnose database connectivity
      2. **Research Solutions**: Use context7 for SQLAlchemy async connection patterns
      3. **Find Examples**: Use grep for production database integration solutions
      4. **Root Cause Analysis**: Use sequential-thinking to identify configuration issues
      
      **Corrective Implementation**:
      - Fix database connection configuration
      - Implement proper connection pooling
      - Add connection retry logic with exponential backoff
      - Update service tests with proper database mocking
      
      **Validation and Recovery**:
      - Verify all database operations work correctly
      - Run full test suite to ensure no regressions
      - Document database configuration patterns in neo4j-memory
      - Update service implementation with lessons learned
    </proper_response>
  </error_handling_example>
</examples>

## Command Overview
**Command**: `/fastapi-service-implement`
**Category**: FastAPI Development - Implementation
**Purpose**: Implement production-ready FastAPI service layer with Clean Architecture principles, modern patterns, and enterprise-grade business logic

## Command Description
This command implements comprehensive FastAPI service layer modules following Clean Architecture principles, Domain-Driven Design patterns, and modern Python/FastAPI best practices. It creates production-ready service implementations with proper dependency injection, transaction management, and business logic separation.

## Key Features

### Clean Architecture Service Layer
- **Application Services**: Orchestrate business operations and use cases
- **Domain Services**: Implement complex business logic and rules
- **Infrastructure Services**: Handle external dependencies and integrations
- **Repository Pattern**: Clean data access abstraction
- **Unit of Work Pattern**: Transaction management across multiple operations
- **Dependency Inversion**: Services depend on abstractions, not concretions

<examples>
  <clean_architecture_pattern>
    <service_layer_example>
      <application_service>
```python
class UserApplicationService:
    def __init__(
        self,
        user_repository: UserRepository,
        email_service: EmailService,
        domain_service: UserDomainService,
        unit_of_work: UnitOfWork
    ):
        self._user_repo = user_repository
        self._email_service = email_service
        self._domain_service = domain_service
        self._uow = unit_of_work
    
    async def create_user(self, command: CreateUserCommand) -> User:
        async with self._uow:
            # Orchestrate the use case
            await self._domain_service.validate_user_creation(command)
            user = User.create(command.email, command.name)
            await self._user_repo.save(user)
            await self._email_service.send_welcome_email(user)
            return user
```
      </application_service>
      
      <domain_service>
```python
class UserDomainService:
    def __init__(self, user_repository: UserRepository):
        self._user_repo = user_repository
    
    async def validate_user_creation(self, command: CreateUserCommand):
        # Complex business rules
        if await self._user_repo.exists_by_email(command.email):
            raise BusinessException("Email already exists")
        
        if not self._is_valid_business_email(command.email):
            raise BusinessException("Invalid business email domain")
```
      </domain_service>
    </service_layer_example>
  </clean_architecture_pattern>

  <dependency_injection_example>
    <fastapi_integration>
```python
# Modern FastAPI dependency injection
from typing import Annotated
from fastapi import Depends

def get_user_service(
    user_repo: Annotated[UserRepository, Depends(get_user_repository)],
    email_service: Annotated[EmailService, Depends(get_email_service)],
    uow: Annotated[UnitOfWork, Depends(get_unit_of_work)]
) -> UserApplicationService:
    return UserApplicationService(user_repo, email_service, uow)

@router.post("/users/")
async def create_user(
    command: CreateUserCommand,
    service: Annotated[UserApplicationService, Depends(get_user_service)]
) -> UserResponse:
    user = await service.create_user(command)
    return UserResponse.from_domain(user)
```
    </fastapi_integration>
  </dependency_injection_example>
</examples>

### Modern Service Patterns
- **Async/Await Operations**: Full asynchronous service implementation
- **Dependency Injection**: Modern FastAPI dependency injection with `Annotated` types
- **Service Composition**: Modular service architecture with clear interfaces
- **Error Handling**: Comprehensive business exception handling
- **Event-Driven Architecture**: Integration with domain events and messaging
- **CQRS Implementation**: Command/Query responsibility segregation

### Business Logic Implementation
- **Use Case Orchestration**: Business use cases as first-class citizens
- **Domain Model Integration**: Rich domain objects with business behavior
- **Business Rule Validation**: Complex business rule enforcement
- **Transaction Management**: ACID compliance with rollback capabilities
- **Audit Logging**: Comprehensive business operation tracking
- **Performance Optimization**: Efficient business logic execution

### Enterprise Features
- **Multi-Tenancy Support**: Tenant-aware service operations
- **Authorization Integration**: Business-level authorization and permissions
- **Caching Strategies**: Multi-layer caching for performance
- **Background Processing**: Asynchronous business operation handling
- **Integration Patterns**: External service integration with circuit breakers
- **Monitoring & Observability**: Business metrics and operation tracking

## Technical Implementation

### Service Layer Architecture
<implementation_example type="service_architecture">
```python
# Clean Architecture service implementation
from typing import Annotated, Protocol, List, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass
from contextlib import asynccontextmanager

class ResourceRepository(Protocol):
    async def get_by_id(self, id: int) -> Optional[Resource]: ...
    async def save(self, resource: Resource) -> Resource: ...
    async def delete(self, id: int) -> bool: ...

class ResourceService:
    def __init__(
        self,
        repository: ResourceRepository,
        unit_of_work: UnitOfWork,
        domain_events: DomainEventDispatcher
    ):
        self._repository = repository
        self._uow = unit_of_work
        self._events = domain_events
```
</implementation_example>

### Business Use Case Implementation
<implementation_example type="use_case_pattern">
```python
# Use case pattern with business logic
@dataclass
class CreateResourceCommand:
    name: str
    description: Optional[str]
    category: ResourceCategory
    owner_id: int

class CreateResourceUseCase:
    async def execute(self, command: CreateResourceCommand) -> Resource:
        async with self._uow:
            # Business validation
            await self._validate_business_rules(command)

            # Create domain object
            resource = Resource.create(
                name=command.name,
                description=command.description,
                category=command.category,
                owner_id=command.owner_id
            )

            # Persist and publish events
            saved_resource = await self._repository.save(resource)
            await self._events.publish(ResourceCreatedEvent(saved_resource))

            return saved_resource
```
</implementation_example>

<examples>
  <cqrs_implementation>
    <command_handler>
```python
# CQRS Command Handler Pattern
class UpdateUserCommand:
    user_id: int
    name: Optional[str] = None
    email: Optional[str] = None
    
class UpdateUserCommandHandler:
    def __init__(
        self,
        user_repository: UserRepository,
        domain_service: UserDomainService,
        event_publisher: EventPublisher
    ):
        self._user_repo = user_repository
        self._domain_service = domain_service
        self._event_publisher = event_publisher
    
    async def handle(self, command: UpdateUserCommand) -> User:
        user = await self._user_repo.get_by_id(command.user_id)
        if not user:
            raise UserNotFoundError(command.user_id)
        
        # Apply business rules
        await self._domain_service.validate_user_update(user, command)
        
        # Apply changes
        if command.email:
            user.change_email(command.email)
        if command.name:
            user.change_name(command.name)
        
        # Persist and publish events
        updated_user = await self._user_repo.save(user)
        await self._event_publisher.publish(
            UserUpdatedEvent(user_id=user.id, changes=command.__dict__)
        )
        
        return updated_user
```
    </command_handler>
    
    <query_handler>
```python
# CQRS Query Handler Pattern
class GetUsersByRoleQuery:
    role: UserRole
    page: int = 1
    size: int = 10

class GetUsersByRoleQueryHandler:
    def __init__(self, user_read_repository: UserReadRepository):
        self._read_repo = user_read_repository
    
    async def handle(self, query: GetUsersByRoleQuery) -> PaginatedResult[UserView]:
        return await self._read_repo.find_users_by_role(
            role=query.role,
            page=query.page,
            size=query.size
        )
```
    </query_handler>
  </cqrs_implementation>

  <event_driven_architecture>
    <domain_event_handling>
```python
# Event-Driven Architecture with Domain Events
class UserCreatedEvent(DomainEvent):
    user_id: int
    email: str
    created_at: datetime

class UserCreatedEventHandler:
    def __init__(
        self,
        email_service: EmailService,
        audit_service: AuditService,
        analytics_service: AnalyticsService
    ):
        self._email_service = email_service
        self._audit_service = audit_service
        self._analytics_service = analytics_service
    
    async def handle(self, event: UserCreatedEvent):
        # Parallel event processing
        await asyncio.gather(
            self._email_service.send_welcome_email(event.email),
            self._audit_service.log_user_creation(event.user_id),
            self._analytics_service.track_user_signup(event)
        )
```
    </domain_event_handling>
  </event_driven_architecture>
</examples>

### Domain Service Implementation
<implementation_example type="domain_service">
```python
# Domain service for complex business logic
class ResourceDomainService:
    async def calculate_resource_score(
        self,
        resource: Resource,
        context: BusinessContext
    ) -> ResourceScore:
        # Complex business logic implementation
        base_score = self._calculate_base_score(resource)
        context_modifier = await self._get_context_modifier(context)
        popularity_boost = await self._calculate_popularity(resource)

        return ResourceScore(
            base=base_score,
            modifier=context_modifier,
            popularity=popularity_boost,
            final=base_score * context_modifier + popularity_boost
        )
```
</implementation_example>

## Architecture Compliance

### SOLID Principles
- **Single Responsibility**: Each service has one clear business purpose
- **Open/Closed**: Services extensible through dependency injection
- **Liskov Substitution**: Interface implementations are interchangeable
- **Interface Segregation**: Focused interfaces for specific business operations
- **Dependency Inversion**: Services depend on abstractions, not implementations

### Clean Architecture Layers
- **Application Layer**: Use cases and application services
- **Domain Layer**: Business entities, value objects, and domain services
- **Infrastructure Layer**: Repository implementations and external integrations
- **Presentation Layer**: Controllers interact through application services

### Domain-Driven Design
- **Bounded Contexts**: Clear service boundaries around business domains
- **Aggregates**: Consistent business operation boundaries
- **Value Objects**: Immutable business concepts
- **Domain Events**: Business event publishing and handling
- **Repositories**: Domain-focused data access patterns

## Performance & Scalability

### Async Operation Patterns
```python
# Efficient async service operations
class ResourceService:
    async def bulk_create_resources(
        self,
        commands: List[CreateResourceCommand]
    ) -> List[Resource]:
        async with self._uow:
            # Parallel validation
            validation_tasks = [
                self._validate_business_rules(cmd) for cmd in commands
            ]
            await asyncio.gather(*validation_tasks)

            # Batch creation
            resources = [
                Resource.create(**cmd.__dict__) for cmd in commands
            ]

            # Efficient bulk save
            return await self._repository.bulk_save(resources)
```

### Caching Integration
```python
# Multi-layer caching strategy
class ResourceService:
    @cache(expire=300, key_builder=resource_cache_key)
    async def get_resource_with_metadata(
        self,
        resource_id: int,
        include_relations: bool = False
    ) -> ResourceWithMetadata:
        return await self._build_resource_metadata(
            resource_id, include_relations
        )
```

### Background Task Processing
```python
# Asynchronous business operations
class ResourceService:
    async def schedule_resource_processing(
        self,
        resource_id: int,
        processing_type: ProcessingType
    ) -> TaskId:
        task = ProcessResourceTask(
            resource_id=resource_id,
            type=processing_type,
            scheduled_at=datetime.utcnow()
        )

        return await self._task_queue.enqueue(task)
```

## Transaction Management

### Unit of Work Implementation
```python
# Transaction management with rollback
class ResourceService:
    async def transfer_resource_ownership(
        self,
        resource_id: int,
        from_owner: int,
        to_owner: int
    ) -> TransferResult:
        async with self._uow:
            # Multi-step business operation
            resource = await self._repository.get_by_id(resource_id)
            await self._validate_ownership_transfer(resource, from_owner, to_owner)

            # Update ownership
            resource.transfer_ownership(to_owner)
            await self._repository.save(resource)

            # Create audit record
            audit_record = OwnershipTransferAudit.create(resource, from_owner, to_owner)
            await self._audit_repository.save(audit_record)

            # Publish domain event
            event = ResourceOwnershipTransferredEvent(resource, from_owner, to_owner)
            await self._events.publish(event)

            return TransferResult.success(resource)
```

### Error Handling & Rollback
```python
# Comprehensive error handling
class BusinessException(Exception):
    def __init__(self, message: str, error_code: str, details: Dict[str, Any] = None):
        self.message = message
        self.error_code = error_code
        self.details = details or {}

class ResourceService:
    async def complex_business_operation(self, request: ComplexRequest) -> Result:
        try:
            async with self._uow:
                result = await self._execute_complex_logic(request)
                await self._uow.commit()
                return Result.success(result)
        except ValidationError as e:
            await self._uow.rollback()
            raise BusinessException("Validation failed", "VALIDATION_ERROR", e.errors())
        except IntegrityError as e:
            await self._uow.rollback()
            raise BusinessException("Data integrity violation", "INTEGRITY_ERROR")
```

## Security & Authorization

### Business-Level Authorization
```python
# Authorization at service layer
class ResourceService:
    async def update_resource(
        self,
        resource_id: int,
        updates: UpdateResourceCommand,
        current_user: User
    ) -> Resource:
        resource = await self._repository.get_by_id(resource_id)

        # Business authorization check
        if not await self._authorization_service.can_update_resource(current_user, resource):
            raise AuthorizationError("Insufficient permissions to update resource")

        # Apply business rules for updates
        await self._validate_update_business_rules(resource, updates)

        # Execute update
        resource.apply_updates(updates)
        return await self._repository.save(resource)
```

### Input Sanitization & Validation
```python
# Business validation with custom rules
class ResourceValidationService:
    async def validate_create_resource_request(
        self,
        request: CreateResourceCommand,
        context: ValidationContext
    ) -> ValidationResult:
        errors = []

        # Business rule validation
        if not await self._is_name_unique_in_category(request.name, request.category):
            errors.append("Resource name must be unique within category")

        if not await self._user_can_create_in_category(request.owner_id, request.category):
            errors.append("User lacks permission to create resources in this category")

        # Complex business validation
        if request.category.requires_approval and not request.approval_reference:
            errors.append("Approval reference required for this category")

        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
```

## Integration Patterns

### External Service Integration
```python
# Circuit breaker pattern for external services
class ExternalIntegrationService:
    @circuit_breaker(failure_threshold=5, recovery_timeout=30)
    async def sync_with_external_system(
        self,
        resource: Resource
    ) -> SyncResult:
        try:
            response = await self._external_client.sync_resource(
                resource.to_external_format()
            )

            return SyncResult.success(response)
        except ExternalServiceError as e:
            logger.error(f"External sync failed: {e}")
            return SyncResult.failure(e.message)
```

### Event-Driven Integration
```python
# Domain event handling
class ResourceEventHandler:
    async def handle_resource_created(self, event: ResourceCreatedEvent):
        # Trigger downstream processes
        await self._notification_service.notify_stakeholders(event.resource)
        await self._analytics_service.track_resource_creation(event.resource)
        await self._search_service.index_resource(event.resource)
```

## Monitoring & Observability

### Business Metrics Collection
```python
# Business operation monitoring
class ResourceService:
    async def create_resource(self, command: CreateResourceCommand) -> Resource:
        start_time = time.time()

        try:
            result = await self._execute_create_resource(command)

            # Success metrics
            self._metrics.increment('resource.created', tags={
                'category': command.category.value,
                'owner_type': 'user' if command.owner_id else 'system'
            })

            return result
        except Exception as e:
            # Error metrics
            self._metrics.increment('resource.creation_failed', tags={
                'error_type': type(e).__name__,
                'category': command.category.value
            })
            raise
        finally:
            # Performance metrics
            duration = time.time() - start_time
            self._metrics.histogram('resource.creation_duration', duration)
```

### Audit Logging
```python
# Comprehensive audit logging
class AuditService:
    async def log_business_operation(
        self,
        operation: str,
        entity_id: int,
        entity_type: str,
        user_id: int,
        changes: Dict[str, Any] = None,
        metadata: Dict[str, Any] = None
    ):
        audit_record = AuditRecord(
            timestamp=datetime.utcnow(),
            operation=operation,
            entity_id=entity_id,
            entity_type=entity_type,
            user_id=user_id,
            changes=changes or {},
            metadata=metadata or {},
            correlation_id=get_correlation_id()
        )

        await self._audit_repository.save(audit_record)
```

## Expected Deliverables

This command produces the following implementation artifacts:

### 1. Core Service Architecture Implementation
**Comprehensive service layer architecture combining all foundational components:**
- **Application Services**: Use case orchestration and business flow control
- **Domain Services**: Complex business logic and domain rules implementation
- **Infrastructure Services**: External integration and technical concerns management
- **Repository Implementations**: Data access with proper abstraction patterns
- **Unit of Work Implementation**: Transaction management and consistency guarantees

### 2. Business Logic and Integration Components
**Complete business domain implementation with integration capabilities:**
- **Domain Models & Value Objects**: Rich business entities with behavior and immutable concepts
- **Business Rules Engine**: Configurable business validation and rule processing
- **Event & Command/Query Handlers**: Domain event processing and CQRS implementation
- **External Service Integration**: Third-party service clients with circuit breaker patterns
- **Asynchronous Processing**: Message queue handlers, cache services, and background task processors

### 3. Quality Assurance and Testing Suite
**Comprehensive testing and validation infrastructure:**
- **Service Tests**: Complete business logic testing with full coverage
- **Integration Tests**: External dependency and service interaction testing
- **Performance Tests**: Service layer benchmarking and optimization validation
- **Security Tests**: Authorization, validation, and vulnerability testing
- **Contract Tests**: API contract validation and compatibility verification

## Usage Examples

### Basic Service Implementation
```python
# Create a new business service
/fastapi-service-implement --domain users --pattern clean --transactions unit-of-work

# Advanced service with event integration
/fastapi-service-implement --domain orders --pattern cqrs --events rabbitmq --cache redis

# Microservice with external integrations
/fastapi-service-implement --domain payments --pattern microservice --integrations stripe,sendgrid
```

### Domain-Specific Services
```python
# E-commerce service implementation
/fastapi-service-implement --domain inventory --rules complex --audit full --tenancy multi

# Analytics service with background processing
/fastapi-service-implement --domain analytics --processing background --metrics prometheus
```

## Quality Standards

### Code Quality Metrics
<quality_thresholds>
  <code_quality>
    <metric name="Test Coverage" threshold="95%">Minimum business logic coverage</metric>
    <metric name="Cyclomatic Complexity" threshold="10">Maximum per method</metric>
    <metric name="Type Safety" threshold="100%">Full type annotations with mypy validation</metric>
    <metric name="Code Style" threshold="100%">Black formatting and Ruff linting compliance</metric>
    <metric name="Security" threshold="0 vulnerabilities">Bandit scanning and business logic security validation</metric>
  </code_quality>

  <performance_benchmarks>
    <metric name="Service Response Time" threshold="50ms/200ms">Simple/complex operations</metric>
    <metric name="Transaction Throughput" threshold="500+">Concurrent business operations</metric>
    <metric name="Memory Efficiency" threshold="optimal">Proper resource management and cleanup</metric>
    <metric name="Database Connections" threshold="pooled">Efficient connection pooling and management</metric>
    <metric name="Cache Hit Ratio" threshold="80%">Frequently accessed business data</metric>
  </performance_benchmarks>

  <business_logic_compliance>
    <requirement>SOLID Principles: Full compliance with all design principles</requirement>
    <requirement>Clean Architecture: Proper layer separation and dependency flow</requirement>
    <requirement>Domain-Driven Design: Proper bounded context and aggregate design</requirement>
    <requirement>Business Rule Coverage: All business rules tested and validated</requirement>
    <requirement>Audit Trail: Complete operation tracking and compliance</requirement>
  </business_logic_compliance>
</quality_thresholds>

## Command Integration

### Related Commands
- **Architecture Phase**: `/fastapi-architecture-design` - Overall service architecture
- **Planning Phase**: `/fastapi-implementation-planning` - Service implementation roadmap
- **Router Integration**: `/fastapi-router-implement` - Controller layer implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - Service layer validation
- **Refactoring**: `/fastapi-code-refactor` - Service improvement and optimization

### Workflow Navigation
```
Architecture  Planning  Service Implementation  Router Implementation  Quality Review
                                                                      
Domain Design  Roadmap  Business Logic  Controllers  Validation  Optimization
```

## MCP Integration

This command requires the following MCP tools for comprehensive service implementation:

### Core Development Tools
- **filesystem**: Create service modules and business logic implementations
- **context7**: Get latest FastAPI, SQLAlchemy, and architecture documentation
- **grep**: Find service implementation patterns from GitHub repositories
- **sequential-thinking**: Plan complex business logic and service architecture

### Business Logic Tools
- **memory**: Track business rules and implementation decisions
- **neo4j-memory**: Persist domain knowledge and architectural decisions
- **time**: Generate timestamps for audit trails and business operations

### Quality Assurance Tools
- **playwright**: Test service integrations and external API calls
- **fetch**: Validate external service documentation and integration patterns

This command ensures production-ready FastAPI service layer implementations that follow Clean Architecture principles, maintain business logic integrity, and deliver enterprise-grade performance and reliability.

<examples>
  <complete_service_workflow>
    <user_request>Implement a complete order management service with payment processing</user_request>
    <comprehensive_implementation>
      **MCP Workflow Execution:**
      1. **Context Loading**: Search neo4j-memory for e-commerce patterns and order processing
      2. **Research**: Use context7 for FastAPI async patterns, grep for order management examples
      3. **Planning**: Use sequential-thinking to design service architecture and data flow
      4. **Implementation**: Build complete service layer with Clean Architecture
      5. **Validation**: Run comprehensive tests and quality checks
      6. **Documentation**: Record patterns and decisions in neo4j-memory
      
      **Service Architecture Delivered:**
      ```python
      # Application Service Layer
      class OrderApplicationService:
          async def create_order(self, command: CreateOrderCommand) -> Order
          async def process_payment(self, order_id: int, payment: PaymentInfo) -> PaymentResult
          async def fulfill_order(self, order_id: int) -> FulfillmentResult
      
      # Domain Service Layer  
      class OrderDomainService:
          async def calculate_total(self, items: List[OrderItem]) -> Money
          async def validate_inventory(self, items: List[OrderItem]) -> ValidationResult
          async def apply_discounts(self, order: Order, customer: Customer) -> Order
      
      # Infrastructure Services
      class PaymentService:
          async def process_payment(self, amount: Money, method: PaymentMethod) -> PaymentResult
      
      class InventoryService:
          async def reserve_items(self, items: List[OrderItem]) -> ReservationResult
      ```
      
      **Quality Assurance Results:**
      - Test coverage: 97% (exceeds 95% requirement)
      - Security scan: 0 vulnerabilities
      - Performance: <200ms response time for order creation
      - Integration tests: All payment providers working
      - Business logic validation: All edge cases covered
    </comprehensive_implementation>
  </complete_service_workflow>

  <production_deployment_validation>
    <deployment_scenario>Service ready for production deployment validation</deployment_scenario>
    <validation_process>
      **Pre-Deployment Checklist:**
      
       **Code Quality (100% Required)**
      - MyPy type checking: 0 errors
      - Pytest coverage: 96% (exceeds minimum)
      - Ruff linting: 0 violations  
      - Bandit security: 0 vulnerabilities
      
       **Business Logic Completeness**
      - All use cases implemented with full business rules
      - Exception handling comprehensive with specific business exceptions
      - Transaction management with proper rollback capabilities
      - Audit logging for all business operations
      
       **Integration Validation**
      - Database connections with proper pooling
      - External service integration with circuit breakers
      - Message queue integration for async processing
      - Caching layer with proper invalidation strategies
      
       **Performance & Scalability**
      - Load testing: 500+ concurrent requests handled
      - Database query optimization validated
      - Memory usage profiled and optimized
      - Async operations properly implemented
      
      **Production Readiness Confirmed**: Service meets all enterprise standards
    </validation_process>
  </production_deployment_validation>

  <troubleshooting_guide>
    <issue_type>Common service implementation problems and solutions</issue_type>
    <diagnostic_approach>
      **Problem**: Service tests failing with database connection errors
      
      **Diagnosis Steps**:
      1. Check database connection configuration
      2. Verify async database client initialization
      3. Validate connection pool settings
      4. Test database migrations and schema
      
      **Solution Implementation**:
      ```python
      # Fixed database configuration
      async def get_database():
          engine = create_async_engine(
              settings.DATABASE_URL,
              pool_size=10,
              max_overflow=20,
              pool_pre_ping=True,
              pool_recycle=3600
          )
          async with AsyncSession(engine) as session:
              yield session
      ```
      
      **Prevention**: 
      - Add comprehensive database integration tests
      - Implement health checks for database connectivity
      - Add retry logic with exponential backoff
      - Monitor connection pool metrics
    </diagnostic_approach>
  </troubleshooting_guide>
</examples>