import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger("ai_agent_query_skills")


class QuerySkill:
    """
    [AI AGENT SKILL] Manages persistence of AI Agent tool results for context conservation.
    Standardizes output to _temp/ai_agent/.
    """

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.temp_root = repo_root / "_temp" / "ai_agent"
        self._ensure_temp_root()

    def _ensure_temp_root(self):
        if not self.temp_root.exists():
            self.temp_root.mkdir(parents=True, exist_ok=True)

    def _slugify(self, text: str) -> str:
        """Creates a safe filename slug from text."""
        return "".join([c if c.isalnum() else "_" for c in text]).strip("_")[:30]

    def create_run_dir(self, tool_name: str, query: str) -> Path:
        """
        Creates a unique directory for a tool run.
        Format: [tool]/[YYYYMMDD_HHMMSS]_[query_slug]
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        slug = self._slugify(query)
        run_dir = self.temp_root / tool_name / f"{timestamp}_{slug}"
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir

    def persist_results(self, run_dir: Path, metadata: dict[str, Any], results: list[Any]) -> Path:
        """Saves results and metadata to the run directory."""
        meta_path = run_dir / "meta.json"
        data_path = run_dir / "results.json"

        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        return run_dir

    def list_runs(self, tool_name: str | None = None) -> list[dict[str, Any]]:
        """Lists available persisted runs."""
        runs = []
        search_path = self.temp_root / tool_name if tool_name else self.temp_root

        if not search_path.exists():
            return []

        for p in search_path.rglob("meta.json"):
            try:
                with open(p, encoding="utf-8") as f:
                    meta = json.load(f)
                    meta["id"] = p.parent.name
                    meta["path"] = str(p.parent)
                    runs.append(meta)
            except Exception as e:
                logger.warning(f"Could not read meta at {p}: {e}")

        # Sort by timestamp (newest first)
        return sorted(runs, key=lambda x: x.get("timestamp", ""), reverse=True)

    def load_results(self, id: str) -> dict[str, Any]:
        """Loads results and metadata for a specific run ID."""
        run_dir = None
        for p in self.temp_root.rglob("*"):
            if p.is_dir() and p.name == id:
                run_dir = p
                break

        if not run_dir:
            raise FileNotFoundError(f"Run ID '{id}' not found in {self.temp_root}")

        meta_path = run_dir / "meta.json"
        data_path = run_dir / "results.json"

        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)

        with open(data_path, encoding="utf-8") as f:
            results = json.load(f)

        return {"metadata": meta, "results": results}
