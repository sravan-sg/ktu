# Characteristics of Interprocess Communication (IPC)

## Explanation

Interprocess Communication (IPC) refers to the mechanisms and protocols that allow processes executing on different nodes in a distributed system to exchange data and synchronize their actions. In a distributed environment, processes do not share memory, so all communication relies on message passing over a network. 

The core characteristics of IPC in distributed systems include:

1. **Synchronous vs. Asynchronous Communication**:
   - **Synchronous (Blocking)**: Both the sender and receiver block until the message is successfully transmitted and received. The sender waits for an acknowledgment before proceeding.
   - **Asynchronous (Non-blocking)**: The sender transmits the message and immediately resumes execution without waiting for an acknowledgment. The message is buffered by the OS or middleware until the receiver is ready to process it.

2. **Message Destinations**:
   - Messages are sent to explicit destinations, typically identified by an **Internet address (IP)** and a **local port number**. This combination forms a socket, which acts as an endpoint for communication.

3. **Reliability**:
   - IPC can be built on top of reliable protocols (like TCP, which guarantees delivery and ordering) or unreliable protocols (like UDP, which offers best-effort delivery but lower latency).

4. **Message Ordering**:
   - Depending on the application requirements, IPC mechanisms may need to enforce message ordering (e.g., FIFO, causal ordering, or total ordering) to ensure consistent state across replicas.

## Example

Consider a distributed banking application where a **Client Process** wants to transfer funds by sending a request to a **Server Process**. 

- **Asynchronous model**: The client sends the "Transfer $100" message and immediately updates its local UI to show "Processing..." while the message travels.
- **Synchronous model**: The client sends the message and the entire application freezes (blocks) until the server completes the transfer, updates the database, and sends back a "Success" reply.

Visually, using sockets:
```
[Client Process]
       |
  (Socket 192.168.1.5:4000)
       |
   [Network]
       |
  (Socket 10.0.0.8:8080)
       |
[Server Process]
```

## Applications & Use Cases

- **Microservices Architectures**: Services communicating via REST (synchronous HTTP) or Message Queues like RabbitMQ/Kafka (asynchronous IPC) to process user orders.
- **Distributed Databases**: Replicas communicating via asynchronous IPC to gossip about state changes and maintain eventual consistency (e.g., Cassandra).
- **Real-Time Multiplayer Games**: Using fast, unreliable IPC (UDP) to stream player coordinates with minimal latency.

## 3 Solved Numerical/Analytical Examples

**Example 1: Blocking Time Calculation**
A client sends a 10 KB message to a server over a link with a bandwidth of 100 Mbps and a one-way propagation delay of 15 ms. The server processes the request in 5 ms and sends a 2 KB reply. How long does the client block in a synchronous RPC call?
*Solution:*
1. Transmission time for request ($T_{tx1}$) = $10 \text{ KB} / 100 \text{ Mbps} = (10 \times 8 \times 1024 \text{ bits}) / (100 \times 10^6 \text{ bits/s}) = 0.819 \text{ ms}$.
2. Propagation delay to server = $15 \text{ ms}$.
3. Processing time = $5 \text{ ms}$.
4. Transmission time for reply ($T_{tx2}$) = $2 \text{ KB} / 100 \text{ Mbps} = 0.163 \text{ ms}$.
5. Propagation delay back = $15 \text{ ms}$.
Total Blocking Time = $0.819 + 15 + 5 + 0.163 + 15 = 35.982 \text{ ms}$.

**Example 2: Buffer Utilization in Asynchronous IPC**
A sender generates asynchronous messages at a rate of 500 messages/sec. Each message is 1 KB. The network transmission rate is 4 Mbps. How much buffer space is required at the sender if the network link goes down for 5 seconds?
*Solution:*
1. Message generation rate = $500 \text{ msg/s} \times 1 \text{ KB/msg} = 500 \text{ KB/s}$.
2. Total data generated during the 5-second outage = $500 \text{ KB/s} \times 5 \text{ s} = 2500 \text{ KB}$.
3. Required buffer space = $2.5 \text{ MB}$. (Since the network is down, the transmission rate is irrelevant to the buildup).

**Example 3: UDP vs TCP Latency Tradeoff**
Calculate the setup and delivery time for a 1-byte payload using TCP versus UDP, assuming a one-way delay (RTT/2) of 20 ms.
*Solution:*
- **TCP**: Requires a 3-way handshake before sending data.
  1. SYN (Client -> Server): 20 ms
  2. SYN-ACK (Server -> Client): 20 ms
  3. ACK + Data (Client -> Server): 20 ms
  Total time = 60 ms.
- **UDP**: Connectionless; data is sent immediately.
  1. Data (Client -> Server): 20 ms
  Total time = 20 ms.
*Conclusion:* UDP provides significantly lower latency for single small messages.

## Previous Year Questions & Solutions

**[April 2018] PART C - Q14b) What are the characteristics of interprocess communication? (3 marks)**
*Solution:*
The primary characteristics of interprocess communication (IPC) in distributed systems include:
1. **Synchronous vs. Asynchronous:** In synchronous IPC, both sender and receiver block until communication completes (e.g., waiting for an acknowledgment). In asynchronous IPC, the sender transmits the message and immediately continues execution, relying on underlying buffers.
2. **Message Destinations:** Communication is directed to specific endpoints (sockets) defined by an IP address and a local port number, decoupling the process from physical hardware.
3. **Reliability:** IPC can be implemented over reliable protocols (like TCP, guaranteeing delivery and order) or unreliable ones (like UDP, which is faster but may drop messages).
4. **Message Ordering:** IPC mechanisms may provide ordering guarantees (FIFO, causal, total) to ensure messages are processed logically, depending on system requirements.
