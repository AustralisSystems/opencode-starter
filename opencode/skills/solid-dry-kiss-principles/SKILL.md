# SOLID, DRY, KISS Principles - Universal Design Fundamentals

**Purpose:** Apply SOLID, DRY, and KISS principles universally across ALL programming (Python, PowerShell, JavaScript, etc.)

**When to use:** ALWAYS - These principles are MANDATORY for ALL development work, ZERO EXCEPTIONS

**Critical Importance:** These principles prevent technical debt, improve maintainability, enable testing, and ensure production-ready code

---

## RFC 2119 COMPLIANCE

**All instructions in this skill MUST be interpreted according to RFC 2119** (<https://datatracker.ietf.org/doc/html/rfc2119>)

### Requirements Language Table

| Term                             | Meaning / Required Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MUST / REQUIRED / SHALL / ALWAYS | Indicates an absolute, non-negotiable requirement of this protocol. Compliance is mandatory in all cases. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                  |
| MUST NOT / SHALL NOT / NEVER     | Indicates an absolute, non-negotiable prohibition. This action, behaviour, or outcome is forbidden. No exceptions.                                                                                                                                                                                                                                                                                                                                                                                                        |
| FORBIDDEN                        | HARD MUST NOT: Indicates an action, word, pattern, code, file, or artefact that is strictly prohibited. If any item matching a FORBIDDEN rule is found in the codebase (e.g. forbidden file names like "enhanced", forbidden function names, or other banned terms, logic, or artefacts), it MUST be immediately removed, renamed, or replaced. All references MUST be updated, and remediation MUST be logged as a protocol enforcement action. No exceptions, and no warnings--violations require immediate correction. |
| SHOULD / RECOMMENDED             | Indicates a strong recommendation. There may exist valid reasons to deviate, but these should be rare and all consequences must be carefully weighed, documented, and justified.                                                                                                                                                                                                                                                                                                                                          |
| SHOULD NOT / NOT RECOMMENDED     | Indicates that the behaviour is strongly discouraged. There may exist valid reasons in particular circumstances when the behaviour is acceptable, but the full implications must be understood and documented.                                                                                                                                                                                                                                                                                                            |
| MAY / OPTIONAL                   | Indicates something that is truly optional. The choice to include or omit the feature or action is left to the implementer, without impact on overall protocol compliance.                                                                                                                                                                                                                                                                                                                                                |

### Special Notes

- **ALWAYS** = MUST (absolute, non-negotiable requirement)
- **NEVER** = MUST NOT (absolute, non-negotiable prohibition)
- **FORBIDDEN** = a hard "MUST NOT" with immediate remediation requirement
- All instructions using these words are enforceable protocol, not mere suggestions.
- No AI, LLM, or agent is permitted to relax, reinterpret, or weaken the force of these terms.

---

## 🔴 CRITICAL: MCP Tools Workflow - MANDATORY

**ALL design and implementation work MUST follow MCP workflow + SOLID/DRY/KISS - ZERO EXCEPTIONS:**

### THE GOLDEN RULE
```
context7 (docs) → grep (examples) → neo4j-memory (record) → code (SOLID/DRY/KISS) → neo4j-memory (persist)
```

### THE 6-PHASE SEQUENCE (REQUIRED)

1. **CONTEXT LOAD**: Use `neo4j-memory` to load previous SOLID/DRY/KISS decisions
2. **🔴 MANDATORY RESEARCH**: Use `context7` + `grep` BEFORE designing
   - `context7`: "SOLID principles best practices 2025"
   - `context7`: "DRY principle software engineering"
   - `grep`: "SOLID principles Python examples github"
   - `grep`: "DRY principle refactoring github"
3. **PLANNING**: Use `sequential-thinking` with SOLID/DRY/KISS principles
4. **IMPLEMENTATION**: Apply principles during coding
5. **PROGRESS TRACKING**: Record principle applications to `neo4j-memory`
6. **CONTEXT SAVE**: Persist design decisions to `neo4j-memory`

**ABSOLUTELY FORBIDDEN:**
- ❌ Violating SOLID principles (monolithic classes, tight coupling)
- ❌ Repeating code (DRY violation)
- ❌ Over-engineering solutions (KISS violation)
- ❌ Skipping neo4j-memory context load
- ❌ Ignoring established patterns from context7 + grep research

---

## Table of Contents

1. [SOLID Principles](#solid-principles)
   - Single Responsibility Principle (SRP)
   - Open/Closed Principle (OCP)
   - Liskov Substitution Principle (LSP)
   - Interface Segregation Principle (ISP)
   - Dependency Inversion Principle (DIP)
2. [DRY Principle](#dry-principle)
3. [KISS Principle](#kiss-principle)
4. [Real-World Examples](#real-world-examples)
5. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## SOLID Principles

**SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.**

### 1. Single Responsibility Principle (SRP)

**Definition:** A class/module/function should have ONE and ONLY ONE reason to change.

**In Simple Terms:** Do ONE thing and do it well.

#### Python Example (FastAPI)

**❌ BAD - Multiple Responsibilities:**

```python
class UserManager:
    """Violates SRP - handles EVERYTHING related to users."""

    def create_user(self, username: str, email: str):
        # Database logic
        user = User(username=username, email=email)
        db.add(user)
        db.commit()

        # Email logic
        smtp = smtplib.SMTP('localhost')
        msg = f"Welcome {username}!"
        smtp.sendmail('noreply@app.com', email, msg)

        # Logging logic
        with open('users.log', 'a') as f:
            f.write(f"{datetime.now()}: Created user {username}\n")

        # Validation logic
        if not self.validate_email(email):
            raise ValueError("Invalid email")

        return user
```

**WHY BAD:** UserManager has 4 reasons to change:
1. Database schema changes
2. Email service changes
3. Logging format changes
4. Validation rules changes

**✅ GOOD - Single Responsibility:**

```python
# Each class has ONE responsibility

class UserRepository:
    """ONLY handles database operations for users."""
    def create(self, user: User) -> User:
        db.add(user)
        db.commit()
        return user

class EmailService:
    """ONLY handles sending emails."""
    def send_welcome_email(self, user: User):
        smtp = smtplib.SMTP('localhost')
        msg = f"Welcome {user.username}!"
        smtp.sendmail('noreply@app.com', user.email, msg)

class UserLogger:
    """ONLY handles logging user operations."""
    def log_user_created(self, user: User):
        logger.info(f"Created user {user.username}")

class EmailValidator:
    """ONLY validates emails."""
    def validate(self, email: str) -> bool:
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

# Usage (coordinated by service layer)
class UserService:
    def __init__(
        self,
        repository: UserRepository,
        email_service: EmailService,
        logger: UserLogger,
        validator: EmailValidator
    ):
        self.repository = repository
        self.email_service = email_service
        self.logger = logger
        self.validator = validator

    def create_user(self, username: str, email: str) -> User:
        if not self.validator.validate(email):
            raise ValueError("Invalid email")

        user = User(username=username, email=email)
        user = self.repository.create(user)
        self.email_service.send_welcome_email(user)
        self.logger.log_user_created(user)

        return user
```

**WHY GOOD:**
- Each class has ONE reason to change
- Easy to test (mock individual dependencies)
- Easy to replace (swap email service implementation)
- Easy to understand (each class is focused)

#### PowerShell Example

**❌ BAD - Multiple Responsibilities:**

```powershell
Function Manage-Users {
    # Database operations
    $users = Get-ADUser -Filter *

    # Filtering logic
    $filtered = $users | Where-Object { $_.Enabled -eq $true }

    # Reporting logic
    $report = foreach ($user in $filtered) {
        [PSCustomObject]@{
            Name = $user.Name
            Email = $user.EmailAddress
        }
    }

    # Export logic
    $report | Export-Csv -Path "report.csv"

    # Email logic
    Send-MailMessage -To "admin@company.com" -Subject "User Report" -Attachments "report.csv"

    # Logging logic
    Add-Content -Path "log.txt" -Value "$(Get-Date): Generated report"
}
```

**✅ GOOD - Single Responsibility:**

```powershell
# Each function has ONE responsibility

Function Get-ActiveUsers {
    """ONLY retrieves active users from AD."""
    Get-ADUser -Filter { Enabled -eq $true }
}

Function Convert-UsersToReport {
    """ONLY converts users to report format."""
    Param([object[]]$Users)

    foreach ($user in $Users) {
        [PSCustomObject]@{
            Name = $user.Name
            Email = $user.EmailAddress
        }
    }
}

Function Export-ReportToCsv {
    """ONLY exports data to CSV."""
    Param([object[]]$Data, [string]$Path)
    $Data | Export-Csv -Path $Path -NoTypeInformation
}

Function Send-ReportEmail {
    """ONLY sends email with attachment."""
    Param([string]$AttachmentPath)
    Send-MailMessage -To "admin@company.com" -Subject "User Report" -Attachments $AttachmentPath
}

Function Write-ReportLog {
    """ONLY logs report generation."""
    Param([object]$Logger, [string]$Message)
    $Logger.LogInfo($Message)
}

# Orchestration (in script, not module)
$users = Get-ActiveUsers
$report = Convert-UsersToReport -Users $users
Export-ReportToCsv -Data $report -Path "report.csv"
Send-ReportEmail -AttachmentPath "report.csv"
Write-ReportLog -Logger $logger -Message "Generated report"
```

### 2. Open/Closed Principle (OCP)

**Definition:** Software entities should be OPEN for extension but CLOSED for modification.

**In Simple Terms:** You should be able to ADD new functionality WITHOUT changing existing code.

#### Python Example (FastAPI - Factory Pattern)

**❌ BAD - Requires Modification:**

```python
class DatabaseConnection:
    def connect(self, db_type: str):
        if db_type == "sqlite":
            return sqlite3.connect("app.db")
        elif db_type == "postgresql":
            return psycopg2.connect("postgresql://localhost/app")
        elif db_type == "mongodb":  # ❌ Had to MODIFY this class
            return pymongo.MongoClient("mongodb://localhost/")
        # Every new database requires MODIFYING this class!
```

**✅ GOOD - Open for Extension:**

```python
# Base abstraction
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Concrete implementations (can add new ones WITHOUT modifying existing)
class SQLiteConnection(DatabaseConnection):
    def connect(self):
        return sqlite3.connect("app.db")

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return psycopg2.connect("postgresql://localhost/app")

class MongoDBConnection(DatabaseConnection):
    def connect(self):
        return pymongo.MongoClient("mongodb://localhost/")

# Factory (coordin ator, follows OCP)
class DatabaseFactory:
    """Can add new database types WITHOUT modifying this class."""

    @staticmethod
    def create(db_type: str) -> DatabaseConnection:
        connections = {
            "sqlite": SQLiteConnection,
            "postgresql": PostgreSQLConnection,
            "mongodb": MongoDBConnection
        }

        if db_type not in connections:
            raise ValueError(f"Unknown database type: {db_type}")

        return connections[db_type]()

# Adding new database? Just create new class, register in factory:
class Neo4jConnection(DatabaseConnection):
    def connect(self):
        return neo4j.GraphDatabase.driver("neo4j://localhost")

# ✅ NO MODIFICATION to existing classes needed!
```

**Real-World Example from Enterprise Template:**

```python
# From fastapi-plugin-architecture-template
# Storage Factory Pattern (OPEN for extension)

class StorageProvider(ABC):
    @abstractmethod
    async def save(self, key: str, data: bytes): pass

    @abstractmethod
    async def load(self, key: str) -> bytes: pass

# Extend by adding new implementations
class SQLiteProvider(StorageProvider): ...
class PostgreSQLProvider(StorageProvider): ...
class MongoDBProvider(StorageProvider): ...
class TinyDBProvider(StorageProvider): ...  # ✅ Added without modifying existing

# Factory enables OCP
class StorageFactory:
    @staticmethod
    def create(provider_type: str, config: dict) -> StorageProvider:
        providers = {
            "sqlite": SQLiteProvider,
            "postgresql": PostgreSQLProvider,
            "mongodb": MongoDBProvider,
            "tinydb": TinyDBProvider  # ✅ Just register new type
        }
        return providers[provider_type](config)
```

#### PowerShell Example

**❌ BAD - Requires Modification:**

```powershell
Function Export-Data {
    Param([string]$Format, [object[]]$Data)

    if ($Format -eq "CSV") {
        $Data | Export-Csv -Path "output.csv"
    }
    elseif ($Format -eq "JSON") {
        $Data | ConvertTo-Json | Set-Content -Path "output.json"
    }
    elseif ($Format -eq "XML") {  # ❌ Had to MODIFY this function
        $Data | Export-Clixml -Path "output.xml"
    }
    # Every new format requires MODIFYING this function!
}
```

**✅ GOOD - Open for Extension:**

```powershell
# Base interface pattern (using classes in PowerShell 5.1+)
class DataExporter {
    [void] Export([object[]]$Data, [string]$Path) {
        throw "Must override Export method"
    }
}

class CsvExporter : DataExporter {
    [void] Export([object[]]$Data, [string]$Path) {
        $Data | Export-Csv -Path $Path -NoTypeInformation
    }
}

class JsonExporter : DataExporter {
    [void] Export([object[]]$Data, [string]$Path) {
        $Data | ConvertTo-Json | Set-Content -Path $Path
    }
}

class XmlExporter : DataExporter {  # ✅ NEW exporter, no modification to existing
    [void] Export([object[]]$Data, [string]$Path) {
        $Data | Export-Clixml -Path $Path
    }
}

# Factory
class ExporterFactory {
    static [DataExporter] Create([string]$Format) {
        $exporters = @{
            "CSV" = [CsvExporter]::new()
            "JSON" = [JsonExporter]::new()
            "XML" = [XmlExporter]::new()  # ✅ Just register new type
        }
        return $exporters[$Format]
    }
}

# Usage
$exporter = [ExporterFactory]::Create("JSON")
$exporter.Export($data, "output.json")
```

### 3. Liskov Substitution Principle (LSP)

**Definition:** Objects of a derived class should be replaceable with objects of the base class without breaking the application.

**In Simple Terms:** Subclasses must be substitutable for their base classes.

#### Python Example

**❌ BAD - Violates LSP:**

```python
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def area(self) -> int:
        return self.width * self.height

class Square(Rectangle):
    """Violates LSP - Square behavior breaks Rectangle expectations."""

    def set_width(self, width: int):
        self.width = width
        self.height = width  # ❌ Changes BOTH dimensions

    def set_height(self, height: int):
        self.width = height  # ❌ Changes BOTH dimensions
        self.height = height

# Problem:
def test_rectangle(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(4)
    assert rect.area() == 20  # Expected: 20

test_rectangle(Rectangle(0, 0))  # ✅ Works (5 * 4 = 20)
test_rectangle(Square(0))        # ❌ FAILS! (4 * 4 = 16, not 20)
```

**✅ GOOD - Follows LSP:**

```python
# Separate abstractions
class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def area(self) -> int:
        return self.side * self.side

# Both can be used interchangeably through Shape interface
def calculate_total_area(shapes: List[Shape]) -> int:
    return sum(shape.area() for shape in shapes)

shapes = [Rectangle(5, 4), Square(3), Rectangle(2, 6)]
total = calculate_total_area(shapes)  # ✅ Works for all shapes
```

**Real-World Example - Result Pattern:**

```python
# Both success and failure results are substitutable
class Result:
    @staticmethod
    def Success(data):
        return Result(success=True, data=data, error=None)

    @staticmethod
    def Failure(error):
        return Result(success=False, data=None, error=error)

# Usage - both results work the same way (LSP compliant)
result1 = Result.Success({"user": "john"})
result2 = Result.Failure("User not found")

# Can treat both identically
def handle_result(result: Result):
    if result.success:
        return result.data
    else:
        raise Exception(result.error)

handle_result(result1)  # ✅ Works
handle_result(result2)  # ✅ Works (both substitutable)
```

### 4. Interface Segregation Principle (ISP)

**Definition:** No client should be forced to depend on methods it does not use.

**In Simple Terms:** Don't force classes to implement methods they don't need.

#### Python Example

**❌ BAD - Fat Interface:**

```python
class Worker(ABC):
    """Fat interface - forces implementation of ALL methods."""

    @abstractmethod
    def work(self): pass

    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def sleep(self): pass

class HumanWorker(Worker):
    def work(self): return "Working"
    def eat(self): return "Eating"
    def sleep(self): return "Sleeping"

class RobotWorker(Worker):
    def work(self): return "Working"
    def eat(self): return None  # ❌ Robots don't eat!
    def sleep(self): return None  # ❌ Robots don't sleep!
```

**✅ GOOD - Segregated Interfaces:**

```python
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self): pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self): return "Working"
    def eat(self): return "Eating"
    def sleep(self): return "Sleeping"

class RobotWorker(Workable):
    def work(self): return "Working"
    # ✅ Only implements what it needs
```

**Real-World Example from Templates:**

```python
# Good: Segregated storage interfaces

class Readable(ABC):
    @abstractmethod
    async def read(self, path: str) -> bytes: pass

class Writable(ABC):
    @abstractmethod
    async def write(self, path: str, data: bytes): pass

class Deletable(ABC):
    @abstractmethod
    async def delete(self, path: str): pass

# Read-only storage only implements Readable
class ReadOnlyStorage(Readable):
    async def read(self, path: str) -> bytes:
        return await self._read_from_source(path)

# Full storage implements all interfaces
class FullStorage(Readable, Writable, Deletable):
    async def read(self, path: str) -> bytes: ...
    async def write(self, path: str, data: bytes): ...
    async def delete(self, path: str): ...
```

### 5. Dependency Inversion Principle (DIP)

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**In Simple Terms:** Depend on interfaces/abstractions, not concrete implementations.

#### Python Example

**❌ BAD - Direct Dependency:**

```python
class EmailNotifier:
    """Concrete implementation."""
    def send(self, message: str):
        # Send email
        pass

class UserService:
    """Depends on CONCRETE EmailNotifier."""

    def __init__(self):
        self.notifier = EmailNotifier()  # ❌ Hard-coded dependency

    def register_user(self, user: User):
        # ... register logic
        self.notifier.send(f"Welcome {user.username}!")
        # ❌ Can't switch to SMS without modifying this class
```

**✅ GOOD - Dependency Injection:**

```python
# Abstraction
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str): pass

# Concrete implementations
class EmailNotifier(Notifier):
    def send(self, message: str):
        # Send email
        pass

class SMSNotifier(Notifier):
    def send(self, message: str):
        # Send SMS
        pass

class UserService:
    """Depends on ABSTRACTION (Notifier interface)."""

    def __init__(self, notifier: Notifier):  # ✅ Dependency injection
        self.notifier = notifier

    def register_user(self, user: User):
        # ... register logic
        self.notifier.send(f"Welcome {user.username}!")
        # ✅ Works with ANY Notifier implementation

# Usage (DI container configures dependencies)
email_notifier = EmailNotifier()
user_service = UserService(notifier=email_notifier)

# Easy to swap implementations
sms_notifier = SMSNotifier()
user_service = UserService(notifier=sms_notifier)  # ✅ No code changes needed
```

#### PowerShell Example

**❌ BAD - Hard-coded Dependency:**

```powershell
Function Process-Data {
    # ❌ Hard-coded dependency on specific logger
    $logger = New-FileLogger -Path "C:\logs\app.log"

    $logger.LogInfo("Processing data")
    # ... processing logic
}
```

**✅ GOOD - Dependency Injection:**

```powershell
Function Process-Data {
    Param(
        [Parameter(Mandatory=$true)]
        [object]$Logger  # ✅ Injected dependency (abstraction)
    )

    $Logger.LogInfo("Processing data")
    # ... processing logic
}

# Usage (caller provides dependency)
$fileLogger = New-FileLogger -Path "C:\logs\app.log"
Process-Data -Logger $fileLogger

# Easy to swap
$consoleLogger = New-ConsoleLogger
Process-Data -Logger $consoleLogger  # ✅ No function changes needed
```

**Real-World Example from PowerShell Modules:**

```powershell
# Good: Dependency injection in modules

Function Get-UserReport {
    Param(
        [Parameter(Mandatory=$true)]
        [object]$Logger,  # ✅ Injected

        [Parameter(Mandatory=$true)]
        [object]$Config   # ✅ Injected
    )

    $Logger.LogInfo("Generating user report")
    $threshold = $Config.GetSetting("UserThreshold")

    # ... report logic
}

# Caller provides dependencies
$logger = Initialize-Logger "UserReports"
$config = Get-Configuration "UserApp"
Get-UserReport -Logger $logger -Config $config
```

---

## DRY Principle (Don't Repeat Yourself)

**Definition:** Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**In Simple Terms:** Don't copy-paste code. Extract common functionality.

### Python Example

**❌ BAD - Code Repetition:**

```python
# Repeated validation logic
def create_user(username: str, email: str):
    if not username or len(username) < 3:
        raise ValueError("Invalid username")
    if not email or '@' not in email:
        raise ValueError("Invalid email")
    # ... create user

def update_user(user_id: int, username: str, email: str):
    if not username or len(username) < 3:  # ❌ REPEATED
        raise ValueError("Invalid username")
    if not email or '@' not in email:  # ❌ REPEATED
        raise ValueError("Invalid email")
    # ... update user
```

**✅ GOOD - DRY:**

```python
# Extract validation into reusable function
def validate_username(username: str):
    if not username or len(username) < 3:
        raise ValueError("Invalid username")

def validate_email(email: str):
    if not email or '@' not in email:
        raise ValueError("Invalid email")

def create_user(username: str, email: str):
    validate_username(username)  # ✅ Reuse
    validate_email(email)          # ✅ Reuse
    # ... create user

def update_user(user_id: int, username: str, email: str):
    validate_username(username)  # ✅ Reuse
    validate_email(email)          # ✅ Reuse
    # ... update user
```

### PowerShell Example

**❌ BAD - Code Repetition:**

```powershell
Function Get-UserReport {
    $users = Get-ADUser -Filter *

    # ❌ Repeated filtering logic
    $activeUsers = $users | Where-Object {
        $_.Enabled -eq $true -and
        $_.PasswordNeverExpires -eq $false -and
        $_.LastLogonDate -gt (Get-Date).AddDays(-90)
    }

    # ... report logic
}

Function Get-UserCount {
    $users = Get-ADUser -Filter *

    # ❌ SAME filtering logic repeated
    $activeUsers = $users | Where-Object {
        $_.Enabled -eq $true -and
        $_.PasswordNeverExpires -eq $false -and
        $_.LastLogonDate -gt (Get-Date).AddDays(-90)
    }

    return $activeUsers.Count
}
```

**✅ GOOD - DRY:**

```powershell
# Extract filtering into reusable function
Function Get-ActiveUsers {
    [CmdletBinding()]
    [OutputType([object[]])]
    Param()

    $users = Get-ADUser -Filter * -Properties LastLogonDate

    return $users | Where-Object {
        $_.Enabled -eq $true -and
        $_.PasswordNeverExpires -eq $false -and
        $_.LastLogonDate -gt (Get-Date).AddDays(-90)
    }
}

Function Get-UserReport {
    $activeUsers = Get-ActiveUsers  # ✅ Reuse
    # ... report logic
}

Function Get-UserCount {
    $activeUsers = Get-ActiveUsers  # ✅ Reuse
    return $activeUsers.Count
}
```

---

## KISS Principle (Keep It Simple, Stupid)

**Definition:** Most systems work best if they are kept simple rather than made complicated.

**In Simple Terms:** Don't over-engineer. Simplest solution that works is often the best.

### Example: Over-Engineered vs Simple

**❌ BAD - Over-Engineered:**

```python
# Over-engineered: Factory + Builder + Strategy + Observer for simple config
class ConfigBuilder:
    def __init__(self):
        self.config = {}

    def with_setting(self, key, value):
        self.config[key] = value
        return self

    def build(self):
        return Config(self.config)

class ConfigFactory:
    @staticmethod
    def create_builder():
        return ConfigBuilder()

class ConfigStrategy(ABC):
    @abstractmethod
    def load_config(self): pass

class JSONConfigStrategy(ConfigStrategy):
    def load_config(self):
        return json.load(open('config.json'))

class ConfigObserver:
    def __init__(self):
        self.listeners = []

    def attach(self, listener):
        self.listeners.append(listener)

    def notify(self, config):
        for listener in self.listeners:
            listener.on_config_change(config)

# Usage requires understanding 4 patterns!
builder = ConfigFactory.create_builder()
config = builder.with_setting("key", "value").build()
strategy = JSONConfigStrategy()
loaded_config = strategy.load_config()
observer = ConfigObserver()
observer.attach(my_listener)
# ❌ Way too complex for simple config loading!
```

**✅ GOOD - KISS:**

```python
# Simple: Just load config
def load_config(path: str = "config.json") -> dict:
    """Load configuration from JSON file."""
    with open(path) as f:
        return json.load(f)

# Usage is obvious
config = load_config()  # ✅ Simple and clear
```

**When to Use Patterns:**

- ✅ Factory Pattern: When you need runtime selection of implementations
- ✅ Builder Pattern: When object construction is complex with many optional parameters
- ❌ Don't use patterns "just because" - use them when they solve a real problem

---

## Real-World Examples

### Example 1: Database Factory (from Enterprise Template)

**Applies SOLID + DRY:**

```python
# From fastapi-plugin-architecture-template

# SRP: Each provider handles ONE database type
class SQLiteProvider:
    def connect(self): ...

class PostgreSQLProvider:
    def connect(self): ...

# OCP: Can add new providers without modifying existing
class MongoDBProvider:  # ✅ NEW provider, no modification to existing
    def connect(self): ...

# DIP: Factory depends on abstraction, not concrete implementations
class DatabaseFactory:
    """Depends on provider interface, not concrete classes."""

    @staticmethod
    def create(db_type: str, config: dict):
        providers = {
            "sqlite": SQLiteProvider,
            "postgresql": PostgreSQLProvider,
            "mongodb": MongoDBProvider
        }
        return providers[db_type](config)

# DRY: Connection logic in factory, not repeated in every service
db = DatabaseFactory.create("postgresql", config)  # ✅ Reuse factory
```

### Example 2: PowerShell Common Modules (from saw-automation-projects)

**Applies SOLID + DRY:**

```powershell
# SRP: Each module has ONE responsibility

# Common.Core - ONLY base classes
class Result { ... }
class BaseEntity { ... }

# Common.Logging - ONLY logging
class CommonLogger { ... }

# Common.Configuration - ONLY configuration
class ConfigurationBase { ... }

# DRY: Shared modules prevent code duplication
# Instead of repeating Result pattern in every script:

# Script 1
Import-Module Common.Core  # ✅ Reuse Result class
$result = [Result]::Success($data)

# Script 2
Import-Module Common.Core  # ✅ Reuse Result class
$result = [Result]::Failure("Error")

# ✅ NO CODE DUPLICATION - DRY achieved through modules
```

### Example 3: REST API Orchestrator (KISS in Action)

**From rest-api-orchestrator:**

```python
# KISS: Simple credential storage (encrypted, but not over-engineered)

class CredentialManager:
    """Simple, focused credential management."""

    def encrypt(self, credential: str, password: str) -> bytes:
        """One method, one purpose."""
        # AES-256-GCM encryption
        # Returns encrypted bytes
        # ✅ Simple and clear

    def decrypt(self, encrypted: bytes, password: str) -> str:
        """One method, one purpose."""
        # AES-256-GCM decryption
        # Returns plaintext
        # ✅ Simple and clear

# NOT over-engineered with:
# - Abstract credential strategies
# - Multiple encryption algorithm factories
# - Complex key derivation builders
# ✅ KISS: Just does what's needed, nothing more
```

---

## Anti-Patterns to Avoid

### 1. God Class/Function (Violates SRP)

**❌ BAD:**

```python
class Application:
    """Does EVERYTHING - violates SRP."""

    def run(self):
        # Database logic
        db = self.connect_database()

        # Authentication logic
        user = self.authenticate_user()

        # Business logic
        data = self.process_data()

        # Reporting logic
        report = self.generate_report(data)

        # Email logic
        self.send_email(report)
```

**✅ GOOD:** Split into focused classes (UserService, ReportService, EmailService, etc.)

### 2. Copy-Paste Programming (Violates DRY)

**❌ BAD:**

```python
# Same validation repeated 10 times across different functions
def create_user(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):  # ❌ Repeated
        raise ValueError("Invalid email")

def update_user(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):  # ❌ Repeated
        raise ValueError("Invalid email")
```

**✅ GOOD:** Extract validation function

### 3. Premature Abstraction (Violates KISS)

**❌ BAD:**

```python
# Over-abstraction for simple task
class AbstractUserFactoryBuilder:
    pass

class ConcreteUserFactoryBuilderStrategy:
    pass

# Just to create a user object!
```

**✅ GOOD:** Start simple, add abstraction when needed

### 4. Tight Coupling (Violates DIP)

**❌ BAD:**

```python
class UserService:
    def __init__(self):
        self.db = PostgreSQLDatabase()  # ❌ Hard-coded dependency
        self.email = SMTPEmailService()  # ❌ Hard-coded dependency
```

**✅ GOOD:** Inject dependencies

---

## Quick Reference Checklist

**Before writing code, ask:**

- [ ] **SRP**: Does this class/function do ONE thing?
- [ ] **OCP**: Can I add features without modifying existing code?
- [ ] **LSP**: Can derived classes substitute base classes?
- [ ] **ISP**: Are interfaces focused (not fat)?
- [ ] **DIP**: Am I depending on abstractions, not concrete classes?
- [ ] **DRY**: Am I repeating code that should be extracted?
- [ ] **KISS**: Is this the simplest solution that works?

**Red flags:**

- ❌ Class with > 5 public methods (likely SRP violation)
- ❌ Function with > 50 lines (likely SRP violation)
- ❌ Copy-pasted code (DRY violation)
- ❌ if/elif chains for type checking (OCP violation)
- ❌ Hard-coded dependencies (DIP violation)
- ❌ Complex abstractions for simple problems (KISS violation)

---

## Integration with MCP Workflow

**When applying SOLID/DRY/KISS:**

1. **Load Context**: `neo4j-memory` - "Load SOLID/DRY/KISS decisions from previous projects"
2. **Research**: `context7` - "SOLID principles best practices 2025"
3. **Research**: `grep` - "SOLID principles Python examples github"
4. **Plan**: `sequential-thinking` - "Plan class hierarchy following SOLID"
5. **Implement**: Apply principles during coding
6. **Track**: `neo4j-memory` - "Record: Used factory pattern for database providers (OCP)"
7. **Save**: `neo4j-memory` - "Persist: Extracted validation to reusable function (DRY)"

---

**Skill Version:** 1.0.0
**Last Updated:** 2025-10-22
**Status:** MANDATORY FOR ALL DEVELOPMENT

**Follow THE GOLDEN RULE + SOLID/DRY/KISS:**
```
context7 → grep → neo4j-memory → code (SOLID/DRY/KISS) → neo4j-memory
```

**These principles are NON-NEGOTIABLE. Apply them to ALL code, ALWAYS.**
