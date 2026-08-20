#!/usr/bin/env python3
"""Validate the portable product-artifact contract without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

INITIATIVE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MANIFEST_PATH = re.compile(r"^\s{2}([a-z_]+):\s*(.+?)\s*$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
REQUIRED_METADATA = {"artifact_type", "initiative_id", "status", "created", "updated", "upstream"}
ARTIFACT_FILENAMES = {
    "framing": "framing.md",
    "discovery": "discovery.md",
    "solution": "solution.md",
    "flow": "flow.md",
    "ui_exploration": "ui-exploration.md",
    "usability_validation": "usability-validation.md",
    "delivery_specification": "delivery-specification.md",
    "launch": "launch.md",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter_keys(path: Path) -> set[str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return set()
    return {
        line.split(":", 1)[0].strip()
        for line in match.group(1).splitlines()
        if ":" in line and not line.lstrip().startswith("-")
    }


def check_markdown(path: Path, errors: list[str]) -> None:
    missing = REQUIRED_METADATA - frontmatter_keys(path)
    if missing:
        fail(errors, f"{path}: missing frontmatter fields: {', '.join(sorted(missing))}")

    for target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = target.split("#", 1)[0]
        if target_path and not (path.parent / target_path).resolve().exists():
            fail(errors, f"{path}: broken local link: {target}")


def manifest_artifacts(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    in_artifacts = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "artifacts:":
            in_artifacts = True
            continue
        if in_artifacts and line and not line.startswith(" "):
            break
        if in_artifacts:
            match = MANIFEST_PATH.match(line)
            if match and match.group(2) != "null":
                entries[match.group(1)] = match.group(2)
    return entries


def manifest_scalar(path: Path, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else None


def validate(product_root: Path) -> list[str]:
    errors: list[str] = []
    if product_root.name != "product":
        fail(errors, f"artifact root must be named product: {product_root}")
    index = product_root / "README.md"
    if not index.is_file():
        fail(errors, f"missing required product index: {index}")
    else:
        check_markdown(index, errors)
    for directory in (product_root / "strategy", product_root / "initiatives"):
        if not directory.is_dir():
            fail(errors, f"missing required directory: {directory}")
    direction = product_root / "strategy" / "direction" / "product-direction.md"
    if not direction.is_file():
        fail(errors, f"missing required product direction: {direction}")
    else:
        check_markdown(direction, errors)

    for initiative in sorted((product_root / "initiatives").glob("*")) if (product_root / "initiatives").is_dir() else []:
        if not initiative.is_dir():
            continue
        if not INITIATIVE_ID.fullmatch(initiative.name):
            fail(errors, f"{initiative}: initiative ID must be lowercase kebab-case")
        manifest = initiative / "manifest.yaml"
        framing = initiative / "framing.md"
        if not manifest.is_file():
            fail(errors, f"{initiative}: missing manifest.yaml")
            continue
        if manifest_scalar(manifest, "initiative_id") != initiative.name:
            fail(errors, f"{manifest}: initiative_id must match its folder name")
        for key in ("status", "owner", "current_decision"):
            if manifest_scalar(manifest, key) is None:
                fail(errors, f"{manifest}: missing required {key}")
        direction_path = manifest_scalar(manifest, "direction")
        if direction_path is None:
            fail(errors, f"{manifest}: missing required direction link")
        elif not (initiative / direction_path).resolve().is_file():
            fail(errors, f"{manifest}: direction points to missing {direction_path}")
        if not framing.is_file():
            fail(errors, f"{initiative}: missing required framing.md")
        for kind, relative_path in manifest_artifacts(manifest).items():
            expected = ARTIFACT_FILENAMES.get(kind)
            if expected is None:
                fail(errors, f"{manifest}: unsupported artifact key {kind}")
            elif relative_path != expected:
                fail(errors, f"{manifest}: {kind} must use {expected}")
            artifact = initiative / relative_path
            if not artifact.is_file():
                fail(errors, f"{manifest}: {kind} points to missing {relative_path}")

        for markdown in initiative.rglob("*.md"):
            relative = markdown.relative_to(initiative)
            if len(relative.parts) == 1 and markdown.name not in ARTIFACT_FILENAMES.values():
                fail(errors, f"{markdown}: unsupported initiative artifact filename")
            if len(relative.parts) == 2 and relative.parts[0] == "learning" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}-outcome-review\.md", markdown.name):
                fail(errors, f"{markdown}: learning reviews must use YYYY-MM-DD-outcome-review.md")
            if len(relative.parts) > 1 and relative.parts[0] not in {"learning", "evidence"}:
                fail(errors, f"{markdown}: nested initiative artifacts must be in evidence/ or learning/")
            check_markdown(markdown, errors)

    for markdown in (product_root / "strategy").rglob("*.md") if (product_root / "strategy").is_dir() else []:
        check_markdown(markdown, errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_product_artifacts.py <path/to/product>")
        return 2
    errors = validate(Path(sys.argv[1]).resolve())
    if errors:
        print("Product artifact validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Product artifact contract is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
