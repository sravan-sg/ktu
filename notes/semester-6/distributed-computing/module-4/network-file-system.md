# Network File System (NFS)

## Explanation
The **Network File System (NFS)**, originally developed by Sun Microsystems, is a distributed file system protocol allowing a user on a client computer to access files over a computer network much like local storage is accessed.

### NFS Architecture
NFS architecture is highly dependent on Remote Procedure Calls (RPC) to facilitate communication between clients and servers. It follows a stateless protocol design to simplify crash recovery:
1.  **Virtual File System (VFS):** To handle both local and remote files seamlessly, UNIX kernels introduced the VFS layer. The VFS distinguishes between local files and remote files and forwards operations appropriately.
2.  **vnodes (Virtual Nodes):** For each open file, the VFS creates a `vnode`. If the file is local, the `vnode` points to a local inode. If it's remote, the `vnode` points to an `rnode` (remote node) which contains the NFS file handle.
3.  **Client and Server Daemons:** The NFS client module handles caching and sending RPC requests. The NFS server module receives these RPC requests, accesses the local file system (using local inodes), and returns the results.
4.  **Statelessness:** NFS servers (up to NFSv3) do not keep track of which clients have which files open. Each RPC request contains all the information needed to complete the operation (e.g., file handle, offset, length). This makes server crash recovery trivial—clients simply retry requests.

## Example
**VFS Routing Example:**
An application calls `read(fd, buffer, size)`.
- The system call reaches the VFS layer.
- The VFS checks the `vnode` associated with `fd`.
- If the `vnode` indicates an NFS file, the VFS forwards the request to the NFS client module.
- The NFS client constructs an `NFS_READ` RPC and sends it to the server.
- The server processes the read, sends the data back, and the client passes it to the application.

## Applications & Use Cases
-   **Centralized Home Directories:** In university or corporate networks, user home directories are often stored on an NFS server, allowing users to log into any workstation and access their files.
-   **Shared Software Distributions:** Large software packages or read-only databases can be mounted via NFS across hundreds of nodes in a compute cluster, saving local disk space.
-   **Web Server Farms:** Multiple web servers can serve the same content mounted from a single NFS backend, ensuring consistency and simplified content updates.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
An NFS client needs to read a 16 KB file. The negotiated NFS block size (rsize) is 8 KB. How many `NFS_READ` RPC calls are required?
*Solution:*
Since the file size is 16 KB and the maximum read size per RPC is 8 KB, the client must issue 16 KB / 8 KB = 2 `NFS_READ` RPC calls.

**Example 2:**
Suppose an NFS server crashes and reboots after 5 seconds. During the crash, a client was attempting to write a block of data. What is the behavior of the client under a "hard" mount versus a "soft" mount?
*Solution:*
-   **Hard Mount:** The client will keep retrying the RPC request indefinitely until the server comes back online. The application will hang but the write will eventually succeed once the server recovers.
-   **Soft Mount:** The client will retry for a specified number of times or a timeout period. If the server is still down, it will return an I/O error to the application.

**Example 3:**
Calculate the effective throughput of an NFS connection if the network bandwidth is 1 Gbps, RPC overhead per request is 1 ms, and the read size is 32 KB.
*Solution:*
Time to transmit 32 KB over 1 Gbps: 32 KB = 262,144 bits. 262,144 bits / 1,000,000,000 bits/sec = 0.262 ms.
Total time per RPC = Transmission time (0.262 ms) + Processing/RPC Overhead (1 ms) = 1.262 ms.
Requests per second = 1000 / 1.262 ≈ 792 requests/sec.
Throughput = 792 requests/sec * 32 KB/request = 25,344 KB/sec ≈ 25.3 MB/sec.

## Previous Year Questions & Solutions
**[April 2018] Explain the architecture of Network File System (NFS). (6 marks)**
*Solution:*
The Network File System (NFS) allows clients to access remote files transparently, as if they were local. Its architecture relies on the following key components:
1.  **Client-Server Model using RPC:** NFS clients and servers communicate via Remote Procedure Calls. The client sends an RPC containing the operation (like `read` or `write`) and arguments (like file handle, offset).
2.  **Virtual File System (VFS):** A layer within the operating system kernel that provides a uniform interface for all file systems, local or remote. When a user process makes a system call (e.g., `open`, `read`), it goes to the VFS.
3.  **vnodes and rnodes:** The VFS uses `vnodes` (virtual nodes) to represent open files. If the file is on a local disk, the `vnode` directs operations to the local file system. If it is an NFS file, the `vnode` directs operations to the NFS client code, and it maintains an `rnode` (remote node) containing the NFS file handle.
4.  **Stateless Server Design:** Traditional NFS servers are stateless. They do not maintain information about open files or client state. Every client request must contain all necessary information (file handle, offset, etc.) to complete the operation. This design makes server crash recovery incredibly simple, as the server just restarts and clients resend unacknowledged requests.
