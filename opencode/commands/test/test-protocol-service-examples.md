# === Universal Code Service Testing Examples: AI-Driven Service-Specific Testing Patterns and Implementation Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST:**

1. **READ AND INDEX**: `.claude/commands/ai-agent-compliance.md`
2. **READ AND INDEX**: `.claude/commands/core/code-protocol-compliance-prompt.md`
3. **VERIFY**: User has given explicit permission to proceed
4. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance.md requirements and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO MOCKING** of data or services in production code
- **NO TODOs** - complete ALL work immediately
- **NO SHORTCUTS** - implement properly ALWAYS
- **NO STUBS** - write complete implementations
- **NO FIXED DATA** - use real, dynamic data
- **NO HARDCODED VALUES** - use configuration
- **NO WORKAROUNDS** - fix root causes
- **NO FAKE IMPLEMENTATIONS** - real code only
- **NO PLACEHOLDER CODE** - production-ready only
- **NO TEMPORARY SOLUTIONS** - permanent fixes only

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MARKDOWN DOCUMENTS:**

   - Search for .ipynb files in the repository
   - Read implementation documents for context
   - Review analysis documents for insights
   - Study documentation documents for patterns

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest documentation
   - Find official framework/library docs
   - Search GitHub for example implementations
   - Review industry best practices
   - Study similar successful projects
   - Check Stack Overflow for common patterns

**SEARCH PRIORITIES:**

- Official documentation (latest version)
- GitHub repositories with high stars
- Industry standard implementations
- Recent blog posts/tutorials (< 1 year old)
- Community best practices

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards.

### **SERVICE-TESTING-EXAMPLES-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR SERVICE-SPECIFIC TESTING EXAMPLES DEVELOPMENT ONLY:**

- **MUST:** Implement comprehensive service-specific testing examples and patterns
- **MUST:** Create detailed testing implementations for each platform service
- **MUST:** Generate comprehensive testing patterns and best practices
- **MUST:** Provide complete service testing documentation with timestamps
- **FORBIDDEN:** Execute ANY actual service implementations or system changes
- **FORBIDDEN:** Modify ANY production services or configurations
- **FORBIDDEN:** Create ANY new service implementations
- **MUST:** Output service testing examples in markdown documents with timestamp tracking

**SERVICE TESTING EXAMPLES FOCUS AREAS:**

- Service-specific testing patterns and implementations
- Comprehensive testing examples for each platform service
- Integration testing patterns between services
- Performance testing examples for service validation
- Security testing patterns for service boundaries
- Error handling and recovery testing examples
- Monitoring and observability testing patterns

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-protocol-service-examples-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for service_scope, testing_depth, example_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the service testing examples protocol
4. **VERIFY COMPLETION**: Ensure all service testing example objectives and pattern criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive service testing examples documentation with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% service testing examples development and pattern completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-protocol-service-examples-prompt"
arguments:
  service_scope: "[all-services|core-services|n8n-focused|database-focused|ai-focused|infrastructure-focused]"
  testing_depth: "[basic|standard|advanced|enterprise|comprehensive]"
  example_complexity: "[simple|standard|detailed|enterprise|comprehensive]"
  pattern_focus: "[optional: functional|performance|security|integration|monitoring]"
  implementation_style: "[optional: unit-testing|integration-testing|e2e-testing|mixed-approach]"
  documentation_level: "[optional: basic|detailed|comprehensive|enterprise]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All service testing example phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive service testing examples development completed
