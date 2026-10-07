# Specification of Tokens using Regular Expressions

## 1. Explanation
In the first phase of compilation, the Lexical Analyzer (or Scanner) reads the raw source code character by character and groups them into meaningful, atomic chunks called **tokens** (e.g., identifiers, keywords, constants, operators). 

To computationally identify these tokens, we need a rigorous mathematical formalism to describe their allowed character patterns. This formalism is the **Regular Expression (Regex)**. In the Chomsky Hierarchy, regular expressions generate Type-3 languages (Regular Languages), which are exactly the set of languages that can be recognized by a Finite State Automaton (FSA).

A regular expression is built recursively from a finite alphabet $\Sigma$ using three fundamental operations:
1.  **Union (Alternation) $r_1 | r_2$:** Matches a string if it matches either $r_1$ or $r_2$. Represented formally as the set union $L(r_1) \cup L(r_2)$.
2.  **Concatenation $r_1 \cdot r_2$:** Matches a string formed by a string from $r_1$ followed immediately by a string from $r_2$.
3.  **Kleene Closure (Star) $r^*$:** Matches zero or more concatenations of strings from $r$. It represents repetition. Note that $r^*$ always includes the empty string $\epsilon$.
4.  **Positive Closure $r^+$ (Syntactic Sugar):** Matches one or more repetitions. It is formally equivalent to $r \cdot r^*$.
5.  **Optional $r?$ (Syntactic Sugar):** Matches zero or one occurrence of $r$. Formally equivalent to $r \mid \epsilon$.

The lexical analyzer takes a set of regular expressions defining all valid tokens in the programming language, constructs a Deterministic Finite Automaton (DFA) for them, and uses this DFA to scan the input stream efficiently in $O(N)$ time.

## 2. Example
Consider the formal specification for a typical C-style **identifier** (variable name). 
The rule is: *An identifier must start with a letter or underscore, followed by any number of letters, digits, or underscores.*

First, we define our shorthand classes:
*   $letter \rightarrow A | B | \dots | Z | a | b | \dots | z | \_$
*   $digit \rightarrow 0 | 1 | 2 | \dots | 9$

Then, the formal regular expression for the token `id` is:
$$id \rightarrow letter \cdot (letter \mid digit)^*$$

Visually, the scanner reads a $letter$, and then enters a state where it accepts a loop of either $letter$ or $digit$ until it hits a whitespace or operator, at which point it emits the `id` token.

## 3. Applications & Use Cases
*   **Lexical Analyzer Generators (Lex/Flex):** In real-world compiler engineering, developers rarely write the DFA state-transitions by hand. Instead, they use tools like `lex` or `flex`. The engineer writes a `.l` file containing only the regular expressions (e.g., `[0-9]+` for integers), and the tool mathematically converts these regexes into a highly optimized C program containing the corresponding DFA transition tables.
*   **Text Processing & Grep:** The ubiquitous Unix tool `grep` (Global Regular Expression Print) and text editors (like VSCode) use these exact same theoretical regex engines for complex text searching and refactoring.
*   **Input Validation:** Web frameworks heavily rely on regular expressions to validate email addresses, phone numbers, and password complexities before accepting user input.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Designing a regex for floating-point numbers**
*Problem:* Write a regular expression for a floating-point number that must contain a decimal point, optionally has a fractional part, optionally has an integer part (but cannot be entirely empty), and optionally contains a signed exponent (e.g., `3.14`, `.5`, `3.`, `1.2E-4`).
*Solution:*
Let $d$ represent a digit (`0-9`).
1.  Integer part (optional): $d^*$
2.  Fractional part (optional): $d^*$
Wait, if both are $d^*$, then just a lone decimal point `.` would be accepted. We must ensure at least one digit exists.
We can break it into two cases:
Case A (Digit before decimal): $d^+ \cdot . \cdot d^*$
Case B (No digit before decimal, so must have digit after): $. \cdot d^+$
Base float: $(d^+ . d^*) \mid (. d^+)$
Exponent part (optional): $(E (+ \mid - \mid \epsilon) d^+)$
Full regex: $((d^+ . d^*) \mid (. d^+)) \cdot (E (+ \mid - \mid \epsilon) d^+)?$

