# Phases of a compiler

## 1. Explanation
A compiler operates in phases, each transforming the source program from one representation to another. The typical phases include:
1. **Lexical Analysis (Scanner):** Converts a stream of characters into a stream of tokens.
2. **Syntax Analysis (Parser):** Uses the tokens to build a syntax tree representing the grammatical structure.
3. **Semantic Analysis:** Checks for semantic consistency (e.g., type checking).
4. **Intermediate Code Generation:** Produces a machine-independent intermediate representation.
5. **Code Optimization:** Improves the intermediate code.
6. **Code Generation:** Maps the optimized intermediate code to the target machine code.

Symbol Table Management and Error Handling interact with all phases.

## 2. Example
Consider the statement `position = initial + rate * 60`
1. Lexical: `id1 = id2 + id3 * 60`
2. Syntax: Syntax Tree showing `*` having higher precedence than `+`.

## 3. Applications & Use Cases
Every modern IDE uses these phases in real-time to provide syntax highlighting (Lexical), code completion (Syntax/Semantic), and just-in-time compilation (Optimization/Code Gen).

## 4. 3 Solved Numerical/Analytical Examples
**Example 1:** Identify the tokens in `x = y + 2;`
- `x` (id)
- `=` (assign_op)
- `y` (id)
- `+` (add_op)
- `2` (num)
- `;` (semi)

## 5. Previous Year Questions & Solutions
[April 2018]
**Question:** Explain the different phases of a compiler with a neat diagram.
**Solution:**
A compiler operates in several phases:
1. Lexical Analysis
2. Syntax Analysis
3. Semantic Analysis
4. Intermediate Code Generation
5. Code Optimization
6. Code Generation
(Diagram: Source Program -> Lexical -> Syntax -> Semantic -> ICG -> Opt -> Code Gen -> Target Program, with Symbol Table & Error Handler on the side.)
