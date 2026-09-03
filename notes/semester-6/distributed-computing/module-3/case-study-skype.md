# Case Study: Skype

## Explanation

Skype (in its original architecture before being acquired and centralized by Microsoft) is the classic textbook case study for a massive-scale Peer-to-Peer (P2P) overlay network and network virtualization. It demonstrated how to provide high-quality Voice over IP (VoIP) without maintaining thousands of expensive central servers to route audio traffic.

### Architecture
Skype's overlay network is built on a two-tier hierarchy:
1. **Ordinary Nodes**: Standard user client applications. These are often behind strict Firewalls or Network Address Translators (NATs) and cannot accept incoming connections directly.
2. **Supernodes**: Ordinary nodes with high bandwidth, high uptime, and no firewalls (public IP addresses) are automatically promoted by the Skype software to act as Supernodes. 

### How it Works (Network Virtualization)
1. **Login and Global Index**: A central login server (the only truly centralized piece) authenticates users. Supernodes maintain a decentralized Global Index (a Distributed Hash Table) mapping Skype Usernames to current IP addresses.
2. **Call Setup**: When User A calls User B, Node A queries its connected Supernode to find B's IP address.
3. **NAT Traversal (Relaying)**: If both users are behind strict NATs (they cannot ping each other), the physical internet blocks their connection. Skype uses a Supernode as a virtual bridge. User A sends voice packets to the Supernode, and the Supernode relays them to User B. The overlay network effectively *virtualizes* a direct connection between A and B, hiding the physical firewall constraints.

## Example

Consider a call between Alice (in an office behind a strict firewall) and Bob (at a coffee shop behind a NAT). 
They cannot establish a TCP/UDP socket directly.

```text
[Alice's PC] --(Blocked by NAT A)--X   X--(Blocked by NAT B)-- [Bob's PC]

       \                                                   /
        \                                                 /
         \-> (Outbound OK)     [Supernode]  <-(Outbound OK)
             (Public IP, No Firewall)
```
In the physical network, packets go Alice -> NAT -> ISP -> Supernode -> ISP -> NAT -> Bob.
In the Skype Virtual Overlay, Alice and Bob appear to have a direct, uninterrupted logical pipe.

## Applications & Use Cases

- **VoIP and Video Conferencing**: Ensuring calls connect regardless of the users' local network configurations (NATs).
- **Decentralized Resource Sharing**: Using the idle bandwidth of standard users (Supernodes) to route traffic, drastically reducing the infrastructure costs for the software provider.
- **Censorship Circumvention**: Overlay routing can obscure traffic patterns, making it harder for firewalls to block VoIP traffic compared to centralized SIP servers.

## 3 Solved Numerical/Analytical Examples

**Example 1: Bandwidth Cost Saving for Skype**
Suppose Skype has 10 million concurrent calls, each requiring 50 kbps (kilobits per second) of bandwidth in both directions. If Skype routed all calls through central servers, what would be the required bandwidth capacity?
*Solution:*
1. Bandwidth per call on the server = $50 \text{ kbps (in)} + 50 \text{ kbps (out)} = 100 \text{ kbps}$.
2. Total bandwidth = $10,000,000 \times 100 \text{ kbps} = 1,000,000,000 \text{ kbps} = 1 \text{ Tbps}$ (Terabit per second).
*Conclusion:* By virtualizing the network and using P2P Supernodes to route the traffic, Skype offloads this massive 1 Tbps cost entirely to the users' ISPs.

**Example 2: Supernode Promotion Criteria**
A node is considered for Supernode promotion if its uptime > 24 hours, its upload bandwidth > 2 Mbps, and it has a public IP. Out of 100,000 nodes, 60% are behind NATs. Of the public IP nodes, 40% have uptime > 24hrs. Of those, 30% have > 2 Mbps upload. How many Supernodes are elected?
*Solution:*
1. Public IP nodes = $100,000 \times 0.40 = 40,000$.
2. Uptime criteria met = $40,000 \times 0.40 = 16,000$.
3. Bandwidth criteria met = $16,000 \times 0.30 = 4,800$.
*Result:* 4,800 nodes become Supernodes.

**Example 3: Relayed Call Latency**
Alice calls Bob. A direct physical path (if it existed) has a ping of 40 ms. Because of NAT, they must relay through a Supernode. Alice to Supernode is 30 ms. Supernode to Bob is 60 ms. What is the virtualization latency penalty?
*Solution:*
1. Virtual/Relayed Latency = $30 \text{ ms} + 60 \text{ ms} = 90 \text{ ms}$.
2. Direct Latency = 40 ms.
3. Penalty = $90 \text{ ms} - 40 \text{ ms} = 50 \text{ ms}$.
*Note:* A penalty of 50 ms is acceptable for VoIP (human ear detects delay > 150 ms), making the overlay architecture highly viable.

## Previous Year Questions & Solutions

**[April 2018] PART C - Q15a) Discuss Skype as a case study for network virtualization. (5 marks)**
*Solution:*
Skype serves as a classic case study for network virtualization by implementing a two-tiered Peer-to-Peer (P2P) overlay network on top of the physical Internet infrastructure.
1. **The Virtual Overlay:** Skype decouples its communication topology from physical IP routing. Instead of relying on centralized servers to route calls, it organizes end-user computers into an overlay network consisting of "Ordinary nodes" and "Supernodes". Supernodes are regular user machines with high bandwidth and public IP addresses that Skype conscripts to act as decentralized traffic routers.
2. **Virtualizing Connectivity (NAT Traversal):** The primary achievement of Skype's virtualization is hiding physical network barriers. Many ordinary nodes are located behind Network Address Translators (NATs) or firewalls, meaning they cannot receive direct incoming connections. Skype's overlay solves this by routing the call data through a mutually accessible Supernode. 
3. **Outcome:** To the Skype client application, it appears there is a direct, seamless virtual link to the other caller, entirely abstracting away the complex physical reality of firewalls, NATs, and fragmented ISP subnets.
