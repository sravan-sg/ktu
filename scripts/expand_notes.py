import os
import glob

module_1_content = {
    "phases-of-a-compiler.md": """# Phases of a compiler

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
""",
    "specification-of-tokens-using-regular-expressions.md": """# Specification of Tokens using Regular Expressions

## 1. Explanation
Regular expressions (regex) are a formal language used for describing sets of strings (patterns). In compilers, they are used by the Lexical Analyzer to specify the exact character patterns for valid tokens.
- `a | b` means `a` or `b`
- `a*` means zero or more `a`s
- `a+` means one or more `a`s
- `(a)` for grouping.

## 2. Example
Identifier definition: `letter (letter | digit)*`
Number definition: `digit+ (. digit+)? (E (+|-)? digit+)?`

## 3. Applications & Use Cases
Regex engines are used in Lex tools like Flex to automatically generate the C code for a lexical analyzer. They are also widely used in data validation and search tools.

## 4. 3 Solved Numerical/Analytical Examples
**Example 1:** Write a regex for a language over {0, 1} containing at least two 0s.
**Solution:** `(0|1)* 0 (0|1)* 0 (0|1)*`

## 5. Previous Year Questions & Solutions
[May 2019]
**Question:** Write a regular expression for identifying floating-point numbers.
**Solution:** `[0-9]+ \. [0-9]+`
"""
}

module_2_content = {
    "top-down-parsing-recursive-descent-parsing.md": """# Top-Down Parsing: Recursive Descent parsing

## 1. Explanation
Top-down parsing attempts to construct a parse tree for the input string starting from the root (start symbol) and creating the nodes in pre-order. Recursive Descent parsing uses a set of recursive procedures, one for each non-terminal in the grammar. If it requires backtracking, it can be slow; but if the grammar is LL(1), predictive parsing can be used.

## 2. Example
Grammar:
`S -> cAd`
`A -> ab | a`
A procedure `S()` will check for 'c', call `A()`, and then check for 'd'.

## 3. Applications & Use Cases
Recursive descent parsers are very common in production compilers (like GCC and Clang) because they are easy to write, read, and maintain by hand, offering excellent custom error reporting.

## 4. 3 Solved Numerical/Analytical Examples
**Example 1:** Why is left recursion a problem for Recursive Descent?
**Solution:** If `A -> A \alpha`, the procedure `A()` will immediately call `A()` again, leading to an infinite loop.

## 5. Previous Year Questions & Solutions
[Sample Question Paper]
**Question:** What are the problems with Top-Down parsing? Explain recursive descent parsing.
**Solution:** 
Problems: Left recursion causes infinite loops, and common prefixes require backtracking.
Recursive Descent Parsing: A top-down parsing technique constructed from a set of mutually recursive procedures where each procedure implements one of the nonterminals of the grammar.
"""
}

base = "/home/sravan/ktu/notes/semester-6/compiler-design"

def write_files(module_num, content_dict):
    mod_dir = os.path.join(base, f"module-{module_num}")
    for file_name, content in content_dict.items():
        path = os.path.join(mod_dir, file_name)
        if os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)
                
write_files(1, module_1_content)
write_files(2, module_2_content)
print("Expanded modules 1 and 2.")
