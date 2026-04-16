from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def makefile_path(repo_root: Path) -> Path:
    return repo_root / "Makefile"


@pytest.fixture(scope="module")
def make_cmd() -> str | None:
    for candidate in ("make", "mingw32-make", "gmake"):
        if shutil.which(candidate):
            return candidate
    return None


def parse_help_targets(makefile_text: str) -> list[str]:
    return re.findall(r"^([a-zA-Z_0-9-]+):.*##", makefile_text, flags=re.MULTILINE)


def run_make(
    make_cmd: str,
    repo_root: Path,
    target: str,
    *,
    timeout: int = 60,
    dry_run: int = 1,
    force_overwrite: int = 0,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            make_cmd,
            "-s",
            target,
            f"DRY_RUN={dry_run}",
            f"FORCE_OVERWRITE={force_overwrite}",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def test_makefile_contains_expected_targets(makefile_path: Path) -> None:
    text = makefile_path.read_text(encoding="utf-8")
    targets = set(parse_help_targets(text))

    expected = {
        "help",
        "check",
        "dry-run",
        "install",
        "uninstall",
        "restow",
        "status",
        "list",
        "clean",
    }
    assert expected.issubset(targets)


def test_makefile_supports_dry_run_and_overwrite_vars(makefile_path: Path) -> None:
    text = makefile_path.read_text(encoding="utf-8")
    assert "DRY_RUN ?= 0" in text
    assert "FORCE_OVERWRITE ?= 0" in text


@pytest.mark.parametrize("target", ["help", "check", "dry-run", "list"])
def test_make_targets_smoke(
    make_cmd: str | None,
    repo_root: Path,
    target: str,
) -> None:
    if not make_cmd:
        pytest.skip("No make-compatible executable found")

    result = run_make(make_cmd, repo_root, target, dry_run=1, force_overwrite=0)
    out = f"{result.stdout}\n{result.stderr}"
    assert result.returncode == 0, f"target={target}\n{out}"
