# File Service Architecture

## Explanation

A Distributed File System (DFS) is designed to emulate the functionality of a local file system for client programs, while physically storing the data across distributed network nodes. The **File Service Architecture** provides a structured way to achieve this by decoupling the responsibilities of storing raw data from the responsibilities of organizing it.

In general distributed systems literature, and aligned with Tanenbaum's DFS architectural principles, this is achieved by dividing the system into distinct services:

1. **File Service (The Storage Layer):** 
   - This service is responsible for implementing operations on the actual contents of files. 
   - It operates on a flat namespace, meaning it uses system-level identifiers (often called Unique File Identifiers or file handles) to refer to files. 
   - It handles core I/O operations like `Read`, `Write`, `Create`, and `Delete`. It does not deal with human-readable directory trees.
2. **Directory Service (The Naming Layer):** 
   - This service provides a mapping between human-readable text names (e.g., `report.txt`) and the system-level file handles used by the File Service. 
   - Clients use the Directory Service to traverse folders and look up a file by name, which returns the handle needed to access the file's bytes. 
   - It supports operations like `Lookup`, `AddName`, and `UnName`.
3. **Client Module:** 
   - This module runs on each client machine (often embedded in the OS kernel or as a VFS layer). 
   - It integrates the operations of the file and directory services under a single Application Programming Interface (API), such as POSIX. 
   - When a user application calls `open()`, the Client Module translates this into the appropriate network RPCs to the Directory and File services.

This modular architecture allows for the **separation of concerns**. A massive DFS can scale the Directory Service (to handle billions of file lookups) independently of the File Service (to handle petabytes of raw data transfer).

## Example

Consider a UNIX client trying to open and read a file `/usr/sravan/test.txt`.

1. **Interception**: The user application makes a standard local `read` system call. The **Client Module** intercepts this.
2. **Directory Resolution**: The Client Module contacts the **Directory Service** via RPC to resolve the hierarchical path `/usr/sravan/test.txt` to a specific file handle.
3. **Handle Return**: The Directory Service looks up its internal metadata tables and returns the handle (e.g., `Handle-9948`).
4. **Data Access**: The **Client Module** then uses `Handle-9948` to contact the **File Service** to request reading the actual block of bytes from the disk.

## Applications & Use Cases

- **Network-Attached Storage (NAS)**: NAS devices heavily rely on file service architectures to expose storage volumes to numerous client machines across a network.
- **Enterprise Cloud Storage**: Systems that provide virtualized storage across multiple data centers use these architectures to decouple the naming/metadata servers from the actual block storage servers.
- **Hadoop Distributed File System (HDFS)**: HDFS explicitly implements this architecture. The `NameNode` acts as the Directory Service (storing all metadata and namespaces), and the `DataNodes` act as the File Service (storing the raw blocks of data).

## 3 Solved Numerical/Analytical Examples

**Example 1: Directory Resolution Round Trips**
*Problem:* Calculate the number of network round trips required to resolve the path `/etc/config/network.conf` assuming an iterative directory resolution where the client has no cached paths.
*Solution:*
1. Client contacts Directory Service for root `/` to resolve `etc`. (1 trip)
2. Client contacts Directory Service for `etc` to resolve `config`. (1 trip)
3. Client contacts Directory Service for `config` to resolve `network.conf`. (1 trip)
4. Client uses the returned handle to contact the File Service to read the file. (1 trip)
*Conclusion:* Total = 4 network round trips.

**Example 2: The Impact of Client-Side Caching**
*Problem:* If the Client Module implements a caching mechanism with an 80% hit rate for directory lookups, what is the expected number of network round trips for the same path `/etc/config/network.conf`?
*Solution:*
1. Each of the 3 directory lookups has a 20% (0.2) chance of requiring a network round trip.
2. Expected directory round trips = $3 \times 0.2 = 0.6$ trips.
3. Expected total round trips (assuming file access itself is not cached and always remote) = $0.6 + 1 = 1.6$ round trips.
*Conclusion:* Caching at the Client Module drastically reduces network overhead on the Directory Service.

**Example 3: File Service CPU Utilization**
*Problem:* A File Service receives 1,000 read/write requests per second. Each request requires 2 ms of CPU processing to execute the disk I/O and marshal the RPC reply. If the service runs on a 4-core processor and scales perfectly, what is the CPU utilization?
*Solution:*
1. Total processing time needed per second = $1,000 \text{ requests} \times 2 \text{ ms} = 2,000 \text{ ms of work}$.
2. Total CPU time available per second on 4 cores = $4 \times 1,000 \text{ ms} = 4,000 \text{ ms of compute capacity}$.
3. Utilization = $2,000 \text{ ms} / 4,000 \text{ ms} = 0.50$.
*Conclusion:* The CPU utilization is 50%.

## Previous Year Questions & Solutions

**[April 2018] What is file service architecture? (4 marks)**
*Solution:*
File service architecture is a structural model used in distributed systems to separate and manage file system components across a network. It primarily consists of three modules:
1. **File Service:** Deals with the actual storage of data. It performs read/write operations on the contents of files using system-level handles or identifiers. It does not understand human-readable hierarchical file names.
2. **Directory Service:** Provides the mapping between human-readable text names and system-level file handles. It manages the hierarchical organization of files into directories.
3. **Client Module:** A component running on the client machine that integrates the file and directory services, presenting a single, unified local file system interface (like POSIX) to user applications. It intercepts local file calls and translates them into network RPCs.
