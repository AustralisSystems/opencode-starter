# MANDATORY: Enterprise Core Template Scaffold

**⚠️ CRITICAL REQUIREMENT ⚠️**

ALL Python/FastAPI/FastMCP code implementations **MUST** follow the COPY-THEN-AUGMENT process using the enterprise core template.

**Template Locations:**

**GitHub (Public Access):**
```
https://github.com/tristanaburns/fastapi-plugin-architecture-template
```

**Local (Development):**
```
C:\github_development\projects\fastapi-enterprise-core-template
```

**Clone Command:**
```bash
git clone https://github.com/tristanaburns/fastapi-plugin-architecture-template.git
```

---

## Why COPY-THEN-AUGMENT?

**Problem:** Generating code from scratch produces inconsistent results each time.

**Solution:** Use proven, tested scaffold → customize for specific needs.

**Template Development:** Weeks of enterprise-grade development already invested.

---

## Template Architecture

### Core Structure

```
fastapi-enterprise-core-template/
├── src/core/              # Universal plugin framework (REUSABLE)
│   ├── plugin_framework_manager.py    # Central orchestrator
│   ├── interfaces/                    # Plugin interfaces
│   ├── registry/                      # Dynamic discovery
│   ├── lifecycle/                     # Hot-loading
│   ├── security/                      # Sandboxing
│   ├── feature_flags/                 # Feature toggles
│   ├── dependency_injection/          # DI container
│   ├── configuration/                 # Config management
│   ├── monitoring/                    # Observability
│   ├── observability/                 # Metrics/logging
│   ├── orchestration/                 # Plugin orchestration
│   └── [20+ more core components]
│
├── app/                   # Reference implementation (CUSTOMIZE)
│   ├── auth/              # Multi-auth (FastAPI Users, OAuth, Auth0)
│   ├── models/            # SQLAlchemy models
│   ├── routes/            # API endpoints
│   ├── services/          # Business logic
│   ├── static/            # CSS, JS, images
│   └── main.py            # Production entry point
│
├── templates/             # Jinja2 templates (HTMX + TailwindCSS)
│   ├── components/        # Reusable components
│   ├── auth/              # Auth pages
│   └── app/               # App pages
│
├── plugins/               # Plugin implementations
├── tests/                 # Comprehensive test suite
├── deployments/           # Docker, K8s configs
├── alembic/               # Database migrations
└── docs/                  # Documentation
```

---

## Feature Flag System

**Toggle entire subsystems:**

```bash
# .env configuration
FEATURE_FLAG_UI_ENABLED=true              # HTMX + Jinja2 web UI
FEATURE_FLAG_MCP_ENABLED=true             # FastMCP integration
FEATURE_FLAG_PLUGIN_SYSTEM_ENABLED=true   # Plugin framework
FEATURE_FLAG_AUTH_OAUTH=true              # OAuth providers
FEATURE_FLAG_AUTH_AUTH0=true              # Auth0 SSO
FEATURE_FLAG_ADMIN_DASHBOARD=true         # Admin interface
```

**Deployment Configurations:**

| Use Case | UI | MCP | Plugins | Result |
|----------|----|----|---------|---------|
| **API-only Microservice** | ❌ | ❌ | ❌ | Pure REST API |
| **Full-Stack Web App** | ✅ | ❌ | ✅ | Web app with plugins |
| **MCP Server** | ❌ | ✅ | ✅ | FastMCP + API |
| **Universal Platform** | ✅ | ✅ | ✅ | Everything |

---

## Technology Stack

### Core (Always Present)
- ✅ **FastAPI** - Web framework
- ✅ **Pydantic v2** - Validation
- ✅ **SQLAlchemy (async)** - ORM
- ✅ **Uvicorn** - ASGI server
- ✅ **Alembic** - Database migrations

### Optional Components (Feature Flag Controlled)

**Web UI:**
- 🎛️ **HTMX** - Dynamic interactions
- 🎛️ **Jinja2** - Server-side templating
- 🎛️ **TailwindCSS** - Styling

