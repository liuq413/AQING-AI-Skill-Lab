#!/usr/bin/env python3
"""Validate this repository's three portable SKILL.md manifests and local links.

This is a lightweight repository check, not official Agent Skills certification.
No third-party packages are required.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "visual-story-director",
    "editorial-poster-designer",
    "cinematic-portrait-director",
}
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_skill(folder: Path) -> list[str]:
    errors = []
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        return [f"{folder.name}: missing SKILL.md"]

    body = skill_file.read_text(encoding="utf-8")
    if not body.startswith("---\n"):
        return [f"{folder.name}: missing initial YAML frontmatter delimiter"]
    chunks = body.split("\n---\n", 1)
    if len(chunks) != 2:
        return [f"{folder.name}: missing closing YAML frontmatter delimiter"]

    frontmatter, instructions = chunks
    metadata = {}
    # Required fields use simple top-level scalar syntax in this repository.
    for line in frontmatter.splitlines()[1:]:
        match = re.match(r"^([a-z][a-z-]*):\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip().strip('"\'')

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{folder.name}: invalid name: {name!r}")
    if name != folder.name:
        errors.append(f"{folder.name}: frontmatter name must match folder")
    if not description or len(description) > 1024:
        errors.append(f"{folder.name}: description must be 1..1024 characters")
    if not instructions.strip():
        errors.append(f"{folder.name}: SKILL.md has no instructions")
    if body.count("```") % 2:
        errors.append(f"{folder.name}: unclosed fenced code block")

    for linked in LINK_RE.findall(instructions):
        linked = linked.split("#", 1)[0]
        if not linked or "://" in linked or linked.startswith("mailto:"):
            continue
        if not (folder / linked).is_file():
            errors.append(f"{folder.name}: broken local reference {linked}")
    return errors


def main() -> int:
    found = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    errors = []
    if found != EXPECTED:
        errors.append(f"skill directories differ: expected {sorted(EXPECTED)}, got {sorted(found)}")
    for name in sorted(EXPECTED & found):
        errors.extend(check_skill(SKILLS / name))

    for error in errors:
        print(f"FAIL  {error}")
    if errors:
        return 1
    print("PASS  3 SKILL.md manifests, folder names, local links and code fences")
    print("NOTE  Does not evaluate AI generation quality or target-platform compatibility")
    return 0


if __name__ == "__main__":
    sys.exit(main())
