# Top-down parsing: Recursive Descent parsing

## 1. Explanation
Top-down parsing is a parsing strategy that attempts to build a parse tree for an input string from the root (the start symbol) down to the leaves (the terminals).

**Recursive Descent Parsing** is a prominent top-down parsing technique. It uses a set of mutually recursive procedures (functions) to process the input. Each non-terminal in the grammar has an associated function.
- The execution begins with the function for the start symbol.
- Inside a function for non-terminal `A`, if the production is `A -> X Y Z`, the function will:
  1. Call the function for `X` (if `X` is a non-terminal) or match `X` with the input (if `X` is a terminal).
  2. Proceed to do the same for `Y` and `Z`.

**Key Problems:**
- **Left Recursion:** If a grammar has left recursion (e.g., `A -> A x`), a recursive descent parser will enter an infinite loop because the function for `A` immediately calls `A` again without consuming any input.
- **Backtracking:** If multiple productions exist for a non-terminal (e.g., `A -> a b | a c`), the parser might choose the first one, successfully match `a`, but fail on `b`. It then has to "backtrack", resetting the input pointer, to try the second alternative.
- Predictive Parsing (a variant of recursive descent without backtracking) solves this by using lookahead tokens, provided the grammar is factored and left-recursion is eliminated.

## 2. Example
Consider a simple grammar:
`S -> c A d`
`A -> a b | a`

Pseudocode for `S`:
```c
void S() {
    if (lookahead == 'c') {
        match('c');
        A();
        match('d');
    } else error();
}
```
Pseudocode for `A` (with backtracking):
```c
void A() {
    int saved_pointer = current_input_pointer;
    if (lookahead == 'a') {
        match('a');
        if (lookahead == 'b') {
            match('b'); return; // Successfully matched A -> a b
        }
    }
    // Backtrack and try A -> a
    current_input_pointer = saved_pointer; 
    if (lookahead == 'a') {
        match('a'); return;
    }
    error();
}
```

## 3. Applications & Use Cases
- **Hand-written Parsers:** Because the structure of a recursive descent parser directly mirrors the grammar, it is very easy to write by hand. High-performance compilers (like GCC and Clang for C/C++) often use hand-written recursive descent parsers because they allow for excellent custom error messages and fast execution.
- **Configuration File Parsers:** Reading formats like JSON or custom DSLs (Domain Specific Languages) is easily achieved with simple recursive descent.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Eliminating Left Recursion**
A recursive descent parser cannot handle `E -> E + T | T`.
We must eliminate left recursion.
Rule: `A -> A α | β` becomes `A -> β A'` and `A' -> α A' | €`.
Applying this to `E`:
`E -> T E'`
`E' -> + T E' | €`
Now `E()` can be implemented recursively without an infinite loop.

**Example 2: Left Factoring**
A recursive descent parser struggles with `A -> a b c | a b d` because it doesn't know which to pick when it sees `a`.
Left factoring extracts the common prefix.
Rule: `A -> α β1 | α β2` becomes `A -> α A'` and `A' -> β1 | β2`.
Result: 
`A -> a b A'`
`A' -> c | d`
This makes the grammar suitable for predictive parsing without backtracking.

**Example 3: Trace of Recursive Descent**
Grammar: `S -> x y Z`, `Z -> z`
Input: `x y z`
1. Call `S()`.
2. `S()` checks if input is `x`. It matches. Consumes `x`. Input is now `y z`.
3. `S()` checks if input is `y`. It matches. Consumes `y`. Input is now `z`.
4. `S()` calls `Z()`.
5. `Z()` checks if input is `z`. It matches. Consumes `z`. Input is empty.
6. `Z()` returns successfully.
7. `S()` returns successfully. Parse complete.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (5)      Explain operator grammar and operator precedence parsing  (4)  PART E  Answer any four full questions, each carries10 marks.
**[May 2019]** (4)  7  a) What is left recursive grammar?
**[May 2019]** 8     Explain the main actions in a shift reduce parser  (3)  9     What are different parsing conflicts in SLR parsing table?
**[May 2019]** (3)  2    Construct a regular expression to denote a language L over ∑= {0,1} accepting  all strings of 0’s and 1’s that do not contain substring 011  (3)  3    Consider the context free grammar S->aSbS | bSaS | €  Check whether the grammar is ambiguous or not  (3)  4    What is Recursive Descent parsing?

*(Note: Solutions to be generated/verified by agent)*


### [May 2019] What is Recursive Descent parsing? List the problems faced in designing such a parser. (3 marks)
**Solution:**
**Recursive Descent Parsing:** It is a top-down parsing technique where a set of mutually recursive procedures is written to represent the grammar rules. Each non-terminal has a corresponding procedure that attempts to match the right side of its production with the input string.
**Problems faced in designing:**
1. **Left Recursion:** If the grammar contains left-recursive rules (e.g., `A -> A α`), the recursive procedure will call itself infinitely without consuming input, leading to a stack overflow.
2. **Backtracking:** If the grammar is not suitably factored, the parser might take a wrong path, fail, and have to undo its actions (backtrack) to try another alternative, which is highly inefficient.
3. **Ambiguity:** Like all parsers, it cannot handle ambiguous grammars directly without specific conflict resolution logic.

### [May 2019] Design a recursive descent parser for the grammar E->E + T | T, T->T*F | F, F->(E) | id. (5 marks)
**Solution:**
**Step 1: Eliminate Left Recursion.**
A recursive descent parser cannot handle the given grammar because of immediate left recursion in `E` and `T`. We must transform it:
```text
E  -> T E'
E' -> + T E' | €
T  -> F T'
T' -> * F T' | €
F  -> ( E ) | id
```

**Step 2: Write Recursive Procedures (Pseudocode in C-style).**
Assuming `lookahead` holds the current token and `match(token)` consumes it and advances.

```c
void E() {
    T();
    Eprime();
}

void Eprime() {
    if (lookahead == '+') {
        match('+');
        T();
        Eprime();
    }
    // Else € production, do nothing (return)
}

void T() {
    F();
    Tprime();
}

void Tprime() {
    if (lookahead == '*') {
        match('*');
        F();
        Tprime();
    }
    // Else € production, do nothing
}

void F() {
    if (lookahead == '(') {
        match('(');
        E();
        if (lookahead == ')') {
            match(')');
        } else error();
    } else if (lookahead == id) {
        match(id);
    } else {
        error();
    }
}
```
This is the complete, working design for a predictive recursive descent parser for the given grammar.
