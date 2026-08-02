# Module 6 — Topic 2: Complexity Theory (P, NP, NP-Hard & NP-Complete)

> **Module 6**: Branch and Bound & Complexity Theory  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Tractable vs Intractable Problems
- **Tractable**: Problems solvable in polynomial time $O(n^k)$.
- **Intractable**: Problems requiring super-polynomial / exponential time $\Omega(2^n)$ to solve.

---

## 2. Complexity Classes
1. **P Class**: Decision problems solvable in polynomial time by a Deterministic Turing Machine.
2. **NP Class**: Decision problems verifiable in polynomial time by a Deterministic Turing Machine (or solvable by a Non-Deterministic Turing Machine).
3. **Polynomial-Time Reduction ($L_1 \le_P L_2$)**: Problem $L_1$ reduces to $L_2$ in polynomial time if an algorithm for $L_2$ can solve $L_1$.
4. **NP-Hard**: Problems at least as hard as any problem in NP (every problem in NP reduces to it in polynomial time).
5. **NP-Complete**: Problems that are BOTH in **NP** and **NP-Hard** (e.g. 3-SAT, Clique, Hamiltonian Cycle, Traveling Salesman Decision Problem).
