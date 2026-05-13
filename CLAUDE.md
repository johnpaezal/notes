# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Personal learning repository for becoming an **AWS Engineer with full-stack backend focus**. Contains study notes, architecture prototypes, and Anki flashcard decks organized across 10 learning stages (see `ROADMAP.md`).

## Note Style

All notes follow the minimalist format defined in `CONTEXT.md`. Key rules:

- Title format: `# Technology Topic` (no "Notes" suffix)
- Every `##` and `###` section has a short italic description (3–6 words) directly below
- Definitions: `**Term** – Short definition (max 10 words)  ` — each line ends with two trailing spaces for line breaks
- Short inline lists for simple enumerations: `**Benefits**: A, B, C`
- Code blocks max 20–30 lines, one concept each, always include `# Usage` section
- `---` separator between every `##` section
- No verbose explanations, no redundant comments

## Concept Uniqueness

Each concept lives in exactly ONE file. Never duplicate a concept across notes — if it already exists elsewhere, do not copy it; omit it or reference the canonical file. Goal: clean notes with no repetition.

## Visual Elements Warning

If a concept requires a diagram that markdown cannot render well (2D matrices, diagrams with crossing arrows, wireframes, architecture diagrams with icons, sequence diagrams, ER diagrams, Gantt, burndown charts, journey maps, user story maps, impact maps, UML), **warn the user** instead of forcing an ugly text version. Suggest the right tool (Excalidraw, draw.io, Miro, Figma, Mermaid, PlantUML, dbdiagram.io) and recommend saving the image in a `diagrams/` folder next to the `.md`, referenced as `![title](diagrams/name.png)`. Keep markdown for: tables, lists, tree hierarchies (`├──`), linear flows (`A → B → C`), code blocks, text templates.

## Anki Cards (Automatic)

Every time a new topic is created or updated, immediately add the corresponding Anki cards to `anki-aws-engineer.txt`. Do not wait for the user to ask.

- Template and format reference: `.claude/PLANTILLA_ANKI.txt`
- Deck hierarchy: `AwsEngineer::Area::Tema::Subtema`
- Vary card types: text, `<ul>` lists, `<table>`, `<pre>` for code
- One idea per card, question on front with `¿...?`, minimal answer on back

## Folder Structure Rules

- Numbered group folders: `01-grupo/`, `02-grupo/` (implies learning progression)
- Single-file topics go directly as `topic.md` inside the group — no subfolder
- Subfolders only when a topic has multiple files (e.g., `oop/notes.md` + `oop/example.py`)
- All names in `kebab-case` lowercase
- Each technology section has a `README.md` with an index table grouped by section

## Repository Map

Only folders that currently exist with content are listed. New stage folders are added on demand per `ROADMAP.md`.

| Folder | Content |
|--------|---------|
| `00-software-engineering/` | SE fundamentals: `01-process`, `02-design`, `03-architecture`, `04-quality`, `05-delivery`, `06-communication`, `07-global-example` |
| `01-languages/` | `python/` (core → fastapi, flask), `java/` (core → ecosystem) |
| `02-infrastructure/` | `docker/`, `networking/`, `linux/`, `bash/`, `kubernetes/` (linux, bash, kubernetes — pending notes) |
| `03-databases/` | `sql/`, `nosql/`, `data-modeling/` |
| `04-web/` | `angular/` (pending) |
| `05-tooling/` | `git/`, `json-yaml/`, `ci-cd/`, `testing/`, `best-practices/` (all pending) |
| `06-cloud/` | `aws/` (01-core → 08-security), `terraform/`, `cdk/` (all pending) |
| `07-automation/` | `claude-ai/`, `n8n/` |
| `08-career/` | `professional-profile/` (linkedin.md) |
| `09-system-design/` | `01-fundamentals/` → `04-case-studies/` (all pending) |
| `anki-aws-engineer.txt` | All Anki flashcard decks |
| `ROADMAP.md` | 10-stage learning plan with progress tracking |
| `CONTEXT.md` | Full style guide for notes and Anki format |

## Architecture Prototypes

`00-software-engineering/03-architecture/tipos-arquitecturas/` contains minimal Flask Todo apps showing architecture styles side by side:

- `01-capas/` — Layered: `repository.py` (data) → `service.py` (logic) → `routes.py` (HTTP) → `app.py` (entry)
- `02-monolito/` — Everything in a single `app.py`

Run any prototype with:
```bash
pip install flask
python app.py
```
