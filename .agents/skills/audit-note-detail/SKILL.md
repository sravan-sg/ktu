---
name: audit-note-detail
description: Scans all generated study notes for a subject and verifies their academic depth, technical rigor, and descriptive quality against the Senior CS Professor standards. Generates a Detail_Audit_Report.md highlighting areas needing expansion.
---

# Academic Depth & Note Detail Audit Pipeline

This skill systematically reads through generated topic notes for a given course subject and evaluates them for depth, clarity, and adherence to the high standards of an advanced engineering curriculum.

---

## Audit Execution Steps

### 1. Global Scan
1. Locate the target subject directory: `notes/<semester>/<subject>/`.
2. Iterate through every module subdirectory (`module-1/` through `module-N/`).
3. For each module, locate and read every topic markdown file (`<topic-kebab-case>.md`).

### 2. Quality & Depth Verification
For every `<topic-kebab-case>.md` file, rigorously evaluate the content against these 4 criteria:

1. **Descriptive Depth & Intuition**: 
   - Does the explanation explicitly teach *why* this concept works, or is it merely a superficial definition?
   - Does it adopt the "Senior CS Professor" stance, providing deep intuition?
2. **Technical Thoroughness**: 
   - Are there complete architectural diagrams, state transition machines, full mathematical derivations, ASCII protocol headers, or robust pseudocode algorithms where applicable?
   - Does it shy away from complexity? If a protocol or algorithm has edge cases, are they explained?
3. **Template Rigor**:
   - In the "3 Solved Numerical/Analytical Examples" section, are the examples actually solved *step-by-step*? Skip-to-the-answer solutions fail this check.
4. **Real-World Engineering Value**:
   - Are the "Applications & Use Cases" specific to real software/systems engineering, or just generic placeholders?

### 3. Report Generation
Generate a comprehensive `Detail_Audit_Report.md` in the subject root (`notes/<semester>/<subject>/Detail_Audit_Report.md`).

The report MUST include:
- **Executive Summary**: A brief overview of the overall quality of the notes across all modules.
- **Flagged Topics Table**: A table listing specific files/topics that failed the depth audit.
  - Columns: `Module`, `Topic File`, `Deficiency Category` (e.g., Lacks Intuition, Weak Examples, Missing Diagrams), `Specific Critique & Action Item`.
- **Exemplary Topics**: Highlight 1-2 topics that perfectly meet the "Senior CS Professor" standard to serve as internal benchmarks.
- **Actionable Correction Plan**: Concrete steps to automatically trigger the expansion of flagged topics (e.g., using `generate-module-notes` to Auto-Expand).

## Note:
Unlike `audit-syllabus-gaps` (which checks for structural completeness and coverage), this skill purely audits the **academic rigor and depth** of existing content.
