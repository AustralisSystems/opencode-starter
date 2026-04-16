# Advanced Production Examples - Real-World Template Applications

**Date:** 2025-10-22
**Status:** PRODUCTION READY - REAL APPLICATIONS
**Purpose:** Showcase advanced capabilities of the enterprise templates in production

---

## Overview

This document showcases advanced production applications built with the FastAPI enterprise templates, demonstrating capabilities beyond the core database factory pattern. These are **REAL, WORKING applications** currently in production use.

**Why These Matter:**
- Prove the templates work for complex enterprise scenarios
- Show advanced patterns (CLI/REST API mapping, HTMX/Jinja2 integration)
- Demonstrate security-first architecture in practice
- Provide real-world reference implementations

---

## 1. REST API Orchestrator - CLI to REST API Automation Engine

**GitHub Repository:** https://github.com/tristanaburns/rest-api-orchestrator

**Clone Command:**
```bash
git clone https://github.com/tristanaburns/rest-api-orchestrator.git
cd rest-api-orchestrator
```

### What Makes This Special

This application demonstrates **1-to-1 mapping between Python CLI and REST API endpoints** - a powerful pattern for creating dual-interface applications that work both as command-line tools and web services.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  CLI Interface (cli.py)    REST API (FastAPI)           │
│  ├── --list-credentials    ← → GET /api/v1/credentials │
│  ├── --store-credential   ← → POST /api/v1/credentials │
│  ├── --get /endpoint       ← → GET /api/proxy/endpoint │
│  ├── --post /endpoint      ← → POST /api/proxy/endpoint│
│  └── --interactive         ← → WebSocket /ws/session   │
└─────────────────────────────────────────────────────────┘
```

**Every CLI command has a corresponding REST API endpoint**

### Key Features

#### 1. Enterprise Security Architecture

**AES-256-GCM Encryption with PBKDF2 Key Derivation**

```python
# Security implementation from production
class CredentialManager:
    """Secure encrypted credential storage."""

    def encrypt_credential(self, credential: str, master_password: str) -> bytes:
        """
        Encrypt credential using AES-256-GCM.

        Security features:
        - PBKDF2 key derivation (100,000 iterations)
        - Unique salt per credential
        - Authentication tag for integrity
        - No plaintext storage
        """
        salt = os.urandom(32)
        key = PBKDF2(master_password, salt, dkLen=32, count=100000)
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(credential.encode())

        return salt + cipher.nonce + tag + ciphertext
```

**Key Security Features:**
- Master password NEVER stored on disk
- Zero-knowledge architecture (lost passwords cannot be recovered)
- Runtime-only password existence
- No backdoors or password hints
- Session-based password caching

#### 2. Platform-Specific Templates

**NSX-T Integration:**
```python
# Automated endpoint discovery for VMware NSX-T
discovery_templates = {
    "nsx-t": {
        "base_paths": [
            "/api/v1",
            "/policy/api/v1"
        ],
        "endpoints": [
            "/logical-switches",
            "/infra/segments",
            "/infra/tier-0s",
            "/infra/tier-1s"
        ]
    }
}
```

**Kubernetes Integration:**
```python
# Kubernetes API discovery
discovery_templates = {
    "kubernetes": {
        "base_paths": [
            "/api/v1",
            "/apis/apps/v1",
            "/apis/networking.k8s.io/v1"
        ],
        "discovery": "openapi/v2"
    }
}
```

#### 3. OpenAPI/Swagger Integration

**Automatic Endpoint Discovery:**
```python
def discover_endpoints(base_url: str, platform: str = None):
    """
    Automatically discover all available API endpoints.

    Process:
    1. Fetch OpenAPI/Swagger specification
    2. Parse endpoint definitions
    3. Extract parameters and schemas
    4. Build interactive endpoint catalog
    5. Cache for offline use
    """
    spec_url = f"{base_url}/openapi.json"
    spec = requests.get(spec_url).json()

    endpoints = {}
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            endpoints[path] = {
                "method": method.upper(),
                "parameters": details.get("parameters", []),
                "requestBody": details.get("requestBody", {}),
                "responses": details.get("responses", {})
            }

    return endpoints
