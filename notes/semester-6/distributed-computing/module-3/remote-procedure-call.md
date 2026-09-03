# Remote Procedure Call (RPC)

## Explanation

Remote Procedure Call (RPC) is a powerful distributed computing paradigm that allows a program to execute a subroutine (procedure) on a different, remote node as if it were a local subroutine call. The goal of RPC is to provide **location transparency**, hiding the complex details of network communication, message serialization, and operating system boundaries from the programmer.

### The RPC Architecture
RPC relies on generated "stubs" on both the client and server sides to mask the network interaction:
1. **Client**: The application calls a local function. This is actually a dummy function called the **Client Stub**.
2. **Client Stub**: Packs (marshals) the function name and parameters into a network message and calls the OS to send it to the server.
3. **Network OS**: Transmits the message over TCP/UDP to the remote machine.
4. **Server OS**: Receives the message and passes it to the **Server Stub** (or skeleton).
5. **Server Stub**: Unpacks (unmarshals) the message and calls the actual implementation of the function on the server.
6. **Server Implementation**: Executes the logic and returns the result to the Server Stub, which marshals it and sends it back through the reverse path.

### Challenges in RPC
- **Parameter Passing**: Since processes don't share memory, pointers (call-by-reference) cannot be sent over the network directly. They must be resolved into actual values (call-by-copy/restore) or handled via special distributed memory handlers.
- **Data Representation**: Different machines may have different endianness or data type sizes. RPC frameworks use standard wire formats (like XDR or Protocol Buffers) to ensure correct decoding.
- **Failure Semantics**: Unlike a local call, an RPC can fail due to network partitions or server crashes. RPC systems provide different semantics: *At-least-once*, *At-most-once*, or *Exactly-once*.

## Example

Consider a client calculating the tax for an item, but the tax engine resides on a remote server.

**Client Code (Python-like):**
```python
# The programmer writes this exactly like a local call.
# They don't write any HTTP or socket code.
total_price = rpc_client.calculate_tax(item_value=100.00, state="CA")
```

**Under the Hood (Stubs):**
The `calculate_tax` function in `rpc_client` serializes `[100.00, "CA"]` into JSON or Protobuf, opens a socket to the tax server, waits for the reply, deserializes it, and returns it to `total_price`.

## Applications & Use Cases

- **Microservices Internal Communication**: High-performance internal communications between microservices often use gRPC (Google's RPC framework based on HTTP/2 and Protobuf) instead of REST because it is strongly typed and significantly faster.
- **Distributed File Systems**: Systems like NFS (Network File System) are built heavily on ONC RPC (Sun RPC) to allow clients to issue read/write commands to remote disks.
- **Distributed Operating Systems**: Components across different machines coordinating OS-level tasks.

## 3 Solved Numerical/Analytical Examples

**Example 1: Endianness Conversion Overhead**
A client is Little-Endian and a server is Big-Endian. The client sends an array of 1,000 32-bit integers via RPC. The network uses Big-Endian (Network Byte Order). If converting a single 32-bit integer takes 5 CPU cycles on a 2 GHz processor, what is the marshalling overhead on the client?
*Solution:*
1. The client must convert 1,000 integers from Little-Endian to Big-Endian.
2. Total cycles = $1,000 \times 5 = 5,000$ cycles.
3. Time taken = $5,000 \text{ cycles} / (2 \times 10^9 \text{ cycles/second}) = 2.5 \mu\text{s}$.
*Note:* The server incurs zero overhead because it is already Big-Endian (matches network order).

**Example 2: Analyzing Call-by-Copy/Restore vs. Call-by-Reference**
A local procedure `increment(&x)` takes 1 ns. `x` is a 4-byte integer. In an RPC system, network latency is 5 ms one-way. How much slower is the RPC call compared to the local call?
*Solution:*
1. Since pointers can't be passed, the RPC uses Call-by-Copy/Restore.
2. The Client Stub copies the value of `x` (4 bytes) into a message, sends it (5 ms), Server increments it, Server Stub copies the new value, and sends it back (5 ms).
3. The Client Stub then overwrites the local `x` with the returned value.
4. Total RPC Time = $5 \text{ ms (out)} + \text{execution} + 5 \text{ ms (back)} \approx 10 \text{ ms} = 10,000,000 \text{ ns}$.
*Conclusion:* The RPC is $10,000,000$ times slower than the local call, highlighting that network latency dominates RPC performance.

**Example 3: RPC Failure Semantics**
A client executes an RPC `withdraw_funds(account=123, amount=50)`. The client's OS times out waiting for the server's reply. If the RPC system uses "At-least-once" semantics, what is the risk if the client retries?
*Solution:*
- **At-least-once** guarantees the call executes *one or more* times. If the timeout was caused by a dropped reply (the server actually processed the withdrawal), retrying will execute the withdrawal a second time, resulting in a $100 deduction. 
- To fix this, financial operations require **At-most-once** semantics (or idempotent operations), where the server filters duplicate requests based on request IDs.

## Previous Year Questions & Solutions

**[April 2018] PART A - Q4) Define Remote Procedure Call (RPC). (4 marks)**
*Solution:*
Remote Procedure Call (RPC) is a distributed computing protocol that allows a program executing on one machine to seamlessly invoke a procedure or function located in a different address space on a remote machine. 
Its primary defining features are:
1. **Transparency:** It hides the complexity of network communication from the developer; the remote call looks and behaves syntactically identically to a local function call.
2. **Stub-based Architecture:** It uses compiler-generated "stubs" on the client and server. The client stub marshals (serializes) parameters into a network message, and the server stub unmarshals the request, executes the code, and marshals the return value back.
3. **Overcoming Address Space Differences:** Since processes don't share memory, RPC handles parameter passing by value (copying data) and manages data format conversions (like endianness) automatically.
