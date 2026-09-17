# LL(1) Grammars

## 1. Explanation
A context-free grammar is classified as an **LL(1)** grammar if it can be parsed by a top-down, predictive parser without any backtracking. The name is an acronym describing the theoretical properties of the parser:
*   **L:** Scans the input from **L**eft to right.
*   **L:** Constructs a **L**eftmost derivation.
*   **1:** Uses exactly **1** token of lookahead to make its parsing decisions.

Mathematically, a grammar $G$ is LL(1) if and only if, for every pair of distinct productions $A \rightarrow \alpha \mid \beta$ (productions sharing the same left-hand side non-terminal), the following three strict conditions hold:
1.  **No intersection in FIRST sets:** $FIRST(\alpha) \cap FIRST(\beta) = \emptyset$. This means $\alpha$ and $\beta$ cannot derive strings starting with the same terminal. If they did, a 1-token lookahead wouldn't be enough to choose between them.
2.  **Only one can be nullable:** At most one of $\alpha$ or $\beta$ can derive the empty string $\epsilon$.
3.  **FOLLOW set non-interference:** If $\beta \Rightarrow^* \epsilon$, then $FIRST(\alpha) \cap FOLLOW(A) = \emptyset$. This means if one production can disappear, the terminals that can legally follow $A$ must be disjoint from the terminals that start $\alpha$.

If a grammar fails any of these rules, it means its predictive parsing table $M$ will have at least one cell with multiple entries (a **Multiply-Defined Entry** or conflict). 

Any grammar that has **Left Recursion** or is **Ambiguous** is mathematically proven to NEVER be LL(1). Grammars requiring **Left Factoring** are also not LL(1) until they are factored.

## 2. Example
Consider the grammar:
$S \rightarrow i E t S S' \mid a$
$S' \rightarrow e S \mid \epsilon$
$E \rightarrow b$

