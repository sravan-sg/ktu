---
name: review-syllabus
description: Read a course syllabus file from the syllabus/ folder and generate a structured notes/<semester>/<subject>/syllabus.md study guide. Use when the user wants to review, process, summarize, or scaffold notes from a syllabus.
---

# Syllabus → Study Guide

Turn a raw syllabus file into a concise, accurate `syllabus.md` study guide, written from the perspective of a **senior Computer Science professor** advising students on how to master the course.

Syllabus files live in `syllabus/`. They are messy PDF/scrape exports (run-together words, collapsed formatting). Read carefully and reconstruct intended structure; do not quote verbatim.

## Modes

Pick the mode from what the user provides:

- **Mode 1 — single file.** The user gives a specific syllabus file path (or a subject name that resolves to exactly one file in `syllabus/`). Process only that file.
- **Mode 2 — batch.** No file is given. List every syllabus file in the `syllabus/` directory and process each one, repeating the Steps below per file.

In both modes, run the **Pre-write check** before generating notes for a subject.

## Pre-write check (run per subject, every time)

Before writing notes for a subject, check whether `notes/<semester>/<subject>/` already exists and contains files.

- If it does **not** exist (or is empty), proceed.
- If it **does** exist with files, **stop and ask the user** whether to re-create the notes for that subject. Only on explicit confirmation, **delete all files in that subject directory** and regenerate from scratch. If the user declines, skip that subject and move on (in batch mode, continue to the next file).
- In batch mode, collect the existing subjects and confirm them together where possible, rather than asking once per file mid-run.

## Steps

1. **Read** the chosen syllabus file in full.

2. **Extract** these facts directly from the file — do not invent or supplement from outside knowledge:
   - Course code and full course name
   - Credits / L-T-P structure
   - Module list, including **every single topic and subtopic** within each module (preserve the exact syllabus ordering exhaustively, as this `syllabus.md` file serves as the sole source of truth forwarded to the `generate-module-notes` and `prepare-knowledge` agents)
   - Textbooks and references (note which modules each textbook covers, if stated)
   - Grading / exam structure (internal marks, end-sem pattern, per-module weightage, question-paper pattern)

3. **Determine the semester.** Prefer an explicit statement in the syllabus. If absent, derive it from the course code using the **KTU 2015/2016 B.Tech scheme** convention on the 3-digit number `H..L` (hundreds digit `H`, last digit `L`):
   - base semester = `2*H - 1`  (so `2xx`→3, `3xx`→5, `4xx`→7)
   - if `L` is **even**, add 1 to the base
   - examples: CS201 → S3, CS204 → S4, CS301 → S5, **CS302 → S6**, CS401 → S7

   Use the format `semester-N` for the directory. State the derived semester in your summary so the user can correct it. If the code doesn't fit this convention, ask.

4. **Create the directory** `notes/<semester>/<subject>/`, where `<subject>` is kebab-case (matching the existing `notes/computer-graphics` convention), e.g. `notes/semester-5/design-and-analysis-of-algorithms/`.

5. **Write** `syllabus.md` inside that directory with exactly these sections, in order:

   ```markdown
   # <Course Code> — <Course Name>

   > <one-line scope: credits, L-T-P, prerequisite if any>

   ## Grading Criteria
   <internal vs end-sem split, per-module weightage, question-paper pattern — as a compact table or bullets>

   ## Textbooks
   <numbered list; mark which modules each covers; list references separately if present>

   ## Modules
   ### Module I — <title>
   - <topic>
   - <topic>
   ### Module II — <title>
   ...
   <every module, every topic, in syllabus order>

   ## Exam Focus — What to Prioritize
   <professor's synthesis: 4-8 bullets naming the highest-yield topics for acing the exam, justified by mark weightage and the question-paper pattern. Call out where the marks concentrate and which topics recur. This is the ONLY section that is analysis rather than extraction.>
   ```

## Rules

- **Verify before writing.** Every fact in the document must trace back to the syllabus file. If you cannot confirm something (e.g. semester), ask rather than assume.
- **Be brief and accurate.** No filler, no generic study advice. The "Exam Focus" synthesis must be grounded in the actual mark distribution stated in the syllabus.
- **Never delete or overwrite existing notes without explicit confirmation.** Re-creating a subject's notes deletes every file under `notes/<semester>/<subject>/` — only do this after the user confirms (see Pre-write check).
