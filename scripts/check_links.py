#!/usr/bin/env python3
"""Check local links and basic page structure for the static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.title = False
        self.main = False
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"a", "link", "script", "img"}:
            target = values.get("href") or values.get("src")
            if target:
                self.links.append(target)
        if tag == "title":
            self.title = True
        elif tag == "main":
            self.main = True
        elif tag == "h1":
            self.h1_count += 1


def html_pages() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.html")
        if not any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts)
    ]


def main() -> int:
    errors: list[str] = []
    pages = html_pages()
    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        label = page.relative_to(ROOT)
        if not parser.title:
            errors.append(f"{label}: missing <title>")
        if not parser.main:
            errors.append(f"{label}: missing <main>")
        if parser.h1_count != 1:
            errors.append(f"{label}: expected one <h1>, found {parser.h1_count}")

        for raw_link in parser.links:
            parsed = urlsplit(raw_link)
            if parsed.scheme or raw_link.startswith(("//", "mailto:", "tel:", "#")):
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"{label}: broken link {raw_link!r}")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(pages)} HTML pages; all local links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
