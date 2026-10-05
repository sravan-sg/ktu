# Module 1 Revision Notes

## 1. Quick Summary of Key Concepts
- **Software Engineering**: A systematic, disciplined, quantifiable approach to software development, operation, and maintenance. It combats the "software crisis" where ad-hoc coding caused cost overruns and failures.
- **Scope**: Covers Historical, Economic, Maintenance (fixing and adapting over time), Specification, Design, and Team Programming aspects.
- **Layered Technology**: Built on four layers: 
  1. Quality Focus (Bedrock)
  2. Process (Framework & KPAs)
  3. Methods (Technical how-to)
  4. Tools (Automation, e.g., CASE tools)
- **Waterfall Model**: Linear, sequential, documentation-heavy. Requires strict upfront requirements. Fails with changing requirements.
- **Incremental Model**: Delivers working software in iterative "increments". Reduces risk by delivering core features early.
- **Prototyping Model**: Builds a quick mock-up to clarify ambiguous requirements before actual engineering begins. Reduces long-term costs by preventing incorrect architecture.
- **Spiral Model**: An evolutionary model uniquely driven by **Risk Analysis** at every loop. Combines prototyping with waterfall control.

## 2. Important Formulas or Algorithms
- *No strict mathematical formulas in this module.* However, the **COCOMO** effort estimation model (introduced here but detailed in Module 3) uses formulas to estimate cost. In Module 1, understand the economic principle: **The cost of fixing a defect increases exponentially the later it is discovered in the SDLC.**

## 3. High-Yield PYQ Topics
- **Process Model Comparisons:** (Highly testable!)
  - Waterfall vs. Incremental (rigid vs. flexible delivery)
  - Characteristics of Waterfall (Linear, no backtracking, late testing)
- **Spiral Model Diagram:** Always draw the 4 quadrants (Planning, Risk Analysis, Engineering, Evaluation) and explicitly mention that it is the only model driven primarily by *Risk Analysis*.
- **Layered Technology:** Memorize the 4 layers (Quality, Process, Methods, Tools) from bottom to top. 
- **Prototyping Impact:** Know that prototyping *adds* early costs but drastically *reduces* overall project costs by preventing requirement errors.

## 4. Common Pitfalls/Mistakes
- **Confusing Spiral with Incremental:** Both use loops, but Spiral is strictly about analyzing risk at each loop before deciding to proceed, whereas Incremental is about delivering partial working versions of the software to the client.
- **Misunderstanding Maintenance:** Students often think maintenance is just "bug fixing". It also heavily includes adapting the software to new operating systems (adaptive) and restructuring code to prevent future decay (preventive).
- **Prototyping Throwaway Code:** A common exam trick asks for the disadvantage of prototyping: remind the examiner that "throwaway" prototype code is often dangerously reused as production code by rushed developers.
