# Analysis Principles

## 1. Explanation
Over the past decades, several different modeling methods (like Structured Analysis and Object-Oriented Analysis) have been developed. Regardless of the specific method used, Roger Pressman defines a set of fundamental **Analysis Principles** that every software engineer must follow when modeling requirements:

1. **The Information Domain must be represented and understood:** Software fundamentally transforms data. The analysis must define the data coming in, the data going out, and the data stored inside the system.
2. **Models that depict software function and behavior must be developed:** The analysis must show what the software *does* (its functions) and how it *reacts* to external events (its behavior/state).
3. **The models must be partitioned:** Complex problems must be divided hierarchically. The analysis should start at a high-level overview and systematically drill down into detailed, granular sub-functions (top-down refinement).
4. **The analysis process should move from essential information toward implementation detail:** Analysis should focus on *what* the system needs to do, deliberately ignoring *how* it will be coded (which is reserved for the design phase).

## 2. Example
Applying the principles to a Smart Home Thermostat:
- **Principle 1 (Information Domain):** Inputs = Room temperature, Target temperature. Outputs = HVAC control signal.
- **Principle 2 (Behavior):** Model the states. If current temp < target temp, transition to "Heating" state.
- **Principle 3 (Partitioning):** Don't analyze the whole house at once. Partition it into "Temperature Sensing", "User UI", and "HVAC Actuator" modules.
- **Principle 4 (Essential vs Implementation):** State "The system must communicate with the user's phone over a network." Do *not* state "The system will use a Node.js WebSocket server" (that is a design choice).

## 3. Applications & Use Cases
- **Structured Analysis:** Uses these principles to build Data Flow Diagrams (DFDs). Principle 1 is handled by the data dictionaries, Principle 2 by the processes, and Principle 3 by leveling the DFDs from Level 0 to Level 2.
- **Object-Oriented Analysis:** Uses these principles to build UML models. Principle 1 is handled by Class diagrams (attributes), Principle 2 by Sequence diagrams (methods), and Principle 3 by breaking the system into Packages.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why must the analysis focus on the "what" rather than the "how" (Principle 4)?**
*Analysis:* If an analyst dictates the "how" (e.g., specifying that a specific SQL database must be used to sort data), they prematurely constrain the software designers. The designers might know a faster NoSQL approach, but they are locked in by a poor analysis document. Analysis must remain implementation-independent.

**Example 2: How does a Data Flow Diagram (DFD) satisfy Principle 3 (Partitioning)?**
*Analysis:* A DFD strictly enforces hierarchical partitioning. It starts with a Level 0 Context Diagram showing the entire system as a single bubble. That bubble is then partitioned into a Level 1 diagram with 4-5 major sub-bubbles. Each of those is partitioned into Level 2 diagrams, allowing deep understanding without overwhelming complexity.

**Example 3: Describe the components of the Information Domain (Principle 1).**
*Analysis:* The information domain contains three views:
1. *Information content and relationships:* The data objects and how they link (e.g., Customer has many Orders).
2. *Information flow:* How data moves through the system (e.g., Input -> Process -> Output).
3. *Information structure:* The internal organization of the data (e.g., array, tree, or relational table).

## 5. Previous Year Questions & Solutions

**[Sample Question] Discuss the core analysis principles in software engineering. (5 Marks)**
**Solution:**
Regardless of the specific modeling methodology used (structured or object-oriented), software requirement analysis is guided by four fundamental principles:
1. **Represent the Information Domain:** The analyst must deeply understand and model the data inputs, outputs, and internal data stores of the system, recognizing that software's primary job is data transformation.
2. **Model Function and Behavior:** The analysis must clearly define the functions that transform data and model the states/behavior of the software when subjected to external events.
3. **Hierarchical Partitioning:** The problem must be subdivided. Analysts must use a top-down approach, starting with a macro-level view of the system and progressively partitioning it into detailed, manageable sub-components.
4. **Separate "What" from "How":** The analysis phase must focus exclusively on *what* the system is required to do logically. It must avoid detailing *how* the system will be implemented technically (e.g., avoiding specifying programming languages or database vendors), leaving those decisions for the design phase.
