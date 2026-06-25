class CompetitorHandler:

    def generate(self, merchant, trigger):

        payload = trigger.get("payload", {})

        if not payload.get("placeholder"):

            return {
                "type": "competitor",
                "competitor_name": payload.get("competitor_name"),
                "distance_km": payload.get("distance_km"),
                "their_offer": payload.get("their_offer")
            }

        return {
            "type": "competitor",
            "placeholder": True
        }