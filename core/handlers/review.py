# core/handlers/review.py

class ReviewHandler:

    def generate(
        self,
        facts
    ):

        reviews = facts.get(
            "review_themes",
            []
        )

        if not reviews:

            return None

        top_review = reviews[0]

        return {

            "theme":
                top_review["theme"],

            "sentiment":
                top_review["sentiment"],

            "occurrences":
                top_review[
                    "occurrences_30d"
                ]
        }