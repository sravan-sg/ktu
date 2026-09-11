# Network File System (NFS)

## Explanation

The **Network File System (NFS)**, originally developed by Sun Microsystems, is one of the most widely deployed distributed file systems. As noted by **Tanenbaum**, it is organized along a classic client-server architecture, allowing users on a client machine to access remote files over an IP network exactly as if they were local.

### NFS Architecture and the VFS Layer
NFS relies heavily on Remote Procedure Calls (RPC) and an abstraction layer within the operating system to achieve **access transparency**:
1. **Virtual File System (VFS):** To handle both local and remote files seamlessly without altering the core OS or applications, the VFS layer was introduced. The VFS intercepts file system calls (like `open`, `read`, `write`) and determines whether the file is local or remote.
2. **vnodes (Virtual Nodes):** For every open file, the VFS creates a `vnode`. 
   - If the file is local, the `vnode` directs operations to the local disk file system. 
   - If the file is remote, the `vnode` acts as a proxy, directing operations to the NFS client module.
3. **RPC Translation:** The NFS client module translates these VFS requests into standardized `NFS` RPC calls and sends them over the network to the NFS server. The server unpacks the RPC and executes it against its local file system.

### Evolution: Stateless (NFSv3) to Stateful (NFSv4)
Tanenbaum highlights a critical distinction between NFS versions:
- **NFSv3 (Stateless):** Traditional NFS servers do not maintain state about which clients have which files open. Every RPC request must be entirely self-contained (providing the file handle, offset, and data). If a server crashes, it simply reboots, and clients retry their RPCs. While this makes crash recovery trivial, it makes file locking and cache consistency very difficult.
- **NFSv4 (Stateful):** Modern NFS introduces stateful operations. It supports explicit `open` and `close` operations, allowing the server to track client state, grant explicit file locks, and utilize compound RPCs to reduce network latency.

## Example

**VFS Routing Example:**
An application calls `read(fd, buffer, size)`.
1. The system call reaches the OS **VFS layer**.
2. The VFS checks the `vnode` associated with `fd`.
3. Seeing it is an NFS file, the VFS forwards the request to the NFS client stub.
4. The NFS client marshals the request into an `NFS_READ` RPC and sends it to the server.
5. The server processes the read locally, sends the data back, and the client unmarshals it and returns it to the user application.

## Applications & Use Cases

- **Centralized Home Directories:** In university or enterprise LANs, user home directories (`/home/user`) are stored on an NFS server, allowing users to log into any physical workstation and instantly access their files.
- **Shared Compute Clusters:** Compute clusters mount massive read-only scientific datasets or shared software installations via NFS to thousands of worker nodes, saving local storage space.
- **Web Server Farms:** Multiple web servers mount the exact same `www` directory from a centralized NFS backend, ensuring all servers deliver consistent web content.

## 3 Solved Numerical/Analytical Examples

**Example 1: NFS Request Fragmentation**
*Problem:* An NFS client needs to read a 16 KB file. The negotiated maximum RPC payload size (rsize) is 8 KB. How many `NFS_READ` RPC calls are required?
*Solution:*
1. The maximum block size the network transport will allow per RPC is 8 KB.
2. The file size is 16 KB.
3. The client must split the read into multiple requests: $16 \text{ KB} / 8 \text{ KB} = 2$.
*Conclusion:* The client issues exactly 2 `NFS_READ` RPC calls.

**Example 2: Crash Recovery (Stateless vs Stateful)**
*Problem:* Suppose an NFS server crashes and reboots after 5 seconds. During the crash, a client was attempting to write a block of data. What is the recovery behavior in NFSv3 vs NFSv4?
*Solution:*
- **NFSv3 (Stateless):** The server has no memory of the client. The client's RPC times out. Under a "hard mount", the client simply re-transmits the identical `NFS_WRITE` RPC. The server processes it as a brand-new request. Recovery is instant and implicit.
- **NFSv4 (Stateful):** The server lost its lock states. Upon reboot, it enters a "grace period" where clients must proactively contact the server to reclaim their previous locks and state before issuing new read/write requests.

**Example 3: NFS Throughput Calculation**
*Problem:* Calculate the effective throughput of an NFS connection if the network bandwidth is 1 Gbps (1,000,000,000 bits/sec), RPC overhead/processing per request is 1 ms, and the read size payload is 32 KB.
*Solution:*
1. Time to transmit 32 KB over 1 Gbps: 
   $32 \text{ KB} = 262,144 \text{ bits}$. 
   $262,144 / 1,000,000,000 = 0.262 \text{ ms}$.
2. Total time per RPC = Transmission time (0.262 ms) + RPC Overhead (1 ms) = 1.262 ms.
3. Requests per second = $1,000 \text{ ms} / 1.262 \text{ ms} \approx 792 \text{ requests/sec}$.
4. Throughput = $792 \text{ req/sec} \times 32 \text{ KB/req} = 25,344 \text{ KB/sec} \approx 25.3 \text{ MB/sec}$.
*Conclusion:* Throughput is bounded significantly by the RPC processing overhead, not just the raw link speed.

## Previous Year Questions & Solutions

**[April 2018] Explain the architecture of Network File System (NFS). (6 marks)**
*Solution:*
The Network File System (NFS) allows clients to access remote files transparently over an IP network. According to Tanenbaum, its architecture relies on the following key components:
1. **Virtual File System (VFS):** A virtualization layer within the OS kernel that provides a uniform interface for all file systems. It intercepts standard system calls (like `open`, `read`) and hides whether the target is local or remote.
2. **vnodes:** The VFS uses `vnodes` (virtual nodes) to represent open files. For NFS, the `vnode` directs operations to the NFS client code and maintains a file handle pointing to the remote server.
3. **RPC Communication:** NFS clients and servers communicate exclusively via Remote Procedure Calls. The client sends an RPC containing the operation (like `NFS_READ`) and arguments (like file handle, offset, length).
4. **Stateless Server Design (NFSv3):** Traditional NFS servers are strictly stateless. They do not maintain information about open files or client state. Every client request is self-contained. This makes server crash recovery trivial, as the server just restarts and clients resend their RPCs. (Note: NFSv4 later introduced state to support advanced file locking).
