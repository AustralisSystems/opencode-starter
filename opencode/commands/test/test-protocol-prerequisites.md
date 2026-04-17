# === Universal Code Test Prerequisites: AI-Driven Test Environment Setup and Validation Protocol ===

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
3. **READ AND INDEX**: `.claude/commands/test/test-protocol-service-examples.md`
4. **VERIFY**: User has given explicit permission to proceed
5. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

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

### **TEST-PREREQUISITES-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR TEST PREREQUISITE SETUP AND VALIDATION ONLY:**

- **MUST:** Implement comprehensive test environment prerequisite validation
- **MUST:** Create detailed service health check and validation systems
- **MUST:** Generate automated environment setup and configuration procedures
- **MUST:** Provide comprehensive prerequisite validation reports with timestamp documentation
- **FORBIDDEN:** Execute ANY actual test implementations or live system changes
- **FORBIDDEN:** Modify ANY production systems or live configurations
- **FORBIDDEN:** Create ANY new test cases or test executions
- **MUST:** Output prerequisite validation results in markdown documents with timestamp tracking

**TEST PREREQUISITE FOCUS AREAS:**

- Service health check automation and validation
- Environment configuration verification and setup
- Data preparation and validation procedures
- Security validation and compliance checking
- Performance baseline establishment
- Monitoring setup and configuration validation
- Backup and recovery procedure verification

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `test-protocol-prerequisites-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for prerequisite_scope, validation_level, setup_complexity
3. **FOLLOW PROTOCOL**: Execute all phases according to the prerequisite validation protocol specifications
4. **VERIFY COMPLETION**: Ensure all prerequisite objectives and validation criteria have been met
5. **DOCUMENT RESULTS**: Create comprehensive prerequisite validation reports with timestamps
6. **VALIDATE COMPLIANCE**: Confirm 100% prerequisite setup and validation completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "test-protocol-prerequisites-prompt"
arguments:
  prerequisite_scope: "[comprehensive|service-specific|environment-setup|security-focused|performance-baseline|minimal]"
  validation_level: "[basic|standard|advanced|enterprise|production-ready]"
  setup_complexity: "[simple|standard|comprehensive|enterprise|full-automation]"
  environment_type: "[optional: local|development|staging|production|multi-environment]"
  service_focus: "[optional: all-services|core-services|specific-services|custom]"
  automation_level: "[optional: manual|semi-automated|fully-automated|enterprise]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All prerequisite validation phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive environment validation completed across all targeted areas
- [ ] All service health checks configured and validated (timestamped)
- [ ] Complete environment setup automation implemented (timestamped)
- [ ] Data preparation and validation procedures functional (timestamped)
- [ ] Security validation and compliance checking operational (timestamped)
- [ ] Performance baseline establishment completed (timestamped)
- [ ] Monitoring setup and configuration validated (timestamped)
- [ ] Backup and recovery procedures verified (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL TEST PREREQUISITE OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All prerequisite validation deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All service health check configurations include precise timestamps
- [ ] All environment setup documentation includes timestamp tracking
- [ ] All validation procedure reports include proper date stamps
- [ ] All security validation follows consistent date stamp format
- [ ] All performance baseline documentation includes timestamps
- [ ] All monitoring setup includes proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating prerequisite validation files without proper reverse date stamps
- Using inconsistent date formats within same validation session
- Missing timestamps in prerequisite documentation

### **TEST PREREQUISITE DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/testing/test-tests/Test_Execution_Report_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
2. **`./project/docs/testing/test-tests/Test_Results_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/testing/test-tests/Coverage_Analysis_{YYYYMMDD-HHMMSS}.ipynb`** - Comprehensive coverage analysis and findings

**NEXT PHASE PREPARATION:**

```bash
# After prerequisite setup completion, proceed with:
/test-execution [prerequisite-scope] [validation-level] [additional-options]

