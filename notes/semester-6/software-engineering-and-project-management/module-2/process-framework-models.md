# Process Framework Models: CMM and ISO 9000

## 1. Explanation
A process framework establishes the foundation for a complete software engineering process by identifying a small number of framework activities that are applicable to all software projects, regardless of their size or complexity. Two of the most globally recognized process frameworks are the **Capability Maturity Model (CMM)** and **ISO 9000**.

**Capability Maturity Model (CMM):** Developed by the Software Engineering Institute (SEI), CMM provides a measure of the global effectiveness of a company's software engineering practices. It defines 5 levels of maturity:
1. **Initial (Ad-hoc):** The software process is characterized as ad-hoc, and occasionally even chaotic. Few processes are defined, and success depends on individual heroic effort.
2. **Repeatable:** Basic project management processes are established to track cost, schedule, and functionality. The necessary process discipline is in place to repeat earlier successes.
3. **Defined:** The software process for both management and engineering activities is documented, standardized, and integrated into a standard software process for the organization.
4. **Managed:** Detailed measures of the software process and product quality are collected. Both the software process and products are quantitatively understood and controlled.
5. **Optimizing:** Continuous process improvement is enabled by quantitative feedback from the process and from piloting innovative ideas and technologies.

**ISO 9000:** A generic set of standards published by the International Organization for Standardization (ISO) that apply to any industry, not just software. In software, ISO 9001 is the standard used for quality assurance in design, development, production, installation, and servicing. It requires a company to document its quality system, adhere to those documents, and prove adherence through external audits.

## 2. Example
- **CMM Level 1 vs. Level 3:** A Level 1 company might successfully build an app because they hired a "rockstar" developer. When that developer leaves, the next project fails. A Level 3 company has a standardized "Defined" process manual; any new developer can read the manual and produce consistent results.
- **ISO 9000 Certification:** A software vendor wants to sell a defense system to the European Union. The EU requires ISO 9001 certification. The vendor must hire an external auditor to verify that they document every single code review and test case according to their own internal quality manual.

## 3. Applications & Use Cases
- **Government Contracts:** The US Department of Defense often mandates that software contractors be evaluated at CMMI (the modern successor to CMM) Level 3 or higher before they are allowed to bid on military contracts.
- **Global Trade & Supply Chain:** ISO 9000 is heavily used in global B2B transactions. If a German automaker buys software from an Indian IT firm, ISO 9001 certification provides international baseline confidence in the IT firm's quality management system.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Contrast CMM and ISO 9000 in scope.**
*Analysis:* ISO 9000 is a generic quality management standard applicable to manufacturing a toaster or writing software; it simply asks, "Are you doing what you say you do?" CMM is highly specific to the software industry, explicitly grading *how well* the organization engineers software across 5 progressive levels.

**Example 2: An organization tracks precise metrics (defects per KLOC) and uses statistics to control process variation. What CMM level are they?**
*Analysis:* They are at **Level 4 (Managed)**. While Level 3 defines the process, Level 4 is characterized by *quantitative* management and statistical control over those processes.

**Example 3: Does ISO 9000 guarantee high-quality software?**
*Analysis:* No. ISO 9000 guarantees that the organization follows a consistent, documented process. If a company's documented process is to write bad code and explicitly document that it is bad, they could theoretically still pass an ISO audit (they followed their documented procedure). It guarantees consistency, not necessarily engineering excellence.

## 5. Previous Year Questions & Solutions

**[December 2019] Describe the different levels of Capability Maturity Model (CMM). (5 Marks)**
**Solution:**
The Capability Maturity Model (CMM) evaluates an organization's software process maturity across 5 levels:
1. **Initial (Level 1):** The process is ad-hoc, chaotic, and relies entirely on individual effort ("heroics"). Success is not easily repeatable.
2. **Repeatable (Level 2):** Basic project management tracking is established. The discipline is in place to repeat previous successes on similar projects.
3. **Defined (Level 3):** Management and engineering processes are fully documented, standardized, and integrated across the entire organization.
4. **Managed (Level 4):** The organization collects detailed quantitative metrics on process and product quality. The process is statistically controlled.
5. **Optimizing (Level 5):** The organization uses the quantitative feedback to engage in continuous process improvement, aggressively pursuing new tools and innovative methodologies to reduce defect rates.
