# conversation/topic_extractor.py

class TopicExtractor:

    TOPICS = [

        "whitening",

        "aligners",

        "cleaning",

        "retention",

        "offers",

        "reviews"
    ]

    def extract(
        self,
        text
    ):

        text = text.lower()

        found = []

        for topic in self.TOPICS:

            if topic in text:
                found.append(topic)

        return found