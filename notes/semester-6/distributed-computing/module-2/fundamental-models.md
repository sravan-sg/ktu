# Fundamental Models

## Explanation
**Fundamental Models** provide an abstract perspective for examining the individual characteristics of distributed systems. Rather than focusing on physical hardware or software architectures, fundamental models examine the fundamental properties that govern the behavior of processes and networks. They allow engineers to reason about correctness, reliability, and security mathematically.

The three primary fundamental models are:
1. **Interaction Model**: Deals with the performance and timing properties of the communication channels between processes. It addresses the fact that distributed processes interact by passing messages, and these messages experience variable delays. It divides systems into:
   - *Synchronous Distributed Systems*: There are known upper and lower bounds on execution times, message transmission delays, and clock drift rates. (Rare in practice, useful for theory).
   - *Asynchronous Distributed Systems*: There are no bounds on execution speeds, message transmission delays, or clock drift rates. (Models the actual Internet).
2. **Failure Model**: Defines the precise ways in which a system can fail. This is crucial for designing fault-tolerant algorithms. Types of failures include:
   - *Omission Failures*: A process or channel fails to perform actions it is supposed to do (e.g., dropping a message, process crashing). Fail-stop is a specific case where a process halts and remains halted.
   - *Arbitrary (Byzantine) Failures*: The worst-case scenario where a process or channel can exhibit any behavior whatsoever, including sending malicious or corrupted data.
   - *Timing Failures*: Applicable only in synchronous systems, where an action occurs outside the specified time bounds.
3. **Security Model**: Defines the threats that a distributed system must mitigate. It categorizes threats against processes (e.g., spoofing, denial of service) and communication channels (e.g., eavesdropping, man-in-the-middle attacks), and outlines mechanisms like cryptography to enforce confidentiality, integrity, and authentication.

## Example
Consider a distributed banking application where a user transfers funds. 
- The **Interaction Model** helps the engineer understand that the network request might take 10ms or 10 seconds (Asynchronous). 
- The **Failure Model** requires the engineer to handle the scenario where the server crashes exactly after deducting money but before crediting the other account (Omission failure). 
- The **Security Model** dictates that the network traffic must be encrypted with TLS to prevent a hacker from intercepting the transaction details (Channel threat).

## Applications & Use Cases
1. **Consensus Algorithms in Blockchain**: Systems like Bitcoin must assume an *Asynchronous Interaction Model* and an *Arbitrary (Byzantine) Failure Model*, as malicious nodes might intentionally broadcast incorrect ledger information.
2. **Aircraft Fly-by-Wire Systems**: These are designed using a *Synchronous Interaction Model*. Sensors and actuators must communicate within strict deadlines, and any *Timing Failure* could result in a catastrophic physical crash.
3. **Secure Web Services (HTTPS)**: Specifically addresses the *Security Model* by employing public-key infrastructure to authenticate the server and symmetric encryption to protect the integrity and confidentiality of the channel.

## 3 Solved Numerical/Analytical Examples

**Example 1: Byzantine Fault Tolerance Threshold**
*Problem:* In a distributed system with $N$ replicas modeled under the Arbitrary (Byzantine) Failure model, what is the maximum number of faulty nodes $f$ the system can tolerate to reach consensus?
*Solution:*
A classic result in distributed computing states that in an asynchronous network, Byzantine consensus requires $N \ge 3f + 1$. 
If $N = 10$, the maximum number of faulty nodes $f$ must satisfy $10 \ge 3f + 1 \implies 9 \ge 3f \implies f \le 3$.
The system can tolerate up to 3 Byzantine failures.

**Example 2: Analyzing Clock Drift in the Interaction Model**
*Problem:* Two servers A and B have hardware clocks with a maximum drift rate of $\rho = 10^{-5}$ seconds per second relative to true time. If they are perfectly synchronized at $T=0$, what is the maximum possible difference between their clocks after 1 hour (3600 seconds)?
*Solution:*
In the worst case, clock A drifts forward at $+\rho$ and clock B drifts backward at $-\rho$.
Max relative drift rate = $2\rho = 2 \times 10^{-5}$.
Max difference after $\Delta T = 3600$ s is:
$2\rho \times \Delta T = 2 \times 10^{-5} \times 3600 = 0.072$ seconds (72 milliseconds).

**Example 3: Message Omission Probability**
*Problem:* In a failure model with omission failures, a communication channel drops packets with a probability of $p = 0.01$. If a sender requires a 99.999% guarantee that a critical message is delivered, how many times $k$ must it transmit the message (assuming independent failures)?
*Solution:*
Probability of all $k$ messages being dropped = $p^k$.
We want $1 - p^k \ge 0.99999 \implies p^k \le 0.00001$.
$(0.01)^k \le 10^{-5}$.
$10^{-2k} \le 10^{-5}$.
$-2k \le -5 \implies k \ge 2.5$.
Therefore, the sender must transmit the message at least 3 times.

## Previous Year Questions & Solutions

**[April 2018] Q12. b) What are the fundamental models? Explain in detail. [4 Marks]**
*Solution:*
**Fundamental Models** are abstract representations used to examine the core properties, behaviors, and design choices in a distributed system, focusing on interaction, failure, and security rather than physical hardware. 

The three primary fundamental models are:
1. **Interaction Model**: Analyzes the communication between processes and the timing of events. It classifies systems into:
   - *Synchronous Systems*: Have strict, known bounds on processing time, message delay, and clock drift.
   - *Asynchronous Systems*: Have no bounds on processing time or message delays (e.g., the Internet).
2. **Failure Model**: Classifies the types of faults that can occur, enabling the design of fault-tolerant systems. Types include:
   - *Omission Failures*: A process crashes (fail-stop) or a channel drops messages.
   - *Arbitrary/Byzantine Failures*: A component behaves maliciously or unpredictably.
   - *Timing Failures*: An action completes outside the specified time limit (only applicable in synchronous systems).
3. **Security Model**: Identifies potential threats to processes and communication channels (e.g., eavesdropping, spoofing) and dictates the necessary cryptographic mechanisms (authentication, encryption) to protect the system's integrity and confidentiality.
