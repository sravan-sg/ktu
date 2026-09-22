# CS304 - COMPILER DESIGN
## Sample Question Paper 1
**Max. Marks: 100 | Duration: 3 Hours**

### PART A
**Answer all questions, each carries 3 marks.**
1. What is the role of the lexical analyzer in a compiler? (3)
2. Define bootstrapping with an example. (3)
3. What is an ambiguous grammar? Explain with an example. (3)
4. State the problems faced when designing a recursive descent parser. (3)

### PART B
**Answer any two full questions, each carries 9 marks.**
5. a) Explain the different phases of a compiler with a neat diagram. (5)
   b) Differentiate between compiler and interpreter. (4)
6. a) Construct a regular expression for a language over ∑= {a, b} containing strings that end with 'abb'. (4)
   b) Compute FIRST and FOLLOW sets for the following grammar: `S -> A B c`, `A -> a | €`, `B -> b | €`. (5)
7. a) What is left recursion? Eliminate left recursion from the grammar: `E -> E + T | T`, `T -> T * F | F`, `F -> ( E ) | id`. (5)
   b) Briefly explain any two compiler writing tools. (4)

### PART C
**Answer all questions, each carries 3 marks.**
8. Explain the main actions performed by a shift-reduce parser. (3)
9. Define a Syntax-Directed Definition (SDD). What are synthesized attributes? (3)
10. What are the conflicts that occur in LR parsing? (3)
11. Give an overview of how type checking works for a simple assignment statement. (3)

### PART D
**Answer any two full questions, each carries 9 marks.**
12. a) Differentiate between S-attributed and L-attributed definitions. (5)
    b) Write a syntax-directed definition for a simple desk calculator. (4)
13. a) Construct the LR(0) items for the grammar: `S -> C C`, `C -> c C | d`. (5)
    b) Explain operator precedence parsing with an example. (4)
14. a) Construct the SLR parsing table for the grammar: `E -> E + T | T`, `T -> T * F | F`, `F -> ( E ) | id`. (9)

### PART E
**Answer any four full questions, each carries 10 marks.**
15. Explain in detail the various storage allocation strategies used in run-time environments. (10)
16. Discuss the issues in the design of a code generator. (10)
17. a) What are the principal sources of code optimization? Explain. (5)
    b) Explain the optimization of basic blocks using DAGs. (5)
18. Translate the expression `a = b * -c + b * -c` into:
    a) Three-address code (4)
    b) Quadruples (3)
    c) Triples (3)
19. a) Explain the intermediate code generation for Boolean expressions. (5)
    b) What is an activation record? Explain its components. (5)
20. Write a simple code generation algorithm and explain it with a suitable example. (10)
