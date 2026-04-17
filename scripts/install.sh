#!/usr/bin/env bash
set -euo pipefail

# Cross-platform prerequisite installer for opencode_starter.
# Installs and updates: git, node.js/npm, make, stow, pre-commit, opencode-ai.

SCRIPT_NAME="$(basename "$0")"
AUTO_UPDATE=1
RUN_MAKE=1
DRY_RUN=0
FORCE_OVERWRITE=0
FORCE_MODE=0
UNINSTALL_MODE=0
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
TARGET_CONFIG_DIR="${HOME}/.config/opencode"

normalize_path() {
  local p="$1"
  if command -v cygpath >/dev/null 2>&1 && [[ "$(uname -s)" =~ MINGW|MSYS|CYGWIN ]]; then
    cygpath -u "$p"
  else
    printf '%s' "$p"
  fi
}

TARGET_CONFIG_DIR="$(normalize_path "${TARGET_CONFIG_DIR}")"
MANAGED_CONFIG_PACKAGES=(agent command mcp plugin rules skill themes)
WINGET_STOW_IDS=(GNU.Stow GnuWin32.Stow)

print_usage() {
  cat <<EOF
Usage: $SCRIPT_NAME [--no-update] [--update] [--skip-make] [--dry-run] [--overwrite] [--uninstall] [--force]

Options:
  --no-update   Install missing prerequisites only, do not upgrade existing ones
  --update      Install missing prerequisites and upgrade existing ones (default)
  --skip-make   Do not run 'make install' after prerequisites are ready
  --dry-run     Print planned actions without changing system state
  --overwrite   Force-overwrite existing destination files during make install
  --uninstall   Remove opencode config content and uninstall managed packages
  --force       In install mode: reinstall packages and overwrite config. In uninstall mode: brute-force deletion/removal.
  -h, --help    Show this help message
EOF
}

log() {
  printf '[INFO] %s\n' "$*"
}

warn() {
  printf '[WARN] %s\n' "$*" >&2
}

err() {
  printf '[ERROR] %s\n' "$*" >&2
}

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

find_make_cmd() {
  local candidate=""
  for candidate in make mingw32-make gmake; do
    if has_cmd "$candidate"; then
      echo "$candidate"
      return 0
    fi
  done
  return 1
}

add_windows_make_paths() {
  local candidate=""
  local added=0

  for candidate in \
    "/c/Program Files (x86)/GnuWin32/bin" \
    "/c/Program Files/Git/usr/bin" \
    "/mingw64/bin" \
    "/usr/bin"
  do
    if [[ -d "$candidate" && ":$PATH:" != *":$candidate:"* ]]; then
      PATH="$PATH:$candidate"
      added=1
    fi
  done

  if [[ "$added" -eq 1 ]]; then
    log "Extended PATH in current shell with common Windows make locations"
  fi
}

run_cmd() {
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "[DRY-RUN] $*"
    return 0
  fi
  log "$*"
  "$@"
}

detect_os() {
  case "$(uname -s)" in
    Darwin*)
      echo "macos"
      ;;
    Linux*)
      echo "linux"
      ;;
    MINGW*|MSYS*|CYGWIN*)
      echo "windows"
      ;;
    *)
      echo "unknown"
      ;;
  esac
}

ensure_npm_global_package() {
  local pkg="$1"
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    if npm list -g --depth=0 "$pkg" >/dev/null 2>&1; then
      run_cmd npm uninstall -g "$pkg" || true
    fi
    run_cmd npm install -g "$pkg"
    return 0
  fi

  if npm list -g --depth=0 "$pkg" >/dev/null 2>&1; then
    if [[ "$AUTO_UPDATE" -eq 1 ]]; then
      run_cmd npm install -g "$pkg"
    else
      log "npm package already installed globally: $pkg"
    fi
  else
    run_cmd npm install -g "$pkg"
  fi
}

remove_npm_global_package() {
  local pkg="$1"
  if ! has_cmd npm; then
    warn "npm not found; could not uninstall npm package: $pkg"
    return 0
  fi

  if npm list -g --depth=0 "$pkg" >/dev/null 2>&1; then
    run_cmd npm uninstall -g "$pkg" || true
  else
    log "npm package not installed globally: $pkg"
  fi
}

