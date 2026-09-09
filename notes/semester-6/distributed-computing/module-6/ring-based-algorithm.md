# Ring-Based Algorithm for Mutual Exclusion

## Explanation
The **Ring-Based Algorithm** provides a distributed solution to mutual exclusion without relying on a single central coordinator. 

**How it works:**
1.  **Logical Ring:** All $N$ processes in the system are organized into a logical ring topology. Each process is assigned an ID (e.g., $P_0, P_1, ..., P_{N-1}$) and only needs to know the network address of its immediate neighbor in the ring (i.e., process $P_i$ talks to $P_{(i+1) \mod N}$).
2.  **The Token:** A single, unique message called the **"token"** constantly circulates around the logical ring from process to process.
3.  **Entering the CS:** When a process wants to enter the Critical Section (CS), it must wait until it receives the token from its neighbor. Once it has the token, it retains it and enters the CS.
4.  **Leaving the CS:** When the process finishes executing in the CS, it simply passes the token to its next neighbor in the ring.
5.  **Idle State:** If a process receives the token but does *not* need to enter the CS, it immediately passes the token to its neighbor.

## Example
Consider a ring of 4 processes: $P_0 \rightarrow P_1 \rightarrow P_2 \rightarrow P_3 \rightarrow P_0$.
- The token is currently at $P_1$. $P_1$ does not need the CS. It passes the token to $P_2$.
- $P_2$ wants to enter the CS. It receives the token, holds it, and enters the CS.
- While $P_2$ is in the CS, $P_0$ decides it wants the CS. $P_0$ must wait.
- $P_2$ finishes the CS. It passes the token to $P_3$.
- $P_3$ doesn't need it, passes to $P_0$.
- $P_0$ receives the token, holds it, and enters the CS.

## Applications & Use Cases
-   **Token Ring Networks:** The original IEEE 802.5 Token Ring local area network standard implemented this exact logic at the hardware/link layer to prevent data collisions on the shared network cable.
-   **Industrial Control Systems:** In environments where guaranteed fairness and a strict upper bound on waiting time are required (hard real-time systems), ring-based passing guarantees every node gets a turn in a deterministic timeframe.

## 3 Solved Numerical/Analytical Examples
**Example 1: Message Complexity**
What is the message complexity for entering and exiting the CS in the worst-case and best-case scenarios for a ring of $N$ nodes?
*Solution:*
-   **Best-case:** The process wants to enter the CS at the exact moment the token arrives. It holds it (0 messages to enter) and then passes it to the next node when done (1 message to exit). Total = 1 to N messages depending on how one defines the boundary, but strictly speaking, once you have it, it's just the passing overhead. In standard terms, it consumes between $1$ and $N$ messages per CS entry depending on how far the token has to travel.
-   **Continuous load (Message Complexity):** To continuously circulate the token when no one wants the CS, it takes $N$ messages per cycle. If only one node wants the CS, it still takes $N$ messages (or $N-1$) for the token to get back to it. Thus, the message complexity is $O(N)$.

**Example 2: Synchronization Delay**
What is the synchronization delay (the time between one process exiting the CS and the next waiting process entering it)?
*Solution:*
It depends on where the next waiting process is in the ring.
-   **Best case:** The immediate neighbor is waiting. Delay = 1 message transmission time.
-   **Worst case:** The process that just finished is waiting again, or the node immediately "behind" it in the ring is waiting. The token must travel all the way around. Delay = $N-1$ message transmission times.

**Example 3: Drawbacks**
Why is the ring-based algorithm considered inefficient at low loads?
*Solution:*
At low loads (when nobody wants to enter the CS), the token must still continuously circulate around the network so that it is available when needed. In a ring of 1000 nodes, this means 1000 messages are constantly being sent and received over the network per cycle, consuming network bandwidth and CPU interrupts, even when absolutely zero useful work is being done.

## Previous Year Questions & Solutions

**[April 2018] Describe the ring-based algorithm for mutual exclusion. (4 marks)**
*Solution:*
The ring-based algorithm achieves distributed mutual exclusion by organizing all participating processes into a logical ring topology. 
1.  **Logical Ring:** Each process is assigned a position in the ring and only knows the address of its immediate successor.
2.  **Token Passing:** A special message called a "token" circulates continuously around this logical ring in one direction.
3.  **Entering CS:** A process can only enter the Critical Section (CS) if it possesses the token. If it wants to enter, it waits for the token to arrive, holds it, and then executes its CS.
4.  **Exiting CS:** Once the process finishes its execution in the CS, it releases the token by forwarding it to its immediate successor in the ring. If a process receives the token but does not need the CS, it forwards the token immediately.

**Advantages:** It guarantees mutual exclusion (since there is only one token) and ensures fairness (no starvation, as the token travels in a strict order).
**Disadvantages:** It has a high synchronization delay (up to $N-1$ message delays) and consumes constant network bandwidth even when no process wants to enter the CS, because the token must keep circulating. Additionally, token loss (if a node crashes while holding it) requires complex recovery mechanisms.
