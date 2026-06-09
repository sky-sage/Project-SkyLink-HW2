import re

REQ_PATTERN = r"(REQ-\d+):\s*(.*)"

def parse_requirements(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    reqs = []

    for rid, body in re.findall(REQ_PATTERN, text):

        reqs.append({
            "id": rid,
            "text": body.strip()
        })

    return reqs