# Examples:
/test-execution comprehensive production-ready
/test-execution service-specific advanced
/test-execution environment-setup standard
```

---

**ENFORCEMENT:** This command performs TEST PREREQUISITE SETUP AND VALIDATION ONLY through the MCP prompt protocol. The comprehensive prerequisite logic is defined in `test-protocol-prerequisites-prompt.yaml` and executed according to Model Context Protocol standards. No actual test execution or live system changes are performed. Use `/test-execution` for actual testing after prerequisites are validated.

model_context:
role: "AI-driven test prerequisite specialist for comprehensive environment setup and validation"
domain: "Test Environment Setup, Service Health Validation, Configuration Management, Security Compliance"
goal: >
Implement comprehensive test prerequisite validation systems that ensure all test environment
requirements are met, all services are healthy and properly configured, all data is prepared
and validated, and all security and performance baselines are established. Create robust
automation and validation systems using Jupyter Notebook format with evidence, metrics,
configuration documentation, and validation procedures including Mermaid diagrams.

configuration:

## Overview

This protocol file contains detailed procedures, examples, and validation methods for test prerequisite setup and validation. This file is referenced by the `test-protocol-prerequisites-prompt.yaml` MCP prompt and provides the non-instructional content including templates, examples, and detailed procedures.

## Prerequisite Validation Procedures

### 1. Service Health Check Procedures

#### Standard Health Check Template

```bash
#!/bin/bash
# Service Health Check Template

SERVICE_NAME="$1"
SERVICE_URL="$2"
EXPECTED_STATUS="$3"

echo "Checking health of $SERVICE_NAME at $SERVICE_URL"

# Basic connectivity check
if curl -s -o /dev/null -w "%{http_code}" "$SERVICE_URL/health" | grep -q "$EXPECTED_STATUS"; then
    echo "✓ $SERVICE_NAME health check passed"
    return 0
else
    echo "✗ $SERVICE_NAME health check failed"
    return 1
fi
```

#### n8n Service Health Check

```bash
# n8n Health Check Procedure
SERVICE_URL="http://localhost:5678"
HEALTH_ENDPOINT="/healthz"

# Check n8n service
curl -s "$SERVICE_URL$HEALTH_ENDPOINT" | jq '.status' | grep -q "ok"
if [ $? -eq 0 ]; then
    echo "✓ n8n service is healthy"
else
    echo "✗ n8n service health check failed"
fi

# Check n8n database connection
curl -s "$SERVICE_URL/api/v1/credentials" -H "Accept: application/json"
if [ $? -eq 0 ]; then
    echo "✓ n8n database connection verified"
else
    echo "✗ n8n database connection failed"
fi
```

#### PostgreSQL Health Check

```bash
# PostgreSQL Health Check Procedure
PG_HOST="localhost"
PG_PORT="5432"
PG_DATABASE="n8n"
PG_USER="n8n"

# Test connection
PGPASSWORD="$N8N_DB_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DATABASE" -c "SELECT 1;" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ PostgreSQL connection successful"
else
    echo "✗ PostgreSQL connection failed"
    exit 1
fi

# Check database size and tables
PGPASSWORD="$N8N_DB_PASSWORD" psql -h "$PG_HOST" -p "$PG_PORT" -U "$PG_USER" -d "$PG_DATABASE" -c "
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
"
```

#### Neo4j Health Check

```bash
# Neo4j Health Check Procedure
NEO4J_URI="bolt://localhost:7687"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="$NEO4J_PASSWORD"

# Test connection using cypher-shell
echo "RETURN 1 as test;" | cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Neo4j connection successful"
else
    echo "✗ Neo4j connection failed"
    exit 1
fi

# Check database statistics
echo "
CALL apoc.monitor.kernel() YIELD name, value
WHERE name IN ['DatabaseName', 'StoreSize', 'NodeCount', 'RelationshipCount']
RETURN name, value;
" | cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD"
```

### 2. Environment Configuration Validation

#### Docker Environment Validation

```bash
# Docker Environment Check Template
echo "Validating Docker environment..."

