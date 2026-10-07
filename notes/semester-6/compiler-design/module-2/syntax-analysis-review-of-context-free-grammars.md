# Syntax analysis: Review of Context-Free Grammars

## 1. Explanation
Syntax analysis (parsing) is the second phase of a compiler, responsible for verifying that the stream of tokens provided by the lexical analyzer conforms to the grammatical rules of the source language. To define these rules formally, we use **Context-Free Grammars (CFGs)**.

A CFG is a mathematical system for describing languages, defined by a 4-tuple `(V, T, P, S)`:
- **V (Variables/Non-terminals):** Syntactic variables that denote sets of strings (e.g., `stmt`, `expr`).
- **T (Terminals):** The basic symbols from which strings are formed. These correspond to tokens (e.g., `id`, `+`, `while`).
- **P (Productions):** Rules specifying how non-terminals can be replaced by terminals and non-terminals. The general form is `A -> α`, where `A` is a non-terminal and `α` is a sequence of terminals and/or non-terminals.
- **S (Start Symbol):** A special non-terminal that represents the entire program or language.

**Derivations:** The process of generating a string from the start symbol by repeatedly replacing non-terminals using productions.
- **Leftmost Derivation:** At each step, the leftmost non-terminal is replaced.
- **Rightmost Derivation:** At each step, the rightmost non-terminal is replaced.

**Parse Tree:** A graphical representation of a derivation. The root is the start symbol, interior nodes are non-terminals, and leaves are terminals.

**Ambiguity:** A grammar is ambiguous if it can produce more than one valid parse tree (or leftmost/rightmost derivation) for the same string. Ambiguous grammars are problematic for compilers because they imply multiple valid syntactic interpretations of the same code.

## 2. Example
Consider a grammar for simple expressions:
`E -> E + E | E * E | ( E ) | id`

Let's derive the string `id + id * id` using a leftmost derivation:
1. `E => E + E`
2. `E => id + E`
3. `E => id + E * E`
4. `E => id + id * E`
5. `E => id + id * id`

This sequence of replacements builds a parse tree from the top down.

## 3. Applications & Use Cases
- **Language Specification:** CFGs provide a precise, unambiguous standard for how a programming language must be structured.
- **Parser Generators:** Tools like YACC, Bison, and ANTLR take a CFG as input and automatically generate C/C++/Java code for the parser.
- **Syntax Highlighting & IDEs:** IDEs use lightweight parsing based on CFGs to provide real-time syntax checking and code folding.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Leftmost and Rightmost Derivations**
Grammar: `S -> aABe`, `A -> Abc | b`, `B -> d`
String: `abbcde`
**Leftmost:** `S => aABe => aAbcBe => abbcBe => abbcde`
**Rightmost:** `S => aABe => aAde => aAbcde => abbcde`

**Example 2: Constructing a Parse Tree**
Grammar: `S -> ( L ) | a`, `L -> L , S | S`
String: `( a , a )`
Parse Tree Structure:
```text
      S
   /  |  \
  (   L   )
    / | \
   L  ,  S
   |     |
   S     a
   |
   a
```

**Example 3: Removing Ambiguity (Operator Precedence)**
The grammar `E -> E + E | E * E | id` is ambiguous for `id + id * id`.
We fix it by introducing precedence levels (Factors and Terms):
`E -> E + T | T` (Lower precedence)
`T -> T * F | F` (Higher precedence)
`F -> id` (Atomic)
This forces `*` to be evaluated deeper in the tree, resolving the ambiguity.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (3)  11   What are L-attributed definitions and S-attributed definitions in a syntax directed  translation scheme?
**[May 2019]** (3)  14 a) Explain the syntax directed definition of a simple desk calculator.
**[May 2019]** (3)  2    Construct a regular expression to denote a language L over ∑= {0,1} accepting  all strings of 0’s and 1’s that do not contain substring 011  (3)  3    Consider the context free grammar S->aSbS | bSaS | €  Check whether the grammar is ambiguous or not  (3)  4    What is Recursive Descent parsing?

*(Note: Solutions to be generated/verified by agent)*


### [May 2019] Consider the context free grammar S->aSbS | bSaS | €. Check whether the grammar is ambiguous or not. (3 marks)
**Solution:**
A grammar is ambiguous if we can find at least one string in the language that has more than one distinct leftmost derivation (or parse tree).
Let's consider the string `abab`.
Since `€` represents epsilon (empty string), we can derive `abab` in multiple ways.

**Derivation 1 (Leftmost):**
1. `S => aSbS`
2. `S => a(bSaS)bS` (using `S -> bSaS` on the first `S`)
3. `S => a(b(€)aS)bS` (using `S -> €`)
4. `S => abaaS` (simplifying epsilon)
Wait, let's derive exactly `abab`.
String: `abab`
Derivation 1:
`S => aSbS`
`S => a(bSaS)bS` (Replace first `S`)
`S => ab(€)aSbS` (Replace next `S` with `€`)
`S => aba(€)bS` (Replace next `S` with `€`)
`S => abab(€)` (Replace final `S` with `€`)
Yields: `abab`

Derivation 2:
`S => aSbS`
`S => a(€)bS` (Replace first `S` with `€`)
`S => abS`
`S => ab(aSbS)` (Replace `S` with `aSbS`)
`S => aba(€)bS` (Replace `S` with `€`)
`S => abab(€)` (Replace `S` with `€`)
Yields: `abab`

Since we have found two completely different leftmost derivations for the same string `abab`, **the grammar is ambiguous**.
