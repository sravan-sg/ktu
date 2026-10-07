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
