# PowerShell Skills Suite - Quick Reference

**Date:** 2025-10-22
**Status:** PRODUCTION READY
**Purpose:** Comprehensive PowerShell development skills with MCP workflow enforcement

---

## Skills Overview

### 1. powershell-module-architecture
**Purpose:** Design and implement modular, reusable PowerShell modules

**Key Topics:**
- Modular design patterns (Modules vs Scripts)
- Naming conventions (Common.*, DomainName.*)
- SOLID principles in PowerShell
- Result pattern for error handling
- Common.Core base classes (BaseEntity, Result, ConfigurationBase)
- Common.Logging centralized logging
- Project structure templates

**When to use:**
- Creating new PowerShell projects
- Structuring reusable modules
- Implementing shared functionality

### 2. powershell-design
**Purpose:** Design PowerShell scripts and modules using best practices

**Key Topics:**
- Module vs Script decision making
- Function design patterns (Verb-Noun convention)
- Parameter validation and pipeline support
- Error handling design (Result pattern)
- Dependency injection patterns
- Logging and configuration design
- Design for testability

**When to use:**
- Before implementing PowerShell solutions
- Planning module architecture
- Designing function interfaces

### 3. powershell-implement
**Purpose:** Implement PowerShell modules following best practices

**Key Topics:**
- Comment-based help
- Parameter attributes and validation
- Pipeline support implementation
- Error handling with try-catch-finally
- Logging integration
- Performance optimization
- Security best practices

**When to use:**
- Writing PowerShell functions
- Implementing module business logic
- Creating orchestration scripts

### 4. powershell-quality
**Purpose:** Test and validate PowerShell code quality

**Key Topics:**
- Pester testing framework
- Unit testing modules
- Integration testing
- Code analysis with PSScriptAnalyzer
- Code coverage
- Performance testing

**When to use:**
- Testing PowerShell modules
- Validating code quality
- Running automated tests

### 5. powershell-refactor
**Purpose:** Improve existing PowerShell code

**Key Topics:**
- Refactoring monolithic scripts to modules
- Improving error handling
- Adding logging
- Implementing Result pattern
- Performance optimization
- Code smell identification

**When to use:**
- Improving existing PowerShell code
- Converting scripts to modules
- Optimizing performance

---

## MCP Workflow (MANDATORY for ALL Skills)

**THE GOLDEN RULE:**
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

**6-PHASE SEQUENCE:**
1. CONTEXT LOAD (`neo4j-memory`)
2. 🔴 MANDATORY RESEARCH (`context7` + `grep`)
3. PLANNING (`sequential-thinking`)
4. IMPLEMENTATION (`filesystem`)
5. PROGRESS TRACKING (`neo4j-memory`)
6. CONTEXT SAVE (`neo4j-memory`)

---

## Quick Start Guide

### Creating a New PowerShell Project

**1. Research Phase (MANDATORY):**
```
context7: "PowerShell module best practices 2025"
context7: "PowerShell SOLID principles"
grep: "PowerShell .psm1 Result pattern github"
grep: "PowerShell module structure examples github"
```

**2. Create Project Structure:**
```powershell
ProjectRoot/
├── Modules/
│   ├── Common.Core/        # Base classes, Result pattern
│   ├── Common.Logging/     # Centralized logging
│   └── DomainName.Feature/ # Domain-specific logic
├── Scripts/                # Orchestration scripts
├── Tests/                  # Pester tests
└── Data/                   # Application data
```

**3. Create Common.Core Module:**
```powershell
# Common.Core.psm1 with BaseEntity, Result, ConfigurationBase classes
# This is MANDATORY for all projects
```

**4. Create Domain Modules:**
```powershell
# Follow module template from powershell-module-architecture skill
```

**5. Create Orchestration Scripts:**
```powershell
# Scripts import modules and call functions
# Scripts do NOT contain business logic
```

---

## Best Practices Summary

### ✅ DO:
- Create modules (`.psm1`) for reusable functionality
- Use `Common.*` for shared modules, `DomainName.*` for domain-specific
- Follow Verb-Noun naming convention for functions
- Implement Result pattern for error handling
- Use centralized logging (Common.Logging)
- Inject dependencies (logger, config)
- Write comment-based help for all functions
- Use `#Requires -Version 5.1`
- Create Pester tests
- Separate scripts (orchestration) from modules (business logic)

### ❌ DON'T:
- Create monolithic scripts with business logic
- Hard-code dependencies
- Skip error handling
- Ignore logging
- Use plural nouns in function names
- Put business logic in scripts
- Skip documentation
- Ignore module versioning

---

## Real-World References

**Production PowerShell Repositories:**

1. **saw-automation-projects**
   - Location: `C:\github_development\projects\saw-automation-projects`
   - Modules: 30+ modular PowerShell modules
   - Patterns: Common.* shared modules, domain-specific modules
   - Examples: StorageAnalysis.*, SoftwareManagement.*, SafeCleanup.*

2. **PowerShell-API-Orchestrator-Toolkit**
   - Location: `C:\github_development\projects\PowerShell-API-Orchestrator-Toolkit`
   - Focus: API orchestration and automation

