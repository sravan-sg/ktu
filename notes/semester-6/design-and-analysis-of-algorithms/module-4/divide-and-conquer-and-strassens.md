# Module 4 — Topic 1: Divide and Conquer & Strassen's Matrix Multiplication

> **Module 4**: Divide and Conquer & Dynamic Programming  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Divide and Conquer Control Abstraction
1. **Divide**: Break problem into smaller independent subproblems.
2. **Conquer**: Solve subproblems recursively.
3. **Combine**: Merge subproblem solutions into total solution.

---

## 2. Strassen's Matrix Multiplication
Standard matrix multiplication takes $O(n^3)$ multiplications. Strassen reduces multiplications from 8 to 7 for $2 \times 2$ matrices using 7 intermediate products ($P_1 \dots P_7$).
- Recurrence: $T(n) = 7T(n/2) + O(n^2)$.
- Time Complexity: $\Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.
