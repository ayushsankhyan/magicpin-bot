from datetime import datetime, timezone

from fastapi import FastAPI, Body

from core.context_store import ContextStore
from core.loader import DataLoader
from core.orchestrator import Orchestrator
from core.reply_engine import ReplyEngine


app = FastAPI(
    title="MagicPin Vera Bot",
    version="1.0.0"
)

store = ContextStore()

loader = DataLoader("expanded")

orchestrator = Orchestrator()

reply_engine = ReplyEngine()

merchants = loader.load_merchants()

triggers = loader.load_triggers()


# ==========================================================
# HEALTH
# ==========================================================

@app.get("/v1/healthz")
def healthz():

    uptime = (
        datetime.utcnow() -
        store.started_at
    ).total_seconds()

    return {
        "status": "ok",
        "uptime_seconds": int(uptime),
        "contexts_loaded": store.counts()
    }


# ==========================================================
# METADATA
# ==========================================================

@app.get("/v1/metadata")
def metadata():

    return {

        "team_name": "Ayush Sankhyan",

        "team_members": [
            "Ayush Sankhyan"
        ],

        "model":
            "deterministic-context-aware-message-engine",

        "approach":
            (
                "Planner + Handlers + "
                "Composer + Memory + "
                "Intent Detection"
            ),

        "contact_email":
            "sankhyanayush95@gmail.com",

        "version":
            "1.0.0",

        "submitted_at":
            datetime.now(
                timezone.utc
            ).isoformat()
    }


# ==========================================================
# CONTEXT
# ==========================================================

@app.post("/v1/context")
def load_context(
    payload: dict = Body(...)
):

    scope = payload.get("scope")

    context_id = (
        payload.get("context_id")
        or payload.get("id")
    )

    version = payload.get(
        "version",
        1
    )

    data = payload.get(
        "payload",
        {}
    )

    result = store.add_context(
        scope,
        context_id,
        version,
        data
    )

    return result


# ==========================================================
# TICK
# ==========================================================

@app.post("/v1/tick")
def tick(
    payload: dict = Body(...)
):

    trigger_ids = payload.get(
        "trigger_ids",
        []
    )[:20]

    actions = []

    for trigger_id in trigger_ids:

        trigger = triggers.get(
            trigger_id
        )

        if not trigger:
            continue

        merchant_id = trigger.get(
            "merchant_id"
        )

        merchant = merchants.get(
            merchant_id
        )

        if not merchant:
            continue

        result = orchestrator.process(
            merchant,
            trigger
        )

        actions.append({

            "trigger_id":
                trigger_id,

            "merchant_id":
                merchant_id,

            "message":
                result["message"],

            "body":
                result["message"],

            "cta":
                result["strategy"].get(
                    "cta"
                ),

            "health_score":
                result["health_score"],

            "rationale":
                result["strategy"][
                    "hook"
                ],

            "suppression_key":
                trigger.get(
                    "suppression_key",
                    trigger_id
                ),

            "send_as":
                "vera",

            "send_as_identity":
                "vera"
        })

    return {
        "actions": actions
    }


# ==========================================================
# REPLY
# ==========================================================

@app.post("/v1/reply")
def reply(
    payload: dict = Body(...)
):

    merchant_id = payload.get(
        "merchant_id",
        "unknown"
    )

    message = payload.get(
        "message",
        ""
    )

    result = reply_engine.reply(
        merchant_id,
        message
    )

    return result