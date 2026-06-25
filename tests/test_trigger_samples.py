# tests/test_trigger_samples.py

from core.loader import DataLoader
import json

loader = DataLoader("expanded")

interesting = [

    "renewal_due",
    "review_theme_emerged",
    "competitor_opened"
]

triggers = loader.load_triggers()

for trigger in triggers.values():

    if trigger["kind"] in interesting:

        print("\n" + "=" * 60)
        print(trigger["kind"])
        print("=" * 60)

        print(
            json.dumps(
                trigger,
                indent=2
            )
        )

        print("\n")