install_precommit_via_pip() {
  local py_cmd=""
  if has_cmd python3; then
    py_cmd="python3"
  elif has_cmd python; then
    py_cmd="python"
  else
    warn "Python not found, could not install pre-commit"
    return 0
  fi

  if [[ "$FORCE_MODE" -eq 1 ]]; then
    if has_cmd pre-commit; then
      run_cmd "$py_cmd" -m pip uninstall -y pre-commit || true
    fi
    run_cmd "$py_cmd" -m pip install --user pre-commit
    return 0
  fi

  if has_cmd pre-commit; then
    if [[ "$AUTO_UPDATE" -eq 1 ]]; then
      run_cmd "$py_cmd" -m pip install --user --upgrade pre-commit
    else
      log "pre-commit already installed"
    fi
  else
    run_cmd "$py_cmd" -m pip install --user pre-commit
  fi
}

remove_precommit_via_pip() {
  local py_cmd=""
  if has_cmd python3; then
    py_cmd="python3"
  elif has_cmd python; then
    py_cmd="python"
  else
    warn "Python not found, could not uninstall pre-commit"
    return 0
  fi

  if has_cmd pre-commit; then
    run_cmd "$py_cmd" -m pip uninstall -y pre-commit || true
  else
    log "pre-commit not installed"
  fi
}

install_macos() {
  if ! has_cmd brew; then
    err "Homebrew is required on macOS. Install from https://brew.sh and re-run."
    exit 1
  fi

  run_cmd brew update
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd brew reinstall git node stow pre-commit make || run_cmd brew install git node stow pre-commit make
  else
    run_cmd brew install git node stow pre-commit make

    if [[ "$AUTO_UPDATE" -eq 1 ]]; then
      run_cmd brew upgrade git node stow pre-commit make || true
    fi
  fi

  if ! has_cmd make; then
    # GNU make installs as gmake on macOS via Homebrew.
    run_cmd brew install make || true
    warn "Installed GNU make as 'gmake'. macOS may still use BSD 'make'."
  fi

  ensure_npm_global_package opencode-ai
}

install_linux_apt() {
  run_cmd sudo apt-get update
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo apt-get install --reinstall -y git nodejs npm stow make python3 python3-pip
  else
    run_cmd sudo apt-get install -y git nodejs npm stow make python3 python3-pip
  fi
  if [[ "$AUTO_UPDATE" -eq 1 && "$FORCE_MODE" -eq 0 ]]; then
    run_cmd sudo apt-get install --only-upgrade -y git nodejs npm stow make python3 python3-pip || true
  fi
}

install_linux_dnf() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo dnf reinstall -y git nodejs npm stow make python3 python3-pip || run_cmd sudo dnf install -y git nodejs npm stow make python3 python3-pip
  else
    run_cmd sudo dnf install -y git nodejs npm stow make python3 python3-pip
  fi
  if [[ "$AUTO_UPDATE" -eq 1 && "$FORCE_MODE" -eq 0 ]]; then
    run_cmd sudo dnf upgrade -y git nodejs npm stow make python3 python3-pip || true
  fi
}

install_linux_yum() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo yum reinstall -y git nodejs npm stow make python3 python3-pip || run_cmd sudo yum install -y git nodejs npm stow make python3 python3-pip
  else
    run_cmd sudo yum install -y git nodejs npm stow make python3 python3-pip
  fi
  if [[ "$AUTO_UPDATE" -eq 1 && "$FORCE_MODE" -eq 0 ]]; then
    run_cmd sudo yum update -y git nodejs npm stow make python3 python3-pip || true
  fi
}

install_linux_pacman() {
  run_cmd sudo pacman -Sy --noconfirm git nodejs npm stow make python python-pip
  if [[ "$AUTO_UPDATE" -eq 1 && "$FORCE_MODE" -eq 0 ]]; then
    run_cmd sudo pacman -S --noconfirm git nodejs npm stow make python python-pip || true
  fi
}

install_linux_zypper() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo zypper --non-interactive install --force git nodejs npm stow make python3 python3-pip
  else
    run_cmd sudo zypper --non-interactive install git nodejs npm stow make python3 python3-pip
  fi
  if [[ "$AUTO_UPDATE" -eq 1 && "$FORCE_MODE" -eq 0 ]]; then
    run_cmd sudo zypper --non-interactive update git nodejs npm stow make python3 python3-pip || true
  fi
}

