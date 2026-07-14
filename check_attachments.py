import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input JSON file")
parser.add_argument("--output", help="Output JSON file")
args = parser.parse_args()

with open(args.input, "r") as f:
    test_cases = json.load(f)
    
flagged = []
for test in test_cases:
    if test["status"] == "Pass" and test["attachments"] == 0:
        flagged.append(test)
    

output = {
    "summary": {
        "total_checked": len(test_cases),
        "total_flagged": len(flagged)
    },
    "flagged": flagged
}

with open(args.output, "w") as f:
    json.dump(output, f, indent=4)

print(f"Done! {len(flagged)} flagged cases saved to {args.output}")