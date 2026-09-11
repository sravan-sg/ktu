# Network Virtualization

## Explanation

In the context of distributed systems, **Virtualization** is the process of extending or replacing an existing interface to mimic the behavior of another system, effectively decoupling the logical system from the underlying physical hardware. While **Tanenbaum (Chapter 3.2)** heavily discusses resource virtualization (like Virtual Machines and Cloud IaaS), **Network Virtualization** applies this same decoupling principle to communication links.

Network virtualization creates a **logical (virtual) network** built on top of a physical underlying network (like the Internet). In distributed systems literature, this is most commonly realized as an **Overlay Network**. 

Key principles derived from Tanenbaum's virtualization and overlay concepts:
1. **Decoupling Topology**: An overlay network consists of application-layer processes acting as nodes. The "links" between them are virtual (TCP/UDP connections), decoupling the logical topology required by the distributed application from the physical routing topology of the underlying network hardware.
2. **Custom Application-Level Routing**: Because the network is virtualized, nodes can implement custom routing algorithms (e.g., routing based on a DHT content ID rather than an IP address) without altering the underlying physical routers.
3. **Encapsulation (Tunneling)**: Data generated in the virtual network is encapsulated inside standard transport-layer packets and routed transparently through the physical Internet.

## Example

Consider a Peer-to-Peer (P2P) file-sharing network:
- **Physical Network**: A massive, rigid graph of ISP routers, trans-oceanic cables, and local Wi-Fi routers operating via BGP and IP routing.
- **Virtual (Overlay) Network**: A flexible logical graph where Node A (in New York) maintains a direct "virtual link" (a persistent TCP socket) to Node B (in Tokyo). 

```text
[Virtual Network View - The Overlay]
Node A --------------------------- Node B
(Logical Link: 1 Hop, 0 intervening routers visible)

[Physical Network Reality]
Node A -> Router1 -> ISP -> OceanCable -> RouterX -> Node B
(Physical Links: 15 Hops)
```
To the application running on Node A, Node B is exactly one hop away on the virtual network.

## Applications & Use Cases

- **Virtual Private Networks (VPNs)**: Creating a secure, private logical network overlay on top of the public Internet using tunneling protocols. The virtual network isolates corporate traffic from public nodes.
- **Cloud Computing (IaaS)**: As Tanenbaum notes, Amazon EC2 allows customers to create networked virtual servers that communicate over a virtualized IP network, completely isolated from other tenants sharing the same physical blades.
- **Peer-to-Peer Overlays**: Systems like Skype (case study) or BitTorrent build application-layer overlay networks to route traffic custom to their needs (e.g., firewall traversal) rather than relying on standard IP routing.

## 3 Solved Numerical/Analytical Examples

**Example 1: Overlay Routing Stretch Calculation**
*Problem:* "Stretch" in an overlay network is defined as the ratio of the latency in the virtual network to the shortest physical latency between two nodes. Node A sends a message to Node C in an overlay network, but the virtual topology forces it to route through Node B. Physical Latencies: A to B = 20 ms. B to C = 15 ms. A to C directly = 25 ms. Calculate the stretch.
*Solution:*
1. Virtual Overlay Latency (A -> B -> C) = $20 \text{ ms} + 15 \text{ ms} = 35 \text{ ms}$.
2. Shortest Physical Latency (A -> C) = $25 \text{ ms}$.
3. Stretch = Overlay Latency / Physical Latency = $35 / 25 = 1.4$.
*Conclusion:* The network virtualization introduces a 40% latency penalty due to sub-optimal virtual routing.

**Example 2: Virtual Link Capacity vs Physical Bottleneck**
*Problem:* A virtual network defines a link from Node A to Node C with a required bandwidth of 50 Mbps. The encapsulated packets traverse a physical path through three links: L1 (100 Mbps), L2 (40 Mbps), L3 (1 Gbps). Can the virtual link be established at full capacity?
*Solution:*
1. The capacity of a virtual link is strictly bottlenecked by the physical link with the lowest bandwidth along its path.
2. Bottleneck = min(100, 40, 1000) = 40 Mbps.
3. Since the required capacity (50 Mbps) > bottleneck (40 Mbps), the virtual link will suffer congestion and cannot sustain the required bandwidth.

**Example 3: Scalability of Full-Mesh Virtual Topologies**
*Problem:* If a virtual overlay network of 1,000 nodes attempts to maintain a full-mesh topology (every node maintains a virtual link/TCP socket with every other node), how many total TCP connections must the virtual network maintain?
*Solution:*
1. Connections per node = $N - 1 = 1,000 - 1 = 999$ sockets.
2. Total connections in the network = $N(N-1)/2 = (1,000 \times 999) / 2 = 499,500$ TCP connections.
*Conclusion:* Full-mesh virtual networks do not scale due to state explosion. This is why virtual network systems use structured topologies (like DHTs or trees) or supernodes (like Skype).

## Previous Year Questions & Solutions

**[April 2018] PART C - Q15a) Discuss Skype as a case study for network virtualization. (5 marks)**
*Solution:*
Skype acts as a prime example of network virtualization by building a massive Peer-to-Peer **overlay network** on top of the physical Internet. 
1. **Virtual Topology:** Instead of relying purely on physical IP routing, Skype organizes nodes into a two-tier virtual topology consisting of "Supernodes" (high-bandwidth, public machines) and "Ordinary nodes" (endpoints behind NAT/firewalls).
2. **Decoupled Routing:** Skype virtualizes addressing. It does not rely on IP routing to find a user; it uses its overlay network's Global Index (hosted on Supernodes) to map a Skype Username to a current, potentially shifting IP address.
3. **NAT Traversal:** If two ordinary nodes cannot communicate directly due to physical firewall restrictions, the virtual network routes their call data through a mutually accessible Supernode. To the endpoints, they are communicating over a direct virtual link, completely hiding the physical network's limitations.
