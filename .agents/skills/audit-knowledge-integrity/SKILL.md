---
name: audit-knowledge-integrity
description: Cross-reference generated study notes against the prescribed textbook markdown files in the knowledge/ folder to ensure factual grounding and prevent hallucination. Generates a Knowledge_Integrity_Audit.md report.
---

# Audit Knowledge Integrity

Perform a cross-referencing audit between the generated module study notes and the AI-extracted textbook markdown files in the `knowledge/` directory to verify academic integrity.

## Steps

### 1. Identify Textbook and Notes
1. For the specified subject (e.g., `notes/semester-6/distributed-computing/`), read the `syllabus.md` to identify the prescribed textbooks.
2. Locate the corresponding markdown files in `notes/<semester>/<subject>/knowledge/`. Ensure they are not empty mocks.
3. Identify all generated study notes under `module-*/<topic>.md`.

### 2. Perform Concept Extraction & Verification
For each generated topic note:
1. Extract the core definitions, algorithms, or concepts discussed in the note.
2. Search the `knowledge/` markdown file(s) for these concepts to verify their presence in the actual textbook. Use semantic search or targeted `grep_search`.
3. Check for specific numeric examples or architectural patterns—if the note contains a specific example that contradicts or is completely absent from the textbook, flag it as ungrounded/hallucinated.

### 3. Missing Topic Scan (Reverse Verification)
Scan the table of contents or index of the `knowledge/` markdown file to ensure that no major chapters required by the syllabus were completely missed in the note generation phase.

### 4. Generate the Audit Report
Create a `Knowledge_Integrity_Audit.md` file in the subject's root directory (`notes/<semester>/<subject>/`). The report MUST include:
- **Grounded Topics:** A list of topics successfully mapped to the textbook, ideally with the chapter/section context.
- **Ungrounded/External Topics:** A list of topics that are present in the notes but missing from the textbook, highlighting potential AI hallucination or the need for a secondary reference book.
- **Missing Topics (Syllabus vs Textbook):** Syllabus topics that are in the textbook but missing from the generated notes.
- **Action Items:** Recommendations for the user or the `generate-module-notes` skill to correct the ungrounded topics.

## Guardrails
- **Performance:** Do not attempt to load the entire 15,000+ line textbook markdown file into context at once. Use targeted searches based on the topic names.
- **Terminology Drift:** Understand that the syllabus and the textbook might use slightly different terminology (e.g., "Processor Pool" vs. "Pool of Processors"). Use fuzzy/semantic reasoning before outright flagging a topic as ungrounded.
