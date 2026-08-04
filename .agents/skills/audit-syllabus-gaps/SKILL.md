---
name: audit-syllabus-gaps
description: Perform an exhaustive academic audit and gap analysis on study materials across semesters and subjects by cross-referencing notes against syllabus requirements, generating a Syllabus_Gap_Analysis.md report for each subject.
---

# Academic Audit & Syllabus Gap Analysis Pipeline

Generates a detailed `Syllabus_Gap_Analysis.md` verification report for each course subject by systematically auditing documented module notes against canonical syllabus requirements.

---

## Audit Execution Steps

### 1. Global Discovery
1. Scan `notes/` directory to identify all existing `<semester>` folders (e.g., `notes/semester-6/`).
2. Inside each semester folder, scan and list all individual `<subject>` directories (e.g., `notes/semester-6/design-and-analysis-of-algorithms/`).

### 2. Map Syllabus Topics
For each `<semester>/<subject>`:
1. Locate the canonical syllabus file in `syllabus/<semester>/<subject>/` or `notes/<semester>/<subject>/syllabus.md`.
2. Extract the complete, exhaustive topic list for all modules (Module 1 through Module N).

### 3. Note Content Audit & Verification
For each topic in the syllabus, inspect the module notes in `notes/<semester>/<subject>/module-<number>/`:
1. **Directory Alignment**: Verify that notes follow `notes/semester-<number>/<subject-name>/module-<number>/`.
2. **Topic Coverage**: Check if the topic has a dedicated markdown file (`<topic-kebab-case>.md`).
3. **Mandatory 5-Part Template Verification**: Confirm every topic note strictly contains:
   - **Explanation**
   - **Example**
   - **Applications & Use Cases**
   - **3 Solved Numerical/Analytical Examples**
   - **Previous Year Questions & Solutions**
4. **PYQ Self-Contained Solution Check**: Verify all PYQs are written in full and solved completely in-place with **zero** shortcut cross-references (such as *"See Example X above"* or *"See Section 1"*).

### 4. Gap Analysis Calculation
Calculate:
- **Missing Topics**: Topics in the syllabus with zero coverage in `module-<number>/`.
- **Underdeveloped Topics**: Topics present but missing depth (e.g. missing explicit formulas, missing deletion cases, or missing proofs).
- **Misplaced Topics**: Topics located in the wrong module folder compared to syllabus specification.
- **Completion Percentage**: Estimated completion based on syllabus coverage and quality checks.

### 5. Generate Report `Syllabus_Gap_Analysis.md`
Save a report named `Syllabus_Gap_Analysis.md` at the subject root `notes/<semester>/<subject>/Syllabus_Gap_Analysis.md` with:
- Executive Summary & Overall Completion %
- Module-by-Module Coverage & Audit Breakdown
- Missing, Underdeveloped, and Misplaced Topics
- Verification Checklist & Quality Audit Table
- Actionable Recommendations for 100% Academic Perfection
