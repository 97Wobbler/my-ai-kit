"""Interview transitions. Meaning and authenticity of evidence remain agent judgments."""

from copy import deepcopy
from datetime import datetime, timezone

from .errors import ClarifyError


def now():
    return datetime.now(timezone.utc).isoformat()


def require(condition, code, message, **details):
    if not condition:
        raise ClarifyError(code, message, **details)


def add_items(state, items):
    for raw in items:
        require(raw["id"] not in state["items"], "duplicate_item", f"Item {raw['id']} already exists")
        state["items"][raw["id"]] = {
            "priority": "beta", "owner": "user", **deepcopy(raw),
            "disposition": "open", "decision": "", "reason": "", "evidence": [],
        }


def create_state(args):
    state = {"schema_version": 1, "session_id": args["session_id"],
             "title": args["title"], "original_request": args["original_request"],
             "context": args.get("context", ""), "workspace": args.get("workspace", ""),
             "status": "active", "revision": 0, "content_revision": 0,
             "reviewed_content_revision": None, "items": {}, "rounds": [],
             "history": [], "created_at": now(), "updated_at": now()}
    add_items(state, args.get("items", []))
    return state


def current_round(state):
    return state["rounds"][-1] if state["rounds"] else None


def open_ids(state):
    return [key for key, item in state["items"].items() if item["disposition"] == "open"]


def pending_current(state):
    round_ = current_round(state)
    if not round_ or round_["status"] != "interviewing":
        return []
    return [key for key in round_["item_ids"] if key not in round_["records"]]


def candidates(state):
    current = set(pending_current(state))
    return [key for key in open_ids(state) if key not in current]


def remember(state, action, **details):
    state["history"].append({"revision": state["revision"] + 1,
                             "at": now(), "action": action, **deepcopy(details)})


def content_changed(state):
    state["content_revision"] = state["revision"] + 1


def update_items(state, args):
    allowed = {"add": {"item"}, "record": {"id", "disposition", "decision"},
               "reopen": {"id"}, "context": {"text"}}
    common = {"action", "reason", "evidence"}
    for op in args["operations"]:
        action = op["action"]
        require(set(op) == common | allowed[action], "invalid_arguments",
                f"{action} requires exactly {sorted(common | allowed[action])}")
        previous = None
        if action == "add":
            add_items(state, [op["item"]])
        elif action == "context":
            previous = state["context"]
            state["context"] = op["text"]
        else:
            require(op["id"] in state["items"], "missing_item", f"Unknown item {op['id']}")
            item = state["items"][op["id"]]
            previous = {key: deepcopy(item[key]) for key in ("disposition", "decision", "reason")}
            if action == "reopen":
                require(item["disposition"] != "open", "invalid_transition", "Item is already open; record a partial answer or add a separate decision")
                item.update(disposition="open", decision="", reason=op["reason"])
            else:
                disposition = op["disposition"]
                if disposition in {"user_decided", "user_delegated", "deferred"}:
                    require(op["evidence"]["source"] == "user", "user_evidence_required",
                            "This disposition needs actual user evidence; recommendations are not agreement")
                if disposition == "agent_owned":
                    require(item["owner"] == "agent", "user_decision_required", "A user-owned decision cannot be silently delegated to the agent")
                if disposition == "partial":
                    require(item["disposition"] == "open", "invalid_transition", "Reopen an unresolved conflict before recording a partial answer")
                else:
                    item.update(disposition=disposition, decision=op["decision"], reason=op["reason"])
                    round_ = current_round(state)
                    if round_ and round_["status"] == "interviewing" and op["id"] in round_["item_ids"]:
                        round_["records"].setdefault(op["id"], {
                            "kind": "handled", "disposition": disposition, "decision": op["decision"],
                            "reason": op["reason"], "revision": state["revision"] + 1,
                        })
            item["evidence"].append({"action": action, "revision": state["revision"] + 1,
                                     **deepcopy(op["evidence"])})
        remember(state, action, input=op, previous=previous)
    content_changed(state)