# Check Docker daemon
docker info > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Docker daemon is running"
else
    echo "✗ Docker daemon is not running"
    exit 1
fi

# Check Docker Compose
docker-compose --version > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Docker Compose is available"
else
    echo "✗ Docker Compose is not available"
    exit 1
fi

# Check container status
docker-compose ps --format "table {{.Name}}\t{{.State}}\t{{.Status}}"

# Validate all containers are healthy
UNHEALTHY=$(docker-compose ps --filter "health=unhealthy" -q | wc -l)
if [ "$UNHEALTHY" -eq 0 ]; then
    echo "✓ All containers are healthy"
else
    echo "✗ $UNHEALTHY containers are unhealthy"
    docker-compose ps --filter "health=unhealthy"
    exit 1
fi
```

#### Network Connectivity Validation

```bash
# Network Connectivity Check Template
echo "Validating network connectivity..."

# Internal service connectivity
SERVICES=(
    "n8n:5678"
    "postgres:5432"
    "neo4j:7474"
    "neo4j:7687"
    "qdrant:6333"
    "lightrag:8000"
)

for service in "${SERVICES[@]}"; do
    IFS=':' read -r host port <<< "$service"
    if nc -z "$host" "$port" 2>/dev/null; then
        echo "✓ $host:$port is reachable"
    else
        echo "✗ $host:$port is not reachable"
    fi
done

# External connectivity check
EXTERNAL_SERVICES=(
    "github.com:443"
    "docker.io:443"
    "registry-1.docker.io:443"
)

for service in "${EXTERNAL_SERVICES[@]}"; do
    IFS=':' read -r host port <<< "$service"
    if nc -z "$host" "$port" 2>/dev/null; then
        echo "✓ External $host:$port is reachable"
    else
        echo "✗ External $host:$port is not reachable"
    fi
done
```

### 3. Data Validation Procedures

#### Test Data Preparation Template

```sql
-- PostgreSQL Test Data Setup
-- This script prepares test data for n8n testing

-- Create test user
INSERT INTO users (email, password, first_name, last_name, settings)
VALUES (
    'test@example.com',
    '$2b$10$test.hash.placeholder',
    'Test',
    'User',
    '{"theme": "dark"}'
) ON CONFLICT (email) DO NOTHING;

-- Create test workflow
INSERT INTO workflow_entity (name, active, nodes, connections, settings, static_data)
VALUES (
    'Test Workflow',
    false,
    '[{"id": "test-node", "type": "test", "position": [100, 100]}]',
    '{}',
    '{}',
    '{}'
) ON CONFLICT (name) DO NOTHING;

-- Verify test data
SELECT
    'users' as table_name,
    count(*) as record_count
FROM users
WHERE email LIKE '%test%'
UNION ALL
SELECT
    'workflows' as table_name,
    count(*) as record_count
FROM workflow_entity
WHERE name LIKE '%Test%';
```

#### Neo4j Test Data Setup

```cypher
// Neo4j Test Data Setup
// This script prepares test graph data

// Create test nodes
CREATE (u:User {id: 'test-user-1', name: 'Test User', email: 'test@example.com'})
CREATE (w:Workflow {id: 'test-workflow-1', name: 'Test Workflow', active: false})
CREATE (n:Node {id: 'test-node-1', type: 'webhook', name: 'Test Webhook'})

// Create relationships
CREATE (u)-[:OWNS]->(w)
CREATE (w)-[:CONTAINS]->(n)

// Verify test data
MATCH (u:User)-[:OWNS]->(w:Workflow)-[:CONTAINS]->(n:Node)
WHERE u.email CONTAINS 'test'
RETURN count(*) as test_relationships;

// Check graph statistics
CALL apoc.meta.graph() YIELD nodes, relationships
RETURN nodes, relationships;
```

### 4. Performance Baseline Establishment

#### Performance Metrics Collection Template

```bash
# Performance Baseline Collection
echo "Collecting performance baselines..."

