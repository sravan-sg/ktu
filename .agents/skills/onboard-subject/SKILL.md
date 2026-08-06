---
name: onboard-subject
description: Autonomous end-to-end subject onboarding pipeline triggered whenever a new course syllabus is added to the syllabus/ folder. Orchestrates directory alignment, syllabus processing, textbook indexing, PYQ scraping with 2-stage verification, sample question paper generation, 5-part modular note generation with self-contained PYQ solutions, and syllabus gap analysis audit.
---

# Master Subject Onboarding & Scaffolding Pipeline

Whenever a new raw syllabus file is added to `syllabus/` or when requested by the user, execute this complete 6-stage autonomous workflow for the target course subject:

```
[Raw Syllabus File in syllabus/]
       │
       ▼
Stage 1: Directory Architecture Alignment (Rule 5)
       │
       ▼
Stage 2: Syllabus Parsing & Exam Focus Synthesis (review-syllabus)
       │
       ▼
Stage 3: Textbook Indexing & Knowledge Base Preparation (download-references & prepare-knowledge)
       │
       ▼
Stage 4: PYQ Scraping, 2-Stage Verification & Sample Question Paper (pyq_scraper_pipeline.py)
       │
       ▼
Stage 5: Modular Note Generation & Auto-Correction Loop (generate-module-notes)
       │
       ▼
Stage 6: Syllabus Gap Analysis Audit & Quality Verification (audit-syllabus-gaps)
```

---

## Detailed Stage Execution Protocol

### Stage 1: Directory Architecture Alignment (Rule 5)
1. Convert the raw subject name into standard **kebab-case** (e.g. `computer-networks`, `design-and-analysis-of-algorithms`).
2. Derive the target semester using the KTU formula (`base = 2*H - 1`, `+1` if last digit is even).
3. Ensure identical, standardized directory naming across all 4 root categories:
   - `syllabus/semester-<number>/<subject-name>/`
   - `previous-question-papers/semester-<number>/<subject-name>/`
   - `textbooks/semester-<number>/<subject-name>/`
   - `notes/semester-<number>/<subject-name>/`

### Stage 2: Syllabus Parsing & Guide Generation (`review-syllabus`)
1. Read the raw syllabus `.txt` file in full.
2. Extract Course Code, Course Name, Credits/L-T-P, Module list (every topic and subtopic), Textbooks, References, and Question Paper Pattern.
3. Write `notes/semester-<number>/<subject-name>/syllabus.md` including a high-yield **Exam Focus — What to Prioritize** synthesis section.

### Stage 3: Textbook Indexing & Knowledge Base (`download-references` & `prepare-knowledge`)
1. Create `textbooks/semester-<number>/<subject-name>/README.md` listing prescribed reference textbooks.
2. Ingest available textbook PDFs and convert to Markdown under `notes/semester-<number>/<subject-name>/knowledge/`.

### Stage 4: PYQ Scraping, 2-Stage Verification & Sample Question Paper
1. Execute `python3 scripts/pyq_scraper_pipeline.py`.
2. Apply **Primary Verification (Link/Metadata)**: Confirm source is KTU, subject code matches, and course title matches.
3. Apply **Secondary Verification (Header Inspection)**: Inspect header block for `APJ ABDUL KALAM TECHNOLOGICAL UNIVERSITY` or `KTU`, subject code, and course title. Fails any non-matching paper.
4. Save verified papers in `previous-question-papers/semester-<number>/<subject-name>/` with standardized names (`Month_Year.txt`).
5. Synthesize and write `previous-question-papers/semester-<number>/<subject-name>/Sample_Question_Paper.txt` following the official KTU Part A, B, C, D, E examination pattern.
6. Clean up temporary staging directories.

### Stage 5: Modular Note Generation & Auto-Correction Loop (`generate-module-notes`)
1. For all modules (1 through N), generate topic detailed notes (`<topic-kebab-case>.md`), `detailed-notes.md`, `revision-notes.md`, and root `README.md`.
2. Enforce the **Mandatory 5-Part Topic Template**:
   - **Explanation**: Conceptual breakdown & core intuition (Senior CS Professor stance).
   - **Example**: Basic theoretical or visual example.
   - **Applications & Use Cases**: Real-world software engineering/systems scenarios.
   - **3 Solved Numerical/Analytical Examples**: Step-by-step mathematical/algorithmic walkthroughs with PYQ session tags.
   - **Previous Year Questions & Solutions**: Dedicated section listing raw past questions paired with **100% complete, self-contained, in-place solutions** (NO shortcut cross-references like *"See Example X above"*).
3. Execute Auto-Correction: Auto-Add missing topics, Auto-Expand underdeveloped topics, Auto-Relocate misplaced topics.
4. Write `Correction_Log.md`.

### Stage 6: Syllabus Gap Analysis Audit (`audit-syllabus-gaps`)
1. Cross-reference all generated module notes against mapped syllabus requirements.
2. Generate `notes/semester-<number>/<subject-name>/Syllabus_Gap_Analysis.md` confirming **100% completion**.
