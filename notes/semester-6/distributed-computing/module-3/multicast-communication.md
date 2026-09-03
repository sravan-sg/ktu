# Multicast Communication

## Explanation

Multicast communication is an Interprocess Communication (IPC) paradigm where a single message is sent from one source to a specific subset of nodes in a network, rather than to just one node (Unicast) or to all nodes (Broadcast).

Multicasting can be implemented at various layers:
- **Hardware/Data Link Layer**: Using MAC-level multicast (e.g., Ethernet multicast addresses).
- **Network Layer (IP Multicast)**: The sender transmits a single IP packet to a special Class D IP address (224.0.0.0 to 239.255.255.255). The network routers (using protocols like IGMP) duplicate the packet only at the branches where subscribed receivers exist. This is highly bandwidth-efficient.
- **Application Layer (Overlay Multicast)**: When IP multicast is not supported across WAN routers, the application nodes form a logical tree (overlay network) and forward unicast TCP/UDP packets to each other to simulate multicasting.

**Reliability in Multicasting**:
Basic IP Multicast (which uses UDP) is unreliable. Packets can be lost, duplicated, or delivered out of order. Distributed systems usually require **Reliable Multicast**, which ensures that if a message is delivered to one correct process, it is delivered to all correct processes. An even stronger guarantee is **Atomic Multicast**, which ensures reliable delivery *and* that all messages are delivered in the exact same total order across all receivers.

## Example

Consider a live video streaming service (like IPTV) broadcasting a sports match to 1,000 subscribers on a local ISP network.

- **Unicast approach**: The server sends 1,000 separate video streams. If the stream is 5 Mbps, the server needs 5 Gbps of uplink bandwidth.
- **Multicast approach**: The server sends exactly **one** 5 Mbps stream to the multicast group address `239.2.2.2`. 
The core router receives this and duplicates it only to the specific subnet links where users have joined the group via IGMP.

```text
               [Streaming Server] (Sends 1 stream)
                      |
                 [Core Router]
                /             \
    [Subnet Router 1]     [Subnet Router 2]
    (Copies stream)       (No subscribers - drops stream)
      /         \
  [User A]    [User B]
```

## Applications & Use Cases

- **Financial Trading Systems**: Stock tickers multicast price updates to hundreds of trading algorithms simultaneously, ensuring fairness and low latency.
- **Live Multimedia Streaming**: IPTV and enterprise video conferencing use IP multicast to save bandwidth.
- **Service Discovery**: Devices use multicast (e.g., mDNS/Apple Bonjour, UPnP) to find local network services like printers or smart speakers without a central DNS server.

## 3 Solved Numerical/Analytical Examples

**Example 1: Bandwidth Savings with Multicast**
A server needs to send a 500 MB software update to 200 machines on a LAN. The network backbone operates at 1 Gbps. How much data crosses the server's network interface using Unicast vs. IP Multicast?
*Solution:*
- **Unicast**: Server establishes 200 TCP connections and sends the file 200 times. Total data = $200 \times 500 \text{ MB} = 100,000 \text{ MB} = 100 \text{ GB}$.
- **Multicast**: Server sends the file to a multicast address exactly once. Total data = $500 \text{ MB}$. (The network switches handle the replication).
*Conclusion:* Multicast saves 99.5% of the server's bandwidth.

**Example 2: Multicast MAC Address Mapping**
Calculate the Ethernet Multicast MAC address for the IP Multicast address `224.128.5.6`.
*Solution:*
1. The standard OUI for IPv4 multicast MAC is `01:00:5E`.
2. The 23rd bit of the MAC must be `0`.
3. The lower 23 bits of the IP address are mapped directly.
   IP: `224.128.5.6` -> Binary: `11100000 . 10000000 . 00000101 . 00000110`
   Lower 23 bits: `0000000 . 00000101 . 00000110` (Hex: `00:05:06`).
4. Resulting MAC: `01:00:5E:00:05:06`.

**Example 3: Overlay Multicast Latency Penalty**
Nodes A, B, C, D form a logical line topology for Application-Layer Multicast: A -> B -> C -> D. The physical latency between any two nodes is 10 ms. How long does it take for a message from A to reach D, compared to a direct Unicast from A to D?
*Solution:*
- **Unicast A -> D**: Message traverses the physical network directly. Delay = 10 ms.
- **Overlay Multicast**: The message is sent A->B (10 ms), processed by B's application layer (assume 2 ms), sent B->C (10 ms), processed by C (2 ms), sent C->D (10 ms).
  Total Delay = $10 + 2 + 10 + 2 + 10 = 34 \text{ ms}$.
*Conclusion:* Overlay multicast trades off increased latency for deployment feasibility where routers don't support IP Multicast.

## Previous Year Questions & Solutions

**[April 2018] PART A - Q5) How is a multicast communication different from a broadcast? (4 marks)**
*Solution:*
1. **Target Audience**: 
   - **Broadcast** sends a message to *all* nodes on the network subnet unconditionally (e.g., address `255.255.255.255` or MAC `FF:FF:FF:FF:FF:FF`). Every NIC must interrupt the CPU to process the packet.
   - **Multicast** sends a message only to a *specific subset* of interested nodes that have actively joined a multicast group. Nodes not in the group safely ignore the packets at the hardware/network layer.
2. **Network Scope**: 
   - **Broadcasts** are strictly contained within a single local area network (LAN) domain; routers drop broadcast packets to prevent internet-wide broadcast storms. 
   - **Multicast** can span across subnets and WANs because multicast-aware routers use protocols like IGMP and PIM to route the traffic to branches with subscribers.
3. **Bandwidth Efficiency**: Both save sender bandwidth compared to unicast, but multicast also saves receiver processing power and network branch bandwidth since packets are only routed where needed.
