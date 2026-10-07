import os
import glob
import re

def main(workspace_dir):
    subjects = glob.glob(os.path.join(workspace_dir, "notes", "semester-*", "*"))
    
    for subject_path in subjects:
        if not os.path.isdir(subject_path): continue
        
        parts = subject_path.split('/')
        subject_name = parts[-1]
        semester = parts[-2]
        
        pyq_dir = os.path.join(workspace_dir, "previous-question-papers", semester, subject_name)
        if not os.path.exists(pyq_dir):
            print(f"No PYQs found for {subject_name}")
            continue
            
        pyq_files = glob.glob(os.path.join(pyq_dir, "*.txt"))
        all_pyqs = []
        for pf in pyq_files:
            session = os.path.basename(pf).replace('.txt', '').replace('_', ' ')
            with open(pf, 'r') as f:
                content = f.read()
                # Simple extraction: split by newlines and look for things ending in ? or starting with a number.
                # A robust extraction would use regex, but for now we chunk it roughly.
                sentences = re.split(r'(?<=[.?!])\s+', content)
                for s in sentences:
                    s = s.strip().replace('\n', ' ')
                    if len(s) > 15 and ('?' in s or 'Explain' in s or 'Define' in s or 'Discuss' in s or 'What' in s):
                        all_pyqs.append((session, s))
        
        module_files = glob.glob(os.path.join(subject_path, "module-*", "*.md"))
        for mf in module_files:
            filename = os.path.basename(mf)
            if filename in ['detailed-notes.md', 'revision-notes.md']: continue
            
            topic = filename.replace('.md', '').replace('-', ' ')
            keywords = topic.lower().split()
            
            matched_questions = []
            for session, q in all_pyqs:
                # Basic keyword matching
                match_count = sum(1 for kw in keywords if len(kw) > 3 and kw in q.lower())
                if match_count > 0 or (len(keywords) == 1 and keywords[0] in q.lower()):
                    matched_questions.append(f"**[{session}]** {q}")
            
            # De-duplicate
            matched_questions = list(set(matched_questions))
            
            if matched_questions:
                with open(mf, 'r') as f:
                    content = f.read()
                
                if '## 5. Previous Year Questions & Solutions' in content:
                    # Append them if not already there
                    injection = "\n".join(matched_questions)
                    if "Actual University Questions:" not in content:
                        content = content.replace('## 5. Previous Year Questions & Solutions', f'## 5. Previous Year Questions & Solutions\n\n### Actual University Questions:\n{injection}\n\n*(Note: Solutions to be generated/verified by agent)*\n')
                        with open(mf, 'w') as f:
                            f.write(content)
                        print(f"Injected {len(matched_questions)} PYQs into {filename}")
                else:
                    print(f"PYQ section not found in {filename}")

if __name__ == "__main__":
    import sys
    workspace = sys.argv[1] if len(sys.argv) > 1 else "."
    main(workspace)
