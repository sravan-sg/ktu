---
name: extract-textbooks-to-txt
description: Extracts and converts all textbooks and reference PDFs in a subject's textbooks/ directory into raw .txt files using PyMuPDF (fitz) to ensure content is fully readable. Use when the user requests converting textbooks to txt or ensuring all reference PDFs are extracted.
---

# Extract Textbooks to TXT

A fallback and strict extraction skill that forcibly converts all downloaded or manually provided PDF textbooks/reference materials into raw `.txt` files. This is highly useful when native markdown conversion (`prepare-knowledge`) fails due to size limits, timeouts, or strict gating on complex PDF layouts.

## Steps

### 1. Locate Target Directories
Find the subject's `textbooks/` directory (e.g. `textbooks/semester-6/software-engineering-and-project-management/`).

### 2. Verify PyMuPDF (fitz) Installation
Ensure `PyMuPDF` is installed in the local virtual environment (`venv/bin/pip install PyMuPDF`).

### 3. Run Python Extraction Script
Write and execute a Python script that iterates through every `.pdf` file in the subject's `textbooks/` folder.
- Use `fitz.open()` to read each PDF.
- Iterate through every page using `page.get_text()`.
- Save the concatenated text into a `.txt` file with the exact same base name as the PDF.
- Save the `.txt` file either alongside the original PDF in the `textbooks/` directory or inside the `knowledge/` directory, depending on the workspace standard.

### 4. Create an Index
Once extraction is complete, automatically update the `textbooks/README.md` or `knowledge/README.md` file to reflect that raw `.txt` equivalents of the reference materials are now available.

### 5. Fallback for Scanned Books
If `PyMuPDF` extracts zero characters (meaning the PDF is purely a scanned image with no text layer), the agent should explicitly inform the user that OCR (Optical Character Recognition) is required or a native PDF version must be provided.
