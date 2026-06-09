import os
import json

from parser import parse_requirements
from extractor import extract_ir

# Get paths relative to workspace root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
INPUT_FILE = os.path.join(ROOT_DIR, "DP5_Datasets", "DS1_CommercialFMS_Requirements.txt")


def main():

    print("Loading requirements...")

    requirements = parse_requirements(
        INPUT_FILE
    )
    
    print(
        f"Loaded {len(requirements)} requirements"
    )

    os.makedirs(
        "logs",
        exist_ok=True
    )

    results = []

    # Uncomment while debugging
    # requirements = requirements[:5]

    for req in requirements:

        req_id = req["id"]

        print(
            f"\nProcessing {req_id}"
        )

        try:

            ir = extract_ir(
                req["text"]
            )

            record = {

                "id": req_id,

                "requirement": req["text"],

                "extraction": ir
            }

            # Save individual log

            log_file = os.path.join(
                "logs",
                f"{req_id}.json"
            )

            with open(
                log_file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    record,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

            print(
                f"Saved {log_file}"
            )

            results.append(record)

        except Exception as e:

            print(
                f"ERROR on {req_id}: {e}"
            )

            record = {

                "id": req_id,

                "requirement": req["text"],

                "extraction": None,

                "error": str(e)
            }

            results.append(record)

        print("-" * 60)

    with open(
        "ir_dump.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(
        "\nFinished."
    )

    print(
        f"Saved {len(results)} records to ir_dump.json"
    )

    print(
        f"Individual requirement logs written to ./logs/"
    )


if __name__ == "__main__":
    main()