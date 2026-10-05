# Module 5 Revision Notes

## 1. Quick Summary of Key Concepts
- **Software Maintenance:** Consumes up to 80% of a project's lifecycle cost.
- **Types of Maintenance:**
  - *Corrective:* Fixing deployed bugs.
  - *Adaptive:* Updating software to run in a new environment (new OS, new DB).
  - *Perfective:* Adding new features requested by users (consumes the most effort).
  - *Preventive:* Refactoring and reengineering code to prevent future deterioration.
- **Risk Management:** Mitigating potential future problems before they cause failure.
  - *Categories:* Project Risks (budget/staff), Technical Risks (design/architecture), Business Risks (market/sales).
  - *RMMM:* Risk Mitigation (proactive prevention), Monitoring (tracking probability), Management/Contingency (reactive safety nets).
- **The 4 P's of Project Management:** The core elements required for success, prioritized as:
  1. *People:* Motivating and organizing the human talent (the most critical factor).
  2. *Product:* Rigidly defining the scope and constraints.
  3. *Process:* Selecting the framework (Waterfall, Agile) that fits the product.
  4. *Project:* Tracking metrics and course-correcting deviations from the plan.

## 2. Important Formulas or Algorithms
- *No strict mathematical formulas in this module.* However, understand the statistical evaluation used in Risk Projection: calculating the **Risk Exposure (RE)**.
  - `RE = Probability * Cost of Impact`

## 3. High-Yield PYQ Topics
- **Types of Maintenance:** Highly testable. Memorize all four (Corrective, Adaptive, Perfective, Preventive) and be able to give a concrete example of each.
- **The 4 P's (People, Product, Process, Project):** A frequent 9-mark essay question. Elaborate on each 'P' and explicitly state that *People* is the most important element because software engineering is a human-driven intellectual process.
- **RMMM (Risk Mitigation, Monitoring, and Management):** Be prepared to write short notes explaining the difference between proactive Mitigation and reactive Management (contingency).

## 4. Common Pitfalls/Mistakes
- **Confusing Adaptive and Perfective Maintenance:** 
  - *Adaptive* means the environment changed around the software, forcing the software to adapt just to survive (e.g., upgrading from Windows 10 to 11). 
  - *Perfective* means the user wants the software to do something entirely new and better (e.g., adding a Dark Mode UI).
- **Misidentifying a Risk vs an Issue:** If you are asked to identify a risk in an exam scenario, do not write a problem that has already occurred. Write a problem that *might* occur (e.g., "The API *might* fail under load," not "The API failed").
- **Ignoring the Order of the 4 P's:** The order matters. You cannot plan the *Project* (schedule) until you define the *Process*. You cannot define the *Process* until you know the *Product* scope. And none of it matters without the *People*.
