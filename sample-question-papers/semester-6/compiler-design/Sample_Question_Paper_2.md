# CS304 - COMPILER DESIGN
## Sample Question Paper 2
**Max. Marks: 100 | Duration: 3 Hours**

### PART A
**Answer all questions, each carries 3 marks.**
1. How does a lexical analyzer handle input buffering using the two-buffer scheme? (3)
2. What are the advantages of grouping compiler phases into front-end and back-end? (3)
3. Give an example of left factoring in a grammar. (3)
4. What is LL(1) grammar? Give the conditions for a grammar to be LL(1). (3)

### PART B
**Answer any two full questions, each carries 9 marks.**
5. a) Explain the working of a lexical analyzer using transition diagrams. (4)
   b) Write down the regular expressions for the following: identifiers, integer constants, and floating-point constants. (5)
6. a) Construct a predictive parsing table for the grammar: `S -> ( L ) | a`, `L -> L , S | S`. (9)
7. a) Design a recursive descent parser for the grammar: `S -> c A d`, `A -> a b | a`. (5)
   b) Draw the derivation tree and parse tree for the expression `id + id * id`. (4)

### PART C
**Answer all questions, each carries 3 marks.**
8. What is a handle in bottom-up parsing? Explain with an example. (3)
9. Define the properties of an L-attributed definition. (3)
10. Differentiate between SLR, LALR, and Canonical LR parsing techniques in terms of power and states. (3)
11. What is a type system? Why is it necessary? (3)

### PART D
**Answer any two full questions, each carries 9 marks.**
12. a) Construct the Canonical LR(1) items for the grammar: `S -> L = R | R`, `L -> * R | id`, `R -> L`. (9)
13. a) Explain the bottom-up evaluation of inherited attributes. (5)
    b) Design a simple type checker for array references. (4)
14. a) Construct an LALR parsing table for the grammar: `S -> A A`, `A -> a A | b`. (9)

### PART E
**Answer any four full questions, each carries 10 marks.**
15. Explain how a target machine's architecture affects the code generator. Discuss instruction selection and register allocation. (10)
16. Generate intermediate code (Three-address code) for the following code snippet:
    `while (a < b) { if (c > d) x = y + z; else x = y - z; }` (10)
17. a) Discuss peephole optimization techniques with examples. (5)
    b) Explain loop optimization techniques (code motion, induction variables). (5)
18. a) Describe how storage organization works for recursive procedure calls. (5)
    b) Differentiate between static and dynamic storage allocation. (5)
19. Explain how intermediate code generation is performed for assignment statements involving mixed types (type conversion). (10)
20. a) Explain quadruples and triples with an example representing `x = (a + b) * (c + d)`. (5)
    b) How is a DAG used for common subexpression elimination in a basic block? (5)