**MCP Integration:**
- 🎛️ **FastMCP** - MCP server protocol
- 🎛️ **@mcp.tool()** decorators
- 🎛️ **@mcp.resource()** handlers
- 🎛️ **@mcp.prompt()** templates

**Authentication:**
- 🎛️ **FastAPI Users** - Built-in auth
- 🎛️ **Auth0** - Enterprise SSO
- 🎛️ **OAuth** - Social login (Google, GitHub)
- 🎛️ **Plugin API Keys** - Service auth

**Plugin System:**
- 🎛️ **54+ Provider Capabilities**
- 🎛️ **Hot-loading** plugins
- 🎛️ **Lifecycle management**
- 🎛️ **Sandboxed execution**

---

## Plugin Capabilities (54+ Types)

```python
class PluginCapability(Enum):
    # Core capabilities
    API = "api"
    UI = "ui"
    MCP = "mcp"
    DATABASE = "database"
    CACHE = "cache"

    # Authentication & Security
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    ENCRYPTION = "encryption"

    # Communication
    WEBSOCKET = "websocket"
    MESSAGING = "messaging"
    EMAIL = "email"

    # Storage & Data
    CLOUD_STORAGE = "cloud_storage"
    FILE_PROCESSING = "file_processing"
    DATA_PIPELINE = "data_pipeline"

    # Observability
    MONITORING = "monitoring"
    LOGGING = "logging"
    METRICS = "metrics"

    # ... 35+ more capabilities
```

---

## MANDATORY COPY-THEN-AUGMENT Process

### Step 1: Copy Template

```bash
# For new project
cp -r C:\github_development\projects\fastapi-enterprise-core-template your-project-name

# Or use as base and copy specific modules
cp -r C:\github_development\projects\fastapi-enterprise-core-template/src/core your-project/
cp -r C:\github_development\projects\fastapi-enterprise-core-template/app your-project/
```

### Step 2: Configure Features

```bash
cd your-project-name
cp .env.example .env

# Edit .env to enable/disable features
nano .env
```

### Step 3: Customize App

```bash
# Keep core framework (src/core/) intact
# Modify app/ for your specific use case:
- Update app/routes/ with your endpoints
- Modify app/models/ with your data models
- Customize templates/ for your UI
- Add plugins/ for domain-specific features
```

### Step 4: Remove Unused Components

```bash
# Example: API-only (no UI)
rm -rf templates/
rm -rf app/static/
# Set FEATURE_FLAG_UI_ENABLED=false
```

---

## Code Quality Standards (Built-In)

**All enforced via Makefile:**

```bash
make lint              # Flake8, Black, isort, mypy
make format            # Auto-format code
make type-check        # MyPy type checking
make security-check    # Bandit security scan
make test              # Pytest with 80% coverage minimum
make ci                # Full CI pipeline
```

**Standards:**
- ✅ **Coverage:** Minimum 80%
- ✅ **Complexity:** Max cyclomatic = 10
- ✅ **Type Hints:** MyPy strict mode
- ✅ **Security:** Bandit + Safety checks
- ✅ **Linting:** Black + isort + flake8

---

## Database Architecture

**Built-in Alembic migrations:**

```bash
make db-init           # Initialize schema
make db-migrate        # Run migrations
make db-migration      # Create new migration
```

**Async SQLAlchemy models:**
- User (FastAPI Users)
- Plugin API Keys
- Your custom models (add to app/models/)

---

## Authentication Layers

**Multiple auth options (choose via feature flags):**

1. **FastAPI Users** - app/auth/dependencies.py
2. **Auth0** - app/auth/oauth.py
3. **OAuth** - Social login
4. **Plugin API Keys** - app/auth/plugin_security.py
5. **JWT & Cookie** - Dual transport

---

## Deployment Configurations

**Docker:**
```bash
make docker-build
make docker-run
```

