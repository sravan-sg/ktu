# Module 3 Revision Notes

## 1. Quick Summary of Key Concepts
- **Software Scope:** The definitive boundary of the project (Data, Function, Constraints). Bounding scope is the mandatory first step before estimation to prevent scope creep.
- **COCOMO:** An empirical estimation model using KLOC. Three modes:
  - *Organic:* Small, simple, experienced team.
  - *Semi-detached:* Medium complexity, mixed team.
  - *Embedded:* Highly constrained hardware/software, critical innovation.
- **Staffing (Brooks' Law):** "Adding manpower to a late project makes it later" due to communication overhead. Staffing follows a bell-shaped Rayleigh curve, not a flat line.
- **Design Principles:** Abstraction (hiding complexity), Information Hiding (protecting local data via interfaces), Modularity.
- **Cohesion & Coupling (CRITICAL):**
  - *Cohesion:* Internal strength. Aim for HIGH (Functional cohesion).
  - *Coupling:* External dependency. Aim for LOW (Data coupling). Avoid Content coupling.
- **Top-Down vs Bottom-Up:** Top-down decomposes from the main architecture (uses stubs). Bottom-up integrates from the utility modules (uses drivers).
- **Stepwise Refinement:** Iteratively adding algorithmic detail to a high-level function statement until code can be written.

## 2. Important Formulas or Algorithms
- **Basic COCOMO Formulas:**
  - Effort (E) = `a * (KLOC)^b` (in Person-Months)
  - Duration (D) = `c * (E)^d` (in Months)
  - Staffing = `E / D` (in Persons)
  *(Note: You will usually be given the constants a, b, c, d in the exam).*

## 3. High-Yield PYQ Topics
- **COCOMO Numerical:** The syllabus mandates 60% analytical/numerical questions. Basic COCOMO effort/duration calculations are highly likely. Memorize the formula structure.
- **Cohesion vs Coupling:** A classic theory question. Always summarize with "Maximize Cohesion, Minimize Coupling" and provide the definitions.
- **Brooks' Law:** Understand *why* it happens (exponential increase in communication paths: `N(N-1)/2`).
- **Information Hiding:** Explain how it localizes errors and prevents the "ripple effect" of bugs across modules.

## 4. Common Pitfalls/Mistakes
- **Calculating Staffing incorrectly:** Students often forget that `Staffing = Effort / Duration`. If Effort is 100 PM and Duration is 10 M, Staffing is 10 people.
- **Mixing up Cohesion and Coupling:** 
  - *Trick to remember:* Cohesion = **Co** (Together inside). Coupling = **Couple** (Two different things attached).
- **Misunderstanding Stubs vs Drivers:** 
  - Top-down uses **Stubs** (fake sub-modules below). 
  - Bottom-up uses **Drivers** (fake main-modules above).
