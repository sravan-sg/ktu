# File Service Architecture

## Explanation
A Distributed File System (DFS) is designed to emulate the functionality of a non-distributed file system for client programs. The **File Service Architecture** provides a structured way to achieve this by dividing the responsibilities into three distinct components:
1.  **Flat File Service:** This service is responsible for implementing operations on the contents of files. Unique File Identifiers (UFIDs) are used to refer to files. It handles operations like `Read`, `Write`, `Create`, `Delete`, and `GetAttributes`. It does not deal with human-readable names.
2.  **Directory Service:** This service provides a mapping between human-readable text names and UFIDs. Clients use the Directory Service to look up a file by name, which returns the UFID needed to access the file via the Flat File Service. It supports operations like `Lookup`, `AddName`, `UnName`, and `GetNames`.
3.  **Client Module:** This module runs on each client computer. It integrates and extends the operations of the flat file and directory services under a single Application Programming Interface (API). For example, in UNIX systems, it provides a unified namespace and holds information about the network locations of the services.

This modular architecture allows for the separation of concerns, making the system easier to design, implement, and maintain.

## Example
Consider a UNIX client trying to open a file `/usr/sravan/test.txt`.
1.  The **Client Module** intercepts the `open` system call.
2.  It contacts the **Directory Service** to resolve the path `/usr/sravan/test.txt` to a specific UFID.
3.  The Directory Service looks up its internal tables and returns the UFID (e.g., `UFID-9948`).
4.  The **Client Module** then uses `UFID-9948` to contact the **Flat File Service** to request reading the file's contents.

## Applications & Use Cases
-   **Network-Attached Storage (NAS):** NAS devices heavily rely on file service architectures to expose storage volumes to numerous client machines across a network.
-   **Enterprise Cloud Storage:** Systems that provide virtualized storage across multiple data centers use these architectures to decouple the naming (metadata) from the actual byte storage (flat file).
-   **Hadoop Distributed File System (HDFS):** While conceptually more complex, HDFS uses a similar split where the NameNode acts as the Directory Service and DataNodes act as the Flat File Service.

## 3 Solved Numerical/Analytical Examples
**Example 1:**
Calculate the number of network round trips required to resolve the path `/etc/config/network.conf` assuming an iterative directory resolution where no paths are cached.
*Solution:*
1.  Root directory `/` -> resolve `etc`
2.  Directory `etc` -> resolve `config`
3.  Directory `config` -> resolve `network.conf`
Total round trips = 3 to the Directory Service, plus 1 to the Flat File Service to access the file. Total = 4 round trips.

**Example 2:**
If the Client Module implements a caching mechanism with an 80% hit rate for directory lookups, what is the expected number of network round trips for the same path `/etc/config/network.conf`?
*Solution:*
Each of the 3 directory lookups has a 20% (0.2) chance of requiring a network round trip.
Expected directory round trips = 3 * 0.2 = 0.6
Expected total round trips (assuming file access is always remote) = 0.6 + 1 = 1.6 round trips.

**Example 3:**
A flat file service receives 1000 requests per second. Each request takes 2ms to process. If the service runs on a 4-core processor and can perfectly parallelize, what is the CPU utilization?
*Solution:*
Total processing time needed per second = 1000 requests * 2ms = 2000ms.
Total CPU time available per second on 4 cores = 4000ms.
Utilization = 2000ms / 4000ms = 50%.

## Previous Year Questions & Solutions
**[April 2018] What is file service architecture? (4 marks)**
*Solution:*
File service architecture is a model used in distributed systems to structure file system components. It primarily consists of three modules:
1.  **Flat File Service:** Deals with the actual storage of data. It performs operations on the contents of files using Unique File Identifiers (UFIDs). It does not understand human-readable hierarchical file names.
2.  **Directory Service:** Provides the mapping between human-readable text names and UFIDs. It handles the hierarchical organization of files into directories.
3.  **Client Module:** A component that runs on the client machine. It integrates the flat file and directory services, presenting a single, unified file system interface (like POSIX) to user applications. It intercepts local file calls and translates them into network requests to the respective services.
