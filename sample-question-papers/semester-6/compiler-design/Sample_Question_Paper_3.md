# Sample Question Paper 3
**Course Code:** CS304
**Course Name:** COMPILER DESIGN
**Max. Marks:** 100
**Duration:** 3 Hours

---

## PART A
**Answer all questions. Each question carries 3 marks.**
1. Differentiate between a compiler and an interpreter. (3 marks)
2. What are the functions of a lexical analyzer? (3 marks)
3. Explain left recursion. How can it be eliminated? (3 marks)
4. What is left factoring? Give an example. (3 marks)

---

## PART B
**Answer any two full questions. Each question carries 9 marks.**
5. (a) Explain the analysis and synthesis model of a compiler. (5 marks)
   (b) Discuss compiler writing tools. (4 marks)

6. (a) Explain how tokens are specified using regular expressions. (5 marks)
   (b) Describe the role of finite automata in recognizing tokens. (4 marks)

7. (a) Construct a predictive parsing table for the grammar:
   `E -> TE'`
   `E' -> +TE' | ε`
   `T -> FT'`
   `T' -> *FT' | ε`
   `F -> (E) | id` (6 marks)
   (b) Briefly explain derivation trees. (3 marks)

---

## PART C
**Answer all questions. Each question carries 3 marks.**
8. Define handle pruning. (3 marks)
9. What are L-attributed definitions? (3 marks)
10. Differentiate between synthesized and inherited attributes. (3 marks)
11. What is type coercion? (3 marks)

---

## PART D
**Answer any two full questions. Each question carries 9 marks.**
12. (a) Construct the Canonical LR(1) items for the grammar:
    `S -> L = R | R`
    `L -> *R | id`
    `R -> L` (6 marks)
    (b) Explain the concept of operator precedence parsing. (3 marks)

13. (a) Explain the bottom-up evaluation of inherited attributes with an example. (5 marks)
    (b) Explain the type systems in a simple type checker. (4 marks)

14. (a) Distinguish between SLR, Canonical LR, and LALR parsers. (5 marks)
    (b) Discuss syntax-directed definitions. (4 marks)

---

## PART E
**Answer any four full questions. Each question carries 10 marks.**
15. (a) Discuss storage organization in run-time environments. (5 marks)
    (b) What are the different intermediate languages? Explain. (5 marks)

16. Write down the simple code generator algorithm and explain it with an example. (10 marks)

17. Explain peephole optimization techniques. (10 marks)

18. (a) Explain the translation of assignment statements into intermediate code. (6 marks)
    (b) What are basic blocks? How are they identified? (4 marks)

19. Explain in detail the principal sources of optimization. (10 marks)

20. Translate the following `while` statement into three-address code:
    `while (a < b and c < d) do x = y + z;` (10 marks)
