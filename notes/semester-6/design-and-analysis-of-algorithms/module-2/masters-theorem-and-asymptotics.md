# Module 2 — Topic 1: Master's Theorem, Asymptotic Notations & Functions

> **Module 2**: Master's Theorem, Asymptotics & Balanced Structures  
> **Course**: CS302 Design and Analysis of Algorithms

---

## 1. Master's Theorem for Divide-and-Conquer

Master's Theorem provides a direct cookbook formula for solving recurrences of the form:
$$T(n) = a T(n/b) + f(n)$$
where $a \ge 1$, $b > 1$, and $f(n)$ is an asymptotically positive function.

### The 3 Master Cases:

Compare $f(n)$ with $n^{\log_b a}$:

1. **Case 1 (Subproblem Heavy)**:  
   If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$:  
   $$T(n) = \Theta(n^{\log_b a})$$

2. **Case 2 (Balanced Work)**:  
   If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$:  
   $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$

3. **Case 3 (Combine Heavy)**:  
   If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, AND regularity condition holds ($a f(n/b) \le c f(n)$ for $c < 1$):  
   $$T(n) = \Theta(f(n))$$

---

## 2. Asymptotic Notations & Core Properties

### Asymptotic Definitions:
- **Big-O ($O$)**: Asymptotic Upper Bound. $T(n) \le c \cdot g(n)$ for all $n \ge n_0$.
- **Big-Omega ($\Omega$)**: Asymptotic Lower Bound. $T(n) \ge c \cdot g(n)$ for all $n \ge n_0$.
- **Big-Theta ($\Theta$)**: Asymptotic Tight Bound. $c_1 g(n) \le T(n) \le c_2 g(n)$ for all $n \ge n_0$.

### Common Complexity Functions Growth Ranking:
$$O(1) < O(\log n) < O(\sqrt{n}) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$
