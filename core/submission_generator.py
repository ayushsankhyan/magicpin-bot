import json

from core.loader import DataLoader
from core.orchestrator import Orchestrator


class SubmissionGenerator:

    def __init__(self):

        self.loader = DataLoader("expanded")

        self.orchestrator = Orchestrator()

    def generate(self):

        merchants = (
            self.loader.load_merchants()
        )

        triggers = (
            self.loader.load_triggers()
        )

        results = []

        for trigger_id, trigger in triggers.items():

            merchant_id = trigger.get(
                "merchant_id"
            )

            merchant = merchants.get(
                merchant_id
            )

            if not merchant:
                continue

            output = (
                self.orchestrator.process(
                    merchant,
                    trigger
                )
            )

            results.append({

                "trigger_id":
                    trigger_id,

                "merchant_id":
                    merchant_id,

                "message":
                    output["message"],

                "health_score":
                    output["health_score"]
            })

        return results

    def save(
        self,
        filename="submission.json"
    ):

        results = self.generate()

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as fp:

            json.dump(
                results,
                fp,
                indent=2
            )

        return filename