# === Universal Kubernetes Deployment Planning: Enterprise-Grade Strategy & Architecture Protocol ===

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

## FORBIDDEN PRACTICES

**FORBIDDEN PRACTICES:**

- Making large, non-atomic changes
- Skipping tests or validation
- Ignoring build/deploy errors
- Proceeding without understanding
- Creating duplicate functionality
- Using outdated patterns
- Deviating from mandatory structure

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
- **NO STRUCTURE DEVIATIONS** - follow mandatory structure exactly

## RTFM (READ THE FUCKING MANUAL) - MANDATORY

**YOU MUST ALWAYS:**

1. **READ MANDATORY STRUCTURE DOCUMENT:**

   - Read `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` thoroughly
   - Understand every directory and file requirement
   - Follow the structure exactly without deviations

2. **READ PROJECT DOCUMENTATION:**

   - Check `./docs` directory thoroughly
   - Check `./project/docs` if it exists
   - Read ALL README files
   - Review architecture documentation
   - Study API documentation

3. **SEARCH ONLINE FOR BEST PRACTICES:**
   - Use web search for latest Kubernetes documentation
   - Find official platform documentation (AWS EKS, Azure AKS, GCP GKE)
   - Search GitHub for enterprise deployment examples
   - Review CNCF landscape and best practices
   - Study production deployment patterns
   - Check Kubernetes security best practices

**SEARCH PRIORITIES:**

- Official Kubernetes documentation (latest version)
- Cloud provider official documentation
- CNCF graduated project documentation
- Enterprise GitHub repositories with high stars
- Industry standard deployment patterns
- Recent security and compliance guidelines

---

## **MCP PROMPT EXECUTION INSTRUCTIONS**

**MANDATORY PROTOCOL COMPLIANCE**: This is an MCP-compliant prompt that must be executed according to Model Context Protocol standards with strict adherence to the mandatory directory structure.

### **PLANNING-ONLY MANDATE - CRITICAL DISTINCTION**

**THIS COMMAND IS FOR COMPREHENSIVE PLANNING AND ARCHITECTURE DESIGN ONLY:**

- **MUST:** Create comprehensive deployment plans and architecture documentation
- **MUST:** Follow DEPLOYMENT-STRUCTURE.md exactly
- **MUST:** Design universal Kubernetes deployment strategies
- **MUST:** Plan for microservices architectures with industry best practices
- **MUST:** Include security-first approach with Pod Security Standards
- **MUST:** Design CI/CD pipeline integration with GitOps patterns
- **MUST:** Plan comprehensive monitoring and observability stack
- **MUST:** Include scalability and performance optimization strategies
- **MUST:** Design disaster recovery and business continuity plans
- **MUST:** Analyze cost optimization and resource efficiency
- **FORBIDDEN:** Execute ANY actual deployment commands
- **FORBIDDEN:** Make ANY changes to live systems
- **FORBIDDEN:** Deploy ANY code or infrastructure
- **FORBIDDEN:** Deviate from mandatory directory structure
- **MUST:** Output planning documentation in markdown documents with timestamps

**UNIVERSAL KUBERNETES DEPLOYMENT FOCUS:**

- Universal platform compatibility (local K8s, AWS EKS, Azure AKS, GCP GKE, on-premises)
- Microservices architecture patterns with service mesh integration
- Security-first approach with Pod Security Standards (Restricted profile)
- GitOps workflows with ArgoCD/Flux integration
- Comprehensive CI/CD pipeline architecture
- Enterprise-grade monitoring and observability stack
- Scalability and performance optimization strategies
- Disaster recovery and business continuity planning
- Cost optimization and resource efficiency analysis
- KISS principles adherence throughout all planning

### **MANDATORY REPOSITORY STRUCTURE REFERENCE:**

**BEFORE EXECUTING**, you MUST read and understand the canonical repository structure:

1. **READ**: `.claude/commands/deployments/DEPLOYMENT-STRUCTURE.md` for complete Kubernetes deployment structure
2. **UNDERSTAND**: NO root wrapper directories (no k8s/, deployments/, kubernetes/ wrapper)
3. **USE**: apps/, infrastructure/, services/, clusters/, gitops/, helm-charts/, ci/, scripts/, docs/, tests/, .templates/
4. **VALIDATE**: Reference VALIDATION-CHECKLIST.md for compliance requirements

### **EXECUTION SEQUENCE:**

1. **LOAD MCP PROMPT**: Execute the MCP prompt defined in `deployments-planning-prompt.yaml`
2. **PROVIDE ARGUMENTS**: Supply required arguments for target_application, architecture_type, target_platforms, environments
3. **FOLLOW PROTOCOL**: Execute all phases according to the universal deployment planning protocol specifications
4. **VERIFY COMPLIANCE**: Ensure strict adherence to DEPLOYMENT-STRUCTURE.md
5. **DOCUMENT RESULTS**: Create comprehensive planning documentation with proper timestamps
6. **VALIDATE COMPLETION**: Confirm 100% planning completeness achieved

