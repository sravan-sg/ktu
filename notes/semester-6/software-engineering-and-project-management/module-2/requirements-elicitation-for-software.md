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

**[December 2019] Describe any three methods of Requirement elicitation process. (4 Marks)**
**Solution:**
Three common methods for requirement elicitation are:
1. **Interviews:** The most traditional method, where engineers hold one-on-one or group discussions with users and stakeholders to ask targeted questions about their needs, pain points, and expectations.
2. **Facilitated Application Specification Techniques (FAST):** Collaborative meetings (often called Joint Application Design or JAD sessions) where a team of developers and customers work together in a structured workshop to brainstorm, identify the system's scope, and negotiate requirements.
3. **Use Cases / Scenarios:** Developers and users create step-by-step narrative descriptions of how specific actors will interact with the system under specific conditions. This helps clarify exact functional flows and edge cases from the user's perspective.
