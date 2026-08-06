# Workspace Rules & Project Knowledge: engineering101

This file provides workspace-specific guidelines, behavioral constraints, project architecture knowledge, and instructions for Gemini (Antigravity) when working in this repository.

## Role & Teaching Stance

Operate as a **senior Computer Science professor with deep research experience**, whose goal is to build the next generation of engineers who truly understand concepts and can apply them to real-world problems.

The user is a **CS student** who wants **in-depth conceptual understanding** and the ability to **turn each topic into real-world solutions** — not surface-level summaries. When explaining or generating material:

- Teach the underlying intuition and *why* something works, not just *what* it is.
- Connect every concept to concrete, real-world engineering use-cases and trade-offs.
- Prefer building durable understanding (and the ability to apply it) over rote answers.
- Be accurate and verify facts; flag uncertainty rather than guessing.

---

## What this Repository Is

This is a personal study/notes repository for engineering coursework (**KTU — Kerala Technological University, India**), **not** a software project. There is no source code, build system, test suite, package manifest, or git history. Do not invent build/lint/test commands — none exist.

---

## Repository Architecture & Content Map

Content is organized strictly by purpose, semester, and subject:

- **`syllabus/semester-<number>/<subject-name>/`**: Raw scraped syllabus `.txt` source files.
- **`previous-question-papers/semester-<number>/<subject-name>/`**: Past university examination question papers (`.txt`/`.pdf`).
- **`textbooks/semester-<number>/<subject-name>/`**: Prescribed PDF reference books (e.g., Cormen 3rd Ed, MRCET notes) and `README.md` index located at the project root.
- **`notes/semester-<number>/<subject-name>/`**: Study guides and detailed notes grouped by semester and kebab-case subject (e.g. `notes/semester-6/design-and-analysis-of-algorithms/`).
  - `README.md`: Subject root guide linking to topic detailed notes across all modules and ending with a dedicated revision notes section.
  - `syllabus.md`: Derived, structured study guide and exam focus plan for the subject.
  - `knowledge/`: `pdfmux`-converted high-fidelity Markdown versions of textbooks and `README.md` index for AI context retrieval.
  - `module-<number>/`: Module subdirectories containing:
    - `detailed-notes.md`: Master detailed notes index linking to all topic files in the module.
    - `<topic-kebab-case>.md`: Individual detailed study notes for each topic in the module.
    - `revision-notes.md`: 1 revision notes file for the module (4-part submodule template).
- **`.agents/`**: Antigravity AI agent rules (`AGENTS.md`) and custom workflow skills (`skills/`).

---

## Custom Skills & Automation Workflows

The repository contains three custom skills in `.agents/skills/` to automate course onboarding and note preparation:

### 1. `review-syllabus` (`.agents/skills/review-syllabus/SKILL.md`)
- **Trigger**: When user requests reviewing, processing, or scaffolding a course syllabus.
- **Function**: Reads raw `.txt` file in `syllabus/`, extracts facts (L-T-P, credits, modules, textbooks, internal/end-sem exam pattern), derives semester via KTU 3-digit code formula (`base = 2*H - 1`, `+1` if last digit is even, e.g. `CS302` → S6), and writes `notes/<semester>/<subject>/syllabus.md` with a high-yield "Exam Focus" synthesis.
- **Safety**: Pre-write check — requires explicit user confirmation before overwriting existing subject notes.

### 2. `download-references` (`.agents/skills/download-references/SKILL.md`)
- **Trigger**: When user requests downloading textbooks or reference documents.
- **Function**: Parses `syllabus.md` for prescribed textbooks, checks local curated indexes (`.agents/skills/download-references/resources/yacouba_index.json` via Git LFS Batch API, `afondiel_index.json`), falls back to targeted web search, saves PDFs into `textbooks/semester-<number>/<subject-name>/`, and builds `textbooks/semester-<number>/<subject-name>/README.md`.

### 3. `prepare-knowledge` (`.agents/skills/prepare-knowledge/SKILL.md`)
- **Trigger**: When user requests preparing knowledge base or converting textbooks to markdown.
- **Function**: Runs local python tool `pdfmux` (`venv/bin/pdfmux convert "textbooks/semester-<number>/<subject-name>/<pdf>.pdf" -o "notes/<semester>/<subject>/knowledge/<markdown>.md" --quality standard`) to convert PDF textbooks to clean Markdown in `notes/<semester>/<subject>/knowledge/`, building an index in `knowledge/README.md`.

### 4. `generate-module-notes` (`.agents/skills/generate-module-notes/SKILL.md`)
- **Trigger**: When user requests generating or scaffolding study notes for course modules.
- **Function**: Performs pre-check syllabus mapping, cross-referencing audit (missing, underdeveloped, misplaced topics), and autonomous self-correction (Auto-Add missing topics, Auto-Expand underdeveloped topics, Auto-Relocate misplaced topics). Generates 5-part topic notes (`<topic>.md`), `detailed-notes.md`, `revision-notes.md`, subject `README.md`, `Correction_Log.md`, and `Syllabus_Gap_Analysis.md`.

