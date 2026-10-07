---
name: inject-actual-pyqs
description: "Injects actual Previous Year Questions (PYQs) into the topic notes by scanning the previous-question-papers directory and matching questions to topics."
---

# inject-actual-pyqs

This skill ensures that all study notes contain REAL Previous Year Questions (PYQs) instead of generic or placeholder "Sample Questions".

## Trigger
When the user asks to inject, add, or enforce actual previous year questions (PYQs) into the study notes.

## Execution
1. Run the `inject_pyqs.py` script located in the `scripts/` directory of this skill.
2. The script will scan all `notes/` and `previous-question-papers/` directories.
3. It will extract raw questions from the PYQ text files, match them against the topic keywords of each `module-<number>/<topic>.md` file, and append the actual university questions into the "## 5. Previous Year Questions & Solutions" section.
4. If solutions are required but missing, the agent will then fill in the solutions for those newly injected questions using the knowledge base.
