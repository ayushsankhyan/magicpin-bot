# tests/test_pipeline.py

from core.loader import DataLoader
from core.planner import MessagePlanner
from core.router import TriggerRouter
from core.composer import Composer

loader = DataLoader("expanded")

merchant = next(
    iter(loader.load_merchants().values())
)

trigger = next(
    iter(loader.load_triggers().values())
)

planner = MessagePlanner()
router = TriggerRouter()
composer = Composer()

facts = planner.extract_facts(
    merchant,
    trigger
)

strategy = planner.create_strategy(
    facts,
    trigger
)

message = composer.compose(
    facts,
    strategy
)

print("\nFACTS:")
print(facts)

print("\nSTRATEGY:")
print(strategy)

print("\nMESSAGE:")
print(message)