# Software Prototyping

## 1. Explanation
Software prototyping is a requirement analysis and design technique where a working, preliminary model of the software (or critical subsets of it) is rapidly built and deployed for customer evaluation. It exists to solve a fundamental psychological barrier in software engineering known as the **"Problem of Understanding"** or the **IKIWISI ("I'll Know It When I See It") syndrome**.

Customers often have a legitimate business need but are completely incapable of defining the granular, technical data transformations required. Conversely, developers understand the technical architecture but cannot read the customer's mind. Text-based requirement documents (like an SRS) often fail to bridge this gap because human beings are poor at visualizing dynamic software from static text. A prototype bridges this gap by acting as an executable specification—a tangible model that the customer can interact with.

**Types of Prototypes:**
- **Throwaway (Rapid) Prototyping:** The prototype is built purely as a communication tool. The engineer uses "quick-and-dirty" code, ignoring performance, security, and architectural best practices to rapidly demonstrate a UI flow or a complex algorithm. **Crucially, the prototype is literally thrown away** once the requirements are clarified. The final production system is engineered from scratch. This prevents the "spaghetti code" of the prototype from infecting the production codebase.
- **Evolutionary Prototyping:** The prototype is built with rigorous, production-level engineering practices from day one. After customer feedback, it is iteratively refined and expanded. Instead of being discarded, the prototype *evolves* directly into the final production system. This requires immense architectural foresight to prevent the system structure from degrading as endless ad-hoc changes are requested.

## 2. Example
To understand the architectural distinction, consider a startup building a complex Drone Delivery routing algorithm:

- **Throwaway Approach:** The engineering team writes a quick, inefficient Python script to simulate drone paths on a 2D grid just to prove to the investors that the math works and to get feedback on the routing rules. The script takes 5 minutes to calculate a route (which is unacceptable for production). The investors approve the logic. The engineers delete the Python script and build the final, highly-optimized, multi-threaded engine in C++.
- **Evolutionary Approach:** The team uses a robust Java framework and builds a highly structured, scalable web interface with a basic version of the routing algorithm. The investors use it, ask for a "weather avoidance" feature, and the team cleanly integrates this new module into the existing architecture. The system grows, iteration by iteration, until it is deployed to production without ever being discarded.

## 3. Applications & Use Cases
- **UI/UX Heavy Applications:** Consumer-facing apps (like Instagram or Uber) rely heavily on throwaway prototyping because user interaction and visual flow are the most critical requirements, and they are impossible to fully specify in a text document.
- **Algorithmic Feasibility:** If a company wants to build a new AI-driven stock trading bot, they will build a mathematical prototype (often in a tool like MATLAB or Python) to test if the predictive algorithm actually works before investing millions in building the low-latency C++ trading platform.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why is the "Throwaway" paradigm so difficult for management to accept?**
*Analysis:* Management often views code as a direct asset. When they see a working throwaway prototype, they assume the project is 90% done and demand its release. The engineer must fight to discard it because releasing quick-and-dirty prototype code leads to catastrophic maintenance costs, security vulnerabilities, and unscalable architecture.

**Example 2: How does Prototyping differ from the standard Waterfall requirements phase?**
*Analysis:* In Waterfall, requirements are assumed to be static, and they are completely documented in a massive text file before any code is written. Prototyping admits that requirements are volatile and uses actual, executable software (rather than text documents) to elicit the final requirements.

**Example 3: When should a prototype *not* be used?**
*Analysis:* Prototyping is unnecessary and wasteful if the problem domain is completely understood, highly regulated, and identical to past projects (e.g., building a standard payroll calculator for the 10th time). In such cases, standard analysis is sufficient.

## 5. Previous Year Questions & Solutions

**[December 2019] Discuss the prototyping model. What is the effect of designing a prototype on the overall cost of the project? (4 Marks)**
**Solution:**
The Prototyping model is a software process model that focuses on rapidly building a working, preliminary version of the software. It is used to clarify ambiguous requirements, test complex algorithms, and allow the customer to interact with the interface before heavy engineering begins. 
**Effect on Overall Cost:**
Designing a prototype incurs a short-term upfront cost (time and effort spent building something that might be thrown away). However, it drastically *reduces* the overall cost of the project in the long run. By validating requirements visually with the customer early on, it prevents the development team from engineering the wrong system, thereby avoiding exponentially expensive rework, redesign, and patching costs during the later testing and maintenance phases.
