<div align="center">
  <a href="https://opencode.ai"><img src="opencode-logo.png" alt="Opencode logo"></a>
</div>

<p align="center">
    <strong>Jumpstart your Opencode environment with this pre-built configuration. It includes a variety of agents, commands, skills, themes and MCP servers definitions, all ready for you to use and customize. Spend less time configuring and more time automating.</strong>
</p>

<p align="center">
    <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
    <a href="https://github.com/jjmartres/opencode"><img src="https://img.shields.io/github/last-commit/jjmartres/opencode?label=Last%20update&style=flat-square" alt="Last Update" /></a>
    <a href="https://github.com/jjmartres/opencode/issues"><img src="https://img.shields.io/github/issues/jjmartres/opencode" alt="GitHub Issues"/></a>
    <a href="https://github.com/jjmartres/opencode/pulls"><img src="https://img.shields.io/github/issues-pr/jjmartres/opencode" alt="GitHub Pull Requests"/></a>
</p>

---

## Table of Contents

- [Features](#features)
- [Documentation](#documentation)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration Structure](#configuration-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Agents**: Specialized AI agents for various domains (payment integration, customer success, etc.)
- **Skills**: Reusable skill definitions for common workflows
- **MCP Servers**: Model Context Protocol server configurations
- **Rules**: Coding rules and best practices
- **Themes**: Custom themes for OpenCode
- **Automated Installation**: Uses GNU Stow or symlinks for easy deployment
- **Pre-commit Hooks**: Automatic validation and linting

## Documentation

- **[Agents](./docs/AGENTS.md)**: Detailed list of all available AI agents.
- **[Commands](./docs/COMMANDS.md)**: Comprehensive list of all available commands.
- **[Skills](./docs/SKILLS.md)**: Detailed list of all available skills.
- **[Rules](./docs/RULES.md)**: Coding rules and best practices.

## Prerequisites

- Bash-compatible shell (Git Bash, WSL, or Linux/macOS shell)
- Internet access for package installation
- Admin/sudo permissions (recommended for system package installs)

### Installing Prerequisites

Use the installer script (recommended):

```bash
./scripts/install.sh
```

By default, the script installs missing tools, updates existing ones, and runs `make install`. To install only missing tools without upgrades:

```bash
./scripts/install.sh --no-update
```

If you only want prerequisite setup and do not want it to run the Makefile:

```bash
./scripts/install.sh --skip-make
```

If destination files already exist and you want to force overwrite during install:

```bash
./scripts/install.sh --overwrite
```

If you want a full force cycle (reinstall packages and overwrite config content):

```bash
./scripts/install.sh --force
```

To uninstall config content and remove managed packages:

```bash
./scripts/install.sh --uninstall
```

To brute-force uninstall (aggressive content deletion + package removal):

```bash
./scripts/install.sh --uninstall --force
```

To preview actions without changing anything:

```bash
./scripts/install.sh --dry-run
```

You can preview the force cycle without changing anything:

```bash
./scripts/install.sh --dry-run --force
```

You can also preview uninstall behavior without changing anything:

```bash
./scripts/install.sh --dry-run --uninstall
./scripts/install.sh --dry-run --uninstall --force
```

The script handles OS detection and installs prerequisites for this submodule, including:

- `git`
- `node` / `npm`
- `make`
- `stow`
- `pre-commit`
- `opencode-ai`

If the script is not executable yet:

```bash
chmod +x ./scripts/install.sh
```

## Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/jjmartres/opencode.git
cd opencode

# Install prerequisites
./scripts/install.sh

# (Optional) Install pre-commit hooks
make install-hooks
```

### What Gets Installed

The installation process creates symlinks from this repository to `~/.config/opencode/`:

```
~/.config/opencode/
├── agent/      -> ~/opencode/opencode/agent/
├── command/    -> ~/opencode/opencode/command/
├── mcp/        -> ~/opencode/opencode/mcp/
├── plugin/     -> ~/opencode/opencode/plugin/
├── rules/      -> ~/opencode/opencode/rules/
├── skill/      -> ~/opencode/opencode/skill/
└── themes/     -> ~/opencode/opencode/themes/
```

### Installation Methods

The Makefile automatically detects if GNU Stow is available:

- **With Stow**: Uses `stow` for proper symlink management
- **Without Stow**: Falls back to `ln -s` for direct symlinks

During install, existing non-symlink destination files are detected as conflicts by default. Use force overwrite only when you intentionally want to replace existing files.

## Usage

### Basic Commands

```bash
# Open current directory in OpenCode
opencode .

# Open specific file
opencode path/to/file.py

# Check installation status
make status

# List available packages
make list

# Update configuration (after pulling changes)
make restow
```

### Available Make Targets

```bash
make help                    # Display all available commands
make install                 # Install OpenCode configuration
make install FORCE_OVERWRITE=1  # Install and replace existing destination files
make install-force           # Shortcut for forced overwrite install
make uninstall              # Remove configuration symlinks
make restow                 # Refresh symlinks (after updates)
make dry-run                # Preview install actions without changing files
make status                 # Show installation status
make list                   # List available packages
make clean                  # Remove broken symlinks

# Pre-commit Hooks
make install-hooks          # Install pre-commit hooks
make run-hooks             # Run hooks manually
make update-hooks          # Update hooks to latest versions

# Combined Operations
make install-all           # Install config + hooks
make uninstall-all         # Remove everything
```

## Configuration Structure

```
opencode/
├── agent/                 # AI agent definitions
│   ├── 01-core/
│   ├── 02-languages/
│   ├── 03-infrastructure/
│   ├── 04-quality-and-security/
│   ├── 05-data-ai/
│   ├── 06-developer-experience/
│   ├── 07-specialized-domains/
│   ├── 08-business-product/
│   ├── 09-meta-orchestration/
│   └── 10-curiosity/
├── command/              # Custom commands
├── mcp/                  # MCP server configurations
├── rules/                # Coding rules and standards
├── skill/                # Reusable skills
│   ├── mcp-builder/
│   ├── content-research-writer/
│   └── meeting-insights-analyzer/
└── themes/               # UI themes
```

## Development

### Making Changes

1. Edit files in the `opencode/` directory
2. Changes are immediately reflected (symlinks!)
3. Restart OpenCode if needed

### Running Pre-commit Hooks

```bash
# Run all hooks on all files
make run-hooks

# Run specific hook
pre-commit run markdownlint --all-files

# Skip hooks for a commit (not recommended)
git commit --no-verify -m "message"
```

### Updating Configuration

```bash
# Pull latest changes
git pull origin main

# Refresh symlinks
make restow
```

## Troubleshooting

### Configuration Not Loading

```bash
# Check installation status
make status

# Verify symlinks
ls -la ~/.config/opencode/

# Reinstall
make uninstall
make install
```

### Stow Conflicts

```bash
# If you get conflicts, remove existing files first
rm -rf ~/.config/opencode/agent  # Repeat for other directories

# Then reinstall
make install
```

### Pre-commit Hooks Failing

```bash
# Run hooks manually to see errors
make run-hooks

# Update hooks
make update-hooks

# Uninstall/reinstall hooks
make uninstall-hooks
make install-hooks
```

## Contributing

Contributions are welcome! We appreciate bug reports, feature suggestions, new agents/skills, and documentation improvements.

Please read our [Contributing Guidelines](CONTRIBUTING.md) for:

- How to report bugs
- How to suggest enhancements
- Development workflow and pull request process
- Coding standards and pre-commit requirements
- Testing procedures

**Quick Start for Contributors:**

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/opencode.git
cd opencode

# Install with development hooks
make install
make install-hooks

# Make changes and test
make run-hooks
make status

# Submit a pull request!
```

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

- [OpenCode](https://opencode.ai) - The AI-powered code editor
- [GNU Stow](https://www.gnu.org/software/stow/) - Symlink farm manager
- All our [contributors](https://github.com/jjmartres/opencode/graphs/contributors)

## Support

- **Issues**: [GitHub Issues](https://github.com/jjmartres/opencode/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jjmartres/opencode/discussions)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Note**: This configuration is tailored for personal use. Feel free to fork and customize for your needs!
