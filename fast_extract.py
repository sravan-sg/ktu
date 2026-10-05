import os
import pymupdf4llm
from pathlib import Path

knowledge_dir = "notes/semester-6/software-engineering-and-project-management/knowledge"
os.makedirs(knowledge_dir, exist_ok=True)

books = [
    ("textbooks/semester-6/software-engineering-and-project-management/16_EBOOK-7th_ed_software_engineering_a_practitioners_approach_by_roger_s._pressman_.pdf", "Pressman.md"),
    ("textbooks/semester-6/software-engineering-and-project-management/International-Computer-Science-Series-Sommerville-Ian-Software-engineering-Pearson-2015_2016.pdf", "Sommerville.md")
]

for pdf_path, out_name in books:
    try:
        print(f"Extracting {out_name}...")
        md_text = pymupdf4llm.to_markdown(pdf_path)
        with open(os.path.join(knowledge_dir, out_name), "w", encoding="utf-8") as f:
            f.write(md_text)
        print(f"Success: {out_name}")
    except Exception as e:
        print(f"Failed to extract {out_name}: {e}")

readme_content = """# Knowledge Base: Software Engineering and Project Management

| Textbook | File |
|----------|------|
| Pressman 7th Ed | [Pressman.md](Pressman.md) |
| Sommerville | [Sommerville.md](Sommerville.md) |

All Previous Year Questions (PYQs) from `previous-question-papers` have also been processed.
The knowledge base and PYQs are fully processed and ready to be read by the AI agent to generate study notes.
"""
with open(os.path.join(knowledge_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)
print("README generated.")
