# core/planner.py

class MessagePlanner:

    def extract_facts(
        self,
        merchant,
        trigger=None,
        category=None,
        customer=None
    ):

        facts = {}

        identity = merchant.get(
            "identity",
            {}
        )

        performance = merchant.get(
            "performance",
            {}
        )

        facts["merchant_name"] = (
            identity.get("name")
        )

        facts["city"] = (
            identity.get("city")
        )

        facts["locality"] = (
            identity.get("locality")
        )

        facts["category_slug"] = (
            merchant.get(
                "category_slug",
                "business"
            )
        )

        facts["views"] = (
            performance.get("views")
        )

        facts["calls"] = (
            performance.get("calls")
        )

        facts["ctr"] = (
            performance.get("ctr")
        )

        facts["leads"] = (
            performance.get("leads")
        )

        facts["signals"] = (
            merchant.get(
                "signals",
                []
            )
        )

        facts["offers"] = [

            offer.get("title")

            for offer in merchant.get(
                "offers",
                []
            )

            if offer.get("status") == "active"
        ]

        facts["review_themes"] = (
            merchant.get(
                "review_themes",
                []
            )
        )

        history = merchant.get(
            "conversation_history",
            []
        )

        if history:

            facts["last_conversation"] = (
                history[-1].get(
                    "body",
                    ""
                )
            )

        if trigger:

            payload = trigger.get(
                "payload",
                {}
            )

            facts["trigger_kind"] = (
                trigger.get("kind")
            )

            facts["trigger_payload"] = (
                payload
            )

            facts["trigger_id"] = (
                trigger.get("id")
            )

            facts["urgency"] = (
                trigger.get(
                    "urgency",
                    1
                )
            )

            facts["scope"] = (
                trigger.get("scope")
            )

            # ======================
            # Recall
            # ======================

            facts["service_due"] = (
                payload.get(
                    "service_due"
                )
            )

            facts["due_date"] = (
                payload.get(
                    "due_date"
                )
            )

            facts["available_slots"] = (
                payload.get(
                    "available_slots",
                    []
                )
            )

            # ======================
            # Renewal
            # ======================

            facts["days_remaining"] = (
                payload.get(
                    "days_remaining"
                )
            )

            facts["renewal_amount"] = (
                payload.get(
                    "renewal_amount"
                )
            )

            facts["plan"] = (
                payload.get(
                    "plan"
                )
            )

            # ======================
            # Research
            # ======================

            facts["research_topic"] = (
                payload.get(
                    "top_item_id"
                )
            )

            # ======================
            # Festival
            # ======================

            facts["festival_name"] = (
                payload.get(
                    "festival"
                )
            )
            # ======================
            # IPL
            # ======================

            facts["match"] = (
                payload.get(
                    "match"
                )
            )

            facts["venue"] = (
                payload.get(
                    "venue"
                )
            )

            # ======================
            # Wedding
            # ======================

            facts["days_to_wedding"] = (
                payload.get(
                    "days_to_wedding"
                )
            )

            facts["wedding_date"] = (
                payload.get(
                    "wedding_date"
                )
            )

            # ======================
            # Supply Alert
            # ======================

            facts["molecule"] = (
                payload.get(
                    "molecule"
                )
            )

            facts["manufacturer"] = (
                payload.get(
                    "manufacturer"
                )
            )

            # ======================
            # Seasonal
            # ======================

            facts["season"] = (
                payload.get(
                    "season"
                )
            )

            facts["trends"] = (
                payload.get(
                    "trends",
                    []
                )
            )

            # ======================
            # Compliance
            # ======================

            facts["deadline_iso"] = (
                payload.get(
                    "deadline_iso"
                )
            )

            # ======================
            # CDE
            # ======================

            facts["credits"] = (
                payload.get(
                    "credits"
                )
            )
            # ======================
            # Reviews
            # ======================

            facts["review_theme"] = (
                payload.get(
                    "theme"
                )
            )

        return facts

    def create_strategy(
        self,
        facts,
        trigger
    ):

        kind = trigger.get(
            "kind"
        )

        category = facts.get(
            "category_slug",
            "business"
        )

        urgency = facts.get(
            "urgency",
            1
        )

        strategy = {}

        # ======================
        # Category Voice
        # ======================

        if category == "dentists":

            strategy["voice"] = (
                "clinical"
            )

        elif category == "salons":

            strategy["voice"] = (
                "beauty"
            )

        elif category == "restaurants":

            strategy["voice"] = (
                "demand"
            )

        elif category == "gyms":

            strategy["voice"] = (
                "fitness"
            )

        elif category == "pharmacies":

            strategy["voice"] = (
                "compliance"
            )

        else:

            strategy["voice"] = (
                "business"
            )

        # ======================
        # Trigger Strategy
        # ======================

        if kind == "research_digest":

            strategy["hook"] = (
                "new research relevant to merchant"
            )

            strategy["compulsion"] = (
                "curiosity"
            )

            strategy["cta"] = (
                "2 minute summary"
            )

        elif kind in [

            "perf_dip",
            "seasonal_perf_dip"

        ]:

            strategy["hook"] = (
                "performance decline"
            )

            strategy["compulsion"] = (
                "loss_aversion"
            )

            strategy["cta"] = (
                "improvement ideas"
            )

        elif kind == "review_theme_emerged":

            strategy["hook"] = (
                "review trend detected"
            )

            strategy["compulsion"] = (
                "social_proof"
            )

            strategy["cta"] = (
                "fix recommendations"
            )

        elif kind == "renewal_due":

            strategy["hook"] = (
                "renewal approaching"
            )

            strategy["compulsion"] = (
                "urgency"
            )

            strategy["cta"] = (
                "renewal summary"
            )

        elif kind == "recall_due":

            strategy["hook"] = (
                "customer follow up due"
            )

            strategy["compulsion"] = (
                "retention"
            )

            strategy["cta"] = (
                "send reminder"
            )

        elif kind == "festival_upcoming":

            strategy["hook"] = (
                "seasonal demand opportunity"
            )

            strategy["compulsion"] = (
                "timeliness"
            )

            strategy["cta"] = (
                "campaign ideas"
            )

        elif kind in [

            "customer_lapsed_soft",
            "customer_lapsed_hard",
            "winback_eligible"

        ]:

            strategy["hook"] = (
                "inactive customers"
            )

            strategy["compulsion"] = (
                "winback"
            )

            strategy["cta"] = (
                "campaign ideas"
            )

        elif kind == "milestone_reached":

            strategy["hook"] = (
                "success momentum"
            )

            strategy["compulsion"] = (
                "achievement"
            )

            strategy["cta"] = (
                "growth ideas"
            )

        else:

            strategy["hook"] = (
                "growth opportunity"
            )

            strategy["compulsion"] = (
                "engagement"
            )

            strategy["cta"] = (
                "recommendations"
            )

        # ======================
        # Priority
        # ======================

        if urgency >= 4:

            strategy["priority"] = (
                "high"
            )

        elif urgency >= 2:

            strategy["priority"] = (
                "medium"
            )

        else:

            strategy["priority"] = (
                "low"
            )

        return strategy