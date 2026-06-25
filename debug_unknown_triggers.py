# debug_unknown_triggers.py

from pprint import pprint
from core.loader import DataLoader

loader = DataLoader("expanded")

triggers = loader.load_triggers()

interesting = {
    "ipl_match_today",
    "supply_alert",
    "regulation_change",
    "gbp_unverified",
    "category_seasonal",
    "cde_opportunity",
    "wedding_package_followup",
    "seasonal_perf_dip"
}

for trigger_id, trigger in triggers.items():

    if trigger.get("kind") in interesting:

        print("\n" + "=" * 80)
        print(trigger_id)
        print("=" * 80)

        pprint(trigger)