### **MCP PROMPT INVOCATION:**

```yaml
# Use this MCP prompt with required arguments:
prompt_name: "universal-k8s-deployment-planning-prompt"
arguments:
  target_application: "[application or microservice name]"
  architecture_type: "[microservice|web-application|api-service|database|worker-service|monolithic|event-driven|data-pipeline]"
  target_platforms:
    [
      "[k8s|docker-desktop|minikube|kind|aws-eks|azure-aks|gcp-gke|on-premises|multi-cloud|edge-computing]",
    ]
  environments:
    [
      "[development|testing|staging|pre-production|production|disaster-recovery]",
    ]
  compliance_requirements: "[optional: SOC2|ISO27001|GDPR|HIPAA|PCI-DSS|FedRAMP|NIST|CIS-Benchmarks]"
  scalability_requirements: "[optional: low-traffic|medium-traffic|high-traffic|enterprise-scale|global-scale|event-driven-scale]"
  security_level: "[optional: standard|high-security|zero-trust|government|financial-services]"
```

### **SUCCESS CRITERIA:**

- [ ] MCP prompt executed with proper arguments and date stamps
- [ ] All planning phases completed according to protocol with timestamp tracking
- [ ] 100% comprehensive universal deployment planning completed
- [ ] STRICT compliance with DEPLOYMENT-STRUCTURE.md verified
- [ ] Universal platform compatibility analysis completed (timestamped)
- [ ] Microservices architecture design completed with service mesh integration
- [ ] Security-first approach implemented with Pod Security Standards (timestamped)
- [ ] CI/CD pipeline architecture designed with GitOps integration (timestamped)
- [ ] Comprehensive monitoring and observability stack designed (timestamped)
- [ ] Scalability and performance optimization strategies planned (timestamped)
- [ ] Disaster recovery and business continuity plans created (timestamped)
- [ ] Cost optimization and resource efficiency analysis completed (timestamped)
- [ ] All deliverables produced as specified in YAML protocol with proper timestamps
- [ ] Implementation roadmap created with clear next steps

### **MANDATORY DATE STAMP REQUIREMENTS:**

**ALL DEPLOYMENT PLANNING OUTPUT FILES MUST USE REVERSE DATE STAMP FORMAT: YYYY-MM-DD-HHMMSS**

- [ ] All planning deliverables (.ipynb) have reverse date stamps in filenames
- [ ] All architecture analysis documentation includes precise timestamps
- [ ] All platform compatibility documentation includes timestamp documentation
- [ ] All security planning includes proper date stamps
- [ ] All CI/CD architecture follows consistent date stamp format
- [ ] All monitoring design documentation includes timestamps
- [ ] All scalability planning includes proper date stamps
- [ ] All disaster recovery plans include timestamp documentation
- [ ] All cost optimization analysis includes proper date stamps
- [ ] All implementation roadmaps include timestamp tracking
- [ ] UTC time used for all timestamp operations

**FORBIDDEN:**

- Creating planning files without proper reverse date stamps
- Using inconsistent date formats within same planning session
- Missing timestamps in planning documentation
- Deviating from mandatory directory structure

### **MANDATORY STRUCTURE COMPLIANCE:**

**DIRECTORY STRUCTURE REQUIREMENTS:**

The planning MUST create documentation that follows the exact structure defined in `DEPLOYMENT-STRUCTURE.md`:

```
repository-name/                       # Repository root (NO WRAPPER)
 apps/                                # K8S APPLICATION MANIFESTS
    base/
       {service-name}/
    overlays/
       development/
       staging/
       production/
    configs/
    secrets/
    policies/
    tests/
    monitoring/
 infrastructure/                      # K8S PLATFORM COMPONENTS
 clusters/                            # ENVIRONMENT CONFIGS
 gitops/                              # GITOPS CONFIGURATIONS
 helm-charts/                         # CUSTOM HELM CHARTS
 ci/                                  # CI/CD PIPELINES
 scripts/                             # PRODUCTION AUTOMATION
 docs/                                # OFFICIAL DOCUMENTATION
 tests/                               # INTEGRATION TESTS
```

**COMPLIANCE VERIFICATION:**

- [ ] Application directory structure planned according to mandatory requirements
- [ ] Base Kustomize configurations planned for all required components
- [ ] Environment overlays planned for development, staging, and production
- [ ] Security policies planned including network policies and Pod Security Standards
- [ ] Monitoring configurations planned including ServiceMonitor and PrometheusRule
- [ ] Platform-specific configurations planned for all target platforms
- [ ] GitOps configurations planned for chosen GitOps tool
- [ ] CI/CD pipeline configurations planned for chosen platform
- [ ] Documentation structure planned according to mandatory requirements

