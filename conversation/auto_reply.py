# conversation/auto_reply.py

class AutoReplyDetector:

    AUTO_PATTERNS = [

        # Customer support
        "thank you for contacting",
        "thank you for reaching out",
        "our team will contact you",
        "our team will get back",
        "automated assistant",
        "auto reply",
        "your message is important to us",
        "we appreciate your message",

        # Out of office
        "out of office",
        "currently out of office",
        "i am out of office",
        "i'm out of office",
        "away from office",
        "currently away",
        "on leave",
        "on vacation",
        "on holiday",
        "will respond when i return",

        # Hindi
        "aapki jaankari ke liye",
        "hamari team aapse sampark karegi"

    ]

    def is_auto_reply(self, message):

        if not message:
            return False

        msg = message.lower().strip()

        return any(
            pattern in msg
            for pattern in self.AUTO_PATTERNS
        )

    def repeated_reply(
        self,
        history,
        threshold=2
    ):

        if not history:
            return False

        latest = history[-1].strip().lower()

        count = sum(
            1
            for msg in history
            if msg.strip().lower() == latest
        )

        return count >= threshold