- [ ] All platform service testing patterns created and documented (timestamped)
- [ ] Complete integration testing examples developed (timestamped)
- [ ] Performance testing patterns implemented (timestamped)
- [ ] Security testing examples created (timestamped)
- [ ] Error handling patterns developed (timestamped)
- [ ] Monitoring testing examples implemented (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL SERVICE TESTING EXAMPLES OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All service testing example deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All testing pattern documentation includes precise timestamps
- [ ] All service implementation examples include timestamp tracking
- [ ] All integration pattern documentation includes proper date stamps
- [ ] All performance testing examples follow consistent date stamp format
- [ ] All security pattern documentation includes timestamps
- [ ] All monitoring examples include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating service testing example files without proper reverse date stamps
- Using inconsistent date formats within same example development session
- Missing timestamps in service testing pattern documentation

### **SERVICE TESTING EXAMPLES DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After service testing examples development completion, implement with:
/test-implementation [service-scope] [testing-depth] [additional-options]

# Examples:
/test-implementation all-services comprehensive
/test-implementation core-services advanced
/test-implementation n8n-focused detailed
```

---

**ENFORCEMENT:** This command performs SERVICE TESTING EXAMPLES DEVELOPMENT ONLY through the MCP prompt protocol. The comprehensive examples logic is defined in `test-protocol-service-examples-prompt.yaml` and executed according to Model Context Protocol standards. No actual service testing or system changes are performed. Use `/test-implementation` for actual testing implementation after examples are developed.

model_context:
role: "AI-driven service testing examples specialist for comprehensive platform service testing pattern development"
domain: "Service Testing Patterns, Platform Service Validation, Integration Testing, Performance Testing"
goal: >
Develop comprehensive service-specific testing examples and patterns that provide detailed
testing implementations for each platform service, enable effective service validation,
and establish best practices for service testing. Create robust testing patterns and
examples using Jupyter Notebook format with implementations, patterns, methodologies,
and service validation examples including Mermaid diagrams.

configuration:

## Overview

This protocol file contains comprehensive service-specific testing examples and patterns for the n8n IaC Agentic Automation Platform. This file provides detailed testing examples for each platform service including n8n, PostgreSQL, Neo4j, Qdrant, LightRAG, and supporting services. This file is referenced by the `test-protocol-service-examples-prompt.yaml` MCP prompt.

## Platform Service Testing Examples

### 1. n8n Workflow Engine Testing

#### n8n Health Check Testing

```javascript
// n8n Health Check Test Examples
describe("n8n Service Health Checks", () => {
  test("Basic health endpoint", async () => {
    const response = await fetch("http://localhost:5678/healthz");

    expect(response.status).toBe(200);

    const healthData = await response.json();
    expect(healthData).toHaveProperty("status", "ok");
    expect(healthData).toHaveProperty("database");
    expect(healthData.database).toHaveProperty("status", "ok");
  });

  test("Database connectivity check", async () => {
    const response = await fetch("http://localhost:5678/api/v1/workflows", {
      headers: {
        Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
      },
    });

    expect(response.status).toBe(200);

    const workflows = await response.json();
    expect(workflows).toHaveProperty("data");
    expect(Array.isArray(workflows.data)).toBe(true);
  });

  test("Service dependency verification", async () => {
    const endpoints = [
      "/api/v1/credentials",
      "/api/v1/executions",
      "/api/v1/nodes",
      "/api/v1/users",
    ];

    for (const endpoint of endpoints) {
      const response = await fetch(`http://localhost:5678${endpoint}`, {
        headers: {
          Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
        },
      });

      expect(response.status).toBeLessThan(500);
    }
  });
});
```

#### n8n Workflow Testing

```javascript
// n8n Workflow Testing Examples
describe("n8n Workflow Operations", () => {
  test("Create workflow", async () => {
    const workflowData = {
      name: "Test Workflow",
      active: false,
      nodes: [
        {
          id: "webhook-node",
          type: "n8n-nodes-base.webhook",
          position: [100, 100],
          parameters: {
            path: "test-webhook",
            httpMethod: "POST",
          },
        },
        {
          id: "response-node",
          type: "n8n-nodes-base.respondToWebhook",
          position: [300, 100],
          parameters: {
            responseBody: '{"status": "received"}',
          },
        },
      ],
      connections: {
        "webhook-node": {
          main: [[{ node: "response-node", type: "main", index: 0 }]],
        },
      },
    };

    const response = await fetch("http://localhost:5678/api/v1/workflows", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
      },
      body: JSON.stringify(workflowData),
    });

    expect(response.status).toBe(201);

    const workflow = await response.json();
    expect(workflow).toHaveProperty("id");
    expect(workflow.name).toBe("Test Workflow");
    expect(workflow.nodes).toHaveLength(2);
  });

  test("Execute workflow", async () => {
    // First create a workflow
    const workflowId = await createTestWorkflow();

    // Activate the workflow
    await fetch(
      `http://localhost:5678/api/v1/workflows/${workflowId}/activate`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
        },
      }
    );

    // Trigger the workflow via webhook
    const triggerResponse = await fetch(
      "http://localhost:5678/webhook/test-webhook",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ test: "data" }),
      }
    );

    expect(triggerResponse.status).toBe(200);

    const result = await triggerResponse.json();
    expect(result).toHaveProperty("status", "received");

    // Verify execution was recorded
    await new Promise((resolve) => setTimeout(resolve, 1000)); // Wait for execution

    const executionsResponse = await fetch(
      `http://localhost:5678/api/v1/executions`,
      {
        headers: {
          Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
        },
      }
    );

    const executions = await executionsResponse.json();
    const recentExecution = executions.data.find(
      (e) => e.workflowId === workflowId
    );

    expect(recentExecution).toBeDefined();
    expect(recentExecution.finished).toBe(true);
    expect(recentExecution.mode).toBe("webhook");
  });

  test("Workflow performance under load", async () => {
    const workflowId = await createPerformanceTestWorkflow();

    // Activate workflow
    await activateWorkflow(workflowId);

    const startTime = Date.now();
    const concurrentRequests = 10;

    const promises = Array.from({ length: concurrentRequests }, (_, i) =>
      fetch("http://localhost:5678/webhook/performance-test", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ request_id: i }),
      })
    );

    const responses = await Promise.all(promises);
    const endTime = Date.now();

    // Verify all requests succeeded
    for (const response of responses) {
      expect(response.status).toBe(200);
    }

    // Verify performance
    const totalTime = endTime - startTime;
    const avgResponseTime = totalTime / concurrentRequests;

    expect(avgResponseTime).toBeLessThan(1000); // < 1s average

    // Verify executions
    await new Promise((resolve) => setTimeout(resolve, 2000));

    const executions = await getWorkflowExecutions(workflowId);
    expect(executions.filter((e) => e.finished).length).toBe(
      concurrentRequests
    );
  });
});
```

### 2. PostgreSQL Database Testing

#### PostgreSQL Connection Testing

```sql
-- PostgreSQL Connection and Performance Tests

