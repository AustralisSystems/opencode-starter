from __future__ import annotations

import itertools
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest


SCRIPT_FLAGS = [
    "--no-update",
    "--update",
    "--skip-make",
    "--dry-run",
    "--overwrite",
    "--uninstall",
    "--force",
]


@pytest.fixture(scope="module")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def install_script(repo_root: Path) -> Path:
    return repo_root / "scripts" / "install.sh"


@pytest.fixture(scope="module")
def bash_exe() -> str:
    bash_path = shutil.which("bash")
    if not bash_path:
        pytest.skip("bash is required to execute install.sh tests")
    return bash_path


def run_install(
    bash_exe: str,
    repo_root: Path,
    install_script: Path,
    *args: str,
    timeout: int = 120,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [bash_exe, str(install_script), *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def combined_output(result: subprocess.CompletedProcess[str]) -> str:
    return f"{result.stdout}\n{result.stderr}"


def test_help_lists_expected_options(bash_exe: str, repo_root: Path, install_script: Path) -> None:
    result = run_install(bash_exe, repo_root, install_script, "--help")
    out = combined_output(result)

    assert result.returncode == 0
    assert "Usage:" in out
    for flag in SCRIPT_FLAGS:
        assert flag in out


def test_unknown_argument_fails_fast(bash_exe: str, repo_root: Path, install_script: Path) -> None:
    result = run_install(bash_exe, repo_root, install_script, "--not-a-real-flag")
    out = combined_output(result)

    assert result.returncode != 0
    assert "Unknown argument" in out


@pytest.mark.parametrize(
    "args",
    [
        ("--dry-run", "--skip-make"),
        ("--dry-run", "--uninstall", "--skip-make"),
        ("--dry-run", "--force", "--skip-make"),
        ("--dry-run", "--overwrite", "--skip-make"),
    ],
)
def test_safe_modes_succeed(
    bash_exe: str,
    repo_root: Path,
    install_script: Path,
    args: tuple[str, ...],
) -> None:
    result = run_install(bash_exe, repo_root, install_script, *args)
    out = combined_output(result)

    assert result.returncode == 0
    assert "[DRY-RUN]" in out


def test_force_sets_overwrite_state_in_log(
    bash_exe: str, repo_root: Path, install_script: Path
) -> None:
    result = run_install(bash_exe, repo_root, install_script, "--dry-run", "--force", "--skip-make")
    out = combined_output(result)

    assert result.returncode == 0
    # The script logs a state line like: overwrite=1 ... force=1
    assert re.search(r"overwrite=1", out)
    assert re.search(r"force=1", out)


@pytest.mark.slow
def test_full_flag_matrix_in_dry_run_mode(
    bash_exe: str, repo_root: Path, install_script: Path
) -> None:
    if os.getenv("RUN_FULL_INSTALL_MATRIX") != "1":
        pytest.skip("Set RUN_FULL_INSTALL_MATRIX=1 to run all 128 combinations")

    for include in itertools.product([False, True], repeat=len(SCRIPT_FLAGS)):
        selected = [flag for flag, enabled in zip(SCRIPT_FLAGS, include) if enabled]
        effective = list(selected)
        if "--dry-run" not in effective:
            effective.append("--dry-run")

        result = run_install(
            bash_exe,
            repo_root,
            install_script,
            *effective,
            timeout=180,
        )
        assert result.returncode == 0, (
            f"Combination failed: {selected}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