```

#### 4. Data Management and Caching

**Response Storage with Transformation:**
```python
class DataManager:
    """Manage API response data with caching and transformation."""

    def store_response(self, endpoint: str, data: dict):
        """
        Store API response with metadata.

        Features:
        - Automatic JSON formatting
        - Timestamp tracking
        - Deduplication
        - Compression for large responses
        """
        cache_entry = {
            "endpoint": endpoint,
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "hash": hashlib.sha256(json.dumps(data).encode()).hexdigest()
        }

        # Store with automatic compression
        with gzip.open(f"data/{endpoint.replace('/', '_')}.json.gz", 'wt') as f:
            json.dump(cache_entry, f, indent=2)

    def transform_data(self, data: dict, transformation: str):
        """
        Apply transformations to response data.

        Transformations:
        - JMESPath queries
        - JSONPath filtering
        - Custom Python expressions
        - Data type conversions
        """
        if transformation.startswith("jmespath:"):
            import jmespath
            return jmespath.search(transformation[9:], data)
        elif transformation.startswith("jsonpath:"):
            from jsonpath_ng import parse
            return [match.value for match in parse(transformation[9:]).find(data)]
```

#### 5. Automation and CI/CD Integration

**Non-Interactive Mode:**
```bash
# Set master password via environment
export CLI_MASTER_PASSWORD="secure_password"

# Run automated sequence
python cli.py --non-interactive --sequence operations.json

# Example operations.json
{
    "operations": [
        {
            "type": "setup",
            "url": "https://api.example.com",
            "auth_type": "basic",
            "credential": "api-prod"
        },
        {
            "type": "get",
            "endpoint": "/api/v1/data",
            "save_to": "backup_data.json"
        },
        {
            "type": "transform",
            "source": "backup_data.json",
            "transformation": "jmespath:items[?status=='active']",
            "save_to": "active_items.json"
        }
    ]
}
```

#### 6. Interactive REST API Client

**CLI Interactive Mode:**
```bash
$ python cli.py --interactive

> setup https://lab-nsx-01.lab.example.com basic lab-nsx-01 --no-verify-ssl
Connected to NSX Manager (version 3.2.0)

> get /api/v1/logical-switches
Retrieved 15 logical switches

> save nsx_switches_backup.json
Data saved successfully

> transform jmespath:items[?admin_state=='UP']
Filtered to 12 active switches
```

### Real-World Usage Example

**NSX Manager Backup and Synchronization:**

```bash
# 1. Set master password
export CLI_MASTER_PASSWORD="production_password"

# 2. Connect to source NSX Manager
python cli.py --interactive
> setup https://nsx-manager-01.corp.com basic nsx-prod-01 --no-verify-ssl
> get /policy/api/v1/infra/segments
> save source_segments.json

# 3. Connect to target NSX Manager
> setup https://nsx-manager-02.corp.com basic nsx-prod-02 --no-verify-ssl
> get /policy/api/v1/infra/segments
> save target_segments.json

# 4. Run diff comparison (using REST API endpoint)
curl -X POST http://localhost:8000/api/v1/diff \
  -H "Content-Type: application/json" \
  -d '{
    "source": "source_segments.json",
    "target": "target_segments.json"
  }'

# 5. Apply synchronization
curl -X POST http://localhost:8000/api/v1/sync \
  -H "Content-Type: application/json" \
  -d '{
    "source": "nsx-manager-01.corp.com",
    "target": "nsx-manager-02.corp.com",
    "diff_file": "segment_diff.json"
  }'
