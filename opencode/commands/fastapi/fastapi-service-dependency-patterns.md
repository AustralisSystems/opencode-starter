# === FastAPI Service Layer & Dependency Injection: AI-Driven Service Architecture and DI Pattern Implementation ===

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

## SERVICE LAYER & DEPENDENCY INJECTION PRINCIPLES

**INDUSTRY-STANDARD SERVICE LAYER PRINCIPLES:**

### Clean Architecture Service Patterns

- **Business Logic Isolation**: Separate business logic from API and data layers
- **Dependency Inversion**: Depend on abstractions, not concretions
- **Single Responsibility**: Each service has a single, well-defined purpose
- **Interface Segregation**: Use focused interfaces for different concerns
- **Domain-Driven Design**: Align services with business domains

### FastAPI Dependency Injection Best Practices

- **Typed Dependencies**: Use Annotated types for all dependencies
- **Dependency Scoping**: Implement appropriate lifecycle management
- **Sub-Dependencies**: Chain dependencies for complex object graphs
- **Dependency Overrides**: Support testing with dependency substitution
- **Lazy Evaluation**: Use callable dependencies for performance

### Service Layer Architecture Patterns

- **Use Case Implementation**: Each service method implements a specific use case
- **Repository Abstraction**: Services depend on repository interfaces
- **Event Publishing**: Services publish domain events for decoupling
- **Transaction Management**: Handle database transactions at service level
- **Error Handling**: Convert domain exceptions to appropriate responses

### Dependency Lifecycle Management

- **Singleton Dependencies**: Shared resources like database connections
- **Request-Scoped**: Dependencies that live for the request duration
- **Transient Dependencies**: New instance for each dependency resolution
- **Context-Managed**: Dependencies with explicit setup/teardown

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **FASTAPI SERVICE & DI PATTERN DESIGN-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR FASTAPI SERVICE & DI PATTERN DESIGN ONLY:**

- **MUST:** Create comprehensive service layer architectures and DI pattern designs
- **MUST:** Design complete FastAPI dependency injection hierarchies and patterns
- **MUST:** Apply Clean Architecture and Domain-Driven Design principles
- **MUST:** Design service interfaces, implementations, and dependency chains
- **FORBIDDEN:** Creating implementation code or actual FastAPI modules
- **FORBIDDEN:** Creating test specifications or test designs
- **FORBIDDEN:** Generating incomplete or placeholder designs
- **MUST:** Output design documentation in markdown documents only

**FASTAPI SERVICE & DI PATTERN DESIGN FOCUS AREAS:**

- Service layer architecture and business logic organization
- FastAPI dependency injection patterns and type-safe implementations
- Repository pattern interfaces and service layer integration
- Domain service design and business rule encapsulation
- Application service patterns and use case implementations
- Dependency scoping and lifecycle management design
- Service composition and orchestration patterns
- Error handling and exception management in services
- Event-driven service communication patterns
- Service testing strategies and dependency mocking

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `fastapi-service-dependency-patterns-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for service_domain and architecture_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the service design protocol specifications
4. **VERIFY COMPLETION**: Ensure all objectives and outcomes have been met
5. **DOCUMENT RESULTS**: Create comprehensive service layer design documentation
6. **VALIDATE COMPLIANCE**: Confirm 100% design completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "fastapi-service-dependency-patterns-prompt"
arguments:
  service_domain: "[user-management|order-processing|inventory|notification|analytics]"
  architecture_complexity: "[simple-services|domain-services|enterprise-services|distributed-services]"
  di_pattern_focus: "[optional: basic-injection|advanced-patterns|lifecycle-management|testing-patterns]"
  business_logic_complexity: "[optional: simple-crud|complex-workflows|domain-heavy|event-driven]"
  integration_requirements: "[optional: database-only|external-apis|message-queues|all-integrations]"
  testing_strategy: "[optional: unit-focused|integration-focused|comprehensive-mocking]"
```

### **COMPREHENSIVE SERVICE LAYER DESIGN PATTERNS:**

#### 1. Service Layer Architecture

**Three-Tier Service Architecture:**

```

     API Layer             Controllers/Routers
  (FastAPI Endpoints)



   Service Layer           Business Logic
 (Application Services)



     Data Layer            Repositories/CRUD
   (Repository Pattern)

```

**Domain-Driven Service Organization:**

```python
# Domain Service (Business Logic)
class UserDomainService:
    """Encapsulates business rules and domain logic"""

    def validate_user_creation(self, user_data: UserCreate) -> None:
        # Domain validation logic
        pass

    def calculate_user_permissions(self, user: User, context: Context) -> Permissions:
        # Business logic for permission calculation
        pass

# Application Service (Use Cases)
class UserApplicationService:
    """Coordinates between domain services and repositories"""

    def __init__(
        self,
        user_repository: UserRepository,
        user_domain_service: UserDomainService,
        event_publisher: EventPublisher
    ):
        self.user_repository = user_repository
        self.domain_service = user_domain_service
        self.event_publisher = event_publisher

    async def create_user(self, user_data: UserCreate) -> User:
        # Orchestrate the use case
        self.domain_service.validate_user_creation(user_data)
        user = await self.user_repository.create(user_data)
        await self.event_publisher.publish(UserCreatedEvent(user.id))
        return user
```

