# conversation/intent.py


class IntentDetector:

    def __init__(self):

        self.join_words = [

            "join",
            "i want to join",
            "interested",
            "go ahead",
            "let's do it",
            "lets do it",
            "tell me more",
            "yes tell me more",
            "yes, tell me more",
            "more details",
            "show me more",
            "continue",
            "please continue",
            "sounds good",
            "okay",
            "ok",
            "yes",
            "yes please",
            "start",
            "sign me up",
            "count me in"
        ]

        self.stop_words = [

            "stop",
            "unsubscribe",
            "remove me",
            "not interested",
            "don't contact",
            "do not contact",
            "leave me alone",
            "opt out",
            "cancel"
        ]

        self.negative_words = [

            "bad",
            "poor",
            "terrible",
            "useless",
            "not useful",
            "waste",
            "problem",
            "issue",
            "complaint",
            "frustrated",
            "disappointed"
        ]

    def detect(
        self,
        message
    ):

        if not message:

            return "UNKNOWN"

        text = message.lower().strip()

        for phrase in self.stop_words:

            if phrase in text:

                return "STOP"

        for phrase in self.join_words:

            if phrase in text:

                return "JOIN"

        for phrase in self.negative_words:

            if phrase in text:

                return "NEGATIVE"

        return "UNKNOWN"