# 2026-09-29 KP Course

Student edition: the public course website with lectures, hands-on exercises, data and Galaxy instructions.

**Course website:** <https://bentpetersendk.github.io/2026-09-29-KP-Course/>

- **Website:** built with [MkDocs](https://www.mkdocs.org/) and the Material theme, published on GitHub Pages.
- **Maintainers:** Bent Petersen <!-- and co-teachers: add names -->
- **Exercises run on:** [Galaxy Europe](https://usegalaxy.eu)

## Two repositories

| Repository | Visibility | Contains |
|---|---|---|
| **this repository** | public | website source, student exercise pages, lecture material, public dataset manifest, student workflows |
| **instructor repository** | private | exercise sources *with solutions*, answer keys, answer-validation workflows and results, Galaxy deployment scripts, instructor notes |

Exercise pages in `content/exercises/` are **generated** from the instructor repository, which removes all solutions and runs an answer-leak test before writing them. Do not edit them here; see [CONTRIBUTING.md](CONTRIBUTING.md).

Nothing with answers is ever committed to this repository. Solutions must never be added here, not even temporarily: everything in a public repository's history stays public.

## Layout

```
mkdocs.yml                 site configuration and navigation
content/                   website pages (Markdown)
  index.md                 Home
  lectures/                lecture list (+ files/ for slide PDFs)
  exercises/               exercise list + one folder per exercise (generated pages)
  data/                    Data page (tables rendered from data/datasets.yaml)
  galaxy/                  getting started with Galaxy Europe
  resources/               links to documentation and further reading
data/datasets.yaml         public dataset manifest: files, checksums, sizes, links (no FASTQ files in Git)
hooks/datasets_table.py    renders data/datasets.yaml into the Data page
workflows/                 Galaxy workflows that may be shared with students
tools/check_public.py      safety checks (no teacher files, no solution markers, no credentials)
tools/install-hooks.sh     installs a pre-commit hook running those checks
```

## Build and preview locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve                 # preview at http://127.0.0.1:8000
mkdocs build --strict        # full build; fails on broken internal links
python3 tools/check_public.py
```

Publishing is described in [CONTRIBUTING.md](CONTRIBUTING.md#publishing-the-website).
