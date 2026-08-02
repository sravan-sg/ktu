---
name: download-references
description: Find and download reference textbooks and reference documents from the internet for a given subject and store them in the textbooks folder inside the subject directory. Use when the user requests downloading or fetching textbooks, reference books, or reference documents for a course or syllabus.
---

# Download Reference Materials

Automatically locate, download, and index the textbook and reference materials mentioned in a subject's `syllabus.md`.

## Steps

### 1. Locate and Parse the Syllabus

1. Locate the subject's directory: `notes/<semester>/<subject>/` (e.g., `notes/semester-6/design-and-analysis-of-algorithms/`).
2. Read the `syllabus.md` file in that directory.
3. Locate the `## Textbooks` and `**References**` (or `## References`) sections.
4. Extract the title, author(s), edition/year, and publisher for each item.

### 2. Create the Destination Directory

Ensure that the target root directory `textbooks/semester-<number>/<subject-name>/` (e.g., `textbooks/semester-6/design-and-analysis-of-algorithms/`) exists. If not, create it.

### 3. Check Local Curated Indexes First

Before searching the web, consult the pre-indexed repository resources located under `.agents/skills/download-references/resources/`:

#### A. yacoubasawadogo/computer-science-books Index
1. Read `.agents/skills/download-references/resources/yacouba_index.json`.
2. Search for the book title or authors in the `"path"` fields.
3. If a match is found:
   - Check the file `size` in the index metadata.
   - If the size is small (~132 bytes) or it contains a Git LFS pointer structure, resolve the real file using the Git LFS Batch API with a Python script:
     ```python
     # Python template to resolve LFS Batch API:
     import urllib.request, json
     url = "https://github.com/yacoubasawadogo/computer-science-books.git/info/lfs/objects/batch"
     payload = {
         "operation": "download",
         "transfer": ["basic"],
         "objects": [{"oid": "<sha_from_pointer>", "size": <size_from_pointer>}]
     }
     req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), 
                                  headers={"Accept": "application/vnd.git-lfs+json", "Content-Type": "application/json"}, method="POST")
     with urllib.request.urlopen(req) as r:
         res = json.loads(r.read().decode("utf-8"))
         download_url = res["objects"][0]["actions"]["download"]["href"]
     ```
     - Download the file from that temporary URL.
   - If the file is not an LFS pointer, download the raw file directly from:
     `https://raw.githubusercontent.com/yacoubasawadogo/computer-science-books/main/<path>`

#### B. afondiel/cs-books Index
1. Read `.agents/skills/download-references/resources/afondiel_index.json`.
2. Look up the topic folder in the `"categories"` map.
3. If a matching category is found, note the Google Drive folder URL to include in the final index `README.md` so the user can easily access the curated category drive folder.

### 4. Search Internet-wide (Fallback)

If a book is not found in the local indexes:
1. Search the web using `search_web`.
   * *Example:* `"<Author>" "<Book Title>" filetype:pdf` or `"<Author>" "<Book Title>" pdf download`
2. Prioritize links from university domains (`.edu`), open educational directories (like `vssut.ac.in` or `nptel.ac.in`), or public archives.
3. **Handling Redirects and Dead Links:**
   - Web search results may return Google Search redirect URLs (e.g., `https://vertexaisearch.cloud.google.com/grounding-api-redirect/...`). Resolve these redirects programmatically using Python (e.g., `urllib.request.urlopen(url).geturl()`) to obtain the actual destination URL.
   - Always verify that the link is alive (does not return a 404). Note that institutional paths like VSSUT links are prone to relocation; if a 404 occurs, do a broader search to find active mirrors or alternative digital notes (e.g., MRCET notes are often organized under `https://mrcet.com/downloads/digital_notes/<Department>/<Year>/`).
4. Download using `curl -L -o "textbooks/semester-<number>/<subject-name>/<clean_filename>.pdf" "<url>"`.
5. If paywalled or strictly copyrighted, mark as `Requires Manual Purchase/Library Access` and link to its informational page.

### 5. Index the Textbooks

Create or update `textbooks/semester-<number>/<subject-name>/README.md` with:
- A structured table listing all textbooks and references.
- The status of each book:
  * `Downloaded` (provide a clickable link to the local file)
  * `Link Found` (provide the URL to the online version or Google Drive folder)
  * `Manual Intervention Required` (if paywalled/not found)
- A brief description of the source and edition downloaded.

## Rules & Guardrails

- **File Naming:** Save files with clean, readable names using `Title_Case` or `kebab-case` incorporating the book name and main author (e.g., `Introduction_to_Algorithms_Cormen.pdf`).
- **File Safety:** Only download document formats (e.g., `.pdf`, `.epub`, `.djvu`, `.docx`). Never download executable files, scripts, or archives containing potential malware.
- **Reporting:** Keep the user informed with status updates per book, and provide a clear final summary of what was successfully downloaded and what requires manual handling.
