# Module 1 — Topic 2: Protocol Hierarchies, Layer Design Issues & Services

> **Module 1**: Network Architecture & Reference Models  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
To reduce design complexity, modern networks are organized as a stack of **layers** or **levels**, each built upon the one below it. 

Key terminology:
- **Protocol**: An agreed-upon set of rules and conventions governing communication between two **peer entities** at the same layer across different machines.
- **Service**: A set of operations/primitives that a lower layer offers to the layer immediately above it (across an Interface).
- **Interface**: Defines the primitive operations and services that the lower layer makes available to the upper layer.
- **Encapsulation**: As data moves down the protocol stack from layer $N+1$ to layer $N$, layer $N$ prepends a **Header** ($H_N$) containing control information (addressing, checksums, sequence numbers). At the receiving host, **Decapsulation** strips headers as data moves up.

**Key Layer Design Issues**:
1. **Addressing**: Identifying senders and receivers (e.g. MAC address at Layer 2, IP address at Layer 3, Port number at Layer 4).
2. **Error Control**: Detecting and correcting corrupted or lost bits/packets (checksums, CRC, ARQ).
3. **Flow Control**: Preventing a fast sender from overwhelming a slow receiver.
4. **Multiplexing / Demultiplexing**: Combining multiple higher-layer streams over a single lower-layer channel.
5. **Routing**: Finding optimal paths through a network of intermediate routers.

### Example
Think of international diplomacy:
- The **President of Country A** wants to send a message to the **President of Country B**.
- Layer 3 (Presidents): High-level message ("Let's sign a treaty").
- Layer 2 (Translators/Secretaries): Translates message into official diplomatic language, adds header ("To Minister of Foreign Affairs, Country B"), passes to courier.
- Layer 1 (Couriers/Postal Service): Encloses letter in envelope, stamps tracking ID, ships via airplane.
- The Presidents (Peers) communicate logically via their protocols, but physical communication flows vertically down through translators and couriers.

### Applications & Use Cases
- **HTTP over TLS over TCP over IP over Ethernet**: Web browsers encapsulate HTTP requests inside TLS encryption headers, TCP segment headers, IP packet headers, and Ethernet frame headers.
- **Modular Software Development**: Protocol layering allows swapping out physical media (Wi-Fi vs Fiber Ethernet) without rewriting the application code (Web Browser or Database engine).

---

## 2. 3 Solved Numerical/Analytical Examples

### Example 1: Header Overhead & Bandwidth Efficiency Calculation
**Problem:** An application sends a 1,000-Byte message down a 5-layer protocol stack. Each layer adds a 20-Byte header. Calculate the overall protocol overhead percentage and data transfer efficiency.
**Step-by-step Solution:**
1. **Calculate Total Header Size:**
   $$\text{Total Header Overhead} = 5 \text{ layers} \times 20 \text{ Bytes/header} = 100 \text{ Bytes}$$
2. **Calculate Total Frame Size:**
   $$\text{Total Frame Size} = \text{Payload} + \text{Headers} = 1,000 \text{ Bytes} + 100 \text{ Bytes} = 1,100 \text{ Bytes}$$
3. **Calculate Protocol Overhead Percentage:**
   $$\text{Overhead \%} = \frac{\text{Headers}}{\text{Total Frame Size}} \times 100 = \frac{100}{1100} \times 100 = 9.09\%$$
4. **Calculate Transmission Efficiency:**
   $$\text{Efficiency } \eta = \frac{\text{Payload}}{\text{Total Frame Size}} \times 100 = \frac{1000}{1100} \times 100 = 90.91\%$$

### Example 2: Connection-Oriented vs Connectionless Service Primitives
**Problem:** Contrast Connection-Oriented Service with Connectionless Service using Service Primitives. Trace the primitive sequence for establishing, transferring, and releasing a connection.
**Step-by-step Solution:**
1. **Connection-Oriented Service (e.g. TCP):**
   - Modeled after the telephone system.
   - Requires 3 distinct phases: (1) Connection Establishment, (2) Data Transfer, (3) Connection Release.
   - **Primitive Sequence:**
     - Client issues `LISTEN` / `CONNECT.request` $\rightarrow$ Server receives `CONNECT.indication`.
     - Server issues `CONNECT.response` $\rightarrow$ Client receives `CONNECT.confirm`.
     - Client issues `DATA.request` $\rightarrow$ Server receives `DATA.indication`.
     - Client/Server issues `DISCONNECT.request`.
2. **Connectionless Service (e.g. UDP / IP):**
   - Modeled after the postal system.
   - Each message (Datagram) carries complete destination address and is routed independently. No setup phase required.

### Example 3: Service Primitives Delay Walkthrough
**Problem:** In a client-server setup using service primitives, a client issues a `CONNECT.request` at time $t = 0$. One-way propagation delay between client and server is $10 \text{ ms}$, and processing time at the server is $2 \text{ ms}$. At what time does the client receive `CONNECT.confirm`?
**Step-by-step Solution:**
1. **Phase 1: Request Transmission & Propagation:**
   - Client sends `CONNECT.request` at $t = 0 \text{ ms}$.
   - Reaches Server as `CONNECT.indication` at $t = 0 + 10 = 10 \text{ ms}$.
2. **Phase 2: Server Processing:**
   - Server processes request from $t = 10 \text{ ms}$ to $t = 10 + 2 = 12 \text{ ms}$.
3. **Phase 3: Response Transmission & Propagation:**
   - Server issues `CONNECT.response` at $t = 12 \text{ ms}$.
   - Reaches Client as `CONNECT.confirm` at $t = 12 + 10 = 22 \text{ ms}$.
4. **Total Time:** The client receives `CONNECT.confirm` at **$t = 22 \text{ ms}$** (equal to $2 \times \text{Propagation Delay} + \text{Processing Time}$).

---

## 3. Previous Year Questions & Solutions

1. **"Explain protocol hierarchy and protocol design issues." [Dec 2019]**
   - **Solution:**
     **Protocol Hierarchy:** Networks are layered to break complex communications into modular subtasks. Each layer $N$ provides services to layer $N+1$ using primitives, shielding upper layers from physical implementation details. Peer entities at layer $N$ exchange protocol data units (PDUs) adhering to layer $N$ protocols.
     **Key Design Issues:**
     - **Addressing:** Disambiguating multiple hosts and processes.
     - **Error Control:** Detecting and recovering from flipped bits using checksums and ACKs.
     - **Flow Control:** Matching transmission rates between fast senders and slow receivers.
     - **Routing:** Finding shortest paths through intermediate networks.

2. **"Differentiate between Connection-Oriented and Connectionless services with examples." [April 2018]**
   - **Solution:**
     - **Connection-Oriented Service:** Establishes a virtual circuit before transmitting data. Guarantees in-order delivery and reliability (e.g. TCP, File Transfer, Web Browsing).
     - **Connectionless Service:** Transmits independent datagrams directly without prior negotiation. Faster, lower overhead, but offers no guarantee of in-order delivery or arrival (e.g. UDP, DNS queries, Video Streaming).
