from collections import Counter
from core.loader import DataLoader

loader = DataLoader("expanded")

triggers = loader.load_triggers()

counter = Counter()

for trigger in triggers.values():
    counter[trigger["kind"]] += 1

print("\nTRIGGERS IN DATASET\n")

for name, count in sorted(counter.items()):
    print(f"{name:30} {count}")