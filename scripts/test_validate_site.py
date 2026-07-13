#!/usr/bin/env python3
"""Failure-path tests for the generated-site validator."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIST = REPO_ROOT / "dist"
VALIDATOR = REPO_ROOT / "scripts/validate_site.py"


class GeneratedSiteValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.fixture = Path(self.temporary_directory.name) / "dist"
        shutil.copytree(SOURCE_DIST, self.fixture)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def validate_fixture(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.fixture)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_rejects_broken_internal_link(self) -> None:
        index = self.fixture / "index.html"
        html = index.read_text(encoding="utf-8")
        index.write_text(
            html.replace(
                "<main>",
                '<main><a href="/temporary-broken-fixture/">fixture</a>',
                1,
            ),
            encoding="utf-8",
        )

        result = self.validate_fixture()

        self.assertEqual(1, result.returncode)
        self.assertIn("broken internal link '/temporary-broken-fixture/'", result.stderr)

    def test_rejects_duplicate_id(self) -> None:
        index = self.fixture / "index.html"
        html = index.read_text(encoding="utf-8")
        index.write_text(
            html.replace("<main>", '<main id="download">', 1),
            encoding="utf-8",
        )

        result = self.validate_fixture()

        self.assertEqual(1, result.returncode)
        self.assertIn("duplicate id(s): download", result.stderr)


if __name__ == "__main__":
    unittest.main()
