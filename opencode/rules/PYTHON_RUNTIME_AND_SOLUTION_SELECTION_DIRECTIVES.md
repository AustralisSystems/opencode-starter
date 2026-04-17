# PYTHON_RUNTIME_AND_SOLUTION_SELECTION_DIRECTIVES

```yaml
PYTHON_RUNTIME_AND_SOLUTION_SELECTION_DIRECTIVES:
  enforcement: MANDATORY
  blocking: true

  python_runtime_and_dependency_policy:
    intent: "Python 3.12+ runtime baseline with a dependency-first, buy-before-build implementation policy."
    PYTHON_RUNTIME_BASELINE: "All agents and LLMs operating under this policy MUST assume Python 3.12+ as the minimum runtime and language baseline."
    DEPENDENCY_FIRST: "External dependencies are not merely permitted; they are expected when they provide a clearer, safer, faster, or more maintainable solution than bespoke local code."
    BUY_BEFORE_BUILD: "When a maintained public package, public repository, or CNCF project already provides the required capability, that existing battle-tested solution MUST be preferred over creating custom modules, wrappers, or replacement implementations."
    CUSTOM_CODE_LAST_RESORT: "Do not default to writing custom code when a proven, actively maintained external solution already exists."
    requirements:
      - "Assume Python 3.12+ language features, typing behavior, and ecosystem compatibility as the default baseline."
      - "Expect external dependencies to be a normal and preferred part of implementation when they improve delivery quality."
      - "Before authoring bespoke code, check whether a public package, repo, or CNCF project already satisfies the requirement."
      - "Prefer maintained, production-proven external solutions over custom code or local utility modules when they fit the task."
      - "Only fall back to custom code when no viable external solution exists or when a documented repository constraint requires an internal implementation."

  external_solution_selection_principles:
    OPEN_SOURCE_FIRST: "Prefer actively maintained open source packages, libraries, and projects over bespoke custom code when they satisfy the requirement."
    CNCF_PREFERENCE: "Prefer CNCF Graduated or Incubating projects when they fit the required capability and operating model."
    EXTEND_BEFORE_REPLACE: "Prefer extending or integrating an existing approved external solution before introducing a bespoke replacement implementation."
    PRODUCTION_PROVEN: "Prefer production-proven, battle-tested solutions with active maintenance and demonstrated operational use over unproven bespoke implementations."

  external_solution_preference_order:
    - "CNCF Graduated or Incubating project"
    - "Actively maintained open source package, library, or project"
    - "Extension of an existing approved external solution already used in the repository"
    - "Archived but still maintained external solution, only when no actively maintained option fits"
    - "Bespoke custom code only when no viable external or CNCF solution exists"

  YOU_MUST:
    - rule: "Apply PYTHON_RUNTIME_BASELINE for production-oriented implementation decisions."
      requirements:
        - "All production-oriented implementation decisions MUST assume Python 3.12+ as the minimum baseline unless an explicit repository exception says otherwise."
    - rule: "Apply DEPENDENCY_FIRST when external dependencies improve delivery quality."
      requirements:
        - "External dependencies MUST be treated as allowed and expected when they improve safety, maintainability, delivery speed, or operational quality."
    - rule: "Apply BUY_BEFORE_BUILD before authoring bespoke implementations."
      requirements:
        - "Before writing bespoke modules, wrappers, or replacement implementations, agents MUST evaluate whether a public package, public repository, or CNCF project already satisfies the requirement."
    - rule: "Apply EXTEND_BEFORE_REPLACE before introducing bespoke replacements."
      requirements:
        - "Before introducing a bespoke replacement for an approved external solution already used in the repository, agents MUST evaluate whether extending or integrating the existing approved solution satisfies the requirement."
    - rule: "Apply OPEN_SOURCE_FIRST, CNCF_PREFERENCE, and PRODUCTION_PROVEN before bespoke custom code."
      requirements:
        - "If a viable, maintained, battle-tested external solution exists, it MUST be preferred over custom code."

  GATE_CPD_001:
    enforcement: MANDATORY
    blocking: true
    UNDERSTAND_AND_ACKNOWLEDGE:
      - PYTHON_RUNTIME_AND_SOLUTION_SELECTION_DIRECTIVES
      - "I MUST apply PYTHON_RUNTIME_BASELINE unless an explicit repository directive states otherwise."
      - "I MUST apply DEPENDENCY_FIRST when external dependencies provide a clearer, safer, faster, or more maintainable solution than bespoke local code."
      - "I MUST apply BUY_BEFORE_BUILD by evaluating maintained public packages, public repositories, and CNCF projects before creating custom modules, wrappers, or replacement implementations."
      - "I MUST apply OPEN_SOURCE_FIRST, CNCF_PREFERENCE, and PRODUCTION_PROVEN before choosing bespoke custom code."
      - "I MUST apply EXTEND_BEFORE_REPLACE before introducing a bespoke replacement for an approved external solution already used in the repository."
    THEN: CONTINUE

## Software Design And Resilience Directives

```
