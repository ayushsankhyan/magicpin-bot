# tests/test_state.py

from conversation.state import ConversationState

memory = ConversationState()

merchant = "m_001"

memory.update(
    merchant,
    "last_trigger",
    "research_digest"
)

memory.update(
    merchant,
    "last_cta",
    "summary_offer"
)

print(
    memory.get(merchant)
)