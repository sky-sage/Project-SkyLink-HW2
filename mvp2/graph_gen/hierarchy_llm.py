import os
import json
import subprocess
from collections import defaultdict

MODEL = "smollm2:360m"

# Get paths relative to workspace root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
LOG_DIR = os.path.join(ROOT_DIR, "logs")

CATEGORIES = [
    "Flight Planning",
    "LNAV"  ,
    "VNAV",
    "Position",
    "Sensors",
    "Display",
    "Fuel",
    "Maintenance",
    "Communications",
    "Other"
]


def classify(extraction):

    prompt = f"""
You are an aircraft systems engineer.

Classify this requirement into EXACTLY ONE category.

Categories:

- Flight Planning
- LNAV
- VNAV
- Position
- Sensors
- Display
- Fuel
- Maintenance
- Communications
- Other

Requirement Data:

{json.dumps(extraction, indent=2)}

Rules:

1. Return ONLY the category name.
2. Choose exactly one category.
3. No explanations.
4. No punctuation.
"""

    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        capture_output=True,
        text=True
    )

    raw = result.stdout.strip()

    print("\nRAW:")
    print(raw)

    for cat in CATEGORIES:

        if cat.lower() in raw.lower():
            return cat

    return "Other"


def main():

    tree = defaultdict(list)

    files = sorted(os.listdir(LOG_DIR))

    total = 0

    for file in files:

        if not file.endswith(".json"):
            continue

        path = os.path.join(
            LOG_DIR,
            file
        )

        try:

            with open(
                path,
                encoding="utf-8"
            ) as f:

                req = json.load(f)

            req_id = req["id"]

            extraction = req["extraction"]

            print(
                f"\nClassifying {req_id}"
            )

            category = classify(
                extraction
            )

            tree[category].append(
                req_id
            )

            print(
                f" -> {category}"
            )

            total += 1

        except Exception as e:

            print(
                f"Failed: {file}"
            )

            print(e)

    print("\n")
    print("=" * 50)
    print("FMS REQUIREMENT HIERARCHY")
    print("=" * 50)

    print("FMS")

    for category in sorted(tree.keys()):

        print(
            f"├── {category}"
        )

        for req in sorted(
            tree[category]
        ):

            print(
                f"│   ├── {req}"
            )

    # HTML Export

    html = """
<html>
<head>

<title>FMS Requirement Hierarchy</title>

<style>

body{
    font-family: Arial;
    padding: 20px;
}

ul{
    list-style-type:none;
}

li{
    margin:4px;
}

</style>

</head>

<body>

<h1>FMS Requirement Hierarchy</h1>

<ul>
<li><b>FMS</b>
<ul>
"""

    for category in sorted(
        tree.keys()
    ):

        html += (
            f"<li><b>{category}</b><ul>"
        )

        for req in sorted(
            tree[category]
        ):

            html += (
                f"<li>{req}</li>"
            )

        html += "</ul></li>"

    html += """
</ul>
</li>
</ul>

</body>
</html>
"""

    with open(
        "hierarchy_tree.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("\n")
    print(
        f"Processed {total} requirements"
    )

    print(
        "Saved hierarchy_tree.html"
    )


if __name__ == "__main__":
    main()