# tests/test_intent.py

from conversation.intent import IntentDetector

detector = IntentDetector()

samples = [

    "I want to join",

    "Go ahead",

    "Let's do it",

    "Not interested",

    "Remove me",

    "Tell me more"
]

for sample in samples:

    print(
        sample,
        "=>",
        detector.detect(sample)
    )