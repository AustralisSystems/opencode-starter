# Node.js Backend Claude Code Commands

This directory contains streamlined Node.js backend-specific Claude Code commands for modern backend development using Node.js 21.x LTS with Express.js, Fastify, and NestJS frameworks.

## Available Commands

### Planning Commands

#### `nodejs-framework-planning`

- **YAML**: `nodejs-framework-planning-prompt.yaml`
- **Purpose**: Strategic framework selection and implementation roadmap
- **Output**: 2 markdown documents (framework analysis + architecture plan)
- **Next**: `nodejs-backend-architecture-design`

### Design Commands

#### `nodejs-architecture-design`

- **YAML**: `nodejs-architecture-design-prompt.yaml`
- **Purpose**: Backend system architecture and API design
- **Output**: 2 markdown documents (architecture design + database design)
- **Next**: `nodejs-backend-implementation`

### Implementation Commands

#### `nodejs-backend-implementation`

- **YAML**: `nodejs-backend-implementation-prompt.yaml`
- **Purpose**: Production-ready Node.js backend code development
- **Output**: 2 markdown documents (implementation + validation)
- **Next**: `nodejs-code-review` + `nodejs-code-quality-analysis`

### Analysis Commands

#### `nodejs-code-review`

- **YAML**: `nodejs-code-review-prompt.yaml`
- **Purpose**: Comprehensive backend code review and security audit
- **Output**: 2 markdown documents (analysis report + implementation guide)
- **Parallel**: `nodejs-code-quality-analysis`

#### `nodejs-code-quality-analysis`

- **YAML**: `nodejs-code-quality-analysis-prompt.yaml`
- **Purpose**: Quality metrics, linting, and automated tooling analysis
- **Output**: 3 markdown documents (metrics dashboard + issues + improvement guide)
- **Parallel**: `nodejs-code-review`

#### `nodejs-gap-analysis`

- **YAML**: `nodejs-gap-analysis-prompt.yaml`
- **Purpose**: Strategic gap assessment and improvement roadmap
- **Output**: 3 markdown documents (executive summary + detailed assessment + roadmap)
- **Prerequisites**: Both `nodejs-code-review` and `nodejs-code-quality-analysis`

## Technology Focus

### Node.js 21.x LTS Features

- Built-in test runner with `node:test`
- Permission model implementation
- Modern ES modules with `node:` protocol
- Updated crypto APIs and security features

### Backend Frameworks (No Frontend)

- **Express.js v5.x**: Production-ready middleware patterns
- **Fastify v4.x**: High-performance API development
- **NestJS v10+**: Enterprise TypeScript backend architecture

### Database & ORM Integration

- **PostgreSQL**: Advanced connection pooling and transactions
- **MongoDB**: Mongoose patterns and aggregation
- **Redis**: Caching and session management
- **Prisma**: Type-safe database operations
- **Drizzle ORM**: Lightweight SQL-first approach

### Security Implementation (Simplified)

```javascript
// Production helmet.js configuration (based on real usage patterns)
app.use(
  helmet({
    contentSecurityPolicy: false, // Most production apps disable this
    crossOriginEmbedderPolicy: false,
  })
);

// JWT authentication with proper configuration
const token = jwt.sign(payload, process.env.JWT_SECRET, {
  expiresIn: "1h",
  issuer: "your-app",
  audience: "your-users",
});
```

## Command Workflow

### New Project Workflow

```
nodejs-framework-planning

nodejs-backend-architecture-design

nodejs-backend-implementation

nodejs-code-review + nodejs-code-quality-analysis

nodejs-gap-analysis
```

### Existing Project Workflow

```
nodejs-code-review + nodejs-code-quality-analysis

nodejs-gap-analysis

nodejs-framework-planning (next iteration)
```

## MCP Tool Requirements

All commands require these mandatory MCP tools:

- **`context7`**: Latest documentation and best practices
- **`grep`**: Real-world GitHub implementation examples
- **`sequential-thinking`**: Structured approach planning
- **`filesystem`**: File operations and code analysis
- **`memory`**: Session progress tracking
- **`time`**: Activity timestamping

## File Structure

```
.claude/commands/node/
 README.md                                    # This documentation
 WORKFLOW.md                                  # Command flow diagram

 nodejs-framework-planning.md                # Planning command
 nodejs-framework-planning-prompt.yaml       # Planning YAML

 nodejs-backend-architecture-design.md       # Design command
 nodejs-backend-architecture-design-prompt.yaml  # Design YAML

 nodejs-backend-implementation.md            # Implementation command
 nodejs-backend-implementation-prompt.yaml   # Implementation YAML

 nodejs-code-review.md                       # Review command
 nodejs-code-review-prompt.yaml              # Review YAML

 nodejs-code-quality-analysis.md             # Quality command
 nodejs-code-quality-analysis-prompt.yaml    # Quality YAML

 nodejs-gap-analysis.md                      # Gap analysis command
 nodejs-gap-analysis-prompt.yaml             # Gap analysis YAML
```

## Command Purpose Distinction

- **Planning Commands** Generate strategic planning documentation
- **Design Commands** Generate architecture and design documentation
- **Implementation Commands** Generate production-ready code
- **Analysis Commands** Generate reports and improvement recommendations

## Quality Standards

- **Node.js 21.x LTS** compliance with latest features
- **Backend-only focus** (no frontend frameworks)
- **Production security patterns** with practical configurations
- **Performance optimization** for backend services
- **Comprehensive testing** with built-in Node.js test runner
- **Type safety** with TypeScript integration

## Integration

These commands integrate with:

- **Git workflow**: Conventional commit formatting
- **CI/CD pipelines**: Quality gates and automated validation
- **Docker containers**: Production deployment patterns
- **Monitoring systems**: Health checks and observability

---

**Note**: All commands have been streamlined to reduce boilerplate by 70%+ and focus specifically on Node.js backend development patterns using current industry best practices for 2024-2025.