**Kubernetes:**
```bash
kubectl apply -f deployments/k8s/
```

**Production:**
```bash
make run-prod  # Gunicorn + Uvicorn workers
```

---

## Testing Framework

**Comprehensive test suite:**

```bash
make test              # All tests with coverage
make test-unit         # Unit tests only (pytest -m "unit")
make test-integration  # Integration tests (pytest -m "integration")
make test-plugin       # Plugin tests (pytest -m "plugin")
```

**Test markers:**
- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.plugin` - Plugin tests
- `@pytest.mark.security` - Security tests

---

## MANDATORY for Implementation Skills

**When using python-implement, fastapi-implement, or fastmcp-implement skills:**

### ⚠️ MUST DO:

1. **COPY from template FIRST**
   ```bash
   cp -r C:\github_development\projects\fastapi-enterprise-core-template your-project
   ```

2. **Configure feature flags** (.env)
   - Enable only what you need

3. **Customize app/** directory
   - Modify routes for your endpoints
   - Update models for your data
   - Customize templates for your UI

4. **Keep src/core/** intact
   - Universal framework stays as-is
   - Don't modify core components

5. **Run quality checks**
   ```bash
   make lint
   make test
   make security-check
   ```

### ❌ NEVER DO:

- ❌ Generate FastAPI code from scratch
- ❌ Create custom plugin systems
- ❌ Write auth from scratch
- ❌ Ignore feature flags
- ❌ Skip quality checks

---

## Key Files Reference

| File | Purpose | Modify? |
|------|---------|---------|
| `src/core/plugin_framework_manager.py` | Central orchestrator | ❌ Keep |
| `src/core/interfaces/` | Plugin interfaces | ❌ Keep |
| `app/main.py` | Production entry | ✅ Customize |
| `app/routes/` | API endpoints | ✅ Customize |
| `app/models/` | Data models | ✅ Customize |
| `templates/` | Jinja2 templates | ✅ Customize |
| `plugins/` | Your plugins | ✅ Add yours |
| `.env` | Configuration | ✅ Configure |
| `pyproject.toml` | Dependencies | ✅ Add yours |
| `Makefile` | Dev commands | ❌ Keep |

---

## Documentation References

**Template Documentation:**
- `README.md` - Quick start guide
- `CLAUDE.md` - AI assistant guidance
- `PROJECT_PURPOSE.md` - Template philosophy
- `docs/FEATURE_FLAGS_V1.0.md` - Feature flag system
- `docs/PROVIDER_CAPABILITIES_V1.0.md` - Plugin capabilities
- `docs/architecture/` - Architecture docs
- `docs/security/` - Security guidelines

---

## ⚠️ MANDATORY: MCP Tools Workflow

**ALL implementations MUST follow the MCP Tools workflow for EVERY task:**

### THE GOLDEN RULE

```
context7 (docs) → grep (examples) → neo4j-memory (record) → code → neo4j-memory (persist)
```

### THE 6-PHASE MANDATORY SEQUENCE

```
┌─────────────────────────────────────────────────────────────┐
│  START TASK                                                 │
│      ↓                                                      │
│  1. ✅ CONTEXT LOAD (neo4j-memory)                         │
│      ↓                                                      │
│  2. 🔴 MANDATORY RESEARCH (context7 + grep)                │
│      ↓                                                      │
│  3. ✅ PLANNING (sequential-thinking)                      │
│      ↓                                                      │
│  4. ✅ IMPLEMENTATION (filesystem + domain tools)          │
│      ↓                                                      │
│  5. ✅ PROGRESS TRACKING (neo4j-memory)                    │
│      ↓                                                      │
│  6. ✅ CONTEXT SAVE (neo4j-memory)                         │
│      ↓                                                      │
│  END TASK                                                   │
└─────────────────────────────────────────────────────────────┘
```

**🔴 CRITICAL: Phase 2 (Research) prevents AI hallucinations**

### MCP Tools Required

**Core Tools (MANDATORY):**
- `neo4j-memory` - Enduring knowledge graph for ALL persistence
- `context7` - Official documentation (REQUIRED before coding)
- `grep` - GitHub code examples (REQUIRED before coding)
- `sequential-thinking` - Structured planning
- `filesystem` - File operations
- `time` - Reverse date stamps (YYYY-MM-DD-HHMMSS)

**ABSOLUTELY FORBIDDEN:**
- ❌ Implementing without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving to neo4j-memory

**See:** `.claude/skills/mcp-tools-workflow/SKILL.md` for complete workflow

---

## Factory Pattern Architecture

**The template uses factory patterns throughout for maximum flexibility:**

### Provider Factory Pattern

```python
# All capabilities use provider factories
class StorageProviderFactory:
    """Factory for creating storage backends dynamically."""

    @staticmethod
    def create_provider(provider_type: str, config: Dict[str, Any]):
        if provider_type == "sqlite":
            return SQLiteProvider(config)
        elif provider_type == "postgresql":
            return PostgreSQLProvider(config)
        elif provider_type == "mongodb":
            return MongoDBProvider(config)
        elif provider_type == "tinydb":
            return TinyDBProvider(config)
