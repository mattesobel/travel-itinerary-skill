#!/usr/bin/env python3
"""
embed_images.py — turn a working trip dashboard into a single self-contained file.

The working Dashboard.html links to a local itinerary-images/ folder. This script
inlines every local image (both <img src="..."> tags and CSS url("...") references,
including the hero background) as base64 data URIs, and writes a shareable copy that
works with no folder and no internet — ideal for emailing or AirDropping.

Usage:
    python3 embed_images.py "path/to/Dashboard.html"
    python3 embed_images.py "path/to/Dashboard.html" -o "path/to/Dashboard (Shareable).html"

Notes:
- Only local images are embedded. Remote URLs (https://...) and Google Fonts are left as-is.
- Re-run after changing images or the dashboard.
- No third-party dependencies; standard library only.
"""

import argparse
import base64
import mimetypes
import os
import re
import sys

# data URIs can't readily reference fonts; we only inline images.
IMG_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"}


def _is_local(ref: str) -> bool:
    ref = ref.strip().strip('"').strip("'")
    if not ref:
        return False
    low = ref.lower()
    if low.startswith(("http://", "https://", "data:", "//", "mailto:", "#")):
        return False
    return True


def _data_uri(path: str) -> str | None:
    if not os.path.isfile(path):
        return None
    ext = os.path.splitext(path)[1].lower()
    if ext not in IMG_EXTS:
        return None
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "image/svg+xml" if ext == ".svg" else "application/octet-stream"
    with open(path, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def embed(html_path: str, out_path: str | None = None) -> str:
    base_dir = os.path.dirname(os.path.abspath(html_path))
    with open(html_path, "r", encoding="utf-8") as fh:
        html = fh.read()

    stats = {"embedded": 0, "missing": [], "skipped_remote": 0}

    def resolve(ref: str) -> str:
        ref = ref.strip().strip('"').strip("'")
        local = os.path.normpath(os.path.join(base_dir, ref.split("?")[0].split("#")[0]))
        uri = _data_uri(local)
        if uri is None:
            stats["missing"].append(ref)
            return ref
        stats["embedded"] += 1
        return uri

    # 1) <img src="...">
    def repl_img(m):
        quote, ref = m.group("q"), m.group("ref")
        if not _is_local(ref):
            stats["skipped_remote"] += 1
            return m.group(0)
        return f'src={quote}{resolve(ref)}{quote}'

    html = re.sub(r'src=(?P<q>["\'])(?P<ref>[^"\']+)(?P=q)', repl_img, html)

    # 2) CSS url("...") — covers the hero background and any inline styles
    def repl_url(m):
        ref = m.group("ref")
        if not _is_local(ref):
            stats["skipped_remote"] += 1
            return m.group(0)
        return f'url("{resolve(ref)}")'

    html = re.sub(r'url\(\s*(?P<ref>[^)]+?)\s*\)', repl_url, html)

    if out_path is None:
        d = os.path.dirname(os.path.abspath(html_path))
        out_path = os.path.join(d, "Dashboard (Shareable).html")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"Embedded {stats['embedded']} image(s).")
    if stats["skipped_remote"]:
        print(f"Left {stats['skipped_remote']} remote reference(s) untouched.")
    if stats["missing"]:
        print("WARNING: could not find these local images (left as-is):", file=sys.stderr)
        for ref in stats["missing"]:
            print(f"  - {ref}", file=sys.stderr)
    print(f"Wrote: {out_path}")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Inline local images into a self-contained dashboard.")
    ap.add_argument("html", help="Path to the working Dashboard.html")
    ap.add_argument("-o", "--out", help="Output path (default: 'Dashboard (Shareable).html' alongside input)")
    args = ap.parse_args()
    if not os.path.isfile(args.html):
        sys.exit(f"Not a file: {args.html}")
    embed(args.html, args.out)


if __name__ == "__main__":
    main()
