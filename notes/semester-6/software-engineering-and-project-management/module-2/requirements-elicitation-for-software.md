# Requirements Elicitation for Software

## 1. Explanation
Requirements elicitation is the most critical and often the most difficult phase of software engineering. It is the process of gathering, discovering, and understanding the needs and constraints of the stakeholders for the software system. 

According to Pressman, elicitation is difficult because:
- **Problems of Scope:** The boundary of the system is ill-defined. Customers specify unnecessary technical details rather than business objectives.
- **Problems of Understanding:** Customers are not completely sure of what they need, have a poor understanding of computer capabilities, or omit "obvious" information.
- **Problems of Volatility:** Requirements change over time as the project evolves.

To overcome these, engineers use structured elicitation methods:
1. **Interviews:** Direct one-on-one or group discussions with stakeholders.
2. **Questionnaires/Surveys:** Useful for gathering broad input from a large, geographically dispersed user base.
3. **Facilitated Application Specification Techniques (FAST):** Joint team meetings between developers and customers to identify the problem, propose elements of the solution, and negotiate different approaches.
4. **Use Cases / Scenarios:** Creating narrative descriptions of how a specific user will interact with the system in a specific circumstance.

## 2. Example
Imagine building a university library management system.
- **Bad Elicitation (Problem of Understanding):** The librarian says, "I want a database." The engineer builds a raw SQL terminal. The librarian is angry because they don't know SQL.
- **Good Elicitation (Use Cases):** The engineer creates a use case: "A student wants to check out a book." They walk through the scenario with the librarian, discovering that the system needs a barcode scanner integration, an overdue fine calculator, and an email notification system.

## 3. Applications & Use Cases
- **Agile Development:** In Agile, elicitation is continuous. Engineers write "User Stories" (a form of use cases) during every sprint planning session with the product owner to ensure the software matches current market needs.
- **Healthcare Systems:** Building Electronic Health Record (EHR) systems requires intense FAST meetings with doctors, nurses, and legal compliance officers, as missing a regulatory requirement (like HIPAA privacy rules) could result in massive fines.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Contrast Interviews vs. FAST meetings.**
*Analysis:* Interviews are often one-directional (engineer asking customer) and can suffer from the "telephone game" miscommunication. FAST meetings (Joint Application Design) bring multiple stakeholders and engineers into the same room to actively collaborate and negotiate requirements in real-time, greatly reducing misunderstandings.

**Example 2: Why are Use Cases considered the most effective elicitation tool for object-oriented design?**
*Analysis:* Use cases force stakeholders to describe the system from the perspective of an *actor* (e.g., a customer, an admin). This naturally maps to the creation of objects, classes, and methods in object-oriented programming (e.g., a `Customer` class with a `checkout()` method).

**Example 3: How do you handle the "Problem of Volatility"?**
*Analysis:* Volatility (changing requirements) is managed by establishing a strict baseline and using Software Configuration Management (SCM). Once the specification is signed off, any new elicitation requests must pass through a formal Change Control Board (CCB) to assess their cost and schedule impact.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[January 2024]** b) Explain the various software maintenance models with the help of diagram.
**[January 2024]** b) Explain any two techniques used in requirement elicitation and analysis.
**[December 2019]** What is the scope of software engineering  (3) Discuss the maintenance aspects of software engineering.
**[May 2019]** 3  Explain quality function deployment technique of requirement elicitation.
**[December 2019]** considering (a, b) : (2.4, 1.05) as multiplicative and exponential factor for the basic cocoMo effort estimation equation and (c, d) : (2.5, 0.38) as multiplicative and exponential factor for the basic cocoMo development time estimation equation, approximately how long does the software project take to complete ?
**[May 2019]** 6  a) What are the major phases in the waterfall model of software (5) development?
**[May 2019]** Which phase consumes the maximum effort for developing a typical software product?
**[December 2019]** (3) Explain the importance of requirements.
**[May 2024]** b) What is the importance of cohesion and coupling in software design, and how (5) can these principles be applied to create more modular and flexible software systems?
**[May 2019]** Determine the effort required thssoftwareprodtre+and ttre nominaffiopmenfti 9  Explain the design guidelines that can be used to produce "good quality" (3) classes or reusable classes.
**[May 2019]** b) Explain the steps of software maintenance with the help of a diagram.
**[December 2019]** a) Explain spiral Model for software development with a neat diagram.
**[December 2019]** b) Describe any three methods of Requirement elicitation process c) Describe the different levels of Capability Maturity Model a) Write the elements of requirements engineering process b) Discuss the prototyping model.
**[May 2024]** 9  What are the fundamental design principles that software developers should (3) follow to create effective and maintainable software products?
**[December 2019]** b) Explain different project scheduling techniques a) Write the different activities of software project management.
**[May 2023]** What is software maintenance?
**[May 2023]** Explain scM (Software configuration Management) activities in detail.
**[May 2023]** 6 a) What is software requirements specification (SRS)?
**[May 2023]** Discuss 4P's of Software Project Management concept What are risk management activities?
**[January 2024]** a) What is software maintenance?
**[May 2024]** (3) I I  How does white box testing differ from other types of software testing?
**[May 2023]** Explain any three techniques used for requirement elicitation.
**[December 2019]** a) Discuss how to define a task set for the software project.
**[January 2024]** a) Explain the role of people, product, process and project in Software engineering.
**[May 2024]** (3) How is the Capability Maturity Model (CMM) used to evaluate and improve (3) the mattuity of software development processes within an organization?
**[May 2024]** What are the main steps involved in the reqgigement engineering process, and how do they contribute to the development of high-quality software products?
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


**[December 2019] Describe any three methods of Requirement elicitation process. (4 Marks)**
**Solution:**
Three common methods for requirement elicitation are:
1. **Interviews:** The most traditional method, where engineers hold one-on-one or group discussions with users and stakeholders to ask targeted questions about their needs, pain points, and expectations.
2. **Facilitated Application Specification Techniques (FAST):** Collaborative meetings (often called Joint Application Design or JAD sessions) where a team of developers and customers work together in a structured workshop to brainstorm, identify the system's scope, and negotiate requirements.
3. **Use Cases / Scenarios:** Developers and users create step-by-step narrative descriptions of how specific actors will interact with the system under specific conditions. This helps clarify exact functional flows and edge cases from the user's perspective.
