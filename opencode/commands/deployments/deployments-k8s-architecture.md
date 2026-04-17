# === Universal Kubernetes Architecture Design: Enterprise-Grade Architecture & Patterns Protocol ===

**ALWAYS THINK THEN...** Before executing any action, operation, or command in this instruction set, you MUST use thinking to:

1. Analyze the request and understand what needs to be done
2. Plan your approach and identify potential issues
3. Consider the implications and requirements
4. Only then proceed with the actual execution

**This thinking requirement is MANDATORY and must be followed for every action.**

## CANONICAL PROTOCOL ENFORCEMENT - READ FIRST

**THIS SECTION IS MANDATORY AND MUST BE READ, INDEXED, AND FOLLOWED BEFORE ANY COMMAND EXECUTION**

**BEFORE PROCEEDING, YOU MUST ALWAYS:**

1. **READ AND EXECUTE**: `.claude/commands/ai-agent-compliance-prompt.md`
2. **READ AND COMPLY**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md`
3. **VERIFY**: User has given explicit permission to proceed
4. **ACKNOWLEDGE**: ALL CANONICAL PROTOCOL requirements

**BINDING COMMITMENT**: I hereby commit to strict, unwavering adherence to ALL ai-agent-compliance-prompt.md requirements and DEPLOYMENT-STRUCTURE.md compliance, and will halt operations immediately upon any protocol violation to perform mandatory root cause analysis and corrective action.

**FORBIDDEN**: Proceeding without complete protocol compliance verification and mandatory structure adherence

## KISS PRINCIPLES MANDATE

**KISS (KEEP IT SIMPLE, STUPID) PRINCIPLES ARE MANDATORY:**

- Design simple, straightforward architectures over complex ones
- Use standard Kubernetes resources over custom resources
- Create clear, readable architecture diagrams and documentation
- Implement proven patterns and established practices
- Design for maintainability and operational simplicity
- Avoid over-engineering unless absolutely necessary
- Choose clarity over cleverness in all architectural decisions
- Use well-established industry patterns and practices

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Creating overly complex architectures
- Using non-standard or experimental patterns without justification
- Designing without security-first approach
- Ignoring universal platform compatibility
- Creating incomplete architecture documentation
- Designing without operational considerations
- Deviating from mandatory structure
- Over-engineering simple solutions

**ABSOLUTELY FORBIDDEN - NO EXCEPTIONS:**

- **NO EXPERIMENTAL FEATURES** - use production-ready, stable patterns only
- **NO SHORTCUTS** - design comprehensive architectures ALWAYS
- **NO INCOMPLETE DESIGNS** - create complete, production-ready architectures
- **NO PLATFORM LOCK-IN** - design for universal platform compatibility
- **NO SECURITY AFTERTHOUGHTS** - implement security-first design
- **NO HARDCODED CONFIGURATIONS** - use parameterized, environment-agnostic designs
- **NO MONOLITHIC THINKING** - design for microservices and modularity
- **NO DOCUMENTATION GAPS** - comprehensive documentation MANDATORY
- **NO STRUCTURE DEVIATIONS** - follow mandatory structure exactly
- **NO OVER-ENGINEERING** - use KISS principles always

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MANDATORY STRUCTURE DOCUMENT:**

   - Read `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` thoroughly
   - Understand every directory and file requirement for architecture compliance
   - Follow the structure exactly without deviations in all designs

2. **READ DEPLOYMENT TEMPLATES:**

   - Study `K8S-DEPLOYMENT-TEMPLATES.md` for proven patterns
   - Understand microservices, web application, and database patterns
   - Apply template patterns consistently across architectures

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest Kubernetes architecture patterns
   - Find CNCF landscape and graduated project patterns
   - Search for production-grade microservices architectures
   - Review service mesh patterns (Istio, Linkerd, Consul)
   - Study ingress controller best practices
   - Check cloud-native security patterns

**SEARCH PRIORITIES:**

- CNCF graduated project documentation and patterns
- Kubernetes official documentation (latest version)
- Cloud provider reference architectures (AWS, Azure, GCP)
- Service mesh official documentation and patterns
- Production-grade open source project architectures
- Industry case studies and success patterns

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to KISS principles and the mandatory directory structure.

### **ARCHITECTURE-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR COMPREHENSIVE ARCHITECTURE DESIGN ONLY:**

- **MUST:** Create comprehensive Kubernetes deployment architectures and documentation
- **MUST:** Design universal platform compatibility across all supported platforms
- **MUST:** Follow DEPLOYMENT-STRUCTURE.md exactly in all architectural designs
- **MUST:** Design microservices architectures with industry best practices
- **MUST:** Include security-first approach with comprehensive policy design
- **MUST:** Design ingress controller integration with unique URI patterns
- **MUST:** Plan service mesh integration and communication patterns
- **MUST:** Design comprehensive observability stack architecture
- **MUST:** Include CI/CD and GitOps integration patterns
- **MUST:** Plan scalability, performance, and disaster recovery
- **FORBIDDEN:** Execute ANY actual deployment commands
- **FORBIDDEN:** Make ANY changes to live systems
- **FORBIDDEN:** Deploy ANY code or infrastructure
- **FORBIDDEN:** Deviate from mandatory directory structure
- **FORBIDDEN:** Create partial or incomplete architectures
- **MUST:** Output architecture documentation in markdown documents with timestamps

**UNIVERSAL KUBERNETES ARCHITECTURE FOCUS:**

- Repository analysis and component discovery
- Universal platform deployment architecture (local K8s, AWS EKS, Azure AKS, GCP GKE, on-premises)
- Ingress controller deployment and unique URI endpoint patterns
- Microservices architecture with service mesh integration (Istio, Linkerd, Consul)
- Security-first architecture with Pod Security Standards and network policies
- Comprehensive observability stack (Prometheus, Grafana, Jaeger, ELK/EFK)
- GitOps workflows with ArgoCD/Flux integration patterns
- CI/CD pipeline integration with security scanning
- Scalability architecture with HPA, VPA, and cluster autoscaling
- Disaster recovery and business continuity planning
- KISS principles adherence throughout all architectural designs

### **MANDATORY REPOSITORY STRUCTURE REFERENCE:**

**BEFORE EXECUTING**, you MUST read and understand the canonical repository structure:

1. **READ**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` for complete Kubernetes deployment structure
2. **UNDERSTAND**: NO root wrapper directories (no k8s/, deployments/, kubernetes/ wrapper)
3. **USE**: apps/, infrastructure/, services/, clusters/, gitops/, helm-charts/, ci/, scripts/, docs/, tests/, .templates/
4. **VALIDATE**: Reference VALIDATION-CHECKLIST.md for compliance requirements

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-k8s-architecture-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for target_repository, repository_type, deployment_scope, target_platforms
3. **FOLLOW PROTOCOL**: Execute all phases according to the architecture design protocol specifications
4. **VERIFY COMPLIANCE**: Ensure strict adherence to DEPLOYMENT-STRUCTURE.md
5. **VALIDATE COMPLETION**: Ensure all architectural objectives and outcomes have been met
6. **DOCUMENT RESULTS**: Create comprehensive architecture documentation with proper timestamps

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "universal-k8s-architecture-design-prompt"
arguments:
  target_repository: "[repository name or identifier]"
  repository_type: "[microservice|monolith|multi-service|data-pipeline|web-application|api-service|batch-processing|event-driven|ml-pipeline]"
  deployment_scope: "[single-service|service-mesh|platform|ecosystem|enterprise]"
  target_platforms:
    [
      "[k8s|docker-desktop|minikube|kind|k3s|aws-eks|azure-aks|gcp-gke|on-premises|openshift|tanzu|rancher]",
    ]
  environment_matrix:
    [
      "[development|testing|staging|pre-production|production|disaster-recovery]",
    ]
  compliance_level: "[optional: basic|enterprise|regulated-industry|government|financial-services]"
  architecture_complexity: "[optional: simple|standard|complex|enterprise]"
  ingress_requirements: "[optional: basic-ingress|advanced-routing|service-mesh|api-gateway|multi-tenant]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All architecture phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive Kubernetes architecture design completed