#### 2. FastAPI Dependency Injection Patterns

**Basic Type-Safe Dependencies:**

```python
from typing import Annotated
from fastapi import Depends

# Database session dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

DatabaseSession = Annotated[AsyncSession, Depends(get_db)]

# Repository dependencies
def get_user_repository(db: DatabaseSession) -> UserRepository:
    return SQLUserRepository(db)

UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]

# Service dependencies
def get_user_service(
    user_repo: UserRepositoryDep,
    domain_service: Annotated[UserDomainService, Depends()]
) -> UserApplicationService:
    return UserApplicationService(user_repo, domain_service)

UserServiceDep = Annotated[UserApplicationService, Depends(get_user_service)]
```

**Advanced Dependency Patterns:**

```python
# Dependency with configuration
def get_email_service(
    settings: Annotated[Settings, Depends(get_settings)]
) -> EmailService:
    if settings.email_backend == "smtp":
        return SMTPEmailService(settings.smtp_config)
    elif settings.email_backend == "sendgrid":
        return SendGridEmailService(settings.sendgrid_api_key)
    else:
        return MockEmailService()

# Context-dependent dependencies
def get_current_user_service(
    request: Request,
    user_repo: UserRepositoryDep
) -> UserService:
    correlation_id = request.headers.get("x-correlation-id")
    return UserService(user_repo, correlation_id=correlation_id)

# Cached/Singleton dependencies
@lru_cache()
def get_cache_service() -> CacheService:
    return RedisCache(url="redis://localhost:6379")
```

#### 3. Repository Pattern Integration

**Abstract Repository Interface:**

```python
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(ABC, Generic[T, ID]):
    """Generic repository interface"""

    @abstractmethod
    async def get_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    async def create(self, entity: T) -> T:
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, id: ID) -> bool:
        pass

    @abstractmethod
    async def list(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass

class UserRepository(Repository[User, UUID]):
    """Domain-specific repository interface"""

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_active_users(self) -> List[User]:
        pass
```

**Concrete Repository Implementation:**

```python
class SQLUserRepository(UserRepository):
    """SQLAlchemy implementation of UserRepository"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, id: UUID) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    # ... other implementations
```

#### 4. Unit of Work Pattern

**Unit of Work for Transaction Management:**

```python
class UnitOfWork(ABC):
    """Abstract Unit of Work pattern"""

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass

class SQLUnitOfWork(UnitOfWork):
    """SQLAlchemy Unit of Work implementation"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

# Service using Unit of Work
class UserService:
    async def create_user_with_profile(
        self,
        user_data: UserCreate,
        profile_data: ProfileCreate,
        uow: UnitOfWork
    ) -> User:
        async with uow:
            user = await self.user_repo.create(user_data)
            profile = await self.profile_repo.create(profile_data, user.id)
            # Both operations committed together
            return user
```

#### 5. Service Composition Patterns

**Service Orchestration:**

```python
class OrderService:
    """Orchestrates multiple services for complex workflows"""

    def __init__(
        self,
        order_repo: OrderRepository,
        inventory_service: InventoryService,
        payment_service: PaymentService,
        notification_service: NotificationService,
        event_publisher: EventPublisher
    ):
        self.order_repo = order_repo
        self.inventory_service = inventory_service
        self.payment_service = payment_service
        self.notification_service = notification_service
        self.event_publisher = event_publisher

    async def create_order(self, order_data: OrderCreate) -> Order:
        """Orchestrate order creation workflow"""

        # 1. Validate inventory
        await self.inventory_service.reserve_items(order_data.items)

        try:
            # 2. Process payment
            payment = await self.payment_service.charge(
                order_data.payment_info,
                order_data.total_amount
            )

            # 3. Create order
            order = await self.order_repo.create(order_data)

            # 4. Publish events
            await self.event_publisher.publish(OrderCreatedEvent(order.id))

            # 5. Send notifications
            await self.notification_service.send_order_confirmation(order)

            return order

        except PaymentException:
            # Compensate - release reserved inventory
            await self.inventory_service.release_reservation(order_data.items)
            raise
```

#### 6. Event-Driven Service Communication

**Event Publisher Pattern:**

```python
class EventPublisher(ABC):
    """Abstract event publisher interface"""

    @abstractmethod
    async def publish(self, event: DomainEvent) -> None:
        pass

class AsyncEventPublisher(EventPublisher):
    """Async in-memory event publisher"""

    def __init__(self):
        self.handlers: Dict[Type[DomainEvent], List[EventHandler]] = {}

    def subscribe(self, event_type: Type[DomainEvent], handler: EventHandler):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    async def publish(self, event: DomainEvent) -> None:
        event_type = type(event)
        if event_type in self.handlers:
            tasks = [handler.handle(event) for handler in self.handlers[event_type]]
            await asyncio.gather(*tasks)

# Event handlers
class UserCreatedEventHandler:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    async def handle(self, event: UserCreatedEvent) -> None:
        # Send welcome email
        await self.email_service.send_welcome_email(event.user_id)
```

