# Ring-Based Algorithm for Mutual Exclusion

## Explanation

The **Ring-Based Algorithm** is a token-based distributed mutual exclusion protocol. According to **Tanenbaum (Chapter 6)**, this approach constructs an overlay network in the form of a logical ring, deterministically coordinating access to a Critical Section (CS) without relying on a centralized coordinator.

**Core Intuition:**
Imagine a single "talking stick" (the **token**) in a circle of people. Only the person holding the stick is allowed to speak (enter the CS). Once they finish, they pass the stick to the person on their immediate right. If the person who receives the stick has nothing to say, they simply pass it along immediately. Because there is strictly only one stick and it travels in an unalterable sequential order, we inherently guarantee that no two people can speak at the same time (Safety/Mutual Exclusion) and that everyone will eventually get a turn (Liveness/No Starvation).

**Technical Mechanism:**
1. **Logical Ring Construction:** The $N$ processes in the system, denoted as $P_0, P_1, \dots, P_{N-1}$, are assigned a position in a logical ring. The physical network topology is irrelevant; process $P_i$ simply needs to know the network address of its logical successor, $P_{(i+1) \mod N}$.
2. **The Token:** A unique control message known as the "token" continuously circulates around the logical ring. 
3. **States of a Process:**
   - **Non-critical:** The process does not need to enter the CS. When it receives the token, it immediately forwards it to its successor.
   - **Waiting:** The process wants to enter the CS but does not possess the token. It must block and wait.
   - **Critical:** The process has received the token, holds it, and executes its critical section. The token is *not* forwarded while the process is in this state.
4. **Exiting the CS:** Upon exiting the CS, the process transitions back to the non-critical state and strictly passes the token to its successor.

## Example

Let us visualize a distributed database system consisting of 4 replica servers: $S_0, S_1, S_2, S_3$. They share a single log file that must be written to sequentially. They form a logical ring: $S_0 \rightarrow S_1 \rightarrow S_2 \rightarrow S_3 \rightarrow S_0$.

**Scenario Timeline:**
- **t=0:** The token is currently held by $S_0$. $S_0$ has no data to write, so it immediately passes the token to $S_1$.
- **t=1:** At this exact moment, $S_2$ receives a client request and needs to write to the log (wants to enter the CS). It transitions to the **Waiting** state.
- **t=2:** The token arrives at $S_1$. $S_1$ doesn't need the CS. It passes the token to $S_2$.
- **t=3:** The token arrives at $S_2$. Since $S_2$ is in the **Waiting** state, it transitions to **Critical**, *retains* the token, and begins writing to the shared log file.
- **t=4:** While $S_2$ is still writing, $S_3$ and $S_0$ both receive client requests and transition to the **Waiting** state. They cannot proceed without the token.
- **t=5:** $S_2$ finishes its write operation. It exits the CS and passes the token to $S_3$.
- **t=6:** $S_3$ receives the token, holds it, and enters its CS. 
- **t=7:** $S_3$ finishes, passes the token to $S_0$.
- **t=8:** $S_0$ receives the token, holds it, and enters its CS.

This deterministic, round-robin passing ensures that despite concurrent requests at $t=4$, access is granted strictly based on the topological order of the ring.

## Applications & Use Cases

1. **Industrial Process Control (e.g., PROFIBUS):** In manufacturing floors, Programmable Logic Controllers (PLCs) often communicate over a token-passing fieldbus network. Hard real-time guarantees are essential; an assembly line robot *must* be guaranteed network access within a strictly bounded time frame (e.g., 5 milliseconds) to avoid physical collisions. The ring algorithm provides this deterministic upper bound.
2. **Legacy Token Ring LANs (IEEE 802.5):** Originally designed by IBM, this LAN technology physically or logically arranged workstations in a ring. A workstation could only transmit data frames on the shared cable if it captured the circulating 3-byte token frame, naturally avoiding data collisions.

## 3 Solved Numerical/Analytical Examples

**Example 1: Mathematical Analysis of Message Complexity**
*Problem:* Derive the message complexity for a process to enter and exit the Critical Section in a logical ring of $N$ processes under heavy load.
*Solution:*
1. **Heavy Load (Every process wants the CS):** When a process $P_i$ releases the token, it sends 1 message to its successor $P_{i+1}$. 
2. Because the load is heavy, $P_{i+1}$ is already waiting and immediately enters the CS.
3. Messages to exit CS = 1. Messages to enter CS = 0 (token just arrived).
*Conclusion:* **1 message per CS execution**. This makes the ring extremely efficient under heavy load (unlike permission-based algorithms that thrash under heavy load).

