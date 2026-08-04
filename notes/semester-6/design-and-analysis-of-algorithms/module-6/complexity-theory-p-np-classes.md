# Module 6 — Topic 2: Complexity Theory (P, NP, NP-Hard & NP-Complete)

> **Module 6**: Branch and Bound & Complexity Theory  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
We usually measure *algorithms* using Big-O notation, but what if the *problem itself* is fundamentally impossible to solve quickly? **Complexity Theory** categorizes computational problems based on their inherent difficulty, dividing them into classes based on how long they take to run on a Turing Machine.
- **P (Polynomial Time)**: Decision problems that a computer can *solve* quickly (in $O(n^k)$ time).
- **NP (Nondeterministic Polynomial Time)**: Decision problems where, if someone hands you a "certificate" (a guessed answer), you can *verify* if it's correct quickly in Polynomial Time.
- **NP-Hard**: The hardest problems in Computer Science. A problem is NP-Hard if *every* problem in NP can be mathematically reduced (translated) into it in polynomial time. If you find a fast algorithm for one NP-Hard problem, you magically cure all NP problems.
- **NP-Complete**: The intersection. Problems that are BOTH in NP (verifiable quickly) AND NP-Hard (everything reduces to them). Examples: 3-SAT, TSP, Clique.

### Example
Imagine an enormous, 10,000-piece jigsaw puzzle.
- Finding the exact configuration from scratch is incredibly difficult and time-consuming. 
- However, if your friend hands you the finished puzzle and says "I solved it!", you can look at the picture and *verify* they are correct in just a few seconds. 
Solving it is hard; verifying it is easy. This is the essence of an **NP** problem.

### Applications & Use Cases
- **Cryptography & Security**: The entire internet (RSA, HTTPS, Blockchain) relies on the assumption that P $\neq$ NP. Factoring large primes to crack passwords is an NP problem—it's incredibly hard for hackers to solve, but very easy for your bank server to verify when you type the correct password.
- **Logistics (TSP)**: FedEx cannot calculate the mathematically absolute perfect route for a truck visiting 50 cities because TSP is NP-Hard. They must use approximations instead of exact algorithms.
- **Compiler Register Allocation**: Assigning a limited number of CPU registers to variables is equivalent to Graph Coloring (an NP-Complete problem), forcing compilers like GCC/Clang to use greedy heuristics.

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Proving a Problem is in NP (Verification Algorithm)
**Problem:** The Hamiltonian Cycle decision problem asks: "Does there exist a simple cycle in Graph $G$ that visits every vertex exactly once?" Prove mathematically that this problem belongs to the class **NP**.
**Step-by-step Solution:**
1. **Understand NP Definition:** To prove a problem is in NP, we do NOT need to prove we can solve it quickly. We only need to prove that if we are given a proposed "Certificate" (an answer), we can *verify* it in polynomial time $O(n^k)$.
2. **Define the Certificate:** Let the certificate be an ordered sequence of vertices $C = \{v_1, v_2, \dots, v_n, v_1\}$ which claims to be the Hamiltonian Cycle.
3. **Design the Verifier Algorithm:**
   - Check 1: Ensure the length of the sequence is exactly $V + 1$. ($O(1)$ time).
   - Check 2: Ensure the first vertex and last vertex in the sequence are the same. ($O(1)$ time).
   - Check 3: Ensure there are no duplicate vertices (except start/end). Sort or hash the sequence. ($O(V \log V)$ time).
   - Check 4: For every consecutive pair $(v_i, v_{i+1})$ in the sequence, check the graph's Adjacency Matrix to ensure an actual edge exists between them. ($O(V)$ time).
4. **Conclusion:** All checks take linear or log-linear time. Because the verification algorithm definitively runs in polynomial time $O(V \log V)$, the Hamiltonian Cycle problem belongs to the class **NP**.

