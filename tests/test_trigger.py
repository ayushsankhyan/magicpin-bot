# tests/test_trigger.py

from core.loader import DataLoader
import json

loader = DataLoader("expanded")

trigger = next(
    iter(loader.load_triggers().values())
)

print(json.dumps(trigger, indent=2))