```

### Production Benefits

**Why This Pattern Matters:**

1. **Dual Interface:** Same functionality via CLI or REST API
2. **Automation Ready:** Non-interactive mode for CI/CD
3. **Security First:** Enterprise-grade encryption and credential management
4. **Platform Agnostic:** Works with any REST API (NSX-T, Kubernetes, custom APIs)
5. **Developer Friendly:** Interactive mode for exploration, automated mode for production

---

## 2. HTMLX/Jinja2 Template System - Modern Web UI

**GitHub Repository:** https://github.com/tristanaburns/fastapi-storage-factory-template

**Clone Command:**
```bash
git clone https://github.com/tristanaburns/fastapi-storage-factory-template.git
cd fastapi-storage-factory-template
```

### What Makes This Special

This template demonstrates **HTMX + Jinja2 integration** for creating modern single-page application experiences without JavaScript frameworks, using the enterprise template as its foundation.

### Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│  FastAPI Backend        HTMX Frontend                        │
│  ├── Jinja2 Templates   ├── Full Page Templates (100+)      │
│  ├── Session Auth       ├── Partial Templates (HTMX)        │
│  ├── CSRF Protection    ├── DaisyUI Components              │
│  └── Auto-Detection     └── Real-time Updates               │
└──────────────────────────────────────────────────────────────┘
```

### Key Features

#### 1. HTMX Single-Page Application Behavior

**WITHOUT JavaScript frameworks, WITHOUT client-side routing:**

```html
<!-- layouts/base.html - Foundation -->
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div id="sidebar">{% include "layouts/components/sidebar.html" %}</div>
    <main id="main-content">
        {% block content %}{% endblock %}
    </main>
    <script>
        // CRITICAL: Configure HTMX for session authentication
        document.body.addEventListener('htmx:configRequest', (event) => {
            event.detail.headers['X-Requested-With'] = 'XMLHttpRequest';
            event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
            event.detail.xhr.withCredentials = true; // Include session cookies
        });
    </script>
</body>
</html>
```

**Navigation with HTMX (No Page Reload):**

```html
<!-- Sidebar navigation - layouts/components/sidebar.html -->
<nav role="navigation" aria-label="Main navigation">
    <ul>
        <li>
            <a href="/objects"
               hx-get="/objects"
               hx-target="#main-content"
               hx-swap="innerHTML"
               hx-push-url="true">
                <i class="fas fa-cubes"></i>
                Network Objects
            </a>
        </li>
        <li>
            <a href="/sync"
               hx-get="/sync"
               hx-target="#main-content"
               hx-swap="innerHTML"
               hx-push-url="true">
                <i class="fas fa-sync"></i>
                Synchronization
            </a>
        </li>
    </ul>
</nav>
```

**What happens:**
1. User clicks "Network Objects"
2. HTMX intercepts the click
3. Sends GET request to `/objects` with header `HX-Request: true`
4. Server detects HTMX request, returns partial template (content only)
5. HTMX swaps content into `#main-content`
6. Browser URL updates to `/objects` (but no page reload!)
7. Result: Instant navigation, no flicker, browser history works

#### 2. Dual-Template Pattern (Full Page + Partial)

**Backend Auto-Detection:**

```python
# FastAPI route with auto-detection
@app.get("/objects")
async def objects_list(request: Request, current_user: User = Depends(get_current_user_session)):
    """
    Serves either full page or partial based on request type.

    - Direct URL access → Full page with layout
    - HTMX request → Partial content only
    """
    context = {
        "request": request,
        "current_user": current_user,
        "objects": await object_service.list_objects()
    }

    # Auto-detection based on HX-Request header
    if request.headers.get("HX-Request"):
        # HTMX request → Return partial (content only)
        return templates.TemplateResponse("objects/list_partial.html", context)
    else:
        # Direct access → Return full page (with layout)
        return templates.TemplateResponse("objects/list.html", context)
```

**Full Page Template:**

```html
<!-- objects/list.html -->
{% extends "layouts/base.html" %}

{% block title %}Network Objects - Configuration Manager{% endblock %}

{% block breadcrumb %}
<ol class="flex items-center space-x-2 text-sm">
    <li><a href="/" hx-get="/" hx-target="#main-content">Home</a></li>
    <li class="text-gray-400">/</li>
    <li class="text-gray-900 font-medium">Network Objects</li>
</ol>
{% endblock %}

{% block content %}
    {% include "objects/list_partial.html" %}
{% endblock %}
```

