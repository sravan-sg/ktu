# Syntax directed translation: Syntax directed definitions

## 1. Explanation
Syntax-Directed Translation (SDT) is a method of translating a source language construct by associating semantic actions with the production rules of a Context-Free Grammar (CFG). It leverages the structure of the parse tree to drive the execution of these semantic actions.

A **Syntax-Directed Definition (SDD)** is a context-free grammar together with attributes and rules. Attributes are associated with grammar symbols, and rules are associated with productions. 
- **Synthesized Attributes:** The value of a synthesized attribute at a node is computed from the values of attributes at its children. SDDs that only use synthesized attributes are called **S-attributed definitions**.
- **Inherited Attributes:** The value of an inherited attribute at a node is computed from the values of attributes at its parent and/or its siblings. SDDs that allow both but restrict inherited attributes to only depend on left siblings and parents are called **L-attributed definitions**.

## 2. Example
Consider a simple production for an assignment statement:
`S -> id = E`
Semantic Rule: `if (id.type == E.type) then S.type = "void" else error("type mismatch")`
Here, `type` is an attribute. The rule evaluates the types of `id` and `E` to ensure they match before assigning a valid type to `S`.

## 3. Applications & Use Cases
- **Type Checking:** Ensuring that operands of operators have compatible types.
- **Intermediate Code Generation:** Building abstract syntax trees (ASTs), three-address code, or quadruples as the parser recognizes language constructs.
- **Desk Calculators:** Evaluating arithmetic expressions directly during parsing without building an explicit AST.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: S-Attributed Definition for a Desk Calculator**
Given the grammar for arithmetic expressions, we can evaluate expressions:
`L -> E n`        { print(E.val) }
`E -> E1 + T`     { E.val = E1.val + T.val }
`E -> T`          { E.val = T.val }
`T -> T1 * F`     { T.val = T1.val * F.val }
`T -> F`          { T.val = F.val }
`F -> ( E )`      { F.val = E.val }
`F -> digit`      { F.val = digit.lexval }
*Trace:* For `3 + 4 * 5 n`, the parser reduces `4 * 5` to `T` with `val = 20`, then adds `3` (`E.val = 23`), and prints `23` on reducing to `L`.

**Example 2: Abstract Syntax Tree Construction**
We can use SDDs to build an AST instead of evaluating:
`E -> E1 + T`     { E.node = new Node('+', E1.node, T.node) }
`E -> T`          { E.node = T.node }
*Trace:* This dynamically allocates a tree node with the operator `+` as the root and the ASTs of `E1` and `T` as its children.

**Example 3: Handling Inherited Attributes (L-Attributed)**
Consider variable declarations: `D -> T L`, `T -> int`, `T -> float`, `L -> L1 , id`, `L -> id`.
We must pass the type from `T` down to `L`.
`D -> T L`        { L.inh = T.type }
`T -> int`        { T.type = integer }
`L -> L1 , id`    { L1.inh = L.inh; addType(id.entry, L.inh) }
`L -> id`         { addType(id.entry, L.inh) }

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (3)  11   What are L-attributed definitions and S-attributed definitions in a syntax directed  translation scheme?
**[May 2019]** (4)    b)  Explain bottom- up evaluation of s-attributed definitions.
**[May 2019]** (3)  14 a) Explain the syntax directed definition of a simple desk calculator.

*(Note: Solutions to be generated/verified by agent)*


### [May 2019] What are L-attributed definitions and S-attributed definitions in a syntax directed translation scheme? (3 marks)
**Solution:**
1. **S-attributed definitions:** A syntax-directed definition that uses only synthesized attributes is called an S-attributed definition. The value of an attribute at a parse tree node is determined entirely by the attributes of its children. They can be evaluated during a simple bottom-up parsing process.
2. **L-attributed definitions:** A syntax-directed definition where inherited attributes depend only on the attributes of parents and left siblings (never on right siblings). This allows the attributes to be evaluated in a single depth-first, left-to-right traversal of the parse tree.

### [May 2019] Explain the syntax directed definition of a simple desk calculator. (5 marks)
**Solution:**
A simple desk calculator evaluates arithmetic expressions on the fly as it parses them. We can specify its behavior using an S-attributed definition, meaning all attributes are synthesized and evaluated bottom-up.
**Grammar and Semantic Rules:**
1. `L -> E n` : `print(E.val)`
2. `E -> E1 + T` : `E.val = E1.val + T.val`
3. `E -> T` : `E.val = T.val`
4. `T -> T1 * F` : `T.val = T1.val * F.val`
5. `T -> F` : `T.val = F.val`
6. `F -> ( E )` : `F.val = E.val`
7. `F -> digit` : `F.val = digit.lexval`
**Explanation:** 
Every non-terminal (`E`, `T`, `F`) has a synthesized attribute called `val`. When the parser performs a reduction (e.g., reducing `T1 * F` to `T`), it executes the semantic rule associated with that production (multiplying the values). Because all attributes are synthesized, they can be safely computed at the moment of reduction in an LR parser. When the final expression is reduced to `L` (followed by a newline `n`), the result is printed.