-- Basic connection test
SELECT 1 as connection_test;

-- Database size and health check
SELECT
    pg_database_size(current_database()) as db_size_bytes,
    pg_size_pretty(pg_database_size(current_database())) as db_size_pretty,
    current_database() as database_name,
    version() as postgres_version;

-- Table health check
SELECT
    schemaname,
    tablename,
    n_tup_ins as inserts,
    n_tup_upd as updates,
    n_tup_del as deletes,
    n_live_tup as live_tuples,
    n_dead_tup as dead_tuples,
    last_vacuum,
    last_autovacuum,
    last_analyze,
    last_autoanalyze
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC;

-- Connection pool status
SELECT
    application_name,
    state,
    COUNT(*) as connection_count
FROM pg_stat_activity
WHERE state IS NOT NULL
GROUP BY application_name, state;

-- Performance metrics
SELECT
    'Query Performance' as metric_type,
    schemaname,
    tablename,
    seq_scan,
    seq_tup_read,
    idx_scan,
    idx_tup_fetch,
    n_tup_ins + n_tup_upd + n_tup_del as total_modifications
FROM pg_stat_user_tables
WHERE seq_scan > 1000 OR idx_scan > 1000;
```

#### PostgreSQL Data Integrity Testing

```javascript
// PostgreSQL Data Integrity Test Examples
describe("PostgreSQL Data Integrity", () => {
  test("User table integrity", async () => {
    const client = new Pool({
      host: "localhost",
      port: 5432,
      database: "n8n",
      user: "n8n",
      password: process.env.N8N_DB_PASSWORD,
    });

    // Test user creation
    const userResult = await client.query(
      `
      INSERT INTO users (email, password, first_name, last_name)
      VALUES ($1, $2, $3, $4)
      RETURNING id, email
    `,
      ["test@example.com", "hashed_password", "Test", "User"]
    );

    expect(userResult.rows).toHaveLength(1);
    expect(userResult.rows[0].email).toBe("test@example.com");

    const userId = userResult.rows[0].id;

    // Test user retrieval
    const retrieveResult = await client.query(
      "SELECT * FROM users WHERE id = $1",
      [userId]
    );

    expect(retrieveResult.rows).toHaveLength(1);
    expect(retrieveResult.rows[0].email).toBe("test@example.com");

    // Cleanup
    await client.query("DELETE FROM users WHERE id = $1", [userId]);

    await client.end();
  });

  test("Workflow data consistency", async () => {
    const client = new Pool({
      /* connection config */
    });

    // Create workflow
    const workflowResult = await client.query(
      `
      INSERT INTO workflow_entity (name, active, nodes, connections)
      VALUES ($1, $2, $3, $4)
      RETURNING id
    `,
      [
        "Test Consistency Workflow",
        false,
        JSON.stringify([{ id: "node1", type: "test" }]),
        JSON.stringify({}),
      ]
    );

    const workflowId = workflowResult.rows[0].id;

    // Create execution
    const executionResult = await client.query(
      `
      INSERT INTO execution_entity (workflow_id, mode, started_at, status_text)
      VALUES ($1, $2, $3, $4)
      RETURNING id
    `,
      [workflowId, "manual", new Date(), "success"]
    );

    const executionId = executionResult.rows[0].id;

    // Verify foreign key relationship
    const joinResult = await client.query(
      `
      SELECT w.name, e.mode, e.status_text
      FROM workflow_entity w
      INNER JOIN execution_entity e ON w.id = e.workflow_id
      WHERE w.id = $1 AND e.id = $2
    `,
      [workflowId, executionId]
    );

    expect(joinResult.rows).toHaveLength(1);
    expect(joinResult.rows[0].name).toBe("Test Consistency Workflow");

    // Test cascade delete
    await client.query("DELETE FROM workflow_entity WHERE id = $1", [
      workflowId,
    ]);

    const orphanCheck = await client.query(
      "SELECT COUNT(*) FROM execution_entity WHERE workflow_id = $1",
      [workflowId]
    );

    expect(parseInt(orphanCheck.rows[0].count)).toBe(0);

    await client.end();
  });

  test("Database performance under load", async () => {
    const client = new Pool({
      /* connection config */
    });

    const startTime = Date.now();
    const testRecords = 1000;

    // Batch insert test
    const values = [];
    const placeholders = [];

    for (let i = 0; i < testRecords; i++) {
      values.push(`test_user_${i}@example.com`, "password", "User", `${i}`);
      placeholders.push(
        `($${i * 4 + 1}, $${i * 4 + 2}, $${i * 4 + 3}, $${i * 4 + 4})`
      );
    }

    const insertQuery = `
      INSERT INTO users (email, password, first_name, last_name)
      VALUES ${placeholders.join(", ")}
    `;

    await client.query(insertQuery, values);

    const insertTime = Date.now() - startTime;

    // Query performance test
    const queryStart = Date.now();

    const result = await client.query(`
      SELECT COUNT(*) FROM users
      WHERE email LIKE 'test_user_%@example.com'
    `);

    const queryTime = Date.now() - queryStart;

    expect(parseInt(result.rows[0].count)).toBe(testRecords);
    expect(insertTime).toBeLessThan(5000); // < 5s for 1000 records
    expect(queryTime).toBeLessThan(1000); // < 1s for count query

    // Cleanup
    await client.query(
      "DELETE FROM users WHERE email LIKE 'test_user_%@example.com'"
    );

    await client.end();
  });
});
```

### 3. Neo4j Graph Database Testing

#### Neo4j Connection and Query Testing

```cypher
// Neo4j Health and Performance Queries

