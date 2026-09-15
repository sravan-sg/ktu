# Specification of Tokens using Regular Expressions

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
