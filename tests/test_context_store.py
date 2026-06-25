from core.context_store import ContextStore

store = ContextStore()

print(
    store.add_context(
        "merchant",
        "m001",
        1,
        {"name": "Demo"}
    )
)

print(
    store.add_context(
        "merchant",
        "m001",
        1,
        {"name": "Demo"}
    )
)

print(
    store.counts()
)