### Example 2: Polynomial-Time Reduction Logic
**Problem:** We know that Problem A is NP-Complete (meaning it's incredibly hard). We want to prove that a new Problem B is also NP-Complete. We write a function that takes the inputs for Problem A, modifies them slightly, and feeds them into Problem B. This translation takes $O(n^2)$ time. Does this prove Problem B is NP-Complete?
**Step-by-step Solution:**
1. **Understand Reduction ($A \le_P B$):** A reduction means "If I have a magic machine that solves B, I can use it to solve A by just translating the inputs."
2. **Direction of Reduction Matters:** 
   - We reduced the *Known Hard Problem (A)* to the *Unknown Problem (B)*. 
   - This means we said: "I can solve A by translating it into B."
3. **Analyze the Implications:** Because A is NP-Complete, it is inherently difficult. If we can solve it by just running a fast $O(n^2)$ translation and then using an algorithm for B, it implies that B *must* be at least as hard as A. If B were easy, A would be easy (which is a contradiction).
4. **Conclusion:** Yes. By successfully reducing a known NP-Complete problem into Problem B in polynomial time ($O(n^2)$), we have mathematically proven that Problem B is **NP-Hard**. (If B is also verifiable in polynomial time, it is NP-Complete).

### Example 3: Defining P, NP, NP-Hard, NP-Complete Intersections [Dec 2019]
**Problem:** Draw a logical conclusion about the relationships between complexity classes if someone suddenly discovers an algorithm that solves the Boolean Satisfiability Problem (3-SAT) in exactly $O(n^3)$ time.
**Step-by-step Solution:**
1. **Identify the Given Problem:** 3-SAT was the very first problem ever proven to be **NP-Complete** (Cook-Levin Theorem, 1971).
2. **Analyze the Discovery:** The discovery states that 3-SAT can be solved in $O(n^3)$ time. $O(n^3)$ is polynomial time. This means 3-SAT now belongs to the class **P**.
3. **Apply the NP-Hard Property:** Because 3-SAT is NP-Complete, it is also NP-Hard. By definition, *every single problem in NP* can be translated (reduced) into 3-SAT in polynomial time.
4. **Chain the Execution:** To solve *any* NP problem, you could translate it into 3-SAT (which takes polynomial time), and then solve the 3-SAT using the newly discovered algorithm (which takes polynomial time). A polynomial plus a polynomial is still a polynomial.
5. **Conclusion:** If an $O(n^3)$ algorithm is found for 3-SAT, it proves that every problem in NP can be solved in polynomial time. This would definitively prove that **P = NP**, solving a million-dollar Clay Mathematics Institute Millennium Prize problem and collapsing the complexity classes.

---

### Previous Year Questions & Solutions

1. **"Explain the classes P, NP, NP Hard and NP complete. Define NP-Hard and NP-complete problems." [Dec 2019, July 2021, Sept 2020]**
   - **Solution:**
     - **Class P (Polynomial Time):** The set of all decision problems that can be **solved** by a deterministic Turing Machine in $O(n^k)$ polynomial time (e.g. Merge Sort, Shortest Path).
     - **Class NP (Nondeterministic Polynomial Time):** The set of all decision problems whose proposed positive solution (certificate) can be **verified** by a deterministic Turing Machine in polynomial time $O(n^k)$. (Note: $P \subseteq NP$).
     - **NP-Hard:** A class of problems $X$ such that *every problem $L \in NP$ can be polynomial-time reduced to $X$* ($L \le_P X$). NP-Hard problems are at least as hard as any problem in NP, but do not need to be in NP themselves (can be optimization problems).
     - **NP-Complete:** The set of problems that are **both** in NP and NP-Hard ($X \in NP$ and $\forall L \in NP, L \le_P X$). They represent the absolute hardest problems in NP (e.g. 3-SAT, Clique, Hamiltonian Cycle, TSP Decision).

2. **"Differentiate between deterministic and non deterministic algorithms..." [April 2018, Dec 2019]**
   - **Solution:** 
     - **Deterministic Algorithm:** At any exact step during execution, there is only one uniquely defined next step. Given a specific input, it will always produce the exact same sequence of operations and the same output.
     - **Non-Deterministic Algorithm:** Has a special `choice()` function that can "guess" the correct path. At any step, it can branch into multiple possible next steps simultaneously. If *any* of those branches leads to a successful solution (a `success()` state), the algorithm instantly succeeds. If all branches fail, it returns `failure()`.

3. **"Write down the non deterministic algorithm for sorting..." [April 2018]**
   - **Solution:** A non-deterministic sorting algorithm magically guesses the correct sorted array indices in $O(n)$ time.
     ```text
     Algorithm NDSort(A, n)
       1. Initialize array B[1..n] to 0
       2. for i = 1 to n do:
       3.     j = choice(1, n)          // magically guess the correct sorted index for A[i]
       4.     if B[j] != 0 then failure() // index already taken, guess was wrong
       5.     B[j] = A[i]
       6. for i = 1 to n-1 do:
       7.     if B[i] > B[i+1] then failure() // verify the array is actually sorted
       8. success(B) // if we didn't fail, we successfully sorted it!
     ```

4. **"What do you mean by state space tree?" [Dec 2019]**
   - **Solution:** A State Space Tree is a tree structure used to represent all possible states (partial solutions) of a combinatorial problem, typically used in Backtracking and Branch & Bound algorithms. The root represents the initial state, edges represent decisions or moves, internal nodes represent partial solutions, and leaves represent final configurations (either successful solutions or dead ends).
