# Module 3 Revision Notes: Interprocess Communication

## 1. Core Concepts & Definitions
- **IPC Characteristics**: Communication between processes with no shared memory. Defined by synchronous/asynchronous behavior, explicit destinations (sockets), and ordering guarantees.
- **RPC (Remote Procedure Call)**: Makes network requests look like local function calls using client/server stubs that marshal and unmarshal parameters. 
- **Network Virtualization**: Decoupling logical topology from physical topology (e.g., Overlay networks, VPNs, SDN).

## 2. Key Algorithms & Mechanisms
- **Multicast**: Sending a single packet to an IP group (Class D) instead of broadcasting. Uses IGMP.
- **Group Communication**: Communicating via a logical group ID. Can be Open/Closed and P2P/Hierarchical.
- **Skype Overlay Architecture**: Relies on a two-tier P2P system. "Supernodes" handle routing and Global Index lookups, allowing ordinary nodes to bypass NATs/firewalls via virtual relaying.

## 3. High-Yield PYQ Triggers
- *If a question asks about Multicast vs Broadcast:* Focus on bandwidth efficiency, subnet containment, and target audience (interested subset vs entire network).
- *If a question asks about RPC:* Explain the role of Stubs, transparency, and data marshalling (XDR).
- *If a question asks about Skype:* Describe Network Virtualization, Supernodes vs Ordinary Nodes, and NAT traversal.

## 4. Common Pitfalls & Mistakes to Avoid
- *Mistake:* Stating RPC passes variables by reference. *Correction:* Pointers cannot cross network boundaries; RPC uses call-by-copy/restore.
- *Mistake:* Confusing IP Multicast with Broadcast. *Correction:* Broadcast floods the local LAN (FF:FF:FF:FF:FF:FF); Multicast is routed via IGMP to specific subscribed branches.
- *Mistake:* Assuming Skype routes calls through central servers. *Correction:* Only login is centralized; all call routing is decentralized via Supernodes (Overlay Virtualization).