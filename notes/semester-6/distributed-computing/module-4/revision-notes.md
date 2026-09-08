# Module 4: Distributed File Systems & Name Services - Revision Notes

## 1. Quick Summary
Module 4 explores the design and architecture of distributed file systems (DFS) and naming services. Key concepts include providing a unified view of file systems across multiple nodes (transparency), managing metadata, and optimizing performance via caching. The core focus areas are the general File Service Architecture, Sun's Network File System (NFS), the Andrew File System (AFS), and the role of Name Services like DNS.

## 2. Key Definitions & Formulas
*   **File Service Architecture:** A modular division into Flat File Service (UFIDs, contents), Directory Service (text names to UFIDs), and Client Module (integration, API).
*   **NFS (Network File System):** A stateless distributed file system relying on RPCs, VFS, and vnodes/rnodes. Server crash recovery is trivial because the server retains no client state.
*   **AFS (Andrew File System):** A highly scalable DFS using Vice (servers) and Venus (clients). It utilizes *whole-file caching* to local disks and *callback promises* to maintain cache consistency and drastically reduce network load.
*   **Name Service:** A system that maps human-readable identifiers to machine-readable attributes (e.g., DNS mapping `example.com` to `192.0.2.1`).
*   **Name Resolution:** The process of translating a name. Can be *Iterative* (client contacts each server in the chain) or *Recursive* (local server acts as a middleman for the client).

## 3. Top Exam Focus Areas (PYQ Patterns)
1.  **Architecture of NFS:** Frequently asked. Be prepared to draw the VFS/vnode architecture and explain the stateless server design. (6 marks, April 2018)
2.  **Andrew File System (AFS):** Expect questions on its caching mechanism (whole-file) and how callbacks work to manage consistency. (4 marks, April 2018)
3.  **Role of a Name Service:** Understand location transparency and how naming facilitates scalability. (4 marks, April 2018)
4.  **File Service Architecture Components:** Differentiate the responsibilities of the Flat File Service vs the Directory Service. (4 marks, April 2018)

## 4. Most Common Mistakes & Tips
*   **NFS vs AFS Confusion:** Remember: NFS is stateless and caches blocks. AFS is stateful (due to callbacks) and caches *whole files* to the local disk. NFS is for LANs, AFS is for WANs/scale.
*   **VFS Misunderstanding:** VFS is not NFS. VFS is the local OS kernel layer that *routes* requests to either the local file system or the NFS client module.
*   **Iterative vs Recursive DNS:** In iterative, the root server returns a referral (pointer). In recursive, the root server fetches the answer and returns the final IP. Don't mix up who does the heavy lifting.