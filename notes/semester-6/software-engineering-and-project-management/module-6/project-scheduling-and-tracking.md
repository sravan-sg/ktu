# Project Scheduling and Tracking

## 1. Explanation
Project scheduling is an activity that distributes estimated effort across the planned project duration by allocating the effort to specific software engineering tasks. It is the core mechanism used by project managers to ensure a project does not fall behind schedule and that resources are used efficiently.

### Basic Principles of Project Scheduling
According to Pressman, there are seven fundamental principles that must guide software project scheduling:
1. **Compartmentalization:** The project must be broken down into a number of manageable activities and work tasks.
2. **Interdependency:** The relationships between tasks must be defined. Some tasks must occur in sequence (e.g., coding cannot start without design), while others can happen in parallel.
3. **Time Allocation:** Each task is allocated a specific number of work units (e.g., person-days) and is assigned a strict start and completion date.
4. **Effort Validation:** The manager must ensure that the total allocated effort on any given day does not exceed the actual number of available staff.
5. **Defined Responsibilities:** Every task must be assigned to a specific, named team member.
6. **Defined Outcomes:** Every scheduled task must produce a tangible work product (e.g., a design document, a tested module).
7. **Defined Milestones:** A milestone is achieved when one or more work products have been reviewed for quality and formally approved.

### Defining a Task Set
A **Task Set** is a collection of software engineering work tasks, milestones, and deliverables that must be accomplished to complete a project. 
- The project manager dynamically selects a task set based on the project's characteristics (size, complexity, criticality) and the chosen process model. 
- For example, a mission-critical project using the Waterfall model will have a heavy task set filled with formal design documents and strict code inspections. A volatile web startup using Agile will have a lightweight task set focused on short sprints, rapid coding, and automated tests.

### Scheduling Techniques
To visualize and track the schedule, managers rely on specific techniques:
1. **Gantt Charts (Timeline Charts):** A horizontal bar chart where the x-axis represents time and the y-axis represents tasks. It visually shows when tasks start, when they end, and their overlap.
2. **PERT (Program Evaluation and Review Technique) & CPM (Critical Path Method):** Network diagrams that show task dependencies. They calculate the **Critical Path**—the longest sequence of dependent tasks. Any delay to a task on the critical path will delay the entire project.

## 2. Example
Imagine scheduling the development of a Login Page.
- **Compartmentalization:** 
  1. Design UI Mockup (1 day)
  2. Create Database User Table (1 day)
  3. Write Backend Auth Logic (3 days)
  4. Write Frontend HTML/JS (2 days)
  5. Integration Testing (1 day)
- **Interdependency:** Task 3 cannot begin until Task 2 is complete. Task 4 cannot begin until Task 1 is complete. Task 5 requires Tasks 3 and 4 to be complete.
- **Tracking:** The manager plots this on a **Gantt Chart**. On day 3, if Task 2 is not finished, the manager immediately knows the entire schedule is at risk because Task 3 (which relies on Task 2) is on the critical path.

## 3. Applications & Use Cases
- **Enterprise Software Development:** Project managers use CPM to find the critical path in multi-year ERP implementations. The best developers are exclusively assigned to tasks on the critical path to ensure the project does not miss its multi-million dollar launch deadline.
- **Agile Development:** Instead of heavy Gantt charts, Scrum teams use **Burndown Charts** to track scheduling visually. It tracks the remaining effort (in hours or story points) day-by-day. If the line doesn't trend down toward zero by the end of the sprint, the Scrum Master intervenes.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why is the "90% complete" syndrome a major problem in tracking?**
*Analysis:* Developers often estimate a task is "90% complete" when the bulk of the coding is done, but debugging the final 10% actually takes 50% of the total time. To combat this, managers must tie completion to objective, binary milestones (e.g., "All 50 unit tests pass"). According to the *Defined Milestones* principle, a task is either 0% or 100% done; there is no 90%.

**Example 2: How does the relationship between people and effort affect scheduling late projects?**
*Analysis:* According to Brooks' Law, adding more people to a late project makes it later. If a project is 2 months behind schedule, management might try to schedule 5 new hires to parallelize the work. However, because new hires require training from the existing staff, the existing staff's productivity drops to zero, increasing communication overhead and causing the schedule to slip further before it accelerates.

**Example 3: What is the purpose of a Work Breakdown Structure (WBS)?**
*Analysis:* A macroscopic project ("Build a Bank App") cannot be scheduled because it is too large to estimate. A WBS systematically breaks it down (Compartmentalization): Bank App $\rightarrow$ User Accounts $\rightarrow$ Login Feature $\rightarrow$ Password Hashing Logic. The lowest level of the WBS (Password Hashing) is small enough to be accurately estimated (e.g., 4 hours) and scheduled to a specific developer.

## 5. Previous Year Questions & Solutions

### Actual University Questions:

*(Note: Automatically injected questions regarding risk management, COCOMO, and maintenance effort have been filtered out of this document to focus purely on Scheduling).*

**[May 2024] What are the basic principles of project scheduling? (4 Marks)**
**Solution:**
According to Pressman, there are seven fundamental principles that guide software project scheduling:
1. **Compartmentalization:** Breaking the project down into manageable activities and tasks.
2. **Interdependency:** Determining the sequence and relationships between tasks (parallel vs. sequential).
3. **Time Allocation:** Assigning work units (person-days), start dates, and end dates to each task.
4. **Effort Validation:** Ensuring the allocated effort does not exceed the number of available people on the team on any given day.
5. **Defined Responsibilities:** Assigning every scheduled task to a specific team member.
6. **Defined Outcomes:** Ensuring every task produces a clear work product.
7. **Defined Milestones:** Tying tasks to formally reviewed and approved milestones to accurately track progress.

**[December 2019] a) Discuss how to define a task set for the software project. (5 Marks)**
**Solution:**
A task set is a collection of software engineering work tasks, project milestones, and deliverables that must be accomplished to complete a particular project. To define a task set, the project manager must:
1. **Evaluate Project Characteristics:** Analyze the size, complexity, and criticality of the software being built.
2. **Select the Process Model:** Map the characteristics to an appropriate software process model (e.g., Waterfall for critical systems, Agile for small web apps).
3. **Tailor the Tasks:** Based on the process model, outline the specific tasks. A strict, formal task set will include exhaustive documentation, rigid reviews, and heavy testing tasks. A lightweight task set will focus on rapid coding iterations, pair programming, and automated testing.

**[July 2021] a) Explain different project scheduling techniques. [December 2019] b) Explain different project scheduling techniques. (5 Marks)**
**Solution:**
The two most common project scheduling techniques are:
1. **Timeline Charts (Gantt Charts):** A visual bar chart that tracks the project schedule. The x-axis represents time (days/weeks/months) and the y-axis represents the individual tasks. It provides a clear, visual representation of when tasks start, when they end, who is assigned to them, and how they overlap. It is excellent for tracking daily progress.
2. **PERT and CPM (Network Diagrams):** Program Evaluation and Review Technique (PERT) and Critical Path Method (CPM) are network scheduling models. They focus heavily on task interdependencies. By mapping out which tasks rely on others, CPM calculates the "Critical Path"—the longest sequence of dependent tasks in the project. The critical path dictates the absolute minimum time required to complete the project. Any delay to a task on the critical path will cause a delay to the entire project schedule.
