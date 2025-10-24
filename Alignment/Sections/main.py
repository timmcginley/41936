import os

# Define the expected sections for each subject
expected_sections = [
    "Introduction",
    "Design Principles",
    "Codes & Standards",
    "Best Practices",
    "Common Pitfalls",
    "References"
]

manual_dir = "../manual"  # Adjust path as needed

for filename in os.listdir(manual_dir):
    if filename.endswith(".md"):
        with open(os.path.join(manual_dir, filename), encoding="utf-8") as f:
            content = f.read()
        print(f"Checking {filename}:")
        for section in expected_sections:
            if f"# {section}" not in content and f"## {section}" not in content:
                print(f"  - Missing: {section}")
        print()
