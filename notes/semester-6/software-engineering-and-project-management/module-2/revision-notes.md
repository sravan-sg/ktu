# Module 2 Revision Notes

## 1. Quick Summary of Key Concepts
- **Capability Maturity Model (CMM):** A 5-level framework measuring a company's software process maturity: (1) Initial/Ad-hoc, (2) Repeatable, (3) Defined, (4) Managed, (5) Optimizing.
- **ISO 9000:** An international quality standard requiring companies to document their quality processes and pass external audits.
- **Requirement Elicitation:** Gathering needs from stakeholders. Hard due to problems of scope, understanding, and volatility. Methods include Interviews, FAST (Joint Application Design), and Use Cases.
- **Software Prototyping:** Building a quick, working model to clarify requirements. 
  - *Throwaway:* Built quickly to test UI/concept, then discarded to prevent maintenance nightmares.
  - *Evolutionary:* Built robustly and refined continuously until it becomes the final product.
- **Analysis Principles & Specification:** The process of taking elicited requirements, analyzing them for feasibility, creating data/control flow models, and formally documenting them into a Software Requirements Specification (SRS) document.

## 2. Important Formulas or Algorithms
- *No strict mathematical formulas in this module.* The focus is on theoretical framework definitions and process models. 

## 3. High-Yield PYQ Topics
- **CMM Levels:** Almost guaranteed to appear. Memorize all 5 levels in exact order and the defining characteristic of each (e.g., Level 4 is quantitative measurement).
- **Prototyping Cost/Benefit:** Be ready to explain the counter-intuitive economic reality that building a "throwaway" prototype saves money by preventing late-stage defect discovery.
- **Elicitation Techniques:** Memorize FAST and Use Cases. Explain why standard interviews often fail (the "telephone game" effect).

## 4. Common Pitfalls/Mistakes
- **CMM Level 3 vs Level 4:** Students frequently confuse these. Level 3 (Defined) means the process is documented in a manual. Level 4 (Managed) means the process is actively measured using statistical data (metrics like bugs-per-line).
- **Prototyping Trap:** When asked about the prototyping model, explicitly mention the danger of the "throwaway" code being forced into production by management. This shows a deep engineering understanding.
- **ISO vs CMM:** Remember that ISO 9000 is generic (works for car factories and software firms alike) and focuses on adherence to documentation. CMM is specifically designed for software engineering maturity.