**Example 2: Calculating Synchronization Delay**
*Problem:* In a ring of 10 nodes ($N=10$), assume the message transmission time between any two adjacent nodes is exactly $T_{msg} = 5$ ms. Calculate the worst-case Synchronization Delay.
*Solution:*
1. **Synchronization Delay:** This is the time between one process leaving the CS and the next waiting process entering it.
2. *Worst Case:* The process that just released the token immediately wants to enter the CS again. The token must travel all the way around the ring through $N-1$ other nodes before returning.
3. *Calculation:* $(N-1) \times T_{msg} = (10 - 1) \times 5 \text{ ms} = 9 \times 5 = 45 \text{ ms}$.
*Conclusion:* The worst-case synchronization delay is exactly 45 ms.

**Example 3: Fault Tolerance and Token Loss Recovery**
*Problem:* What happens if the process holding the token crashes? How can the ring algorithm recover?
*Solution:*
1. If the token holder crashes, the token is permanently lost. The system halts (violating Liveness) because no other process can enter the CS.
2. **Detection:** Processes must implement a timeout mechanism. If a process does not see the token after a specified maximum time (e.g., $N \times (T_{msg} + E)$), it suspects token loss.
3. **Recovery Algorithm:**
   - The process that times out initiates an **Election** (e.g., using the Bully Algorithm).
   - The newly elected coordinator is responsible for generating a *new* single token and injecting it into the ring.
*Conclusion:* The coordinator must ensure the old token is truly lost to prevent the catastrophic failure of having two tokens simultaneously (which violates Safety).

## Previous Year Questions & Solutions

**[April 2018] Describe the ring-based algorithm for mutual exclusion. (4 marks)**

*Solution:*
Based on Tanenbaum's principles, the ring-based algorithm provides a decentralized mechanism to achieve mutual exclusion by organizing all participating distributed processes into a logical ring topology. 

**Algorithm Steps:**
1. **Logical Ring Initialization:** Let there be $N$ processes, $P_0, P_1, \dots, P_{N-1}$. Each process $P_i$ is configured to only know the network address of its immediate successor, $P_{(i+1) \mod N}$.
2. **Token Generation:** A single, unique control message called a "token" is generated and injected into the ring.
3. **Continuous Circulation:** The token continuously circulates from process to process in one direction.
4. **CS Entry Protocol:** 
   - If a process $P_i$ wishes to enter the Critical Section, it enters a `WAITING` state.
   - It cannot proceed until it receives the token from its predecessor.
   - Once it receives the token, it transitions to the `CRITICAL` state, retains the token, and executes the shared resource code.
5. **CS Exit Protocol:**
   - When $P_i$ completes its execution in the CS, it immediately forwards the token to its successor $P_{(i+1) \mod N}$.

**[April 2018] Compare Ring-based election algorithm and Bully algorithm with examples. (6 marks)**
*Solution:*
Note: This question asks to compare the **Ring Election Algorithm** (used to elect a coordinator) against the Bully algorithm, *not* the Ring Mutual Exclusion algorithm.
1. **Topology:** The Bully algorithm requires a fully connected network where every node knows every other node. The Ring algorithm only requires a logical ring topology where each node only knows its successor.
2. **Election Initiation:** In Bully, the initiator sends messages to all higher ID nodes. In Ring, the initiator sends an ELECTION message (containing its own ID) to its successor.
3. **Voting Process:** 
   - Bully: Higher ID nodes immediately reply and take over the election, bullying lower IDs into submission.
   - Ring: The ELECTION message circulates the ring. Each node appends its own ID to the message if its ID is higher than the ones currently in the message (or simply replaces it). 
4. **Resolution:** 
   - Bully: The node that receives no responses from higher IDs declares itself the winner and broadcasts a COORDINATOR message.
   - Ring: When the original ELECTION message completes a full lap and returns to the initiator, the initiator examines the list of IDs, selects the highest one, and circulates a COORDINATOR message around the ring to announce the winner.
*Example comparison:* Bully is faster (fewer message hops) but requires $O(N^2)$ messages in the worst case. Ring is slower (requires exactly 2 full laps around the ring) but is strictly bounded to $O(N)$ messages.