// Basic connectivity test
RETURN "Neo4j Connected" as status, datetime() as timestamp;

// Database statistics
CALL apoc.monitor.kernel() YIELD name, value
WHERE name IN ['DatabaseName', 'StoreSize', 'NodeCount', 'RelationshipCount']
RETURN name, value;

// Memory usage check
CALL apoc.monitor.memory() YIELD name, value
RETURN name, value;

// Index performance check
CALL db.indexes() YIELD name, type, state, populationPercent
RETURN name, type, state, populationPercent;

// Query performance analysis
CALL apoc.monitor.query()
YIELD query, elapsedTimeMillis, cpuTimeMillis
WHERE elapsedTimeMillis > 1000
RETURN query, elapsedTimeMillis, cpuTimeMillis
ORDER BY elapsedTimeMillis DESC
LIMIT 10;
```

#### Neo4j Graph Operations Testing

```javascript
// Neo4j Graph Operations Test Examples
const neo4j = require("neo4j-driver");

describe("Neo4j Graph Operations", () => {
  let driver;
  let session;

  beforeAll(async () => {
    driver = neo4j.driver(
      "bolt://localhost:7687",
      neo4j.auth.basic("neo4j", process.env.NEO4J_PASSWORD)
    );
    session = driver.session();
  });

  afterAll(async () => {
    await session.close();
    await driver.close();
  });

  test("Create and query nodes", async () => {
    // Create test nodes
    const createResult = await session.run(
      `
      CREATE (u:User {id: $userId, name: $name, email: $email})
      CREATE (w:Workflow {id: $workflowId, name: $workflowName})
      CREATE (u)-[:OWNS]->(w)
      RETURN u, w
    `,
      {
        userId: "test-user-1",
        name: "Test User",
        email: "test@example.com",
        workflowId: "test-workflow-1",
        workflowName: "Test Workflow",
      }
    );

    expect(createResult.records).toHaveLength(1);

    const userNode = createResult.records[0].get("u");
    const workflowNode = createResult.records[0].get("w");

    expect(userNode.properties.name).toBe("Test User");
    expect(workflowNode.properties.name).toBe("Test Workflow");

    // Query relationships
    const queryResult = await session.run(
      `
      MATCH (u:User)-[r:OWNS]->(w:Workflow)
      WHERE u.id = $userId
      RETURN u.name as userName, w.name as workflowName, type(r) as relationshipType
    `,
      { userId: "test-user-1" }
    );

    expect(queryResult.records).toHaveLength(1);
    expect(queryResult.records[0].get("userName")).toBe("Test User");
    expect(queryResult.records[0].get("workflowName")).toBe("Test Workflow");
    expect(queryResult.records[0].get("relationshipType")).toBe("OWNS");

    // Cleanup
    await session.run(
      `
      MATCH (u:User {id: $userId})-[r]-(w:Workflow)
      DELETE r, u, w
    `,
      { userId: "test-user-1" }
    );
  });

  test("Complex graph traversal", async () => {
    // Create complex graph structure
    await session.run(`
      CREATE (u1:User {id: 'user1', name: 'User 1'})
      CREATE (u2:User {id: 'user2', name: 'User 2'})
      CREATE (w1:Workflow {id: 'workflow1', name: 'Workflow 1'})
      CREATE (w2:Workflow {id: 'workflow2', name: 'Workflow 2'})
      CREATE (n1:Node {id: 'node1', type: 'webhook'})
      CREATE (n2:Node {id: 'node2', type: 'http'})
      CREATE (n3:Node {id: 'node3', type: 'database'})

      CREATE (u1)-[:OWNS]->(w1)
      CREATE (u2)-[:OWNS]->(w2)
      CREATE (w1)-[:CONTAINS]->(n1)
      CREATE (w1)-[:CONTAINS]->(n2)
      CREATE (w2)-[:CONTAINS]->(n2)
      CREATE (w2)-[:CONTAINS]->(n3)
      CREATE (n1)-[:CONNECTS_TO]->(n2)
      CREATE (n2)-[:CONNECTS_TO]->(n3)
    `);

    // Test complex traversal
    const traversalResult = await session.run(`
      MATCH path = (u:User)-[:OWNS]->(w:Workflow)-[:CONTAINS]->(n:Node)-[:CONNECTS_TO*1..3]->(target:Node)
      WHERE u.id = 'user1'
      RETURN u.name as user, w.name as workflow,
             collect(DISTINCT n.type) as nodeTypes,
             length(path) as pathLength
    `);

    expect(traversalResult.records.length).toBeGreaterThan(0);

    const record = traversalResult.records[0];
    expect(record.get("user")).toBe("User 1");
    expect(record.get("nodeTypes")).toContain("webhook");

    // Test aggregation queries
    const aggregationResult = await session.run(`
      MATCH (u:User)-[:OWNS]->(w:Workflow)-[:CONTAINS]->(n:Node)
      RETURN u.name as user,
             count(w) as workflowCount,
             count(n) as nodeCount,
             collect(DISTINCT n.type) as nodeTypes
      ORDER BY nodeCount DESC
    `);

    expect(aggregationResult.records.length).toBeGreaterThan(0);

    // Cleanup
    await session.run(`
      MATCH (n)
      WHERE n.id IN ['user1', 'user2', 'workflow1', 'workflow2', 'node1', 'node2', 'node3']
      DETACH DELETE n
    `);
  });

  test("Graph performance under load", async () => {
    const startTime = Date.now();

    // Create large graph structure
    const nodeCount = 1000;
    const relationshipCount = 2000;

    // Batch create nodes
    const nodeCreationPromises = [];
    for (let i = 0; i < nodeCount; i += 100) {
      const batch = [];
      for (let j = 0; j < 100 && i + j < nodeCount; j++) {
        batch.push(`CREATE (:TestNode {id: ${i + j}, value: 'test_${i + j}'})`);
      }

      nodeCreationPromises.push(session.run(batch.join("\n")));
    }

    await Promise.all(nodeCreationPromises);

    const nodeCreationTime = Date.now() - startTime;

    // Test query performance
    const queryStart = Date.now();

    const queryResult = await session.run(`
      MATCH (n:TestNode)
      WHERE n.id > 500
      RETURN count(n) as nodeCount
    `);

    const queryTime = Date.now() - queryStart;

    expect(parseInt(queryResult.records[0].get("nodeCount"))).toBeLessThan(
      nodeCount
    );
    expect(nodeCreationTime).toBeLessThan(30000); // < 30s for 1000 nodes
    expect(queryTime).toBeLessThan(5000); // < 5s for query

    // Cleanup
    await session.run("MATCH (n:TestNode) DELETE n");
  });
});
```

### 4. Qdrant Vector Database Testing

#### Qdrant API Testing

```javascript
// Qdrant Vector Database Test Examples
describe("Qdrant Vector Operations", () => {
  const qdrantUrl = "http://localhost:6333";

  test("Qdrant health check", async () => {
    const response = await fetch(`${qdrantUrl}/`);

    expect(response.status).toBe(200);

    const health = await response.json();
    expect(health).toHaveProperty("title", "qdrant - vector search engine");
  });

  test("Collection operations", async () => {
    const collectionName = "test_collection";

    // Create collection
    const createResponse = await fetch(
      `${qdrantUrl}/collections/${collectionName}`,
      {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          vectors: {
            size: 384,
            distance: "Cosine",
          },
        }),
      }
    );

    expect(createResponse.status).toBe(200);

    // Verify collection exists
    const listResponse = await fetch(`${qdrantUrl}/collections`);
    const collections = await listResponse.json();

    expect(
      collections.result.collections.some((c) => c.name === collectionName)
    ).toBe(true);

    // Insert vectors
    const vectors = Array.from({ length: 10 }, (_, i) => ({
      id: i,
      vector: Array.from({ length: 384 }, () => Math.random()),
      payload: { text: `Document ${i}`, category: i % 3 },
    }));

    const insertResponse = await fetch(
      `${qdrantUrl}/collections/${collectionName}/points`,
      {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          points: vectors,
        }),
      }
    );

    expect(insertResponse.status).toBe(200);

    // Search vectors
    const searchResponse = await fetch(
      `${qdrantUrl}/collections/${collectionName}/points/search`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          vector: vectors[0].vector,
          limit: 5,
          with_payload: true,
        }),
      }
    );

    expect(searchResponse.status).toBe(200);

    const searchResults = await searchResponse.json();
    expect(searchResults.result).toHaveLength(5);
    expect(searchResults.result[0].id).toBe(0);
    expect(searchResults.result[0].score).toBeCloseTo(1.0, 2);

    // Cleanup
    await fetch(`${qdrantUrl}/collections/${collectionName}`, {
      method: "DELETE",
    });
  });

  test("Vector search performance", async () => {
    const collectionName = "performance_test_collection";

    // Create collection
    await fetch(`${qdrantUrl}/collections/${collectionName}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        vectors: { size: 384, distance: "Cosine" },
        optimizers_config: {
          default_segment_number: 2,
        },
      }),
    });

    // Insert large number of vectors
    const batchSize = 100;
    const totalVectors = 1000;

    const insertStart = Date.now();

    for (let i = 0; i < totalVectors; i += batchSize) {
      const batch = Array.from(
        { length: Math.min(batchSize, totalVectors - i) },
        (_, j) => ({
          id: i + j,
          vector: Array.from({ length: 384 }, () => Math.random()),
          payload: {
            text: `Document ${i + j}`,
            batch: Math.floor((i + j) / batchSize),
          },
        })
      );

      await fetch(`${qdrantUrl}/collections/${collectionName}/points`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ points: batch }),
      });
    }

    const insertTime = Date.now() - insertStart;

    // Wait for indexing
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Performance search test
    const searchStart = Date.now();
    const searchPromises = [];

    for (let i = 0; i < 50; i++) {
      searchPromises.push(
        fetch(`${qdrantUrl}/collections/${collectionName}/points/search`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            vector: Array.from({ length: 384 }, () => Math.random()),
            limit: 10,
          }),
        })
      );
    }

    const searchResults = await Promise.all(searchPromises);
    const searchTime = Date.now() - searchStart;

    // Verify all searches succeeded
    for (const response of searchResults) {
      expect(response.status).toBe(200);
    }

    expect(insertTime).toBeLessThan(60000); // < 60s for 1000 vectors
    expect(searchTime).toBeLessThan(5000); // < 5s for 50 searches

    // Cleanup
    await fetch(`${qdrantUrl}/collections/${collectionName}`, {
      method: "DELETE",
    });
  });
});
```

### 5. LightRAG Service Testing

#### LightRAG API Testing

```javascript
// LightRAG Service Test Examples
describe("LightRAG Service Operations", () => {
  const lightragUrl = "http://localhost:8000";

  test("LightRAG health check", async () => {
    const response = await fetch(`${lightragUrl}/health`);

    expect(response.status).toBe(200);

    const health = await response.json();
    expect(health).toHaveProperty("status", "healthy");
    expect(health).toHaveProperty("services");
    expect(health.services).toHaveProperty("qdrant");
    expect(health.services).toHaveProperty("embedding_model");
  });

  test("Document ingestion and retrieval", async () => {
    const testDocument = {
      id: "test-doc-1",
      content:
        "This is a test document for RAG processing. It contains information about testing procedures and best practices.",
      metadata: {
        title: "Test Document",
        category: "testing",
        tags: ["test", "documentation"],
      },
    };

    // Ingest document
    const ingestResponse = await fetch(`${lightragUrl}/api/v1/documents`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(testDocument),
    });

    expect(ingestResponse.status).toBe(201);

    const ingestResult = await ingestResponse.json();
    expect(ingestResult).toHaveProperty("document_id");
    expect(ingestResult).toHaveProperty("chunks_created");

    // Wait for processing
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Search for document
    const searchResponse = await fetch(`${lightragUrl}/api/v1/search`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: "testing procedures",
        limit: 5,
      }),
    });

    expect(searchResponse.status).toBe(200);

    const searchResults = await searchResponse.json();
    expect(searchResults).toHaveProperty("results");
    expect(searchResults.results.length).toBeGreaterThan(0);
    expect(searchResults.results[0]).toHaveProperty(
      "document_id",
      "test-doc-1"
    );
    expect(searchResults.results[0]).toHaveProperty("score");
    expect(searchResults.results[0]).toHaveProperty("content");

    // Test RAG query
    const ragResponse = await fetch(`${lightragUrl}/api/v1/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: "What are the best practices for testing?",
        max_results: 3,
      }),
    });

    expect(ragResponse.status).toBe(200);

    const ragResult = await ragResponse.json();
    expect(ragResult).toHaveProperty("answer");
    expect(ragResult).toHaveProperty("sources");
    expect(ragResult.sources.length).toBeGreaterThan(0);

    // Cleanup
    await fetch(`${lightragUrl}/api/v1/documents/test-doc-1`, {
      method: "DELETE",
    });
  });

  test("Batch document processing", async () => {
    const documents = Array.from({ length: 10 }, (_, i) => ({
      id: `batch-doc-${i}`,
      content: `This is batch document ${i}. It contains unique content about topic ${
        i % 3
      }.`,
      metadata: {
        title: `Batch Document ${i}`,
        topic: `topic_${i % 3}`,
        batch_id: "test-batch-1",
      },
    }));

    const batchStart = Date.now();

    // Batch ingest
    const batchResponse = await fetch(`${lightragUrl}/api/v1/documents/batch`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ documents }),
    });

    expect(batchResponse.status).toBe(202);

    const batchResult = await batchResponse.json();
    expect(batchResult).toHaveProperty("job_id");

    // Wait for processing
    let processed = false;
    let attempts = 0;

    while (!processed && attempts < 30) {
      await new Promise((resolve) => setTimeout(resolve, 1000));

      const statusResponse = await fetch(
        `${lightragUrl}/api/v1/jobs/${batchResult.job_id}`
      );
      const status = await statusResponse.json();

      if (status.status === "completed") {
        processed = true;
        expect(status.processed_documents).toBe(10);
      }

      attempts++;
    }

    expect(processed).toBe(true);

    const batchTime = Date.now() - batchStart;
    expect(batchTime).toBeLessThan(60000); // < 60s for 10 documents

    // Test search across batch
    const searchResponse = await fetch(`${lightragUrl}/api/v1/search`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: "topic",
        filters: { "metadata.batch_id": "test-batch-1" },
        limit: 10,
      }),
    });

    const searchResults = await searchResponse.json();
    expect(searchResults.results.length).toBe(10);

    // Cleanup
    for (let i = 0; i < 10; i++) {
      await fetch(`${lightragUrl}/api/v1/documents/batch-doc-${i}`, {
        method: "DELETE",
      });
    }
  });
});
```

### 6. Integration Testing Examples

#### End-to-End Workflow Integration

```javascript
// End-to-End Integration Test Examples
describe("Platform Integration Tests", () => {
  test("Complete workflow with RAG integration", async () => {
    // 1. Create knowledge base in LightRAG
    const document = {
      id: "integration-doc",
      content:
        "Integration testing involves testing the interaction between different components.",
      metadata: { type: "knowledge" },
    };

    await fetch("http://localhost:8000/api/v1/documents", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(document),
    });

    // 2. Create workflow in n8n that uses RAG
    const workflow = {
      name: "RAG Integration Workflow",
      nodes: [
        {
          id: "webhook",
          type: "n8n-nodes-base.webhook",
          parameters: { path: "rag-test" },
        },
        {
          id: "rag-query",
          type: "n8n-nodes-base.httpRequest",
          parameters: {
            url: "http://localhost:8000/api/v1/query",
            method: "POST",
            body: {
              question: "={{$json.question}}",
            },
          },
        },
        {
          id: "store-result",
          type: "n8n-nodes-base.postgres",
          parameters: {
            operation: "insert",
            table: "rag_results",
            columns: "question,answer,timestamp",
          },
        },
      ],
    };

    const workflowResponse = await fetch(
      "http://localhost:5678/api/v1/workflows",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.N8N_API_TOKEN}`,
        },
        body: JSON.stringify(workflow),
      }
    );

    const createdWorkflow = await workflowResponse.json();

    // 3. Activate workflow
    await fetch(
      `http://localhost:5678/api/v1/workflows/${createdWorkflow.id}/activate`,
      {
        method: "POST",
        headers: { Authorization: `Bearer ${process.env.N8N_API_TOKEN}` },
      }
    );

    // 4. Trigger workflow
    const triggerResponse = await fetch(
      "http://localhost:5678/webhook/rag-test",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: "What is integration testing?",
        }),
      }
    );

    expect(triggerResponse.status).toBe(200);

    // 5. Wait and verify execution
    await new Promise((resolve) => setTimeout(resolve, 3000));

    const executions = await fetch(
      `http://localhost:5678/api/v1/executions?workflowId=${createdWorkflow.id}`,
      {
        headers: { Authorization: `Bearer ${process.env.N8N_API_TOKEN}` },
      }
    );

    const executionData = await executions.json();
    expect(executionData.data.length).toBeGreaterThan(0);
    expect(executionData.data[0].finished).toBe(true);

    // 6. Verify data in PostgreSQL
    const pgClient = new Pool({
      /* connection config */
    });
    const result = await pgClient.query(
      "SELECT * FROM rag_results WHERE question = $1",
      ["What is integration testing?"]
    );

    expect(result.rows.length).toBeGreaterThan(0);
    expect(result.rows[0].answer).toContain("integration");

    await pgClient.end();
  });

  test("Cross-service performance integration", async () => {
    const startTime = Date.now();

    // Simulate complex workflow execution
    const promises = [];

    // Concurrent n8n workflow executions
    for (let i = 0; i < 5; i++) {
      promises.push(
        fetch("http://localhost:5678/webhook/performance-test", {
          method: "POST",
          body: JSON.stringify({ test_id: i }),
        })
      );
    }

    // Concurrent RAG queries
    for (let i = 0; i < 5; i++) {
      promises.push(
        fetch("http://localhost:8000/api/v1/query", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question: `Performance test query ${i}`,
          }),
        })
      );
    }

    // Concurrent database operations
    const pgClient = new Pool({
      /* connection config */
    });
    for (let i = 0; i < 5; i++) {
      promises.push(pgClient.query("SELECT COUNT(*) FROM users"));
    }

    const results = await Promise.all(promises);
    const totalTime = Date.now() - startTime;

    // Verify all operations succeeded
    expect(results.length).toBe(15);

    // Verify performance
    expect(totalTime).toBeLessThan(10000); // < 10s for all operations

    await pgClient.end();
  });
});
```

This comprehensive service testing protocol provides detailed examples and patterns for testing each component of the n8n IaC Agentic Automation Platform, ensuring thorough validation of all services and their integrations.
