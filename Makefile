.DEFAULT_GOAL := help
STOW_DIR := opencode
TARGET ?= $(HOME)/.config/opencode
TARGET := $(abspath $(TARGET))
STOW := $(shell command -v stow 2>/dev/null)
DRY_RUN ?= 0
FORCE_OVERWRITE ?= 0
STOW_PACKAGES := $(patsubst $(STOW_DIR)/%/,%,$(wildcard $(STOW_DIR)/*/))
STOW_BASE_ARGS := -d $(STOW_DIR) -t $(TARGET)
ROOT_CONFIG_FILES := $(wildcard $(STOW_DIR)/*.jsonc)
ROOT_CONFIG_NAMES := $(notdir $(ROOT_CONFIG_FILES))
MANAGED_FILE_MARKER_SUFFIX := .opencode-managed-file

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Installation

.PHONY: check
check: ## Verify setup
	@test -d $(STOW_DIR) || (echo "Error: $(STOW_DIR) directory not found" && exit 1)
ifdef STOW
	@echo "✓ Using stow: $(STOW)"
	@test -f .stowrc || (echo "Warning: .stowrc not found")
else
	@echo "⚠ stow not found - will use ln -s instead"
endif
	@echo "✓ Setup verified"

.PHONY: dry-run
dry-run: ## Preview install actions without changing files
	@"$(MAKE)" -s install DRY_RUN=1

.PHONY: install-force
install-force: ## Install and force-overwrite existing destination files
	@"$(MAKE)" -s install FORCE_OVERWRITE=1 DRY_RUN=$(DRY_RUN)

.PHONY: preflight-targets
preflight-targets: ## Detect destination conflicts before install
	@conflicts=0; \
	for dir in $(STOW_DIR)/*/; do \
		package=$$(basename "$$dir"); \
		target_link="$(TARGET)/$$package"; \
		if [ -e "$$target_link" ] && [ ! -L "$$target_link" ]; then \
			if [ -f "$$target_link/.opencode-managed-copy" ]; then \
				continue; \
			fi; \
			if [ "$(FORCE_OVERWRITE)" = "1" ]; then \
				if [ "$(DRY_RUN)" = "1" ]; then \
					echo "  [DRY-RUN] rm -rf \"$$target_link\""; \
				else \
					echo "  ! Force-overwriting existing destination: $$target_link"; \
					rm -rf "$$target_link"; \
				fi; \
			else \
				echo "  ✗ $$package destination exists and is not a symlink: $$target_link"; \
				conflicts=1; \
			fi; \
		fi; \
	done; \
	for file in $(ROOT_CONFIG_NAMES); do \
		target_file="$(TARGET)/$$file"; \
		managed_marker="$(TARGET)/.$$file$(MANAGED_FILE_MARKER_SUFFIX)"; \
		if [ -e "$$target_file" ] && [ ! -L "$$target_file" ] && [ ! -f "$$managed_marker" ]; then \
			if [ "$(FORCE_OVERWRITE)" = "1" ]; then \
				if [ "$(DRY_RUN)" = "1" ]; then \
					echo "  [DRY-RUN] rm -f \"$$target_file\""; \
				else \
					echo "  ! Force-overwriting existing destination: $$target_file"; \
					rm -f "$$target_file"; \
				fi; \
			else \
				echo "  ✗ config destination exists and is not managed: $$target_file"; \
				conflicts=1; \
			fi; \
		fi; \
	done; \
	if [ "$$conflicts" -eq 1 ]; then \
		echo "Conflict(s) detected. Re-run with FORCE_OVERWRITE=1 (or make install-force) to replace existing destinations."; \
		exit 1; \
	fi

.PHONY: install-root-files
install-root-files: ## Install root-level config files (internal)
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] mkdir -p $(TARGET)"; \
	else \
		mkdir -p $(TARGET); \
	fi
	@for src_file in $(ROOT_CONFIG_FILES); do \
		config_name=$$(basename "$$src_file"); \
		target_file="$(TARGET)/$$config_name"; \
		managed_marker="$(TARGET)/.$$config_name$(MANAGED_FILE_MARKER_SUFFIX)"; \
		if [ -e "$$target_file" ] && [ ! -L "$$target_file" ] && [ ! -f "$$managed_marker" ]; then \
			if [ "$(FORCE_OVERWRITE)" = "1" ]; then \
				if [ "$(DRY_RUN)" = "1" ]; then \
					echo "  [DRY-RUN] rm -f \"$$target_file\""; \
				else \
					rm -f "$$target_file"; \
				fi; \
			else \
				echo "  ✗ $$config_name exists and is not managed - skipping"; \
				continue; \
			fi; \
		fi; \
		if [ "$(DRY_RUN)" = "1" ]; then \
			echo "  [DRY-RUN] ln -sfn \"$(CURDIR)/$$src_file\" \"$$target_file\""; \
			echo "  [DRY-RUN] fallback copy if symlink unsupported"; \
		else \
			if ln -sfn "$(CURDIR)/$$src_file" "$$target_file" 2>/dev/null && [ -L "$$target_file" ]; then \
				rm -f "$$managed_marker"; \
				echo "  [OK] $$config_name (symlink)"; \
			else \
				cp -f "$(CURDIR)/$$src_file" "$$target_file"; \
				touch "$$managed_marker"; \
				echo "  [OK] $$config_name (managed copy)"; \
			fi; \
		fi; \
	done

.PHONY: install
install: check ## Install opencode configuration
	@"$(MAKE)" -s preflight-targets FORCE_OVERWRITE=$(FORCE_OVERWRITE) DRY_RUN=$(DRY_RUN)
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] mkdir -p $(TARGET)"; \
	else \
		mkdir -p $(TARGET); \
	fi
