#!/usr/bin/env python3
"""Safety checks for the PUBLIC course repository.

This script knows no answers (it is public). It checks the structure instead:
  - no teacher-only files (solution sources, validation manifests, teacher
    workflows, runbooks, FASTQ data, key files),
  - no solution boxes or teacher markers in any text file,
  - no credentials (Galaxy API keys, GitHub tokens, private keys),
  - no files larger than 20 MB (large files belong in an archive, not in Git),
  - no links to the old KBase Narratives (the site must work on its own).
The answer-level leak test runs in the private instructor repository
(tests/test_answer_leak.py), which scans this repository and its Git history.

Usage:
  python tools/check_public.py            # working tree (+ site/ if built)
  python tools/check_public.py --staged   # only files staged for commit (pre-commit hook)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 20 * 1024 * 1024
PRIVATE_NAMES = {"validation.yaml", "migration-notes.md", "runbook.md", "tutorial.md", "leakcheck.py", "data.yaml"}
PRIVATE_SUFFIXES = (".gxwf.yml", ".ga", ".fastq", ".fastq.gz", ".fq", ".fq.gz", ".key", ".env", ".pem")
MARKERS = [
    (re.compile(r"\{:\s*\.solution"), "GTN solution box"),
    (re.compile(r"\{:\s*\.(teacher_note|common_problem|live_demo|expected|answer|legacy_kbase)\b"), "GTN teacher-only box"),
    (re.compile(r"!!! (answer|expected|teacher-note|common-problem|live-demo|legacy-kbase)\b"), "teacher-only admonition"),
    (re.compile(r"(?i)teacher edition|contains solutions"), "teacher-edition marker"),
    (re.compile(r"<solution-title>"), "GTN solution title"),
    (re.compile(r"<!--\s*validation:"), "validation marker"),
    (re.compile(r"(?i)teacher validation|teacher version|teacher appendix"), "teacher-only heading"),
    (re.compile(r"(?i)kbase\.us/n/"), "link to an old KBase Narrative"),
]
CREDENTIALS = [
    (re.compile(r"(?<![0-9a-fA-F])[0-9a-f]{32}(?![0-9a-fA-F])"), "32-hex token (Galaxy API key format)"),
    (re.compile(r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|gh[ous]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"(?i)(x-api-key|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"), "assigned credential"),
]
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
SELF = Path(__file__).resolve()


def files(staged: bool) -> list[Path]:
    if staged:
        out = subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
                             capture_output=True, text=True, check=True).stdout.split()
        return [ROOT / f for f in out]
    return [p for p in ROOT.rglob("*") if p.is_file() and not SKIP_DIRS & set(p.relative_to(ROOT).parts)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--staged", action="store_true")
    args = ap.parse_args()
    problems = []
    for p in files(args.staged):
        rel = p.relative_to(ROOT)
        if p.name in PRIVATE_NAMES or p.name.endswith(PRIVATE_SUFFIXES):
            problems.append(f"{rel}: teacher-only or data file must not be in the public repository")
        if p.stat().st_size > MAX_BYTES:
            problems.append(f"{rel}: larger than 20 MB")
            continue
        data = p.read_bytes()
        if b"\0" in data[:4096] or p.resolve() == SELF:
            continue
        text = data.decode("utf-8", errors="replace")
        in_asset = rel.parts[:1] == ("site",) and p.suffix in (".js", ".css", ".map")
        if not in_asset:
            problems += [f"{rel}: {label}" for rx, label in MARKERS if rx.search(text)]
        problems += [f"{rel}: possible credential ({label})" for rx, label in CREDENTIALS if rx.search(text)]
    if problems:
        print("Public repository check FAILED:\n  " + "\n  ".join(problems))
        return 1
    print("Public repository check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
