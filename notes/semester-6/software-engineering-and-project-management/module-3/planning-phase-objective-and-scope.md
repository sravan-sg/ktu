# Planning Phase: Objective and Software Scope

## 1. Explanation
The planning phase of software engineering is fundamentally about estimating the cost, effort, and duration of the project before heavy coding begins. Estimation risk is driven by uncertainty; therefore, the planning phase exists to replace uncertainty with a quantitative framework.

### The Objective of Software Project Planning
According to Roger S. Pressman, the objective of software project planning is to **"provide a framework that enables the manager to make reasonable estimates of resources, cost, and schedule."**
- **Bounded Outcomes:** Estimates must attempt to define best-case and worst-case scenarios so that project outcomes are bounded. 
- **Iterative Adaptation:** The plan is never a static, one-time document. Because software requirements are volatile, the plan must be continuously adapted and updated as the project proceeds and more information becomes known.

### Defining Software Scope
Before any accurate estimation can occur, the project manager must rigorously define the **Software Scope**.
Software scope describes the functions and features that are to be delivered to end-users. It acts as the boundary of the project. To determine scope, the manager must define:
1. **The Information Domain:** The data that are input into the system and the output that is produced.
2. **Function and Content:** The specific features the software will execute and the content it will present.
3. **Performance Criteria:** How fast or efficiently the system must process the data (e.g., response time limits).
4. **Constraints and Interfaces:** Limits placed on the software by external hardware, available memory, or integration with existing systems.

Scope is established either via a narrative description (derived from stakeholder communication) or by developing a comprehensive set of Use Cases.

### Feasibility
Once the scope is bounded, the manager must immediately ask: *"Is this project feasible?"*
According to Putnam and Myers, software feasibility has four solid dimensions that must be evaluated:
1. **Technology:** Is it within the state of the art? Can defects be reduced to acceptable levels?
2. **Finance:** Can the development be funded?
3. **Time:** Will the product reach the market before the window of opportunity closes?
4. **Resources:** Does the organization have the requisite skilled personnel to execute the scope?

## 2. Example
Imagine planning the construction of an automated Drone Delivery Routing System for a logistics startup:
- **Objective:** The manager needs to estimate if the initial routing engine will take 3 months and 5 developers (best-case), or 8 months and 10 developers (worst-case).
- **Scope Definition:** 
  - *Functions:* Calculate optimal flight paths, avoid no-fly zones.
  - *Data:* Input = GPS coordinates and package weight. Output = 3D flight trajectory.
  - *Constraints:* Must run on a lightweight Raspberry Pi onboard the drone.
- **Feasibility Check:** The manager realizes they lack engineers who understand 3D spatial aerodynamics (Resource Feasibility failure). The scope must either be reduced, or external experts must be hired before planning can proceed.

## 3. Applications & Use Cases
- **Contract Bidding:** In IT consulting (like TCS or IBM), project managers rely heavily on defining strict software scope to bid on fixed-price client contracts. If they loosely define the scope, they suffer from "scope creep" (endless addition of unpaid features by the client), leading to catastrophic financial losses.
- **Agile Release Planning:** While Agile minimizes long-term 2-year planning, the *objective* remains the same. Teams define the scope for a single "Sprint" (a 2-week block) to estimate exactly how much effort can fit into that timeframe, adapting the overall plan iteratively at the end of every sprint.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why must a statement of software scope be "bounded"?**
*Analysis:* An unbounded scope (e.g., "Build a fast search engine") cannot be estimated. How fast is "fast"? A bounded scope (e.g., "Search engine must return queries of up to 1 million records in under 2.0 seconds") provides quantitative limits. Only bounded statements can be mapped to cost and schedule estimates.

**Example 2: What is the relationship between Scope Variability and Estimation Risk?**
*Analysis:* Estimation risk is directly proportional to scope variability. If a customer's requirements are highly unstable and the scope constantly shifts, the uncertainty in cost and schedule becomes dangerously high. Bounding the scope early minimizes this risk.

**Example 3: Can a project be technologically feasible but financially infeasible?**
*Analysis:* Yes. For instance, building a real-time global satellite internet routing system is technologically feasible today. However, if the startup only has $500,000 in funding, it is completely financially infeasible. Feasibility must pass all four dimensions (Technology, Finance, Time, Resources) to proceed.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2023]** 14 a) Discuss the importance of project planning.
**[December 2019]** What is the scope of software engineering  (3) Discuss the maintenance aspects of software engineering.
**[May 2023]** Discuss about its features, phases, advantages and disadvantages.
**[May 2019]** 6  a) What are the major phases in the waterfall model of software (5) development?
**[May 2023]** What are the activities carried out (4.5) during project planning?
**[May 2019]** Which phase consumes the maximum effort for developing a typical software product?
**[May 2023]** b) Discuss the term phase containment of errors.
**[May 2019]** What are the various phases of these model.

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] What are the objectives of software project planning? (3 Marks)**
**Solution:**
According to Pressman, the primary objective of software project planning is to provide a framework that enables the manager to make reasonable estimates of resources, cost, and schedule. It involves defining both best-case and worst-case scenarios to bound project outcomes. Furthermore, the objective recognizes that planning is an iterative process; the established estimates must be continuously adapted and updated as the project proceeds and requirements evolve.

**[Sample Question] Define software scope and list the key elements it describes. (4 Marks)**
**Solution:**
Software scope is the clearly defined boundary of the software project. It must be bounded to allow for accurate cost and schedule estimation. It describes four key elements:
1. The functions and features to be delivered to end-users.
2. The data that are input to and output from the system.
3. The performance criteria (like processing speed and response time).
4. The constraints and interfaces (limits placed by hardware, memory, or external systems).

**[Sample Question] Discuss the dimensions of software feasibility. (4 Marks)**
**Solution:**
Once scope is defined, the project must be evaluated for feasibility across four solid dimensions:
1. **Technology:** Assessing if the project is technically possible within the current state of the art and if defect rates can be managed.
2. **Finance:** Determining if the organization has the budget to fund the development.
3. **Time:** Evaluating if the software can be built and delivered before the market window of opportunity closes.
4. **Resources:** Checking if the organization currently possesses, or can acquire, the human resources with the necessary technical skills to execute the project.
