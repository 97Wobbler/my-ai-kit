#!/usr/bin/env python3
"""Local research records: validate, create, compare-and-save, and bounded recovery.

No model calls, experiment execution, or inferred authorization live here.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import os
import sys
from pathlib import Path
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "references" / "research-schema.json"


class RecordError(ValueError):
    pass


def schema_check(value, schema, root, location="$", errors=None):
    """Validate the small documented JSON Schema subset used by our schema."""
    if errors is None:
        errors = []
    if "$ref" in schema:
        schema = root["$defs"][schema["$ref"].split("/")[-1]]
    kind = schema.get("type")
    valid_type = {
        "object": lambda: isinstance(value, dict),
        "array": lambda: isinstance(value, list),
        "string": lambda: isinstance(value, str),
        "number": lambda: type(value) in (int, float) and abs(value) <= sys.float_info.max and math.isfinite(value),
        "integer": lambda: type(value) in (int, float) and abs(value) <= sys.float_info.max and math.isfinite(value) and value % 1 == 0,
        "boolean": lambda: type(value) is bool,
    }
    if kind and not valid_type[kind]():
        errors.append(f"{location}: expected {kind}")
        return errors
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected {schema['const']}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: invalid choice {value!r}")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{location}.{key}: required")
        for key, item in value.items():
            if key in properties:
                schema_check(item, properties[key], root, f"{location}.{key}", errors)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{location}.{key}: unknown field")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", math.inf):
            errors.append(f"{location}: invalid item count")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            errors.append(f"{location}: duplicate items")
        for index, item in enumerate(value):
            schema_check(item, schema.get("items", {}), root, f"{location}[{index}]", errors)
    if isinstance(value, str) and len(value) < schema.get("minLength", 0):
        errors.append(f"{location}: empty text")
    if type(value) in (int, float):
        if value < schema.get("minimum", -math.inf) or value > schema.get("maximum", math.inf):
            errors.append(f"{location}: out of range")
    return errors


def validate(record):
    schema = json.loads(SCHEMA_PATH.read_text())
    errors = schema_check(record, schema, schema)
    if errors:
        raise RecordError("\n".join(errors))
    tables = {}
    for key in ("nodes", "edges", "paths", "decisions", "recoveries", "documents", "evidence"):
        tables[key] = {item["id"]: item for item in record[key]}
        if len(tables[key]) != len(record[key]):
            errors.append(f"{key}: duplicate id")

    def refs(ids, table, where):
        for ident in ids:
            if ident not in tables[table]:
                errors.append(f"{where}: unknown {table} id {ident}")

    for node in record["nodes"]:
        if node["type"] == "hypothesis" and "evidence_state" not in node:
            errors.append(f"node {node['id']}: hypothesis needs evidence_state")
        if node.get("parent_id"):
            refs([node["parent_id"]], "nodes", node["id"])
            if tables["nodes"].get(node["parent_id"], {}).get("type") != "goal" or node["type"] != "goal":
                errors.append(f"node {node['id']}: parent_id belongs to goals")
        refs(node.get("evidence_refs", []), "evidence", node["id"])
        refs(node.get("document_refs", []), "documents", node["id"])
    for edge in record["edges"]:
        refs([edge["from"], edge["to"]], "nodes", edge["id"])
        if edge["from"] == edge["to"]:
            errors.append(f"edge {edge['id']}: self relationship")
    for group in record["prerequisites"]:
        refs([group["target_id"], *group["members"]], "nodes", group["id"])
        if group["target_id"] in group["members"]:
            errors.append(f"group {group['id']}: self prerequisite")
    if len({x["id"] for x in record["prerequisites"]}) != len(record["prerequisites"]):
        errors.append("prerequisites: duplicate id")
    for path in record["paths"]:
        refs(path["node_ids"], "nodes", path["id"])
        refs(path["goal_ids"], "nodes", path["id"])
        if any(tables["nodes"].get(x, {}).get("type") != "goal" for x in path["goal_ids"]):
            errors.append(f"path {path['id']}: goal_ids must refer to goals")
        if path.get("decision_id"):
            refs([path["decision_id"]], "decisions", path["id"])
        if path["state"] == "adopted":
            decision = tables["decisions"].get(path.get("decision_id"), {})
            if decision.get("action") not in ("adopt_strategy", "pivot"):
                errors.append(f"path {path['id']}: adopted path needs strategy decision")
    for decision in record["decisions"]:
        refs(decision["node_ids"], "nodes", decision["id"])
        refs(decision["evidence_refs"], "evidence", decision["id"])
        refs(decision["document_refs"], "documents", decision["id"])
        refs(decision["alternatives"], "paths", decision["id"])
        if decision["action"] == "final_adoption" and decision["actor"] != "user":
            errors.append(f"decision {decision['id']}: final adoption requires user")
        if decision["mode_at_decision"] in ("A", "B") and decision["action"] in ("adopt_strategy", "pivot") and decision["actor"] != "user":
            errors.append(f"decision {decision['id']}: strategy adoption requires user in A/B")
    recovery_roots, recovery_successors = set(), set()
    for recovery in record["recoveries"]:
        refs([recovery["path_id"]], "paths", recovery["id"])
        refs([recovery["failed_premise_id"]], "nodes", recovery["id"])
        refs([recovery["adopted_at_decision_id"], *recovery["reviewed_points"]], "decisions", recovery["id"])
        refs(recovery["reset_evidence_refs"], "evidence", recovery["id"])
        if recovery["backtracks"] > recovery["backtrack_limit"]:
            errors.append(f"recovery {recovery['id']}: backtrack limit exceeded")
        if recovery["attempts_at_point"] > recovery["attempt_limit"]:
            errors.append(f"recovery {recovery['id']}: attempt limit exceeded")
        context = (recovery["failed_premise_id"], recovery["adopted_at_decision_id"])
        prior_id = recovery.get("prior_episode_id")
        if prior_id:
            refs([prior_id], "recoveries", recovery["id"])
            if not recovery["reset_evidence_refs"]:
                errors.append(f"recovery {recovery['id']}: new episode needs meaningful change evidence")
            refs([recovery.get("reset_decision_id", "")], "decisions", recovery["id"])
            judgment = tables["decisions"].get(recovery.get("reset_decision_id"), {})
            if judgment.get("action") not in ("review", "advance", "pivot") or not set(recovery["reset_evidence_refs"]) <= set(judgment.get("evidence_refs", [])):
                errors.append(f"recovery {recovery['id']}: reset needs a decision citing the change evidence")
            before = tables["recoveries"].get(prior_id)
            if before and ((before["failed_premise_id"], before["adopted_at_decision_id"]) != context or before["status"] == "active"):
                errors.append(f"recovery {recovery['id']}: continue the same failure context after closing its prior episode")
            if prior_id in recovery_successors:
                errors.append(f"recovery {recovery['id']}: continue the latest episode, not a parallel reset")
            recovery_successors.add(prior_id)
        else:
            if context in recovery_roots:
                errors.append(f"recovery {recovery['id']}: same failure context needs a linked prior episode")
            recovery_roots.add(context)
        seen, cursor = set(), recovery
        while cursor:
            if cursor["id"] in seen:
                errors.append(f"recovery {recovery['id']}: cyclic episode ancestry")
                break
            seen.add(cursor["id"])
            cursor = tables["recoveries"].get(cursor.get("prior_episode_id"))
    # Only hard dependencies and goal ancestry must be acyclic. Evidence and
    # supersession relationships are not mistaken for execution prerequisites.
    adjacency = {key: [] for key in tables["nodes"]}
    for edge in record["edges"]:
        if edge["type"] == "requires" and edge["from"] in adjacency:
            adjacency[edge["from"]].append(edge["to"])
    for group in record["prerequisites"]:
        if group["operator"] == "any":
            continue  # alternative prerequisites are not all mandatory edges
        for member in group["members"]:
            if member in adjacency:
                adjacency[member].append(group["target_id"])
    for node in record["nodes"]:
        if node.get("parent_id") in adjacency:
            adjacency[node["parent_id"]].append(node["id"])
    pending, visited = set(), set()

    def visit(key):
        if key in pending:
            errors.append("nodes: cyclic hard dependency or goal ancestry")
            return
        if key in visited:
            return
        pending.add(key)
        for child in adjacency.get(key, []):
            visit(child)
        pending.remove(key)
        visited.add(key)

    for key in adjacency:
        visit(key)
    if errors:
        raise RecordError("\n".join(errors))
    return record


def load(path):
    try:
        return validate(json.loads(Path(path).read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        raise RecordError(str(exc)) from exc


def check_transition(old, new):
    if old["research_id"] != new["research_id"]:
        raise RecordError("research_id cannot change")
    if new["budget"]["spent"] < old["budget"]["spent"]:
        raise RecordError("cumulative budget spent cannot decrease")
    for key in ("nodes", "edges", "paths", "decisions", "recoveries", "documents", "evidence", "prerequisites"):
        prior = {x["id"]: x for x in old[key]}
        updated = {x["id"]: x for x in new[key]}
        if not prior.keys() <= updated.keys():
            raise RecordError(f"{key}: preserve prior records; supersede rather than delete")
        if key in ("decisions", "documents", "evidence"):
            if new[key][:len(old[key])] != old[key]:
                raise RecordError(f"{key}: append history in order; do not reorder prior entries")
            if any(updated[x] != value for x, value in prior.items()):
                raise RecordError(f"{key}: immutable history; append a new version")
        if key == "recoveries":
            for ident, before in prior.items():
                after = updated[ident]
                if any(after[x] < before[x] for x in ("backtracks", "attempts_at_point", "spent")):
                    raise RecordError("recovery counters cannot reset within an episode")
                if any(after[x] != before[x] for x in ("backtrack_limit", "attempt_limit", "path_id", "failed_premise_id", "adopted_at_decision_id")):
                    raise RecordError("preserve recovery identity and limits; amend through a new episode")
                if after["reviewed_points"][:len(before["reviewed_points"])] != before["reviewed_points"]:
                    raise RecordError("preserve reviewed upper points in order; append rather than erase or reorder")
                if any(after.get(x) != before.get(x) for x in ("prior_episode_id", "reset_evidence_refs", "reset_decision_id")):
                    raise RecordError("preserve episode reset provenance")
            old_decisions = {x["id"] for x in old["decisions"]}
            for ident in updated.keys() - prior.keys():
                episode = updated[ident]
                if episode.get("prior_episode_id") and episode.get("reset_decision_id") in old_decisions:
                    raise RecordError("a new episode needs a new meaningful-change judgment, not an old decision")


def writable_path(path):
    path = Path(path).absolute()
    if path.is_symlink():
        raise RecordError("refusing a symlink destination")
    if path.resolve().is_relative_to(ROOT):
        raise RecordError("research records belong in the workspace, outside the plugin package")
    return path


def save(path, proposal, expected_revision=None, create=False):
    path = writable_path(path)
    validate(proposal)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise RecordError("writer lock exists; inspect it, do not automatically clear it") from exc
    temporary = None
    try:
        os.close(fd)
        result = copy.deepcopy(proposal)
        if create:
            if path.exists():
                raise RecordError("record exists; refusing overwrite")
            result["revision"] = 0
        else:
            old = load(path)
            if expected_revision is None or old["revision"] != expected_revision:
                raise RecordError("revision conflict; re-read and reconcile before saving")
            check_transition(old, result)
            result["revision"] = old["revision"] + 1
        validate(result)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as f:
            temporary = Path(f.name)
            json.dump(result, f, ensure_ascii=False, indent=2, allow_nan=False)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
        return result
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
        lock.unlink()


def backtrack(record, episode_id, point_id, decision_id):
    result = copy.deepcopy(record)
    episode = next((x for x in result["recoveries"] if x["id"] == episode_id), None)
    if not episode or episode["status"] != "active":
        raise RecordError("unknown or inactive recovery episode")
    if point_id not in {x["id"] for x in result["decisions"]}:
        raise RecordError("unknown upper strategy decision; do not follow arbitrary parents")
    stopped = episode["backtracks"] >= episode["backtrack_limit"] or episode["attempts_at_point"] >= episode["attempt_limit"] or result["budget"]["spent"] >= result["budget"]["limit"]
    if stopped:
        episode["status"] = "stopped"
        reason = "Automatic recovery bound reached; untested alternatives may remain."
    else:
        episode["backtracks"] += 1
        episode["reviewed_points"].append(point_id)
        reason = "Review the selected upper strategy decision without resetting counters."
    result["decisions"].append({"id": decision_id, "timestamp": datetime.now(timezone.utc).isoformat(), "mode_at_decision": result["authority"]["mode"], "actor": "agent", "action": "hold" if stopped else "review", "summary": "Recovery stopped" if stopped else "Upper strategy review", "rationale": reason, "node_ids": [episode["failed_premise_id"]], "evidence_refs": [], "document_refs": [], "alternatives": [], "reviews": []})
    validate(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("file", type=Path)
    init.add_argument("--id", required=True)
    init.add_argument("--title", required=True)
    init.add_argument("--mode", choices=["A", "B", "C"], default="B")
    init.add_argument("--scope", default="Design only; execution contract not yet approved")
    init.add_argument("--budget-unit", default="calls")
    init.add_argument("--budget-limit", type=float, required=True)
    check = sub.add_parser("validate"); check.add_argument("file", type=Path)
    update = sub.add_parser("save"); update.add_argument("file", type=Path)
    update.add_argument("--proposal", required=True, type=Path)
    update.add_argument("--expected-revision", required=True, type=int)
    recover = sub.add_parser("backtrack"); recover.add_argument("file", type=Path)
    for name in ("episode", "point", "decision"):
        recover.add_argument(f"--{name}", required=True)
    recover.add_argument("--expected-revision", required=True, type=int)
    route = sub.add_parser("route"); route.add_argument("file", type=Path)
    route.add_argument("--runtime", choices=["codex", "claude"], required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            record = {"schema": "inquiry-research/v1", "research_id": args.id, "title": args.title, "revision": 0, "authority": {"mode": args.mode, "approved_scope": args.scope, "experiment_contracts": []}, "budget": {"unit": args.budget_unit, "limit": args.budget_limit, "spent": 0}, **{x: [] for x in ("nodes", "edges", "paths", "prerequisites", "decisions", "recoveries", "documents", "evidence")}}
            result = save(args.file, record, create=True)
        elif args.command == "save":
            result = save(args.file, load(args.proposal), args.expected_revision)
        elif args.command == "backtrack":
            result = save(args.file, backtrack(load(args.file), args.episode, args.point, args.decision), args.expected_revision)
        elif args.command == "route":
            record = load(args.file)
            invocation = "$inquiry:research" if args.runtime == "codex" else "/inquiry:research"
            print(f"For research strategy, evidence, or path decisions use {invocation}.\nResearch record: {args.file.resolve()}\nRead existing project goals/doc rules first; preserve their lifecycle and ownership.\nUse the record's mode and approved experiment contracts; viewing it grants no execution authority.")
            return 0
        else:
            result = load(args.file)
        print(json.dumps({"valid": True, "research_id": result["research_id"], "revision": result["revision"]}))
        return 0
    except (RecordError, OSError, RecursionError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
