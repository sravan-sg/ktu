# Recognition of Tokens

## 1. Explanation
While Regular Expressions (Regex) provide the mathematical and declarative **specification** of what tokens should look like, they do not provide an algorithm for the computer to actually read the source file and extract those tokens. The computational mechanism used to scan the text and recognize these patterns is the **Transition Diagram** and its formal mathematical equivalent, the **Finite State Automaton (FSA)**.

To **recognize** tokens, the lexical analyzer uses a state machine. It begins in an initial state, reads a character from the input buffer, and transitions to a new state based on that character. 
*   **Transition Diagrams:** These are flowcharts used by compiler engineers to manually design scanners. They consist of nodes (states) and directed edges (transitions labeled with characters). Double circles denote **accepting states**, meaning a valid token has been fully matched.
*   **Finite Automata (NFA and DFA):** These are the formal equivalents. 
    *   **NFA (Nondeterministic Finite Automaton):** Allows multiple transitions for the same character or $\epsilon$-transitions (spontaneous state changes). It's easy to build directly from a regex, but slow to simulate in software.
    *   **DFA (Deterministic Finite Automaton):** Has exactly one transition per state per character, and no $\epsilon$-transitions. It is fast to execute (taking $O(N)$ time for $N$ characters). Compilers mathematically convert Regex $\rightarrow$ NFA $\rightarrow$ DFA, and then the DFA is implemented as a 2D lookup table in the generated C code.

When the scanner reaches an accepting state but reading the *next* character causes a failure, it performs a **retract** operation (pushing the last read character back into the buffer) and emits the token. This relies on the **longest-match principle** (maximal munch).

## 2. Example
Consider the token for relational operators: `<`, `<=`, `<>`, `>`, `>=`, `=`.

A transition diagram to recognize them starts at State 0:
1.  Read `<`. Transition to State 1.
2.  From State 1:
    *   Read `=`. Transition to State 2 (Accepting state for `<=`).
    *   Read `>`. Transition to State 3 (Accepting state for `<>`).
    *   Read any *other* character. Transition to State 4 (Accepting state for `<`), and execute a `retract()` to push the *other* character back.

## 3. Applications & Use Cases
*   **Lex/Flex Tools:** When you run `flex scan.l`, the tool parses your regular expressions, builds an NFA using Thompson's Construction, converts it to a minimized DFA using subset construction, and outputs a highly optimized `switch-case` or table-driven loop in C code to recognize those tokens at extremely high speeds.
*   **Network Packet Inspection:** Deep Packet Inspection (DPI) hardware routers use DFA tables compiled directly into ASIC silicon to recognize malware signatures in network streams at wire speed (100+ Gbps).

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: State Transition for Identifiers**
*Problem:* Design a Transition Diagram for an identifier: `letter (letter | digit)*`. What happens if the input is `sum =`?
*Solution:*
*   **State 0 (Start):** On reading `letter`, go to State 1.
*   **State 1:** On reading `letter` or `digit`, loop back to State 1.
*   **State 1:** On reading `other` (e.g., whitespace, `=`), go to State 2.
*   **State 2 (Accepting):** Emit `id`. Execute `retract()` for the `other` character.
*Trace for `sum =`:*
1.  Read `s` $\rightarrow$ State 1.
2.  Read `u` $\rightarrow$ State 1.
3.  Read `m` $\rightarrow$ State 1.
4.  Read ` ` (space) $\rightarrow$ State 2. 
5.  State 2 emits `id` for "sum". The space is retracted to be processed as whitespace.

**Example 2: The Longest Match Principle**
*Problem:* A language has tokens for `<=` (less equal) and `<` (less). If the input is `<=`, why doesn't the scanner just emit `<` after the first character?
*Solution:*
Lexical analyzers implement the **maximal munch** rule. The scanner is programmed to consume characters as long as there is a valid path forward in the DFA. When reading `<`, it enters a state where `=` is a valid next transition. Because it greedily looks for the longest possible match, it will read `=`, reach a final state for `<=`, and only emit when no further characters can extend the token.

**Example 3: Simulating a DFA Transition Table**
*Problem:* Create a transition table for recognizing `a(b|c)*`.
*Solution:*
State 0: Start. State 1: Accepting. State 2: Error/Dead state.
*   Input `a`: `T[0, 'a'] = 1`
*   Input `b` or `c`: `T[0, 'b'] = 2`, `T[0, 'c'] = 2`
*   Input `b` or `c`: `T[1, 'b'] = 1`, `T[1, 'c'] = 1`
*   Input `a`: `T[1, 'a'] = 2`
The table allows a software loop to simply execute `state = T[state, char]` until an error or EOF is reached, proving how abstract tokens are practically recognized in code.

## 5. Previous Year Questions & Solutions

### [April 2018]
**Question:** How are transition diagrams used for recognizing tokens? Illustrate with an example of relational operators.
**Solution:**
**Use of Transition Diagrams:**
While regular expressions specify the syntax of tokens, Transition Diagrams provide a computational model (a flowchart) that demonstrates how a lexical analyzer sequentially reads input characters to identify those tokens. A transition diagram acts as a deterministic finite automaton (DFA) where nodes represent the state of the scanner and edges represent state transitions triggered by the current input character. 
The scanner starts at the initial node. For each character read from the input buffer, it follows the corresponding edge. If it lands on a node with double circles (an accepting state), it signifies a token has been recognized. Some accepting states are marked with an asterisk `*`, which indicates that a **retract** operation is required (meaning the scanner read one character too far to realize the token had ended, and that character must be pushed back into the buffer).

**Illustration for Relational Operators:**
Consider the C-style relational operators: `<`, `<=`, `==`, `!=`, `>`, `>=`.
The transition diagram would start at `State 0`.
1.  **Branch for `<`**: 
    If input is `<`, go to `State 1`.
    From `State 1`:
    - If input is `=`, go to `State 2` (Accepting State, emit `<=`).
    - If input is `>`, go to `State 3` (Accepting State, emit `<>`).
    - If input is any `other` character, go to `State 4*` (Accepting State, emit `<`. Retract the `other` character).
2.  **Branch for `=`**: 
    If input is `=`, go to `State 5`.
    From `State 5`:
    - If input is `=`, go to `State 6` (Accepting State, emit `==`).
    - If input is `other`, go to `State 7*` (Accepting State, emit `=`. Retract `other`).
3.  **Branch for `>`**:
    If input is `>`, go to `State 8`.
    From `State 8`:
    - If input is `=`, go to `State 9` (Accepting State, emit `>=`).
    - If input is `other`, go to `State 10*` (Accepting State, emit `>`. Retract `other`).

By directly translating these nodes and edges into `switch` statements or a 2D array, the compiler successfully recognizes complex tokens from raw text.
