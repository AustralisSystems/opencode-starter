# Node.js Framework Planning Command

**YAML Prompt**: `nodejs-framework-planning-prompt.yaml`

## Purpose
Strategic planning for Node.js backend framework selection, architecture design, and implementation roadmap based on project requirements.

## MCP Tool Requirements
- `context7` - Latest framework documentation and performance comparisons
- `grep` - Real-world production implementations on GitHub
- `sequential-thinking` - Structured framework evaluation methodology
- `filesystem` - Project requirements and constraints analysis
- `memory` - Track planning decisions and rationale
- `time` - Timestamp planning activities

## Framework Evaluation Matrix

### Express.js v5.x
- **Characteristics**: Minimalist, flexible, mature ecosystem
- **Best For**: REST APIs, rapid prototyping, web applications
- **Performance**: Good with proper optimization
- **Learning Curve**: Low - industry standard

### Fastify v4.x
- **Characteristics**: High performance, schema-based, plugin architecture
- **Best For**: High-performance APIs, microservices, JSON-heavy applications
- **Performance**: Excellent out-of-the-box (2x faster than Express)
- **Learning Curve**: Medium - modern patterns

### NestJS v10+
- **Characteristics**: Enterprise-grade, TypeScript-first, Angular-inspired
- **Best For**: Large applications, enterprise systems, complex business logic
- **Performance**: Good with some overhead
- **Learning Curve**: High - comprehensive framework

## Architecture Pattern Selection

### Clean Architecture Implementation
```javascript
// Domain Layer (entities)
export class User {
  constructor(id, email, hashedPassword) {
    this.id = id;
    this.email = email;
    this.hashedPassword = hashedPassword;
  }
}

// Use Case Layer (business logic)
export class AuthenticateUserUseCase {
  constructor(userRepository, passwordService, tokenService) {
    this.userRepository = userRepository;
    this.passwordService = passwordService;
    this.tokenService = tokenService;
  }

  async execute(email, password) {
    const user = await this.userRepository.findByEmail(email);
    if (!user || !await this.passwordService.verify(password, user.hashedPassword)) {
      throw new Error('Invalid credentials');
    }
    return this.tokenService.generate(user.id);
  }
}
```

## Database and ORM Selection

### PostgreSQL with Prisma (Recommended)
```javascript
// Modern type-safe database operations
const user = await prisma.user.create({
  data: {
    email: 'user@example.com',
    hashedPassword: await hash(password),
    profile: {
      create: {
        firstName: 'John',
        lastName: 'Doe'
      }
    }
  },
  include: {
    profile: true
  }
});
```

### Alternative Options
- **Drizzle ORM**: Lightweight, SQL-first approach
- **MongoDB with Mongoose**: NoSQL flexibility
- **Redis**: Caching and session management

## Security Implementation Strategy
```javascript
// Production helmet.js configuration
app.use(helmet({
  contentSecurityPolicy: false,  // Disabled in most production apps
  crossOriginEmbedderPolicy: false
}));

// JWT authentication with proper configuration
const token = jwt.sign(
  { userId: user.id, role: user.role },
  process.env.JWT_SECRET,
  {
    expiresIn: '1h',
    issuer: 'your-app-name',
    audience: 'your-app-users'
  }
);
```

## Decision Framework

### Evaluation Criteria (Weighted Scoring)
- **Performance**: 25% - Throughput and response times
- **Developer Experience**: 20% - Learning curve and productivity
- **Ecosystem Maturity**: 15% - Community and library support
- **Business Alignment**: 15% - Time to market and requirements fit
- **Long-term Viability**: 15% - Maintenance and upgrade path
- **Team Readiness**: 10% - Existing skills and hiring

### Risk Assessment Categories
- **Technical**: Framework abandonment, performance bottlenecks
- **Business**: Development timeline, hiring challenges
- **Operational**: Production stability, scaling complexity

## Implementation Roadmap Template

### Phase 1: Foundation (2-3 weeks)
- Framework setup and basic project structure
- Database integration and ORM configuration
- Authentication middleware implementation
- Initial API endpoint development

### Phase 2: Core Features (4-6 weeks)
- Business logic implementation
- API validation and error handling
- Testing framework setup and coverage
- Security hardening and middleware

### Phase 3: Optimization (2-3 weeks)
- Performance optimization and caching
- Production deployment configuration
- Monitoring and observability integration
- Documentation and deployment guides

## Deliverables
1. **Framework Analysis and Selection** - Comparison matrix with recommendations
2. **Architecture Design and Implementation Plan** - Detailed technical roadmap

## Success Criteria
- Framework selection supported by evidence and benchmarking
- Architecture design aligns with business objectives and scale requirements
- Implementation timeline is realistic with defined milestones
- Risk mitigation strategies address identified concerns

## Command Integration
- **Follow-up**: `nodejs-backend-architecture-design`
- **Parallel**: `nodejs-gap-analysis` (for existing projects)
- **Next Phase**: `nodejs-backend-implementation`

**Note**: This is a planning command that produces comprehensive framework selection and architecture planning documentation.