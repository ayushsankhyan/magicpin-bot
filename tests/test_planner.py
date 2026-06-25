from core.loader import DataLoader
from core.planner import MessagePlanner
import pprint

loader = DataLoader("expanded")

merchant = next(
    iter(loader.load_merchants().values())
)

planner = MessagePlanner()

facts = planner.extract_facts(merchant)

pprint.pprint(facts)