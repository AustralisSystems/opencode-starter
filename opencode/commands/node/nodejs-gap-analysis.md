# Node.js Gap Analysis Command

**YAML Prompt**: `nodejs-gap-analysis-prompt.yaml`

## Purpose
Comprehensive gap analysis comparing current Node.js implementation against industry best practices, modern patterns, and business requirements.

## MCP Tool Requirements
- `context7` - Latest Node.js industry standards and benchmarks
- `grep` - Production implementations and best practices on GitHub
- `sequential-thinking` - Structured gap analysis methodology
- `filesystem` - Current implementation analysis
- `memory` - Track analysis findings and decisions
- `time` - Timestamp gap analysis activities

## Analysis Domains

### 1. Technology Stack Currency
- **Node.js Version**: Current vs 21.x LTS feature utilization
- **Framework Versions**: Express v5.x, Fastify v4.x, NestJS v10+
- **Database Integration**: PostgreSQL, MongoDB, Redis optimization
- **ORM/Query Builder**: Prisma vs Drizzle vs TypeORM effectiveness
- **Security Libraries**: helmet.js, JWT, validation library currency

### 2. Architecture Pattern Maturity
```javascript
// Clean Architecture implementation assessment
// Domain Layer (entities, value objects)
class User {
  constructor(id, email, hashedPassword) {
    this.id = id;
    this.email = email;
    this.hashedPassword = hashedPassword;
  }
}

// Use Case Layer (business logic)
class AuthenticateUser {
  constructor(userRepository, passwordService) {
    this.userRepository = userRepository;
    this.passwordService = passwordService;
  }
}
```

### 3. Performance Optimization Maturity
- **Connection Pooling**: Database connection management effectiveness
- **Caching Strategy**: Redis implementation and hit rates
- **Async Patterns**: Promise handling and event loop optimization
- **Memory Management**: Garbage collection and leak prevention
- **Response Times**: API endpoint performance benchmarking

### 4. Security Implementation Gaps
- Authentication flow robustness and JWT handling
- Input validation coverage and sanitization completeness
- Environment variable and secret management practices
- Dependency vulnerability management and scanning

### 5. Development Process Maturity
- **Code Quality**: ESLint, Prettier, TypeScript integration
- **Testing Strategy**: Unit, integration, end-to-end coverage
- **CI/CD Pipeline**: Deployment automation and validation
- **Documentation**: API documentation and development guides

## Gap Classification Framework

### Critical Gaps (P0)
- Security vulnerabilities or compliance violations
- Performance issues affecting user experience
- Architectural decisions blocking scalability
- Major version dependencies with known issues

### Strategic Gaps (P1)
- Technology stack modernization opportunities
- Architecture improvements for maintainability
- Development process enhancements
- Performance optimization with measurable ROI

### Tactical Gaps (P2)
- Code quality and consistency improvements
- Documentation and knowledge sharing gaps
- Developer experience optimizations
- Minor dependency updates

## Maturity Assessment Levels
- **Level 5**: Optimizing - Continuous improvement and innovation
- **Level 4**: Quantitatively Managed - Performance monitoring and optimization
- **Level 3**: Defined - Well-architected with documented best practices
- **Level 2**: Managed - Organized code with standard practices
- **Level 1**: Basic - Working functionality with minimal optimization

## Deliverables
1. **Gap Analysis Executive Summary** - Business impact and investment priorities
2. **Detailed Assessment by Domain** - Technical gaps with benchmarking
3. **Implementation Roadmap** - Prioritized improvement phases with timelines

## Success Metrics Definition
- **Response Time**: <200ms average for API endpoints
- **Error Rate**: <0.1% for production requests
- **Test Coverage**: >85% line coverage
- **Security**: Zero critical/high vulnerabilities
- **Development Velocity**: 25% faster feature delivery
- **System Reliability**: 99.9% uptime target

## Implementation Phases
- **Phase 1 (Months 1-2)**: Critical gaps and security fixes
- **Phase 2 (Months 3-4)**: Architecture improvements and tooling
- **Phase 3 (Months 5-6)**: Performance optimization and advanced features

## Command Integration
- **Prerequisite**: `nodejs-code-review`, `nodejs-code-quality-analysis`
- **Parallel**: `nodejs-framework-planning`
- **Follow-up**: `nodejs-backend-architecture-design` (for next iteration)

**Note**: This is an analysis command that produces comprehensive gap assessment reports and improvement roadmaps.