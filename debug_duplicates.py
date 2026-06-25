# debug_duplicates.py

import json
from collections import Counter

with open("submission.json", "r", encoding="utf-8") as fp:
    data = json.load(fp)

messages = [x["message"] for x in data]

counts = Counter(messages)

for msg, count in counts.items():

    if count > 1:

        print("\n" + "=" * 80)
        print("COUNT:", count)
        print("=" * 80)
        print(msg)