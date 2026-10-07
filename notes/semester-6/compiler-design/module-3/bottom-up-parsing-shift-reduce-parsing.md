# Bottom-up parsing: Shift-reduce parsing

## 1. Explanation
Bottom-up parsing attempts to construct a parse tree for an input string beginning at the leaves (the bottom) and working up towards the root (the starting non-terminal). A widely used method of bottom-up parsing is **Shift-Reduce Parsing**.

It operates by performing two main actions on a stack and an input buffer:
- **Shift:** Move the next input token onto the top of the stack.
- **Reduce:** If the symbols on the top of the stack match the right side (body) of a production rule, replace them with the non-terminal on the left side (head) of that production.

The parser continues to shift and reduce until the stack contains only the start symbol and the input buffer is empty (Accept). If it cannot proceed and neither condition is met, a syntax error has occurred.

**Key Concepts:**
- **Handle:** A substring that matches the body of a production and whose reduction represents one step along the reverse of a rightmost derivation. Finding the handle is the core challenge of shift-reduce parsing.
- **Conflicts:** Shift-reduce parsers can suffer from two types of conflicts:
  1. **Shift/Reduce Conflict:** The parser cannot decide whether to shift the next input symbol or reduce the current stack top.
  2. **Reduce/Reduce Conflict:** The parser has multiple valid reductions for the symbols on the stack top.

## 2. Example
Consider the grammar:
`S -> a A B e`
`A -> A b c | b`
`B -> d`

Input: `a b b c d e`

Let's look at the stack and input buffer during a shift-reduce parse:
| Stack | Input Buffer | Action |
| :--- | :--- | :--- |
| `$` | `a b b c d e $` | Shift |
| `$ a` | `b b c d e $` | Shift |
| `$ a b` | `b c d e $` | Reduce by `A -> b` |
| `$ a A` | `b c d e $` | Shift |
| `$ a A b` | `c d e $` | Shift |
| `$ a A b c`| `d e $` | Reduce by `A -> A b c` |
| `$ a A` | `d e $` | Shift |
| `$ a A d` | `e $` | Reduce by `B -> d` |
| `$ a A B` | `e $` | Shift |
| `$ a A B e`| `$` | Reduce by `S -> a A B e` |
| `$ S` | `$` | Accept |

## 3. Applications & Use Cases
- **LR Parsers (Yacc/Bison):** Tools like Yacc and Bison use LALR parsing, which is a powerful and efficient form of shift-reduce parsing. It is used to generate parsers for complex programming languages (e.g., C, C++, Java).
- **Expression Evaluation:** Parsing mathematical expressions efficiently taking operator precedence and associativity into account using Operator Precedence Parsers (a type of shift-reduce parser).

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Shift-Reduce Trace for Expressions**
Grammar: `E -> E + E | E * E | id`
Input: `id1 + id2 * id3`
| Stack | Input Buffer | Action |
| :--- | :--- | :--- |
| `$` | `id1 + id2 * id3 $` | Shift |
| `$ id1` | `+ id2 * id3 $` | Reduce by `E -> id` |
| `$ E` | `+ id2 * id3 $` | Shift |
| `$ E +` | `id2 * id3 $` | Shift |
| `$ E + id2` | `* id3 $` | Reduce by `E -> id` |
| `$ E + E` | `* id3 $` | Shift (Wait! Because `*` has higher precedence than `+`) |
| `$ E + E *` | `id3 $` | Shift |
| `$ E + E * id3`| `$` | Reduce by `E -> id` |
| `$ E + E * E` | `$` | Reduce by `E -> E * E` |
| `$ E + E` | `$` | Reduce by `E -> E + E` |
| `$ E` | `$` | Accept |

**Example 2: Resolving a Shift/Reduce Conflict**
Consider the "dangling-else" grammar:
`stmt -> if expr then stmt | if expr then stmt else stmt | other`
When the parser sees `if E then if E then S`, and the next token is `else`:
The stack is: `... if E then if E then S`
Input: `else ...`
**Conflict:** Should the parser reduce `if E then S` to `stmt`, or shift `else`?
**Resolution:** Modern parsers resolve this by preferring the shift, matching the `else` with the closest unmatched `if`.

**Example 3: Identify Handles in a Rightmost Derivation**
Given `E -> E + E | E * E | ( E ) | id`
Trace the reverse rightmost derivation of `id + id * id`:
`E => E + E => E + E * E => E + E * id => E + id * id => id + id * id`
Handles:
1. `id` in `id + id * id` (reduces to `E`) -> `E + id * id`
2. `id` in `E + id * id` (reduces to `E`) -> `E + E * id`
3. `id` in `E + E * id` (reduces to `E`) -> `E + E * E`
4. `E * E` in `E + E * E` (reduces to `E`) -> `E + E`
5. `E + E` in `E + E` (reduces to `E`) -> `E`

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (5)      Explain operator grammar and operator precedence parsing  (4)  PART E  Answer any four full questions, each carries10 marks.
**[May 2019]** (4)    b)  Explain bottom- up evaluation of s-attributed definitions.
**[May 2019]** 8     Explain the main actions in a shift reduce parser  (3)  9     What are different parsing conflicts in SLR parsing table?
**[May 2019]** (3)  2    Construct a regular expression to denote a language L over ∑= {0,1} accepting  all strings of 0’s and 1’s that do not contain substring 011  (3)  3    Consider the context free grammar S->aSbS | bSaS | €  Check whether the grammar is ambiguous or not  (3)  4    What is Recursive Descent parsing?

*(Note: Solutions to be generated/verified by agent)*


### [May 2019] Explain the main actions in a shift reduce parser. (3 marks)
**Solution:**
A shift-reduce parser uses a stack to hold grammar symbols and an input buffer to hold the string to be parsed. It performs four primary actions:
1.  **Shift:** The parser shifts the next input symbol from the input buffer onto the top of the stack.
2.  **Reduce:** The parser recognizes the right end of a handle at the top of the stack. It pops the symbols corresponding to the body of the production (the handle) from the stack and pushes the non-terminal on the left side of the production rule.
3.  **Accept:** The parser announces the successful completion of parsing. This occurs when the input buffer is empty (except for the end marker `$`) and the stack contains only the start symbol of the grammar (along with the bottom marker `$`).
4.  **Error:** The parser discovers that a syntax error has occurred and invokes an error recovery routine. This happens when neither a valid shift nor a valid reduce can be performed.