**Key Files to Study:**
- `Modules/Common.Core/Common.Core.psm1` - Base classes (BaseEntity, Result)
- `Modules/Common.Logging/Common.Logging.psm1` - Logging infrastructure
- `windows-server-storage-management/Modules/StorageAnalysis.Core/` - Domain modules
- `Scripts/FileAnalysis/Get-StorageFileScan.ps1` - Orchestration example

---

## Module Templates

### Common.Core Template

```powershell
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
}

class Result {
    [bool] $Success
    [object] $Data
    [string] $ErrorMessage
    [System.Exception] $Exception
    [hashtable] $Metadata

    static [Result] Success([object]$data) {
        return [Result]::new($true, $data, $null)
    }

    static [Result] Failure([string]$errorMessage) {
        return [Result]::new($false, $null, $errorMessage)
    }
}
```

### Function Template

```powershell
Function Get-ModuleFunction {
    <#
    .SYNOPSIS
        Brief description

    .DESCRIPTION
        Detailed description

    .PARAMETER ParameterName
        Parameter description

    .EXAMPLE
        Get-ModuleFunction -ParameterName "Value"

    .OUTPUTS
        Result object with Success and Data properties
    #>
    [CmdletBinding()]
    [OutputType([Result])]
    Param(
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$ParameterName,

        [Parameter(Mandatory=$true)]
        [object]$Logger
    )

    begin {
        Write-Verbose "Starting $($MyInvocation.MyCommand)"
        $Logger.LogInfo("Starting operation")
    }

    process {
        try {
            # Implementation
            $result = # ... do work

            $Logger.LogInfo("Operation successful")
            return [Result]::Success($result)
        }
        catch {
            $Logger.LogError("Operation failed: $_")
            return [Result]::Failure("Operation failed", $_)
        }
    }

    end {
        Write-Verbose "Completed $($MyInvocation.MyCommand)"
    }
}
```

---

## Skill Usage Matrix

| Task | Use This Skill | MCP Research Focus |
|------|---------------|-------------------|
| Plan new PowerShell project | `powershell-module-architecture` | Module structure patterns |
| Design module functions | `powershell-design` | Function design best practices |
| Write PowerShell code | `powershell-implement` | PowerShell coding standards |
| Test PowerShell modules | `powershell-quality` | Pester testing patterns |
| Improve existing code | `powershell-refactor` | Refactoring techniques |

---

## Integration with Python/FastAPI Skills

**PowerShell and Python Complement Each Other:**

| PowerShell | Python/FastAPI |
|-----------|---------------|
| Windows automation | Web APIs and services |
| Active Directory | Database operations |
| File system operations | Data processing |
| Registry management | REST API endpoints |
| Remote management | Async processing |

**Combined Example:**
```
PowerShell script → Calls FastAPI REST endpoint → FastAPI processes data → Returns JSON → PowerShell displays results
```

**Both Follow Same MCP Workflow:**
- Research with context7 + grep
- Result/Result pattern for error handling
- Modular architecture (modules vs monolithic)
- Centralized logging
- Configuration management
- SOLID principles

---

## Common Patterns Across Skills

### 1. Result Pattern (from Common.Core)
```powershell
$result = Get-SomeData
if ($result.Success) {
    # Use $result.Data
} else {
    # Handle $result.ErrorMessage
}
```

### 2. Logger Injection
```powershell
Function Do-Something {
    Param([object]$Logger)
    $Logger.LogInfo("Doing something")
}
```

### 3. Configuration Injection
```powershell
Function Do-Something {
    Param([object]$Config)
    $setting = $Config.GetSetting("SettingName")
}
```

### 4. Module Import Pattern
```powershell
#Requires -Version 5.1

Import-Module "$PSScriptRoot\..\Common.Core\Common.Core.psm1" -ErrorAction Stop
Import-Module "$PSScriptRoot\..\Common.Logging\Common.Logging.psm1" -ErrorAction Stop
```

---

## Troubleshooting

**Common Issues:**

1. **Module not found**
   - Check module path is correct
   - Use absolute paths with `$PSScriptRoot`
   - Ensure `-ErrorAction Stop` to catch import errors

2. **Result pattern not working**
   - Ensure Common.Core module is imported
   - Check class definition is loaded
   - Verify using `[Result]::Success()` static methods

3. **Logger not logging**
   - Ensure Common.Logging module is imported
   - Check logger instance is initialized
   - Verify logger is passed to functions

4. **Functions not exported**
   - Add `Export-ModuleMember -Function FunctionName`
   - Check function is in `#region Public Functions`

---

## Next Steps

1. **Review Skills:** Read each skill's SKILL.md for detailed guidance
2. **Study Examples:** Explore saw-automation-projects repository
3. **Practice MCP Workflow:** Use context7 + grep before coding
4. **Build Projects:** Create modular PowerShell solutions
5. **Save Learnings:** Use neo4j-memory to persist patterns

---

**Document Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** PRODUCTION READY
**Compliance:** MANDATORY MCP workflow enforcement

**Follow THE GOLDEN RULE for ALL PowerShell work:**
```
context7 → grep → neo4j-memory → code → neo4j-memory
```
