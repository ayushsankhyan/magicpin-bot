# tests/test_orchestrator.py

from core.loader import DataLoader
from core.orchestrator import Orchestrator
import pprint

loader = DataLoader("expanded")

merchant = next(
    iter(loader.load_merchants().values())
)

trigger = next(
    iter(loader.load_triggers().values())
)

orch = Orchestrator()

result = orch.process(
    merchant,
    trigger
)

pprint.pprint(result)