**Partial Template:**

```html
<!-- objects/list_partial.html -->
<div class="space-y-6">
    <div class="flex justify-between items-center">
        <div>
            <h1 class="text-3xl font-bold text-gray-900">Network Objects</h1>
            <p class="text-gray-600 mt-1">Manage network configuration objects</p>
        </div>
        <div class="flex space-x-3">
            <button hx-get="/objects/create"
                    hx-target="#main-content"
                    hx-swap="innerHTML"
                    hx-push-url="true"
                    class="btn btn-primary">
                <i class="fas fa-plus mr-2"></i>Create Object
            </button>
        </div>
    </div>

    <!-- Objects table -->
    <div id="objects-table">
        {% for obj in objects %}
        <div class="card">
            <h3>{{ obj.name }}</h3>
            <button hx-delete="/objects/{{ obj.id }}"
                    hx-confirm="Delete {{ obj.name }}?"
                    hx-target="closest .card"
                    hx-swap="outerHTML">
                Delete
            </button>
        </div>
        {% endfor %}
    </div>
</div>
```

#### 3. Real-Time Updates with HTMX Polling

**Live Synchronization Status:**

```html
<!-- sync/dashboard.html -->
<div hx-get="/api/v1/sync/status"
     hx-trigger="every 5s"
     hx-target="#sync-status"
     hx-swap="innerHTML">
    <div id="sync-status">
        <!-- Status updates automatically every 5 seconds -->
        <div class="flex items-center space-x-3">
            <i class="fas fa-sync fa-spin text-blue-500"></i>
            <span>Syncing... {{ progress }}%</span>
        </div>
    </div>
</div>
```

**Backend Endpoint:**

```python
@app.get("/api/v1/sync/status")
async def sync_status(request: Request):
    """Returns current sync status for HTMX polling."""
    status = await sync_service.get_current_status()

    # Return partial template with updated status
    return templates.TemplateResponse("partials/sync_status.html", {
        "request": request,
        "status": status.state,
        "progress": status.progress_percentage,
        "current_operation": status.current_operation
    })
```

#### 4. Form Submissions Without Page Reload

**Create Object Form:**

```html
<!-- objects/create_partial.html -->
<form hx-post="/objects/create"
      hx-target="#main-content"
      hx-swap="innerHTML"
      hx-indicator="#create-spinner"
      class="space-y-4">

    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">

    <div>
        <label for="name">Object Name</label>
        <input type="text"
               id="name"
               name="name"
               required
               class="form-input">
    </div>

    <div>
        <label for="type">Object Type</label>
        <select id="type" name="type" required class="form-select">
            <option value="segment">Segment</option>
            <option value="tier1">Tier-1 Gateway</option>
            <option value="tier0">Tier-0 Gateway</option>
        </select>
    </div>

    <div class="flex justify-end space-x-3">
        <button type="button"
                hx-get="/objects"
                hx-target="#main-content"
                class="btn btn-secondary">
            Cancel
        </button>
        <button type="submit" class="btn btn-primary">
            <span id="create-spinner" class="htmx-indicator">
                <i class="fas fa-spinner fa-spin mr-2"></i>
            </span>
            Create Object
        </button>
    </div>
</form>
```

**Backend Handler:**

```python
@app.post("/objects/create")
async def create_object(
    request: Request,
    name: str = Form(...),
    type: str = Form(...),
    csrf_token: str = Form(...),
    current_user: User = Depends(get_current_user_session)
):
    """
    Create new object and return updated list.

    For HTMX requests:
    - Return partial template with success message
    - Include updated objects list
    """
    # Validate CSRF token
    if not validate_csrf(request, csrf_token):
        return templates.TemplateResponse("partials/error.html", {
            "request": request,
            "error": "Invalid CSRF token"
        }, status_code=403)

    # Create object
    obj = await object_service.create(name=name, type=type, created_by=current_user.id)

    # Return success response (HTMX will swap into #main-content)
    objects = await object_service.list_objects()
    return templates.TemplateResponse("objects/list_partial.html", {
        "request": request,
        "objects": objects,
        "flash_message": {
            "type": "success",
            "message": f"Object '{name}' created successfully"
        }
    })
```

