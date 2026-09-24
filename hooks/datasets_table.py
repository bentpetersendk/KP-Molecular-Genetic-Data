"""MkDocs hook: render data/datasets.yaml into pages.

In any page, the marker

    <!-- datasets: ngs-preprocessing -->

is replaced by a section describing that dataset group: how to get the data
(shared Galaxy history, archive, direct download), a file table with sizes and
SHA-256 checksums, and any Galaxy collections. The YAML file is the single place
where dataset links and checksums are maintained.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

MARKER = re.compile(r"<!--\s*datasets:\s*([\w-]+)\s*-->")
_cache: dict | None = None


def _load(config) -> dict:
    global _cache
    if _cache is None:
        path = Path(config["config_file_path"]).parent / "data" / "datasets.yaml"
        _cache = {d["id"]: d for d in yaml.safe_load(path.read_text())["datasets"]}
    return _cache


def _size(n: int) -> str:
    return f"{n / 1e6:.0f} MB"


def _render(ds: dict, page_url_depth: int) -> str:
    up = "../" * page_url_depth
    out = [f"### {ds['title']} {{#{ds['id']}}}", ""]
    out.append(f"Used in the exercise [{ds['title']}]({up}{ds['exercise']}).")
    out.append("")
    out.append("**How to get the data**")
    out.append("")
    if ds.get("galaxy_history_url"):
        out.append(f"- **Recommended:** import the shared Galaxy history: <{ds['galaxy_history_url']}>. "
                   "It already contains every file with the correct datatype, and the paired collection.")
    else:
        out.append("- **Recommended:** a shared Galaxy history with all files will be linked here before the course.")
    if ds.get("archive_url"):
        out.append(f"- Archived copy: <{ds['archive_url']}>")
    out.append("- Direct download of the individual files: links in the table below. "
               "Upload them to Galaxy with the datatype shown.")
    out.append("")
    out.append("| File | Description | Technology | Layout | Galaxy datatype | Size |")
    out.append("|---|---|---|---|---|---|")
    for f in ds["files"]:
        name = f"[`{f['filename']}`]({f['download_url']})" if f.get("download_url") else f"`{f['filename']}`"
        out.append(f"| {name} | {f['description']} | {f['technology']} | {f['layout']} "
                   f"| `{f['galaxy_datatype']}` | {_size(f['size_bytes'])} |")
    out.append("")
    for c in ds.get("collections", []):
        out.append(f"Galaxy **{c['type']} collection** `{c['name']}`: forward = `{c['forward']}`, "
                   f"reverse = `{c['reverse']}`.")
        out.append("")
    out.append('??? info "SHA-256 checksums"')
    out.append("")
    out.append("    Use these to check that a downloaded file is complete and unchanged "
               "(`shasum -a 256 <file>` on macOS/Linux, `certutil -hashfile <file> SHA256` on Windows).")
    out.append("")
    out.append("    | File | SHA-256 |")
    out.append("    |---|---|")
    for f in ds["files"]:
        out.append(f"    | `{f['filename']}` | `{f['sha256']}` |")
    out.append("")
    out.append(f"*Terms of use:* {ds['redistribution'].strip()}")
    out.append("")
    return "\n".join(out)


def on_page_markdown(markdown, page, config, files, **kwargs):
    if "<!--" not in markdown:
        return markdown
    data = _load(config)
    depth = page.file.src_uri.count("/")  # e.g. data/index.md -> 1

    def repl(m):
        key = m.group(1)
        if key not in data:
            raise KeyError(f"{page.file.src_uri}: unknown dataset id {key!r} in data/datasets.yaml")
        return _render(data[key], depth)

    return MARKER.sub(repl, markdown)
