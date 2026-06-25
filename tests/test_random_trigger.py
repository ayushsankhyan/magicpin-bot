from core.loader import DataLoader
import random
import json

loader = DataLoader("expanded")

trigger = random.choice(
    list(loader.load_triggers().values())
)

print(json.dumps(trigger, indent=2))