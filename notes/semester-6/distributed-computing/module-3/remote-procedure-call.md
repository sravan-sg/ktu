# Remote Procedure Call (RPC)

## Explanation

Remote Procedure Call (RPC) is a distributed computing paradigm that allows a program to execute a subroutine on a remote node as if it were a local subroutine call. According to **Tanenbaum (Chapter 4.2)**, the ultimate goal of RPC is **access transparency**—hiding the intricacies of message passing and network boundaries from the developer.

### The RPC Architecture (Stubs and Marshaling)
RPC relies on generated **stubs** to mask network interactions:
1. **Client**: The application calls a local dummy function called the **Client Stub**.
2. **Client Stub**: Packs the parameters into a neutral, machine-independent format—a process called **Marshaling**—and asks the OS to send the message.
3. **Network OS**: Transmits the message over the network.
4. **Server OS**: Receives the message and passes it to the **Server Stub**.
5. **Server Stub**: **Unmarshals** the parameters and calls the actual server implementation.
6. **Return**: The server implementation executes, returns the result to the server stub, which marshals it and sends it back to the client stub.

### Parameter Passing and Data Representation
A major challenge identified by Tanenbaum is parameter passing. Since processes do not share memory:
- **Pass-by-Value**: Easy. The data is copied, marshaled, and sent.
- **Pass-by-Reference**: Complex. Pointers cannot simply be sent over the network. Solutions include **Copy/Restore** (copying the array to the server, and copying the modified array back to the client) or using **Distributed Object References** (where a remote reference acts as a proxy).
Additionally, machines may use different data representations (e.g., Big-Endian vs. Little-Endian). RPC frameworks solve this by marshaling data into a neutral wire format before transmission.

### Variations of RPC (Tanenbaum's Classifications)
Standard RPC is inherently **synchronous** (the client blocks waiting for the reply). Tanenbaum highlights several variations to improve performance:
- **Asynchronous RPC**: The client sends the request and immediately continues execution. The server does not send a reply (used for one-way events).
- **Deferred Synchronous RPC**: The client sends the request, continues execution, and later polls or waits for the server's reply when it actually needs the result.
- **Multicast RPC**: A client sends an asynchronous RPC request to a group of servers (via multicast). Each server processes the request in parallel, and the client receives multiple callbacks with the results.

## Example

Consider a client calculating tax via a remote server using a Python-like RPC syntax (similar to Tanenbaum's RPyC examples).

**Client Code:**
```python
# The programmer writes this exactly like a local call.
total_price = rpc_client.calculate_tax(item_value=100.00, state="CA")
```

**Under the Hood:**
1. The `rpc_client` (Client Stub) marshals `100.00` and `"CA"` into a byte array (handling any Endianness conversions).
2. It sends the byte array over a TCP socket.
3. The server stub receives it, unmarshals the string and float, and invokes the real `calculate_tax` function.
4. The float result is marshaled and sent back.

## Applications & Use Cases

- **Distributed Computing Environment (DCE)**: Developed by the OSF, DCE RPC is the classic framework that formed the basis for Microsoft's DCOM and the Samba file server.
- **Microservices**: Modern systems use gRPC (based on HTTP/2 and Protocol Buffers) for extremely fast, strongly-typed internal communications between microservices.
- **Network File Systems (NFS)**: Tanenbaum notes that NFS clients implement file system operations as remote procedure calls to the NFS server.

## 3 Solved Numerical/Analytical Examples

**Example 1: Endianness Conversion (Marshaling) Overhead**
*Problem:* A Little-Endian client sends an array of 1,000 32-bit integers via RPC to a Big-Endian server. The RPC framework mandates a Big-Endian wire format. If converting a single integer takes 5 CPU cycles on a 2 GHz processor, what is the marshaling overhead on the client?
*Solution:*
1. The client must convert 1,000 integers to the wire format.
2. Total cycles = $1,000 \times 5 = 5,000$ cycles.
3. Time taken = $5,000 \text{ cycles} / (2 \times 10^9 \text{ cycles/second}) = 2.5 \mu\text{s}$.
*Conclusion:* The client incurs $2.5 \mu\text{s}$ of overhead. The server incurs zero overhead because its native format matches the wire format.

**Example 2: Analyzing Call-by-Copy/Restore vs. Local Call**
*Problem:* A local procedure `increment(&x)` takes 1 ns. `x` is a 4-byte integer. In an RPC system, network latency is 5 ms one-way. How much slower is the RPC call compared to the local call?
*Solution:*
1. Since pointers can't be passed, the RPC uses Call-by-Copy/Restore.
2. Client Stub copies `x`, sends it (5 ms), Server increments it (1 ns), Server Stub copies the new value, and sends it back (5 ms).
3. Client Stub overwrites the local `x`.
4. Total RPC Time = $5 \text{ ms (out)} + \text{execution} + 5 \text{ ms (back)} \approx 10 \text{ ms} = 10,000,000 \text{ ns}$.
*Conclusion:* The RPC is $10,000,000$ times slower, highlighting that network latency, not execution time, dominates RPC performance.

**Example 3: Asynchronous RPC Performance Gain**
*Problem:* A client needs to log 5 events to a remote server. A synchronous RPC takes 20 ms round-trip. How long does it take using Synchronous RPC vs. Asynchronous RPC (assuming network transmission takes 1 ms and server processing takes 19 ms)?
*Solution:*
1. **Synchronous**: Client blocks for each call. Total time = $5 \times 20 \text{ ms} = 100 \text{ ms}$.
2. **Asynchronous**: Client sends a request (1 ms) and immediately sends the next without waiting. Total time on client = $5 \times 1 \text{ ms} = 5 \text{ ms}$.
*Conclusion:* Asynchronous RPC reduces client-side blocking time from 100 ms to 5 ms, massively increasing client throughput for one-way operations.

## Previous Year Questions & Solutions

**[April 2018] PART A - Q4) Define Remote Procedure Call (RPC). (4 marks)**
*Solution:*
Remote Procedure Call (RPC) is a distributed communication mechanism that allows a program executing on one machine to seamlessly invoke a procedure located in a different address space on a remote machine. 
According to Tanenbaum, its primary defining features are:
1. **Access Transparency:** It hides the complexity of message passing from the developer; the remote call behaves syntactically identically to a local function call.
2. **Stub-based Architecture:** It relies on compiler-generated "stubs". The client stub marshals parameters into a network message, and the server stub unmarshals the request, executes the code, and marshals the return value back.
3. **Handling Address Space Differences:** Since processes don't share memory, RPC handles parameter passing by value (or copy/restore) and manages data format conversions (like endianness) automatically through neutral wire formats.
