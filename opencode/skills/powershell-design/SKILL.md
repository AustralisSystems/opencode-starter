# PowerShell Design Skill

**Purpose:** Design PowerShell scripts and modules using best practices, SOLID principles, and modular architecture

**When to use:** Before implementing PowerShell solutions - planning architecture, module structure, and dependencies

---

## RFC 2119 COMPLIANCE

All instructions in this skill MUST be interpreted according to RFC 2119 <https://datatracker.ietf.org/doc/html/rfc2119>.

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

### Enforcement Statement

All instructions in this skill MUST be interpreted according to RFC 2119. No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.

### Important Notes

- **MUST/SHALL** = absolute requirement (non-negotiable)
- **MUST NOT/NEVER** = absolute prohibition (strictly forbidden)
- **SHOULD** = strong recommendation (with documented exceptions allowed)
- **MAY/OPTIONAL** = truly optional (implementer's choice)

---

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL PowerShell design work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → design (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)

1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous PowerShell design decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` BEFORE designing
   - `context7`: "PowerShell module design patterns 2025"
   - `context7`: "PowerShell SOLID design principles"
   - `context7`: "PowerShell parameter validation best practices"
   - `grep`: "PowerShell module structure examples github"
   - `grep`: "PowerShell error handling patterns github"
3. **PLANNING**: Use `sequential-thinking` to structure design approach
4. **DESIGN**: Create architecture documents and module specifications
5. **PROGRESS TRACKING**: Record design decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist design patterns to `neo4j-memory`

**ABSOLUTELY FORBIDDEN:**
- ❌ Designing without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving design decisions to neo4j-memory
- ❌ Designing monolithic scripts instead of modular solutions
- ❌ Ignoring PowerShell naming conventions (Verb-Noun)

---

## PowerShell Design Principles

### 1. Module vs Script Decision Matrix

**Use MODULES (`.psm1`) when:**
- ✅ Functionality will be reused across multiple scripts
- ✅ Creating shared utilities (Common.*)
- ✅ Implementing domain-specific business logic
- ✅ Need to export functions for import
- ✅ Following SOLID principles and separation of concerns

**Use SCRIPTS (`.ps1`) when:**
- ✅ Orchestrating module functions (calling modules)
- ✅ Creating entry points for automation
- ✅ Implementing workflow-specific logic
- ✅ Providing command-line interfaces

**Example Decision:**
```powershell
# BAD: Monolithic script with everything
# Get-UserReport.ps1 (500+ lines)
#   - AD query logic
#   - Data processing
#   - Report generation
#   - Email sending
# ❌ Not reusable, hard to test, violates SRP

# GOOD: Modular design
# Modules/Common.ActiveDirectory/Get-ADUserData.psm1
# Modules/Common.Reporting/New-HTMLReport.psm1
# Modules/Common.Email/Send-EmailReport.psm1
# Scripts/Get-UserReport.ps1 (imports and orchestrates modules)
# ✅ Reusable, testable, follows SOLID
```

### 2. Module Naming Conventions

**Common Modules (Shared):**
```
Common.Core           # Base classes, Result pattern
Common.Logging        # Centralized logging
Common.Configuration  # Configuration management
Common.Utilities      # General utilities
Common.ActiveDirectory # AD operations
Common.FileSystem     # File system operations
Common.JsonFile       # JSON file operations
Common.CsvFile        # CSV file operations
```

**Domain-Specific Modules:**
```
DomainName.Feature    # Use descriptive domain names
StorageAnalysis.Core  # Storage domain, core feature
StorageAnalysis.NTFS  # Storage domain, NTFS feature
SoftwareManagement.Remote  # Software domain, remote feature
SafeCleanup.UserProfiles   # Cleanup domain, profiles feature
```

**Naming Rules:**
- Always use PascalCase
- Use dot notation for hierarchy: `Domain.Subdomain.Feature`
- Start with domain/namespace
- End with specific feature
- Avoid generic names (`Utilities`, `Helpers` need namespace prefix)

### 3. Function Design Patterns

**Follow PowerShell Verb-Noun Convention:**

```powershell
# Approved Verbs (Get-Verb for full list)
Get-Something      # Retrieve data
Set-Something      # Set/modify data
New-Something      # Create new object
Remove-Something   # Delete object
Invoke-Something   # Execute operation
Test-Something     # Validate/test condition
Start-Something    # Begin process
Stop-Something     # End process

# Nouns should be singular
Get-User    # ✅ Good
Get-Users   # ❌ Bad (plural)

# Nouns should be specific
Get-ADUserAccount     # ✅ Good (specific)
Get-Data              # ❌ Bad (too generic)
```

**Function Structure Template:**

```powershell
Function Get-ModuleFunctionName {
    <#
    .SYNOPSIS
        Brief description (one line)

    .DESCRIPTION
        Detailed description of what the function does
        Include multiple paragraphs if needed

    .PARAMETER ParameterName
        Description of what this parameter does

    .EXAMPLE
        Get-ModuleFunctionName -ParameterName "Value"
        Description of what this example demonstrates

    .OUTPUTS
        PSCustomObject with properties: Property1, Property2

    .NOTES
        Additional information
        Author: Your Name
        Version: 1.0.0
        Date: YYYY-MM-DD
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    Param(
        [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$ParameterName
    )

    begin {
        Write-Verbose "Starting $($MyInvocation.MyCommand)"
    }

    process {
        try {
            # Implementation
            $result = [PSCustomObject]@{
                Property1 = "Value"
                Success = $true
            }
            return $result
        }
        catch {
            Write-Error "Error in $($MyInvocation.MyCommand): $_"
            throw
        }
    }

    end {
        Write-Verbose "Completed $($MyInvocation.MyCommand)"
    }
}
```

### 4. Parameter Design Best Practices

**Parameter Validation:**

```powershell
Param(
    # Required with validation
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$ComputerName,

    # Optional with default
    [Parameter(Mandatory=$false)]
    [ValidateSet("Low", "Medium", "High")]
    [string]$Priority = "Medium",

    # Numeric range
    [Parameter(Mandatory=$true)]
    [ValidateRange(1, 100)]
    [int]$Percentage,

    # File path validation
    [Parameter(Mandatory=$true)]
    [ValidateScript({Test-Path $_ -PathType Container})]
    [string]$FolderPath,

    # Multiple values
    [Parameter(Mandatory=$false)]
    [string[]]$ServerNames,

    # Switch parameter
    [Parameter(Mandatory=$false)]
    [switch]$WhatIf
)
```

**Pipeline Support:**

```powershell
Param(
    # Accept from pipeline by value
    [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
    [string]$InputObject,

    # Accept from pipeline by property name
    [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
    [string]$ComputerName
)

# Usage:
Get-Content servers.txt | Get-ServerInfo
Get-ADComputer -Filter * | Get-ServerInfo
```

### 5. Error Handling Design

**Use Result Pattern (from Common.Core):**

```powershell
# Import Common.Core for Result class
Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1"

Function Get-UserData {
    [CmdletBinding()]
    [OutputType([Result])]
    Param(
        [Parameter(Mandatory=$true)]
        [string]$Username
    )

    try {
        $user = Get-ADUser -Identity $Username
        return [Result]::Success($user)
    }
    catch [Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException] {
        return [Result]::Failure("User '$Username' not found")
    }
    catch [Microsoft.ActiveDirectory.Management.ADServerDownException] {
        return [Result]::Failure("AD server is unreachable", $_)
    }
    catch {
        return [Result]::Failure("Unexpected error: $($_.Exception.Message)", $_)
    }
}

# Usage in scripts
$result = Get-UserData -Username "jdoe"
if ($result.Success) {
    # Process user data
    $user = $result.Data
} else {
    Write-Error $result.ErrorMessage
    if ($result.Exception) {
        Write-Error $result.Exception.StackTrace
    }
}
```

### 6. Dependency Design

**Module Dependencies:**

```powershell
# At top of module file (.psm1)
#Requires -Version 5.1
#Requires -Modules ActiveDirectory, ImportExcel

# Import internal dependencies
Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1" -ErrorAction Stop
Import-Module "$PSScriptRoot\..\Common.Logging\Common.Logging.psm1" -ErrorAction Stop
```

**Dependency Injection Pattern:**

```powershell
# Good: Inject dependencies
Function Process-Users {
    Param(
        [Parameter(Mandatory=$true)]
        [object]$Logger,  # Injected

        [Parameter(Mandatory=$true)]
        [object]$Config   # Injected
    )

    $Logger.LogInfo("Processing users")
    $threshold = $Config.GetSetting("UserThreshold")
}

# Usage
$logger = Initialize-Logger "MyScript"
$config = Get-Configuration "MyApp"
Process-Users -Logger $logger -Config $config

# Bad: Hard-coded dependencies
Function Process-Users {
    $logger = New-Logger  # ❌ Hard-coded
    $config = Get-Config  # ❌ Hard-coded
}
```

### 7. Logging Design

**Use Common.Logging Module:**

```powershell
Import-Module "$PSScriptRoot\..\Common.Logging\Common.Logging.psm1"

# In module functions
Function Get-SomeData {
    Param(
        [Parameter(Mandatory=$true)]
        [object]$Logger
    )

    $Logger.LogInfo("Starting data retrieval")
    $Logger.LogDebug("Query parameters: $params")

    try {
        # ... operation
        $Logger.LogInfo("Successfully retrieved $count items")
    }
    catch {
        $Logger.LogError("Failed to retrieve data: $_")
        throw
    }
}

# In scripts
$logger = Initialize-Logger -ScriptName $MyInvocation.MyCommand.Name

$logger.LogHeader("Starting Script")
$result = Get-SomeData -Logger $logger
$logger.LogHeader("Completed Script")
```

### 8. Configuration Design

**Use Common.Configuration Module:**

```powershell
# Configuration structure
$config = [ConfigurationBase]::new("MyApp", "Application configuration")

$config.SetSetting("ServerName", "server01.domain.com")
$config.SetSetting("Timeout", 300)
$config.SetSetting("RetryCount", 3)

# In functions
Function Connect-Server {
    Param(
        [object]$Config
    )

    $serverName = $Config.GetSetting("ServerName")
    $timeout = $Config.GetSetting("Timeout")

    # Use settings
}
```

### 9. Design for Testability

**Pester-Friendly Design:**

```powershell
# Design functions to be testable
Function Get-UserAge {
    Param(
        [Parameter(Mandatory=$true)]
        [datetime]$BirthDate,

        [Parameter(Mandatory=$false)]
        [datetime]$ReferenceDate = (Get-Date)  # Inject current date for testing
    )

    $age = ($ReferenceDate - $BirthDate).Days / 365.25
    return [int]$age
}

# Test with specific reference date
Describe "Get-UserAge Tests" {
    It "Calculates correct age" {
        $birthDate = Get-Date "1990-01-01"
        $referenceDate = Get-Date "2025-01-01"

        $age = Get-UserAge -BirthDate $birthDate -ReferenceDate $referenceDate

        $age | Should -Be 35
    }
}
```

### 10. Project Structure Design Template

```
ProjectRoot/
├── Modules/                          # All reusable modules
│   ├── Common.Core/                 # MANDATORY - Base classes
│   │   ├── Common.Core.psm1
│   │   ├── Common.Core.psd1         # Module manifest
│   │   └── examples/
│   ├── Common.Logging/              # MANDATORY - Logging
│   │   ├── Common.Logging.psm1
│   │   └── examples/
│   ├── Common.Configuration/
│   └── DomainName.Feature/
│       ├── DomainName.Feature.psm1
│       ├── DomainName.Feature.psd1
│       └── examples/
├── Scripts/                          # Orchestration scripts
│   ├── Shared/
│   │   ├── Initialize-Logger.ps1
│   │   └── Get-Configuration.ps1
│   └── Operations/
│       ├── Get-UserReport.ps1
│       └── Sync-ADUsers.ps1
├── Tests/                            # Pester tests
│   ├── Common.Core.Tests.ps1
│   ├── Common.Logging.Tests.ps1
│   └── DomainName.Feature.Tests.ps1
├── Config/                           # Configuration files
│   ├── app.config.json
│   └── logging.config.json
├── Data/                             # Application data
│   ├── input/
│   └── output/
├── Logs/                             # Log files
├── README.md
└── .gitignore
```

### 11. Real-World Design Example

**From saw-automation-projects:**

**Problem:** Need to analyze Windows Server storage, find duplicates, export data

**Design Decision:**

```
Modules (Reusable Business Logic):
├── Common.Core            # Result pattern, base classes
├── Common.Logging         # Centralized logging
├── StorageAnalysis.Core   # Core scanning engine
├── StorageAnalysis.FileSystem  # File system operations
├── StorageAnalysis.NTFS   # NTFS-specific operations
├── StorageAnalysis.Hashing   # File hashing
├── StorageAnalysis.Filtering # Data filtering
└── StorageAnalysis.Export    # Export to JSON/CSV

Scripts (Orchestration):
└── Scripts/FileAnalysis/Get-StorageFileScan.ps1
    - Imports modules
    - Initializes logger
    - Calls module functions in sequence
    - Handles overall workflow
```

**Why This Design:**
- ✅ Each module has single responsibility (SRP)
- ✅ Modules are reusable across scripts
- ✅ Easy to test individual modules
- ✅ Can swap implementations (e.g., different export formats)
- ✅ Clear dependency hierarchy

### 12. Design Checklist

**Before implementing, verify:**

- [ ] Module vs script decision made correctly
- [ ] Naming follows PowerShell conventions (Verb-Noun)
- [ ] SOLID principles considered
- [ ] Dependencies identified and injection planned
- [ ] Error handling strategy defined (Result pattern)
- [ ] Logging approach planned (Common.Logging)
- [ ] Configuration needs identified
- [ ] Testing approach designed (Pester)
- [ ] Parameter validation designed
- [ ] Pipeline support considered
- [ ] Comment-based help planned
- [ ] Version control considered (.psd1 manifest)

---

## Integration with MCP Workflow

**When designing PowerShell solutions:**

1. **Load Context**: `neo4j-memory` - "Load PowerShell design patterns from previous projects"
2. **Research**: `context7` - "PowerShell module design best practices 2025"
3. **Research**: `grep` - "PowerShell SOLID principles examples github"
4. **Plan**: `sequential-thinking` - "Plan module hierarchy and dependencies"
5. **Design**: Document architecture and module specifications
6. **Track**: `neo4j-memory` - "Record design: Using Common.Core Result pattern for all functions"
7. **Save**: `neo4j-memory` - "Persist: StorageAnalysis modules follow single responsibility principle"

---

## Quick Reference

**Design Decision Tree:**

```
Need functionality?
│
├─ Used by multiple scripts? ────YES──> Create MODULE (.psm1)
│                                       │
│                                       ├─ Shared across projects? ──YES──> Common.* module
│                                       └─ Project-specific? ──YES──> DomainName.* module
│
└─ One-time workflow? ────YES──> Create SCRIPT (.ps1)
                                 (imports modules, orchestrates)
```

**Module Design Template:**

```powershell
#Requires -Version 5.1

# Import dependencies
Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1"
Import-Module "$PSScriptRoot\..\Common.Logging\Common.Logging.psm1"

# Public functions (begin, process, end)
Function Verb-Noun {
    [CmdletBinding()]
    [OutputType([Result])]
    Param([object]$Logger)

    try {
        # Logic
        return [Result]::Success($data)
    }
    catch {
        return [Result]::Failure("Error", $_)
    }
}

# Export
Export-ModuleMember -Function Verb-Noun
```

---

**References:**
- Production Examples: `C:\github_development\projects\saw-automation-projects`
- Module Architecture: See `powershell-module-architecture` skill
- PowerShell Best Practices: Use context7 + grep for latest guidance

**Skill Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** PRODUCTION READY

**Follow THE GOLDEN RULE. Research before designing. Save decisions to neo4j-memory.**
