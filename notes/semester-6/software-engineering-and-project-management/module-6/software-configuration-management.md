# Software Configuration Management (SCM)

## 1. Explanation
Software is incredibly volatile; it changes constantly during development and maintenance. **Software Configuration Management (SCM)** is the set of activities designed to control change by identifying the work products that are likely to change, establishing relationships among them, defining mechanisms for managing different versions of these work products, and controlling the changes imposed.

SCM is the "umbrella activity" that is applied throughout the entire software process. It tracks everything collectively referred to as the **Software Configuration**:
- Computer programs (source code and executables)
- Work products (SRS documents, design models, UML diagrams)
- Data structures (databases, configuration files, test data)

**Core Basics and Standards of SCM:**
1. **Identification:** Identifying Software Configuration Items (SCIs) and establishing baselines. A baseline is a milestone where a document/code is formally reviewed and frozen. Any further changes require formal approval.
2. **Version Control:** Managing the evolution of the software. Every time an SCI is modified, a new version is created and stored in a repository, ensuring old versions are never destroyed.
3. **Change Control:** A formal process where any requested change must be evaluated for its impact (cost, schedule, technical risk) by a Change Control Board (CCB) before the developer is allowed to check out and modify the code.
4. **Configuration Audit:** Verifying that the changes were actually implemented correctly according to the CCB's approval and that standards were followed.

## 2. Example
Imagine building a website for a client.
- **Baseline:** The client signs the requirement document on Monday. It is placed under SCM.
- **Change Control:** On Wednesday, the client asks to add a "Live Chat" feature. The developer doesn't just start coding. The CCB evaluates it and says it will cost an extra $5,000 and 2 weeks. The client approves.
- **Version Control:** The developer uses `git` to create a new branch, writes the chat code, and merges it into the main repository, bumping the software version from `v1.0` to `v1.1`.
- **Audit:** The QA team audits `v1.1` to ensure the live chat matches the approved change request.

## 3. Applications & Use Cases
- **Git and GitHub:** The entire modern software industry relies on Git for **Version Control**. It allows thousands of developers to work on the Linux Kernel simultaneously without overwriting each other's code, utilizing branches, commits, and pull requests to maintain SCM.
- **Regulatory Compliance (FDA/FAA):** If a medical device software causes a patient injury, the FDA will audit the company's SCM logs. The company must mathematically prove exactly which developer wrote the flawed line of code, who approved the change request, and what the baseline requirement was. Without strict SCM standards, the company faces massive fines.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: What is a "Baseline" in SCM and why is it critical?**
*Analysis:* A baseline is a conceptual line in the sand. Before a requirement document is baselined, it is just a draft—anyone can change it. Once it is baselined (formally signed off), it is locked. Any changes to it now require a formal, expensive Change Control process. This prevents "scope creep" from silently ruining the project schedule.

**Example 2: Differentiate between Version Control and Change Control.**
*Analysis:* Version Control is a technical tool (like Git) that tracks *what* changed in the files and *who* changed it, allowing rollbacks to previous states. Change Control is a human, managerial process that decides *if* a change should be allowed to happen in the first place, based on budget and schedule impacts.

**Example 3: Why are requirement documents placed under SCM, not just source code?**
*Analysis:* Because software engineering is highly interdependent. If a developer changes the source code without updating the requirement document, the QA team will test the code against the old document and fail it. SCM ensures that if the code changes, the corresponding SRS and Design models are versioned and updated simultaneously.

## 5. Previous Year Questions & Solutions

**[Sample Question] What is Software Configuration Management (SCM)? (3 Marks)**
**Solution:**
Software Configuration Management (SCM) is an umbrella activity applied throughout the software development lifecycle to systematically manage, track, and control changes in the software. It involves identifying all software configuration items (code, documents, data), managing different versions of these items, controlling change requests through a formal evaluation process, and auditing the system to ensure integrity and traceability.

**[Sample Question] Define the term "Baseline" in the context of SCM. (2 Marks)**
**Solution:**
A baseline is a milestone in software development that acts as a foundation for further work. It represents a software configuration item (like an SRS document or a stable code release) that has been formally reviewed and agreed upon. Once baselined, the item is "frozen," and any subsequent changes to it can only be made through formal, documented change control procedures.
