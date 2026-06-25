# tests/test_auto_reply.py

from conversation.auto_reply import AutoReplyDetector

detector = AutoReplyDetector()

msg1 = (
    "Thank you for contacting us. "
    "Our team will get back to you."
)

msg2 = (
    "Yes, tell me more."
)

print(
    detector.is_auto_reply(msg1)
)

print(
    detector.is_auto_reply(msg2)
)