# Risk Management: Identification and Monitoring

## 1. Explanation
Risk management is an essential project management activity. A software risk is a potential problem that *might* happen in the future. If a risk becomes a reality, it causes unwanted consequences (schedule delays, budget overruns, or project failure). 

The goal of risk management is to identify these potential problems early, analyze their impact, and develop plans to avoid or mitigate them. It consists of three primary steps:

**1. Risk Identification:**
The systematic attempt to specify threats to the project plan. Risks are generally categorized into:
- **Project Risks:** Threaten the project plan (budget, schedule, personnel). E.g., The lead developer quits.
- **Technical Risks:** Threaten the quality and timeliness of the software. E.g., The chosen database technology cannot handle the required data load.
- **Business Risks:** Threaten the viability of the software to be built. E.g., A competitor releases a better product before yours is finished.

**2. Risk Projection (Analysis):**
Once identified, each risk is rated based on two factors:
- *Probability:* The likelihood that the risk will actually occur (e.g., 20%).
- *Impact:* The consequences if the risk occurs (e.g., Critical, Marginal, Negligible).

**3. Risk Mitigation, Monitoring, and Management (RMMM):**
- **Mitigation:** Proactive steps taken before the risk occurs to reduce its probability (e.g., cross-training staff so the project doesn't fail if the lead developer quits).
- **Monitoring:** Continuously tracking the project to see if the probability of a risk is increasing or if it has occurred.
- **Management (Contingency Plan):** The reactive steps taken *after* the risk becomes a reality to minimize the damage.

## 2. Example
Building a new AI Chatbot for a bank.
- **Identification (Technical Risk):** The third-party NLP API we plan to use might be too slow to process 1,000 concurrent chats.
- **Projection:** Probability = 40%. Impact = Critical (the system will crash).
- **Mitigation:** During the first week, build a quick prototype to benchmark the API's speed.
- **Monitoring:** Check the API response times every day during development.
- **Management:** If the API fails the benchmark, execute the contingency plan: switch to an in-house Python NLP library.

## 3. Applications & Use Cases
- **Spiral Process Model:** Risk management is literally baked into the Spiral software development model. The entire second quadrant of every iteration is dedicated exclusively to Risk Analysis before any engineering begins.
- **Space Exploration (NASA):** Software bugs in aerospace (like the Mars Climate Orbiter) destroy billions of dollars of hardware. Their risk identification and RMMM plans are exhaustive, utilizing techniques like Fault Tree Analysis to mitigate every conceivable software failure.

## 4. 3 Solved Numerical/Analytical Examples

**Example 1: Differentiate between a Risk and an Issue.**
*Analysis:* A risk is a *potential* future problem (e.g., "The server *might* run out of memory during launch"). An issue is a *current* problem that has already happened (e.g., "The server *has* run out of memory"). Risk management attempts to stop risks from evolving into issues.

**Example 2: How does Risk Mitigation differ from Risk Management?**
*Analysis:* Mitigation is proactive; you spend money and effort *now* to prevent the disaster from happening. Management (Contingency) is reactive; you accept the disaster might happen and prepare a safety net (like a data backup) to catch you when you fall.

**Example 3: What is the risk of having a high "Staff Turnover" rate?**
*Analysis:* This is a classic **Project Risk**. If highly skilled developers leave mid-project, they take the undocumented domain knowledge with them. This delays the schedule (violating Brooks' Law when new hires are brought on) and increases the budget due to recruiting and training costs.

## 5. Previous Year Questions & Solutions

### Actual University Questions:
**[January 2024]** How risks are monitored and managed by project Managers?
**[December 2019]** a) Discuss Risk management activities in detail.
**[January 2024]** Explain different activities (5) involved in configuration management.
**[May 2019]** Explain different activities involved in configuration management.
**[May 2023]** Is it possible to prioritize risk?
**[December 2019]** b) Explain different project scheduling techniques a) Write the different activities of software project management.
**[May 2019]** b) What are risk management activities?
**[January 2024]** b) What is risk identification?
**[May 2024]** (4) 16 ' a) What is risk projection?
**[May 2023]** Explain scM (Software configuration Management) activities in detail.
**[May 2023]** Discuss 4P's of Software Project Management concept What are risk management activities?
**[July 2021]** Duration: 3 Hours Marks (3) (3) (3) (3) (4) (s) help of a  (4) a) b) a) b) Suppose you were to plan to undertake the development of a product with a large (5) number of technical as well as customer related risks, which life cycle model would you adopt?
**[July 2021]** (4) b) Discuss Risk management activities in detail.
**[July 2021]** b) Discuss 4 p's of software management concepts.
**[May 2019]** Is it possible to prioritize risk?
**[July 2021]** b) Explain software configuration management activities.
**[May 2024]** What are the risk orojection activities performed by (5) the project planner along with other rnanagers and technical statr?
**[May 2019]** a) What is meant by software configuration management?
**[May 2019]** Explain different types of software risk.
**[December 2019]** b) Explain software configuration management activities.
**[January 2024]** (6) a) Explain the term software configuration management?
**[January 2024]** a) Identi$ the various types of risks in software project development 'b) Explain the Software Risk management process with the help of neat diagram.
**[May 2023]** Which software process model allows risk management?
**[May 2019]** b) Suppose you were to plan to undertake the development of a product with  (5) a large number of technical as well as customer related risks, which life cycle model would you adopt?
**[May 2024]** b) Explain different categories of risk.
**[May 2019]** a) What is risk?
**[December 2019]** b) Discuss 4 p's of software management concepts.

*(Note: Solutions to be generated/verified by agent)*


**[December 2019] What are the steps in software risk management? (4 Marks)**
**Solution:**
Software risk management consists of three primary steps:
1. **Risk Identification:** Brainstorming and categorizing potential future problems that could derail the project. These are categorized into Project risks (schedule/budget), Technical risks (design/implementation failures), and Business risks (market viability).
2. **Risk Projection (Analysis):** Evaluating each identified risk based on its *Probability* (likelihood of occurrence) and its *Impact* (severity of consequences). This helps prioritize which risks require immediate attention.
3. **Risk Mitigation, Monitoring, and Management (RMMM):** Developing a proactive strategy to reduce the probability of the risk (Mitigation), continuously tracking factors that indicate a risk is becoming likely (Monitoring), and preparing a contingency plan to execute if the risk actually occurs (Management).

**[Sample Question] Differentiate between project risks and technical risks. (2 Marks)**
**Solution:**
**Project Risks** threaten the project plan itself; they involve issues with budget, scheduling, personnel, and resources (e.g., running out of funding or the lead architect resigning).
**Technical Risks** threaten the quality and functionality of the software being built; they involve issues with complex design, unproven technology, or ambiguous requirements (e.g., the chosen database architecture cannot scale to meet user demand).