install_linux() {
  if has_cmd apt-get; then
    install_linux_apt
  elif has_cmd dnf; then
    install_linux_dnf
  elif has_cmd yum; then
    install_linux_yum
  elif has_cmd pacman; then
    install_linux_pacman
  elif has_cmd zypper; then
    install_linux_zypper
  else
    err "Unsupported Linux package manager. Install prerequisites manually."
    exit 1
  fi

  install_precommit_via_pip
  ensure_npm_global_package opencode-ai
}

uninstall_linux_apt() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo apt-get purge -y git nodejs npm stow make || true
    run_cmd sudo apt-get autoremove -y || true
  else
    run_cmd sudo apt-get remove -y git nodejs npm stow make || true
  fi
}

uninstall_linux_dnf() {
  run_cmd sudo dnf remove -y git nodejs npm stow make || true
}

uninstall_linux_yum() {
  run_cmd sudo yum remove -y git nodejs npm stow make || true
}

uninstall_linux_pacman() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    run_cmd sudo pacman -Rns --noconfirm git nodejs npm stow make || true
  else
    run_cmd sudo pacman -R --noconfirm git nodejs npm stow make || true
  fi
}

uninstall_linux_zypper() {
  run_cmd sudo zypper --non-interactive rm git nodejs npm stow make || true
}

uninstall_linux() {
  if has_cmd apt-get; then
    uninstall_linux_apt
  elif has_cmd dnf; then
    uninstall_linux_dnf
  elif has_cmd yum; then
    uninstall_linux_yum
  elif has_cmd pacman; then
    uninstall_linux_pacman
  elif has_cmd zypper; then
    uninstall_linux_zypper
  else
    warn "Unsupported Linux package manager. Skipping system package uninstall."
  fi

  remove_precommit_via_pip
  remove_npm_global_package opencode-ai
}

winget_install() {
  local id="$1"
  run_cmd winget install --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity
}

winget_upgrade() {
  local id="$1"
  run_cmd winget upgrade --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity || true
}

winget_reinstall() {
  local id="$1"
  run_cmd winget install --id "$id" -e --force --accept-source-agreements --accept-package-agreements --disable-interactivity || true
}

winget_uninstall() {
  local id="$1"
  run_cmd winget uninstall --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity || true
}

winget_install_any() {
  local mode="$1"
  shift

  local id=""
  for id in "$@"; do
    case "$mode" in
      install)
        if run_cmd winget install --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity; then
          return 0
        fi
        ;;
      reinstall)
        if run_cmd winget install --id "$id" -e --force --accept-source-agreements --accept-package-agreements --disable-interactivity; then
          return 0
        fi
        ;;
      upgrade)
        if run_cmd winget upgrade --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity; then
          return 0
        fi
        ;;
      uninstall)
        if run_cmd winget uninstall --id "$id" -e --accept-source-agreements --accept-package-agreements --disable-interactivity; then
          return 0
        fi
        ;;
      *)
        err "Unsupported winget_install_any mode: $mode"
        return 1
        ;;
    esac
  done

  return 1
}

