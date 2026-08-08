---
name: generate-module-notes
description: Generate comprehensive, highly descriptive modular study notes following the module directory structure (notes/semester-<number>/<subject-name>/module-<number>/) with built-in syllabus mapping, textbook knowledge integration, cross-referencing audit, auto-correction loop, sample question paper generation, and gap analysis logging.
---

# Master Modular Study Notes Pipeline (With Auto-Correction & Quality Audit)

Generates topic-wise detailed notes, module revision guides, and subject root documentation while automatically auditing and self-correcting syllabus gaps according to the strict workspace directory structure:

```
notes/semester-<number>/<subject-name>/
├── README.md                           # Master subject guide linking all topic detailed notes & revision notes
├── syllabus.md                         # Extracted syllabus, grading criteria & exam focus
├── Syllabus_Gap_Analysis.md            # Audit report & completion metrics
├── Correction_Log.md                   # Auto-correction execution log
├── knowledge/                          # Ingested PDF-to-Markdown reference texts & README.md index
├── module-1/                           # Module 1 directory
│   ├── detailed-notes.md               # Detailed notes index for Module 1 (links to topic files)
│   ├── <topic-1-kebab-case>.md         # Individual detailed notes for Topic 1
│   ├── <topic-2-kebab-case>.md         # Individual detailed notes for Topic 2
│   └── revision-notes.md               # Last-minute revision notes for Module 1
├── module-2/                           # Module 2 directory
│   ├── detailed-notes.md
│   ├── <topic-1-kebab-case>.md ...
│   └── revision-notes.md
...
```

---

## Core Guidelines & Quality Constraints

- **MANDATORY Knowledge Ingestion First**: Before writing any note section, read and inspect all converted textbook Markdown files in `notes/semester-<number>/<subject-name>/knowledge/` and reference textbooks in `textbooks/semester-<number>/<subject-name>/`. Extract exact definitions, proofs, pseudocode, and numerical examples directly from prescribed textbooks (Tanenbaum, Forouzan, Peterson & Davie, Cormen, etc.).
- **MANDATORY Exhaustive Descriptive Depth**: Every topic note must be **in-depth and highly descriptive**. Avoid superficial one-liners or quick bullet summaries. Include complete architectural diagrams, state transition machines, full mathematical derivations, ASCII protocol headers, and pseudocode algorithms.
- **MANDATORY PYQ & Sample Question Paper Integration**: Read and analyze all question papers in `previous-question-papers/semester-<number>/<subject-name>/` (including past university papers and synthesized `Sample_Question_Paper.txt`). Incorporate past questions with **100% self-contained, in-place solutions** (NO shortcut pointers like *"See Example X above"* or *"See Section 1"*).
- **Mandatory 5-Part Topic Structure**: Every single topic markdown file (`<topic-kebab-case>.md`) MUST strictly contain all 5 of these sections:
  1. **Explanation**: A clear, highly descriptive conceptual breakdown of the topic and core intuition.
  2. **Example**: A basic theoretical, visual, or structural diagram example explaining the concept.
  3. **Applications & Use Cases**: Real-world software/systems engineering scenarios where this algorithm/concept is applied.
  4. **3 Solved Numerical/Analytical Examples**: Step-by-step mathematical or algorithmic walkthroughs (recurrences, tree rotations, graph traces, subnetting math), tagged with PYQ sessions where applicable (e.g. `[April 2018]`, `[May 2019]`, `[Sample Question Paper]`).
  5. **Previous Year Questions & Solutions**: Sub-section listing raw past questions paired immediately with full, complete, in-place solutions.
- **Senior CS Professor Persona**: Teach *why* concepts work, combining deep intuition, step-by-step mathematical derivations, clear code snippets, and real-world engineering trade-offs.

---

## Automated Verification & Self-Correction Workflow

Whenever this skill is executed for any semester and subject, it MUST automatically execute the following 5-step loop:

### Step 1: Syllabus Mapping (Pre-check)
1. Locate target subject directory: `notes/semester-<number>/<subject-name>/`.
2. Read the official syllabus document `notes/semester-<number>/<subject-name>/syllabus.md` (or raw file in `syllabus/semester-<number>/<subject-name>/`).
3. Extract an explicit, exhaustive list of every topic and subtopic belonging to Module 1 through Module N.

### Step 2: Content Verification & Audit (Cross-Referencing)
Scan all existing module folders (`module-1/` through `module-N/`) and compare existing note files against the mapped syllabus to identify:
- **Missing Topics**: Syllabus topics with zero coverage in `module-X/`.
- **Underdeveloped Topics**: Topics that exist but lack standard KTU depth, complete derivations, step-by-step walkthroughs, or are missing any of the mandatory 5 sections.
- **Misplaced Topics**: Topics documented in the wrong module directory.

### Step 3: Automatic Self-Correction (Autonomous Execution)
Fix all issues identified in Step 2 immediately without asking for user permission:
- **Auto-Add**: Generate comprehensive, KTU-standard notes for any Missing Topics following the 5-part template and place them into the correct `module-X/<topic-kebab-case>.md` file.
- **Auto-Expand**: Rewrite and expand any Underdeveloped Topics so they meet university-level academic depth and complete all 5 mandatory sections.
- **Auto-Relocate**: Move any Misplaced Topics out of their current file into the correct `module-X/` directory and update index links.

### Step 4: Generate & Update Modular Notes & Indices
For all modules (Module 1 through Module N):
1. Write/update `<topic-kebab-case>.md` files for all topics.
2. Write/update `module-<number>/detailed-notes.md` (master index for Module X).
3. Write/update `module-<number>/revision-notes.md` (4-part submodule summary).
4. Update subject root `README.md` to link all detailed notes and revision guides.

### Step 5: Logging & Report Generation
Output two log files in `notes/semester-<number>/<subject-name>/`:
1. **`Correction_Log.md`**: Detailing exact actions taken during Step 3 (items Auto-Added, Auto-Expanded, or Auto-Relocated).
2. **`Syllabus_Gap_Analysis.md`**: Global verification report detailing:
   - Module-by-module syllabus coverage
   - Audit checklist (5-part template, self-contained PYQs, folder structure)
   - Final Completion Percentage (100% target)
