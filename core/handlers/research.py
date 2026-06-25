# core/handlers/research.py

class ResearchHandler:

    def generate(
        self,
        facts,
        trigger
    ):

        topic = trigger[
            "payload"
        ].get(
            "top_item_id",
            "research"
        )

        return {

            "topic":
                topic,

            "angle":
                "curiosity",

            "cta":
                "summary"
        }