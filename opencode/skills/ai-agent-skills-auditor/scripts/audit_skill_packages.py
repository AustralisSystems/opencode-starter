#!/usr/bin/env python3
"""Audit in-scope skill packages and optionally scaffold missing support directories."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SKILL_FILE_CANDIDATES = ("SKILL.md", "skill.md")
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


@dataclass
class Finding:
    skill: str
    severity: str
    code: str
    message: str
    location: str


@dataclass
class SkillResult:
    skill: str
    path: str
    frontmatter: Dict[str, str]
    findings: List[Finding]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skills-root",
        default="_ai_agent/.agents/skills",
        help="Root directory that contains skill package folders.",
    )
    parser.add_argument(
        "--output-dir",
        default="_ai_agent/.agents/skills/ai-agent-skills-auditor/.reports",
        help="Directory for generated JSON and Markdown reports.",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Create missing references/, scripts/, and assets/ directories.",
    )
    parser.add_argument(
        "--fail-on",
        default="high",
        choices=["none", "critical", "high", "medium", "low"],
        help="Exit non-zero when findings at or above this severity exist.",
    )
    return parser.parse_args()


def find_skill_file(skill_dir: Path) -> Optional[Path]:
    for name in SKILL_FILE_CANDIDATES:
        candidate = skill_dir / name
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    end_index: Optional[int] = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break

    if end_index is None:
        return {}, text

    frontmatter: Dict[str, str] = {}
    for line in lines[1:end_index]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")

    body = "\n".join(lines[end_index + 1 :])
    return frontmatter, body


def is_local_link(link_target: str) -> bool:
    lowered = link_target.lower()
    return not (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("#")
    )


def collect_findings(skill_dir: Path, skill_file: Path, fix: bool) -> SkillResult:
    findings: List[Finding] = []
    text = skill_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    skill_name = skill_dir.name

    if not frontmatter:
        findings.append(
            Finding(
                skill=skill_name,
                severity="high",
                code="missing_frontmatter",
                message="SKILL.md should include YAML frontmatter.",
                location=str(skill_file),
            )
        )

    name_value = frontmatter.get("name", "")
    description_value = frontmatter.get("description", "")

    if not name_value:
        findings.append(
            Finding(
                skill=skill_name,
                severity="high",
                code="missing_name",
                message="Frontmatter should include a name field.",
                location=str(skill_file),
            )
        )
    elif not NAME_PATTERN.match(name_value):
        findings.append(
            Finding(
                skill=skill_name,
                severity="medium",
                code="name_pattern",
                message="Skill name should match lowercase-hyphen format and max length expectations.",
                location=str(skill_file),
            )
        )

    if not description_value:
        findings.append(
            Finding(
                skill=skill_name,
                severity="high",
                code="missing_description",
                message="Frontmatter should include a description field.",
                location=str(skill_file),
            )
        )
    elif len(description_value) > 250:
        findings.append(
            Finding(
                skill=skill_name,
                severity="low",
                code="description_long",
                message="Description is long and may be truncated by some runtimes.",
                location=str(skill_file),
            )
        )

    body_line_count = len(body.splitlines())
    if body_line_count > 500:
        findings.append(
            Finding(
                skill=skill_name,
                severity="low",
                code="body_too_long",
                message="SKILL.md body is over 500 lines; consider progressive disclosure.",
                location=str(skill_file),
            )
        )

    for required_dir in ("references", "scripts", "assets"):
        subdir = skill_dir / required_dir
        if not subdir.exists():
            findings.append(
                Finding(
                    skill=skill_name,
                    severity="medium",
                    code=f"missing_{required_dir}",
                    message=f"Missing optional support directory: {required_dir}/",
                    location=str(skill_dir),
                )
            )
            if fix:
                subdir.mkdir(parents=True, exist_ok=True)
        elif not subdir.is_dir():
            findings.append(
                Finding(
                    skill=skill_name,
                    severity="high",
                    code=f"invalid_{required_dir}",
                    message=f"Expected {required_dir} to be a directory.",
                    location=str(subdir),
                )
            )

    for link_target in LINK_PATTERN.findall(body):
        if not is_local_link(link_target):
            continue
        local_target = (skill_dir / link_target).resolve()
        if not local_target.exists():
            findings.append(
                Finding(
                    skill=skill_name,
                    severity="medium",
                    code="broken_local_link",
                    message=f"Broken local link target in SKILL.md: {link_target}",
                    location=str(skill_file),
                )
            )

    if skill_name == "ai-agent-skills-auditor":
        expected = skill_dir / "references" / "ai-agent-skills-authoring-best-practices.md"
        if not expected.exists():
            findings.append(
                Finding(
                    skill=skill_name,
                    severity="critical",
                    code="missing_best_practices_reference",
                    message="Required best-practices reference file is missing.",
                    location=str(expected),
                )
            )

    return SkillResult(
        skill=skill_name,
        path=str(skill_dir),
        frontmatter=frontmatter,
        findings=findings,
    )


def scan_skill_packages(skills_root: Path, fix: bool) -> List[SkillResult]:
    results: List[SkillResult] = []

    if not skills_root.exists() or not skills_root.is_dir():
        raise FileNotFoundError(f"Skills root not found or not a directory: {skills_root}")

    for child in sorted(skills_root.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue

        skill_file = find_skill_file(child)
        if skill_file is None:
            continue

        results.append(collect_findings(child, skill_file, fix=fix))

    return results


def summarize(results: List[SkillResult]) -> Dict[str, int]:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for result in results:
        for finding in result.findings:
            counts[finding.severity] += 1
    counts["skill_count"] = len(results)
    return counts


def to_markdown(results: List[SkillResult], summary: Dict[str, int], skills_root: Path) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines: List[str] = []
    lines.append("# Skill Package Audit Report")
    lines.append("")
    lines.append(f"Generated: {timestamp}")
    lines.append(f"Scope root: {skills_root}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Skill packages audited: {summary['skill_count']}")
    lines.append(f"- Critical: {summary['critical']}")
    lines.append(f"- High: {summary['high']}")
    lines.append(f"- Medium: {summary['medium']}")
    lines.append(f"- Low: {summary['low']}")
    lines.append("")

    lines.append("## Findings")
    lines.append("")

    any_finding = False
    for result in results:
        if not result.findings:
            continue
        any_finding = True
        lines.append(f"### {result.skill}")
        lines.append("")
        for finding in sorted(result.findings, key=lambda f: SEVERITY_ORDER[f.severity]):
            lines.append(
                f"- [{finding.severity.upper()}] `{finding.code}`: {finding.message} ({finding.location})"
            )
        lines.append("")

    if not any_finding:
        lines.append("No findings.")
        lines.append("")

    return "\n".join(lines)


def should_fail(summary: Dict[str, int], fail_on: str) -> bool:
    if fail_on == "none":
        return False
    threshold = SEVERITY_ORDER[fail_on]
    for severity, order in SEVERITY_ORDER.items():
        if order <= threshold and summary[severity] > 0:
            return True
    return False


def main() -> int:
    args = parse_args()
    skills_root = Path(args.skills_root).resolve()
    output_dir = Path(args.output_dir).resolve()

    output_dir.mkdir(parents=True, exist_ok=True)

    results = scan_skill_packages(skills_root=skills_root, fix=args.fix)
    summary = summarize(results)

    findings_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skills_root": str(skills_root),
        "summary": summary,
        "results": [
            {
                "skill": result.skill,
                "path": result.path,
                "frontmatter": result.frontmatter,
                "findings": [asdict(item) for item in result.findings],
            }
            for result in results
        ],
    }

    json_path = output_dir / "skill_audit_report.json"
    md_path = output_dir / "skill_audit_report.md"

    json_path.write_text(json.dumps(findings_payload, indent=2), encoding="utf-8")
    md_path.write_text(to_markdown(results, summary, skills_root), encoding="utf-8")

    print(f"Wrote JSON report: {json_path}")
    print(f"Wrote Markdown report: {md_path}")
    print(
        "Summary: "
        f"critical={summary['critical']} "
        f"high={summary['high']} "
        f"medium={summary['medium']} "
        f"low={summary['low']}"
    )

    return 1 if should_fail(summary, args.fail_on) else 0


if __name__ == "__main__":
    sys.exit(main())
