"""Tool schemas and validation of the small JSON Schema subset used here."""

import re

from .errors import ClarifyError


def obj(properties, required=()):
    return {"type": "object", "properties": properties,
            "required": list(required), "additionalProperties": False}


TEXT = {"type": "string", "minLength": 1}
STRING = {"type": "string"}
ID = {"type": "string", "pattern": r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,95}$"}
EVIDENCE = obj({"source": {"type": "string", "enum": ["user", "context", "agent"]},
                "text": TEXT}, ["source", "text"])
ITEM = obj({"id": ID, "title": TEXT, "impact": TEXT, "why_user": TEXT,
            "priority": {"type": "string", "enum": ["alpha", "beta", "gamma"]},
            "owner": {"type": "string", "enum": ["user", "agent"]}},
           ["id", "title", "impact", "why_user"])
ITEMS = {"type": "array", "items": ITEM}
DISPOSITIONS = ["partial", "user_decided", "user_delegated", "agent_owned", "deferred", "inapplicable"]
OPERATION = obj({
    "action": {"type": "string", "enum": ["add", "record", "reopen", "context"]},
    "reason": TEXT, "evidence": EVIDENCE, "item": ITEM, "id": ID,
    "disposition": {"type": "string", "enum": DISPOSITIONS}, "decision": TEXT,
    "text": STRING,
}, ["action", "reason", "evidence"])
REVISION = {"type": "integer", "minimum": 0}
SESSION_WRITE = {"session_id": ID, "expected_revision": REVISION}


def writing(properties):
    return obj({**SESSION_WRITE, **properties}, [*SESSION_WRITE, *properties])


SCHEMAS = {
    "clarify_session_create": obj({
        "session_id": ID, "title": TEXT, "original_request": TEXT,
        "context": STRING, "workspace": STRING, "items": ITEMS,
    }, ["session_id", "title", "original_request"]),
    "clarify_session_list": obj({"workspace": STRING,
                                 "limit": {"type": "integer", "minimum": 1, "maximum": 100}}),
    "clarify_session_read": obj({"session_id": ID, "include_history": {"type": "boolean"}}, ["session_id"]),
    "clarify_items_update": writing({"operations": {"type": "array", "items": OPERATION, "minItems": 1}}),
    "clarify_round_start": obj({**SESSION_WRITE,
                                "ordered_item_ids": {"type": "array", "items": ID, "minItems": 1}},
                               [*SESSION_WRITE]),
    "clarify_round_review": obj({**SESSION_WRITE, "summary": TEXT, "new_items": ITEMS,
                                 "interruption_reason": TEXT,
                                 "prerequisite_ids": {"type": "array", "items": ID, "minItems": 1}},
                                [*SESSION_WRITE, "summary"]),
    "clarify_session_close": writing({"outcome": {"type": "string", "enum": ["completed", "stopped"]},
                                      "reason": TEXT, "evidence": EVIDENCE}),
}

DESCRIPTIONS = {
    "clarify_session_create": "Start an explicitly requested Clarify interview. Choose a stable session_id before calling; on an uncertain response, read that ID. Does not judge whether requirements are complete.",
    "clarify_session_list": "List interview metadata, optionally for an explicit workspace. No state creation; never automatically resume the globally latest session.",
    "clarify_session_read": "Read actual item and round progress, decisions, and evidence. Include history for corrections/recovery. Read after uncertain mutations before retrying.",
    "clarify_items_update": "Atomically add items or record partial/decided/delegated/deferred/inapplicable answers, reopen unresolved choices, or replace context. Supply evidence and reasons. Uses expected_revision; no free-form patches.",
    "clarify_round_start": "Freeze all open items. Optional ordered_item_ids must contain every open ID exactly once in the reconsidered question order; otherwise uses alpha/beta/gamma. After the first round, requires review of the latest content. Questions remain adaptive.",
    "clarify_round_review": "Record contextual review and optional material new items. For prerequisite-driven interruption, name queued prerequisite_ids and an interruption_reason; remaining items carry unresolved. Cannot prove semantic completeness.",
    "clarify_session_close": "Close naturally only after latest-content review and no open items, or stop on explicit user evidence preserving unresolved work. Drafts do not require closing.",
}


def validate(value, schema, path="arguments"):
    kind = schema["type"]
    valid = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str), "integer": type(value) is int,
             "boolean": type(value) is bool}[kind]
    if not valid:
        raise ClarifyError("invalid_arguments", f"{path} must be {kind}")
    if "enum" in schema and value not in schema["enum"]:
        raise ClarifyError("invalid_arguments", f"{path} must be one of {schema['enum']}")
    if kind == "object":
        missing = set(schema.get("required", [])) - value.keys()
        extra = value.keys() - schema["properties"].keys()
        if missing or extra:
            raise ClarifyError("invalid_arguments", f"{path}: missing {sorted(missing)}, unexpected {sorted(extra)}")
        for key, item in value.items():
            validate(item, schema["properties"][key], f"{path}.{key}")
    elif kind == "array":
        if len(value) < schema.get("minItems", 0):
            raise ClarifyError("invalid_arguments", f"{path} needs at least one item")
        for index, item in enumerate(value):
            validate(item, schema["items"], f"{path}[{index}]")
    elif kind == "string":
        if "minLength" in schema and len(value.strip()) < schema["minLength"]:
            raise ClarifyError("invalid_arguments", f"{path} must not be blank")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value):
            raise ClarifyError("invalid_arguments", f"{path} must be a short stable identifier, not a path")
    elif kind == "integer":
        if value < schema.get("minimum", value) or value > schema.get("maximum", value):
            raise ClarifyError("invalid_arguments", f"{path} is outside its allowed range")
