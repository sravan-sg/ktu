# Predictive Parsing & FIRST/FOLLOW Sets

## 1. Explanation
Predictive Parsing is an optimized form of top-down recursive descent parsing that entirely eliminates **backtracking**. Instead of guessing which production rule to apply, a predictive parser looks ahead at the very next token in the input stream (a 1-token lookahead) and consults a mathematically derived **Parsing Table** to make the absolute correct choice in $O(1)$ time.

To build this table, the compiler computes two vital sets for the grammar: **FIRST** and **FOLLOW**.

**1. FIRST($\alpha$):** 
The set of all terminal symbols that can appear as the *very first symbol* of any string derived from $\alpha$.
*   If $X$ is a terminal, $FIRST(X) = \{X\}$.
*   If $X \rightarrow \epsilon$ is a production, then $\epsilon \in FIRST(X)$.
*   If $X \rightarrow Y_1 Y_2 \dots Y_k$, then add $FIRST(Y_1)$ to $FIRST(X)$. If $Y_1$ can derive $\epsilon$, also add $FIRST(Y_2)$, and so on.

**2. FOLLOW($A$):** 
The set of all terminal symbols that can appear *immediately to the right* of non-terminal $A$ in some sentential form. 
*   Place the end-of-input marker `$` in $FOLLOW(S)$, where $S$ is the start symbol.
*   If there is a production $A \rightarrow \alpha B \beta$, then everything in $FIRST(\beta)$ except $\epsilon$ is placed in $FOLLOW(B)$.
*   If there is a production $A \rightarrow \alpha B$, or $A \rightarrow \alpha B \beta$ where $FIRST(\beta)$ contains $\epsilon$, then everything in $FOLLOW(A)$ is added to $FOLLOW(B)$.

**The Parsing Table $M[A, a]$:**
The table has non-terminals as rows and terminals as columns.
For every production $A \rightarrow \alpha$:
1.  For each terminal $a$ in $FIRST(\alpha)$, add $A \rightarrow \alpha$ to $M[A, a]$.
2.  If $\epsilon \in FIRST(\alpha)$, for each terminal $b$ in $FOLLOW(A)$, add $A \rightarrow \alpha$ to $M[A, b]$.

## 2. Example
Consider the grammar:
$S \rightarrow a B$
$B \rightarrow b \mid \epsilon$

**Compute FIRST:**
*   $FIRST(S) = \{a\}$
*   $FIRST(B) = \{b, \epsilon\}$

**Compute FOLLOW:**
*   $FOLLOW(S) = \{\$\}$
*   $B$ appears at the end of $S \rightarrow a B$, so $FOLLOW(B)$ gets $FOLLOW(S)$. $FOLLOW(B) = \{\$\}$.

**Parsing Table $M$:**
| Non-Terminal | $a$ | $b$ | $\$$ |
| :--- | :--- | :--- | :--- |
| **S** | $S \rightarrow a B$ | | |
| **B** | | $B \rightarrow b$ | $B \rightarrow \epsilon$ |

Because there is at most one rule in every cell, this grammar can be deterministically parsed without backtracking!

## 3. Applications & Use Cases
*   **LL(1) Parser Generators:** Tools like JavaCC use predictive parsing logic to generate top-down parsers in Java. They calculate FIRST and FOLLOW sets during compilation of the grammar file to populate the internal dispatch tables.
*   **Fast Failures:** Predictive parsing provides immediate error detection. If the parser looks up $M[A, a]$ and the cell is empty, it instantly throws a syntax error before wasting time attempting to process the token.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Computing FIRST sets with nullables**
*Problem:* Compute FIRST sets for $S \rightarrow A B C$, $A \rightarrow a \mid \epsilon$, $B \rightarrow b \mid \epsilon$, $C \rightarrow c$.
*Solution:*
*   $FIRST(A) = \{a, \epsilon\}$
*   $FIRST(B) = \{b, \epsilon\}$
*   $FIRST(C) = \{c\}$
*   To find $FIRST(S)$: Look at $A B C$. Add $FIRST(A)$ (which is $a$). Since $A$ has $\epsilon$, look at $B$. Add $FIRST(B)$ (which is $b$). Since $B$ has $\epsilon$, look at $C$. Add $FIRST(C)$ (which is $c$). Thus, $FIRST(S) = \{a, b, c\}$.

**Example 2: Computing FOLLOW sets**
*Problem:* Compute FOLLOW sets for $E \rightarrow T E'$, $E' \rightarrow + T E' \mid \epsilon$, $T \rightarrow \text{id}$.
*Solution:*
1.  $FOLLOW(E)$ gets `$` because it's the start symbol. $FOLLOW(E) = \{\$\}$.
2.  In $E \rightarrow T E'$, $E'$ is at the end, so $FOLLOW(E')$ gets $FOLLOW(E)$. $FOLLOW(E') = \{\$\}$.
3.  In $E \rightarrow T E'$, $T$ is followed by $E'$. So $FIRST(E')$ (which is `{+}`) goes into $FOLLOW(T)$. Also, since $E'$ can be $\epsilon$, $FOLLOW(E)$ goes into $FOLLOW(T)$. $FOLLOW(T) = \{+, \$\}$.

**Example 3: Filling a Parsing Table Cell**
*Problem:* For $E' \rightarrow + T E' \mid \epsilon$, where $FIRST(E') = \{+\}$ and $FOLLOW(E') = \{\$\}$, fill the table row for $E'$.
*Solution:*
*   For rule $E' \rightarrow + T E'$: The FIRST set of $+ T E'$ is just $\{+\}$. So put $E' \rightarrow + T E'$ in $M[E', +]$.
*   For rule $E' \rightarrow \epsilon$: The FIRST set is $\{\epsilon\}$. We look at $FOLLOW(E')$, which is $\{\$\}$. So put $E' \rightarrow \epsilon$ in $M[E', \$]$.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2019]** (5)      Explain operator grammar and operator precedence parsing  (4)  PART E  Answer any four full questions, each carries10 marks.
**[May 2019]** 8     Explain the main actions in a shift reduce parser  (3)  9     What are different parsing conflicts in SLR parsing table?
**[May 2019]** (3)  2    Construct a regular expression to denote a language L over ∑= {0,1} accepting  all strings of 0’s and 1’s that do not contain substring 011  (3)  3    Consider the context free grammar S->aSbS | bSaS | €  Check whether the grammar is ambiguous or not  (3)  4    What is Recursive Descent parsing?

