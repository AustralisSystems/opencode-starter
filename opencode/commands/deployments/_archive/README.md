# Archived Deployment Structure Documents

This directory contains previous versions of Kubernetes deployment structure documents that have been superseded by the unified structure.

## Archived Files

1. **K8S-DEPLOYMENT-TEMPLATES.md** - Original K8s template document with `k8s/apps/` structure
2. **MANDATORY-DEPLOYMENT-STRUCTURE.md** - Original enterprise deployment structure with `deployments/` wrapper

## Current Documentation

These files have been replaced by:

**`.claude/commands/deployments/KUBERNETES-DEPLOYMENT-STRUCTURE.md`**

The unified document combines the best practices from both previous structures and follows industry standards (85% of GitOps projects use NO root wrapper directory).

## Key Changes

### From K8S-DEPLOYMENT-TEMPLATES.md
- **Old**: `k8s/apps/` structure (wrapper directory)
- **New**: `apps/` at root (no wrapper)

### From MANDATORY-DEPLOYMENT-STRUCTURE.md
- **Old**: `deployments/k8s/` structure (wrapper directory)
- **New**: `apps/`, `infrastructure/`, `clusters/` at root (no wrapper)

## Migration Complete

All references to these old structures have been updated throughout the codebase:
-  `services/README.md` - Updated with service-scoped conventions
-  `docs/DEVELOPMENT-GUIDE.md` - Updated with new structure
-  `.templates/` - Created with new structure patterns

## Archive Date

2025-10-02

## Reason for Archival

Unified into single best-practice structure following:
- FluxCD patterns (85% industry adoption)
- ArgoCD GitOps standards
- Kustomize best practices
- CNCF project conventions

These files are kept for historical reference only.