install_windows() {
  if has_cmd winget; then
    if [[ "$FORCE_MODE" -eq 1 ]]; then
      winget_reinstall Git.Git
      winget_reinstall OpenJS.NodeJS.LTS
      winget_reinstall GnuWin32.Make
      winget_reinstall Python.Python.3.12
    else
      if has_cmd git; then
        [[ "$AUTO_UPDATE" -eq 1 ]] && winget_upgrade Git.Git
      else
        winget_install Git.Git || true
      fi

      if has_cmd node; then
        [[ "$AUTO_UPDATE" -eq 1 ]] && winget_upgrade OpenJS.NodeJS.LTS
      else
        winget_install OpenJS.NodeJS.LTS || true
      fi

      if has_cmd make; then
        [[ "$AUTO_UPDATE" -eq 1 ]] && winget_upgrade GnuWin32.Make
      else
        winget_install GnuWin32.Make || true
      fi

      if has_cmd python; then
        [[ "$AUTO_UPDATE" -eq 1 ]] && winget_upgrade Python.Python.3.12
      else
        winget_install Python.Python.3.12 || true
      fi
    fi
  else
    warn "winget not found; trying alternative package managers"
  fi

  if [[ "$FORCE_MODE" -eq 1 ]]; then
    if has_cmd winget; then
      if ! winget_install_any reinstall "${WINGET_STOW_IDS[@]}"; then
        warn "Could not force-reinstall stow via winget using known IDs (${WINGET_STOW_IDS[*]})."
      fi
    elif has_cmd choco; then
      run_cmd choco uninstall stow -y --no-progress || true
      run_cmd choco install stow -y --no-progress || true
    elif has_cmd scoop; then
      run_cmd scoop uninstall stow || true
      run_cmd scoop install stow || true
    else
      warn "Could not force-reinstall stow on Windows (winget/choco/scoop unavailable for stow)."
    fi
  elif ! has_cmd stow; then
    if has_cmd winget; then
      if ! winget_install_any install "${WINGET_STOW_IDS[@]}"; then
        warn "Could not install stow via winget using known IDs (${WINGET_STOW_IDS[*]})."
      fi
    elif has_cmd choco; then
      run_cmd choco install stow -y --no-progress || true
    elif has_cmd scoop; then
      run_cmd scoop install stow || true
    else
      warn "Could not auto-install stow on Windows (winget/choco/scoop unavailable for stow)."
    fi
  elif [[ "$AUTO_UPDATE" -eq 1 ]]; then
    if has_cmd winget; then
      winget_install_any upgrade "${WINGET_STOW_IDS[@]}" || true
    elif has_cmd choco; then
      run_cmd choco upgrade stow -y --no-progress || true
    elif has_cmd scoop; then
      run_cmd scoop update stow || true
    fi
  fi

  install_precommit_via_pip

  if has_cmd npm; then
    ensure_npm_global_package opencode-ai
  else
    warn "npm not found; could not install opencode-ai"
  fi

  if [[ -d "/c/Program Files (x86)/GnuWin32/bin" ]]; then
    warn "If make is still not found in this shell, add C:\\Program Files (x86)\\GnuWin32\\bin to PATH or open a new terminal session."
  fi

  add_windows_make_paths

  if ! find_make_cmd >/dev/null 2>&1; then
    warn "No make-compatible command detected after install attempts (make/mingw32-make/gmake)."
  fi
}

uninstall_windows() {
  remove_precommit_via_pip
  remove_npm_global_package opencode-ai

  if has_cmd winget; then
    winget_uninstall Git.Git
    winget_uninstall OpenJS.NodeJS.LTS
    winget_uninstall GnuWin32.Make
    winget_uninstall Python.Python.3.12
    winget_install_any uninstall "${WINGET_STOW_IDS[@]}" || true
  else
    warn "winget not found; skipping winget package uninstall"
  fi

  if has_cmd choco; then
    run_cmd choco uninstall stow -y --no-progress || true
  fi
  if has_cmd scoop; then
    run_cmd scoop uninstall stow || true
  fi
}

uninstall_macos() {
  if has_cmd brew; then
    if [[ "$FORCE_MODE" -eq 1 ]]; then
      run_cmd brew uninstall --ignore-dependencies git node stow pre-commit make || true
    else
      run_cmd brew uninstall git node stow pre-commit make || true
    fi
  else
    warn "Homebrew not found; skipping system package uninstall"
  fi

  remove_precommit_via_pip
  remove_npm_global_package opencode-ai
}

print_summary() {
  printf '\nInstall summary:\n'
  for tool in git node npm stow pre-commit opencode; do
    if has_cmd "$tool"; then
      printf '  [OK] %s -> %s\n' "$tool" "$(command -v "$tool")"
    else
      printf '  [MISSING] %s\n' "$tool"
    fi
  done

  local make_cmd=""
  if make_cmd="$(find_make_cmd)"; then
    printf '  [OK] make-compatible -> %s (%s)\n' "$make_cmd" "$(command -v "$make_cmd")"
  else
    printf '  [MISSING] make-compatible (make/mingw32-make/gmake)\n'
  fi
}

