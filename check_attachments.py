import argparse
import json


def check_attachments(test_cases):
    flagged = []
    for test in test_cases:
        if test["status"] == "Pass" and test["attachments"] == 0:
            flagged.append(test)
    return {
        "summary": {
            "total_checked": len(test_cases),
            "total_flagged": len(flagged)
        },
        "flagged": flagged
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input JSON file")
    parser.add_argument("--output", help="Output JSON file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        test_cases = json.load(f)

    output = check_attachments(test_cases)

    with open(args.output, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Done! {output['summary']['total_flagged']} flagged cases saved to {args.output}")