#### 5. DaisyUI Components Integration

**Modern UI Components Without Custom CSS:**

```html
<!-- Using DaisyUI classes for instant professional UI -->
<div class="card bg-base-100 shadow-xl">
    <div class="card-body">
        <h2 class="card-title">Network Object Details</h2>
        <div class="stats stats-vertical lg:stats-horizontal shadow">
            <div class="stat">
                <div class="stat-title">Total Objects</div>
                <div class="stat-value">{{ total_objects }}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Active</div>
                <div class="stat-value text-success">{{ active_objects }}</div>
            </div>
        </div>
        <div class="card-actions justify-end">
            <button class="btn btn-primary">View Details</button>
        </div>
    </div>
</div>

<!-- Alert/Toast notifications -->
<div class="alert alert-success shadow-lg">
    <div>
        <svg class="stroke-current flex-shrink-0 h-6 w-6">...</svg>
        <span>Object synchronized successfully!</span>
    </div>
</div>

<!-- Loading states -->
<button class="btn btn-primary loading">
    Synchronizing...
</button>
```

#### 6. Modular Component Architecture (SOLID Principles)

**Components Directory Structure:**

```
app/templates/layouts/components/
├── sidebar.html         # Navigation ONLY
├── header.html          # Top bar ONLY
├── styles.html          # CSS and theming ONLY
├── scripts.html         # JavaScript and HTMX config ONLY
├── alerts.html          # Server-side flash messages ONLY
└── toasts.html          # Client-side notifications ONLY
```

**Each component has a single responsibility:**

```html
<!-- layouts/components/sidebar.html - Navigation ONLY -->
<aside class="w-64 bg-gray-900 text-white min-h-screen">
    <div class="p-4">
        <img src="/static/logo.png" alt="Logo" class="h-8">
    </div>
    <nav>
        <ul>
            {% for item in navigation_items %}
            <li>
                <a href="{{ item.url }}"
                   hx-get="{{ item.url }}"
                   hx-target="#main-content">
                    {{ item.name }}
                </a>
            </li>
            {% endfor %}
        </ul>
    </nav>
</aside>
```

```html
<!-- layouts/components/alerts.html - Flash messages ONLY -->
<div id="alerts-container" class="fixed top-4 right-4 z-50 space-y-2">
    {% if flash_messages %}
        {% for message in flash_messages %}
        <div class="alert alert-{{ message.type }} shadow-lg">
            <div>
                <i class="fas fa-{{ message.icon }}"></i>
                <span>{{ message.text }}</span>
            </div>
            <button onclick="this.parentElement.remove()">✕</button>
        </div>
        {% endfor %}
    {% endif %}
</div>
```

### Template Inventory

**100+ Production-Ready Templates:**

**Admin Templates (15 files):**
- `admin/dashboard.html` - Enhanced admin dashboard
- `admin/user_registration.html` - User management
- `admin/database_health.html` - Database monitoring
- `admin/storage_health.html` - Storage system monitoring
- `admin/logs.html` - Application logs viewer
- `admin/rbac_interface.html` - Role-based access control
- `admin/bulk_user_management.html` - Bulk operations
- And more...

**HTMX Integration Examples:**
- `sync/index.html` - Real-time sync status with polling
- `diff/diff.html` - Configuration diff viewer
- `excel/import.html` - Excel import with progress tracking
- `discovery/operations.html` - API endpoint discovery
- `audit/index.html` - Audit trail with filtering

**Workflow Components:**
- `components/workflow/workflow_canvas.html` - Drag-and-drop workflow builder
- `components/workflow/node_palette.html` - Available workflow nodes
- `components/workflow/property_panel.html` - Node configuration

### Security Architecture

**Session-Based Authentication:**

```python
# Session configuration
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie="session_id",
    max_age=3600,
    same_site="lax",
    https_only=True  # Production only
)

# Session authentication dependency
async def get_current_user_session(request: Request) -> User:
    """Get current user from session (for web UI)."""
    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_id = await session_service.get_user_id(session_id)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid session")

    return await user_service.get(user_id)
```

