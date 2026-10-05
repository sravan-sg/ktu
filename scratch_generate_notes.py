import os

base_path = "/home/sravan/ktu/notes/semester-6/software-engineering-and-project-management"
modules = {
    1: ["Introduction to software engineering", "Scope of software engineering", "Software engineering a layered technology", "Software process models"],
    2: ["Process Framework Models", "Phases in Software development requirement analysis", "Requirements elicitation for software", "Analysis principles", "Software prototyping", "Specification"],
    3: ["Planning phase", "Empirical estimation models", "Staffing and personal planning", "Design phase", "Effective modular design", "Top down bottom up strategies stepwise refinement"],
    4: ["Coding", "Testing fundamentals", "Testing strategies"],
    5: ["Maintenance", "Risk management", "Project Management concept"],
    6: ["Project scheduling and tracking", "Software configuration management", "User interface design rules", "Computer aided software engineering tools"]
}

template = """# {title}

> **STRICT LOCAL KNOWLEDGE GROUNDING ENFORCED:** The textbooks for this subject are strictly copyrighted and require manual purchase. Because no markdown reference materials exist in `knowledge/`, the contents of this file have been withheld to strictly prevent external AI hallucination according to the repository rules.

## 1. Explanation
[Content Pending Textbook Ingestion]

## 2. Example
[Content Pending Textbook Ingestion]

## 3. Applications & Use Cases
[Content Pending Textbook Ingestion]

## 4. 3 Solved Numerical/Analytical Examples
[Content Pending Textbook Ingestion]

## 5. Previous Year Questions & Solutions
[Content Pending Textbook Ingestion]
"""

detailed_template = """# Module {mod} Detailed Notes

## Topics
{links}
"""

revision_template = """# Module {mod} Revision Notes

[Content Pending Textbook Ingestion]
"""

readme_content = """# CS308 — Software Engineering and Project Management

## Modules

{mod_links}
"""

mod_links = ""

for mod, topics in modules.items():
    mod_dir = os.path.join(base_path, f"module-{mod}")
    os.makedirs(mod_dir, exist_ok=True)
    
    links = ""
    for topic in topics:
        kebab_case = topic.lower().replace(" ", "-").replace(",", "")
        file_path = os.path.join(mod_dir, f"{kebab_case}.md")
        with open(file_path, "w") as f:
            f.write(template.format(title=topic))
        links += f"- [{topic}]({kebab_case}.md)\n"
        
    with open(os.path.join(mod_dir, "detailed-notes.md"), "w") as f:
        f.write(detailed_template.format(mod=mod, links=links))
        
    with open(os.path.join(mod_dir, "revision-notes.md"), "w") as f:
        f.write(revision_template.format(mod=mod))
        
    mod_links += f"### Module {mod}\n- [Detailed Notes](module-{mod}/detailed-notes.md)\n- [Revision Notes](module-{mod}/revision-notes.md)\n\n"

with open(os.path.join(base_path, "README.md"), "w") as f:
    f.write(readme_content.format(mod_links=mod_links))

with open(os.path.join(base_path, "Correction_Log.md"), "w") as f:
    f.write("# Correction Log\n\n- Scaffolded module folders 1-6.\n- Enforced strict local knowledge grounding by withholding content generation due to missing textbooks.\n")

with open(os.path.join(base_path, "Syllabus_Gap_Analysis.md"), "w") as f:
    f.write("# Syllabus Gap Analysis\n\n- **100% of topics scaffolded** from the syllabus.\n- **0% of topics completed** due to missing local textbooks, enforcing the hallucination-prevention rule.\n")
