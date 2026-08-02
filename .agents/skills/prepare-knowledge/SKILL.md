---
name: prepare-knowledge
description: Convert PDF reference textbooks and materials inside a subject's textbooks folder to clean markdown files in the subject's knowledge folder using pdfmux or marker, ensuring a fully AI-readable knowledge base. Use when the user requests converting textbooks to markdown or preparing the knowledge base for a subject.
---

# Prepare Subject Knowledge Base

Automatically convert downloaded reference books, textbooks, or documents inside a subject's `textbooks/` directory into a high-fidelity, AI-readable markdown format inside the subject's `knowledge/` directory using the project's local `pdfmux` installation.

## Steps

### 1. Locate the Subject Directories

1. Find the subject's note directory under `notes/`: `notes/<semester>/<subject>/` (e.g., `notes/semester-6/design-and-analysis-of-algorithms/`).
2. Verify that the root `textbooks/` directory `textbooks/semester-<number>/<subject-name>/` exists and contains the downloaded PDF documents (e.g., `Introduction_to_Algorithms_Cormen_3rd_Ed.pdf`).

### 2. Create the Knowledge Directory

Ensure that the target directory `notes/<semester>/<subject>/knowledge/` exists. If not, create it.

### 3. Run PDF-to-Markdown Conversion

For each PDF file in `textbooks/semester-<number>/<subject-name>/`:
1. Check if the output markdown file already exists in `notes/<semester>/<subject>/knowledge/`. If it does, and you are not instructed to overwrite it, you may skip it.
2. Formulate the output markdown path: `notes/<semester>/<subject>/knowledge/<pdf_name_no_ext>.md`.
3. Use the `run_command` tool to execute `pdfmux` using the local python virtual environment `venv`:
   * *Command:* `venv/bin/pdfmux convert "textbooks/semester-<number>/<subject-name>/<file>.pdf" -o "notes/<semester>/<subject>/knowledge/<file_no_ext>.md" --quality standard`
   * *Quality Presets:* Use `--quality standard` (balanced) or `--quality high` (ML-based layout analysis) to preserve mathematical formulas, code blocks, and complex tables accurately.
4. Verify that the command completes successfully and the markdown output is written.

### 4. Create a Knowledge Base Index (README.md)

Create or update a central index file `notes/<semester>/<subject>/knowledge/README.md` containing:
- A title: `# Knowledge Base: <Subject Name>`
- A table listing all converted markdown documents, their local file links, and the syllabus modules or topics they cover.
- A confirmation section noting that the knowledge base is fully processed and ready to be read by the AI agent to generate study notes.

## Rules & Guardrails

- **Overwriting Safety:** If markdown files already exist in the `knowledge/` directory, ask the user before overwriting them.
- **Accuracy:** Ensure tables and math symbols are extracted in readable Markdown formats. Do not alter the original PDF files.
- **Resource Management:** HuggingFace models used by pdfmux backends are cached in `~/.cache/huggingface/`. Do not delete these caches.
