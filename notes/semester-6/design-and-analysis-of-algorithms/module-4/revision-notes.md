# Module 4: Last-Minute Revision & Submodule Guide

> **Semester**: S6 | **Subject**: Design and Analysis of Algorithms (CS302)  
> **Purpose**: Rapid revision guide for Module 4 covering Divide & Conquer, Strassen's Algorithm, Dynamic Programming, and Strategy Comparisons.

---

## Submodule 4.1: Divide & Conquer & Strassen's Algorithm

### 1. Explanation
Divide problem into subproblems, solve recursively, combine solutions. Strassen reduces subproblem multiplications from 8 to 7, improving runtime from $O(n^3)$ to $O(n^{2.81})$.

### 2. Real-World Example
Large-scale image processing and graphics matrix transformations.

### 3. Applications & Use Cases
High-performance linear algebra libraries (BLAS, LAPACK).

### 4. 3 Solved Micro-Examples
- **Example 1**: Merge Sort recurrence $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$.
- **Example 2**: Strassen recurrence $T(n) = 7T(n/2) + O(n^2) \implies \Theta(n^{\log_2 7}) \approx \Theta(n^{2.81})$.
- **Example 3**: Standard $n \times n$ matrix multiplication performs $n^3$ multiplications.

---

## Submodule 4.2: Dynamic Programming & Comparison

### 1. Explanation
DP uses Optimality Principle and stores overlapping subproblems in a table to prevent re-computation. D&C handles independent subproblems.

### 2. Real-World Example
Text diff algorithms (git diff) using Longest Common Subsequence (LCS).

### 3. Applications & Use Cases
DNA sequence alignment in bioinformatics, financial portfolio optimization.

### 4. 3 Solved Micro-Examples
- **Example 1**: Matrix Chain Multiplication DP table computes optimal parenthesization order in $O(n^3)$ time.
- **Example 2**: Bellman-Ford algorithm runs $V-1$ relaxation passes over $E$ edges in $O(V \cdot E)$ time.
- **Example 3**: D&C re-computes subproblems exponentially ($O(2^n)$ in naive Fibonacci), whereas DP reduces it to $O(n)$.
