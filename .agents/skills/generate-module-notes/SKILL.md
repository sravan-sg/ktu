---
name: generate-module-notes
description: Generate comprehensive modular study notes following the module directory structure (notes/semester-<number>/<subject-name>/module-<number>/). Produces topic-wise detailed notes linked via detailed-notes.md, 1 revision-notes.md per module, and updates the subject root README.md. Use when generating, scaffolding, or updating course notes.
---

# Generate Modular Study Notes Pipeline

Generates topic-wise detailed notes and module revision notes according to the strict workspace directory structure:

```
notes/semester-<number>/<subject-name>/
├── README.md                           # Master subject guide linking all topic detailed notes & module revision notes
├── syllabus.md                         # Extracted syllabus, grading criteria & exam focus
├── knowledge/                          # Ingested PDF-to-Markdown reference texts
├── module-1/                           # Module 1 directory
│   ├── detailed-notes.md               # Detailed notes index for Module 1 (links to topic files)
│   ├── <topic-1>.md                    # Individual detailed notes for Topic 1
│   ├── <topic-2>.md                    # Individual detailed notes for Topic 2
│   └── revision-notes.md               # Last-minute revision notes for Module 1
├── module-2/                           # Module 2 directory
│   ├── detailed-notes.md
│   ├── <topic-1>.md ...
│   └── revision-notes.md
...
```

---

## Core Guidelines & Style Constraints

- **MANDATORY Knowledge Ingestion First**: Before writing any note section, you MUST first read and inspect all converted textbook Markdown files in the subject's `knowledge/` directory (`notes/semester-<number>/<subject-name>/knowledge/`). Extract exact definitions, proofs, pseudocode, and numerical examples directly from these source texts.
- **Simplicity & Clarity**: Write in plain, clear, easy-to-understand language. Avoid dense jargon or unnecessarily complex terms. Introduce technical terms only after giving simple intuitive explanations.
- **Senior CS Professor Persona**: Teach *why* concepts work, not just *what* they are. Combine intuition, step-by-step mathematical derivations, clear code snippets, and real-world engineering use-cases.
- **100% Syllabus Coverage**: Ensure every topic listed for Module X in `syllabus.md` gets its own dedicated topic markdown file (`<topic-name>.md`) inside `module-X/`.

---

## Step-by-Step Execution Plan

### Step 1: Read Knowledge Base & Syllabus
1. Locate target subject directory: `notes/semester-<number>/<subject-name>/`.
2. Read `syllabus.md` to extract Module X title, submodules, and full list of topics.
3. List and inspect all Markdown files in `knowledge/`. Extract textbook formulas, code, and numerical problems.

---

### Step 2: Create Module Directory `module-<number>/`

Create directory `notes/semester-<number>/<subject-name>/module-<number>/`.

---

### Step 3: Write Topic-Wise Detailed Notes Files

For each topic in Module X:
- Create a dedicated file: `notes/semester-<number>/<subject-name>/module-<number>/<topic-kebab-case>.md`.
- Include core intuition, theoretical framework, algorithms & pseudocode, mathematical derivations, comparative tables, real-world systems insights, and solved exam problems.

---

### Step 4: Write `module-<number>/detailed-notes.md`

Create `notes/semester-<number>/<subject-name>/module-<number>/detailed-notes.md`:
- Serves as the master index for Module X.
- Provides a summary overview of the module.
- Includes clickable relative markdown links to every `<topic-kebab-case>.md` file created in Step 3.

---

### Step 5: Write `module-<number>/revision-notes.md`

Create `notes/semester-<number>/<subject-name>/module-<number>/revision-notes.md`:
- Standardized 4-part submodule template (*Explanation, Real-World Example, Applications & Use Cases, 3 Solved Numerical Micro-Examples*) for each topic in Module X.

---

### Step 6: Create or Update Subject Root `README.md`

Create or update `notes/semester-<number>/<subject-name>/README.md`:
- **Header & Scope**: Subject code, title, semester, credits, and course overview.
- **Detailed Notes Section**: Table of Contents listing every module and linking to all topic-wise detailed notes files (`[Topic Name](module-X/topic-name.md)`).
- **Revision Notes Section (Final Section)**: Dedicated section providing direct links to the revision notes file of each module (`[Module X Revision Notes](module-X/revision-notes.md)`).
