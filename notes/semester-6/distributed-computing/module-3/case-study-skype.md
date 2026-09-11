# Case Study: Skype

## Explanation

Skype (in its original architectural design, documented by Baset and Schulzrinne, and heavily featured in Tanenbaum) is one of the most successful examples of a **Hierarchically Organized Peer-to-Peer (P2P) Network**. It serves as a prime case study for building massively scalable distributed systems that span multiple administrative domains (like different corporate networks and ISPs) without suffering from administrative scalability bottlenecks, because the end-users themselves collaborate to keep the network running.

Skype is not a pure P2P network; it uses a **Hybrid Architecture** consisting of three distinct components:

1. **Weak Peers (Ordinary Clients):** The standard Skype software running on a user's laptop or mobile device. These nodes have limited bandwidth and are often hidden behind Network Address Translation (NAT) routers or strict corporate firewalls.
2. **Super Peers (Super Nodes):** Ordinary nodes that have public IP addresses, high bandwidth, and high availability. They are dynamically promoted by the network. Super nodes act as relay stations and directory servers for the weak peers connected to them.
3. **The Centralized Login Server:** The only purely centralized component. It authenticates users, ensures user IDs are globally unique, and handles administrative tasks (like billing) that are mathematically or practically impossible to handle in a decentralized manner.

### Key Mechanisms:
- **Bootstrapping (The Host Cache):** How does a new peer find the network? Every weak peer maintains a local **Host Cache**—a list containing a few hundred `(IP Address, Port Number)` pairs of known super nodes. When Skype starts, it tries to connect to these. If none are reachable, it falls back to a hard-coded list of default super nodes built into the software binary.
- **NAT Traversal:** Because most weak peers are behind firewalls, they cannot accept incoming TCP connections. To solve this, a weak peer immediately establishes a persistent outgoing TCP connection to a super peer upon startup. When another user wants to call them, the incoming call is routed *through* the super peer, bypassing the firewall constraint.

## Example

**Alice Calls Bob (Both Behind Firewalls)**
Imagine Alice is on a university Wi-Fi (behind NAT) and Bob is on a corporate network (behind a strict firewall). 
1. **Bootstrapping:** Alice opens Skype. Her software checks its **Host Cache** and establishes an outbound TCP connection to Super Node A (a user with a public IP in Texas). Bob does the same, connecting to Super Node B in London.
2. **Authentication:** Alice securely logs in via the **Centralized Login Server**.
3. **Routing:** Alice wants to call Bob. Because both are behind NATs and cannot directly connect to each other's IP addresses, Alice sends the voice data to Super Node A, which routes it to Super Node B, which pushes it down the persistent TCP connection to Bob. The super nodes act as an essential bridge.

## Applications & Use Cases

1. **Voice Over IP (VOIP) Telephony:** Providing free, global voice and video calls without the company (Skype) having to pay for the massive bandwidth required, as the users (super nodes) shoulder the routing burden.
2. **Peer-Assisted Streaming:** Systems like Spotify (historically) used identical hierarchical P2P models where users with fast connections buffered and served music tracks to nearby users to save centralized server costs.
3. **Firewall Bypassing Services:** The architecture is heavily used in VPNs and overlay networks (like Hamachi or ZeroTier) where a publicly accessible "super node" coordinates connections between isolated LANs.

## 3 Solved Numerical/Analytical Examples

**Example 1: Bootstrapping Delay Calculation**
*Problem:* A weak peer starts up and begins pinging its Host Cache to find an active super node. It takes 50 ms to ping an address and timeout if it's dead. The Host Cache has 200 addresses. Historically, 95% of these super nodes have gone offline since the user last logged in. How long will it take, on average, for the peer to find an active super node, assuming it tests them sequentially?
*Solution:*
1. The probability that a node is active is $p = 0.05$.
2. The expected number of attempts $E(X)$ to find the first active node follows a geometric distribution: $E(X) = \frac{1}{p}$.
3. $E(X) = \frac{1}{0.05} = 20$ attempts.
4. The expected delay is $20 \times 50 \text{ ms} = 1000 \text{ ms} = 1 \text{ second}$.
5. *Conclusion:* Due to the dynamic nature of P2P networks, caching hundreds of addresses is required to keep bootstrapping time under a second.

