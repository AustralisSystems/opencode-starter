# Node.js Code Quality Analysis Command

**YAML Prompt**: `nodejs-code-quality-analysis-prompt.yaml`

## Purpose
Deep code quality analysis with metrics, automated tooling recommendations, and maintainability assessment for Node.js backend applications.

## MCP Tool Requirements
- `context7` - Latest Node.js quality standards and tooling
- `grep` - Production-quality codebases and configurations
- `sequential-thinking` - Structured quality analysis approach
- `filesystem` - Code analysis and configuration reading
- `memory` - Track metrics during analysis session
- `time` - Timestamp quality assessment activities

## Quality Analysis Dimensions

### 1. Code Complexity and Maintainability
- **Cyclomatic Complexity**: Target <10 per function
- **Cognitive Complexity**: Target <15 per function
- **Technical Debt Ratio**: Target <5%
- **Code Duplication**: Target <3%

### 2. Node.js-Specific Quality Patterns
```javascript
// Modern ES modules pattern analysis
import { readFile } from 'node:fs/promises';
import { performance } from 'node:perf_hooks';

// Async/await pattern quality
async function handleRequest(req, res) {
  try {
    const data = await processData(req.body);
    res.json({ success: true, data });
  } catch (error) {
    // Error handling pattern assessment
    logger.error('Request processing failed:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}
```

### 3. Framework-Specific Quality Assessment
- **Express.js**: Middleware organization, error handling patterns
- **Fastify**: Schema validation completeness, plugin architecture
- **NestJS**: Decorator usage, dependency injection quality

### 4. Testing Quality Metrics
- **Line Coverage**: Target >80%
- **Branch Coverage**: Target >75%
- **Function Coverage**: Target >90%
- **Integration Test Coverage**: Target >60%

### 5. Security Quality Assessment
- Input validation coverage using joi/zod
- Authentication pattern consistency
- Environment variable and secret management
- Dependency vulnerability scanning results

## Automated Tool Integration

### ESLint Configuration Analysis
```json
{
  "extends": ["@typescript-eslint/recommended"],
  "plugins": ["security", "node", "import"],
  "rules": {
    "node/prefer-global/process": ["error", "always"],
    "import/no-unresolved": "error"
  }
}
```

### Quality Gate Definitions
- **Zero critical security vulnerabilities**
- **No major code smells**
- **All public APIs documented**
- **Duplication ratio <3%**

## Quality Scoring Framework
- **Level 5 (90-100%)**: Optimizing - Industry leading practices
- **Level 4 (80-89%)**: Quantitatively managed - Performance monitored
- **Level 3 (70-79%)**: Defined - Well-architected with best practices
- **Level 2 (60-69%)**: Managed - Organized with standard practices
- **Level 1 (<60%)**: Basic - Minimal optimization

## Deliverables
1. **Quality Metrics Dashboard** - Comprehensive scoring with visualizations
2. **Issue Analysis Report** - Prioritized findings with impact assessment
3. **Quality Improvement Guide** - Automated tooling setup and processes

## Tool Recommendations
- **Linting**: ESLint with TypeScript, security, and Node.js plugins
- **Formatting**: Prettier with 2-space indentation
- **Testing**: Jest with coverage reporting
- **Quality Analysis**: SonarQube integration for continuous monitoring

## Command Integration
- **Prerequisite**: `nodejs-backend-implementation`
- **Parallel**: `nodejs-code-review`
- **Follow-up**: `nodejs-gap-analysis`

**Note**: This is an analysis command that produces quality assessment reports and tooling recommendations.