```

### Plugin Factory Pattern

```python
# Plugins are created via factory with dependency injection
class PluginFactory:
    """Central factory for all plugin creation."""

    def create_plugin(
        self,
        plugin_id: str,
        config: PluginConfig,
        context: IPluginContext
    ) -> IPlugin:
        # Factory handles:
        # - Plugin instantiation
        # - Dependency injection
        # - Configuration binding
        # - Context provision
```

**Factory patterns used for:**
- Storage backends (SQLite, PostgreSQL, MongoDB, TinyDB)
- Authentication providers (FastAPI Users, OAuth, Auth0)
- Cache providers (Redis, Memcached, in-memory)
- Message queues (Kafka, RabbitMQ, Redis)
- All 54+ plugin capabilities

---

## Advanced Database Features

### Auto-Switching Database Backends

**The template provides enterprise-grade database capabilities:**

#### SQLite ↔ PostgreSQL Auto-Switching

```python
# Automatic switching based on environment
if os.getenv("DATABASE_TYPE") == "production":
    # PostgreSQL for production
    DATABASE_URL = os.getenv("POSTGRES_URL")
else:
    # SQLite for development
    DATABASE_URL = "sqlite+aiosqlite:///./dev.db"

# Auto-failover on connection failure
try:
    engine = create_async_engine(PRIMARY_DATABASE_URL)
    await engine.connect()
except Exception:
    # Automatic failback to SQLite
    engine = create_async_engine("sqlite+aiosqlite:///./fallback.db")
```

#### MongoDB Auto-Switching: Community ↔ Atlas

```python
# MongoDB provider auto-switches between local and cloud
class MongoDBProvider:
    """Auto-switching MongoDB provider."""

    async def connect(self):
        # Try MongoDB Atlas first (production)
        if os.getenv("MONGODB_ATLAS_URI"):
            try:
                client = AsyncIOMotorClient(os.getenv("MONGODB_ATLAS_URI"))
                await client.admin.command('ping')
                return client
            except Exception:
                # Failback to local MongoDB Community
                pass

        # Fallback to local MongoDB Community
        return AsyncIOMotorClient("mongodb://localhost:27017")
```

#### TinyDB ↔ MongoDB Failover

```python
# Lightweight NoSQL with failover
class NoSQLProviderFactory:
    """Factory with automatic failover."""

    async def create_provider(self, config):
        try:
            # Try MongoDB first
            return await MongoDBProvider(config).connect()
        except Exception:
            # Failback to TinyDB (file-based, no server required)
            return TinyDBProvider(config)
