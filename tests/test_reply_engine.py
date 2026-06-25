from core.reply_engine import ReplyEngine

engine = ReplyEngine()

print("\nJOIN")
print(
    engine.reply(
        "m1",
        "yes do it"
    )
)

print("\nSTOP")
print(
    engine.reply(
        "m1",
        "stop"
    )
)

print("\nTOPIC")
print(
    engine.reply(
        "m1",
        "whitening and aligners"
    )
)

print("\nNEGATIVE")
print(
    engine.reply(
        "m1",
        "you are stupid"
    )
)

print("\nUNKNOWN")
print(
    engine.reply(
        "m1",
        "hello"
    )
)