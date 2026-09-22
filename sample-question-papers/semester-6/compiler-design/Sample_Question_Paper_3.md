# CS304 - COMPILER DESIGN
## Sample Question Paper 3
**Max. Marks: 100 | Duration: 3 Hours**

### PART A
**Answer all questions, each carries 3 marks.**
1. Briefly explain cross-compiler and bootstrapping. (3)
2. What are tokens, patterns, and lexemes? (3)
3. Construct a context-free grammar for generating all palindromes over {0, 1}. (3)
4. Why is predictive parsing preferred over recursive descent parsing with backtracking? (3)

### PART B
**Answer any two full questions, each carries 9 marks.**
5. a) Discuss how a Lex tool can be used to generate a lexical analyzer. (5)
   b) Write a regular expression for a C-like block comment `/* ... */`. (4)
6. a) For the grammar `E -> T E'`, `E' -> + T E' | €`, `T -> F T'`, `T' -> * F T' | €`, `F -> ( E ) | id`, compute FIRST and FOLLOW sets. (5)
   b) Show the top-down parsing trace for the string `id + id * id`. (4)
7. a) Explain the role of the symbol table in various phases of compilation. (5)
   b) Prove that the grammar `S -> iCtS | iCtSeS | a`, `C -> b` is ambiguous. (4)

### PART C
**Answer all questions, each carries 3 marks.**
1. Explain how a shift-reduce parser resolves a shift/reduce conflict. (3)
2. What is an annotated parse tree? Give a small example. (3)
3. What is structural equivalence and name equivalence in type checking? (3)
4. List the components of a shift-reduce parser. (3)

### PART D
**Answer any two full questions, each carries 9 marks.**
12. a) Construct the LALR parsing table for the grammar: `S -> C C`, `C -> c C | d`. (9)
13. a) Explain the syntax-directed definition for declarations and type checking. (5)
    b) Explain top-down translation schemes. (4)
14. a) Construct the SLR parsing table for the grammar: `S -> E`, `E -> E + T | T`, `T -> T * F | F`, `F -> (E) | id`. (9)

### PART E
**Answer any four full questions, each carries 10 marks.**
15. Explain heap allocation and stack allocation strategies in detail. (10)
16. Explain the generation of intermediate code for Boolean expressions and flow-of-control statements. (10)
17. a) Write down a simple code generation algorithm using a register descriptor and address descriptor. (5)
    b) Generate code for `x = a + b * c` using a simple code generator for a machine with two registers R0, R1. (5)
18. Explain the following optimization techniques with examples:
    a) Constant folding (3)
    b) Dead code elimination (3)
    c) Strength reduction (4)
19. a) Represent the expression `a + a * (b - c) + (b - c) * d` as a DAG. (5)
    b) Explain the data structures used to implement quadruples and triples. (5)
20. Detail the various issues in the design of a code generator. (10)
