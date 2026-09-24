# Maintaining the course website

This guide is for the course teachers. It covers everything needed to update the website without prior knowledge of the project.

## What to edit where

| I want to… | Edit | Repository |
|---|---|---|
| change the home page, Getting started (Galaxy help) or resources | `content/index.md`, `content/galaxy/index.md`, `content/resources/index.md` | public (this one) |
| add or update a lecture | `content/lectures/index.md` (+ PDF in `content/lectures/files/`) | public |
| change an exercise's text or questions | `exercises/<name>/tutorial.md` | **instructor (private)** |
| change an answer / expected result | `exercises/<name>/tutorial.md` (solution box) and `exercises/<name>/validation.yaml` | **instructor (private)** |
| add a dataset, change a download link or the shared Galaxy history link | `data/datasets.yaml` | public |
| add a student workflow | `workflows/` + a link from the exercise | public (read `workflows/README.md` first) |
| change the menu | `nav:` in `mkdocs.yml` | public |

Never edit files in `content/exercises/<name>/` by hand. They are overwritten by the instructor build.

## Lectures

1. Export the slides to PDF. Keep files below ~20 MB; compress images if needed. For larger files, attach them to a GitHub release (or an archive such as Zenodo) and link to them.
2. Put the PDF in `content/lectures/files/`, e.g. `content/lectures/files/02-alignment.pdf`.
3. Add a row to the table in `content/lectures/index.md`:
   `| 2 | Read alignment | [Slides (PDF)](files/02-alignment.pdf) | ... |`
4. Build locally (below) and check the link.

Only publish slides you have the right to share, including third-party figures.

## Exercises

Exercises are written in the **instructor repository**, because the source contains the solutions. The workflow is:

1. Edit or add `exercises/<name>/tutorial.md` there. Use the Galaxy Training Network box format (`hands_on`, `question` with a nested `solution`, `tip`, `comment`), and put every answer inside a solution box.
2. In the instructor repository, run `python build/build.py` and then `python tests/test_answer_leak.py`.
   The build writes `content/exercises/<name>/index.md` into this repository, but only if the leak check passes.
3. Add a new practical to `nav:` in `mkdocs.yml` (under **Practicals**) and to `content/exercises/index.md` (the Practicals page); add its slides and references under its own heading on the Lectures and Resources pages.
4. Build this site locally, check it, then commit here.

## Data

`data/datasets.yaml` is the single place for dataset information. The Data page and the exercise pages link to it.

- **Never commit FASTQ or other data files to Git.** Record the name, size, SHA-256, description and a download location instead.
- **Keep answers out of the manifest.** Do not add read counts, read lengths, GC content or quality values: these are exercise answers.
- **Shared Galaxy history link:** once it exists, set `galaxy_history_url` and rebuild both repositories. The exercise page picks the link up from here.
- **Long-term archive:** when redistribution rights are confirmed, deposit the files (e.g. on Zenodo) and set `archive_url`.

## Build and check locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs build --strict          # fails on broken internal links or anchors
python3 tools/check_public.py  # no teacher files, solution markers or credentials
mkdocs serve                   # preview at http://127.0.0.1:8000
```

Run `bash tools/install-hooks.sh` once after cloning. It makes `git commit` refuse commits that fail `tools/check_public.py`.

## Publishing the website

The site is published from the `gh-pages` branch, which `mkdocs gh-deploy` creates. No CI build is needed.

1. In the instructor repository: `python build/build.py && python tests/test_answer_leak.py` (this also scans this repository and its history).
2. Here: `mkdocs build --strict && python3 tools/check_public.py`.
3. Commit and push `main`.
4. Run `mkdocs gh-deploy --clean`. This builds the site and pushes it to the `gh-pages` branch.

## Course iterations

Tag the repository at the start of each course run (for example `git tag 2026-autumn`). Last year's material stays retrievable while the pages continue to evolve.

## Style

- Write for students: short paragraphs, the exact Galaxy button and field names, one action per step.
- Link to tool versions with the "open tool" links that the exercise build generates, so students always use the tested versions.
- Do not add answers anywhere in this repository.

## Licensing of contributions

Original material added to this repository is published under CC BY 4.0 (see `LICENSE.md`).
- Only add third-party material (figures, slides, data) if its licence allows it, and state its source and licence next to it.
- Never add FASTQ or other datasets to Git.
