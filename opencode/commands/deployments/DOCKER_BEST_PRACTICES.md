# Docker Configuration Protocol & Best Practices Guide

**Version:** 3.0.0
**Last Updated:** 2025-01-11
**Status:** MANDATORY - Must be strictly followed
**Scope:** Universal protocol for all Docker configurations and deployments

---

## Purpose

This document provides **MANDATORY protocols and best practices** for creating, maintaining, and validating Docker configurations. It serves as an **instruction guide for LLMs** to ensure all Dockerfiles, docker-compose files, and related configurations follow industry best practices and align with DEPLOYMENT-STRUCTURE.md v1.0.0.

## Core Principles

1. **Multi-Stage Builds** - Separate build and runtime stages
2. **Layer Caching Optimization** - Dependencies before source code
3. **Security First** - Non-root users, minimal images, no build tools in runtime
4. **Production-Grade Servers** - Gunicorn with worker processes, not single-process
5. **Proper Entry Points** - Use production application, not test servers
6. **Structure Alignment** - Follow DEPLOYMENT-STRUCTURE.md directory structure

---

## MANDATORY Directory & File Structure

### Service-Level Structure (Per Service)

```
services/
└── service-name/                    # Service root directory
    ├── Dockerfile                  # MANDATORY: Service Dockerfile
    ├── README.md                   # MANDATORY: Service documentation
    ├── .dockerignore               # RECOMMENDED: Exclude unnecessary files
    ├── pyproject.toml              # If Python service (reference to root)
    ├── requirements.txt            # If Python service (reference to root)
    └── [application code]          # Service-specific code structure
```

### Repository-Level Structure

```
repository-root/
├── .dockerignore                   # MANDATORY: Root-level Docker ignore
├── docker-compose.yml              # MANDATORY: Base compose file
├── docker-compose.base.yml        # RECOMMENDED: Base configuration
├── docker-compose.dev.yml          # RECOMMENDED: Development overrides
├── docker-compose.staging.yml      # RECOMMENDED: Staging overrides
├── docker-compose.prod.yml         # RECOMMENDED: Production overrides
├── Dockerfile                      # OPTIONAL: Root Dockerfile (backward compat)
├── services/                       # MANDATORY: Service directory
│   └── service-name/
│       └── Dockerfile              # Service-specific Dockerfile
└── deployment/                     # OPTIONAL: Legacy deployment configs
    └── docker/
        └── Dockerfile              # OPTIONAL: Legacy Dockerfile
```

### Docker Compose File Organization

```
docker-compose.yml                  # Main compose (references service Dockerfile)
docker-compose.base.yml             # Base services definition
docker-compose.dev.yml              # Development environment overrides
docker-compose.staging.yml          # Staging environment overrides
docker-compose.prod.yml             # Production environment overrides
```

**Usage Pattern:**

```bash
# Development
docker-compose -f docker-compose.base.yml -f docker-compose.dev.yml up

# Staging
docker-compose -f docker-compose.base.yml -f docker-compose.staging.yml up

# Production
docker-compose -f docker-compose.base.yml -f docker-compose.prod.yml up
```

---

## MANDATORY Dockerfile Requirements

### 1. Multi-Stage Build Structure

**REQUIRED Stages:**

- `builder` - Install dependencies with build tools
- `base` - Minimal runtime with dependencies only
- `development` - Full source with dev dependencies
- `production` - Optimized production image

**Template:**

```dockerfile
# Stage 1: Builder - Install dependencies
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt pyproject.toml ./
RUN pip install --user --no-warn-script-location -r requirements.txt

# Stage 2: Base - Runtime image
FROM python:3.11-slim AS base
ENV PYTHONPATH=/service
WORKDIR /service
COPY --from=builder /root/.local /home/appuser/.local

# Stage 3: Development
FROM base AS development
COPY . .
RUN pip install --user -e ".[dev]"
CMD ["uvicorn", "src.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8500"]

# Stage 4: Production
FROM base AS production
COPY . .
RUN pip install --user -e ".[production]"
CMD ["gunicorn", "src.app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
```

### 2. Layer Caching Optimization

**MANDATORY Order:**

1. Copy dependency files FIRST (`requirements.txt`, `pyproject.toml`)
2. Install dependencies
3. Copy source code LAST

**Why:** Dependency files change rarely, source code changes frequently. This maximizes cache hits.

**Correct Pattern:**

```dockerfile
# ✅ CORRECT: Dependencies first
COPY requirements.txt pyproject.toml ./
RUN pip install -r requirements.txt
COPY . .  # Source code last

# ❌ WRONG: Source code first
COPY . .
RUN pip install -r requirements.txt  # Cache invalidated on every code change
```

### 3. Build vs Runtime Dependencies

