# tests/test_submission_quality.py

import json

with open("submission.json") as fp:
    data = json.load(fp)

generic = 0

for item in data:

    if item["message"] == \
       "Would you like more details?":

        generic += 1

print("TOTAL:", len(data))
print("GENERIC:", generic)
print("QUALITY:",
      round(
          (1 - generic/len(data))*100,
          2
      ),
      "%")