# System resource baseline
echo "System Resources:"
echo "CPU Cores: $(nproc)"
echo "Memory: $(free -h | grep '^Mem:' | awk '{print $2}')"
echo "Disk Space: $(df -h / | tail -1 | awk '{print $2}')"

# Container resource usage
echo "Container Resource Usage:"
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"

# Database performance baseline
echo "Database Performance Baseline:"
PGPASSWORD="$N8N_DB_PASSWORD" psql -h localhost -U n8n -d n8n -c "
SELECT
    'Total DB Size' as metric,
    pg_size_pretty(pg_database_size('n8n')) as value
UNION ALL
SELECT
    'Active Connections' as metric,
    count(*)::text as value
FROM pg_stat_activity;
"

# API response time baseline
echo "API Response Time Baseline:"
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:5678/api/v1/workflows"
```

#### Curl Format Template

```text
# curl-format.txt
     time_namelookup:  %{time_namelookup}\n
        time_connect:  %{time_connect}\n
     time_appconnect:  %{time_appconnect}\n
    time_pretransfer:  %{time_pretransfer}\n
       time_redirect:  %{time_redirect}\n
  time_starttransfer:  %{time_starttransfer}\n
                     ----------\n
          time_total:  %{time_total}\n
```

### 5. Security Validation Procedures

#### Security Check Template

```bash
# Security Validation Procedures
echo "Performing security validation..."

# Check for default passwords
echo "Checking for default passwords..."
DEFAULT_CHECKS=(
    "admin:admin"
    "admin:password"
    "test:test"
    "root:root"
)

for cred in "${DEFAULT_CHECKS[@]}"; do
    IFS=':' read -r user pass <<< "$cred"
    # Attempt login with default credentials
    response=$(curl -s -X POST http://localhost:5678/api/v1/login \
        -H "Content-Type: application/json" \
        -d "{\"email\":\"$user\",\"password\":\"$pass\"}" \
        -w "%{http_code}")

    if echo "$response" | grep -q "200"; then
        echo "⚠️  Default credentials $cred still active"
    else
        echo "✓ Default credentials $cred are disabled"
    fi
done

# Check SSL/TLS configuration
echo "Checking SSL/TLS configuration..."
for port in 5678 7474 6333; do
    openssl s_client -connect localhost:$port -verify_return_error < /dev/null 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "✓ SSL/TLS properly configured on port $port"
    else
        echo "⚠️  SSL/TLS not configured on port $port"
    fi
done

# Check exposed ports
echo "Checking exposed ports..."
netstat -tlnp | grep LISTEN | while read line; do
    port=$(echo $line | awk '{print $4}' | cut -d: -f2)
    echo "Port $port is exposed"
done
```

### 6. Monitoring Setup Procedures

#### Monitoring Configuration Template

```yaml
# monitoring-config.yml
# Monitoring configuration for test environment

version: "3.8"
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--web.console.libraries=/etc/prometheus/console_libraries"
      - "--web.console.templates=/etc/prometheus/consoles"

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=test123
    volumes:
      - grafana-storage:/var/lib/grafana

volumes:
  grafana-storage:
```

#### Prometheus Configuration

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "n8n"
    static_configs:
      - targets: ["localhost:5678"]
    metrics_path: "/metrics"

  - job_name: "postgres"
    static_configs:
      - targets: ["localhost:9187"]

  - job_name: "neo4j"
    static_configs:
      - targets: ["localhost:2004"]

  - job_name: "docker"
    static_configs:
      - targets: ["localhost:9323"]
```

### 7. Backup and Recovery Procedures

#### Backup Procedure Template

