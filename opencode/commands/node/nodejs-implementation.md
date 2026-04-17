# Node.js Implementation Command

**YAML Prompt**: `nodejs-implementation-prompt.yaml`

## Purpose
Implement production-ready Node.js backend services, APIs, and infrastructure using current patterns and best practices.

## MCP Tool Requirements
- `context7` - Latest documentation for chosen frameworks
- `grep` - Real-world production implementations on GitHub
- `sequential-thinking` - Structured implementation approach
- `filesystem` - Code generation and file management
- `memory` - Track implementation progress and decisions
- `time` - Timestamp development activities

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

## Implementation Focus Areas

### 1. Node.js 21.x LTS Implementation Patterns
```javascript
// Modern ES modules with node: protocol
import { readFile } from 'node:fs/promises';
import { performance } from 'node:perf_hooks';
import { test } from 'node:test';  // Built-in test runner

// Async/await error handling pattern
export async function processUserData(userId) {
  try {
    const userData = await userService.findById(userId);
    const processed = await dataProcessor.transform(userData);
    return { success: true, data: processed };
  } catch (error) {
    logger.error('User data processing failed:', { userId, error: error.message });
    throw new ApplicationError('Processing failed', 'USER_PROCESSING_ERROR');
  }
}
```

### 2. Framework-Specific Implementation

#### Express.js v5.x Implementation
```javascript
import express from 'express';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';

const app = express();

// Production security middleware
app.use(helmet({
  contentSecurityPolicy: false,  // Most production apps disable this
  crossOriginEmbedderPolicy: false
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);

// Error handling middleware
app.use((error, req, res, next) => {
  logger.error('Request error:', error);
  res.status(error.statusCode || 500).json({
    error: error.message || 'Internal server error'
  });
});
```

#### Fastify v4.x Implementation
```javascript
import Fastify from 'fastify';

const fastify = Fastify({
  logger: {
    level: process.env.LOG_LEVEL || 'info'
  }
});

// Register security plugin
await fastify.register(import('@fastify/helmet'), {
  contentSecurityPolicy: false
});

// Schema-based validation
const userSchema = {
  type: 'object',
  required: ['email', 'password'],
  properties: {
    email: { type: 'string', format: 'email' },
    password: { type: 'string', minLength: 8 }
  }
};

fastify.post('/api/users', {
  schema: { body: userSchema }
}, async (request, reply) => {
  const user = await userService.create(request.body);
  return { success: true, user };
});
```

### 3. Database Integration Implementation
```javascript
// Prisma integration with connection pooling
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL
    }
  }
});

// Repository pattern implementation
export class UserRepository {
  async create(userData) {
    return await prisma.user.create({
      data: {
        email: userData.email,
        hashedPassword: await hashPassword(userData.password),
        profile: {
          create: {
            firstName: userData.firstName,
            lastName: userData.lastName
          }
        }
      },
      include: { profile: true }
    });
  }

  async findByEmail(email) {
    return await prisma.user.findUnique({
      where: { email },
      include: { profile: true }
    });
  }
}
```

### 4. Authentication Implementation
```javascript
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

// JWT service implementation
export class AuthService {
  generateToken(userId) {
    return jwt.sign(
      { userId, iat: Date.now() },
      process.env.JWT_SECRET,
      {
        expiresIn: '1h',
        issuer: 'your-app',
        audience: 'your-users'
      }
    );
  }

  async verifyPassword(plaintext, hashed) {
    return await bcrypt.compare(plaintext, hashed);
  }

  async hashPassword(password) {
    return await bcrypt.hash(password, 12);
  }
}

// Authentication middleware
export const requireAuth = async (req, res, next) => {
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

### 5. Testing Implementation (Built-in Node.js Test Runner)
```javascript
import { test, describe } from 'node:test';
import assert from 'node:assert';
import { UserService } from '../services/UserService.js';

describe('UserService', () => {
  test('should create user with valid data', async () => {
    const userService = new UserService();
    const userData = {
      email: 'test@example.com',
      password: 'securepassword123',
      firstName: 'Test',
      lastName: 'User'
    };

    const user = await userService.create(userData);
    assert.strictEqual(user.email, userData.email);
    assert.ok(user.id);
  });

  test('should throw error for invalid email', async () => {
    const userService = new UserService();
    const userData = { email: 'invalid-email', password: 'password123' };

    await assert.rejects(
      () => userService.create(userData),
      { message: /invalid email format/i }
    );
  });
});
```

## Production Configuration

### Environment Configuration
```javascript
// config/database.js
export const databaseConfig = {
  development: {
    url: process.env.DEV_DATABASE_URL,
    pool: { min: 2, max: 10 }
  },
  production: {
    url: process.env.DATABASE_URL,
    pool: { min: 10, max: 100 },
    ssl: { rejectUnauthorized: false }
  }
};

// config/redis.js
export const redisConfig = {
  host: process.env.REDIS_HOST || 'localhost',
  port: process.env.REDIS_PORT || 6379,
  password: process.env.REDIS_PASSWORD,
  retryDelayOnFailover: 100,
  maxRetriesPerRequest: 3
};
```

## Deliverables

**NO DOCUMENTATION DELIVERABLES - CODING ONLY COMMAND**

This command produces CODE ONLY:
- Node.js/TypeScript source code files in appropriate directories
- Configuration files (package.json, tsconfig.json, etc.)
- Test files for validation
- Build artifacts from compilation/bundling

**REMINDER**: This is a pure implementation command. NO Jupyter Notebooks, NO Markdown files, NO reports of any kind will be created. Documentation creation is STRICTLY FORBIDDEN per the protocol above.

## Success Criteria
- All code compiles and runs without errors
- API endpoints respond with correct status codes and data
- Database operations complete successfully with proper error handling
- Security middleware functions correctly
- Tests pass with adequate coverage

## Command Integration
- **Prerequisite**: `nodejs-architecture-design`
- **Follow-up**: `nodejs-code-review` + `nodejs-code-quality-analysis`
- **Parallel**: None (implementation is sequential)

**Note**: This is an implementation command that generates production-ready executable code, not documentation.