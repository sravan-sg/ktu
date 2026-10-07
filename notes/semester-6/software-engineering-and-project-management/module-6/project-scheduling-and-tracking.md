# Project Scheduling and Tracking

## 1. Explanation
Project scheduling is an activity that distributes estimated effort across the planned project duration by allocating the effort to specific software engineering tasks. It is the core mechanism used by project managers to ensure a project does not fall behind schedule.

**Basic Concepts:**
- **Compartmentalization:** The project must be compartmentalized into a number of manageable activities and tasks (often using a Work Breakdown Structure).
- **Interdependency:** Tasks are rarely independent. A task network must be created to show dependencies (e.g., you cannot start coding the database until the database schema design task is finished).
- **Time Allocation:** Every task must be assigned a start date, a completion date, and the specific people (effort) responsible for it.
- **Milestones:** Every task must be tied to a specific, measurable milestone (e.g., a signed-off document or a passing test suite) so the manager knows it is truly 100% complete.

**Relation Between People and Effort:**
As discussed in Brooks' Law (Module 3), people and time are not highly interchangeable. If a task requires 10 person-months, you cannot assign 10 people and finish it in 1 month due to the exponential increase in communication overhead. The scheduling equation must account for this non-linear relationship.

**Defining and Selecting the Task Set:**
A task set is a collection of software engineering work tasks, milestones, and deliverables that must be accomplished. 
The manager selects the task set based on the chosen process model. If the project uses a rigid Waterfall model, the task set will include heavy documentation tasks. If it uses an Agile model, the task set will be lightweight, focusing heavily on iterative coding and testing tasks within a sprint.

## 2. Example
Imagine scheduling the development of a Login Page.
- **Task Set Definition:** 
  1. Design UI Mockup (1 day)
  2. Create Database User Table (1 day)
  3. Write Backend Auth Logic (3 days)
  4. Write Frontend HTML/JS (2 days)
  5. Integration Testing (1 day)
- **Interdependency:** Task 3 cannot begin until Task 2 is complete. Task 4 cannot begin until Task 1 is complete. Task 5 requires Tasks 3 and 4 to be complete.
- **Tracking:** The manager uses a Gantt chart. On day 3, if Task 2 is not finished, the manager immediately knows the entire schedule is at risk.

## 3. Applications & Use Cases
- **PERT / CPM:** Project managers use the Critical Path Method (CPM) to calculate the longest path through the task network. Any delay to a task on the critical path will delay the entire project launch. This dictates where the manager assigns their best developers.
- **Agile Burndown Charts:** In Scrum, tracking is visual. The team uses a burndown chart to track the remaining effort (in hours or story points) day-by-day. If the line doesn't trend down toward zero by the end of the sprint, the Scrum Master intervenes.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why is the "90% complete" syndrome a major problem in tracking?**
*Analysis:* Developers often estimate a task is "90% complete" when the bulk of the coding is done, but debugging the final 10% actually takes 50% of the total time. To combat this, managers must tie completion to objective, binary milestones (e.g., "All 50 unit tests pass"). A task is either 0% or 100% done; there is no 90%.

**Example 2: How does the relationship between people and effort affect scheduling late projects?**
*Analysis:* If a project is 2 months behind schedule, management might try to schedule 5 new hires to parallelize the work. However, because new hires require training from the existing staff, the existing staff's productivity drops to zero. The schedule slips further before it accelerates.

**Example 3: What is the purpose of a Work Breakdown Structure (WBS)?**
*Analysis:* A macroscopic project ("Build a Bank App") cannot be scheduled. A WBS systematically breaks it down: Bank App -> User Accounts -> Login Feature -> Password Hashing Logic. The lowest level of the WBS (Password Hashing) is small enough to be accurately estimated (e.g., 4 hours) and scheduled to a specific developer.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2024]** b) Explain Democratic Decentralised team organization and Controlled Decen- (2) tralised team organi zatton (e) Page 3 of4 -,1 qlgGsmt2302 18 4 Whd ale fu basic principles of project scheduling?
**[December 2019]** considering (a, b) : (2.4, 1.05) as multiplicative and exponential factor for the basic cocoMo effort estimation equation and (c, d) : (2.5, 0.38) as multiplicative and exponential factor for the basic cocoMo development time estimation equation, approximately how long does the software project take to complete ?
**[July 2021]** If life time ofthe project is 10 years, what is the total effort of the project?
**[May 2023]** What are the activities carried out (4.5) during project planning?
**[January 2024]** How risks are monitored and managed by project Managers?
**[May 2019]** Compute an estimate for annual maintenance effortCAME).If life time of the project is l0 years,what is the total effort of the project?
**[May 2023]** 14 a) Discuss the importance of project planning.
**[December 2019]** b) Explain different project scheduling techniques a) Write the different activities of software project management.
**[May 2024]** (4) 16 ' a) What is risk projection?
**[May 2023]** Discuss 4P's of Software Project Management concept What are risk management activities?
**[December 2019]** l0  Differentiate between code walk through and codeinspection l1  Draw the Rayleigh manpower loading curve and state pNR model for staffing Marks (3) (3) (3) (3) (3) (3) (3) (2) (4) c) 7a) b) overall cost ofthe project?
**[December 2019]** a) Discuss how to define a task set for the software project.
**[May 2023]** If life time of the project is l5 years, what is the total effort of the project?
**[July 2021]** a) Explain different project scheduling techniques.
**[May 2024]** What are the risk orojection activities performed by (5) the project planner along with other rnanagers and technical statr?
**[May 2024]** (5) 17 a) Whatare the 4 P's of project man4gement, and how can they be leveraged to (8) ,  ensure project success?
**[May 2019]** What are the  (3) testing that are usually performed on large (3) (3) Page 2 of 3 D F1077 b) Consider a project with the following functional units: Number of user inputs:50 Number of user outputs:40 Number of user enquiries=35 Number of user files:6 Number of extemal interfaces:4 Assume all complexity adjustment factors and weighting factors are average.
**[January 2024]** a) Explain the role of people, product, process and project in Software engineering.
**[January 2024]** a) Identi$ the various types of risks in software project development 'b) Explain the Software Risk management process with the help of neat diagram.

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] What is the relationship between people and effort in software scheduling? (3 Marks)**
**Solution:**
In software engineering, people and effort (time) are not perfectly interchangeable variables. While physical tasks (like digging a ditch) scale linearly with more people, software is an intellectual and highly interdependent process. According to Brooks' Law, adding more people to a project exponentially increases the communication paths and training overhead required to keep the team synchronized. Therefore, when scheduling, project managers cannot assume that doubling the staff will cut the project duration in half.

**[Sample Question] How does a project manager select a software engineering task set? (3 Marks)**
**Solution:**
A project manager selects a task set by evaluating the characteristics of the project (size, complexity, criticality) and mapping it to the chosen software process model. If the project is highly critical and uses the Waterfall model, the manager selects a rigorous task set heavily loaded with formal design documents, code inspections, and strict sign-off milestones. If the project is a small, volatile web application using Agile, the manager selects a lightweight task set focused on rapid prototyping, pair programming, and automated testing tasks.
