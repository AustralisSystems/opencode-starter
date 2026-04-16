import logging
import re
from collections.abc import Generator
from pathlib import Path

from ai_agent_skill_fs_ops import FileSystemSkill

logger = logging.getLogger("ai_agent_search_skills")


class SearchSkill:
    """
    [AI AGENT SKILL] A specialized skill for advanced file and content searching.
    Leverages FileSystemSkill for repository awareness and path resolution.
    """

    def __init__(self, fs_skill: FileSystemSkill | None = None):
        self.fs = fs_skill or FileSystemSkill()

    def find_files(
        self, pattern: str, root: str | None = None, regex: bool = False, recursive: bool = True
    ) -> Generator[Path, None, None]:
        """
        Yields paths matching a name pattern.
        """
        root_path = self.fs._resolve_paths(root or str(self.fs.repo_root))

        if regex:
            compiled_pattern = re.compile(pattern)
            search_iter = root_path.rglob("*") if recursive else root_path.glob("*")
            for item in search_iter:
                if item.is_file() and compiled_pattern.search(item.name):
                    yield item
        else:
            yield from self.fs.list_files(str(root_path), pattern, recursive)

    def grep_content(
        self,
        query: str,
        root: str | None = None,
        file_pattern: str = "*",
        regex: bool = False,
        recursive: bool = True,
    ) -> Generator[dict, None, None]:
        """
        Searches for a string or regex pattern within files.
        Yields dicts with: {path, line_number, content}
        """
        root_path = self.fs._resolve_paths(root or str(self.fs.repo_root))

        # Identify candidate files
        files = self.find_files(file_pattern, str(root_path), regex=False, recursive=recursive)

        compiled_query = re.compile(query if regex else re.escape(query))

        for file_path in files:
            if not file_path.is_file():
                continue

            try:
                # Use incremental reading for memory efficiency
                with open(file_path, encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if compiled_query.search(line):
                            yield {"path": file_path, "line_number": i, "content": line.strip()}
            except Exception as e:
                logger.debug(f"Could not read file {file_path}: {e}")