```

### Local-to-Remote Database Sync

**Built-in synchronization engine:**

```python
# Sync local changes to remote database
class DatabaseSyncEngine:
    """Synchronizes local SQLite/TinyDB to remote PostgreSQL/MongoDB."""

    async def sync(self):
        # 1. Detect local changes (since last sync)
        local_changes = await self.local_db.get_changes_since(last_sync)

        # 2. Upload to remote database
        await self.remote_db.bulk_upsert(local_changes)

        # 3. Download remote updates
        remote_changes = await self.remote_db.get_changes_since(last_sync)
        await self.local_db.bulk_upsert(remote_changes)

        # 4. Conflict resolution (last-write-wins)
        await self.resolve_conflicts()
```

### Failover and Failback

```python
# Automatic failover with health checks
class DatabaseHealthMonitor:
    """Monitors database health and triggers failover."""

    async def monitor_loop(self):
        while True:
            if not await self.check_primary_health():
                # Failover to backup
                await self.switch_to_backup()

            elif self.using_backup and await self.check_primary_health():
                # Failback to primary when healthy
                await self.switch_to_primary()

            await asyncio.sleep(60)  # Check every minute
```

### Database Configuration Examples

**SQLite + PostgreSQL with auto-failover:**
```bash
# .env configuration
DATABASE_TYPE=production  # or development
POSTGRES_URL=postgresql+asyncpg://user:pass@localhost:5432/db
SQLITE_FALLBACK=sqlite+aiosqlite:///./fallback.db
DATABASE_AUTO_FAILOVER=true
DATABASE_HEALTH_CHECK_INTERVAL=60
```

**MongoDB Atlas + Community with TinyDB failback:**
```bash
# .env configuration
MONGODB_ATLAS_URI=mongodb+srv://user:pass@cluster.mongodb.net/db
MONGODB_LOCAL_URI=mongodb://localhost:27017/db
TINYDB_FALLBACK=./fallback.json
MONGODB_AUTO_FAILOVER=true
```

**Local-to-Remote Sync:**
```bash
# .env configuration
DATABASE_SYNC_ENABLED=true
DATABASE_SYNC_INTERVAL=300  # seconds
DATABASE_SYNC_DIRECTION=bidirectional  # or upload-only, download-only
DATABASE_CONFLICT_RESOLUTION=last-write-wins  # or custom
```

---

## Expanded Plugin Provider Capabilities (54+)

### Complete Provider Taxonomy

**Core Infrastructure (11 capabilities):**
- Storage Provider, API Provider, Sync Provider, Data Provider
- Auth Provider, Cache Provider, Security Provider
- Logging Provider, Monitoring Provider, CLI Provider, Docs Provider

**Specialized Data (5 capabilities):**
- External API Provider, File Data Provider
- Database Data Provider, Stream Data Provider, ORM Provider

**Media & Communication (4 capabilities):**
- Audio Provider, Video Provider, Messaging Provider, SaaS Provider

**Real-time Communication (5 capabilities):**
- Voice Provider, Video Call Provider, Streaming Provider
- Notification Provider, Realtime Provider

**Message Queuing & Events (3 capabilities):**
- Message Queue Provider, Event Bus Provider, PubSub Provider

**Automation & Orchestration (6 capabilities):**
- Automation Provider, Orchestration Provider, Workflow Provider
- LowCode Provider, IaC Provider, CI/CD Provider

**Task & Job Processing (3 capabilities):**
- Task Queue Provider, Job Scheduler Provider, Worker Provider

**Cloud & Infrastructure (6 capabilities):**
- Cloud Provider, Hosting Provider, Compute Provider
- Network Provider, FaaS Provider, Serverless Provider

**Security & Identity (4 capabilities):**
- IAM Provider, RBAC Provider, SSO Provider, Certificate Provider

**User Interface (1 capability):**
- Web UI Provider (HTMX + Jinja2 + TailwindCSS)

**AI/ML (4 capabilities):**
- AI Provider, ML Provider, LLM Provider, Agent Provider

**Protocol (1 capability):**
- MCP Provider (Model Context Protocol)

**System Capabilities (3 capabilities):**
- Extension Point, Hot Swappable, Tool Integration

---

## Hot-Loading and State Preservation

**Zero-downtime plugin updates:**

### Hot-Loading Process

```python
# 1. Preserve current plugin state
old_state = await old_plugin.preserve_state()

