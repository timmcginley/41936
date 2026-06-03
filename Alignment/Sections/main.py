import os

# Define the expected sections for each subject
expected_sections = [
    "Skills and motivation",
    "Your chief consultant can support you with",
    "You will need to independently learn",
    "Assignments",
    "Common Pitfalls",
    "References"
]

manual_dir = os.getcwd()+"\Subjects"   # Adjust path as needed
print(manual_dir)
print(os.listdir(manual_dir))

for dirname in os.listdir(manual_dir):
    path = os.path.join(manual_dir, dirname)
    if os.path.isdir(path): 
        for file in os.listdir(path):
            if file.endswith(".md"):
                print(file)
                with open(file, encoding="utf-8") as f:
                    content = f.read()
                print(f"Checking {dirname}:")
                for section in expected_sections:
                    if f"# {section}" not in content and f"## {section}" not in content:
                        print(f"  - Missing: {section}")
        #print(dirname)