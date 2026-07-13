#!/usr/bin/env python3
"""Validate the generated Cloudflare Pages artifact without extra packages."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


SITE_ORIGIN = "https://kodade.com"
CSS_URL_PATTERN = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
ASSET_LINK_RELS = {"icon", "preload", "stylesheet"}


class SiteValidationError(Exception):
    """Raised when generated output does not match the public-site contract."""


class ParsedHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.canonicals: list[str] = []
        self.main_count = 0
        self.noindex = False

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = {name.lower(): value or "" for name, value in attrs}
        tag = tag.lower()

        self.ids.extend(value for name, value in attrs if name.lower() == "id" and value)
        if tag == "main":
            self.main_count += 1

        if tag in {"a", "area"} and attributes.get("href"):
            self.links.append(("link", attributes["href"]))
        if tag in {"img", "script", "source"} and attributes.get("src"):
            self.links.append((f"{tag} asset", attributes["src"]))
        if tag == "video" and attributes.get("poster"):
            self.links.append(("video poster", attributes["poster"]))

        if tag == "link" and attributes.get("href"):
            rels = set(attributes.get("rel", "").lower().split())
            if "canonical" in rels:
                self.canonicals.append(attributes["href"])
            if rels & ASSET_LINK_RELS:
                self.links.append(("link asset", attributes["href"]))

        if tag == "meta" and attributes.get("name", "").lower() == "robots":
            directives = {
                directive.strip().lower()
                for directive in attributes.get("content", "").split(",")
            }
            self.noindex = "noindex" in directives


def fail(message: str) -> None:
    raise SiteValidationError(message)


def web_path(path: Path, dist: Path) -> str:
    relative = path.relative_to(dist).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return f"/{relative.removesuffix('index.html')}"
    return f"/{relative}"


def canonical_url(path: Path, dist: Path) -> str:
    return f"{SITE_ORIGIN}{web_path(path, dist)}"


def artifact_for_url(url_path: str, dist: Path) -> Path | None:
    decoded = unquote(url_path)
    if "\0" in decoded:
        return None

    candidate = dist / decoded.lstrip("/")
    if decoded.endswith("/"):
        candidate /= "index.html"
    elif candidate.is_dir():
        candidate /= "index.html"
    elif not candidate.is_file() and not candidate.suffix:
        html_candidate = candidate.with_suffix(".html")
        if html_candidate.is_file():
            candidate = html_candidate

    try:
        candidate.resolve().relative_to(dist.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def internal_parts(reference: str, source_url: str) -> tuple[str, str] | None:
    reference = reference.strip()
    if not reference:
        return None

    parts = urlsplit(reference)
    if parts.scheme and parts.scheme not in {"http", "https"}:
        return None
    if parts.netloc and parts.netloc.lower() != "kodade.com":
        return None

    resolved = urlsplit(urljoin(f"{SITE_ORIGIN}{source_url}", reference))
    if resolved.netloc.lower() != "kodade.com":
        return None
    return resolved.path or "/", unquote(resolved.fragment)


def parse_html_files(dist: Path) -> dict[Path, ParsedHTML]:
    parsed_files: dict[Path, ParsedHTML] = {}
    for path in sorted(dist.rglob("*.html")):
        parser = ParsedHTML()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        parsed_files[path] = parser
    return parsed_files


def validate_html_structure(parsed_files: dict[Path, ParsedHTML], dist: Path) -> None:
    for path, page in parsed_files.items():
        relative = path.relative_to(dist)
        if page.main_count != 1:
            fail(f"{relative}: expected exactly one main landmark; found {page.main_count}")

        duplicate_ids = sorted(
            identifier for identifier, count in Counter(page.ids).items() if count > 1
        )
        if duplicate_ids:
            fail(f"{relative}: duplicate id(s): {', '.join(duplicate_ids)}")

    docs_404 = dist / "docs/404.html"
    for path, page in parsed_files.items():
        if not path.is_relative_to(dist / "docs") or path == docs_404:
            continue
        expected = canonical_url(path, dist)
        if page.canonicals != [expected]:
            fail(
                f"{path.relative_to(dist)}: expected one canonical URL {expected!r}; "
                f"found {page.canonicals!r}"
            )


def validate_reference(
    *,
    reference: str,
    source_path: Path,
    source_url: str,
    kind: str,
    parsed_files: dict[Path, ParsedHTML],
    dist: Path,
) -> None:
    target_parts = internal_parts(reference, source_url)
    if target_parts is None:
        return

    target_url, fragment = target_parts
    target_path = artifact_for_url(target_url, dist)
    source_relative = source_path.relative_to(dist)
    if target_path is None:
        fail(f"{source_relative}: broken internal {kind} {reference!r}")

    if fragment:
        target_page = parsed_files.get(target_path)
        if target_page is None:
            fail(f"{source_relative}: anchor targets a non-HTML file: {reference!r}")
        if fragment not in target_page.ids:
            fail(f"{source_relative}: missing anchor in {reference!r}")


def validate_references(parsed_files: dict[Path, ParsedHTML], dist: Path) -> None:
    for path, page in parsed_files.items():
        source_url = web_path(path, dist)
        for kind, reference in page.links:
            validate_reference(
                reference=reference,
                source_path=path,
                source_url=source_url,
                kind=kind,
                parsed_files=parsed_files,
                dist=dist,
            )

    for path in sorted(dist.rglob("*.css")):
        source_url = web_path(path, dist)
        for match in CSS_URL_PATTERN.finditer(path.read_text(encoding="utf-8")):
            validate_reference(
                reference=match.group(2),
                source_path=path,
                source_url=source_url,
                kind="CSS asset",
                parsed_files=parsed_files,
                dist=dist,
            )


def content_pages(dist: Path) -> list[Path]:
    return sorted((dist / "docs").rglob("index.html"))


def validate_sitemap(pages: list[Path], dist: Path) -> None:
    sitemap_path = dist / "docs/sitemap.xml"
    root = ElementTree.parse(sitemap_path).getroot()
    locations = {
        element.text.strip()
        for element in root.iter()
        if element.tag.endswith("loc") and element.text
    }
    expected = {canonical_url(path, dist) for path in pages}
    if locations != expected:
        missing = sorted(expected - locations)
        unexpected = sorted(locations - expected)
        fail(f"docs/sitemap.xml: missing {missing!r}; unexpected {unexpected!r}")


def validate_search_index(
    pages: list[Path], parsed_files: dict[Path, ParsedHTML], dist: Path
) -> None:
    index_path = dist / "docs/search/search_index.json"
    data = json.loads(index_path.read_text(encoding="utf-8"))
    entries = data.get("docs")
    if not isinstance(entries, list):
        fail("docs/search/search_index.json: expected a docs list")

    covered_urls: set[str] = set()
    for entry in entries:
        location = entry.get("location") if isinstance(entry, dict) else None
        if not isinstance(location, str):
            fail("docs/search/search_index.json: every entry needs a string location")
        validate_reference(
            reference=location or ".",
            source_path=index_path,
            source_url="/docs/",
            kind="search URL",
            parsed_files=parsed_files,
            dist=dist,
        )
        parts = internal_parts(location or ".", "/docs/")
        if parts is None:
            fail(f"docs/search/search_index.json: invalid location {location!r}")
        target_path = artifact_for_url(parts[0], dist)
        if target_path is None:
            fail(f"docs/search/search_index.json: broken location {location!r}")
        covered_urls.add(canonical_url(target_path, dist))

    expected = {canonical_url(path, dist) for path in pages}
    missing = sorted(expected - covered_urls)
    if missing:
        fail(f"docs/search/search_index.json: missing public page URLs: {missing!r}")


def validate_404s(parsed_files: dict[Path, ParsedHTML], dist: Path) -> None:
    root_404 = dist / "404.html"
    docs_404 = dist / "docs/404.html"
    for path in (root_404, docs_404):
        if not parsed_files[path].noindex:
            fail(f"{path.relative_to(dist)}: expected robots noindex")
    if root_404.read_bytes() == docs_404.read_bytes():
        fail("root and docs 404 artifacts must be distinct")


def validate(dist: Path) -> None:
    if not dist.is_dir():
        fail(f"site directory does not exist: {dist}")

    parsed_files = parse_html_files(dist)
    if not parsed_files:
        fail("generated site contains no HTML files")

    pages = content_pages(dist)
    validate_html_structure(parsed_files, dist)
    validate_references(parsed_files, dist)
    validate_sitemap(pages, dist)
    validate_search_index(pages, parsed_files, dist)
    validate_404s(parsed_files, dist)

    print(
        f"Validated {len(parsed_files)} HTML files and {len(pages)} public content pages."
    )


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dist")
    try:
        validate(dist.resolve())
    except (ElementTree.ParseError, json.JSONDecodeError, OSError, SiteValidationError) as error:
        print(f"Site validation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
