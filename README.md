# KTU Engineering Coursework & AI Notes Repository

> **Workspace Overview**: This repository is a personal study, reference, and knowledge-base workspace for **KTU (Kerala Technological University)** Computer Science & Engineering coursework. It integrates structured syllabus extractions, downloaded reference textbooks, AI-converted markdown knowledge bases, and professor-grade study guides.

---

## 📐 Repository Structure

```
ktu/
├── .agents/                            # AI agent configuration & automation skills
│   ├── AGENTS.md                       # Workspace rules & complete project knowledge base
│   └── skills/                         # Automated workflow skills for study material prep
│       ├── review-syllabus/            # Skill 1: Raw syllabus text → syllabus.md study guide
│       ├── download-references/        # Skill 2: Textbook fetcher (curated indexes & web search)
│       └── prepare-knowledge/          # Skill 3: PDF to Markdown conversion via pdfmux
├── syllabus/                           # Canonical raw syllabus files (exported/scraped text)
│   └── Ktunotes.in-CS302...txt         # e.g., CS302 Design & Analysis of Algorithms
├── textbooks/                          # Downloaded PDF reference books at project root
│   └── semester-6/
│       └── design-and-analysis-of-algorithms/
│           ├── Introduction_to_Algorithms_Cormen_3rd_Ed.pdf
│           └── README.md               # Textbook index & download status
├── notes/                              # Semester & Subject-wise study guides & notes
│   └── semester-6/
│       └── design-and-analysis-of-algorithms/
│           ├── Module_I_Detailed_Submodules.md
│           ├── module-1.md ... module_6...md
│           └── knowledge/              # pdfmux converted Markdown knowledge base
└── README.md                           # Workspace overview (this file)
```

---

## 🛠️ Automated Workflows & Custom Skills

This repository uses automated AI agent skills defined under `.agents/skills/`:

1. **Syllabus Ingestion (`review-syllabus`)**:
   - Parses raw syllabus exports from `syllabus/`.
   - Extracts course details, L-T-P structure, exam mark distributions, and module topics.
   - Derives semester using KTU course code conventions (e.g. `CS302` → Semester 6).
   - Generates `notes/<semester>/<subject>/syllabus.md`.

2. **Reference Fetching (`download-references`)**:
   - Reads prescribed textbooks from `syllabus.md`.
   - Queries curated repositories (via Git LFS API) and web sources.
   - Stores PDF reference books under `textbooks/semester-<number>/<subject-name>/`.
   - Maintains an index in `textbooks/semester-<number>/<subject-name>/README.md`.

3. **Knowledge Base Preparation (`prepare-knowledge`)**:
   - Processes downloaded textbook PDFs using `pdfmux`.
   - Outputs AI-readable Markdown files into `notes/<semester>/<subject>/knowledge/`.
   - Generates indexed overview in `knowledge/README.md`.

4. **Dual-Format Note Generation (`generate-module-notes`)**:
   - Synthesizes two complementary note files for each syllabus module using `knowledge/` and canonical texts:
     - `module-x-detailed-notes.md`: In-depth master learning guide (based on `module-1.md`).
     - `module-x-revision-notes.md`: Last-minute revision guide (based on `Module_I_Detailed_Submodules.md`).
   - Ensures simple, easy-to-understand language free of dense jargon while maintaining conceptual depth.

---

## 🎓 Teaching Stance & Standards

- **Intuition First**: Explains *why* algorithms and data structures work, not just *what* they are.
- **Mathematical Rigor**: Provides complete recurrence relation derivations, asymptotic analysis, and formal proofs where relevant.
- **Engineering Trade-offs**: Connects concepts to real-world software engineering (e.g., cache locality, database indexing, network routing, memory bounds).
- **Accuracy**: Grounded directly in canonical reference textbooks (Cormen, Horowitz & Sahni).