### **PLANNING DELIVERABLES WITH REVERSE DATE STAMPS:**

**MANDATORY MARKDOWN DOCUMENT DELIVERABLES:**

1. **`./project/docs/planning/deployments-planning/Implementation_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Complete implementation details with all components and modules
2. **`./project/docs/planning/deployments-planning/Testing_Strategy_{YYYYMMDD-HHMMSS}.ipynb`** - Test execution results, coverage analysis, and validation
3. **`./project/docs/planning/deployments-planning/Integration_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Integration patterns, dependencies, and implementation
4. **`./project/docs/planning/deployments-planning/Deployment_Plan_{YYYYMMDD-HHMMSS}.ipynb`** - Deployment architecture, strategy, and SOLID compliance review

**MANDATORY MARKDOWN DELIVERABLES:**

11. **`Directory_Structure_Implementation-YYYY-MM-DD-HHMMSS.md`** - Mandatory structure compliance documentation
12. **`Implementation_Roadmap-YYYY-MM-DD-HHMMSS.md`** - Step-by-step implementation guide with phases
13. **`Quickstart_Deployment_Guide-YYYY-MM-DD-HHMMSS.md`** - User-friendly deployment commands for all environments and platforms
14. **`Lifecycle_Management_Guide-YYYY-MM-DD-HHMMSS.md`** - Application lifecycle management procedures and workflows
15. **`Terraform_Infrastructure_Guide-YYYY-MM-DD-HHMMSS.md`** - Infrastructure as Code patterns and Terraform configurations

### **UNIVERSAL PLATFORM SUPPORT:**

**PLATFORM COMPATIBILITY REQUIREMENTS:**

The planning MUST address compatibility and optimization for ALL specified target platforms:

**Local Development Platforms:**

- Docker Desktop with Kubernetes
- Minikube
- Kind (Kubernetes in Docker)
- K3s/K3d
- Local K8s clusters

**Cloud Provider Platforms:**

- AWS EKS with AWS Load Balancer Controller, EBS/EFS CSI
- Azure AKS with Application Gateway, Azure Disk/File CSI
- GCP GKE with GCP Load Balancer, Compute/Filestore CSI

**On-Premises Platforms:**

- Enterprise Kubernetes clusters with MetalLB
- OpenShift environments
- VMware Tanzu environments
- Bare metal Kubernetes clusters

### **MICROSERVICES ARCHITECTURE REQUIREMENTS:**

**SERVICE MESH INTEGRATION:**

- Istio service mesh patterns and configurations
- Linkerd integration for lightweight service mesh
- Consul Connect patterns for service discovery
- Traffic management and routing strategies
- Security policies and mTLS configurations

**COMMUNICATION PATTERNS:**

- Synchronous communication (REST, GraphQL, gRPC)
- Asynchronous communication (message queues, events)
- Circuit breaker and retry patterns
- API gateway integration patterns

**DATA MANAGEMENT PATTERNS:**

- Database per service patterns
- Event sourcing and CQRS patterns
- Distributed transaction management
- Data synchronization strategies

### **SECURITY-FIRST APPROACH:**

**POD SECURITY STANDARDS:**

- Restricted Pod Security Standard implementation
- Security contexts for all containers
- Capability dropping and privilege restrictions
- Read-only root filesystem configurations

**NETWORK SECURITY:**

- Network policies for microsegmentation
- Default-deny network policies
- Service mesh security policies
- Ingress and egress traffic control

**SECRET MANAGEMENT:**

- External Secrets Operator integration
- Secret rotation strategies
- Least privilege secret access
- Secret scanning and validation

**COMPLIANCE INTEGRATION:**

- RBAC implementation with least privilege
- OPA Gatekeeper policy enforcement
- Admission controller configurations
- Audit logging and monitoring

### **NEXT PHASE PREPARATION:**

```bash
# After planning approval, execute deployment with:
/deployments-implement [application] [environment] [platform] [additional-options]

# Examples:
/deployments-implement my-microservice development k8s
/deployments-implement api-gateway staging aws-eks --region=us-east-1
/deployments-implement user-service production multi-cloud --ha-enabled
```

---

**ENFORCEMENT:** This command performs COMPREHENSIVE PLANNING ONLY through the MCP prompt protocol with STRICT adherence to DEPLOYMENT-STRUCTURE.md. The comprehensive planning logic is defined in `deployments-planning-prompt.yaml` and executed according to Model Context Protocol standards. No actual deployment actions are taken. All planning must follow the mandatory directory structure exactly. Use `/deployments-implement` for actual deployment execution after planning is complete and approved.
