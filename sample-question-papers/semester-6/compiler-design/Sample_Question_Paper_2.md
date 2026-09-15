# Sample Question Paper 2
**Course Code:** CS304
**Course Name:** COMPILER DESIGN
**Max. Marks:** 100
**Duration:** 3 Hours

---

## PART A
**Answer all questions. Each question carries 3 marks.**
1. What is bootstrapping? (3 marks)
2. Define a regular expression and explain its role in lexical analysis. (3 marks)
3. Explain the term "ambiguity" with respect to context-free grammars. (3 marks)
4. What is a predictive parser? (3 marks)

---

## PART B
**Answer any two full questions. Each question carries 9 marks.**
5. (a) Discuss the grouping of phases in a compiler. (5 marks)
   (b) How are tokens recognized using transition diagrams? Explain with an example. (4 marks)

6. (a) Convert the following NFA to DFA. (5 marks)
   *Assume a generic NFA to DFA conversion problem is given here.*
   (b) Write a short note on input buffering in a lexical analyzer. (4 marks)

7. (a) Is the grammar `S -> iEtS | iEtSeS | a`, `E -> b` ambiguous? Justify your answer. (6 marks)
   (b) What are LL(1) grammars? (3 marks)

---

## PART C
**Answer all questions. Each question carries 3 marks.**
8. What is a shift-reduce parser? (3 marks)
9. Define a syntax-directed definition (SDD). (3 marks)
10. What are inherited attributes? (3 marks)
11. Differentiate between static and dynamic type checking. (3 marks)

---

## PART D
**Answer any two full questions. Each question carries 9 marks.**
12. (a) Construct the LALR parsing table for the grammar:
    `S -> AA`
    `A -> aA | b` (6 marks)
    (b) Discuss the bottom-up evaluation of S-attributed definitions. (3 marks)

13. (a) Explain the top-down translation scheme. (5 marks)
    (b) Describe the type systems and type expressions with examples. (4 marks)

14. (a) What are the rules to construct the SLR parsing table? Explain. (5 marks)
    (b) Give the specification of a simple type checker. (4 marks)

---

## PART E
**Answer any four full questions. Each question carries 10 marks.**
15. (a) Explain in detail the various storage allocation strategies. (6 marks)
    (b) Write short notes on intermediate languages. (4 marks)

16. Write the three-address code, triples, and quadruples for the expression:
    `x = a * -b + a * -b` (10 marks)

17. Explain the optimization of basic blocks using DAGs (Directed Acyclic Graphs). (10 marks)

18. (a) Discuss the issues in the design of a code generator. (5 marks)
    (b) Explain the target machine architecture. (5 marks)

19. Explain the principal sources of optimization with suitable examples. (10 marks)

20. (a) Explain how Boolean expressions are translated into three-address code. (5 marks)
    (b) Discuss source language issues in run-time environments. (5 marks)