**Builder Stage (WITH build tools):**

- gcc, g++, make
- libffi-dev, libssl-dev
- libpq-dev (PostgreSQL development)
- python3-dev

**Runtime Stage (WITHOUT build tools):**

- curl (for health checks)
- postgresql-client (runtime client)
- libpq5 (runtime library)
- NO gcc, g++, make, \*-dev packages

**Pattern:**

```dockerfile
# Builder stage
FROM python:3.11-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ make libffi-dev libssl-dev libpq-dev

# Runtime stage
FROM python:3.11-slim AS base
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl postgresql-client libpq5 \
    && rm -rf /var/lib/apt/lists/*
```

### 4. Production Server Configuration

**MANDATORY:** Use Gunicorn with Uvicorn workers, NOT single-process uvicorn

**Production Command Template:**

```dockerfile
CMD ["gunicorn", "src.app.main:app", \
     "--bind", "0.0.0.0:8500", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--worker-connections", "1000", \
     "--timeout", "120", \
     "--keep-alive", "5", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "--log-level", "info"]
```

**Configuration Parameters:**

- `--workers`: Number of worker processes (default: 4, adjust based on CPU cores)
- `--worker-class`: Must be `uvicorn.workers.UvicornWorker` for ASGI
- `--worker-connections`: Connections per worker (default: 1000)
- `--timeout`: Request timeout in seconds (default: 120)
- `--keep-alive`: Keep-alive timeout (default: 5)
- `--access-logfile`: Access logs (use `-` for stdout)
- `--error-logfile`: Error logs (use `-` for stdout)

**❌ FORBIDDEN in Production:**

- `python src/test_server.py` (test server, not production)
- `uvicorn ... --reload` (development only)
- Single-process uvicorn without workers

### 5. Entry Point Requirements

**MANDATORY:** Use production application entry point

**FastAPI Services (src-layout):**

```dockerfile
# ✅ CORRECT
CMD ["gunicorn", "src.app.main:app", ...]

# ❌ WRONG
CMD ["python", "src/test_server.py"]
```

**FastAPI Services (app/ convention):**

```dockerfile
# ✅ CORRECT
CMD ["gunicorn", "app.main:app", ...]

# ❌ WRONG
CMD ["python", "test_server.py"]
```

**Entry Point Detection:**

1. Check for `src/app/main.py` (src-layout) → Use `src.app.main:app`
2. Check for `app/main.py` (app convention) → Use `app.main:app`
3. Check for `main.py` at root → Use `main:app`
4. NEVER use `test_server.py`, `test_*.py`, or `*_test.py` files

### 6. Security Requirements

**MANDATORY Security Practices:**

1. **Non-Root User:**

```dockerfile
RUN groupadd -g 1000 appuser && \
    useradd -r -u 1000 -g appuser -m -d /home/appuser appuser
USER appuser
```

2. **User Installation:**

```dockerfile
RUN pip install --user --no-warn-script-location ...
ENV PATH="/home/appuser/.local/bin:$PATH"
```

3. **File Permissions:**

```dockerfile
COPY --chown=appuser:appuser . .
RUN chown -R appuser:appuser /service
```

