# Sample Question Paper 1
**Course Code:** CS304
**Course Name:** COMPILER DESIGN
**Max. Marks:** 100
**Duration:** 3 Hours

---

## PART A
**Answer all questions. Each question carries 3 marks.**
1. Explain the different phases of a compiler with a neat diagram. (3 marks)
2. What is the role of an input buffering scheme in lexical analysis? (3 marks)
3. Write a regular expression for identifying floating-point numbers. (3 marks)
4. Differentiate between parse trees and derivation trees. (3 marks)

---

## PART B
**Answer any two full questions. Each question carries 9 marks.**
5. (a) Explain compiler writing tools and bootstrapping in detail. (5 marks)
   (b) Construct a DFA for the regular expression `(a|b)*abb`. (4 marks)

6. (a) Consider the grammar `E -> E + E | E * E | (E) | id`. Show that this grammar is ambiguous for the string `id * id + id`. (5 marks)
   (b) What are the problems with Top-Down parsing? Explain recursive descent parsing. (4 marks)

7. (a) Compute FIRST and FOLLOW for the following grammar:
   `S -> ACB | Cbb | Ba`
   `A -> da | BC`
   `B -> g | ε`
   `C -> h | ε` (6 marks)
   (b) Explain the role of a Lexical Analyzer. (3 marks)

---

## PART C
**Answer all questions. Each question carries 3 marks.**
8. What are the advantages of LR parsing over LL parsing? (3 marks)
9. Define S-attributed and L-attributed definitions. (3 marks)
10. Explain operator precedence parsing briefly. (3 marks)
11. What is the purpose of type checking? (3 marks)

---

## PART D
**Answer any two full questions. Each question carries 9 marks.**
12. (a) Construct the SLR parsing table for the grammar:
    `S -> E`
    `E -> E + T | T`
    `T -> T * F | F`
    `F -> (E) | id` (6 marks)
    (b) Briefly explain bottom-up evaluation of inherited attributes. (3 marks)

13. (a) Design a syntax-directed translation scheme to evaluate arithmetic expressions. (5 marks)
    (b) Construct the Canonical LR parsing table for the grammar `S -> CC`, `C -> cC | d`. (4 marks)

14. (a) Explain shift-reduce parsing with an example. What are the conflicts that can occur? (5 marks)
    (b) Write the specification of a simple type checker. (4 marks)

---

## PART E
**Answer any four full questions. Each question carries 10 marks.**
15. (a) Discuss the various issues in the design of a code generator. (6 marks)
    (b) What is an activation record? Explain its components. (4 marks)

16. Translate the following expression `a = b * -c + b * -c` into:
    (a) Syntax tree (3 marks)
    (b) Three-address code (3 marks)
    (c) Quadruples (4 marks)

17. Explain the principal sources of code optimization with examples for each. (10 marks)

18. (a) Discuss the different storage allocation strategies. (6 marks)
    (b) Write short notes on optimization of basic blocks. (4 marks)

19. Explain a simple code generator algorithm. How are registers allocated? (10 marks)

20. (a) Represent the Boolean expression `A < B OR (C < D AND E < F)` in three-address code. (5 marks)
    (b) Explain intermediate languages and graphical representations. (5 marks)