# 2. Load new plugin version
new_plugin = await plugin_loader.load_plugin(new_version)

# 3. Restore state to new plugin
await new_plugin.restore_state(old_state)

# 4. Swap plugins atomically
await plugin_registry.replace_plugin(old_plugin, new_plugin)

# 5. Cleanup old plugin
await old_plugin.cleanup()
```

### State Preservation Interface

```python
class IHotSwappablePlugin(IPlugin):
    """Interface for plugins that support hot-loading."""

    async def preserve_state(self) -> Dict[str, Any]:
        """Preserve plugin state before swap."""

    async def restore_state(self, state: Dict[str, Any]) -> None:
        """Restore plugin state after swap."""
```

**All plugins in template support:**
- State preservation
- Zero-downtime updates
- Atomic swapping
- Rollback on failure

---

## Summary

**The Process:**
1. ✅ LOAD context with neo4j-memory
2. ✅ RESEARCH with context7 + grep
3. ✅ COPY enterprise template
4. ✅ CONFIGURE feature flags
5. ✅ CUSTOMIZE app/ directory
6. ✅ ADD your domain logic
7. ✅ RUN quality checks
8. ✅ SAVE outcomes to neo4j-memory
9. ✅ DEPLOY

**DO NOT:**
- ❌ Generate from scratch
- ❌ Ignore the scaffold
- ❌ Skip MCP tools workflow
- ❌ Skip quality gates

**This scaffold represents weeks of enterprise development. Use it!**

**Key Features:**
- ✅ Factory patterns throughout
- ✅ Database auto-switching (SQLite/PostgreSQL, MongoDB/TinyDB)
- ✅ Auto-failover and failback
- ✅ Local-to-remote sync
- ✅ 54+ plugin provider capabilities
- ✅ Hot-loading with state preservation
- ✅ MCP tools workflow integration

---

## Related GitHub Repositories

### Enterprise Templates (Public Access)

**1. FastAPI Plugin Architecture Template** (Main Enterprise Template)
- **GitHub:** https://github.com/tristanaburns/fastapi-plugin-architecture-template
- **Description:** Universal FastAPI Plugin Architecture Template - Enterprise-grade plugin system with hot-loading, security sandbox, and dynamic service management
- **Use For:** Complete FastAPI applications with plugin architecture
- **Features:** 54+ plugin capabilities, hot-loading, feature flags, multi-auth

**2. FastAPI Storage Factory Template**
- **GitHub:** https://github.com/tristanaburns/fastapi-storage-factory-template
- **Description:** MongoDB auto-failover & recovery with comprehensive health monitoring
- **Use For:** Applications requiring robust database failover
- **Features:** MongoDB/TinyDB auto-failover, Apache Kafka, object storage factories

**3. Real-World Production Example**
- **GitHub:** https://github.com/tristanaburns/agentic-intelligent-automation-azure
- **Description:** Enterprise AD group management automation with Power Automate, Azure AI, and Azure Automation
- **Use For:** Reference implementation showing template in production
- **Location:** See `ai_agent_services/shared_components/database/factory.py` (745 lines)

### Quick Clone Commands

```bash
# Clone main enterprise template
git clone https://github.com/tristanaburns/fastapi-plugin-architecture-template.git

# Clone storage factory template
git clone https://github.com/tristanaburns/fastapi-storage-factory-template.git

# Clone real-world example (for reference)
git clone https://github.com/tristanaburns/agentic-intelligent-automation-azure.git
```

---

**Template Version:** v2.0.0
**Last Updated:** 2025-10-22
**Mandatory for:** ALL Python/FastAPI/FastMCP implementations
**MCP Workflow:** REQUIRED for all tasks
**GitHub:** https://github.com/tristanaburns/fastapi-plugin-architecture-template
