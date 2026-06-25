# tests/test_trigger_distribution.py

from core.loader import DataLoader
from collections import Counter

loader = DataLoader("expanded")

triggers = loader.load_triggers().values()

counter = Counter()

for trigger in triggers:
    counter[trigger["kind"]] += 1

print(counter)