```bash
# Backup Procedure for Test Environment
BACKUP_DIR="/backup/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "Creating backup in $BACKUP_DIR"

# PostgreSQL backup
echo "Backing up PostgreSQL..."
PGPASSWORD="$N8N_DB_PASSWORD" pg_dump -h localhost -U n8n -d n8n > "$BACKUP_DIR/postgres_backup.sql"
if [ $? -eq 0 ]; then
    echo "✓ PostgreSQL backup completed"
else
    echo "✗ PostgreSQL backup failed"
fi

# Neo4j backup
echo "Backing up Neo4j..."
docker exec neo4j neo4j-admin dump --database=neo4j --to=/tmp/neo4j_backup.dump
docker cp neo4j:/tmp/neo4j_backup.dump "$BACKUP_DIR/neo4j_backup.dump"
if [ $? -eq 0 ]; then
    echo "✓ Neo4j backup completed"
else
    echo "✗ Neo4j backup failed"
fi

# Configuration backup
echo "Backing up configurations..."
cp -r .env docker-compose.yml "$BACKUP_DIR/"
if [ $? -eq 0 ]; then
    echo "✓ Configuration backup completed"
else
    echo "✗ Configuration backup failed"
fi

echo "Backup completed: $BACKUP_DIR"
```

#### Recovery Procedure Template

```bash
# Recovery Procedure for Test Environment
BACKUP_DIR="$1"

if [ -z "$BACKUP_DIR" ]; then
    echo "Usage: $0 <backup_directory>"
    exit 1
fi

echo "Restoring from backup: $BACKUP_DIR"

# Stop services
docker-compose down

# Restore PostgreSQL
echo "Restoring PostgreSQL..."
PGPASSWORD="$N8N_DB_PASSWORD" psql -h localhost -U n8n -d n8n < "$BACKUP_DIR/postgres_backup.sql"
if [ $? -eq 0 ]; then
    echo "✓ PostgreSQL restore completed"
else
    echo "✗ PostgreSQL restore failed"
fi

# Restore Neo4j
echo "Restoring Neo4j..."
docker cp "$BACKUP_DIR/neo4j_backup.dump" neo4j:/tmp/neo4j_backup.dump
docker exec neo4j neo4j-admin load --database=neo4j --from=/tmp/neo4j_backup.dump --force
if [ $? -eq 0 ]; then
    echo "✓ Neo4j restore completed"
else
    echo "✗ Neo4j restore failed"
fi

# Restore configurations
echo "Restoring configurations..."
cp "$BACKUP_DIR/.env" "$BACKUP_DIR/docker-compose.yml" .
if [ $? -eq 0 ]; then
    echo "✓ Configuration restore completed"
else
    echo "✗ Configuration restore failed"
fi

# Start services
docker-compose up -d

echo "Recovery completed from: $BACKUP_DIR"
```

## Validation Checklists

### Pre-Test Environment Checklist

- [ ] All required services are installed and configured
- [ ] All service health checks pass
- [ ] All network connectivity tests pass
- [ ] All database connections are verified
- [ ] All test data is prepared and validated
- [ ] All security measures are in place and tested
- [ ] All monitoring systems are configured and functional
- [ ] All backup procedures are tested and verified
- [ ] All recovery procedures are tested and verified
- [ ] All performance baselines are established
- [ ] All configuration files are backed up
- [ ] All environment variables are set correctly

### Service-Specific Validation Checklists

#### n8n Service Validation

- [ ] n8n web interface is accessible
- [ ] n8n API endpoints respond correctly
- [ ] n8n database connection is working
- [ ] n8n workflow execution is functional
- [ ] n8n authentication is working
- [ ] n8n logging is configured
- [ ] n8n metrics are being collected

#### PostgreSQL Validation

- [ ] PostgreSQL service is running
- [ ] Database connections are working
- [ ] All required tables exist
- [ ] Database permissions are correct
- [ ] Database backup is working
- [ ] Database restore is working
- [ ] Database monitoring is configured

#### Neo4j Validation

- [ ] Neo4j service is running
- [ ] Neo4j web interface is accessible
- [ ] Cypher queries are working
- [ ] Graph data is accessible
- [ ] Neo4j backup is working
- [ ] Neo4j restore is working
- [ ] Neo4j monitoring is configured

This protocol provides comprehensive procedures and templates for validating all test prerequisites. All procedures should be customized based on specific environment requirements and organizational standards.