#### 7. Dependency Scoping and Lifecycle

**Dependency Scopes:**

```python
# Application-scoped (Singleton)
@lru_cache()
def get_settings() -> Settings:
    return Settings()

# Request-scoped
async def get_current_user(
    request: Request,
    user_service: UserServiceDep
) -> User:
    token = request.headers.get("Authorization")
    return await user_service.get_user_by_token(token)

# Transient (New instance each time)
def get_correlation_id() -> str:
    return str(uuid.uuid4())

# Context-managed (with setup/teardown)
class DatabaseConnection:
    async def __aenter__(self):
        self.connection = await create_connection()
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

async def get_db_connection():
    async with DatabaseConnection() as conn:
        yield conn
```

#### 8. Testing Patterns for Services

**Service Testing with Dependency Injection:**

```python
# Test configuration
def get_test_db():
    # Return test database session
    pass

def get_mock_email_service():
    return Mock(spec=EmailService)

# Override dependencies for testing
app.dependency_overrides[get_db] = get_test_db
app.dependency_overrides[get_email_service] = get_mock_email_service

# Unit test example
async def test_create_user():
    # Arrange
    user_data = UserCreate(username="test", email="test@example.com")
    mock_repo = Mock(spec=UserRepository)
    mock_repo.create.return_value = User(id=1, username="test")

    service = UserService(mock_repo)

    # Act
    result = await service.create_user(user_data)

    # Assert
    assert result.username == "test"
    mock_repo.create.assert_called_once()
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All service design phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive service layer architecture designed
- [ ] Complete dependency injection patterns and hierarchies created (timestamped)
- [ ] Repository pattern interfaces and implementations designed (timestamped)
- [ ] Service composition and orchestration patterns specified (timestamped)
- [ ] Dependency scoping and lifecycle management designed (timestamped)
- [ ] Event-driven communication patterns defined (timestamped)
- [ ] Error handling and transaction management designed (timestamped)
- [ ] Testing strategies and dependency mocking patterns specified (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL FASTAPI SERVICE & DI PATTERN DESIGN OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All design deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All service architecture documentation includes precise timestamps
- [ ] All dependency injection design documents include timestamp documentation
- [ ] All repository pattern designs include proper date stamps
- [ ] All service composition designs follow consistent date stamp format
- [ ] All testing strategy documents include timestamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating design files without proper reverse date stamps
- Using inconsistent date formats within same design session
- Missing timestamps in service design documentation

### **FASTAPI SERVICE & DI PATTERN DESIGN DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/python/Implementation_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Complete implementation details with all components and modules
2. **`./project/docs/testing/python/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/quality/python/Quality_Assessment_{YYYYMMDD-HHMMSS}.ipynb`** - Code quality metrics, analysis, and compliance assessment

**NEXT PHASE PREPARATION:**

```bash
# After service design approval, proceed to implementation with:
/fastapi-service-implement [service-domain] [implementation-scope] [design-source]

# Examples:
/fastapi-service-implement user-management comprehensive service-designs
/fastapi-service-implement order-processing core-services architecture-documents
/fastapi-service-implement inventory-management domain-services design-specifications
```

## Command Integration

### Related Commands

- **Architecture Phase**: `/fastapi-architecture-design` - Overall application architecture design
- **Planning Phase**: `/fastapi-implementation-planning` - Implementation roadmap and task breakdown
- **API Design**: `/fastapi-api-endpoint-design` - RESTful API endpoint specifications
- **Service Implementation**: `/fastapi-service-implement` - Service layer implementation
- **Router Implementation**: `/fastapi-router-implement` - Router-specific implementation
- **Application Implementation**: `/fastapi-application-implement` - Full application implementation
- **Quality Assurance**: `/fastapi-code-quality-review` - Service pattern validation

### Workflow Navigation

```
Architecture Design  Implementation Planning  Service Patterns  Service Implementation  Quality Review

   Domain Models      Task Breakdown      Service Design       Business Logic        Validation
```

### Next Phase Commands

After completing service dependency pattern design, proceed with:

1. `/fastapi-service-implement` - Implement the designed service patterns
2. `/fastapi-router-implement` - Implement API controllers with service integration
3. `/fastapi-application-implement` - Full application implementation

---

**ENFORCEMENT:** This command performs FASTAPI SERVICE & DI PATTERN DESIGN ONLY through the MCP prompt protocol. The comprehensive design logic is defined in `fastapi-service-dependency-patterns-prompt.yaml` and executed according to Model Context Protocol standards. No implementation code creation allowed. Use implementation commands for actual FastAPI development after design is complete and approved.

---
