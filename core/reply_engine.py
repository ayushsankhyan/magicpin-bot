from conversation.intent import IntentDetector
from conversation.auto_reply import AutoReplyDetector
from conversation.topic_extractor import TopicExtractor
from conversation.state import ConversationState

class ReplyEngine:

    def __init__(self):
        self.intent = IntentDetector()
        self.auto_reply = AutoReplyDetector()
        self.topics = TopicExtractor()
        self.state = ConversationState()

    def reply(
        self,
        merchant_id,
        message
    ):

        message = (
            message or ""
        ).strip()

        # ==========================
        # Auto Reply Detection
        # ==========================

        if self.auto_reply.is_auto_reply(
            message
        ):

            return {
                "action": "ignore",
                "reply": None,
                "reason": "auto_reply_detected"
            }

        # ==========================
        # Hostile / Negative Replies
        # ==========================

        hostile_words = [

            "stupid",
            "idiot",
            "useless",
            "hate",
            "nonsense",
            "annoying",
            "worst",
            "fake",
            "spam",
            "stop bothering",
            "waste"

        ]

        msg_lower = message.lower()

        if any(

            word in msg_lower

            for word in hostile_words

        ):

            return {

                "action": "send",

                "body":
                (
                    "I understand your concern.\n\n"
                    "Could you tell me what "
                    "didn't work as expected?"
                ),

                "cta":
                "share_feedback",

                "rationale":
                "negative sentiment detected",

                "intent":
                "NEGATIVE"
            }

        # ==========================
        # Intent Detection
        # ==========================

        intent = self.intent.detect(
            message
        )

        self.state.update(
            merchant_id,
            "last_intent",
            intent
        )

        # ==========================
        # Topic Extraction
        # ==========================

        extracted_topics = (
            self.topics.extract(
                message
            )
        )

        for topic in extracted_topics:

            self.state.add_topic(
                merchant_id,
                topic
            )

        # ==========================
        # JOIN Intent
        # ==========================

        if intent == "JOIN":

            return {

                "action":
                "send",

                "body":
                (
                    "Thanks for confirming.\n\n"
                    "I'll prepare the onboarding "
                    "details and share the next "
                    "recommended step shortly."
                ),

                "cta":
                "next_step",

                "rationale":
                "merchant accepted engagement",

                "intent":
                "JOIN"
            }

        # ==========================
        # STOP Intent
        # ==========================

        if intent == "STOP":

            return {

                "action":
                "end",

                "body":
                (
                    "Understood.\n\n"
                    "I'll stop follow-ups related "
                    "to this topic."
                ),

                "cta":
                None,

                "rationale":
                "merchant requested stop",

                "intent":
                "STOP"
            }

        # ==========================
        # Topic Interest
        # ==========================

        if extracted_topics:

            return {

                "action":
                "send",

                "body":
                (
                    f"I noted your interest in "
                    f"{', '.join(extracted_topics)}.\n\n"
                    f"I'll use this information "
                    f"to prioritize future "
                    f"recommendations."
                ),

                "cta":
                "continue",

                "rationale":
                "topic interest detected",

                "topics":
                extracted_topics
            }

        # ==========================
        # Unknown
        # ==========================

        return {

            "action":
            "send",

            "body":
            (
                "Thanks for your message.\n\n"
                "Could you share a little more "
                "about what you're looking for?"
            ),

            "cta":
            "clarify",

            "rationale":
            "insufficient context",

            "intent":
            "UNKNOWN"
        }