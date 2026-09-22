---
name: scrape-pyqs
description: Actively connect to the internet to search for, download, extract text from, and verify Previous Year Question (PYQ) papers for a given subject. Use this when the user asks to fetch, scrape, or download question papers from the web.
---

# Scrape Previous Year Question Papers (PYQs)

Automatically search the internet for university question papers, download the PDFs, extract their text, and mathematically verify their headers against official KTU subject codes and titles.

## Steps

### 1. Execute the Scraper Pipeline

When the user asks to scrape or download previous year question papers, execute the python script located at `scripts/pyq_scraper_pipeline.py`.

```bash
venv/bin/python3 scripts/pyq_scraper_pipeline.py
```

### 2. How the Pipeline Works

The script will automatically perform the following steps for all subjects defined in `syllabus/` and `notes/`:
1. **Active Internet Search:** It queries search engines (like DuckDuckGo HTML) for `KTU <Subject Code> <Subject Name> previous question paper filetype:pdf`.
2. **Download & Extraction:** It downloads potential PDF matches and uses `PyMuPDF` (`fitz`) to extract the raw text from the first two pages.
3. **Strict Verification:** It mathematically verifies the extracted text header (first 30 lines) against the official University Name, Subject Code, and Subject Title.
4. **Standardization:** If it passes the strict check, the paper is renamed to `Month_Year.txt` and saved in `previous-question-papers/<semester>/<subject>/`. Staging files that fail verification are automatically cleaned up.

### 3. Review the Output

After the script completes, review the summary logs and inform the user how many verified PYQs were successfully saved for their subject and how many failed the strict watermarking/tampering verification check.
