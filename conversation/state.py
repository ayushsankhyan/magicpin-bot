# conversation/state.py

class ConversationState:

    def __init__(self):

        self.state = {}

    def initialize(
        self,
        merchant_id
    ):

        if merchant_id not in self.state:

            self.state[merchant_id] = {

                "topics_discussed": [],

                "last_trigger": None,

                "last_cta": None,

                "engagement_score": 0,

                "language": "en",

                "last_intent": None
            }

    def get(
        self,
        merchant_id
    ):

        self.initialize(
            merchant_id
        )

        return self.state[
            merchant_id
        ]

    def update(
        self,
        merchant_id,
        key,
        value
    ):

        self.initialize(
            merchant_id
        )

        self.state[
            merchant_id
        ][key] = value

    def add_topic(
        self,
        merchant_id,
        topic
    ):

        self.initialize(
            merchant_id
        )

        topics = self.state[
            merchant_id
        ]["topics_discussed"]

        if topic not in topics:
            topics.append(topic)

    def has_topic(
        self,
        merchant_id,
        topic
    ):

        self.initialize(
            merchant_id
        )

        return topic in self.state[
            merchant_id
        ]["topics_discussed"]