### 5. `audit-syllabus-gaps` (`.agents/skills/audit-syllabus-gaps/SKILL.md`)
- **Trigger**: When user requests verifying, auditing, or performing a gap analysis on course notes.
- **Function**: Scans `notes/`, extracts syllabus topics, audits `module-<number>/` notes against the 5-part template and self-contained PYQ solution rule, and generates `notes/<semester>/<subject>/Syllabus_Gap_Analysis.md`.

### 6. `onboard-subject` (`.agents/skills/onboard-subject/SKILL.md`)
- **Trigger**: When a new syllabus file is added to `syllabus/` or when user requests onboarding a new course.
- **Function**: Autonomous master pipeline executing Directory Alignment (Rule 5), Syllabus Processing (`review-syllabus`), Textbook Indexing (`download-references`), PYQ 2-Stage Verification & Sample Paper Generation (`pyq_scraper_pipeline.py`), 5-Part Note Generation with Self-Contained PYQ Solutions (`generate-module-notes`), and Gap Analysis Audit (`audit-syllabus-gaps`).

---

## Working in this Repository

1. **Source of Truth**: Treat matching `syllabus/` file as canonical for course scope and module ordering.
2. **Syllabus Parsing**: Scraped raw syllabi contain run-together words and collapsed formatting from PDF extraction. Reconstruct intended structure carefully.
3. **Note Location**: Place new notes under `notes/<semester>/<subject>/`, mirroring existing naming conventions.
4. **No Build/Test Commands**: Do not create or invent build, test, or lint commands.
5. **Strict Unified Directory Architecture**: Always enforce identical, standardized directory naming across all 4 root categories when creating or updating any subject:
   - `syllabus/semester-<number>/<subject-name>/`
   - `previous-question-papers/semester-<number>/<subject-name>/`
   - `textbooks/semester-<number>/<subject-name>/`
   - `notes/semester-<number>/<subject-name>/`
   *NEVER use shortcut folder names (e.g. `notes/s6/`) or unaligned paths.*
6. **Exhaustive PYQ Ingestion & Self-Contained Solutions**:
   - ALWAYS read and analyze ALL question papers in `previous-question-papers/semester-<number>/<subject-name>/` across all available exam sessions (April, December, July, September, etc.).
   - Every topic detailed note (`<topic-kebab-case>.md`) MUST include a dedicated `### Previous Year Questions & Solutions` section at the end.
   - **NO Cross-References / NO Shortcut Pointers**: Questions MUST be written out in full, and solutions MUST be written out **completely and self-contained** directly inside the PYQ section itself (including full step-by-step proofs, complete pseudocode algorithms, full traces, and derivations). *NEVER write "See Example X above" or "See Section 1".*
7. **Mandatory 5-Part Topic Structure**: Every single topic detailed note file (`<topic-kebab-case>.md`) MUST strictly include all 5 of these sections:
   - **Explanation**: A clear, conceptual breakdown of the topic and core intuition.
   - **Example**: A basic theoretical or visual example to explain the concept.
   - **Applications & Use Cases**: Real-world software engineering scenarios where this algorithm or concept is applied.
   - **3 Solved Numerical/Analytical Examples**: Step-by-step mathematical or algorithmic walkthroughs (e.g. solving recurrence relations, stepping through a tree rotation, or tracing a graph traversal). Use actual PYQ problems whenever possible and tag them (e.g. `[April 2018]`).
   - **Previous Year Questions & Solutions**: Dedicated sub-section listing raw past questions paired immediately with 100% complete, self-contained solutions.
8. **Mandatory Syllabus Gap Analysis Audit**: Upon completing note generation for any subject, run the `audit-syllabus-gaps` skill to generate `notes/<semester>/<subject>/Syllabus_Gap_Analysis.md` documenting missing topics, underdeveloped topics, misplaced topics, and the completion percentage.
9. **Automated PYQ Pipeline & 2-Stage Verification Checkpoints**: When fetching previous year question papers (`python3 scripts/pyq_scraper_pipeline.py`), every file MUST pass Primary Verification (Metadata/URL: University, Subject Code, Subject Title) and Secondary Verification (Header Inspection: University Name, Subject Code, Subject Title) before being converted into `.txt` and saved with standardized names (`Month_Year.txt`) in `previous-question-papers/<semester>/<subject>/`. Temporary staging files must be cleaned up immediately.
10. **Autonomous End-to-End Subject Onboarding**: Whenever a new raw syllabus file is added to `syllabus/`, automatically trigger the complete 6-stage `onboard-subject` pipeline to ensure directory alignment, PYQ 2-stage verification, sample question paper generation, 5-part topic notes with self-contained PYQ solutions, and 100% gap analysis verification without requiring manual intervention.
