# Node.js Architecture Design Command

**YAML Prompt**: `nodejs-architecture-design-prompt.yaml`

## Purpose
Design comprehensive Node.js backend architecture, system specifications, and API structure for production-ready applications.

## MCP Tool Requirements
- `context7` - Latest Node.js architecture patterns and design principles
- `grep` - Production architecture examples on GitHub
- `sequential-thinking` - Structured architecture design methodology
- `filesystem` - Requirements analysis and existing code review
- `memory` - Track design decisions and rationale
- `time` - Timestamp design activities

## Architecture Design Focus

### 1. System Architecture Patterns
- **Clean Architecture**: Domain-driven design with clear layer separation
- **Hexagonal Architecture**: Port and adapter pattern for external integrations
- **Layered Architecture**: Traditional N-tier architecture with clear boundaries
- **Event-Driven Architecture**: Async messaging and event sourcing patterns

### 2. Node.js 21.x LTS Architecture
```javascript
// Modern ES modules architecture
// Domain Layer
export class User {
  constructor(id, email, preferences) {
    this.id = id;
    this.email = email;
    this.preferences = preferences;
  }
}

// Use Case Layer
export class CreateUserUseCase {
  constructor(userRepository, emailService) {
    this.userRepository = userRepository;
    this.emailService = emailService;
  }

  async execute(userData) {
    const user = new User(generateId(), userData.email, userData.preferences);
    await this.userRepository.save(user);
    await this.emailService.sendWelcome(user.email);
    return user;
  }
}
```

### 3. Database Architecture Design
- **PostgreSQL**: Relational data with ACID compliance and complex queries
- **MongoDB**: Document storage for flexible schemas and rapid iteration
- **Redis**: Caching layer, session storage, and pub/sub messaging
- **Connection Pooling**: Optimize database connections and performance

### 4. API Architecture Patterns
- **RESTful Design**: Resource-based URLs with proper HTTP methods
- **GraphQL Integration**: Flexible query language for complex data needs
- **API Versioning**: Backward compatibility and evolution strategies
- **Rate Limiting**: Request throttling and abuse prevention

### 5. Security Architecture
```javascript
// Production security middleware stack
app.use(helmet({
  contentSecurityPolicy: false,  // Most production apps disable this
  crossOriginEmbedderPolicy: false
}));

// Authentication architecture
const authMiddleware = async (req, res, next) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = await userService.findById(decoded.userId);
    next();
  } catch (error) {
    res.status(401).json({ error: 'Unauthorized' });
  }
};
```

### 6. Performance Architecture
- **Async/Await Patterns**: Non-blocking I/O optimization
- **Caching Strategy**: Multi-layer caching with Redis and in-memory
- **Load Balancing**: Horizontal scaling and traffic distribution
- **Database Optimization**: Query optimization and indexing strategy

## Framework-Specific Architecture

### Express.js v5.x Architecture
- Middleware-based request pipeline
- Router-based modular organization
- Error handling middleware chain
- Custom middleware for cross-cutting concerns

### Fastify v4.x Architecture
- Plugin-based architecture with encapsulation
- Schema-first validation and serialization
- Lifecycle hooks for request/response processing
- Performance-optimized request handling

### NestJS v10+ Architecture
- Decorator-based dependency injection
- Module-based application structure
- Guard and interceptor patterns
- Enterprise-grade architectural patterns

## Deliverables
1. **System Architecture Design** - High-level architecture with component diagrams
2. **Database Design Specification** - Schema design and relationship modeling

## Success Criteria
- Architecture aligns with business requirements and scale projections
- Design patterns support maintainability and testability
- Performance characteristics meet defined SLAs
- Security architecture addresses identified threat models

## Command Integration
- **Follow-up**: `nodejs-implementation`
- **Parallel**: `nodejs-framework-planning` (if framework not yet selected)
- **Prerequisites**: Project requirements and business objectives

**Note**: This is a design command that produces comprehensive architecture documentation, not implementation code.