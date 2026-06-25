# core/router.py

class TriggerRouter:

    ROUTES = {

        "research_digest": "research",

        "perf_dip": "performance",

        "perf_spike": "performance",

        "milestone_reached": "milestone",

        "review_theme_emerged": "review",

        "festival_upcoming": "festival",

        "competitor_opened": "competitor",

        "renewal_due": "renewal",

        "recall_due": "recall",

        "customer_lapsed_soft": "winback",

        "appointment_tomorrow": "appointment",

        "dormant_with_vera": "engagement",

        "curious_ask_due": "curiosity"
    }

    def route(self, trigger):

        kind = trigger.get("kind")

        return self.ROUTES.get(
            kind,
            "generic"
        )