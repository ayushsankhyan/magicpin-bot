# core/orchestrator.py

from core.planner import MessagePlanner
from core.composer import Composer
from core.health_score import MerchantHealthScore

from core.handlers.performance import PerformanceHandler
from core.handlers.research import ResearchHandler
from core.handlers.review import ReviewHandler
from core.handlers.competitor import CompetitorHandler
from core.handlers.renewal import RenewalHandler
from core.handlers.recall import RecallHandler
from core.handlers.milestone import MilestoneHandler
from core.handlers.engagement import EngagementHandler


class Orchestrator:

    def __init__(self):

        self.planner = MessagePlanner()

        self.composer = Composer()

        self.health = MerchantHealthScore()

        self.performance_handler = (
            PerformanceHandler()
        )

        self.research_handler = (
            ResearchHandler()
        )

        self.review_handler = (
            ReviewHandler()
        )

        self.competitor_handler = (
            CompetitorHandler()
        )

        self.renewal_handler = (
            RenewalHandler()
        )

        self.recall_handler = (
            RecallHandler()
        )

        self.milestone_handler = (
            MilestoneHandler()
        )

        self.engagement_handler = (
            EngagementHandler()
        )

    def process(
        self,
        merchant,
        trigger,
        customer=None,
        memory=None
    ):

        facts = self.planner.extract_facts(
            merchant,
            trigger
        )

        strategy = self.planner.create_strategy(
            facts,
            trigger
        )

        health_score = (
            self.health.calculate(
                merchant
            )
        )

        kind = trigger.get(
            "kind"
        )

        handler_output = {}

        # ======================
        # Performance
        # ======================

        if kind in [

            "perf_dip",
            "perf_spike",
            "seasonal_perf_dip"

        ]:

            handler_output = (
                self.performance_handler.generate(
                    facts,
                    health_score
                )
            )

        # ======================
        # Research
        # ======================

        elif kind == "research_digest":

            handler_output = (
                self.research_handler.generate(
                    facts,
                    trigger
                )
            )

        # ======================
        # Reviews
        # ======================

        elif kind == "review_theme_emerged":

            handler_output = (
                self.review_handler.generate(
                    facts
                )
            )

        # ======================
        # Renewal
        # ======================

        elif kind == "renewal_due":

            handler_output = (
                self.renewal_handler.generate(
                    merchant,
                    trigger
                )
            )

        # ======================
        # Recall
        # ======================

        elif kind == "recall_due":

            handler_output = (
                self.recall_handler.generate(
                    merchant,
                    customer,
                    trigger
                )
            )

        # ======================
        # Competitor
        # ======================

        elif kind == "competitor_opened":

            handler_output = (
                self.competitor_handler.generate(
                    merchant,
                    trigger
                )
            )

        # ======================
        # Milestone
        # ======================

        elif kind == "milestone_reached":

            handler_output = (
                self.milestone_handler.generate(
                    facts
                )
            )

        # ======================
        # Engagement
        # ======================

        elif kind in [

            "trial_followup",
            "curious_ask_due",
            "dormant_with_vera",
            "active_planning_intent",
            "wedding_package_followup",
            "category_seasonal",
            "cde_opportunity"

        ]:

            handler_output = (
                self.engagement_handler.generate(
                    trigger
                )
            )

        # ======================
        # Merge Handler Output
        # ======================

        if handler_output:

            for key, value in (
                handler_output.items()
            ):

                facts[key] = value

        # ======================
        # Health Layer
        # ======================

        facts["health_score"] = (
            health_score
        )

        # ======================
        # Message Generation
        # ======================

        message = (
            self.composer.compose(
                facts,
                strategy,
                memory
            )
        )

        return {

            "facts":
                facts,

            "strategy":
                strategy,

            "health_score":
                health_score,

            "handler_output":
                handler_output,

            "message":
                message
        }