**Example 2: Centralized Login Server Load Reduction**
*Problem:* Skype has 10 million active users. If it used a pure client-server model, every user would send a 1 KB "keep-alive" heartbeat to the central server every 10 seconds. In the hierarchical P2P model, only the 100,000 Super Nodes send an aggregated 5 KB heartbeat to the central server every 10 seconds. Calculate the bandwidth saved at the central server in Megabytes per second (MBps).
*Solution:*
1. **Client-Server Load:** 
   $10,000,000 \text{ users} \times 1 \text{ KB} = 10,000,000 \text{ KB}$ every 10 seconds.
   Load = $1,000,000 \text{ KB/s} \approx 1,000 \text{ MBps}$ (or 8 Gbps).
2. **Hierarchical P2P Load:** 
   $100,000 \text{ Super Nodes} \times 5 \text{ KB} = 500,000 \text{ KB}$ every 10 seconds.
   Load = $50,000 \text{ KB/s} \approx 50 \text{ MBps}$.
3. **Savings:** $1000 - 50 = 950 \text{ MBps}$.
4. *Conclusion:* The hierarchical architecture reduces the central server's bandwidth costs by 95%, making the system economically viable.

**Example 3: NAT Traversal Routing Overhead**
*Problem:* Alice and Bob are communicating via a Super Node. The direct distance between Alice and Bob is 500 km. However, the available Super Node is physically located 3,000 km away. The speed of data in the fiber is $2 \times 10^8$ m/s. What is the latency penalty (overhead) in milliseconds introduced by the P2P NAT routing?
*Solution:*
1. **Direct Latency (if no NAT existed):**
   Delay = $\frac{500 \times 10^3 \text{ m}}{2 \times 10^8 \text{ m/s}} = 0.0025 \text{ s} = 2.5 \text{ ms}$.
2. **Routed Latency (Alice -> Super Node -> Bob):**
   Distance = $3,000 \text{ km} + 3,000 \text{ km} = 6,000 \text{ km}$. (Assuming Bob is also roughly 3,000 km from the node).
   Delay = $\frac{6000 \times 10^3 \text{ m}}{2 \times 10^8 \text{ m/s}} = 0.03 \text{ s} = 30 \text{ ms}$.
3. **Latency Penalty:** $30 \text{ ms} - 2.5 \text{ ms} = 27.5 \text{ ms}$.
4. *Conclusion:* Bypassing firewalls via super nodes introduces physical routing latency, which is an acceptable trade-off for connectivity in VOIP.

## Previous Year Questions & Solutions

**[December 2019] With the help of the Skype case study, explain how hierarchical peer-to-peer systems operate and solve the problem of NAT traversal. (9 Marks)**
*Solution:*
**Skype** operates as a **Hierarchical (Hybrid) Peer-to-Peer network**, combining the scalability of decentralized nodes with the security of a centralized server.

1. **Architecture Breakdown:**
   - **Weak Peers:** Ordinary users running the Skype application. They usually have limited bandwidth and are placed behind NAT routers or firewalls.
   - **Super Peers (Super Nodes):** Promoted weak peers that have public IP addresses and high bandwidth. They act as directory servers, connection relays, and traffic hubs for the weak peers.
   - **Centralized Login Server:** A single centralized authority used strictly for user authentication, unique ID assignment, and billing.

2. **Bootstrapping (Joining the Network):**
   When a weak peer starts, it attempts to connect to the network using a local **Host Cache**—a saved list of hundreds of known super node IP addresses. If these are offline, it falls back to hard-coded default super nodes embedded in the Skype binary.

3. **Solving the NAT Traversal Problem:**
   Network Address Translation (NAT) firewalls block unsolicited incoming TCP connections, making pure P2P calls impossible for most home users. Skype solves this using the super peers:
   - When Alice (behind a firewall) starts Skype, she immediately establishes an *outgoing* persistent TCP connection to a public Super Node. Firewalls generally allow outgoing connections.
   - When Bob wants to call Alice, he cannot connect to her directly. Instead, Bob routes the voice packets to Alice's Super Node.
   - Because Alice already has an open, persistent outgoing connection to that Super Node, the node simply pushes Bob's data down that open pipe to Alice, effectively bypassing the firewall and achieving seamless NAT traversal.