4. **Health Checks:**

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8500/health || exit 1
```

5. **Minimal Base Image:**

- Use `python:3.11-slim` (not `python:3.11`)
- Remove build tools from runtime stage
- Clean apt cache: `&& rm -rf /var/lib/apt/lists/*`

### 7. Environment Variables

**MANDATORY Environment Variables:**

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/service \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH="/home/appuser/.local/bin:$PATH"
```

**PYTHONPATH Rules:**

- For src-layout: `PYTHONPATH=/service` (allows `src.app.main` imports)
- For app convention: `PYTHONPATH=/service` (allows `app.main` imports)
- Must match WORKDIR value

### 8. WORKDIR Configuration

**MANDATORY:** Use `/service` for consistency with DEPLOYMENT-STRUCTURE.md

```dockerfile
WORKDIR /service
```

**Why:** Aligns with DEPLOYMENT-STRUCTURE.md FastAPI example and allows consistent volume mounts.

---

## Docker Compose Configuration Requirements

### 1. Service Dockerfile Reference

**MANDATORY:** All compose files MUST reference service-level Dockerfile

```yaml
services:
  app:
    build:
      context: . # Repository root
      dockerfile: services/main-app/Dockerfile # Service Dockerfile
      target: production # Build target
```

**❌ FORBIDDEN:**

- Building from root Dockerfile without service structure
- Hardcoding Dockerfile paths incorrectly
- Missing `dockerfile:` specification

### 2. Volume Path Alignment

**MANDATORY:** Volume paths MUST match WORKDIR (`/service`)

```yaml
volumes:
  - ./uploads:/service/uploads # ✅ Matches WORKDIR
  - ./storage:/service/storage # ✅ Matches WORKDIR
  - ./logs:/service/logs # ✅ Matches WORKDIR
```

**❌ WRONG:**

```yaml
volumes:
  - ./uploads:/app/uploads # ❌ Mismatch with WORKDIR=/service
```

### 3. Build Target Specification

**MANDATORY:** Specify build target for each environment

```yaml
# Development
build:
  target: development

# Production
build:
  target: production
```

### 4. Health Check Configuration

**MANDATORY:** Include health checks in compose files

```yaml
healthcheck:
  test: ['CMD', 'curl', '-f', 'http://localhost:8500/health']
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

---

## .dockerignore Requirements

### MANDATORY Exclusions

**Create/Update `.dockerignore` at repository root:**

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/

# Virtual environments
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp

# Git
.git/
.gitignore

# Docker (avoid recursion)
Dockerfile*
docker-compose*.yml
.dockerignore

# Documentation
*.md
docs/
LICENSE

# Tests
tests/
test_*.py
*_test.py
.pytest_cache/

# Build artifacts
build/
dist/

# Logs
*.log
logs/

# Data (should be volumes)
data/
*.db

# Environment files
.env
.env.*

# Temporary files
tmp/
temp/
*.tmp
```

---

## Validation Checklist

### Pre-Deployment Validation

**MANDATORY Checks Before Deployment:**

- [ ] **Multi-stage build:** Builder, base, development, production stages present
- [ ] **Layer caching:** Dependencies copied before source code
- [ ] **Build tools separation:** Build tools only in builder stage, not runtime
- [ ] **Production server:** Uses gunicorn with uvicorn workers (not single-process)
- [ ] **Entry point:** Uses production application (`src.app.main:app` or `app.main:app`)
- [ ] **Non-root user:** Runs as `appuser:1000`, not root
- [ ] **Health checks:** HEALTHCHECK directive configured
- [ ] **WORKDIR:** Set to `/service` (matches DEPLOYMENT-STRUCTURE.md)
- [ ] **PYTHONPATH:** Set to `/service` (matches WORKDIR)
- [ ] **Volume paths:** All volumes use `/service` prefix
- [ ] **Compose files:** Reference service Dockerfile correctly
- [ ] **.dockerignore:** Excludes unnecessary files

### Build Validation

```bash
# 1. Build production image
docker build -f services/main-app/Dockerfile --target production -t main-app:prod .

# 2. Check image size (should be <500MB for Python apps)
docker images main-app:prod

# 3. Verify no build tools in runtime
docker run --rm main-app:prod sh -c "which gcc || echo 'No gcc (good)'"

# 4. Verify non-root user
docker run --rm main-app:prod sh -c "whoami"  # Should output: appuser

# 5. Test health check
docker run -d --name test-app -p 8500:8500 main-app:prod
sleep 10
docker exec test-app curl -f http://localhost:8500/health || echo "Health check failed"
docker rm -f test-app
```

### Runtime Validation

```bash
# 1. Verify worker processes
docker run -d --name test-app -p 8500:8500 main-app:prod
docker exec test-app ps aux | grep gunicorn
# Should show: 1 master + 4 workers

# 2. Test application
curl http://localhost:8500/health

# 3. Check logs
docker logs test-app

# 4. Cleanup
docker rm -f test-app
```

---

## Common Mistakes & Anti-Patterns

### ❌ Mistake 1: Wrong Entry Point

```dockerfile
# ❌ WRONG: Test server in production
CMD ["python", "src/test_server.py"]

# ✅ CORRECT: Production application
CMD ["gunicorn", "src.app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
```

### ❌ Mistake 2: Poor Layer Caching

```dockerfile
# ❌ WRONG: Source code first
COPY . .
RUN pip install -r requirements.txt

# ✅ CORRECT: Dependencies first
COPY requirements.txt pyproject.toml ./
RUN pip install -r requirements.txt
COPY . .
```

### ❌ Mistake 3: Build Tools in Runtime

```dockerfile
# ❌ WRONG: Build tools in production
FROM python:3.11-slim
RUN apt-get install -y gcc g++ make  # Build tools in runtime

# ✅ CORRECT: Build tools only in builder
FROM python:3.11-slim AS builder
RUN apt-get install -y gcc g++ make
FROM python:3.11-slim AS production
# No build tools here
```

### ❌ Mistake 4: Single-Process Server

```dockerfile
# ❌ WRONG: Single process
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8500"]

# ✅ CORRECT: Multi-worker
CMD ["gunicorn", "src.app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
```

### ❌ Mistake 5: Root User

```dockerfile
# ❌ WRONG: Running as root
CMD ["gunicorn", ...]

# ✅ CORRECT: Non-root user
USER appuser
CMD ["gunicorn", ...]
```

### ❌ Mistake 6: Volume Path Mismatch

```yaml
# ❌ WRONG: Mismatch with WORKDIR
volumes:
  - ./uploads:/app/uploads  # WORKDIR is /service, not /app

# ✅ CORRECT: Matches WORKDIR
volumes:
  - ./uploads:/service/uploads
```

---

## Framework-Specific Guidelines

### FastAPI Services (src-layout)

**Structure:**

```
services/service-name/
├── Dockerfile
└── [src/ at repository root]
    └── app/
        └── main.py
```

**Dockerfile Pattern:**

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt pyproject.toml ./
RUN pip install --user -r requirements.txt gunicorn

FROM python:3.11-slim AS base
ENV PYTHONPATH=/service
WORKDIR /service
COPY --from=builder /root/.local /home/appuser/.local

FROM base AS production
COPY . .
USER appuser
CMD ["gunicorn", "src.app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
```

### FastAPI Services (app/ convention)

**Structure:**

```
services/service-name/
├── Dockerfile
├── app/
│   └── main.py
└── pyproject.toml
```

**Dockerfile Pattern:**

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt pyproject.toml ./
RUN pip install --user -r requirements.txt gunicorn

FROM python:3.11-slim AS base
ENV PYTHONPATH=/service
WORKDIR /service
COPY --from=builder /root/.local /home/appuser/.local

FROM base AS production
COPY app/ /service/app/
COPY pyproject.toml /service/
RUN pip install --user -e .
USER appuser
CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
```

---

## Alignment with DEPLOYMENT-STRUCTURE.md

### Service Structure Compliance

**MANDATORY:** Follow DEPLOYMENT-STRUCTURE.md service structure:

```
services/service-name/
├── Dockerfile              # ✅ Service-level Dockerfile
├── pyproject.toml          # ✅ Dependencies
├── README.md               # ✅ Service documentation
└── [application code]      # ✅ Framework-specific structure
```

### Docker Compose Alignment

**MANDATORY:** Compose files MUST:

- Reference service Dockerfile: `dockerfile: services/service-name/Dockerfile`
- Use correct build context: `context: .` (repository root)
- Match volume paths with WORKDIR: `/service/*`
- Specify build targets: `target: production|development`

---

## LLM Instruction Protocol

### When Creating/Updating Dockerfiles

1. **Check Structure:**
   - Verify service exists in `services/service-name/`
   - Confirm Dockerfile location: `services/service-name/Dockerfile`
   - Check for `.dockerignore` at repository root

2. **Apply Multi-Stage Pattern:**
   - Create builder stage with build tools
   - Create base stage with runtime dependencies
   - Create development stage with dev dependencies
   - Create production stage optimized for production

3. **Optimize Layer Caching:**
   - Copy dependency files FIRST
   - Install dependencies
   - Copy source code LAST

4. **Configure Production Server:**
   - Use gunicorn with uvicorn workers
   - Set appropriate worker count (default: 4)
   - Configure timeouts and connection limits

5. **Apply Security:**
   - Create non-root user (`appuser:1000`)
   - Use `--user` flag for pip installs
   - Set proper file permissions
   - Add health checks

6. **Validate:**
   - Run validation checklist
   - Test build
   - Verify image size
   - Check worker processes

### When Creating/Updating Docker Compose Files

1. **Reference Service Dockerfile:**
   - Use `dockerfile: services/service-name/Dockerfile`
   - Set `context: .` (repository root)

2. **Align Volume Paths:**
   - Use `/service/*` prefix (matches WORKDIR)
   - Never use `/app/*` unless WORKDIR is `/app`

3. **Specify Build Targets:**
   - Development: `target: development`
   - Production: `target: production`

4. **Add Health Checks:**
   - Include healthcheck configuration
   - Use `/health` endpoint

---

## References

- **DEPLOYMENT-STRUCTURE.md:** `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md`
- **Docker Best Practices:** https://docs.docker.com/develop/dev-best-practices/
- **Gunicorn Configuration:** https://docs.gunicorn.org/en/stable/settings.html
- **Uvicorn Workers:** https://www.uvicorn.org/deployment/

---

## Version History

- **v3.0.0** (2025-01-11): Converted to protocol/instruction guide for LLMs
- **v2.0.0** (2025-01-11): Added Docker best practices analysis
- **v1.0.0** (2025-01-11): Initial alignment with DEPLOYMENT-STRUCTURE.md

---

**ENFORCEMENT:** This protocol is MANDATORY. All Docker configurations MUST follow these requirements. Deviations require explicit approval and documentation.
