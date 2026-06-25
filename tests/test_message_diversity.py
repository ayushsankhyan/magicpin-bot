# tests/test_message_diversity.py

import json

with open("submission.json") as fp:
    data = json.load(fp)

messages = [x["message"] for x in data]

unique = len(set(messages))

print("TOTAL:", len(messages))
print("UNIQUE:", unique)

print(
    "DIVERSITY:",
    round(
        unique / len(messages) * 100,
        2
    ),
    "%"
)