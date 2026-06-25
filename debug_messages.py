from core.loader import DataLoader
from core.orchestrator import Orchestrator

loader = DataLoader("expanded")
orch = Orchestrator()

merchants = loader.load_merchants()
triggers = loader.load_triggers()

for trigger_id, trigger in list(triggers.items())[:30]:

    merchant = merchants.get(
        trigger["merchant_id"]
    )

    result = orch.process(
        merchant,
        trigger
    )

    print("=" * 80)
    print(trigger["kind"])
    print(result["message"])