ifdef STOW
	@echo "Installing with stow..."
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] stow $(STOW_BASE_ARGS) -R $(STOW_PACKAGES)"; \
	else \
		stow $(STOW_BASE_ARGS) -R $(STOW_PACKAGES) || (echo "✗ Stow failed - check for conflicts" && exit 1); \
	fi
else
	@echo "Installing with ln -s..."
	@"$(MAKE)" -s install-ln DRY_RUN=$(DRY_RUN)
endif
	@"$(MAKE)" -s install-root-files FORCE_OVERWRITE=$(FORCE_OVERWRITE) DRY_RUN=$(DRY_RUN)
	@echo "✓ Installation complete"

.PHONY: install-ln
install-ln: ## Install using ln -s (internal)
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] mkdir -p $(TARGET)"; \
	else \
		mkdir -p $(TARGET); \
	fi
	@for dir in $(STOW_DIR)/*/; do \
		package=$$(basename "$$dir"); \
		target_link="$(TARGET)/$$package"; \
		if [ -e "$$target_link" ] && [ ! -L "$$target_link" ]; then \
			if [ -f "$$target_link/.opencode-managed-copy" ]; then \
				if [ "$(DRY_RUN)" = "1" ]; then \
					echo "  [DRY-RUN] refresh managed copy \"$$target_link\""; \
				else \
					rm -rf "$$target_link"; \
					mkdir -p "$$target_link"; \
					cp -R "$(CURDIR)/$$dir." "$$target_link/"; \
					touch "$$target_link/.opencode-managed-copy"; \
					echo "  [OK] $$package (managed copy)"; \
				fi; \
				continue; \
			fi; \
			if [ "$(FORCE_OVERWRITE)" = "1" ]; then \
				if [ "$(DRY_RUN)" = "1" ]; then \
					echo "  [DRY-RUN] rm -rf \"$$target_link\""; \
				else \
					echo "  ! Force-overwriting existing destination: $$target_link"; \
					rm -rf "$$target_link"; \
				fi; \
			else \
				echo "  ✗ $$package exists and is not a symlink - skipping"; \
				continue; \
			fi; \
		fi; \
		if [ "$(DRY_RUN)" = "1" ]; then \
			echo "  [DRY-RUN] ln -sfn \"$(CURDIR)/$$dir\" \"$$target_link\""; \
			echo "  [DRY-RUN] fallback copy if symlink unsupported"; \
		else \
			if ln -sfn "$(CURDIR)/$$dir" "$$target_link" 2>/dev/null && [ -L "$$target_link" ]; then \
				echo "  [OK] $$package (symlink)"; \
			else \
				rm -rf "$$target_link"; \
				mkdir -p "$$target_link"; \
				cp -R "$(CURDIR)/$$dir." "$$target_link/"; \
				touch "$$target_link/.opencode-managed-copy"; \
				echo "  [OK] $$package (managed copy)"; \
			fi; \
		fi; \
	done

.PHONY: uninstall
uninstall: ## Uninstall opencode configuration
ifdef STOW
	@echo "Uninstalling with stow..."
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] stow $(STOW_BASE_ARGS) -D $(STOW_PACKAGES)"; \
	else \
		stow $(STOW_BASE_ARGS) -D $(STOW_PACKAGES) 2>/dev/null || true; \
	fi
else
	@echo "Removing symlinks..."
	@"$(MAKE)" -s uninstall-ln DRY_RUN=$(DRY_RUN)
endif
	@"$(MAKE)" -s uninstall-root-files DRY_RUN=$(DRY_RUN)
	@echo "✓ Uninstallation complete"

.PHONY: uninstall-ln
uninstall-ln: ## Uninstall using rm (internal)
	@for dir in $(STOW_DIR)/*/; do \
		package=$$(basename "$$dir"); \
		target_link="$(TARGET)/$$package"; \
		if [ -L "$$target_link" ]; then \
			if [ "$(DRY_RUN)" = "1" ]; then \
				echo "  [DRY-RUN] rm -f \"$$target_link\""; \
			else \
				echo "  Removing $$package..."; \
				rm -f "$$target_link"; \
			fi; \
		elif [ -d "$$target_link" ] && [ -f "$$target_link/.opencode-managed-copy" ]; then \
			if [ "$(DRY_RUN)" = "1" ]; then \
				echo "  [DRY-RUN] rm -rf \"$$target_link\""; \
			else \
				echo "  Removing $$package managed copy..."; \
				rm -rf "$$target_link"; \
			fi; \
		fi; \
	done

