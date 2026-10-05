# Module 4 Revision Notes

## 1. Quick Summary of Key Concepts
- **Coding Standards:** Uniform rules for writing code. Reduces complexity and slashes maintenance costs.
- **Code Walk-through vs Inspection:** Walk-through is informal, author-led. Inspection is formal, moderator-led with strict checklists to find defects.
- **White Box Testing:** Tests internal logic and paths. Uses source code. Done early (Unit testing).
- **Black Box Testing:** Tests external behavior against requirements. Ignorant of source code. Done late (Validation).
- **Cyclomatic Complexity (V(G)):** A mathematical metric representing the number of independent paths in a program. Crucial for Basis Path Testing.
- **Testing Strategy Spiral:** 
  1. *Unit Test:* Tests single module (White box, uses stubs/drivers).
  2. *Integration Test:* Tests interfaces between modules (Top-down/Bottom-up, Regression testing).
  3. *Validation Test:* Tests if customer requirements are met (Black box, Alpha/Beta testing).
  4. *System Test:* Tests software + hardware + network as a whole (Stress, Security, Recovery).

## 2. Important Formulas or Algorithms
- **Cyclomatic Complexity V(G) Formulas:**
  - `V(G) = Edges - Nodes + 2`
  - `V(G) = Predicate Nodes + 1` (A predicate node is an `if`, `while`, or `for` statement).
  - `V(G) = Number of enclosed regions + 1` (exterior region).
  *Note: The calculated V(G) equals the exact number of test cases you must write to achieve 100% basis path coverage.*

## 3. High-Yield PYQ Topics
- **Alpha vs Beta Testing:** A highly repeated question. Know the difference in location (developer site vs customer site) and environment control.
- **Unit vs Integration Testing:** Be able to explain the progression from testing one module to combining them, and the necessity of Stubs/Drivers.
- **White Box vs Black Box:** The most fundamental testing theory question. Contrast internal logic vs external behavior.
- **Calculating V(G):** You may be given a simple pseudocode block or a flow graph and asked to calculate its Cyclomatic Complexity.

## 4. Common Pitfalls/Mistakes
- **Confusing Verification and Validation:** 
  - *Verification:* "Are we building the product right?" (Code matches design).
  - *Validation:* "Are we building the right product?" (Code solves the customer's actual problem).
- **"Big Bang" Integration Trap:** When asked about integration, never recommend combining all modules at once. Always explain that incremental integration (Top-down or Bottom-up) is required to isolate interface errors.
- **Miscalculating Predicate Nodes:** When using `V(G) = P + 1`, remember that a compound condition like `if (a > 0 AND b < 1)` actually counts as TWO predicate nodes, because it evaluates two separate conditions.