**CSRF Protection:**

```python
# CSRF token generation
def generate_csrf_token(request: Request) -> str:
    """Generate CSRF token for session."""
    token = secrets.token_urlsafe(32)
    request.session["csrf_token"] = token
    return token

# CSRF validation
def validate_csrf(request: Request, token: str) -> bool:
    """Validate CSRF token from form."""
    session_token = request.session.get("csrf_token")
    return secrets.compare_digest(token, session_token) if session_token else False
```

### Real-World Usage Example

**Complete CRUD Flow with HTMX:**

```python
# 1. List objects (GET /objects)
# → Returns full page on direct access
# → Returns partial on HTMX request

# 2. Create form (GET /objects/create)
# → User clicks "Create" button (HTMX navigation)
# → Server returns create form partial
# → Form appears in #main-content (no page reload)

# 3. Submit form (POST /objects/create)
# → User submits form (HTMX intercepts)
# → Server validates, creates object
# → Server returns updated list partial
# → List appears in #main-content with success message

# 4. Delete object (DELETE /objects/{id})
# → User clicks "Delete" (HTMX confirms)
# → Server deletes object
# → Server returns empty response
# → HTMX removes the card from DOM

# 5. Real-time sync (polling every 5s)
# → HTMX automatically polls /api/v1/sync/status
# → Server returns updated status partial
# → HTMX swaps new status into #sync-status
# → User sees live progress without manual refresh
```

### Production Benefits

**Why HTMX + Jinja2 Matters:**

1. **No JavaScript Framework:** Simpler stack, faster development
2. **Progressive Enhancement:** Works without JavaScript (accessibility)
3. **Server-Side Rendering:** Better SEO, faster initial load
4. **Security:** Session-based auth, CSRF protection built-in
5. **Developer Experience:** Familiar Jinja2 syntax, Python backend
6. **Performance:** Partial updates reduce data transfer
7. **100+ Templates:** Complete application UI ready to use

---

## 3. Integration with Enterprise Template

### How These Examples Use the Core Template

Both applications are built on the **FastAPI Plugin Architecture Template** foundation:

**REST API Orchestrator:**
```
Uses from core template:
├── Factory pattern for credential providers (encrypted, plaintext, env vars)
├── Database factory for caching (SQLite/PostgreSQL auto-switching)
├── Plugin architecture for platform templates (NSX-T, Kubernetes)
└── Security framework (encryption, validation, audit logging)

Adds on top:
├── CLI interface with 1-to-1 REST API mapping
├── Interactive mode with command history
├── Batch operation automation
└── OpenAPI/Swagger integration
```

**HTMLX/Jinja2 Template:**
```
Uses from core template:
├── Database factory (MongoDB with TinyDB fallback)
├── Authentication factory (session-based for web, JWT for API)
├── Cache factory (Redis with in-memory fallback)
└── Storage factory (MinIO with local filesystem fallback)

Adds on top:
├── 100+ HTMX-enabled Jinja2 templates
├── Dual-template pattern (full page + partial)
├── DaisyUI component integration
├── Real-time updates with HTMX polling
└── SOLID principles component architecture
```

### Common Patterns Across All Examples

**1. COPY-THEN-AUGMENT Workflow:**
```bash
# Copy template
git clone https://github.com/tristanaburns/fastapi-plugin-architecture-template.git my-app
cd my-app

# Configure feature flags
# Edit config/features.yaml
features:
  database_factory: true
  authentication_factory: true
  cache_factory: true
  storage_factory: true
  # Add custom features
  htmx_templates: true  # For web UI
  cli_interface: true   # For CLI/REST mapping

# Customize app/ directory
# Keep src/core/ intact
# Add your domain logic in app/
```

