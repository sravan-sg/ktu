# CS304 — COMPILER DESIGN

> Credits: 3 | L-T-P: 3-0-0-3 | Prerequisite: Nil

## Grading Criteria

| Exam | Modules Covered | Marks | Structure |
| :--- | :--- | :--- | :--- |
| First Internal | Modules I, II | - | - |
| Second Internal | Modules III, IV | - | - |
| End Semester Exam | All Modules | 100 | 5 Parts (A, B, C, D, E) |

**Question Paper Pattern:**
- **Part A (12 Marks):** 4 questions × 3 marks (Modules I & II). All mandatory.
- **Part B (18 Marks):** 3 questions × 9 marks (Modules I & II). Answer any 2. Max 3 subparts per question.
- **Part C (12 Marks):** 4 questions × 3 marks (Modules III & IV). All mandatory.
- **Part D (18 Marks):** 3 questions × 9 marks (Modules III & IV). Answer any 2. Max 3 subparts per question.
- **Part E (40 Marks):** 6 questions × 10 marks (Modules V & VI). Answer any 4. Max 3 subparts per question.
*Note: At least 60% analytical/numerical questions.*

## Textbooks

**Prescribed:**
1. Aho A., Ravi Sethi, and D. Ullman, "Compilers - Principles, Techniques, and Tools", Addison-Wesley, 2006.
2. D. M. Dhamdhere, "Systems Programming and Operating Systems", Tata McGraw-Hill, 1996.

**References:**
1. Kenneth C. Louden, "Compiler Construction - Principles and Practice", Cengage Learning Indian Edition, 2006.
2. Tremblay and Sorenson, "The Theory and Practice of Compiler Writing", Tata McGraw-Hill, 1984.

## Modules

### Module I — Introduction to compilers and Lexical Analysis
- Introduction to compilers: Analysis of the source program
- Phases of a compiler
- Grouping of phases
- Compiler writing tools - bootstrapping
- Lexical Analysis: The role of Lexical Analyzer
- Input Buffering
- Specification of Tokens using Regular Expressions
- Review of Finite Automata
- Recognition of Tokens

### Module II — Syntax Analysis and Top-Down Parsing
- Syntax Analysis: Review of Context-Free Grammars
- Derivation trees and Parse Trees
- Ambiguity
- Top-Down Parsing: Recursive Descent parsing
- Predictive parsing
- LL(1) Grammars

### Module III — Bottom-Up Parsing and LR parsing
- Bottom-Up Parsing: Shift Reduce parsing
- Operator precedence parsing (Concepts only)
- LR parsing: Constructing SLR parsing tables
- Constructing Canonical LR parsing tables
- Constructing LALR parsing tables

### Module IV — Syntax directed translation and Type Checking
- Syntax directed translation: Syntax directed definitions
- Bottom-up evaluation of S-attributed definitions
- L-attributed definitions
- Top-down translation
- Bottom-up evaluation of inherited attributes
- Type Checking: Type systems
- Specification of a simple type checker

### Module V — Run-Time Environments and Intermediate Code Generation
- Run-Time Environments: Source Language issues
- Storage organization
- Storage-allocation strategies
- Intermediate Code Generation (ICG): Intermediate languages
- Graphical representations
- Three-Address code
- Quadruples, Triples
- Assignment statements
- Boolean expressions

### Module VI — Code Optimization and Code Generation
- Code Optimization: Principal sources of optimization
- Optimization of Basic blocks
- Code Generation: Issues in the design of a code generator
- The target machine
- A simple code generator

## Exam Focus — What to Prioritize

- **High-Yield parsing techniques**: Constructing SLR, Canonical LR, and LALR parsing tables (Module III) are practically guaranteed numerical/analytical questions. Master them as they carry significant weight.
- **Top-Down parsing**: Practice converting grammar to LL(1) and computing FIRST and FOLLOW sets, which are essential for Predictive parsing (Module II).
- **Intermediate Code Generation (ICG)**: Module V is heavily weighted (20%). Focus strongly on generating Three-Address code, Quadruples, and Triples for expressions and assignments.
- **Code Optimization & Code Generation (Module VI)**: This module also carries 20%. Understanding the optimization of Basic blocks and the design of a simple code generator will yield high marks in Part E (where 4x10=40 marks are clustered).
- **Phases of compilation & Lexical analysis**: In Part A & B, expect direct questions on the phases, regular expressions to finite automata (DFA/NFA) construction, and syntax-directed definitions.
- **Analytical Priority**: The syllabus explicitly states that at least 60% of the questions will be analytical/numerical. Prioritize solving problems over memorizing theory, especially parsing tables, automata, and ICG formats.
