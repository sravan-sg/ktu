# Module 1 — Topic 2: Protocol Hierarchies, Layer Design Issues & Services

> **Module 1**: Network Architecture & Reference Models  
> **Course**: CS306 Computer Networks

---

## 1. Core Intuition & Fundamental Concepts

### Explanation
To manage the immense complexity of network communications, networks are structured as a stack of **layers** or **levels**, each built upon the one below it. 

Key Terminology:
- **Protocol**: An agreed-upon set of rules and conventions governing communication between two **peer entities** operating at the same layer on different machines.
- **Service**: A set of operations/primitives that a lower layer offers to the layer immediately above it (across an Interface).
- **Interface**: Defines the primitive operations and boundary rules through which Layer $N$ exposes its services to Layer $N+1$.
- **Encapsulation**: As data moves down the protocol stack from Layer $N+1$ to Layer $N$, Layer $N$ prepends a **Header** ($H_N$) containing control info (addresses, checksums, sequence numbers). At the receiving host, **Decapsulation** strips headers as data ascends.

---

### Key Design Issues for Layers

Every layer in a network architecture must address several core engineering design issues:

1. **Addressing & Naming**:
   - Disambiguating senders and receivers at different levels of granularity.
   - Examples: MAC addresses (Layer 2 physical link), IP addresses (Layer 3 network host), Port numbers (Layer 4 application process).

2. **Error Control**:
   - Physical circuits are imperfect and flip bits due to noise, attenuation, or interference.
   - Requires mechanisms for **Error Detection** (Checksums, CRC) and **Error Correction / Retransmission** (ARQ protocols).

3. **Flow Control**:
   - Prevents a fast, high-capacity sender from overflowing the limited buffer space of a slow receiver.
   - Implemented using Feedback mechanisms (Stop-and-Wait, Sliding Window).

4. **Multiplexing & Demultiplexing**:
   - **Multiplexing**: Combining multiple higher-layer application data streams over a single shared lower-layer physical transmission channel.
   - **Demultiplexing**: Separating combined traffic streams at the destination based on protocol port tags.

5. **Routing & Scalability**:
   - Finding optimal, shortest, or least-cost paths when multiple intermediate physical paths exist between source and destination routers.

6. **Fragmentation & Reassembly**:
   - Dividing large packets into smaller fragments when traversing networks with smaller Maximum Transmission Units (MTUs), and reassembling them correctly at the destination.

---

### Service Primitives & Service Types

A service is formally specified by a set of **Primitives** (basic operations/calls) available to user processes or higher layers:

```
    Client (Layer N+1)                             Server (Layer N+1)
            │                                              ▲
  1. REQUEST│                                              │2. INDICATION
            ▼                                              │
  ┌────────────────────────────────────────────────────────────────┐
  │                           LAYER N                              │
  └────────────────────────────────────────────────────────────────┘
            ▲                                              │
   4.CONFIRM│                                              │3. RESPONSE
            │                                              ▼
```

#### The 4 Abstract Service Primitives:
1. **REQUEST**: An entity at Layer $N+1$ asks Layer $N$ to perform a service (e.g. establish a connection, send data).
2. **INDICATION**: An entity at Layer $N$ notifies an entity at Layer $N+1$ that a service request or event has occurred.
3. **RESPONSE**: An entity at Layer $N+1$ responds to an `INDICATION` primitive.
4. **CONFIRM**: An entity at Layer $N$ notifies the requesting entity at Layer $N+1$ that its prior `REQUEST` has completed.

#### Service Classification:
- **Confirmed Services**: Uses all 4 primitives (`REQUEST`, `INDICATION`, `RESPONSE`, `CONFIRM`). Used in connection setup (e.g., TCP connection establishment).
- **Unconfirmed Services**: Uses only 2 primitives (`REQUEST`, `INDICATION`). No confirmation is returned to the sender (e.g., UDP datagram delivery).

---

### Real-World Example
Think of international diplomacy:
- **Presidents (Layer 3 Peers)**: Communicate logically ("Let me sign a treaty").
- **Translators (Layer 2)**: Translate message, append formal headers ("To Foreign Minister"), pass to courier.
- **Couriers (Layer 1)**: Put letter in stamped envelope, transport via airplane.
- The Presidents communicate logically via their protocol, but physical communication flows vertically down through translators and couriers using primitive interfaces.

### Applications & Use Cases
- **HTTP over TLS over TCP over IP over Ethernet**: Web browsers encapsulate HTTP requests inside TLS encryption headers, TCP segment headers, IP packet headers, and Ethernet frame headers.
- **Modular Network Protocol Replacement**: Protocol layering allows swapping out physical media (Wi-Fi vs Fiber Ethernet) without rewriting upper-layer application software (Web Browser or Database engine).

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
1. **Connection-Oriented Service (Confirmed Service):**
   - Requires 3 distinct phases: (1) Connection Establishment, (2) Data Transfer, (3) Connection Release.
   - **Primitive Sequence:**
     - Client issues `CONNECT.request` $\rightarrow$ Server receives `CONNECT.indication`.
     - Server issues `CONNECT.response` $\rightarrow$ Client receives `CONNECT.confirm`.
     - Client issues `DATA.request` $\rightarrow$ Server receives `DATA.indication`.
     - Client/Server issues `DISCONNECT.request`.
2. **Connectionless Service (Unconfirmed Service):**
   - Each message (Datagram) carries a complete destination address and is routed independently. No setup phase required.
   - Primitive Sequence: Client issues `UNITDATA.request` $\rightarrow$ Server receives `UNITDATA.indication`.

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
     - *Addressing*: Disambiguating senders/receivers (MAC, IP, Port numbers).
     - *Error Control*: Detecting/correcting corrupted bits using checksums & ARQ.
     - *Flow Control*: Matching rates between fast senders and slow receivers.
     - *Multiplexing*: Combining multiple upper streams over 1 lower link.
     - *Routing*: Determining optimal paths through subnets.

2. **"Explain the 4 service primitives (Request, Indication, Response, Confirm) and differentiate between Confirmed and Unconfirmed services." [April 2018, July 2021]**
   - **Solution:**
     - **Request**: Layer $N+1$ requests a service from Layer $N$.
     - **Indication**: Layer $N$ notifies Layer $N+1$ of an incoming request or event.
     - **Response**: Layer $N+1$ responds to an indication.
     - **Confirm**: Layer $N$ notifies requesting Layer $N+1$ that service is completed.
     **Confirmed vs Unconfirmed:**
     - *Confirmed Services* use all 4 primitives (`Request`, `Indication`, `Response`, `Confirm`) to guarantee acknowledgment (e.g. TCP setup).
     - *Unconfirmed Services* use only 2 primitives (`Request`, `Indication`) without returning confirmation (e.g. UDP datagram transmission).
