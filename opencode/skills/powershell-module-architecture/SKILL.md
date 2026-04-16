# PowerShell Module Architecture Skill

**Purpose:** Design and implement modular, reusable PowerShell modules following enterprise best practices

**When to use:** Creating PowerShell modules with proper separation of concerns, shared functionality, and SOLID principles

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

**ALL PowerShell module architecture work MUST follow the MCP workflow - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)

1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous PowerShell architecture decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` BEFORE designing modules
   - `context7`: "PowerShell module best practices 2025"
   - `context7`: "PowerShell SOLID principles modules"
   - `grep`: "PowerShell module architecture patterns"
   - `grep`: "PowerShell .psm1 examples github"
3. **PLANNING**: Use `sequential-thinking` to structure module organization
4. **IMPLEMENTATION**: Use `filesystem` to create module files
5. **PROGRESS TRACKING**: Record architecture decisions to `neo4j-memory`
6. **CONTEXT SAVE**: Persist module patterns to `neo4j-memory`

**ABSOLUTELY FORBIDDEN:**
- ❌ Designing modules without context7 + grep research
- ❌ Skipping neo4j-memory context load
- ❌ Completing without saving architecture decisions to neo4j-memory
- ❌ Creating monolithic scripts instead of modular code
- ❌ Ignoring PowerShell best practices and naming conventions

---

## PowerShell Module Architecture Principles

### 1. Modular Design Pattern (MANDATORY)

**Project Structure:**
```
ProjectRoot/
├── Modules/                    # All reusable modules
│   ├── Common.Core/           # Shared base classes and interfaces
│   │   ├── Common.Core.psm1  # Module file
│   │   └── examples/         # Usage examples
│   ├── Common.Logging/        # Centralized logging
│   ├── Common.Configuration/  # Configuration management
│   └── DomainName.Feature/    # Domain-specific modules
├── Scripts/                    # Orchestration scripts (call modules)
│   ├── Shared/                # Shared script utilities
│   └── DomainSpecific/        # Domain-specific orchestration
├── Tests/                      # Pester tests
├── Data/                       # Application data
└── README.md                   # Project documentation
```

**Naming Conventions:**

**Common Modules** (shared across projects):
- `Common.Core` - Base classes, interfaces, Result pattern
- `Common.Logging` - Centralized logging service
- `Common.Configuration` - Configuration management
- `Common.Utilities` - General utility functions
- `Common.ExceptionHandling` - Error handling utilities
- `Common.JsonFile` - JSON file operations
- `Common.CsvFile` - CSV file operations

**Domain-Specific Modules** (project-specific):
- `DomainName.Feature` - Use descriptive domain names
- `StorageAnalysis.Core` - Core storage scanning engine
- `StorageAnalysis.FileSystem` - File system operations
- `SoftwareManagement.Remote` - Remote software management
- `SafeCleanup.UserProfiles` - User profile cleanup

### 2. Module File Structure (`.psm1`)

**Standard Module Template:**

```powershell
#Requires -Version 5.1

<#
.SYNOPSIS
    Brief description of module purpose

.DESCRIPTION
    Detailed description of module functionality:
    - Key feature 1
    - Key feature 2
    - Key feature 3

.NOTES
    Module: ModuleName
    Version: 1.0.0
    Date: YYYY-MM-DD

    Dependencies:
    - PowerShell 5.1 or higher
    - Other required modules

    Design Principles:
    - SOLID: Single Responsibility
    - DRY: Don't Repeat Yourself
    - KISS: Keep It Simple, Stupid
#>

# Module-level variables
$script:ModuleName = 'ModuleName'
$script:ModuleVersion = '1.0.0'

#region Imports and Dependencies

# Import required modules
Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1" -ErrorAction Stop

#endregion

#region Public Functions

