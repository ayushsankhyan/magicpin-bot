# tests/test_state_methods.py

from conversation.state import ConversationState

state = ConversationState()

state.add_topic(
    "m1",
    "whitening"
)

print(
    state.has_topic(
        "m1",
        "whitening"
    )
)