# core/context_store.py

from datetime import datetime


class ContextStore:

    def __init__(self):

        self.categories = {}
        self.merchants = {}
        self.customers = {}
        self.triggers = {}

        self.versions = {}

        self.started_at = datetime.utcnow()

    def add_context(
        self,
        scope,
        context_id,
        version,
        payload
    ):

        key = f"{scope}:{context_id}"

        current_version = self.versions.get(key)

        if (
            current_version is not None
            and version <= current_version
        ):

            return {
                "accepted": False,
                "reason": "stale_version",
                "current_version": current_version
            }

        self.versions[key] = version

        if scope == "category":
            self.categories[context_id] = payload

        elif scope == "merchant":
            self.merchants[context_id] = payload

        elif scope == "customer":
            self.customers[context_id] = payload

        elif scope == "trigger":
            self.triggers[context_id] = payload

        return {
            "accepted": True,
            "ack_id": f"ack_{context_id}_v{version}",
            "stored_at": datetime.utcnow().isoformat()
        }

    def get_category(
        self,
        category_id
    ):
        return self.categories.get(
            category_id
        )

    def get_merchant(
        self,
        merchant_id
    ):
        return self.merchants.get(
            merchant_id
        )

    def get_customer(
        self,
        customer_id
    ):
        return self.customers.get(
            customer_id
        )

    def get_trigger(
        self,
        trigger_id
    ):
        return self.triggers.get(
            trigger_id
        )

    def counts(self):

        return {

            "category": len(
                self.categories
            ),

            "merchant": len(
                self.merchants
            ),

            "customer": len(
                self.customers
            ),

            "trigger": len(
                self.triggers
            )
        }