Function Get-SomethingFromModule {
    <#
    .SYNOPSIS
        Brief description of function

    .DESCRIPTION
        Detailed description of what the function does

    .PARAMETER ParameterName
        Description of the parameter

    .EXAMPLE
        Get-SomethingFromModule -ParameterName "Value"
        Description of the example

    .OUTPUTS
        PSCustomObject with properties: Property1, Property2

    .NOTES
        This function follows PowerShell best practices
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    Param(
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$ParameterName
    )

    begin {
        Write-Verbose "Starting $($MyInvocation.MyCommand)"
    }

    process {
        try {
            # Implementation here
            $result = [PSCustomObject]@{
                Property1 = "Value"
                Property2 = 123
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

#endregion

#region Private Functions

# Private helper functions (not exported)
Function Invoke-PrivateHelper {
    # Implementation
}

#endregion

#region Module Initialization

# Module initialization code
Write-Verbose "$ModuleName version $ModuleVersion loaded"

#endregion

# Export public functions
Export-ModuleMember -Function Get-SomethingFromModule
```

### 3. Common.Core Module (BASE CLASSES)

**MANDATORY base classes for all projects:**

```powershell
# Common.Core.psm1

class BaseEntity {
    [datetime] $CreatedAt
    [datetime] $ModifiedAt
    [string] $CreatedBy
    [string] $ModifiedBy
    [guid] $Id

    BaseEntity() {
        $this.CreatedAt = Get-Date
        $this.ModifiedAt = Get-Date
        $this.Id = [guid]::NewGuid()
    }

    [void] Update() {
        $this.ModifiedAt = Get-Date
    }

    [string] ToString() {
        return "$($this.GetType().Name) ($($this.Id))"
    }
}

class Result {
    [bool] $Success
    [object] $Data
    [string] $ErrorMessage
    [System.Exception] $Exception
    [hashtable] $Metadata

    Result() {
        $this.Success = $true
        $this.Metadata = @{}
    }

    Result([bool]$success, [string]$errorMessage) {
        $this.Success = $success
        $this.ErrorMessage = $errorMessage
        $this.Metadata = @{}
    }

    Result([bool]$success, [object]$data, [string]$errorMessage) {
        $this.Success = $success
        $this.Data = $data
        $this.ErrorMessage = $errorMessage
        $this.Metadata = @{}
    }

    # Static factory methods
    static [Result] Success([object]$data) {
        return [Result]::new($true, $data, $null)
    }

    static [Result] Success() {
        return [Result]::new($true, $null, $null)
    }

    static [Result] Failure([string]$errorMessage) {
        return [Result]::new($false, $null, $errorMessage)
    }

    static [Result] Failure([string]$errorMessage, [System.Exception]$exception) {
        $result = [Result]::new($false, $null, $errorMessage)
        $result.Exception = $exception
        return $result
    }

    [void] AddMetadata([string]$key, [object]$value) {
        $this.Metadata[$key] = $value
    }

    [string] ToString() {
        if ($this.Success) {
            return "Success: $(if ($this.Data) { $this.Data.ToString() } else { 'No data' })"
        } else {
            return "Failure: $($this.ErrorMessage)"
        }
    }
}

class ConfigurationBase : BaseEntity {
    [string] $Name
    [string] $Description
    [hashtable] $Settings

    ConfigurationBase() {
        $this.Settings = @{}
    }

    ConfigurationBase([string]$name, [string]$description) {
        $this.Name = $name
        $this.Description = $description
        $this.Settings = @{}
    }

    [void] SetSetting([string]$key, [object]$value) {
        $this.Settings[$key] = $value
        $this.Update()
    }

    [object] GetSetting([string]$key) {
        return $this.Settings[$key]
    }
}
```

**Usage in other modules:**

```powershell
Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1" -ErrorAction Stop

# Use Result pattern for function returns
Function Get-SomeData {
    try {
        $data = # ... fetch data
        return [Result]::Success($data)
    }
    catch {
        return [Result]::Failure("Failed to fetch data", $_)
    }
}
```

### 4. Common.Logging Module (CENTRALIZED LOGGING)

**MANDATORY logging for all scripts and modules:**

```powershell
# Common.Logging.psm1

class CommonLogger {
    hidden [object] $LoggerInstance
    [string] $ScriptName
    [string] $LogLevel
    [bool] $ConsoleOutput
    [bool] $FileOutput

    CommonLogger([string]$scriptName, [object]$LoggerInstance) {
        $this.ScriptName = $scriptName
        $this.LoggerInstance = $LoggerInstance
        $this.LogLevel = "INFO"
        $this.ConsoleOutput = $true
        $this.FileOutput = $true
    }

    [void] LogInfo([string]$message) {
        $this.LogInfo($message, "General")
    }

    [void] LogInfo([string]$message, [string]$category) {
        if ($this.LoggerInstance) {
            $this.LoggerInstance.LogInfo($message, $category)
        }
    }

    [void] LogWarning([string]$message) {
        $this.LogWarning($message, "General")
    }

    [void] LogWarning([string]$message, [string]$category) {
        if ($this.LoggerInstance) {
            $this.LoggerInstance.LogWarning($message, $category)
        }
    }

    [void] LogError([string]$message) {
        $this.LogError($message, "General")
    }

    [void] LogError([string]$message, [string]$category) {
        if ($this.LoggerInstance) {
            $this.LoggerInstance.LogError($message, $category)
        }
    }

    [void] LogDebug([string]$message) {
        $this.LogDebug($message, "General")
    }

    [void] LogDebug([string]$message, [string]$category) {
        if ($this.LoggerInstance) {
            $this.LoggerInstance.LogDebug($message, $category)
        }
    }

    # Specialized logging methods
    [void] LogStep([string]$message) {
        $this.LogInfo("STEP: $message", "Workflow")
    }

    [void] LogHeader([string]$message) {
        $this.LogInfo("========== $message ==========", "Header")
    }

    [void] LogRemoteCommand([string]$serverName, [string]$command) {
        $this.LogDebug("REMOTE EXEC: $serverName - $command", "RemoteExecution")
    }

    [void] LogRemoteSuccess([string]$serverName, [string]$operation) {
        $this.LogInfo("SUCCESS: $serverName - $operation", "RemoteExecution")
    }

    [void] LogRemoteFailure([string]$serverName, [string]$operation, [string]$error) {
        $this.LogError("FAILURE: $serverName - $operation - $error", "RemoteExecution")
    }
}
```

### 5. Script Organization (Orchestration)

**Scripts call modules, scripts do NOT contain business logic:**

```powershell
# Scripts/DomainSpecific/Do-SomeOperation.ps1

#Requires -Version 5.1

[CmdletBinding()]
Param(
    [Parameter(Mandatory=$true)]
    [string]$TargetPath,

    [Parameter(Mandatory=$false)]
    [switch]$WhatIf
)

# Import required modules
Import-Module "$PSScriptRoot\..\..\Modules\Common.Core\Common.Core.psm1" -ErrorAction Stop
Import-Module "$PSScriptRoot\..\..\Modules\Common.Logging\Common.Logging.psm1" -ErrorAction Stop
Import-Module "$PSScriptRoot\..\..\Modules\DomainName.Feature\DomainName.Feature.psm1" -ErrorAction Stop

# Initialize logger
$logger = Initialize-ModuleLogger -ScriptName $MyInvocation.MyCommand.Name

try {
    $logger.LogHeader("Starting $($MyInvocation.MyCommand.Name)")

    # Call module functions (business logic is in modules)
    $result = Get-SomethingFromModule -ParameterName $TargetPath

    if ($result.Success) {
        $logger.LogInfo("Operation completed successfully")
        $logger.LogInfo("Results: $($result.Data.Count) items processed")
    }
    else {
        $logger.LogError("Operation failed: $($result.ErrorMessage)")
        exit 1
    }
}
catch {
    $logger.LogError("Unhandled exception: $_")
    throw
}
finally {
    $logger.LogHeader("Completed $($MyInvocation.MyCommand.Name)")
}
```

### 6. SOLID Principles in PowerShell

**Single Responsibility Principle (SRP):**
- Each module has ONE clear purpose
- `Common.Logging` - ONLY logging
- `Common.Configuration` - ONLY configuration
- `DomainName.FileSystem` - ONLY filesystem operations for that domain

**Open/Closed Principle (OCP):**
- Modules are open for extension (inheritance, composition)
- Modules are closed for modification (stable interfaces)

```powershell
# Extend base classes, don't modify them
class CustomEntity : BaseEntity {
    [string] $CustomProperty

    CustomEntity() : base() {
        $this.CustomProperty = "Custom"
    }
}
```

**Liskov Substitution Principle (LSP):**
- Derived classes can substitute base classes

```powershell
# All Result objects work the same way
$result1 = [Result]::Success($data)
$result2 = [Result]::Failure("Error")
# Both have same interface: .Success, .Data, .ErrorMessage
```

**Interface Segregation Principle (ISP):**
- Modules depend only on what they need
- Don't force dependencies on unused functionality

**Dependency Inversion Principle (DIP):**
- Depend on abstractions (interfaces), not concrete implementations
- Inject dependencies (logger, configuration)

```powershell
# Good: Dependency injection
Function Process-Data {
    Param(
        [object]$Logger,  # Injected dependency
        [object]$Config   # Injected dependency
    )
    $Logger.LogInfo("Processing data")
}

# Bad: Hard-coded dependency
Function Process-Data {
    $logger = New-Logger  # Hard-coded!
}
```

### 7. Error Handling Patterns

**Use Result Pattern:**

```powershell
Function Get-UserData {
    try {
        $users = Get-ADUser -Filter *
        return [Result]::Success($users)
    }
    catch [Microsoft.ActiveDirectory.Management.ADServerDownException] {
        return [Result]::Failure("AD server is down", $_)
    }
    catch {
        return [Result]::Failure("Unexpected error retrieving users", $_)
    }
}

# Usage
$result = Get-UserData
if ($result.Success) {
    foreach ($user in $result.Data) {
        # Process user
    }
}
else {
    Write-Error $result.ErrorMessage
    if ($result.Exception) {
        Write-Error $result.Exception.Message
    }
}
```

### 8. Real-World Example from Production

**From saw-automation-projects repository:**

**Modules Structure:**
```
Modules/
├── Common.Core/
│   └── Common.Core.psm1         # Base classes (BaseEntity, Result, ConfigurationBase)
├── Common.Logging/
│   └── Common.Logging.psm1      # Centralized logging (CommonLogger class)
├── Common.Configuration/
│   └── Common.Configuration.psm1 # Configuration management
├── StorageAnalysis.Core/
│   └── StorageAnalysis.Core.psm1 # Core storage scanning engine
├── StorageAnalysis.FileSystem/
│   └── StorageAnalysis.FileSystem.psm1 # File system operations
├── StorageAnalysis.NTFS/
│   └── StorageAnalysis.NTFS.psm1 # NTFS-specific operations
└── StorageAnalysis.Export/
    └── StorageAnalysis.Export.psm1 # Export functionality
```

**Scripts use modules:**
```powershell
# Scripts/FileAnalysis/Get-StorageFileScan.ps1

# Import modules
Import-Module "$PSScriptRoot\..\..\Modules\Common.Core\Common.Core.psm1"
Import-Module "$PSScriptRoot\..\..\Modules\Common.Logging\Common.Logging.psm1"
Import-Module "$PSScriptRoot\..\..\Modules\StorageAnalysis.Core\StorageAnalysis.Core.psm1"
Import-Module "$PSScriptRoot\..\..\Modules\StorageAnalysis.FileSystem\StorageAnalysis.FileSystem.psm1"
Import-Module "$PSScriptRoot\..\..\Modules\StorageAnalysis.Export\StorageAnalysis.Export.psm1"

# Initialize
$logger = Initialize-StorageLogger -ScriptName $MyInvocation.MyCommand.Name

# Use module functions
$scanResult = Invoke-StorageScan -Path $TargetPath -Logger $logger
$exportResult = Export-StorageData -Data $scanResult.Data -Format "JSON" -Logger $logger
```

### 9. Module Manifest (.psd1) - RECOMMENDED

**For distribution and versioning:**

```powershell
# ModuleName.psd1

@{
    ModuleVersion = '1.0.0'
    GUID = 'unique-guid-here'
    Author = 'Your Name'
    CompanyName = 'Company Name'
    Copyright = '(c) 2025. All rights reserved.'
    Description = 'Module description'
    PowerShellVersion = '5.1'
    RequiredModules = @(
        @{ModuleName = 'Common.Core'; ModuleVersion = '1.0.0'},
        @{ModuleName = 'Common.Logging'; ModuleVersion = '1.0.0'}
    )
    FunctionsToExport = @('Get-SomethingFromModule', 'Set-SomethingInModule')
    CmdletsToExport = @()
    VariablesToExport = @()
    AliasesToExport = @()
}
```

### 10. Testing with Pester

**Module tests:**

```powershell
# Tests/ModuleName.Tests.ps1

Describe "ModuleName Tests" {
    BeforeAll {
        Import-Module "$PSScriptRoot\..\Modules\ModuleName\ModuleName.psm1" -Force
    }

    Context "Get-SomethingFromModule" {
        It "Should return success result" {
            $result = Get-SomethingFromModule -ParameterName "Test"
            $result.Success | Should -Be $true
        }

        It "Should throw on invalid input" {
            { Get-SomethingFromModule -ParameterName "" } | Should -Throw
        }
    }

    AfterAll {
        Remove-Module ModuleName -Force
    }
}
```

---

## Quick Start: Creating a New PowerShell Project

### 1. RESEARCH PHASE (MANDATORY)

```
Use context7 + grep to research:
- PowerShell module best practices
- SOLID principles in PowerShell
- PowerShell error handling patterns
- PowerShell testing with Pester
```

### 2. Create Project Structure

```powershell
# Create directory structure
New-Item -ItemType Directory -Path "ProjectRoot/Modules/Common.Core"
New-Item -ItemType Directory -Path "ProjectRoot/Modules/Common.Logging"
New-Item -ItemType Directory -Path "ProjectRoot/Modules/DomainName.Feature"
New-Item -ItemType Directory -Path "ProjectRoot/Scripts/Shared"
New-Item -ItemType Directory -Path "ProjectRoot/Scripts/DomainSpecific"
New-Item -ItemType Directory -Path "ProjectRoot/Tests"
New-Item -ItemType Directory -Path "ProjectRoot/Data"
```

### 3. Create Common.Core Module

```powershell
# Copy Common.Core.psm1 template with BaseEntity, Result, ConfigurationBase classes
# This is the foundation for ALL projects
```

### 4. Create Common.Logging Module

```powershell
# Copy Common.Logging.psm1 template with CommonLogger class
# This is MANDATORY for all projects
```

### 5. Create Domain-Specific Modules

```powershell
# Follow module template with:
# - #Requires -Version 5.1
# - Comment-based help
# - Design principles documented
# - Public and private functions regions
# - Export-ModuleMember
```

### 6. Create Orchestration Scripts

```powershell
# Scripts import modules and call functions
# Scripts do NOT contain business logic
# Business logic belongs in modules
```

### 7. Create Tests

```powershell
# Use Pester for module testing
# Test public functions
# Test error handling
```

---

## GitHub Reference Repositories

**Real-World PowerShell Module Examples:**

1. **saw-automation-projects**
   - Location: `C:\github_development\projects\saw-automation-projects`
   - Modules: 30+ modular PowerShell modules
   - Patterns: Common.* shared modules, domain-specific modules
   - Best Practices: SOLID principles, Result pattern, centralized logging

2. **PowerShell-API-Orchestrator-Toolkit**
   - Location: `C:\github_development\projects\PowerShell-API-Orchestrator-Toolkit`
   - Focus: API orchestration and automation

**Key Modules to Study:**
- `Modules/Common.Core/Common.Core.psm1` - Base classes
- `Modules/Common.Logging/Common.Logging.psm1` - Logging infrastructure
- `windows-server-storage-management/Modules/StorageAnalysis.*` - Domain modules
- `Scripts/FileAnalysis/*` - Orchestration scripts

---

## Best Practices Summary

✅ **DO:**
- Create modules (`.psm1`) for reusable functionality
- Use `Common.*` naming for shared modules
- Use `DomainName.*` naming for domain-specific modules
- Implement Result pattern for function returns
- Use centralized logging (Common.Logging)
- Inject dependencies (logger, config)
- Follow SOLID principles
- Write comment-based help for all functions
- Use `#Requires -Version 5.1`
- Create Pester tests
- Separate scripts (orchestration) from modules (logic)

❌ **DON'T:**
- Create monolithic scripts with business logic
- Hard-code dependencies
- Skip error handling
- Ignore logging
- Use generic names (avoid `Utilities`, `Helpers` without namespace)
- Put business logic in scripts (it belongs in modules)
- Skip documentation
- Ignore module versioning

---

## Integration with MCP Workflow

**When creating PowerShell modules:**

1. **Load Context**: `neo4j-memory` - Load previous PowerShell architecture decisions
2. **Research**: `context7` + `grep` - PowerShell module best practices 2025
3. **Plan**: `sequential-thinking` - Structure module organization
4. **Create**: `filesystem` - Create module files following templates
5. **Track**: `neo4j-memory` - Record module structure decisions
6. **Save**: `neo4j-memory` - Persist PowerShell patterns for future use

**Example MCP Workflow:**

```
1. neo4j-memory: "Load PowerShell module architecture from previous projects"
2. context7: "PowerShell SOLID principles module design 2025"
3. grep: "PowerShell .psm1 Result pattern github"
4. sequential-thinking: "Plan Common.Core, Common.Logging, DomainName.Feature modules"
5. filesystem: "Create module files with standard template"
6. neo4j-memory: "Save module architecture: Common.Core has BaseEntity, Result classes"
```

---

**References:**
- Production Examples: `C:\github_development\projects\saw-automation-projects`
- Module Templates: `saw-automation-projects/Modules/Common.*`
- Script Templates: `saw-automation-projects/Scripts/*`

**Skill Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** PRODUCTION READY

**Follow THE GOLDEN RULE. Research before coding. Save learnings to neo4j-memory.**
