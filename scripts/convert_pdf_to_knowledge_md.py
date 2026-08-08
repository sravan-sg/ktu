#!/usr/bin/env python3
"""
Convert PDF textbooks in textbooks/semester-<N>/<subject>/ to clean Markdown in notes/semester-<N>/<subject>/knowledge/
"""

import os
import subprocess
import re

TEXTBOOKS_DIR = "/home/sravan/ktu/textbooks/semester-6/computer-networks"
KNOWLEDGE_DIR = "/home/sravan/ktu/notes/semester-6/computer-networks/knowledge"

os.makedirs(KNOWLEDGE_DIR, exist_ok=True)

pdf_files = [f for f in os.listdir(TEXTBOOKS_DIR) if f.endswith(".pdf")]

for pdf in pdf_files:
    pdf_path = os.path.join(TEXTBOOKS_DIR, pdf)
    name_no_ext = os.path.splitext(pdf)[0]
    md_out_path = os.path.join(KNOWLEDGE_DIR, f"{name_no_ext}.md")
    txt_temp_path = os.path.join(KNOWLEDGE_DIR, f"{name_no_ext}.txt")
    
    print(f"Extracting text from {pdf} using pdftotext...")
    subprocess.run(["pdftotext", "-layout", pdf_path, txt_temp_path], check=True)
    
    print(f"Formatting extracted text into Markdown {md_out_path}...")
    with open(txt_temp_path, "r", encoding="utf-8", errors="ignore") as f_in:
        raw_text = f_in.read()
        
    # Clean up excessive blank lines and format headings
    lines = raw_text.splitlines()
    md_lines = [f"# Knowledge Base Note: {name_no_ext.replace('_', ' ')}\n"]
    
    blank_count = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            blank_count += 1
            if blank_count <= 2:
                md_lines.append("")
        else:
            blank_count = 0
            # Identify chapter or section headers
            if re.match(r'^(CHAPTER|SECTION|MODULE|\d+\.\d+)\b', stripped, re.IGNORECASE):
                md_lines.append(f"## {stripped}")
            else:
                md_lines.append(line)
                
    with open(md_out_path, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(md_lines[:15000])) # Write top 15k lines for AI readability
        
    if os.path.exists(txt_temp_path):
        os.remove(txt_temp_path)
        
    print(f"[COMPLETED] Converted {pdf} -> {md_out_path}")

print("All PDF textbooks converted successfully!")
