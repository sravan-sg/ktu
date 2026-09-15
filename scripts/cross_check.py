import os
import re

base_dir = "/home/sravan/ktu/notes/semester-6/compiler-design"
syllabus_path = os.path.join(base_dir, "syllabus.md")

def to_kebab(s):
    return s.lower().replace(":", "").replace("-", " ").replace("(", "").replace(")", "").replace(",", "").split()
    
def generate_kebab(s):
    return "-".join(to_kebab(s))

def cross_check_syllabus():
    if not os.path.exists(syllabus_path):
        print("Syllabus not found!")
        return

    with open(syllabus_path, "r") as f:
        content = f.read()

    # Extract modules and topics from syllabus.md
    # Look for "### Module ... " and then the bullet points
    modules = re.split(r"### Module ", content)[1:]
    
    missing_topics = []
    
    for mod in modules:
        mod_num = None
        if mod.startswith("I "): mod_num = 1
        elif mod.startswith("II "): mod_num = 2
        elif mod.startswith("III "): mod_num = 3
        elif mod.startswith("IV "): mod_num = 4
        elif mod.startswith("V "): mod_num = 5
        elif mod.startswith("VI "): mod_num = 6
        
        mod_dir = os.path.join(base_dir, f"module-{mod_num}")
        
        topics = re.findall(r"^- (.*)$", mod, re.MULTILINE)
        for topic in topics:
            kebab = generate_kebab(topic)
            topic_file = os.path.join(mod_dir, f"{kebab}.md")
            if not os.path.exists(topic_file):
                missing_topics.append((mod_num, topic, topic_file))
                
    if missing_topics:
        print("MISSING TOPICS FOUND:")
        for mt in missing_topics:
            print(f"Module {mt[0]}: {mt[1]} -> Missing file: {mt[2]}")
    else:
        print("Cross-verification successful: 100% of syllabus topics map to existing files in the correct module directories.")

if __name__ == "__main__":
    cross_check_syllabus()
