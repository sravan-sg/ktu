# Phases in Software Development Requirement Analysis

## 1. Explanation
Requirement analysis is a software engineering task that bridges the gap between system-level requirements engineering and software design. It allows the systems engineer to specify software function and performance, indicates software's interface with other system elements, and establishes constraints.

The requirement analysis process is typically divided into specific phases:
1. **Problem Recognition:** The analyst studies the system specification (if one exists) and the software project plan. The goal is to understand the system context and the basic problem domain.
2. **Evaluation and Synthesis:** The analyst evaluates the flow and structure of information, defines all software functions, and establishes system interface characteristics. If the problem is complex, it is partitioned (synthesized) into smaller, manageable sub-problems.
3. **Modeling:** The analyst creates models (e.g., Data Flow Diagrams, Entity-Relationship Diagrams) to better understand the data and control flow, functional processing, and operational behavior.
4. **Specification:** All the gathered and modeled data is formalized into a comprehensive Software Requirements Specification (SRS) document.
5. **Review:** The SRS is reviewed by the customer, developers, and quality assurance teams to validate that it correctly and completely represents the software to be built.

## 2. Example
Imagine analyzing requirements for an ATM network.
- **Problem Recognition:** Understanding that the system needs to dispense cash, check balances, and connect to multiple banks.
- **Evaluation/Synthesis:** Breaking down the "dispense cash" function into sub-functions: read card -> verify PIN -> check balance -> dispense -> print receipt.
- **Modeling:** Drawing a State Transition Diagram showing how the ATM moves from "Idle" to "Verifying PIN" to "Dispensing".
- **Specification:** Writing down the exact rule: "If PIN is entered incorrectly 3 times, swallow card."
- **Review:** Showing the models and specification to the bank managers for approval.

## 3. Applications & Use Cases
- **Safety Critical Medical Devices:** In a pacemaker, the requirement analysis phases are strictly audited. The evaluation phase must map every possible heart rhythm input to a specific electrical output, modeled extensively before any C code is written.
- **E-Commerce Platforms:** Analysis must partition massive problems (like Amazon's checkout system) into smaller modules (inventory check, payment gateway, shipping calculation) during the synthesis phase.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Why is "Partitioning" (Synthesis) necessary?**
*Analysis:* The human brain can only hold about 7 independent pieces of information at once. A system like an ERP is too complex to analyze as a monolith. Partitioning horizontally (breaking system into independent features) and vertically (breaking features into layers of detail) makes the analysis cognitively manageable.

**Example 2: What is the purpose of the Modeling phase?**
*Analysis:* Textual descriptions are often ambiguous. Modeling provides a mathematical and visual representation of data flow (using DFDs) and behavioral state (using STDs) which removes ambiguity and provides a direct blueprint for the design phase.

**Example 3: Describe the output of the Specification phase.**
*Analysis:* The output is the Software Requirements Specification (SRS). It acts as the legal contract between the client and developer, defining exactly what will be built, constraints (like response time < 2 seconds), and acceptance criteria.

## 5. Previous Year Questions & Solutions

**[Sample Question] List the phases in software development requirement analysis. (3 Marks)**
**Solution:**
The requirement analysis process consists of five distinct phases:
1. **Problem Recognition:** Understanding the system context, constraints, and business goals.
2. **Evaluation and Synthesis:** Assessing information flow and breaking down (partitioning) complex problems into smaller, manageable modules.
3. **Modeling:** Creating graphical models (like Data Flow Diagrams and State Transition Diagrams) to map out functional behavior and data structures.
4. **Specification:** Formalizing all analyzed requirements into a comprehensive Software Requirements Specification (SRS) document.
5. **Review:** Validating the specification with stakeholders to ensure accuracy, consistency, and completeness before design begins.
