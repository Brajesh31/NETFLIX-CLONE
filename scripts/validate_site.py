#!/usr/bin/env python3
"""Validate required files and local asset references for the static page."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "index.html",
    "style.css",
    "images/logo.png",
    "images/bg.jpg",
    "video/video1.mp4",
    "video/video2.mp4",
)


class AssetParser(HTMLParser):
    """Collect local resource references from HTML elements."""

    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attribute in ("src", "poster"):
            value = values.get(attribute)
            if value:
                self.references.append(value)
        if tag == "link":
            href = values.get("href")
            rel = (values.get("rel") or "").lower().split()
            if href and ("stylesheet" in rel or "icon" in rel):
                self.references.append(href)


def is_external_or_non_file_reference(value: str) -> bool:
    value = value.strip()
    if not value or value.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
        return True
    parsed = urlsplit(value)
    return bool(parsed.scheme or parsed.netloc)


def resolve_reference(reference: str, source_file: Path) -> Path | None:
    if is_external_or_non_file_reference(reference):
        return None
    path = urlsplit(reference).path
    if not path:
        return None
    return (source_file.parent / path).resolve()


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Required file missing or empty: {relative}")

    html_path = ROOT / "index.html"
    css_path = ROOT / "style.css"
    if not html_path.is_file() or not css_path.is_file():
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    parser = AssetParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    references = [(item, html_path) for item in parser.references]

    css = css_path.read_text(encoding="utf-8")
    css_references = re.findall(r"url\(\s*['\"]?([^'\")]+)", css, flags=re.IGNORECASE)
    references.extend((item.strip(), css_path) for item in css_references)

    for reference, source_file in references:
        target = resolve_reference(reference, source_file)
        if target is None:
            continue
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"Local reference escapes repository root: {reference}")
            continue
        if not target.is_file():
            errors.append(f"Referenced local asset does not exist: {reference}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Static site validation passed. Checked {len(REQUIRED_FILES)} required files "
        f"and {len(references)} resource references."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