def start_round(state, args):
    previous = current_round(state)
    require(not previous or previous["status"] != "interviewing", "review_required", "Review the current round before starting another")
    require(not previous or state["reviewed_content_revision"] == state["content_revision"],
            "review_required", "Review the latest content before composing the next round")
    ids = open_ids(state)
    require(bool(ids), "invalid_transition", "No open items; review and close, or add a material decision")
    if "ordered_item_ids" in args:
        ordered = args["ordered_item_ids"]
        require(len(ordered) == len(ids) and set(ordered) == set(ids),
                "invalid_round_order", "Include every open item exactly once; resolve candidates with evidence before review", item_ids=ids)
        ids = list(ordered)
    else:
        priority = {"alpha": 0, "beta": 1, "gamma": 2}
        ids.sort(key=lambda key: priority[state["items"][key]["priority"]])
    state["rounds"].append({"number": len(state["rounds"]) + 1, "status": "interviewing",
                            "item_ids": ids, "records": {}})
    remember(state, "round_start", item_ids=ids)


def review_round(state, args):
    new = args.get("new_items", [])
    if new:
        add_items(state, new)
        content_changed(state)
    pending = pending_current(state)
    round_ = current_round(state)
    interruption = args.get("interruption_reason")
    prerequisites = args.get("prerequisite_ids", [])
    if interruption or prerequisites:
        require(bool(interruption) and bool(prerequisites) and bool(pending), "invalid_transition",
                "An interruption needs pending current items, a reason, and queued prerequisites")
        require(set(prerequisites) <= set(candidates(state)), "invalid_prerequisite",
                "Prerequisites must be open queued candidates, not unanswered current-round items")
        for key in pending:
            round_["records"][key] = {"kind": "carried", "reason": interruption,
                                      "revision": state["revision"] + 1}
        round_["status"] = "interrupted"
    else:
        require(not pending, "round_incomplete", "Current round still has unanswered items", item_ids=pending)
        if round_ and round_["status"] == "interviewing":
            round_["status"] = "reviewed"
    review = {"summary": args["summary"], "content_revision": state["content_revision"],
              "revision": state["revision"] + 1, "new_item_ids": [item["id"] for item in new]}
    if interruption:
        review.update(interruption_reason=interruption, prerequisite_ids=prerequisites)
    state["latest_review"] = review
    state["reviewed_content_revision"] = state["content_revision"]
    if round_:
        round_["review"] = deepcopy(review)
    remember(state, "round_review", review=review, new_items=new)


def close_session(state, args):
    if args["outcome"] == "completed":
        require(not open_ids(state), "open_items", "Open decisions still require interview", item_ids=open_ids(state))
        require(not pending_current(state), "round_incomplete", "Current round has not been handled")
        require(state["reviewed_content_revision"] == state["content_revision"],
                "review_required", "Review the latest interview content before natural completion")
    else:
        require(args["evidence"]["source"] == "user", "user_evidence_required", "Stopping requires an explicit user request")
    state["status"] = args["outcome"]
    state["closure"] = {"reason": args["reason"], "evidence": deepcopy(args["evidence"])}
    remember(state, "close", outcome=args["outcome"], **state["closure"])


def snapshot(state, include_history=False):
    result = deepcopy(state)
    if not include_history:
        result.pop("history")
    round_ = current_round(state)
    progress = {"open_item_ids": open_ids(state), "next_round_candidate_ids": candidates(state),
                "review_current": state["reviewed_content_revision"] == state["content_revision"],
                "deferred_item_ids": [key for key, item in state["items"].items() if item["disposition"] == "deferred"]}
    if round_:
        records = round_["records"]
        progress["round"] = {"number": round_["number"], "status": round_["status"],
                             "total": len(round_["item_ids"]),
                             "handled": sum(r["kind"] == "handled" for r in records.values()),
                             "carried": sum(r["kind"] == "carried" for r in records.values()),
                             "remaining": len(round_["item_ids"]) - len(records)}
    else:
        progress["round"] = None
    result["progress"] = progress
    return result
