# Group Communication

## Explanation

Group communication is an abstraction in distributed systems that allows a message to be sent to a group of processes, rather than just a single destination. A group is defined by a single logical identifier (like a multicast address), and the underlying system is responsible for delivering the message to all current members of that group.

Key concepts in group communication:
1. **Group Membership Management**: A service must maintain the view of who is currently in the group (joins, leaves, crashes).
2. **Open vs. Closed Groups**:
   - **Closed Group**: Only current members of the group can send messages to it. Useful for parallel processing where nodes compute and share results strictly among themselves.
   - **Open Group**: Any process (even outside the group) can send a message to the group. Useful for delivering events to a cluster of subscribers (e.g., publish-subscribe systems).
3. **Peer-to-Peer vs. Hierarchical**:
   - **Peer-to-Peer Group**: All members are equal. Messages are multicast to all directly. If a node fails, the rest continue without structural changes.
   - **Hierarchical Group**: One member acts as a coordinator (root). Senders send to the root, which then multicasts to the members. Easier to manage ordering but introduces a single point of failure and bottleneck.

## Example

Imagine a **Distributed Database Replicaset** consisting of 3 database nodes (Node A, Node B, Node C).
These nodes form a **Closed Peer-to-Peer Group**.

```text
       [Client Process]
             | (Writes to any node)
             v
       +-----------+
       |  Node A   |
       +-----------+
      /             \
 (Multicast)     (Multicast)
    /                 \
+-----------+    +-----------+
|  Node B   |----|  Node C   |
+-----------+    +-----------+
```
When Node A receives a write request, it multicasts the update to the group {A, B, C}. The group communication middleware guarantees that all functioning nodes receive the update, ensuring database consistency.

## Applications & Use Cases

- **Fault-Tolerant Replicated Servers**: Using a group of servers so that if one fails, others can immediately take over (e.g., ZooKeeper ensemble).
- **Publish-Subscribe Systems**: Subscribers join a group corresponding to a specific topic. Publishers send messages to the open group (e.g., Kafka topics, MQTT).
- **Service Discovery**: Nodes broadcast a "Who has service X?" message to a local network group.

## 3 Solved Numerical/Analytical Examples

**Example 1: Message Complexity in P2P vs Hierarchical**
In a group of $N = 100$ nodes, a node wishes to broadcast a message. Calculate the total number of point-to-point messages required if the underlying network doesn't support hardware multicast.
*Solution:*
- **Peer-to-Peer Group**: The sending node must send $N-1$ messages (one to each other member). Total = $99$ messages. Bottleneck is on the sender's uplink.
- **Hierarchical (Tree with degree $k=10$)**: Sender sends to the root ($1$). Root sends to $10$ children ($10$). Each child sends to its $9$ leaf children ($90$). Total = $1 + 10 + 90 = 101$ messages. The load is distributed, so no single node sends 99 messages.

**Example 2: Probability of Group Failure**
A service is replicated across a group of $k=5$ identical nodes to improve availability. The probability of any single node failing independently is $p = 0.02$. What is the availability of the group (assuming the group functions if at least one node is alive)?
*Solution:*
1. Probability that all 5 nodes fail simultaneously = $p^5 = (0.02)^5 = 3.2 \times 10^{-9}$.
2. Availability = $1 - P(\text{all fail}) = 1 - 3.2 \times 10^{-9} = 0.9999999968$ (approx 9 nines).

**Example 3: Scalability of Acknowledgment Implosion**
In a reliable P2P group of $N$ members, a sender multicasts a message and requires an ACK from every receiver. If each ACK is 50 bytes and the sender's downlink is 1 Mbps, how long does it take just to receive all ACKs if $N = 10,000$?
*Solution:*
1. Number of ACKs = $10,000 - 1 = 9,999$.
2. Total ACK data = $9,999 \times 50 \text{ bytes} \approx 500 \text{ KB}$.
3. Time to receive = $(500 \times 1024 \times 8 \text{ bits}) / (10^6 \text{ bits/s}) = 4.09 \text{ seconds}$.
*Note:* This demonstrates the "ACK implosion" problem, showing why simple P2P reliable multicast scales poorly without hierarchical ACK aggregation.

## Previous Year Questions & Solutions

**[April 2018] PART C - Q16a) Explain group communication and its types. (5 marks)**
*Solution:*
Group communication is a mechanism in distributed systems where a single message is sent to a logical group identifier, and the system delivers it to all processes that are members of that group. This abstracts away the complexity of tracking individual IP addresses and managing multiple point-to-point connections.

**Types of Group Communication:**
1. **Based on Membership Access:**
   - **Open Groups:** Any process, even those outside the group, can send messages to the group. This is heavily used in publish-subscribe event systems.
   - **Closed Groups:** Only processes that have explicitly joined the group can send messages to it. This is typically used for cooperating server clusters (like database replicas) where external interference must be prevented.
2. **Based on Structure/Topology:**
   - **Peer-to-Peer Groups:** All members are considered equal. Messages are multicast directly from the sender to all other members. It is highly resilient because there is no single point of failure, but managing message ordering is complex.
   - **Hierarchical Groups:** Members are organized in a tree or hierarchy, usually with a coordinator or root node. Senders transmit to the root, which multicasts to the rest. This makes message ordering simpler but introduces a bottleneck and a single point of failure at the coordinator.
