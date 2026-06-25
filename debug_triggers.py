from core.loader import DataLoader

loader = DataLoader("expanded")

triggers = loader.load_triggers()

kinds = {}

for _, trigger in triggers.items():

    kind = trigger.get("kind")

    kinds[kind] = kinds.get(kind, 0) + 1

for kind, count in sorted(kinds.items()):
    print(f"{kind}: {count}")