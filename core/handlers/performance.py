# core/handlers/performance.py

class PerformanceHandler:

    def generate(
        self,
        facts,
        health_score
    ):

        recommendations = []

        signals = facts.get(
            "signals",
            []
        )

        if any(
            "stale_posts" in s
            for s in signals
        ):
            recommendations.append(
                "Create fresh content"
            )

        if (
            "ctr_below_peer_median"
            in signals
        ):
            recommendations.append(
                "Improve listing CTR"
            )

        return {

            "problem":
                "performance",

            "health_score":
                health_score,

            "recommendations":
                recommendations
        }