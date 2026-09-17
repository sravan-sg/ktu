# Phases of a Compiler

## 1. Explanation
A compiler is a complex software system that translates a program written in a high-level source language (like C, Java, or Rust) into a low-level target language (like Assembly or Machine Code). Because this translation is incredibly complex, modern compilers are architected as a pipeline of sequential **phases**. Each phase transforms the source program from one representation to another, progressively stripping away human-readable abstraction and replacing it with machine-level specificity.

The compilation process is broadly divided into two logical parts:
1.  **Analysis (Front-End):** Breaks up the source program into constituent pieces and creates an intermediate representation. Its primary job is to understand the *syntax and semantics* of the code. This part is largely independent of the target machine.
2.  **Synthesis (Back-End):** Constructs the desired target program from the intermediate representation. Its primary job is *optimization and code generation*. This part is heavily dependent on the target machine's architecture.

The classic 6 phases of a compiler are:
1.  **Lexical Analysis (Scanner):** Reads the raw character stream and groups them into meaningful sequences called **tokens** (e.g., identifiers, operators, keywords). It eliminates whitespace and comments.
2.  **Syntax Analysis (Parser):** Takes the stream of tokens and groups them hierarchically into a **Syntax Tree** (or Parse Tree) governed by the Context-Free Grammar of the language. It verifies grammatical correctness.
3.  **Semantic Analysis:** Checks the syntax tree for semantic consistency with the language rules. It performs **type checking** (e.g., ensuring you don't add a string to a float) and resolves variable declarations.
4.  **Intermediate Code Generation (ICG):** Translates the semantic tree into an explicit, machine-independent low-level representation (like Three-Address Code). It acts as a bridge between the front-end and back-end.
5.  **Code Optimization:** Modifies the intermediate code to make it faster and consume less memory, without changing its logical output. Examples include loop unrolling and constant folding.
6.  **Code Generation:** Maps the optimized intermediate code to the specific instruction set and registers of the target CPU architecture.

Throughout all these phases, two critical data structures operate globally:
*   **Symbol Table:** A data structure (usually a hash table) containing a record for each identifier, with fields for its attributes (type, scope, memory location).
*   **Error Handler:** A subsystem invoked whenever a phase detects an error, allowing the compiler to report it and potentially recover to find further errors.

## 2. Example
Consider the compilation of the assignment statement: `position = initial + rate * 60`
1.  **Lexical Analyzer:** Yields tokens: `id1 = id2 + id3 * 60`
2.  **Syntax Analyzer:** Builds a tree respecting precedence: `*` binds `id3` and `60` tighter than `+`.
3.  **Semantic Analyzer:** Discovers that `60` is an integer but `rate` is a float. It inserts an `inttofloat` conversion node into the tree.
4.  **Intermediate Code Generator:** Emits Three-Address Code:
    ```
    t1 = inttofloat(60)
    t2 = id3 * t1
    t3 = id2 + t2
    id1 = t3
    ```
5.  **Code Optimizer:** Notices `60` is a constant. Pre-computes the float conversion at compile time:
    ```
    t1 = id3 * 60.0
    id1 = id2 + t1
    ```
6.  **Code Generator:** Emits x86 Assembly:
    ```assembly
    MOVF id3, R2
    MULF #60.0, R2
    MOVF id2, R1
    ADDF R2, R1
    MOVF R1, id1
    ```

## 3. Applications & Use Cases
*   **LLVM Architecture:** Modern production compilers like Clang (for C/C++) and rustc (for Rust) strictly follow this phased architecture using the LLVM framework. The Front-End (Analysis) converts C++ or Rust to LLVM Intermediate Representation (IR). The Middle-End optimizes the IR. The Back-End (Synthesis) generates machine code for x86, ARM, or WebAssembly. This phased design allows the same optimizer and backend to be reused across dozens of languages.
*   **Just-in-Time (JIT) Compilation:** Engines like V8 (JavaScript) or the JVM execute the Lexical, Syntax, and Semantic phases rapidly, generating bytecode. The Code Optimization and Generation phases happen dynamically at runtime, optimizing hot code paths based on live execution data.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Tracing Lexical Output**
*Problem:* What is the output of the Lexical Analyzer for the statement `while (x >= 10) x = x - 1;`?
*Solution:*
The lexical analyzer groups characters and emits a stream of token-attribute pairs:
`<KEYWORD, "while">`, `<PUNCT, "(">`, `<ID, "x">`, `<REL_OP, ">=">`, `<NUM, 10>`, `<PUNCT, ")">`, `<ID, "x">`, `<ASSIGN, "=">`, `<ID, "x">`, `<ARITH_OP, "-">`, `<NUM, 1>`, `<PUNCT, ";">`.

**Example 2: Semantic Analysis Type Coercion**
*Problem:* Given the declaration `int a; float b;` and the expression `b = a + 3.14;`, how does the Semantic Analyzer modify the syntax tree?
*Solution:*
The syntax tree initially shows addition between `a` (type: integer) and `3.14` (type: float). The semantic analyzer queries the Symbol Table, confirms `a` is an `int`, and detects a type mismatch. It strictly enforces language semantics by inserting a type coercion node: `inttofloat(a)`. The resulting node evaluates to a `float`, which correctly matches the type of `b` for the assignment.

**Example 3: Three-Address Code (TAC) Generation**
*Problem:* Generate the Three-Address Code for the expression `x = -y * (z + w)`.
*Solution:*
TAC allows a maximum of three operands (two sources, one destination) per line.
```
t1 = -y          // Unary minus
t2 = z + w       // Addition inside parentheses
t3 = t1 * t2     // Multiplication
x = t3           // Final assignment
```

## 5. Previous Year Questions & Solutions

### [April 2018]
**Question:** Explain the different phases of a compiler with a neat diagram. Trace the translation of the statement `a = b + c * 50` through all phases.
**Solution:**
A compiler operates in several sequential phases, divided logically into Analysis (front-end) and Synthesis (back-end). 

**The Phases:**
1.  **Lexical Analysis:** Scans the source string and groups characters into tokens.
2.  **Syntax Analysis:** Groups tokens into grammatical phrases, represented by a parse tree.
3.  **Semantic Analysis:** Checks the parse tree for semantic errors (e.g., type checking).
4.  **Intermediate Code Generation:** Produces a machine-independent, low-level representation (like 3-address code).
5.  **Code Optimization:** Optimizes the intermediate code for speed and memory efficiency.
6.  **Code Generation:** Translates the optimized code into target machine language.
*Both the Symbol Table (which stores identifiers) and the Error Handler communicate directly with all 6 phases.*

*(Diagram Description: A linear flow from "Source Program" down through the 6 phases to "Target Program", with "Symbol Table Manager" and "Error Handler" positioned parallel to the flow, with bidirectional arrows connecting to every single phase.)*

**Trace for `a = b + c * 50`:**
Assume `a`, `b`, and `c` are floats.
1.  **Lexical Analysis:** `<id, 1> <=> <id, 2> <+> <id, 3> <*> <num, 50>`
2.  **Syntax Analysis:** Generates an Abstract Syntax Tree where `=` is the root. Its left child is `id1`. Its right child is a `+` node. The `+` node's left child is `id2`, and its right child is a `*` node (due to precedence). The `*` node has children `id3` and `50`.
3.  **Semantic Analysis:** Detects that `50` is an integer while the rest are floats. Modifies the tree so the `50` node is wrapped in an `inttofloat` conversion node.
4.  **Intermediate Code Gen:**
    `t1 = inttofloat(50)`
    `t2 = id3 * t1`
    `t3 = id2 + t2`
    `id1 = t3`
5.  **Code Optimization:** Pre-computes the float conversion.
    `t1 = id3 * 50.0`
    `id1 = id2 + t1`
6.  **Code Generation:** (Assuming generic accumulator-based assembly)
    `LDF R2, id3`
    `MULF R2, #50.0`
    `LDF R1, id2`
    `ADDF R1, R2`
    `STF id1, R1`

### [December 2019]
**Question:** Differentiate between the Analysis and Synthesis phases of a compiler. Which phase is responsible for type checking?
**Solution:**
**Analysis Phase (Front-End):**
The analysis phase breaks down the source code to understand its structure and meaning. It consists of Lexical Analysis, Syntax Analysis, and Semantic Analysis. Its primary goal is to ensure the program is syntactically and semantically correct, and then it generates an Intermediate Representation (IR). This phase is heavily dependent on the *source language* (e.g., C vs Java) but is completely independent of the target machine hardware.

**Synthesis Phase (Back-End):**
The synthesis phase takes the Intermediate Representation and constructs the final target program. It consists of Code Optimization and Code Generation. Its primary goal is efficiency and accurate translation to machine code. This phase is heavily dependent on the *target machine architecture* (e.g., x86 vs ARM) but is completely independent of the original source language.

**Type Checking Responsibility:**
Type checking is the sole responsibility of the **Semantic Analysis** phase. After the Syntax Analyzer confirms the structure is valid (e.g., $A + B$), the Semantic Analyzer queries the Symbol Table to ensure the operation is meaningful (e.g., verifying you are not trying to add a boolean to an array). If types mismatch, it either throws a type error or performs implicit type coercion (like converting an `int` to a `float`).
