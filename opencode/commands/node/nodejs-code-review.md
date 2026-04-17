# Node.js Code Review Command

**YAML Prompt**: `nodejs-code-review-prompt.yaml`

## Purpose
Comprehensive code review for Node.js backend applications with focus on security, performance, architecture, and maintainability.

## MCP Tool Requirements
- `context7` - Latest Node.js best practices and security patterns
- `grep` - Real-world production implementations on GitHub
- `sequential-thinking` - Structured review approach
- `filesystem` - Code analysis and file reading
- `memory` - Track findings during review session
- `time` - Timestamp review activities

## Review Focus Areas

### 1. Node.js 21.x LTS Compliance
- Built-in test runner usage and implementation
- Permission model utilization where applicable
- Modern ES modules with `node:` protocol
- Updated crypto APIs and security features

### 2. Backend Framework Patterns
- **Express.js v5.x**: Middleware patterns, error handling, route organization
- **Fastify v4.x**: Schema validation, plugin architecture, performance optimization
- **NestJS v10+**: Dependency injection, decorators, module structure

### 3. Security Implementation Review
```javascript
// Production helmet.js configuration (validate against production usage)
app.use(helmet({
  contentSecurityPolicy: false,  // Most production apps disable this
  crossOriginEmbedderPolicy: false
}));

// JWT authentication patterns
const token = jwt.sign(payload, process.env.JWT_SECRET, {
  expiresIn: '1h',
  issuer: 'your-app',
  audience: 'your-users'
});
```

### 4. Database and ORM Patterns
- **PostgreSQL**: Connection pooling, query optimization, transaction handling
- **Prisma/Drizzle**: Type safety, migration patterns, query efficiency
- **Redis**: Caching strategies, session management, pub/sub patterns

### 5. Architecture Quality Checks
- Clean Architecture compliance (entities, use cases, adapters)
- SOLID principles implementation
- Error handling consistency and proper HTTP status codes
- Async/await patterns and promise management

## Deliverables
1. **Code Review Analysis Report** - Detailed findings with severity ratings
2. **Implementation Guide** - Specific fixes with before/after examples

## Quality Scoring Framework
- **A (90-100%)**: Production ready, minimal issues
- **B (80-89%)**: Good quality, minor improvements needed
- **C (70-79%)**: Acceptable, moderate issues to address
- **D (60-69%)**: Below standard, significant improvements required
- **F (<60%)**: Major issues, substantial refactoring needed

## Critical Review Items
- Security headers and input validation coverage
- Database connection handling and query optimization
- Error handling consistency across all endpoints
- Test coverage adequacy and quality
- Performance bottlenecks and memory usage patterns

## Command Integration
- **Prerequisite**: `nodejs-backend-implementation`
- **Parallel**: `nodejs-code-quality-analysis`
- **Follow-up**: `nodejs-gap-analysis`

**Note**: This is an analysis command that produces comprehensive review reports, not implementation code.