**2. Factory Pattern Throughout:**
```python
# All three applications use factory patterns

# Database Factory (all apps)
db = DatabaseFactory.create("postgresql", config)  # Auto-fails to SQLite

# Storage Factory (HTMLX app)
storage = StorageFactory.create("minio", config)  # Auto-fails to filesystem

# Credential Factory (REST Orchestrator)
creds = CredentialFactory.create("encrypted", config)  # AES-256-GCM

# Template Factory (HTMLX app)
template = TemplateFactory.create(request)  # Auto-detects full vs partial
```

**3. Security-First Architecture:**
```python
# Common security patterns across all apps

# 1. No hardcoded credentials
credentials = os.getenv("API_KEY")  # From environment

# 2. Encryption at rest
encrypted_value = encrypt_aes_gcm(value, key)  # AES-256-GCM

# 3. Secure sessions
session_id = secrets.token_urlsafe(32)  # Cryptographically secure

# 4. CSRF protection
csrf_token = generate_csrf_token(request)  # All forms protected

# 5. Input validation
validated_data = ObjectSchema.parse_obj(data)  # Pydantic validation
```

---

## Quick Reference: Which Example for Which Use Case

### Use REST API Orchestrator When:
- ✅ You need both CLI and REST API interfaces
- ✅ You're automating multi-platform REST APIs (NSX-T, Kubernetes, etc.)
- ✅ You need secure credential management for CI/CD
- ✅ You want OpenAPI/Swagger auto-discovery
- ✅ You need data caching and transformation
- ✅ You're building platform integration tools

### Use HTMLX/Jinja2 Template When:
- ✅ You need a modern web UI without JavaScript frameworks
- ✅ You want server-side rendering with SPA-like experience
- ✅ You need real-time updates (polling, websockets)
- ✅ You want 100+ production-ready templates
- ✅ You need session-based authentication for web
- ✅ You're building admin dashboards or configuration managers

### Use Database Factory Example When:
- ✅ You need automatic database failover
- ✅ You want SQLite ↔ PostgreSQL auto-switching
- ✅ You need MongoDB with TinyDB fallback
- ✅ You want local-to-remote database sync
- ✅ You need health monitoring and automatic failback

---

## GitHub Repositories Summary

| Repository | Purpose | Key Features | Clone Command |
|------------|---------|--------------|---------------|
| **fastapi-plugin-architecture-template** | Core enterprise template | 54+ plugin capabilities, factory patterns, feature flags | `git clone https://github.com/tristanaburns/fastapi-plugin-architecture-template.git` |
| **rest-api-orchestrator** | CLI/REST automation engine | 1-to-1 CLI/API mapping, AES-256-GCM encryption, platform templates | `git clone https://github.com/tristanaburns/rest-api-orchestrator.git` |
| **fastapi-storage-factory-template** | HTMLX/Jinja2 web UI | 100+ templates, HTMX SPA, DaisyUI components, SOLID architecture | `git clone https://github.com/tristanaburns/fastapi-storage-factory-template.git` |
| **agentic-intelligent-automation-azure** | Production database factory | 745-line factory.py, multi-DB support, real failover | `git clone https://github.com/tristanaburns/agentic-intelligent-automation-azure.git` |

---

## Next Steps

### To Explore REST API Orchestrator:
```bash
git clone https://github.com/tristanaburns/rest-api-orchestrator.git
cd rest-api-orchestrator
pip install -r requirements.txt
export CLI_MASTER_PASSWORD="test_password"
python cli.py --interactive
```

### To Explore HTMLX/Jinja2 Templates:
```bash
git clone https://github.com/tristanaburns/fastapi-storage-factory-template.git
cd fastapi-storage-factory-template
pip install -r requirements.txt
uvicorn app.main:app --reload
# Visit http://localhost:8000
```

### To Explore Database Factory:
```bash
git clone https://github.com/tristanaburns/agentic-intelligent-automation-azure.git
cd agentic-intelligent-automation-azure/ai_agent_services/shared_components/database
# Read factory.py (745 lines of production database factory code)
```

---

**Document Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** PRODUCTION READY
**All Examples:** Verified working in production environments

**These are REAL applications, not theoretical examples.**
**Clone them. Run them. Learn from them. Build with them.**
