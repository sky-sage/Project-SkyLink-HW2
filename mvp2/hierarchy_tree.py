import os
import json
from collections import defaultdict

LOG_DIR = "logs"

tree = defaultdict(list)


def classify(req):

    text = ""

    ext = req.get("extraction", {})

    fields = []

    for k in [
        "subject",
        "verb"
    ]:
        fields.append(
            str(ext.get(k, ""))
        )

    for k in [
        "objects",
        "sources",
        "destinations",
        "constraints"
    ]:
        fields.extend(
            ext.get(k, [])
        )

    text = " ".join(fields).lower()

    if any(
        x in text
        for x in [
            "waypoint",
            "flight plan",
            "cdu"
        ]
    ):
        return "Flight Planning"

    if any(
        x in text
        for x in [
            "track",
            "lnav",
            "cross-track"
        ]
    ):
        return "LNAV"

    if any(
        x in text
        for x in [
            "vnav",
            "vertical",
            "tod",
            "toc",
            "altitude"
        ]
    ):
        return "VNAV"

    if any(
        x in text
        for x in [
            "gps",
            "irs",
            "position",
            "adc"
        ]
    ):
        return "Sensors"

    if any(
        x in text
        for x in [
            "fuel",
            "burn"
        ]
    ):
        return "Fuel"

    if any(
        x in text
        for x in [
            "display",
            "nd",
            "pfd",
            "efis"
        ]
    ):
        return "Displays"

    if any(
        x in text
        for x in [
            "maintenance",
            "fault",
            "health",
            "crc",
            "airac"
        ]
    ):
        return "Maintenance"

    return "Other"


# --------------------------------
# Load logs
# --------------------------------

for file in os.listdir(LOG_DIR):

    if not file.endswith(".json"):
        continue

    with open(
        os.path.join(LOG_DIR, file),
        encoding="utf-8"
    ) as f:

        req = json.load(f)

    category = classify(req)

    tree[category].append(
        req["id"]
    )


# --------------------------------
# Console tree
# --------------------------------

print("\nFMS")

for category in sorted(tree.keys()):

    print(f"├── {category}")

    for req in sorted(tree[category]):

        print(
            f"│   ├── {req}"
        )


# --------------------------------
# HTML export
# --------------------------------

html = """
<html>
<head>
<title>FMS Requirement Hierarchy</title>

<style>

body{
font-family:Arial;
padding:20px;
}

ul{
list-style-type:none;
}

li{
margin:5px;
}

</style>

</head>

<body>

<h1>FMS Requirement Hierarchy</h1>

<ul>
"""

html += "<li><b>FMS</b><ul>"

for category in sorted(tree.keys()):

    html += f"<li><b>{category}</b><ul>"

    for req in sorted(tree[category]):

        html += f"<li>{req}</li>"

    html += "</ul></li>"

html += "</ul></li></ul>"

html += """
</body>
</html>
"""

with open(
    "hierarchy_tree.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html)

print(
    "\nSaved hierarchy_tree.html"
)