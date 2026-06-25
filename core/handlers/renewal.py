class RenewalHandler:

    def generate(self, merchant, trigger):

        payload = trigger.get("payload", {})

        return {
            "days_remaining":
                payload.get("days_remaining"),

            "plan":
                payload.get("plan"),

            "renewal_amount":
                payload.get("renewal_amount"),

            "placeholder":
                payload.get("placeholder", False)
        }