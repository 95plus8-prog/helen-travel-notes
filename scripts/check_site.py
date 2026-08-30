# -*- coding: utf-8 -*-
"""Static-site validation for HELEN travel notes."""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urldefrag, urlparse

ROOT = Path(__file__).resolve().parents[1]
BUILD_PATH = ROOT / "build_pages.py"
HTML_ATTR_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
CSS_URL_RE = re.compile(r"""url\((?!['"]?data:)(['"]?)([^)'"]+)\1\)""")


def load_build_module():
    spec = importlib.util.spec_from_file_location("build_pages", BUILD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import build_pages.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_generated_files(build, errors: list[str]) -> None:
    expected = {
        ROOT / "work.html": build.work_page(),
        ROOT / "sitemap.xml": build.sitemap_xml(),
        ROOT / "robots.txt": build.robots_txt(),
    }
    for index, work in enumerate(build.WORKS):
        expected[ROOT / "work" / f"{work['slug']}.html"] = build.detail_page(index, work)

    for path, content in expected.items():
        if not path.exists():
            fail(errors, f"missing generated file: {path.relative_to(ROOT)}")
            continue
        if path.read_text(encoding="utf-8") != content:
            fail(errors, f"generated file is stale: {path.relative_to(ROOT)}")


def check_work_assets(build, errors: list[str]) -> None:
    slugs = set()
    for work in build.WORKS:
        slug = work["slug"]
        if slug in slugs:
            fail(errors, f"duplicate work slug: {slug}")
        slugs.add(slug)

        asset = ROOT / "assets" / "works" / f"{slug}.jpg"
        if not asset.exists():
            fail(errors, f"missing work image: {asset.relative_to(ROOT)}")
            continue

        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(asset)],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            fail(errors, f"cannot inspect image: {asset.relative_to(ROOT)}")
            continue
        width = re.search(r"pixelWidth:\s+(\d+)", result.stdout)
        height = re.search(r"pixelHeight:\s+(\d+)", result.stdout)
        if not width or not height:
            fail(errors, f"cannot parse image dimensions: {asset.relative_to(ROOT)}")
            continue
        actual = (int(width.group(1)), int(height.group(1)))
        declared = (int(work["w"]), int(work["h"]))
        if actual != declared:
            fail(errors, f"image dimension mismatch for {slug}: declared {declared}, actual {actual}")


def local_target(source: Path, raw: str) -> Path | None:
    href, _ = urldefrag(raw.strip())
    if not href:
        return None
    if href.startswith("#") or href.startswith("%23"):
        return None
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https", "mailto", "tel"}:
        return None
    if href.startswith("//"):
        return None
    return (source.parent / parsed.path).resolve()


def check_references(errors: list[str]) -> None:
    files = list(ROOT.glob("*.html")) + list((ROOT / "work").glob("*.html"))
    files.extend([ROOT / "css" / "style.css", ROOT / "js" / "main.js"])

    for source in files:
        text = source.read_text(encoding="utf-8")
        refs = [match.group(1) for match in HTML_ATTR_RE.finditer(text)]
        refs.extend(match.group(2) for match in CSS_URL_RE.finditer(text))
        for ref in refs:
            target = local_target(source, ref)
            if target is None:
                continue
            if not target.exists():
                rel_source = source.relative_to(ROOT)
                fail(errors, f"broken local reference in {rel_source}: {ref}")


def main() -> int:
    errors: list[str] = []
    build = load_build_module()

    check_generated_files(build, errors)
    check_work_assets(build, errors)
    check_references(errors)

    if errors:
        print("Site check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    page_count = len(build.STATIC_PAGES) + len(build.WORKS)
    print(f"Site check passed: {page_count} pages, {len(build.WORKS)} works, sitemap and robots verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
