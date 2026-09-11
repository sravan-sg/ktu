# Characteristics of Interprocess Communication (IPC)

## Explanation

Interprocess Communication (IPC) is at the heart of all distributed systems. Because distributed processes do not share memory, they must exchange information via message passing over a network. According to **Tanenbaum**, the characteristics of IPC can be rigorously classified across two independent dimensions: **Persistence** and **Synchronization**.

1. **Persistence vs. Transient Communication**
   - **Persistent Communication**: A message submitted for transmission is stored by the communication middleware as long as it takes to deliver it to the receiver. Neither the sender nor the receiver needs to be executing simultaneously. The middleware acts as a reliable buffer (e.g., an email system or message queuing system).
   - **Transient Communication**: A message is stored only as long as both the sending and receiving applications are executing. If the receiver is down or the network drops the packet, the message is discarded. All standard transport-level services (like TCP/UDP sockets) offer only transient communication.

2. **Synchronous vs. Asynchronous Communication**
   - **Synchronous Communication (Blocking)**: The sender blocks (halts execution) after submitting a message. Tanenbaum defines three points of synchronization:
     - Blocking until the middleware receives the message.
     - Blocking until the message is delivered to the receiver.
     - Blocking until the receiver processes the message and returns a response (e.g., standard RPC).
   - **Asynchronous Communication (Non-blocking)**: The sender submits the message and immediately resumes execution. The middleware temporarily buffers the message and takes responsibility for transmitting it in the background.

3. **Connection-Oriented vs. Connectionless (OSI Reference Model)**
   - **Connection-oriented**: A connection must be explicitly established and negotiated before data is sent, and released afterward (e.g., TCP).
   - **Connectionless**: No prior setup is needed; messages are simply dispatched when ready (e.g., UDP).

## Example

Consider a distributed banking system that uses different IPC combinations based on the task:
- **Transient + Synchronous (RPC)**: A client checking its account balance. The client sends a request to the server and blocks until the server replies with the balance. Both must be online simultaneously.
- **Persistent + Asynchronous (Message Queue)**: The banking system processing daily batch transactions. A batch server submits thousands of transaction messages into a Message-Oriented Middleware (MOM). The sender immediately resumes execution. The database server can process these messages at its own pace, even if it goes offline temporarily.

## Applications & Use Cases

- **Remote Procedure Calls (RPC)**: Widely used for client-server architectures requiring immediate responses, employing **Transient + Synchronous** characteristics.
- **Message-Oriented Middleware (MOM)**: Systems like RabbitMQ or IBM WebSphere MQ use **Persistent + Asynchronous** communication to decouple microservices and ensure fault tolerance.
- **MPI (Message Passing Interface)**: Used in high-performance computing clusters, relying on fast, **Transient** communication where failures are considered fatal rather than recoverable.

## 3 Solved Numerical/Analytical Examples

**Example 1: Blocking Time in Synchronous Communication**
*Problem:* A sender uses synchronous transient communication. It takes 10 ms for a request to reach the server, 5 ms for the server to process it, and 10 ms for the reply to return. If the sender issues 50 requests sequentially, what is the total blocking time?
*Solution:*
1. Time per request = $10 \text{ ms} + 5 \text{ ms} + 10 \text{ ms} = 25 \text{ ms}$.
2. Total blocking time = $50 \times 25 \text{ ms} = 1250 \text{ ms} = 1.25 \text{ seconds}$.
*Conclusion:* Synchronous communication can introduce severe latency bottlenecks in wide-area networks.

**Example 2: Buffer Requirements in Asynchronous Persistent IPC**
*Problem:* A sender generates asynchronous persistent messages at 100 messages/second (each 2 KB). The receiver processes them at 80 messages/second. How much middleware buffer space is required to store the backlog if the system runs for 1 minute?
*Solution:*
1. Generation rate = $100 \times 2 \text{ KB} = 200 \text{ KB/s}$.
2. Processing rate = $80 \times 2 \text{ KB} = 160 \text{ KB/s}$.
3. Backlog accumulation rate = $200 - 160 = 40 \text{ KB/s}$.
4. Buffer needed for 60 seconds = $40 \text{ KB/s} \times 60 \text{ s} = 2400 \text{ KB} = 2.4 \text{ MB}$.
*Conclusion:* Persistent asynchronous systems must dimension their storage carefully to handle processing imbalances.

**Example 3: Connectionless Latency Advantage**
*Problem:* Compare the setup and delivery time for a 1 KB payload over a link with a 20 ms one-way propagation delay using Connection-oriented TCP vs. Connectionless UDP.
*Solution:*
- **TCP (Connection-oriented):**
  1. SYN (Sender -> Receiver): 20 ms
  2. SYN-ACK (Receiver -> Sender): 20 ms
  3. ACK + Data (Sender -> Receiver): 20 ms
  Total = 60 ms.
- **UDP (Connectionless):**
  1. Data (Sender -> Receiver): 20 ms
  Total = 20 ms.
*Conclusion:* Connectionless communication avoids the 3-way handshake overhead, making it ideal for fast, transient message passing.

## Previous Year Questions & Solutions

**[April 2018] PART C - Q14b) What are the characteristics of interprocess communication? (3 marks)**
*Solution:*
Based on the foundational principles of distributed systems, Interprocess Communication (IPC) is characterized by:
1. **Persistence vs. Transience:** 
   - *Persistent:* The communication middleware stores the message until it can be delivered, allowing sender and receiver to be offline at different times.
   - *Transient:* The message is discarded if it cannot be delivered immediately (e.g., if the receiver is down or a network link fails).
2. **Synchronization (Synchronous vs. Asynchronous):**
   - *Synchronous (Blocking):* The sender halts execution after sending the message until it reaches the middleware, the receiver, or a full reply is processed.
   - *Asynchronous (Non-blocking):* The sender submits the message and immediately resumes execution, allowing for higher concurrency.
3. **Connection Model:** IPC can be *Connection-oriented* (requiring explicit setup and teardown before data exchange, like TCP) or *Connectionless* (messages are sent without prior negotiation, like UDP).