.PHONY: uninstall-root-files
uninstall-root-files: ## Uninstall root-level config files (internal)
	@for file in $(ROOT_CONFIG_NAMES); do \
		target_file="$(TARGET)/$$file"; \
		managed_marker="$(TARGET)/.$$file$(MANAGED_FILE_MARKER_SUFFIX)"; \
		if [ -L "$$target_file" ]; then \
			if [ "$(DRY_RUN)" = "1" ]; then \
				echo "  [DRY-RUN] rm -f \"$$target_file\""; \
			else \
				rm -f "$$target_file"; \
			fi; \
			if [ "$(DRY_RUN)" = "1" ]; then \
				echo "  [DRY-RUN] rm -f \"$$managed_marker\""; \
			else \
				rm -f "$$managed_marker"; \
			fi; \
		elif [ -f "$$target_file" ] && [ -f "$$managed_marker" ]; then \
			if [ "$(DRY_RUN)" = "1" ]; then \
				echo "  [DRY-RUN] rm -f \"$$target_file\" \"$$managed_marker\""; \
			else \
				rm -f "$$target_file" "$$managed_marker"; \
			fi; \
		fi; \
	done

.PHONY: restow
restow: ## Restow opencode configuration
ifdef STOW
	@echo "Restowing with stow..."
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] stow $(STOW_BASE_ARGS) -R $(STOW_PACKAGES)"; \
	else \
		stow $(STOW_BASE_ARGS) -R $(STOW_PACKAGES) || (echo "✗ Restow failed - check for conflicts" && exit 1); \
	fi
else
	@echo "Refreshing symlinks..."
	@"$(MAKE)" -s uninstall-ln install-ln DRY_RUN=$(DRY_RUN)
endif
	@"$(MAKE)" -s install-root-files FORCE_OVERWRITE=$(FORCE_OVERWRITE) DRY_RUN=$(DRY_RUN)
	@echo "✓ Restow complete"

##@ Utilities

.PHONY: status
status: ## Show installation status
	@echo "Installation method: $(if $(STOW),stow,ln -s)"
	@echo "Target: $(TARGET)"
	@echo ""
	@echo "Installed packages:"
	@if [ -d "$(TARGET)" ]; then \
		for link in $(TARGET)/*; do \
			if [ -L "$$link" ]; then \
				target=$$(readlink "$$link"); \
				echo "  ✓ $$(basename $$link) -> $$target"; \
			elif [ -e "$$link" ]; then \
				echo "  ⚠ $$(basename $$link) (not a symlink)"; \
			fi; \
		done | sort; \
	else \
		echo "  Not installed"; \
	fi

.PHONY: list
list: ## List available packages
	@echo "Available packages:"
	@ls -d $(STOW_DIR)/*/ 2>/dev/null | sed 's|$(STOW_DIR)/||g; s|/$$||' | sed 's/^/  /' || echo "  None found"

.PHONY: clean
clean: ## Remove broken symlinks in target
	@echo "Cleaning broken symlinks in $(TARGET)..."
	@if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[DRY-RUN] find $(TARGET) -xtype l -delete"; \
	else \
		find $(TARGET) -xtype l -delete 2>/dev/null || true; \
	fi
	@echo "✓ Cleanup complete"

.PHONY: install-all
install-all: install ## Install everything
	@echo ""
	@echo "✓ Complete installation finished"

.PHONY: uninstall-all
uninstall-all: uninstall ## Uninstall everything
	@echo ""
	@echo "✓ Complete uninstallation finished"

##@ Pre-commit hooks
.PHONY: install-hooks
install-hooks: ## Install pre-commit hooks
	@command -v pre-commit >/dev/null 2>&1 || \
		(echo "❌ pre-commit not installed. Install with: pip install pre-commit" && exit 1)
	@pre-commit install
	@echo "✓ Pre-commit hooks installed"

.PHONY: uninstall-hooks
uninstall-hooks: ## Uninstall pre-commit hooks
	@pre-commit uninstall
	@echo "✓ Pre-commit hooks uninstalled"

.PHONY: run-hooks
run-hooks: ## Run pre-commit hooks manually
	@pre-commit run --all-files

.PHONY: update-hooks
update-hooks: ## Update pre-commit hooks to latest versions
	@pre-commit autoupdate
	@echo "✓ Pre-commit hooks updated"
