---
name: generate-sample-papers
description: Generate 3 unique Sample Question Papers for a subject by analyzing the pattern and topics of existing previous year questions (PYQs). It stores the generated papers in the dedicated sample-question-papers/ root directory.
---

# Sample Question Paper Generation Skill

This skill is responsible for synthesizing mock sample question papers for any given semester and subject, based on the official KTU (Kerala Technological University) examination pattern and the historical questions present in the repository.

## Execution Workflow

1. **Locate Source Materials**:
   - Navigate to `previous-question-papers/semester-<number>/<subject-name>/`.
   - Read and analyze all available university PYQs (e.g. `April_2018.txt`, `December_2019.txt`) to understand the topic distribution and difficulty level.

2. **Directory Architecture Check**:
   - Ensure the directory `sample-question-papers/semester-<number>/<subject-name>/` exists. If it does not, create it in compliance with the updated 5-root repository architecture (Rule 5).

3. **Synthesize Papers with Double Verification**:
   - Generate exactly **3 unique Sample Question Papers**.
   - **Double Verification Rule**: Before generating any question, you MUST perform a strict verification step:
     1. Verify the question aligns with a topic explicitly listed in the official `syllabus.md`.
     2. Verify the question style, difficulty, and format matches the historical `previous-question-papers/`.
     Do NOT invent topics outside the syllabus or use question formats not seen in PYQs.
   - Each paper must rigorously follow the KTU Part A, B, C, D, E examination pattern:
     - **Part A**: 4 questions × 3 marks (Total 12)
     - **Part B**: Answer 2 full questions out of 3, each 9 marks (Total 18)
     - **Part C**: 4 questions × 3 marks (Total 12)
     - **Part D**: Answer 2 full questions out of 3, each 9 marks (Total 18)
     - **Part E**: Answer 4 questions out of 6, each 10 marks (Total 40)
   - Ensure a balanced mix of theoretical explanations, derivations, and numerical problems across all 5 modules.
   - Do NOT simply duplicate existing PYQs verbatim; paraphrase, combine, or invent new reasonable questions that pass the double verification check.

4. **Save Output as Markdown**:
   - Write the generated papers in Markdown format (`.md`) to:
     - `sample-question-papers/semester-<number>/<subject-name>/Sample_Question_Paper_1.md`
     - `sample-question-papers/semester-<number>/<subject-name>/Sample_Question_Paper_2.md`
     - `sample-question-papers/semester-<number>/<subject-name>/Sample_Question_Paper_3.md`

## Integration Note
This skill is automatically triggered by the `onboard-subject` pipeline (Stage 4) whenever a new subject is scaffolded, but can also be triggered manually by the user.
