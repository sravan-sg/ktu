# Overview and Types of Maintenance

## 1. Explanation
Software maintenance is the final, longest, and arguably most expensive phase of the software development lifecycle. Once software is delivered and deployed, it does not remain static. It must evolve to meet changing business needs, correct latent errors, and adapt to new hardware or operating systems. 

Historically, maintenance consumes up to **70-80%** of total project lifecycle costs. Therefore, designing software for maintainability (using high cohesion, low coupling, and comprehensive documentation) during the initial design phase is economically critical.

**Types of Software Maintenance:**
According to Lientz and Swanson, maintenance activities are categorized into four distinct types:
1. **Corrective Maintenance:** The reactive modification of a software product performed after delivery to correct discovered problems (fixing bugs).
2. **Adaptive Maintenance:** Modification of a software product performed after delivery to keep a software program usable in a changed or changing environment (e.g., updating an app to work on a new version of iOS).
3. **Perfective Maintenance:** Modification of a software product after delivery to improve performance or maintainability, or to add new features requested by users. (This consumes the majority of maintenance effort).
4. **Preventive Maintenance:** Also known as Software Reengineering. Modifying software to detect and correct latent faults *before* they become effective faults. It involves restructuring code and updating documentation to prevent future deterioration.

## 2. Example
Imagine maintaining a web-based Payroll System:
- **Corrective:** An employee reports that their overtime pay was calculated incorrectly. The developer patches the calculation bug.
- **Adaptive:** The company upgrades its database servers from MySQL 5.7 to MySQL 8.0. The developer modifies the SQL queries in the code to ensure they don't break on the new database.
- **Perfective:** The HR department requests a new button to export payroll data directly to a PDF. The developer adds this new feature.
- **Preventive:** The developer notices the 10-year-old authentication module is written in deprecated, messy "spaghetti code." They completely rewrite (refactor) it to be clean and modular, preventing a future catastrophic security breach.

## 3. Applications & Use Cases
- **Legacy Systems:** Banks and airlines run COBOL mainframes built in the 1980s. They employ massive teams dedicated entirely to **Preventive and Adaptive Maintenance** to keep these critical systems running in the modern era of cloud computing.
- **Mobile Applications:** Mobile apps require constant **Adaptive Maintenance**. Whenever Apple or Google releases a major OS update (like iOS 17), developers must update their apps to comply with new privacy APIs or screen sizes.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why does software require maintenance if it doesn't physically "wear out"?**
*Analysis:* Unlike a car engine, software doesn't rust. It deteriorates logically. As adaptive and perfective maintenance is applied over the years, the original pristine architecture gets hacked, patched, and mutated. This "software entropy" makes the code increasingly fragile until preventive maintenance is performed to restore its structural integrity.

**Example 2: Which type of maintenance consumes the most resources?**
*Analysis:* **Perfective maintenance** consumes the vast majority of resources (often >50% of the maintenance budget). Once a system is delivered, users inevitably want it to do more than originally specified. Adding new features to an existing, live architecture is extremely difficult and time-consuming.

**Example 3: Analyze the ROI of Preventive Maintenance.**
*Analysis:* Preventive maintenance (refactoring) adds zero new features for the end-user, making it hard to justify to management. However, its ROI is massive in the long term. If a module is not refactored, the cost to add a new feature next year might be $10,000 due to complexity. If refactored today for $2,000, adding that feature next year might only cost $1,000.

## 5. Previous Year Questions & Solutions

**[Sample Question] What are the different types of software maintenance? (4 Marks)**
**Solution:**
Software maintenance is broadly categorized into four types:
1. **Corrective Maintenance:** Fixing latent errors or bugs discovered in the software after it has been deployed to the end users.
2. **Adaptive Maintenance:** Modifying the software so it can continue to operate in a changed hardware or software environment (e.g., upgrading to support a new operating system or database).
3. **Perfective Maintenance:** Enhancing the software by adding new features, improving performance, or upgrading the UI based on new user requests. This is the most resource-intensive type.
4. **Preventive Maintenance:** Restructuring or rewriting existing code (Software Reengineering) to make it more maintainable and prevent future logical deterioration, without changing its external behavior.

**[Sample Question] Why is software maintenance expensive? (2 Marks)**
**Solution:**
Software maintenance is expensive because it requires engineers to understand and safely modify code they likely did not write. If the original software was poorly designed (low cohesion, high coupling, missing documentation), every modification carries a high risk of breaking other parts of the system, requiring extensive regression testing and reverse engineering.