**Example 2: String matching and ambiguity**
*Problem:* Given the regex `(a | b)* a b b`, verify if the strings `aabb` and `bbab` are accepted.
*Solution:*
The regex describes strings of `a`'s and `b`'s that *must* end in the exact sequence `a b b`.
*   String `aabb`: Can be split into `a` (from `(a|b)*`) followed by `abb`. ACCEPTED.
*   String `bbab`: Ends in `bab`, not `abb`. REJECTED.

**Example 3: Constructing regex for a specific binary constraint**
*Problem:* Write a regular expression for the language over alphabet $\Sigma = \{0, 1\}$ representing all binary strings containing at least two consecutive 1s.
*Solution:*
The required substring is `11`.
Before the `11`, we can have any sequence of 0s and 1s: $(0 \mid 1)^*$
After the `11`, we can have any sequence of 0s and 1s: $(0 \mid 1)^*$
Concatenating them guarantees the condition:
$(0 \mid 1)^* \cdot 11 \cdot (0 \mid 1)^*$

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (3)  2    Construct a regular expression to denote a language L over ∑= {0,1} accepting  all strings of 0’s and 1’s that do not contain substring 011  (3)  3    Consider the context free grammar S->aSbS | bSaS | €  Check whether the grammar is ambiguous or not  (3)  4    What is Recursive Descent parsing?

*(Note: Solutions to be generated/verified by agent)*


### [May 2019]
**Question:** Write a regular expression for identifying valid floating-point numbers in a standard programming language. Explain the components of your expression.
**Solution:**
A standard floating-point number can have an optional sign, an integer part, a mandatory decimal point, a fractional part, and an optional exponent (e.g., `-3.14e+10`). 

Let us define the building block:
$digit \rightarrow [0-9]$
$digits \rightarrow digit^+$ (one or more digits)

The regular expression is composed of three main parts:
1.  **Sign (Optional):** `(+ | -)?`
2.  **Base Number:** `(digits \. digits?) | (\. digits)`
    This allows numbers like `123.45`, `123.`, and `.45`, ensuring that at least one digit is present either before or after the mandatory decimal point (`\.`).
3.  **Exponent (Optional):** `( [eE] (+ | -)? digits )?`
    This captures the scientific notation, allowing `e` or `E`, an optional sign, and the exponent power.

**Final Complete Regular Expression:**
`(+ | -)? ( (digits \. digits?) | (\. digits) ) ( [eE] (+ | -)? digits )?`

*Explanation of components:*
*   `?` denotes zero or one occurrence (optional).
*   `|` denotes alternation (OR).
*   `\` is used to escape the literal dot character, distinguishing it from the regex metacharacter that matches any character. 

### [December 2020]
**Question:** Explain how tokens are specified using regular expressions. Give the regular expression for an identifier.
**Solution:**
In lexical analysis, a token is a logically cohesive sequence of characters. We specify the valid structures of these tokens using **Regular Expressions (Regex)** because they provide a precise, concise, and mathematically rigorous way to define pattern rules, which can then be algorithmically converted into Finite Automata for rapid string matching.

Tokens are specified by combining base character classes using three core operations:
1.  **Union ($|$):** To allow multiple valid characters (e.g., matching a digit OR a letter).
2.  **Concatenation ($\cdot$):** To mandate sequence order (e.g., an `i` followed strictly by an `f` for the keyword `if`).
3.  **Kleene Closure ($^*$):** To allow unbounded repetition (e.g., zero or more characters forming a variable name).

**Regex for an Identifier:**
In most programming languages, an identifier must begin with an alphabetic character or an underscore, and can be followed by zero or more alphanumeric characters or underscores. 
We define the character classes:
$letter \rightarrow [a-zA-Z\_]$
$digit \rightarrow [0-9]$

The regular expression specifying this token is:
`letter (letter | digit)*`

This explicitly enforces that the first character drawn from the input stream MUST belong to the $letter$ class, while subsequent characters (iterated by the $^*$ operator) can belong to either the $letter$ or $digit$ class.
