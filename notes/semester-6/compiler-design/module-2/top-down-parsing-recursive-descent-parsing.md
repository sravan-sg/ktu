# Top-Down Parsing: Recursive Descent parsing

## 1. Explanation
Top-down parsing attempts to construct a parse tree for the input string starting from the root (start symbol) and creating the nodes in pre-order. Recursive Descent parsing uses a set of recursive procedures, one for each non-terminal in the grammar. If it requires backtracking, it can be slow; but if the grammar is LL(1), predictive parsing can be used.

## 2. Example
Grammar:
`S -> cAd`
`A -> ab | a`
A procedure `S()` will check for 'c', call `A()`, and then check for 'd'.

## 3. Applications & Use Cases
Recursive descent parsers are very common in production compilers (like GCC and Clang) because they are easy to write, read, and maintain by hand, offering excellent custom error reporting.

## 4. 3 Solved Numerical/Analytical Examples
**Example 1:** Why is left recursion a problem for Recursive Descent?
**Solution:** If `A -> A lpha`, the procedure `A()` will immediately call `A()` again, leading to an infinite loop.

## 5. Previous Year Questions & Solutions
[Sample Question Paper]
**Question:** What are the problems with Top-Down parsing? Explain recursive descent parsing.
**Solution:** 
Problems: Left recursion causes infinite loops, and common prefixes require backtracking.
Recursive Descent Parsing: A top-down parsing technique constructed from a set of mutually recursive procedures where each procedure implements one of the nonterminals of the grammar.
