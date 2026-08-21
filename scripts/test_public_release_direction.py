#!/usr/bin/env python3
"""Regression tests for the public-release positioning and supported scope."""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").casefold().split())


class PublicReleaseDirectionTests(unittest.TestCase):
    def test_landing_matches_public_release_direction(self) -> None:
        landing = normalized_text(REPO_ROOT / "index.html")

        for expected in (
            "your agents. one window",
            "apache license 2.0",
            "windows is not included in this release",
            "linux is planned",
            "https://github.com/kodade/kodade/releases",
            "https://github.com/kodade/kodade/releases/download/v2.0.1/kodade_2.0.1_aarch64.dmg",
            "the tabbed workspace",
            "the agents tab",
            "ködwork background tasks and ködpr review",
            '<meta name="twitter:site" content="@kodadeapp">',
            '<a href="https://github.com/kodade/kodade">github</a>',
            '<a href="https://x.com/kodadeapp" rel="me" '
            'aria-label="ködade on 𝕏 (@kodadeapp)">𝕏</a>',
        ):
            self.assertIn(expected, landing)

        for stale in (
            "two döts",
            "your subscriptions, one window",
            "macos — coming soon",
            "public installers pending",
        ):
            self.assertNotIn(stale, landing)

    def test_docs_match_supported_public_scope(self) -> None:
        docs = REPO_ROOT / "docs"
        overview = normalized_text(docs / "index.md")
        platform = normalized_text(docs / "support/platform-status.md")

        self.assertIn("your agents. one window", overview)
        self.assertIn("apache license 2.0", overview)
        self.assertIn("no current release package", platform)
        self.assertIn("linux", platform)
        self.assertIn("ködwork", platform)
        self.assertIn("ködpr", platform)
        self.assertIn("ködweb", platform)
        self.assertIn("no longer", platform)

        removed_pages = (
            "free-and-pro.md",
            "kodlocal.md",
            "kodpr.md",
            "kodssh.md",
            "kodweb.md",
            "kodwhisper.md",
        )
        for page in removed_pages:
            self.assertFalse((docs / "features" / page).exists(), page)

        public_docs = "\n".join(
            path.read_text(encoding="utf-8").casefold()
            for path in sorted(docs.rglob("*.md"))
        )
        self.assertNotRegex(public_docs, r"\bpro\b")
        self.assertNotIn("there is no public download", public_docs)


if __name__ == "__main__":
    unittest.main()
