# Design Phase: Process, Principles, and Concepts

## 1. Explanation
Software design sits at the technical kernel of software engineering. According to Pressman, it is the phase where the requirements (the "what") generated during the analysis phase are transformed into a blueprint (the "how") for constructing the software. 

M. A. Jackson once stated, "The beginning of wisdom for a software engineer is to recognize the difference between getting a program to work, and getting it right." The design phase provides the framework for getting it right.

### The Design Process
Design is an iterative process through which requirements are translated into a "model" of the software. Pressman identifies four distinct levels of design abstraction that occur during this process:
1. **Data Design (or Class Design):** Transforms the information domain model created during analysis into the data structures (e.g., database schema or complex object classes) that will be required to implement the software.
2. **Architectural Design:** Defines the relationship between major structural elements of the software, the architectural styles and patterns that can be used to achieve the requirements, and the constraints that affect the way in which architecture can be implemented.
3. **Interface Design:** Describes how the software communicates within itself, with systems that interoperate with it, and with humans who use it.
4. **Component-Level Design:** Transforms structural elements of the software architecture into a procedural description of software components (the actual algorithmic logic).

### Software Design Principles
According to David Parnas and the guidelines outlined in Pressman, a high-quality design must adhere to specific principles:
- **Design should be traceable to the analysis model:** A single element of the design must trace back to a specific customer requirement.
- **Design should not reinvent the wheel:** Time is short, and resources are limited; design should use repeatable patterns and proven architectural styles.
- **Design should exhibit uniformity and integration:** A design should appear as if a single person developed it, even if a team of 20 built it.
- **Design should minimize intellectual distance:** The structure of the software should mimic the structure of the real-world problem domain.

### Fundamental Software Design Concepts
A set of fundamental software design concepts has evolved over the history of software engineering. These concepts provide the criteria to answer how software should be partitioned:
1. **Abstraction:** At the highest level, a solution is stated in broad terms using the language of the problem environment. At lower levels, detailed implementation is provided. There are *Procedural Abstractions* (a sequence of instructions with a specific limited function, e.g., `openDoor()`) and *Data Abstractions* (a named collection of data attributes, e.g., the `Door` object containing weight and dimensions).
2. **Architecture:** The overall structure or organization of program components (modules) and the manner in which they interact.
3. **Patterns:** A design structure that solves a particular recurring design problem within a specific context.
4. **Separation of Concerns:** A complex problem can be more easily handled if it is subdivided into pieces that can each be solved independently.
5. **Modularity:** The most common manifestation of separation of concerns. Software is divided into separately named and addressable components (modules). 
6. **Information Hiding:** Modules should be specified and designed so that information (algorithms and data) contained within a module is inaccessible to other modules that have no need for such information.
7. **Functional Independence:** Achieved by developing modules with a "single-minded" function (high Cohesion) and an aversion to excessive interaction with other modules (low Coupling).
8. **Stepwise Refinement:** A top-down design strategy proposed by Niklaus Wirth where a program is developed by successively refining levels of procedural detail.

## 2. Example
Imagine designing a smart banking application (mapping the Process):
- **Data Design:** Designing the SQL database schema mapping the `Customer`, `Account`, and `Transaction` entities.
- **Architectural Design:** Choosing an N-Tier architecture (Presentation Layer, Business Logic Layer, Data Access Layer) to separate concerns.
- **Interface Design:** Designing a REST API that allows the mobile app to securely fetch `Account` data from the server.
- **Component-Level Design:** Writing the pseudocode algorithm inside the `Transaction` module that safely subtracts money from Account A and adds it to Account B (ensuring atomicity).

