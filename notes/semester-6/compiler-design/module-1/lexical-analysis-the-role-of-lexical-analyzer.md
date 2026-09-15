# Lexical Analysis: The Role of Lexical Analyzer

## 1. Explanation
The **Lexical Analyzer** (or Scanner) is the first phase of a compiler. Its primary role is to read the raw input characters of the source program, group them into lexemes (meaningful character strings), and output a sequence of **tokens** for the Syntax Analyzer (Parser).

A token is a pair `<token-name, attribute-value>`:
- **Token Name:** An abstract symbol representing the lexical unit (e.g., `id`, `num`, `assign_op`).
- **Attribute Value:** A pointer to the symbol table entry containing information about the token (e.g., the actual string "count", or the value 42).

**Key Responsibilities of the Lexical Analyzer:**
1. **Tokenization:** Converting the character stream into a token stream.
2. **Stripping Whitespace & Comments:** Removing spaces, tabs, newlines, and comments which the parser does not care about.
3. **Error Reporting:** Correlating error messages with the source program (e.g., tracking the line number where an illegal character was found).
4. **Macro Expansion:** In some languages (like C), preprocessing directives are handled here.

The lexer and parser typically operate in a producer-consumer relationship. The parser calls a function (e.g., `getNextToken()`), and the lexer reads characters until it identifies the next valid token, returning it to the parser.

## 2. Example
Consider the C code snippet:
`/* Calculate sum */`
`sum = 3 + 2;`

The Lexical Analyzer processes this as follows:
1. Encounters `/* ... */`, identifies it as a comment, and strips it.
2. Reads `s`, `u`, `m`. Encounters space. Outputs `<id, pointer to symbol table entry for "sum">`.
3. Reads `=`. Outputs `<assign_op, >`.
4. Reads `3`. Outputs `<num, 3>`.
5. Reads `+`. Outputs `<add_op, >`.
6. Reads `2`. Outputs `<num, 2>`.
7. Reads `;`. Outputs `<semi, >`.

## 3. Applications & Use Cases
- **Syntax Highlighting:** IDEs use lightweight lexical analyzers to color-code keywords (blue), strings (green), and comments (grey) in real-time as you type.
- **Minifiers:** Web development tools use a lexer to strip out all comments, whitespace, and shorten variable names in JavaScript files to reduce load times (e.g., UglifyJS).

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Distinguishing Lexeme and Token**
*Problem:* In the statement `printf("Hello");`, what is the lexeme and token for `printf`?
*Solution:* 
- **Lexeme:** The actual character sequence `p-r-i-n-t-f`.
- **Token:** `<id, ptr>` (Identifier).

**Example 2: Lexical Error Detection**
*Problem:* What happens when the lexical analyzer encounters `int x = 5$y;` in C?
*Solution:* It reads `int` (keyword), `x` (id), `=` (assign_op), `5` (num). It then encounters `$`. Since `$` is not a valid character in C identifiers or operators, the lexer throws a **Lexical Error** (e.g., "Illegal character '$' at line N").

**Example 3: Token Count with Comments**
*Problem:* How many tokens are generated for the following snippet?
```c
int main() {
    // Return 0
    return 0;
}
```
*Solution:*
1. `int` (keyword)
2. `main` (id)
3. `(` (punctuation)
4. `)` (punctuation)
5. `{` (punctuation)
*(The comment `// Return 0` is stripped and yields 0 tokens)*
6. `return` (keyword)
7. `0` (num)
8. `;` (punctuation)
9. `}` (punctuation)
Total = 9 tokens.

## 5. Previous Year Questions & Solutions
[Sample Question Paper]
**Question:** Explain the role of a Lexical Analyzer. (3 marks)
**Solution:**
The Lexical Analyzer is the first phase of compilation. Its primary roles are:
1. It reads the source program as a stream of characters and groups them into meaningful sequences called lexemes.
2. It produces a sequence of tokens (`<token-name, attribute-value>`) corresponding to each lexeme and passes it to the parser.
3. It filters out comments and whitespace from the source code, simplifying the parser's job.
4. It keeps track of line numbers to provide precise error reporting for the subsequent phases.