run_default_make_install() {
  if [[ "$RUN_MAKE" -eq 0 ]]; then
    log "Skipping make install (--skip-make)"
    return 0
  fi

  local make_cmd=""
  if ! make_cmd="$(find_make_cmd)"; then
    if [[ "$DRY_RUN" -eq 1 ]]; then
      warn "No make-compatible command in PATH during dry-run; skipping make install preview"
      return 0
    fi
    err "No make-compatible command available (make/mingw32-make/gmake); cannot apply config install"
    return 1
  fi

  if [[ ! -f "$PROJECT_ROOT/Makefile" ]]; then
    warn "No Makefile found at $PROJECT_ROOT; skipping make install"
    return 0
  fi

  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "Running $make_cmd install dry run in $PROJECT_ROOT"
    "$make_cmd" -C "$PROJECT_ROOT" install DRY_RUN=1 "FORCE_OVERWRITE=$FORCE_OVERWRITE" "TARGET=$TARGET_CONFIG_DIR"
  else
    log "Running $make_cmd install in $PROJECT_ROOT"
    run_cmd "$make_cmd" -C "$PROJECT_ROOT" install "FORCE_OVERWRITE=$FORCE_OVERWRITE" "TARGET=$TARGET_CONFIG_DIR"
  fi
}

run_default_make_uninstall() {
  local make_cmd=""
  if make_cmd="$(find_make_cmd)" && [[ -f "$PROJECT_ROOT/Makefile" ]]; then
    if [[ "$DRY_RUN" -eq 1 ]]; then
      log "Running $make_cmd uninstall dry run in $PROJECT_ROOT"
      "$make_cmd" -C "$PROJECT_ROOT" uninstall DRY_RUN=1
    else
      log "Running $make_cmd uninstall in $PROJECT_ROOT"
      run_cmd "$make_cmd" -C "$PROJECT_ROOT" uninstall
    fi
    return 0
  fi

  warn "make or Makefile not available; falling back to direct content removal in $TARGET_CONFIG_DIR"
  for package in "${MANAGED_CONFIG_PACKAGES[@]}"; do
    local target_link="$TARGET_CONFIG_DIR/$package"
    if [[ ! -e "$target_link" && ! -L "$target_link" ]]; then
      continue
    fi

    if [[ -L "$target_link" ]]; then
      run_cmd rm -f "$target_link"
      continue
    fi

    if [[ "$FORCE_MODE" -eq 1 ]]; then
      warn "Force-removing non-symlink managed path: $target_link"
      run_cmd rm -rf "$target_link"
      continue
    fi

    warn "Removing non-symlink managed path during uninstall: $target_link"
    run_cmd rm -rf "$target_link"
  done
}

bruteforce_remove_config_dir() {
  if [[ "$FORCE_MODE" -eq 1 ]]; then
    if [[ "$DRY_RUN" -eq 1 ]]; then
      log "[DRY-RUN] rm -rf \"$TARGET_CONFIG_DIR\""
    else
      log "Brute-force removing config directory: $TARGET_CONFIG_DIR"
      rm -rf "$TARGET_CONFIG_DIR"
    fi
  fi
}

run_uninstall_flow() {
  run_default_make_uninstall
  bruteforce_remove_config_dir

  case "$1" in
    macos)
      uninstall_macos
      ;;
    linux)
      uninstall_linux
      ;;
    windows)
      uninstall_windows
      ;;
    *)
      err "Unsupported OS for uninstall flow: $1"
      exit 1
      ;;
  esac
}

main() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --no-update)
        AUTO_UPDATE=0
        ;;
      --update)
        AUTO_UPDATE=1
        ;;
      --skip-make)
        RUN_MAKE=0
        ;;
      --dry-run)
        DRY_RUN=1
        ;;
      --overwrite)
        FORCE_OVERWRITE=1
        ;;
      --uninstall)
        UNINSTALL_MODE=1
        ;;
      --force)
        FORCE_MODE=1
        FORCE_OVERWRITE=1
        ;;
      -h|--help)
        print_usage
        exit 0
        ;;
      *)
        err "Unknown argument: $1"
        print_usage
        exit 1
        ;;
    esac
    shift
  done

  local os
  os="$(detect_os)"
  log "Detected OS: $os (auto-update=$AUTO_UPDATE, dry-run=$DRY_RUN, overwrite=$FORCE_OVERWRITE, uninstall=$UNINSTALL_MODE, force=$FORCE_MODE)"

  if [[ "$UNINSTALL_MODE" -eq 1 ]]; then
    run_uninstall_flow "$os"
    print_summary
    exit 0
  fi

  case "$os" in
    macos)
      install_macos
      ;;
    linux)
      install_linux
      ;;
    windows)
      install_windows
      ;;
    *)
      err "Unsupported OS: $os"
      exit 1
      ;;
  esac

  run_default_make_install

  print_summary
}

main "$@"
