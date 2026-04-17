# SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES

```yaml
SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true

  foundational_design_principles:
    SOLID: "Implement Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. Ensure decoupled and maintainable capability hubs."
    DRY: "Don't Repeat Yourself. Consolidate duplicated logic without creating fragile, tightly-coupled global utilities."
    YAGNI: "You Aren't Gonna Need It. Do not implement speculative, future-proofing code. Author strictly what is defined by the SPEC_DOC in the current context."
    KISS: "Keep It Simple, Stupid. Prefer simple, explicit, deterministic implementations over clever or overly abstract metaprogramming."

  architectural_and_design_patterns:
    HEXAGONAL_ARCHITECTURE: "Use hexagonal architecture to isolate domain logic from infrastructure and enable flexible integration through ports and adapters."
    PORTS_AND_ADAPTERS_ARCHITECTURE: "Organize systems around domain logic with ports and adapters so infrastructure concerns stay isolated from core behavior."
    FACTORY_PATTERN: "Use factory patterns to centralize complex object creation and keep construction concerns separate from runtime behavior."
    SINGLETON_PATTERN: "Use singleton patterns only when a single coordinated instance is genuinely required and its lifecycle can be explicitly controlled."
    OBSERVER_PATTERN: "Use observer patterns when state changes must notify dependent components without tightly coupling publishers and subscribers."
    STRATEGY_PATTERN: "Use strategy patterns to swap algorithms or behaviors behind a stable contract without branching through large conditional blocks."
    ADAPTER_PATTERN: "Use adapter patterns to translate external or legacy interfaces into internal contracts without leaking incompatible APIs into core code."
    DECORATOR_PATTERN: "Use decorator patterns to layer orthogonal behavior around an existing component without changing its core implementation."
    REPOSITORY_PATTERN: "Use repository patterns to isolate persistence concerns and provide stable domain-facing access patterns for stored data."
    DEPENDENCY_INJECTION: "Inject dependencies through constructors or explicit boundaries so components remain testable, replaceable, and loosely coupled."
    INTERFACE_CONTRACTS: "Define explicit interface contracts at boundaries so collaborating components remain decoupled and agreements stay stable."
    HEXAGONAL_PORTS: "Define ports as boundary contracts so core behavior can interact with external systems through deterministic integration points."
    HEXAGONAL_ADAPTERS: "Use hexagonal adapters to implement boundary contracts and translate external implementations without coupling core logic to infrastructure details."
    ANTI_CORRUPTION_LAYER: "Use an anti-corruption layer to isolate internal models from legacy or third-party semantics by translating data and behavior at the boundary."
    FACADE_PATTERN: "Use a facade pattern to provide a simplified entry point over a complex subsystem without exposing internal complexity to callers."
    BOUNDED_CONTEXT: "Use bounded contexts to keep domain language, rules, and models explicit within clear boundaries so different parts of the system can evolve without semantic drift."

  design_pattern_application_guidance:
    USE_PORTS_AND_ADAPTERS_ARCHITECTURE: "Use ports and adapters architecture when domain logic needs to stay isolated from frameworks, transports, and infrastructure implementations."
    USE_SINGLETON_PATTERN: "Use singleton patterns sparingly and only where a single shared instance is operationally required and explicitly controlled."
    USE_FACTORY_PATTERN: "Use factory patterns when object construction logic is complex, variable, or environment-dependent."
    USE_DECORATOR_PATTERN: "Use decorator patterns to layer orthogonal behavior such as logging, retries, or policy enforcement without modifying core implementations."
    USE_OBSERVER_PATTERN: "Use observer patterns where event-driven propagation is needed without introducing tight runtime dependencies."
    USE_FACADE_PATTERN: "Use a facade pattern when callers need a simplified entry point over a subsystem whose internal workflow or dependency graph would otherwise leak outward."
    USE_ANTI_CORRUPTION_LAYER: "Use an anti-corruption layer when integrating with legacy or third-party systems whose models, contracts, or semantics should not leak into the internal domain model."
    USE_BOUNDED_CONTEXT: "Use bounded contexts when different parts of the business or platform need distinct domain language, rules, or models with explicit translation between them."
    CONNECTION_POOLING: "Use connection pooling for shared external resources to improve throughput, reuse, and operational stability."
    FASTAPI_BEST_PRACTICES: "Follow FastAPI best practices for application structure, routing, dependency boundaries, and lifecycle management."
    PROJECT_STRUCTURE: "Use project and directory structures that keep routers, schemas, services, dependencies, and lifecycle modules organized in clear, maintainable locations."
    STRUCTURAL_HYGIENE: "Enforce structural hygiene by keeping files cohesive, boundaries explicit, naming consistent, and module placement aligned with responsibility."
    PYTHON_BEST_PRACTICES: "Follow modern Python best practices for readability, typing, packaging, testing, and maintainability."
    ASYNCHRONOUS: "Prefer asynchronous I/O for network, file, and service-bound operations when it improves scalability and latency behavior."
    NON_BLOCKING_IO: "Prefer non-blocking execution for network, file, and service-bound operations when blocking would reduce throughput or responsiveness."

  implementation_quality_practices:
    EXTENSIBILITY: "Design modules so new behavior can be added through clear extension points without destabilizing existing contracts."
    MODULARITY: "Partition code into cohesive modules with explicit responsibilities and minimal hidden dependencies."
    DYNAMIC_CONFIGURATION: "Design implementations so operational values, properties, props, keys, constants, mappings, thresholds, and runtime behavior are sourced from authoritative runtime inputs instead of fixed hard-coded definitions unless a documented requirement explicitly requires a fixed literal."
    IDEMPOTENCY: "Design repeatable operations to be idempotent so they can be executed safely without unintended side effects or divergent state, unless a documented requirement explicitly makes idempotency inapplicable."
    DETERMINISM: "Design implementations to produce predictable, repeatable outcomes for the same inputs, state, and documented execution conditions unless a documented requirement explicitly permits nondeterministic behavior."
    RESPONSIVENESS: "Design services and workflows to return timely results and degrade predictably under load or dependency delay."
    RESILIENCE: "Build components to tolerate transient failures, recover gracefully, and avoid cascading outages."
    ADAPTABILITY: "Keep interfaces and implementations flexible enough to absorb requirement changes without broad rewrites."
    LOOSE_COUPLING: "Minimize direct cross-component knowledge so modules can evolve, test, and deploy with lower coordination cost."
    HIGH_COHESION: "Keep related behavior and data close together so modules remain understandable, focused, and easier to change safely."
    SEPARATION_OF_CONCERNS: "Separate responsibilities across modules and layers so policy, orchestration, domain logic, and infrastructure concerns do not bleed into each other."
    TESTABILITY: "Design components so behavior can be verified in isolation through explicit boundaries, deterministic dependencies, and observable outcomes."

  resiliency_and_fault_tolerance_patterns:
    CIRCUIT_BREAKER: "Stop repeated calls into failing dependencies once a failure threshold is reached so the system can recover without cascading damage."
    RETRY: "Retry transient failures when the failure mode is likely temporary and the operation remains safe to repeat."
    TIMEOUT: "Set explicit execution time bounds so slow dependencies cannot block work indefinitely."
    FALLBACK: "Provide controlled fallback behavior when the primary dependency or path is unavailable."
    RATE_LIMITING: "Constrain request volume to protect downstream systems and preserve service stability under load."
    BULKHEAD: "Isolate resource pools and execution domains so one failing subsystem cannot exhaust the capacity of others."
    BACKOFF: "Increase retry spacing after repeated failures to reduce pressure on degraded dependencies."
    EXPONENTIAL_BACKOFF: "Use progressively increasing retry delays for transient failure handling so repeated retries do not amplify outages."
    JITTER: "Randomize retry intervals so concurrent callers do not synchronize retries and create a thundering herd against degraded dependencies."
    GRACEFUL_DEGRADATION: "Reduce nonessential functionality in a controlled way when dependencies or capacity are constrained so core user journeys remain available."
    LOAD_SHEDDING: "Deliberately reject, defer, or down-prioritize noncritical work when the system approaches saturation so critical paths stay healthy."

  resiliency_pattern_application_guidance:
    EXTERNAL_SERVICE_CALLS: "Use circuit breakers, retries with backoff, timeouts, and fallbacks for external service and API calls so dependency failures do not destabilize the system."
    DATABASE_OPERATIONS: "Use retries with backoff and circuit breakers for database operations to handle transient connectivity issues without overwhelming the data store."
    INTERNAL_SERVICE_CALLS: "Use timeouts and fallbacks for internal service-to-service calls to prevent cascading failures while allowing graceful degradation."
    USE_RATE_LIMITING: "Apply rate limiting to protect critical resources and maintain overall system responsiveness under load."
    BULKHEAD_ISOLATION: "Use bulkhead isolation to separate critical resource pools and execution domains so failures in one area do not exhaust shared capacity elsewhere."
    USE_JITTER: "Use jitter to randomize retry timing so concurrent callers do not synchronize retries and amplify load on degraded dependencies."
    RETRY_WITH_TIMEOUT_AND_JITTER: "Use retries with explicit timeouts and jitter when operations need both bounded execution time and randomized retry spacing."
    USE_GRACEFUL_DEGRADATION: "Use jitter, timeouts, and fallback behavior together when retry alone is insufficient and a controlled degraded response is required."
    USE_LOAD_SHEDDING: "Use jitter, timeouts, fallback behavior, and rate limiting together when degraded dependencies still need caller-side pressure controls."
    FAULT_CONTAINMENT: "Use the full stack of jitter, timeouts, fallback behavior, rate limiting, and bulkhead isolation for high-risk integrations that require strong containment and controlled degradation."

  YOU_MUST:
    - rule: "Apply foundational design principles."
      requirements:
        - "The principles defined in foundational_design_principles are MANDATORY; all production code MUST comply with them."
    - rule: "Implement required quality practices (or justify)."
      requirements:
        - "The practices defined in implementation_quality_practices are MANDATORY."
        - "All production code MUST be extensible unless a documented requirement explicitly makes extensibility not applicable."
        - "All production code MUST be modular unless a documented requirement explicitly makes modularity not applicable."
        - "All production code MUST be dynamically configured from authoritative runtime inputs unless a documented requirement explicitly requires a fixed literal."
        - "All repeatable production operations MUST be idempotent unless a documented requirement explicitly makes idempotency not applicable."
        - "All production code MUST be resilient unless a documented requirement explicitly makes resilience not applicable."
    - rule: "Justify any deviation explicitly."
      requirements:
        - "If a required practice from implementation_quality_practices is not applicable, the deviation MUST be explicitly justified (e.g., via code comment + review note) and MUST NOT be used to bypass required implementation work."
    - rule: "Keep implementations simple, deterministic, and testable."
      requirements:
        - "Implementations MUST remain simple, deterministic, and testable; complexity MUST be justified by requirements."

  YOU_SHOULD:
    - rule: "Prefer composition over inheritance."
      guidance:
        - "Prefer composition over inheritance when it reduces coupling."
    - rule: "Prefer explicit interfaces/contracts."
      guidance:
        - "Prefer explicit interfaces/contracts for cross-module boundaries."
    - rule: "Prefer async non-blocking I/O."
      guidance:
        - "Prefer async non-blocking I/O for network and file operations."

  GATE_CDP_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - SOFTWARE_DESIGN_AND_RESILIENCE_DIRECTIVES
      - "I MUST apply SOLID, DRY, YAGNI, and KISS to all production code."
      - "I MUST treat EXTENSIBILITY as a required implementation quality practice unless a documented requirement explicitly makes it not applicable."
      - "I MUST treat MODULARITY as a required implementation quality practice unless a documented requirement explicitly makes it not applicable."
      - "I MUST treat DYNAMIC_CONFIGURATION as a required implementation quality practice unless a documented requirement explicitly requires a fixed literal."
      - "I MUST treat RESILIENCE as a required implementation quality practice unless a documented requirement explicitly makes it not applicable."
      - "I MUST treat DETERMINISM as a required implementation quality practice unless a documented requirement explicitly permits nondeterministic behavior."
      - "I MUST treat IDEMPOTENCY as a required implementation quality practice for repeatable operations unless a documented requirement explicitly makes it not applicable."
      - "I MUST NOT implement speculative future-proofing code; I MUST author only what is required by the current SPEC_DOC."
      - "I MUST explicitly justify any deviation from required design practices via code comment and review note."
    THEN: CONTINUE

# ------------------------------------------------------------
## Concurrent Development Environment Directives

```