Is it LL(1)? Let's check the distinct productions for $S'$: $S' \rightarrow e S$ and $S' \rightarrow \epsilon$.
*   $FIRST(e S) = \{e\}$
*   $FIRST(\epsilon) = \{\epsilon\}$
*   Intersection is empty (Condition 1 & 2 passed).
*   Since $S' \rightarrow \epsilon$, we must check Condition 3: $FIRST(e S) \cap FOLLOW(S')$. 
*   $FOLLOW(S')$ inherits from $FOLLOW(S)$. Since $S$ is the start symbol, $FOLLOW(S) = \{\$\}$. Also in $S \rightarrow i E t S S'$, $S$ is followed by $S'$. So $FOLLOW(S)$ gets $FIRST(S') \setminus \{\epsilon\} = \{e\}$. So $FOLLOW(S') = \{e, \$\}$.
*   Wait! $FIRST(e S) = \{e\}$. $FOLLOW(S') = \{e, \$\}$. Their intersection is $\{e\}$!
*   Condition 3 fails! The intersection is not empty.
Therefore, this grammar is **NOT LL(1)**. This represents the classic dangling-else ambiguity.

## 3. Applications & Use Cases
*   **Compiler Design (Parser Generators):** When developers use JavaCC, ANTLR (historically LL-based), or write custom Recursive Descent Parsers, they must manually massage their grammar into an LL(1) format (or use LL(k)/GLR techniques). Understanding the strict LL(1) rules allows language designers to shape syntax that compiles extremely fast (linear time $O(n)$) without immense memory overhead.
*   **Network Protocol Parsers:** Protocols like HTTP headers or JSON bodies are parsed using strict non-ambiguous LL(1) rules to guarantee fast, deterministic parsing without DoS vulnerabilities caused by backtracking.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Demonstrating Left Recursion violates LL(1)**
*Problem:* Prove $E \rightarrow E + T \mid T$ is not LL(1).
*Solution:*
Let $\alpha = E + T$ and $\beta = T$.
To be LL(1), $FIRST(E + T)$ and $FIRST(T)$ must be disjoint.
Because $E$ can derive $T$, any terminal that starts a string derived from $T$ can also start a string derived from $E$. Thus, $FIRST(T) \subseteq FIRST(E + T)$. Therefore, the intersection is $FIRST(T) \neq \emptyset$. The grammar fails condition 1 and is not LL(1).

**Example 2: Tracing an LL(1) parse using a stack**
*Problem:* Given an LL(1) parsing table where $M[S, a] = S \rightarrow a$, input string is `a$`. Trace the stack.
*Solution:*
1.  Initialize stack with `$` then `S`. Input is `a$`. Lookahead is `a`.
2.  Top of stack is non-terminal `S`. Look up $M[S, a]$. It gives $S \rightarrow a$.
3.  Pop `S`, push `a` (right side of production reversed). Stack is now `$ a`.
4.  Top of stack is terminal `a`. It matches lookahead `a`. Pop `a`, consume input `a`.
5.  Stack is `$`. Input is `$`. Parsing successful.

**Example 3: Checking LL(1) conditions**
*Problem:* Is the grammar $S \rightarrow A B$, $A \rightarrow a \mid \epsilon$, $B \rightarrow a \mid b$ LL(1)?
*Solution:*
Check $A \rightarrow a \mid \epsilon$.
1. $FIRST(a) = \{a\}$, $FIRST(\epsilon) = \{\epsilon\}$. Intersection empty.
2. Only one nullable.
3. Since $A \rightarrow \epsilon$, check $FIRST(a) \cap FOLLOW(A)$.
$FOLLOW(A) = FIRST(B) = \{a, b\}$.
$FIRST(a) \cap FOLLOW(A) = \{a\} \cap \{a, b\} = \{a\}$.
The intersection is not empty! Fails condition 3. It is NOT LL(1). (If lookahead is `a`, should parser expand $A \rightarrow a$ or $A \rightarrow \epsilon$ letting $B$ handle the `a`? It's ambiguous for a 1-token lookahead).

## 5. Previous Year Questions & Solutions

### [April 2018]
**Question:** What is an LL(1) grammar? What are the conditions for a grammar to be LL(1)?
**Solution:**
An **LL(1) grammar** is a context-free grammar that can be deterministically parsed from Left-to-right, producing a Leftmost derivation, using exactly 1 token of lookahead, without ever requiring backtracking.

**Conditions:**
A grammar $G$ is LL(1) if and only if, for every set of productions $A \rightarrow \alpha \mid \beta$ (two distinct productions for the same non-terminal $A$), the following three strict mathematical conditions hold:
1.  **Disjoint FIRST sets:** $FIRST(\alpha)$ and $FIRST(\beta)$ are disjoint sets (i.e., $FIRST(\alpha) \cap FIRST(\beta) = \emptyset$). This ensures that the lookahead token can uniquely identify which production to use.
2.  **Unique Nullability:** At most one of the strings $\alpha$ or $\beta$ can derive the empty string $\epsilon$. If both could derive $\epsilon$, the parser could not decide which one to apply when bypassing $A$.
3.  **FOLLOW set disjointness (if nullable):** If $\beta \Rightarrow^* \epsilon$ (meaning $\beta$ is nullable), then the set $FIRST(\alpha)$ must be completely disjoint from the set $FOLLOW(A)$ (i.e., $FIRST(\alpha) \cap FOLLOW(A) = \emptyset$). This ensures that if the parser sees a token that can follow $A$, it unambiguously knows to choose the $\epsilon$-production ($\beta$) rather than mistakenly trying to parse it as part of $\alpha$.

If these conditions are met, the predictive parsing table $M$ constructed for the grammar will have at most one production in any cell $M[A, a]$, guaranteeing deterministic $O(n)$ time parsing. Left recursive and ambiguous grammars inherently violate these conditions.
