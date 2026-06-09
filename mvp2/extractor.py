import subprocess
import json
import re


MODEL = "deepseek-r1:1.5b"


PROMPT = """
You are an information extraction engine.

Requirement:

{requirement}

Return ONLY valid JSON.

Schema:

{{
    "subject":"",
    "verb":"",
    "objects":[],
    "sources":[],
    "destinations":[],
    "constraints":[]
}}

Rules:

1. Copy words directly from the requirement.
2. Do NOT paraphrase.
3. Do NOT summarize.
4. Do NOT invent words.
5. Do NOT infer engineering meaning.
6. Every extracted value must appear exactly in the requirement text.
7. If a field cannot be determined, use "" or [].
8. Do NOT create inputs, outputs, categories, or dependencies.
9. Return ONLY JSON.
10. No explanations.
11. No markdown.

Example:

Requirement:
The FMS shall receive barometric altitude from the ADC via ARINC 429 Label 200 at a minimum update rate of 20 Hz.

Output:
{{
    "subject":"FMS",
    "verb":"receive",
    "objects":["barometric altitude"],
    "sources":["ADC"],
    "destinations":[],
    "constraints":["ARINC 429 Label 200","20 Hz"]
}}
"""


def extract_ir(text):

    prompt = PROMPT.format(
        requirement=text
    )

    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        capture_output=True,
        text=True
    )

    raw = result.stdout

    print("\nRAW RESPONSE:")
    print(raw)
    print("=" * 80)

    match = re.search(
        r'\{.*\}',
        raw,
        re.DOTALL
    )

    if not match:
        raise RuntimeError(
            f"Could not parse:\n{raw}"
        )

    json_text = match.group(0)

    json_text = " ".join(
        json_text.splitlines()
    )

    try:

        return json.loads(
            json_text
        )

    except Exception:

        repaired = (
            json_text
            .replace("\n", " ")
            .replace("\t", " ")
        )

        return json.loads(
            repaired
        )