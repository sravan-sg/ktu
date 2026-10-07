# Derivation Trees and Parse Trees

## 1. Explanation
A **Derivation** is a sequence of rule applications (productions) from a Context-Free Grammar that generates a specific string of terminals starting from the start symbol. At each step, a non-terminal is replaced by the right-hand side of one of its productions. There are two systematic ways to perform a derivation:
1.  **Leftmost Derivation (LMD):** At each step, the leftmost non-terminal in the sentential form is replaced. This is the derivation strategy implicitly used by Top-Down parsers.
2.  **Rightmost Derivation (RMD):** At each step, the rightmost non-terminal in the sentential form is replaced. This is the derivation strategy used by Bottom-Up (Shift-Reduce) parsers. (Sometimes called a canonical derivation).

A **Parse Tree** (or Derivation Tree) is the graphical, hierarchical representation of a derivation. It abstracts away the *order* of rule applications (whether it was leftmost or rightmost) and purely shows the structural relationship of how non-terminals expand into terminals. 
*   **Root:** The start symbol of the grammar.
*   **Internal Nodes:** Non-terminals.
*   **Leaves (Yield):** Terminals (or $\epsilon$). Reading the leaves from left to right yields the parsed string.

If a grammar generates the exact same parse tree for a string regardless of whether an LMD or RMD was used, the derivation is structurally unique. If multiple distinct parse trees exist for the same string, the grammar is ambiguous.

## 2. Example
Consider the grammar: $E \rightarrow E + E \mid \text{id}$

**String:** `id + id`
**Leftmost Derivation:**
1.  $E \Rightarrow E + E$ (Applying $E \rightarrow E + E$)
2.  $E \Rightarrow \text{id} + E$ (Replacing leftmost $E$ with $\text{id}$)
3.  $E \Rightarrow \text{id} + \text{id}$ (Replacing remaining $E$ with $\text{id}$)

**Parse Tree:**
```text
      E
    / | \
   E  +  E
   |     |
  id    id
```
Notice how the parse tree visually captures the `+` operation joining two `id` leaves, abstracting away the fact that we expanded the left `E` before the right `E`.

## 3. Applications & Use Cases
*   **Compiler Debugging & Visualization:** Developers use tools that generate parse trees visually to debug why a specific line of code is failing to parse or is parsing incorrectly due to precedence issues.
*   **Abstract Syntax Tree (AST) Generation:** The Parse Tree contains a lot of redundant syntactic details (like parentheses or intermediate single-production nodes). Compilers traverse the concrete Parse Tree to generate a much leaner Abstract Syntax Tree (AST), which is then passed to the semantic analyzer.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Tracing a Rightmost Derivation**
*Problem:* Given $S \rightarrow A B$, $A \rightarrow a \mid \epsilon$, $B \rightarrow b \mid c$. Write the Rightmost Derivation for the string `ac`.
*Solution:*
1.  $S \Rightarrow A B$
2.  $S \Rightarrow A c$ (Replace rightmost non-terminal $B$ with $c$)
3.  $S \Rightarrow a c$ (Replace remaining non-terminal $A$ with $a$)

**Example 2: Yield of a Parse Tree**
*Problem:* In a parse tree where the root is $S$, its children are $A, +, B$. $A$'s child is $x$, and $B$'s child is $y$. What is the yield?
*Solution:* The yield is formed by reading the leaves from left to right. The leaves are $x$, $+$, and $y$. Thus, the yield is the string `x+y`.

**Example 3: Verifying structural equivalence**
*Problem:* Does a leftmost derivation and a rightmost derivation of the string `id+id` using $E \rightarrow E+E \mid id$ produce the same parse tree?
*Solution:* Yes. In LMD, the left $E$ becomes `id` first. In RMD, the right $E$ becomes `id` first. However, graphically, the root $E$ splits into $E, +, E$, and both child $E$ nodes terminate at `id`. The resulting graphical tree is identical.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (3)  10    What are annotated parse trees?
**[May 2019]** 8     Explain the main actions in a shift reduce parser  (3)  9     What are different parsing conflicts in SLR parsing table?

*(Note: Solutions to be generated/verified by agent)*


### [July 2021]
**Question:** Explain Leftmost and Rightmost derivations with an example.
**Solution:**
A **derivation** is a sequence of production rule applications replacing non-terminals to generate a string of terminals.
**1. Leftmost Derivation (LMD):** In this derivation, the leftmost non-terminal in the current sentential form is always chosen to be expanded first. Top-down parsers construct Leftmost derivations.
**2. Rightmost Derivation (RMD):** In this derivation, the rightmost non-terminal in the current sentential form is always chosen to be expanded first. Bottom-up parsers construct Rightmost derivations in reverse.

**Example:**
Consider the grammar: $S \rightarrow S * S \mid S + S \mid a$
String to derive: $a * a + a$

*Leftmost Derivation:*
$S \Rightarrow S * S$ (Replace leftmost S)
$\Rightarrow a * S$ (Replace leftmost S)
$\Rightarrow a * S + S$ (Replace leftmost S)
$\Rightarrow a * a + S$ (Replace leftmost S)
$\Rightarrow a * a + a$

*Rightmost Derivation:*
$S \Rightarrow S * S$ (Replace rightmost S)
$\Rightarrow S * S + S$ (Replace rightmost S)
$\Rightarrow S * S + a$ (Replace rightmost S)
$\Rightarrow S * a + a$ (Replace rightmost S)
$\Rightarrow a * a + a$

### [September 2020]
**Question:** Define Parse Tree. What is the relationship between a derivation and a parse tree?
**Solution:**
A **Parse Tree** (or Derivation tree) is a graphical representation of a derivation that shows the hierarchical syntactic structure of a string according to a Context-Free Grammar.
*   The root node is labeled with the start symbol.
*   Each internal node is a non-terminal.
*   Each leaf node is a terminal symbol or $\epsilon$.
*   If a node $A$ has children $X_1, X_2, \dots, X_n$, then there must be a production rule $A \rightarrow X_1 X_2 \dots X_n$ in the grammar.

**Relationship:**
A parse tree abstracts away the order of derivation. While there can be multiple derivations for a single string (e.g., one Leftmost Derivation and one Rightmost Derivation), they will both map to the exact same unique parse tree (provided the grammar is unambiguous). The derivation is the sequential step-by-step process, while the parse tree is the final static structural proof of the derivation.
