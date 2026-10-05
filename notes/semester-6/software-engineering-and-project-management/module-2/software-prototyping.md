# Software Prototyping

## 1. Explanation
Software prototyping is a requirement analysis and design technique where a working, preliminary model of the software (or parts of it) is rapidly built and deployed for customer evaluation. It is used primarily to mitigate the "Problem of Understanding" during requirement elicitation.

Prototyping serves as a mechanism for identifying software requirements. If a customer has a legitimate need but is unsure of the details, or if the developer is unsure of the underlying algorithm's efficiency, a prototype bridges the gap.

**Types of Prototypes:**
- **Throwaway Prototyping:** The prototype is built quickly using "quick-and-dirty" code just to demonstrate the UI or a concept. Once the requirements are clarified, the prototype is literally thrown away, and the actual system is engineered from scratch.
- **Evolutionary Prototyping:** The prototype is built with robust engineering practices from day one. After customer feedback, it is iteratively refined and evolved until it becomes the final production system.

## 2. Example
- **Throwaway:** An engineer builds a mock-up of a mobile banking app using Figma or a raw HTML page. The buttons work, but they just link to static images. The customer clicks through it, realizes they want the "Transfer" button on the home screen, and approves the layout. The HTML is discarded, and the real app is built in Swift/Kotlin.
- **Evolutionary:** A developer writes a Python script to analyze sensor data. It works, but it's slow. After getting feedback from scientists, the developer refactors the same script, adds multithreading, and deploys it as the final product.

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
