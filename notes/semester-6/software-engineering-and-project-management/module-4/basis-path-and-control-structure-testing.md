# Basis Path and Control Structure Testing

## 1. Explanation
These are advanced **White Box** testing techniques used to guarantee that the internal logic of a program has been comprehensively tested.

**1. Basis Path Testing:**
Proposed by Tom McCabe, this technique enables the test case designer to derive a logical complexity measure of a procedural design (McCabe's Cyclomatic Complexity) and use this measure as a guide for defining a basis set of execution paths.
- **Cyclomatic Complexity (V(G)):** A software metric that provides a quantitative measure of the logical complexity of a program.
- **The Rule:** If V(G) = 4, the tester must write exactly 4 test cases to guarantee that every independent path through the program has been executed at least once.

**How to calculate V(G) using a Flow Graph:**
A flow graph uses nodes (circles) for code statements and edges (arrows) for control flow.
- *Formula 1:* V(G) = Edges - Nodes + 2
- *Formula 2:* V(G) = Predicate Nodes + 1 (A predicate node is a condition like `if` or `while` that branches).
- *Formula 3:* V(G) = Number of regions in the flow graph.

**2. Control Structure Testing:**
Basis path testing is a subset of control structure testing. Other techniques include:
- **Condition Testing:** Exercises the logical conditions contained in a program module (e.g., ensuring `if(a > 0 AND b < 5)` is tested for all truth combinations).
- **Loop Testing:** Focuses exclusively on the validity of loop constructs. Tests include bypassing the loop entirely, exactly one pass, exactly two passes, `m` passes, and maximum `n` passes (boundary testing).

## 2. Example
Consider this pseudo-code:
```python
1. function calculate(x):
2.    if x > 10:
3.        print("High")
4.    else:
5.        print("Low")
6.    return
```
- **Predicate Nodes:** There is 1 predicate node (Line 2: `if x > 10`).
- **Cyclomatic Complexity:** V(G) = 1 + 1 = 2.
- **Basis Paths:** 
  - Path 1: 1 -> 2 -> 3 -> 6
  - Path 2: 1 -> 2 -> 4 -> 5 -> 6
- **Test Cases:** Because V(G) = 2, we need exactly 2 test cases. Test Case 1: `x = 15`. Test Case 2: `x = 5`. This guarantees 100% path coverage.

## 3. Applications & Use Cases
- **Safety-Critical Avionics (DO-178C):** The FAA requires that all flight control software achieves 100% Modified Condition/Decision Coverage (MCDC). Basis path and condition testing are legally mandated to mathematically prove that no dead code exists and every loop functions safely.
- **Automated Test Coverage:** Modern CI/CD tools (like SonarQube or Istanbul) automatically calculate cyclomatic complexity and flag functions with V(G) > 10 as "Too Complex," forcing developers to refactor the code before it is allowed to merge.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: A flow graph has 14 edges and 11 nodes. Calculate the Cyclomatic Complexity and state its significance.**
*Analysis:* Using the formula V(G) = E - N + 2.
V(G) = 14 - 11 + 2 = 5.
*Significance:* The cyclomatic complexity is 5. This means there are 5 linearly independent paths through the code. The tester must write exactly 5 distinct test cases to achieve 100% basis path coverage.

**Example 2: A module has 4 `if` statements and 1 `while` loop. Calculate V(G).**
*Analysis:* Each `if` and `while` represents a predicate node (a node where the flow branches).
Number of predicate nodes = 4 + 1 = 5.
Using the formula V(G) = Predicate Nodes + 1.
V(G) = 5 + 1 = 6.

**Example 3: In loop testing, why is it critical to test "exactly one pass" and "maximum n passes"?**
*Analysis:* "Exactly one pass" checks if the initialization logic is correct. "Maximum n passes" checks for boundary errors (off-by-one errors) and ensures the loop terminates correctly without causing a buffer overflow or infinite loop.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[December 2019]** a) Define any four types of System testing b) Differentiate between stamp coupling and content coupling.
**[May 2024]** b) Explain Democratic Decentralised team organization and Controlled Decen- (2) tralised team organi zatton (e) Page 3 of4 -,1 qlgGsmt2302 18 4 Whd ale fu basic principles of project scheduling?
**[May 2023]** b) What is the purpose of integration testing?
**[May 2023]** Cost required to develop the product 13 a) Explain about Unit testing in detail.
**[May 2024]** complexity { int i, j, k; for (i=0 ; i<:\ ; i+r) plil: l; for (i:2 ; i<:|rl ; i#) { k: p[i]; j=l; - ufiile (atptj-lll > alkl { plil:pli-ll; 'r  j-; ) p[i]:k; ) 14  Explain any three types of Black box testing.
**[May 2019]** D by the term system testing?
**[July 2021]** (3) Explain basic path coverage testing.
**[January 2024]** b) Explain basic path coverage testing with example.
**[December 2019]** Explain different types of cohesion b) Explain stepwise refinement c) How Black box testing differ from White box testing (5) (s) (s) (s) (5) (s) (s) (s) (s) (s) (s) r2 a) b) c) l3 t4 (4) (2) (3) (s) (2) (2) l6 t7 l8 l9 PART E Answer anyfourfull questions, each corriesl| marks.
**[May 2024]** (3) I I  How does white box testing differ from other types of software testing?
**[December 2019]** c) Explain basis path testing with example a) Define Cohesion.
**[May 2023]** (5) b) What do you understand by the term system testing?
**[January 2024]** I a) ' Explain System testing and its variants.
**[July 2021]** b) Define any four types of System testing.
**[May 2019]** a) Explain the following CASE tools: (i) SCM tools (ii) Documentation tools (iii) Integration & Testing tools.
**[January 2024]** l0  Explain with an example how equivalence class partitioning helps in testing.
**[May 2023]** What are the different kinds (4) ofsystem testing that are usually performed on large software products?
**[May 2019]** What are the  (3) testing that are usually performed on large (3) (3) Page 2 of 3 D F1077 b) Consider a project with the following functional units: Number of user inputs:50 Number of user outputs:40 Number of user enquiries=35 Number of user files:6 Number of extemal interfaces:4 Assume all complexity adjustment factors and weighting factors are average.
**[May 2024]** As you move outward along the process flow path of the spiral model, what can you say about the software that is being developed or maintained?

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] What is Cyclomatic Complexity? How is it calculated? (5 Marks)**
**Solution:**
Cyclomatic Complexity is a software metric based on graph theory, introduced by Thomas McCabe. It provides a quantitative measure of the logical complexity of a program. In the context of Basis Path Testing, the cyclomatic complexity value (V(G)) dictates the exact number of independent paths that exist in the code, which equals the minimum number of test cases required to execute every statement at least once.

It is calculated by first converting the code into a Flow Graph (where nodes represent code blocks and edges represent control flow), and then using one of three formulas:
1. **V(G) = E - N + 2**, where E is the number of flow graph edges and N is the number of nodes.
2. **V(G) = P + 1**, where P is the number of predicate nodes (nodes that contain a condition/branch).
3. **V(G) = Number of regions** in the flow graph (including the exterior region).