- [ ] STRICT compliance with DEPLOYMENT-STRUCTURE.md verified in all designs
- [ ] Complete repository analysis and component inventory (timestamped)
- [ ] Universal platform compatibility architecture designed across all specified platforms
- [ ] Ingress controller architecture with unique URI endpoints designed (timestamped)
- [ ] Microservices architecture with service mesh integration designed (timestamped)
- [ ] Security-first architecture with Pod Security Standards implemented (timestamped)
- [ ] Comprehensive observability stack architecture designed (timestamped)
- [ ] CI/CD and GitOps integration architecture completed (timestamped)
- [ ] Scalability and performance architecture designed (timestamped)
- [ ] Disaster recovery and business continuity architecture planned (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps
- [ ] Implementation roadmap created with clear next steps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL ARCHITECTURE OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All architecture deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All repository analysis documentation includes precise timestamps
- [ ] All platform compatibility architecture includes timestamp documentation
- [ ] All ingress controller designs include proper date stamps
- [ ] All microservices architecture follows consistent date stamp format
- [ ] All security architecture documentation includes timestamps
- [ ] All observability stack designs include proper date stamps
- [ ] All CI/CD integration architecture includes timestamp documentation
- [ ] All scalability planning includes proper date stamps
- [ ] All disaster recovery architecture includes timestamp tracking
- [ ] All implementation roadmaps include proper date stamps
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating architecture files without proper reverse date stamps
- Using inconsistent date formats within same architecture session
- Missing timestamps in architecture documentation
- Deviating from mandatory directory structure in designs

### **MANDATORY STRUCTURE COMPLIANCE IN ARCHITECTURE DESIGN:**

**DIRECTORY STRUCTURE ARCHITECTURE REQUIREMENTS:**

All architecture designs MUST incorporate and validate the exact structure defined in `DEPLOYMENT-STRUCTURE.md`:

```
repository-name/                       # Repository root (NO WRAPPER)
 apps/                                # K8S APPLICATION MANIFESTS
    base/                            #  MUST design base manifest patterns
       {service-name}/
          kustomization.yaml
          deployment.yaml
          service.yaml
          configmap.yaml
          ingress.yaml
    overlays/                        #  MUST design environment-specific patterns
       development/
       staging/
       production/
    configs/                         #  MUST design configuration management
    secrets/                         #  MUST design secret management patterns
    policies/                        #  MUST design security policy patterns
    tests/                           #  MUST design validation test patterns
    monitoring/                      #  MUST design observability patterns
 infrastructure/                      # K8S PLATFORM COMPONENTS
    controllers/                     #  MUST design ingress controllers, operators
    storage/                         #  MUST design storage class patterns
    monitoring/                      #  MUST design observability stack
    security/                        #  MUST design security policies
    service-mesh/                    #  MUST design service mesh patterns
 clusters/                            # ENVIRONMENT CONFIGS
 gitops/                              # GITOPS CONFIGURATIONS
 helm-charts/                         # CUSTOM HELM CHARTS
 ci/                                  # CI/CD PIPELINES
 scripts/                             # PRODUCTION AUTOMATION
 docs/                                # OFFICIAL DOCUMENTATION
 tests/                               # INTEGRATION TESTS
```

### **ARCHITECTURE DESIGN PATTERNS:**

**REPOSITORY ANALYSIS PATTERNS:**

The architecture design MUST include comprehensive repository analysis:

```yaml
# Repository Component Analysis Pattern
components:
  services:
    - name: "user-service"
      type: "microservice"
      dependencies: ["database", "redis", "auth-service"]
      ports: [8080, 9090]
      protocols: ["http", "grpc"]
    - name: "auth-service"
      type: "microservice"
      dependencies: ["database", "external-oauth"]
      ports: [8081, 9091]
      protocols: ["http"]

  databases:
    - name: "user-database"
      type: "postgresql"
      version: "14"
      persistence: true
    - name: "session-cache"
      type: "redis"
      version: "7"
      persistence: false

  external_dependencies:
    - name: "oauth-provider"
      type: "external-api"
      endpoint: "https://auth.provider.com"
    - name: "payment-gateway"
      type: "external-api"
      endpoint: "https://payments.stripe.com"
```

**UNIVERSAL PLATFORM ARCHITECTURE PATTERNS:**

```yaml
# Universal Platform Compatibility Pattern
platforms:
  local_development:
    ingress_controller: "nginx-ingress"
    storage_class: "local-path"
    load_balancer: "nodeport"
    dns: "local-dns"

  aws_eks:
    ingress_controller: "aws-load-balancer-controller"
    storage_class: "gp3-csi"
    load_balancer: "nlb"
    dns: "external-dns"
    authentication: "irsa"

  azure_aks:
    ingress_controller: "application-gateway"
    storage_class: "azure-disk-csi"
    load_balancer: "azure-lb"
    dns: "azure-dns"
    authentication: "workload-identity"

  gcp_gke:
    ingress_controller: "gce-ingress"
    storage_class: "gce-pd-csi"
    load_balancer: "gcp-lb"
    dns: "cloud-dns"
    authentication: "workload-identity"
```

**INGRESS CONTROLLER ARCHITECTURE PATTERNS:**

```yaml
# Comprehensive Ingress Architecture Pattern
ingress_architecture:
  controller:
    name: "nginx-ingress-controller"
    replicas: 3
    high_availability: true
    ssl_termination: true

  routing_patterns:
    api_services:
      - path: "/api/v1/users"
        service: "user-service"
        port: 8080
      - path: "/api/v1/auth"
        service: "auth-service"
        port: 8081

    web_applications:
      - path: "/web"
        service: "frontend-service"
        port: 3000
      - path: "/admin"
        service: "admin-dashboard"
        port: 4000

  ssl_configuration:
    cert_manager: true
    letsencrypt: true
    auto_renewal: true
    tls_version: "1.2+"

  advanced_features:
    rate_limiting: true
    ddos_protection: true
    header_routing: true
    canary_deployments: true
```

### **ARCHITECTURE DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/deployments/deployments/Deployment_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment architecture, strategy, and SOLID compliance review
2. **`./project/docs/deployments/deployments/Rollback_Strategy_{YYYYMMDD-HHMMSS}.ipynb`** - Rollback Strategy
3. **`./project/docs/deployments/deployments/Infrastructure_Requirements_{YYYYMMDD-HHMMSS}.ipynb`** - Infrastructure Requirements

**MANDATORY MARKDOWN DELIVERABLES:**

11. **`Implementation_Roadmap-YYYY-MM-DD-HHMMSS.md`** - Step-by-step implementation guide with phases
12. **`Architectural_Decision_Records-YYYY-MM-DD-HHMMSS.md`** - ADR documentation with rationale
13. **`Quickstart_Deployment_Guide-YYYY-MM-DD-HHMMSS.md`** - User-friendly deployment commands for all environments and platforms
14. **`Lifecycle_Management_Guide-YYYY-MM-DD-HHMMSS.md`** - Application lifecycle management procedures and workflows
15. **`Terraform_Infrastructure_Guide-YYYY-MM-DD-HHMMSS.md`** - Infrastructure as Code patterns and Terraform configurations

### **ARCHITECTURE DESIGN METHODOLOGIES:**

**REPOSITORY ANALYSIS METHODOLOGY:**

1. **Component Discovery**: Identify all services, databases, and external dependencies
2. **Dependency Mapping**: Map service-to-service and service-to-external dependencies
3. **Communication Analysis**: Analyze protocols, ports, and integration patterns
4. **Data Flow Analysis**: Map data flows and storage requirements
5. **Interface Documentation**: Document API contracts and service interfaces

**UNIVERSAL PLATFORM DESIGN METHODOLOGY:**

1. **Platform Assessment**: Analyze capabilities and constraints of each target platform
2. **Common Patterns**: Design patterns that work across all platforms
3. **Platform Optimizations**: Plan platform-specific optimizations without breaking universality
4. **Compatibility Validation**: Ensure consistent behavior across all platforms
5. **Resource Planning**: Design resource allocation strategies for each platform

**MICROSERVICES ARCHITECTURE METHODOLOGY:**

1. **Service Boundary Definition**: Define clear service boundaries and responsibilities
2. **Communication Patterns**: Design synchronous and asynchronous communication
3. **Data Management**: Plan data ownership and consistency patterns
4. **Service Mesh Integration**: Design traffic management and security policies
5. **Resilience Patterns**: Implement circuit breakers, retries, and timeout strategies

### **SECURITY-FIRST ARCHITECTURE REQUIREMENTS:**

**POD SECURITY ARCHITECTURE:**

```yaml
# Security-First Architecture Pattern
pod_security_standards:
  profile: "restricted"
  security_context:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    seccompProfile:
      type: "RuntimeDefault"

  container_security_context:
    allowPrivilegeEscalation: false
    readOnlyRootFilesystem: true
    runAsNonRoot: true
    capabilities:
      drop: ["ALL"]

  network_policies:
    default_deny: true
    explicit_allow: true
    microsegmentation: true
    dns_restrictions: true
```

**COMPREHENSIVE OBSERVABILITY ARCHITECTURE:**

```yaml
# Observability Stack Architecture Pattern
observability_stack:
  metrics:
    prometheus:
      deployment: "prometheus-operator"
      retention: "30d"
      storage: "100Gi"
    grafana:
      deployment: "grafana-helm"
      dashboards: "automated"
      alerting: "integrated"

  logging:
    aggregation: "elk-stack"
    retention:
      hot: "7d"
      warm: "30d"
      cold: "365d"
    structured_format: "json"
    correlation_ids: true

  tracing:
    system: "jaeger"
    sampling_rate: "0.1"
    retention: "7d"
    storage: "elasticsearch"

  alerting:
    prometheus_rules: true
    escalation_policies: true
    notification_channels: ["slack", "email", "pagerduty"]
```

### **NEXT PHASE PREPARATION:**

```bash
# After architecture approval, proceed with planning phase:
/deployments-planning [application-name] [architecture-type] [platforms] [environments]

# Then execute implementation:
/deployments-implement [application] [environment] [platform] [options]

# Examples:
/deployments-k8s-architecture my-platform multi-service service-mesh aws-eks,azure-aks,k8s development,staging,production
/deployments-planning user-service microservice aws-eks,azure-aks development,staging,production
/deployments-implement user-service development k8s --deployment-strategy=rolling
```

### **ARCHITECTURE VALIDATION COMMANDS:**

**Architecture Design Validation:**

```bash
# Validate architecture designs against KISS principles
conftest verify --policy kiss-principles/ architecture-designs/

# Validate universal platform compatibility
conftest verify --policy platform-compatibility/ platform-designs/

# Validate security-first architecture
conftest verify --policy security-architecture/ security-designs/

# Validate mandatory structure compliance
conftest verify --policy structure-compliance/ architecture-patterns/
```

**Architecture Documentation Validation:**

```bash
# Validate architecture documentation completeness
find architecture-docs/ -name "*.ipynb" -exec jupyter nbconvert --execute {} \;

# Validate implementation roadmap accuracy
conftest verify --policy roadmap-validation/ Implementation_Roadmap-*.md

# Validate architectural decision records
conftest verify --policy adr-validation/ Architectural_Decision_Records-*.md
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE ARCHITECTURE DESIGN ONLY through the MCP prompt protocol with STRICT adherence to KISS principles and DEPLOYMENT-STRUCTURE.md. The comprehensive architecture logic is defined in `deployments-k8s-architecture-prompt.yaml` and executed according to Model Context Protocol standards. No actual deployment actions are taken. All architecture designs must follow the mandatory directory structure exactly and incorporate universal platform compatibility. Use `/deployments-planning` for detailed planning after architecture approval, then `/deployments-implement` for actual deployment execution. Focus on creating production-ready, universally deployable Kubernetes architectures with comprehensive documentation and proper timestamp tracking.