## 3. Applications & Use Cases
- **Information Hiding in Modern OS:** Modern Operating Systems strictly apply **Information Hiding**. A user application (like a word processor) cannot directly access the computer's memory hardware. The OS Kernel hides the memory management algorithms and exposes only a limited API (`malloc()`). This prevents user apps from crashing the entire system.
- **Modularity Cost Curve:** Why not make 1 million tiny modules? Pressman's modularity cost curve shows that as the number of modules increases, the cost to develop each individual module drops. However, the cost to *integrate* those modules rises exponentially. The engineer must find the optimal middle ground.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: How does Abstraction differ from Information Hiding?**
*Analysis:* Abstraction is about *simplifying* reality for the user to make complexity manageable (e.g., providing a `drive()` function for a car). Information Hiding is about *protecting* the internal data from external modification to prevent errors (e.g., locking the hood of the car so the driver cannot accidentally break the engine's timing belt).

**Example 2: What is the relationship between Separation of Concerns, Cohesion, and Coupling?**
*Analysis:* Separation of Concerns dictates breaking a problem into independent pieces. To measure if we did this correctly, we use two metrics: Cohesion and Coupling. **Cohesion** measures how single-minded a module is (we want High Cohesion). **Coupling** measures how entangled a module is with others (we want Low Coupling). Together, they define **Functional Independence**.

**Example 3: Describe Stepwise Refinement (Elaboration).**
*Analysis:* It is a top-down elaboration process. We start with a high-level abstraction: "Calculate Taxes". We refine it in step 1: "Get Income, Apply Deductions, Calculate Brackets". We refine step 2 further: "Iterate through deduction list, sum valid charitable donations...". This continues until we reach code-level detail.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[May 2024]** b) Explain Democratic Decentralised team organization and Controlled Decen- (2) tralised team organi zatton (e) Page 3 of4 -,1 qlgGsmt2302 18 4 Whd ale fu basic principles of project scheduling?
**[May 2019]** 6  a) What are the major phases in the waterfall model of software (5) development?
**[May 2019]** Which phase consumes the maximum effort for developing a typical software product?
**[May 2023]** b) Discuss the term phase containment of errors.
**[May 2019]** What are the various phases of these model.
**[May 2024]** b) What is the importance of cohesion and coupling in software design, and how (5) can these principles be applied to create more modular and flexible software systems?
**[May 2019]** Determine the effort required thssoftwareprodtre+and ttre nominaffiopmenfti 9  Explain the design guidelines that can be used to produce "good quality" (3) classes or reusable classes.
**[December 2019]** b) Describe any three methods of Requirement elicitation process c) Describe the different levels of Capability Maturity Model a) Write the elements of requirements engineering process b) Discuss the prototyping model.
**[May 2024]** 9  What are the fundamental design principles that software developers should (3) follow to create effective and maintainable software products?
**[May 2019]** Is the number of loops of the spiral., fixed for different development process?
**[May 2024]** 13 a) Explain the concept of abstraction in design?
**[May 2024]** 15 a) ExplaintheprocessofMaintenance.
**[May 2024]** (3) How is the Capability Maturity Model (CMM) used to evaluate and improve (3) the mattuity of software development processes within an organization?
**[May 2023]** Discuss about its features, phases, advantages and disadvantages.
**[May 2023]** Discuss the rules for user interface design.
**[May 2024]** What are the main steps involved in the reqgigement engineering process, and how do they contribute to the development of high-quality software products?
**[January 2024]** 4  Explain the stages of ISO 9000 registration process.
**[July 2021]** b) Discuss 4 p's of software management concepts.
**[December 2019]** what is the effect of designing a prototype on the D RegNo.: I 2 3 4 possible ?
**[January 2024]** a) Identi$ the various types of risks in software project development 'b) Explain the Software Risk management process with the help of neat diagram.
**[July 2021]** What is a software process?
**[May 2023]** Which software process model allows risk management?
**[May 2024]** As you move outward along the process flow path of the spiral model, what can you say about the software that is being developed or maintained?
**[July 2021]** b) Explain the User interface design rules.
**[July 2021]** Explain the layered technology used in software engineering process.
**[July 2021]** (4) Discuss the specification and design aspects of software engineering.
**[May 2023]** What are the umbrella activities of generic soltware process framework?
**[January 2024]** a) Explain the role of people, product, process and project in Software engineering.
**[May 2023]** 7 a) What is incremental process mode?
**[December 2019]** b) Discuss 4 p's of software management concepts.

*(Note: Solutions to be generated/verified by agent)*


**[Sample Question] Briefly explain the different levels of the software design process. (4 Marks)**
**Solution:**
According to Pressman, software design is conducted at four levels of abstraction:
1. **Data Design:** Transforms the analysis domain models into physical data structures and database schemas.
2. **Architectural Design:** Defines the overall structure of the software, showing the major sub-systems and how they interact.
3. **Interface Design:** Details how the software communicates with human users, external systems, and internally between its own components.
4. **Component-Level Design:** The lowest level, where the internal algorithmic logic and local data structures of individual modules are specified before coding begins.

**[Sample Question] Explain any four fundamental design concepts in software engineering. (6 Marks)**
**Solution:**
1. **Abstraction:** Simplifying complexity by creating procedural abstractions (a named sequence of instructions like `calculateTax`) and data abstractions (a named collection of attributes).
2. **Information Hiding:** Designing modules so that their internal algorithms and local data structures are completely inaccessible and hidden from other modules, preventing unauthorized changes and localizing errors.
3. **Modularity:** Dividing monolithic software into separately named and addressable components (modules) to make the system intellectually manageable.
4. **Stepwise Refinement:** A top-down design strategy where a macroscopic statement of function is successively elaborated and broken down into smaller, highly detailed steps until it reaches the level of programming language statements.

**[Sample Question] What is meant by functional independence? How is it measured? (4 Marks)**
**Solution:**
Functional independence is a design concept achieved by developing modules with a "single-minded" function and an aversion to excessive interaction with other modules. It is the key to good design because it makes software easier to maintain, test, and develop in parallel without causing ripple-effect errors. It is measured using two qualitative criteria:
- **Cohesion:** An indication of the relative functional strength of a module (high cohesion is desired).
- **Coupling:** An indication of the relative interdependence among modules (low coupling is desired).
