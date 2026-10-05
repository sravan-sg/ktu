# Module 6 Revision Notes

## 1. Quick Summary of Key Concepts
- **Project Scheduling:** Translating effort (Person-Months) into a chronological calendar using task networks. Remember that adding people does *not* proportionally reduce time due to communication overhead.
- **Software Configuration Management (SCM):** The umbrella activity tracking all project changes.
  - *Baseline:* A formally approved and frozen work product.
  - *Version Control:* Tracking "what" and "who" changed a file.
  - *Change Control:* The managerial process (CCB) deciding "if" a change should be allowed.
- **User Interface (UI) Rules (Mandel's 3 Golden Rules):**
  1. Place the user in control (allow Undo, don't force sequences).
  2. Reduce the user's memory load (use smart defaults, carry data forward).
  3. Make the interface consistent (predictable layouts and behaviors).
- **CASE Tools (Computer Aided Software Engineering):** Automated tools to help build software.
  - *Building Blocks:* Environment Architecture -> Portability Services -> Integration Framework -> CASE Tools (all sharing a central Repository).
  - *I-CASE:* Integrated CASE, where tools communicate (e.g., changing a design model automatically updates the code).

## 2. Important Formulas or Algorithms
- *No complex formulas in this module.* However, the concept of **Critical Path Method (CPM)** in scheduling is vital: The critical path is the longest sequence of dependent tasks in a project plan. A delay in any task on the critical path guarantees the final project will be delayed.

## 3. High-Yield PYQ Topics
- **SCM Concept & Baseline:** Expect a question asking to define SCM and the importance of establishing a Baseline to prevent scope creep.
- **Mandel's UI Rules:** A very high-yield, straightforward theory question. Memorize the 3 golden rules and provide one brief example for each (e.g., "Undo" for placing the user in control).
- **CASE Building Blocks:** Draw the 4-layer block diagram (Architecture -> Portability -> Integration -> Tools) to secure full marks.

## 4. Common Pitfalls/Mistakes
- **Confusing Version Control with SCM:** Version control (like Git) is merely a *tool*. SCM is the overarching *management process* that includes baselines, human change control boards, and configuration audits.
- **Misunderstanding "User Memory Load":** Don't interpret this as computer RAM. It explicitly means the *human user's* short-term brain memory (e.g., forcing a user to remember a generated ID number to type on the next page).
- **Upper vs Lower CASE:** 
  - *Upper CASE:* Early phases (Analysis & Design models). 
  - *Lower CASE:* Late phases (Coding & Testing tools).
