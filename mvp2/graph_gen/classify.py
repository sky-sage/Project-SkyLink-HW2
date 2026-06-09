import json
import subprocess

MODEL = "deepseek-r1:1.5b"


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

    return result.stdout.strip()