*(Note: Solutions to be generated/verified by agent)*


### [July 2021]
**Question:** What are FIRST and FOLLOW sets? Explain their roles in predictive parsing.
**Solution:**
**FIRST Set:** For any string of grammar symbols $\alpha$, $FIRST(\alpha)$ is the set of terminal symbols that begin strings derived from $\alpha$. If $\alpha$ can derive the empty string $\epsilon$, then $\epsilon$ is also in $FIRST(\alpha)$.
**FOLLOW Set:** For any non-terminal $A$, $FOLLOW(A)$ is the set of terminals that can appear immediately to the right of $A$ in some sentential form derived from the start symbol.

**Role in Predictive Parsing:**
Predictive parsers eliminate backtracking by using a lookahead token to deterministically choose the correct production rule. To construct the 2D predictive parsing table (with non-terminals on rows and terminals on columns), the compiler algorithm heavily relies on these two sets:
1.  When constructing the table, if we are at non-terminal $A$ and looking at input token $a$, we must pick a production $A \rightarrow \alpha$ such that $a$ is in $FIRST(\alpha)$. This guarantees that choosing this production is a valid path to eventually matching the token $a$.
2.  If the lookahead token $a$ is not in $FIRST(\alpha)$ for any production, but there is a production $A \rightarrow \epsilon$, we must know if it's safe to erase $A$ and let the *next* non-terminal handle the token $a$. We use the $FOLLOW(A)$ set for this. If $a$ is in $FOLLOW(A)$, we safely select $A \rightarrow \epsilon$.
Without FIRST and FOLLOW sets, building an algorithmic predictive parsing table is impossible.

### [April 2018]
**Question:** Compute the FIRST and FOLLOW sets for the grammar: 
$S \rightarrow ( L ) \mid a$
$L \rightarrow S L'$
$L' \rightarrow , S L' \mid \epsilon$
**Solution:**
**Step 1: Compute FIRST Sets**
*   $FIRST(S)$: Look at RHS. First rule starts with terminal `(`. Second rule starts with terminal `a`. So, $FIRST(S) = \{ (, a \}$.
*   $FIRST(L)$: Looks at RHS $S L'$. The FIRST of $L$ is $FIRST(S)$ because $S$ cannot be $\epsilon$. So, $FIRST(L) = \{ (, a \}$.
*   $FIRST(L')$: Look at RHS. First rule starts with terminal `,`. Second rule is $\epsilon$. So, $FIRST(L') = \{ ,, \epsilon \}$.

**Step 2: Compute FOLLOW Sets**
*   $FOLLOW(S)$: Rule 1: Start symbol gets `$\Rightarrow FOLLOW(S)$ contains `$`. 
    Rule 2: $S \rightarrow ( L )$. Here $L$ is followed by `)`. So `)` goes into $FOLLOW(L)$. No, wait, what follows $S$? 
    Look at $L \rightarrow S L'$. $S$ is followed by $L'$. So $FIRST(L') \setminus \{\epsilon\}$ goes into $FOLLOW(S)$. Thus `,` goes into $FOLLOW(S)$. Since $L' \rightarrow \epsilon$, $FOLLOW(L)$ also goes into $FOLLOW(S)$. 
    Look at $L' \rightarrow , S L'$. $S$ is followed by $L'$. Same as above.
    We need $FOLLOW(L)$ to finish $FOLLOW(S)$. Let's find $FOLLOW(L)$ first.
*   $FOLLOW(L)$: $L$ appears in $S \rightarrow ( L )$. It is followed by `)`. So $FOLLOW(L) = \{ ) \}$.
*   Back to $FOLLOW(S)$: $FOLLOW(S)$ gets `$`, gets `,` (from FIRST of L'), and gets $FOLLOW(L)$ (which is `)`). 
    So $FOLLOW(S) = \{ \$, ,, ) \}$.
*   $FOLLOW(L')$: $L'$ appears at the end of $L \rightarrow S L'$ and $L' \rightarrow , S L'$. So $FOLLOW(L')$ gets $FOLLOW(L)$ and $FOLLOW(L')$. 
    So $FOLLOW(L') = FOLLOW(L) = \{ ) \}$.

**Final Sets:**
$FIRST(S) = \{ (, a \}$
$FIRST(L) = \{ (, a \}$
$FIRST(L') = \{ ,, \epsilon \}$

$FOLLOW(S) = \{ \$, ,, ) \}$
$FOLLOW(L) = \{ ) \}$
$FOLLOW(L') = \{ ) \}$
