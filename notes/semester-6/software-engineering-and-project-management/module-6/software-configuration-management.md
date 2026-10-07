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

### Actual University Questions:
**[January 2024]** b) Explain the various software maintenance models with the help of diagram.
**[December 2019]** What is the scope of software engineering  (3) Discuss the maintenance aspects of software engineering.
**[December 2019]** considering (a, b) : (2.4, 1.05) as multiplicative and exponential factor for the basic cocoMo effort estimation equation and (c, d) : (2.5, 0.38) as multiplicative and exponential factor for the basic cocoMo development time estimation equation, approximately how long does the software project take to complete ?
**[May 2019]** 6  a) What are the major phases in the waterfall model of software (5) development?
**[May 2019]** Which phase consumes the maximum effort for developing a typical software product?
**[December 2019]** a) Discuss Risk management activities in detail.
**[May 2024]** b) What is the importance of cohesion and coupling in software design, and how (5) can these principles be applied to create more modular and flexible software systems?
**[May 2019]** Determine the effort required thssoftwareprodtre+and ttre nominaffiopmenfti 9  Explain the design guidelines that can be used to produce "good quality" (3) classes or reusable classes.
**[May 2019]** b) Explain the steps of software maintenance with the help of a diagram.
**[January 2024]** Explain different activities (5) involved in configuration management.
**[May 2019]** Explain different activities involved in configuration management.
**[December 2019]** a) Explain spiral Model for software development with a neat diagram.
**[May 2024]** 9  What are the fundamental design principles that software developers should (3) follow to create effective and maintainable software products?
**[December 2019]** b) Explain different project scheduling techniques a) Write the different activities of software project management.
**[May 2023]** What is software maintenance?
**[May 2019]** b) What are risk management activities?
**[May 2023]** Explain scM (Software configuration Management) activities in detail.
**[May 2023]** 6 a) What is software requirements specification (SRS)?
**[May 2023]** Discuss 4P's of Software Project Management concept What are risk management activities?
**[January 2024]** a) What is software maintenance?
**[May 2024]** (3) I I  How does white box testing differ from other types of software testing?
**[December 2019]** a) Discuss how to define a task set for the software project.
**[January 2024]** a) Explain the role of people, product, process and project in Software engineering.
**[May 2024]** (3) How is the Capability Maturity Model (CMM) used to evaluate and improve (3) the mattuity of software development processes within an organization?
**[May 2024]** What are the main steps involved in the reqgigement engineering process, and how do they contribute to the development of high-quality software products?
**[July 2021]** (4) b) Discuss Risk management activities in detail.
**[July 2021]** b) Discuss 4 p's of software management concepts.
**[July 2021]** b) Explain software configuration management activities.
**[December 2019]** Explain software engineering as a layered technology write characteristics of waterfall model for software development How prototyping helps in software development write the significance of Requirement analysis in software engineering PART B Answer any twofall questions, each carriesg marks.
**[May 2019]** a) What is software maintenance?
**[May 2019]** a) What is meant by software configuration management?
**[May 2019]** Explain different types of software risk.
**[December 2019]** b) Explain software configuration management activities.
**[May 2023]** Explain the steps of software maintenance with help of a diagram.
**[May 2023]** What are the different kinds (4) ofsystem testing that are usually performed on large software products?
**[January 2024]** (6) a) Explain the term software configuration management?
**[May 2023]** Define the term software crisis.
**[July 2021]** What is a software process?
**[May 2023]** Which software process model allows risk management?
**[May 2019]** PART D Answer any twofull questions, each carries9 marks' modularityf List out the important properties of a modular (3) b) What do you understand different kinds of system software products?
**[May 2024]** As you move outward along the process flow path of the spiral model, what can you say about the software that is being developed or maintained?
**[May 2023]** b) Define the term software prototyping.
**[May 2023]** What do you understand by software configuration?
**[December 2019]** b) Discuss 4 p's of software management concepts.
**[July 2021]** Explain the layered technology used in software engineering process.
**[July 2021]** (4) Discuss the specification and design aspects of software engineering.
**[January 2024]** Marks I  Explain the major differences between software engineering and other traditional (3) engineering disciplines.
**[January 2024]** a) Identi$ the various types of risks in software project development 'b) Explain the Software Risk management process with the help of neat diagram.
**[May 2019]** 5  a) Explain with suitable examples, the types of software development for  (4) which the spiral'model is suitable.

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] What is Software Configuration Management (SCM)? (3 Marks)**
**Solution:**
Software Configuration Management (SCM) is an umbrella activity applied throughout the software development lifecycle to systematically manage, track, and control changes in the software. It involves identifying all software configuration items (code, documents, data), managing different versions of these items, controlling change requests through a formal evaluation process, and auditing the system to ensure integrity and traceability.

**[Sample Question] Define the term "Baseline" in the context of SCM. (2 Marks)**
**Solution:**
A baseline is a milestone in software development that acts as a foundation for further work. It represents a software configuration item (like an SRS document or a stable code release) that has been formally reviewed and agreed upon. Once baselined, the item is "frozen," and any subsequent changes to it can only be made through formal, documented change control procedures.
