class RecallHandler:

    def generate(
        self,
        merchant,
        customer,
        trigger
    ):

        payload = trigger.get("payload", {})

        return {
            "service_due":
                payload.get("service_due"),

            "due_date":
                payload.get("due_date"),

            "slots":
                payload.get(
                    "available_slots",
                    []
                )
        }