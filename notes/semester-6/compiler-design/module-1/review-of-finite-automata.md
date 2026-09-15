# Review of Finite Automata

## 1. Explanation
Finite Automata (FA) are theoretical mathematical machines used to recognize patterns described by regular expressions. They are the backbone of Lexical Analysis. A Lexer generator (like Lex) converts regular expressions into finite automata to process character streams.

There are two main types:
1. **NFA (Nondeterministic Finite Automata):**
   - Can have multiple transitions for the same input symbol from a single state.
   - Can have $\epsilon$-transitions (state changes without consuming any input character).
   - Easier to construct directly from a regular expression (using Thompson's Construction).
2. **DFA (Deterministic Finite Automata):**
   - For a given state and input symbol, there is exactly one transition to a next state.
   - No $\epsilon$-transitions allowed.
   - Faster to execute in software because simulating a DFA requires tracking only one current state, whereas an NFA requires tracking a set of possible states.

**The Pipeline:**
`Regular Expression` $\rightarrow$ (Thompson's Construction) $\rightarrow$ `NFA` $\rightarrow$ (Subset Construction) $\rightarrow$ `DFA` $\rightarrow$ (State Minimization) $\rightarrow$ `Optimized DFA` (Code).

## 2. Example
To recognize the regex `(a|b)*abb`:
1. Start in an initial state $q_0$.
2. Loop on $q_0$ for `a` and `b`.
3. Transition to $q_1$ on `a`.
4. Transition to $q_2$ on `b`.
5. Transition to final state $q_3$ on `b`.
Because $q_0$ has two transitions for `a` (one looping to $q_0$, one going to $q_1$), this is an NFA. 

## 3. Applications & Use Cases
- **Lexical Analyzers:** Flex converts your `.l` regex rules into a minimized DFA represented as a 2D transition table in C code.
- **Text Search:** Tools like `grep` build NFAs/DFAs on the fly to search massive text files for string patterns in $O(N)$ time.
- **Network Intrusion Detection:** Deep packet inspection tools use DFAs to scan network traffic payloads for malicious byte signatures.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Regex to NFA (Thompson's Construction)**
*Problem:* Construct an NFA for the regex `ab`.
*Solution:* 
Create a start state $q_0$. Add transition on `a` to $q_1$. Add an $\epsilon$-transition from $q_1$ to $q_2$. Add transition on `b` from $q_2$ to $q_3$ (final state). (Or simply $q_0 \xrightarrow{a} q_1 \xrightarrow{b} q_2$).

**Example 2: NFA to DFA (Subset Construction)**
*Problem:* Why convert NFA to DFA?
*Solution:* Simulating an NFA in software requires maintaining a dynamic list (or set) of all currently active states, which is computationally expensive ($O(N \times M)$ where $N$ is string length and $M$ is states). A DFA only requires a single state pointer and a 2D array lookup `next_state = transition_table[current_state][input_char]`, making it $O(N)$ time.

**Example 3: Epsilon Closure**
*Problem:* In an NFA, state 1 has an $\epsilon$-transition to state 2, and state 2 has an $\epsilon$-transition to state 3. What is $\epsilon$-closure(1)?
*Solution:* $\epsilon$-closure of a state includes the state itself and all states reachable by following only $\epsilon$ edges. 
Result: `{1, 2, 3}`.

## 5. Previous Year Questions & Solutions
[May 2019]
**Question:** Differentiate between NFA and DFA. (4 marks)
**Solution:**
| Feature | NFA (Nondeterministic Finite Automata) | DFA (Deterministic Finite Automata) |
| :--- | :--- | :--- |
| **Transitions** | Multiple transitions allowed for the same input symbol from a single state. | Exactly one transition per input symbol from a given state. |
| **Epsilon ($\epsilon$) Moves** | Allowed. Can change states without consuming input. | Not allowed. Every transition must consume an input symbol. |
| **Construction** | Easier to construct directly from a regular expression. | Harder to construct directly; usually derived by converting an NFA. |
| **Execution Speed** | Slower to simulate (must track multiple active states). | Much faster to simulate (tracks only one active state). |
| **Memory** | Requires less memory (fewer states). | Can suffer from state explosion (exponential memory increase). |
