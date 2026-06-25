class MilestoneHandler:

    def generate(
        self,
        facts
    ):

        return {

            "views":
                facts.get("views"),

            "calls":
                facts.get("calls"),

            "leads":
                facts.get("leads")
        }