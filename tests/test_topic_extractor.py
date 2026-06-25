# tests/test_topic_extractor.py

from conversation.topic_extractor import TopicExtractor

extractor = TopicExtractor()

text = (
    "Yes please, focus on "
    "whitening and aligners"
)

print(
    extractor.extract(text)
)