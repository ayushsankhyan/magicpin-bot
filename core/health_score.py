# core/health_score.py

class MerchantHealthScore:

    def calculate(self, merchant):

        score = 100

        signals = merchant.get(
            "signals",
            []
        )

        if any(
            "stale_posts" in s
            for s in signals
        ):
            score -= 10

        if (
            "ctr_below_peer_median"
            in signals
        ):
            score -= 15

        if (
            "engaged_in_last_48h"
            in signals
        ):
            score += 5

        reviews = merchant.get(
            "review_themes",
            []
        )

        for review in reviews:

            if (
                review["sentiment"]
                == "pos"
            ):
                score += 3

            if (
                review["sentiment"]
                == "neg"
            ):
                score -= 3

        return max(
            0,
            min(score, 100)
        )