# Phases in Software Development Requirement Analysis

## 1. Explanation
Requirement analysis (often termed Requirements Engineering) is the crucial software engineering action that bridges the gap between the initial customer request and the technical design phase. According to Roger S. Pressman, skipping this phase is the fastest way to ensure project failure, as building the wrong system perfectly is completely useless. 

Pressman explicitly divides the requirements engineering process into **7 distinct phases (functions):**

1. **Inception:** 
   - **Goal:** Establish a basic understanding of the problem.
   - **Action:** Software engineers ask context-free questions to identify the stakeholders, understand the nature of the problem, and define the overarching business goals. They establish if the project is even feasible before investing heavy resources.

2. **Elicitation (Gathering):**
   - **Goal:** Draw out the specific functional and non-functional requirements from the customer.
   - **Action:** The team conducts facilitated meetings, Quality Function Deployment (QFD) sessions, and develops usage scenarios (Use Cases). This phase is notoriously difficult because of the "IKIWISI" (I'll Know It When I See It) syndrome and conflicting stakeholder desires.

3. **Elaboration (Modeling):**
   - **Goal:** Expand and refine the elicited requirements into a structured technical model.
   - **Action:** The analyst creates rigorous models—such as Data Flow Diagrams, Class Models, and State Transition Diagrams—to understand data, function, and behavioral states. This transforms ambiguous English into mathematical and visual logic.

4. **Negotiation:**
   - **Goal:** Reconcile conflicting requirements and establish a realistic project scope.
   - **Action:** Customers inevitably ask for more features than the budget allows. The software team and stakeholders rank requirements by priority and negotiate what will be included in the first release versus what gets deferred, establishing a realistic project plan.

5. **Specification:**
   - **Goal:** Produce a final, formalized document.
   - **Action:** The finalized models and negotiated requirements are bound into a formal Software Requirements Specification (SRS). This can be a written document, a set of graphical models, or an executable prototype. It serves as the legal and technical foundation for the design team.

6. **Validation (Review):**
   - **Goal:** Ensure the specification accurately represents the customer's true needs.
   - **Action:** The SRS is formally reviewed by stakeholders, developers, and quality assurance teams. They hunt for errors in interpretation, missing information, and conflicting rules before any code is written.

7. **Requirements Management:**
   - **Goal:** Control requirement changes over the project lifecycle.
   - **Action:** Requirements are never static; they change constantly. This phase involves tracking each requirement (traceability) so that if the customer requests a change in month 6, the team knows exactly which design models and code modules must be modified.

## 2. Example
Imagine building a new course registration system for a University:
- **Inception:** Meeting the Dean to understand that the goal is to stop servers from crashing during enrollment week.
- **Elicitation:** Interviewing students and professors. Students want 1-click registration; professors want strict prerequisite checks.
- **Elaboration:** Drawing a UML Sequence Diagram showing exactly how a student's request hits the database and validates against the prerequisite table.
- **Negotiation:** The Dean wants AI-based course recommendations, but the budget is too small. The team negotiates to drop the AI feature to meet the August deadline.
- **Specification:** Writing the 100-page SRS document detailing the exact database schemas, response time limits (<2 seconds), and UI layouts.
- **Validation:** Holding a formal review meeting where the Dean signs off on the SRS document.
- **Management:** Using a tool like Jira to track a change request when the University suddenly decides to change its grading system halfway through development.

## 3. Applications & Use Cases
- **Aviation Software (Boeing/Airbus):** In safety-critical domains, the **Validation** and **Specification** phases are extreme. The FAA requires mathematically verifiable specifications (formal methods) where every line of code traces back to a requirement in the management phase, ensuring no unexpected behavior can ever occur mid-flight.
- **Agile Development:** While Agile minimizes heavy documentation, it still performs all 7 phases. **Elicitation** happens via "User Stories", **Negotiation** happens during "Sprint Planning", and **Specification** is handled via executable automated test cases rather than a PDF document.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why is the Elicitation phase considered psychologically difficult?**
*Analysis:* Customers suffer from the "Problem of Understanding." They know their business deeply but lack the technical vocabulary to describe what software should do. Furthermore, different stakeholders have conflicting needs (e.g., the Marketing team wants rich, heavy graphics, while the IT team wants a lightweight, fast-loading page). The engineer must navigate these psychological and political barriers.

**Example 2: How does Elaboration resolve the ambiguity of the Elicitation phase?**
*Analysis:* During elicitation, a customer might say, "The system should lock the account if the user is suspicious." This is highly ambiguous. What defines "suspicious"? During elaboration, the analyst forces a logical model: "If State = 'Login' and Failed_Attempts > 3, transition to State = 'Locked'." This mathematical modeling removes all human ambiguity.

**Example 3: What is the primary purpose of Requirements Management traceability?**
*Analysis:* Software is volatile. If a customer changes a requirement related to "Tax Calculation" late in the project, the team must know exactly which design documents, source code files, and test cases are affected. Traceability matrices map requirements to code, ensuring a change doesn't break undocumented parts of the system.

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
**[May 2019]** What are the various phases of these model.
**[May 2024]** b) What is the importance of cohesion and coupling in software design, and how (5) can these principles be applied to create more modular and flexible software systems?
**[May 2019]** Determine the effort required thssoftwareprodtre+and ttre nominaffiopmenfti 9  Explain the design guidelines that can be used to produce "good quality" (3) classes or reusable classes.
**[May 2019]** (3) Why a value factor is always associated with every requirement?
**[May 2019]** b) Explain the steps of software maintenance with the help of a diagram.
**[December 2019]** a) Explain spiral Model for software development with a neat diagram.
**[December 2019]** b) Describe any three methods of Requirement elicitation process c) Describe the different levels of Capability Maturity Model a) Write the elements of requirements engineering process b) Discuss the prototyping model.
**[May 2024]** 9  What are the fundamental design principles that software developers should (3) follow to create effective and maintainable software products?
**[May 2019]** Is the number of loops of the spiral., fixed for different development process?
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
**[May 2023]** Discuss about its features, phases, advantages and disadvantages.
**[July 2021]** Duration: 3 Hours Marks (3) (3) (3) (3) (4) (s) help of a  (4) a) b) a) b) Suppose you were to plan to undertake the development of a product with a large (5) number of technical as well as customer related risks, which life cycle model would you adopt?
**[May 2024]** What are the main steps involved in the reqgigement engineering process, and how do they contribute to the development of high-quality software products?
**[July 2021]** b) Discuss 4 p's of software management concepts.
**[July 2021]** b) Explain software configuration management activities.
**[May 2019]** b) What are the crucial steps of requirement engineering?
**[December 2019]** c) Differentiate between waterfall model and incremental model development?
**[December 2019]** Explain software engineering as a layered technology write characteristics of waterfall model for software development How prototyping helps in software development write the significance of Requirement analysis in software engineering PART B Answer any twofall questions, each carriesg marks.
**[May 2019]** a) What is software maintenance?
**[May 2019]** a) What is meant by software configuration management?
**[January 2024]** a) Explain cyclomatic complexity analysis with suitable example.
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
**[May 2019]** b) Suppose you were to plan to undertake the development of a product with  (5) a large number of technical as well as customer related risks, which life cycle model would you adopt?
**[July 2021]** What are the crucial steps of requirement engineering?
**[July 2021]** b) Explain cyclomatic complexity analysis with suitable example.
**[May 2023]** b) Define the term software prototyping.
**[December 2019]** b) Discuss 4 p's of software management concepts.
**[July 2021]** Explain the layered technology used in software engineering process.
**[July 2021]** (4) Discuss the specification and design aspects of software engineering.
**[May 2023]** What do you understand by software configuration?
**[January 2024]** Marks I  Explain the major differences between software engineering and other traditional (3) engineering disciplines.
**[January 2024]** a) Identi$ the various types of risks in software project development 'b) Explain the Software Risk management process with the help of neat diagram.
**[May 2019]** 5  a) Explain with suitable examples, the types of software development for  (4) which the spiral'model is suitable.

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] List and explain the seven distinct phases of requirements engineering as defined in modern software engineering. (7 Marks)**
**Solution:**
According to Pressman, the seven phases of requirements engineering are:
1. **Inception:** Establishing the basic problem, identifying stakeholders, and defining the overall project constraints and business goals.
2. **Elicitation:** Gathering requirements from stakeholders through interviews, use cases, and meetings to determine what the system must do.
3. **Elaboration:** Expanding the gathered requirements into detailed technical models (like UML diagrams) that depict data, function, and behavioral states.
4. **Negotiation:** Resolving conflicting requirements among stakeholders and prioritizing features to fit within the project budget and schedule constraints.
5. **Specification:** Compiling the negotiated and modeled requirements into a formal, structured document (the SRS) or executable prototype.
6. **Validation:** Formally reviewing the specification with all stakeholders to ensure it accurately and completely represents the true needs of the customer, fixing errors before design begins.
7. **Requirements Management:** Establishing mechanisms to identify, control, and track changes to requirements over the entire lifespan of the project.
