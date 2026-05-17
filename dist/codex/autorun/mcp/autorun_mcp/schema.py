"""Deterministic plan schema checks for Autorun MCP."""

from __future__ import annotations

import re
from typing import Any, Mapping

VALID_HUMAN_GATES = {None, "approve", "execute"}
VALID_STATUSES = {"pending", "started", "verified", "committed", "retired"}
OPTIONAL_PLAN_SECTIONS = ("invariants", "surfaces", "criteria_map", "not_assessed")
VALID_ESTIMATED_SIZES = {"S", "M", "L"}
SPLIT_WARNING_CODES = {
    "broad_output_scope",
    "broad_spec_many_outputs",
    "compound_scope",
    "contract_many_surfaces",
    "helper_rollout_combined",
    "medium_task_needs_split",
    "oversized_task",
    "too_many_outputs",
    "too_many_requirements",
    "too_many_surfaces",
}
METADATA_WARNING_CODES = {"missing_output", "needs_granularity_metadata", "needs_metadata", "missing_required_field"}
BLOCKING_WARNING_CODES = {*SPLIT_WARNING_CODES, *METADATA_WARNING_CODES, "blocking_not_assessed"}
CRITICAL_NOT_ASSESSED_TERMS = (
    "authorization",
    "auth",
    "permission",
    "security",
    "tenant",
    "isolation",
    "access",
    "public",
    "token",
    "secret",
    "data integrity",
    "integrity",
    "contract",
    "compatibility",
    "migration",
    "execution",
    "sandbox",
)
BROAD_KEYWORDS = (
    "전체",
    "모든",
    "각각",
    "한번에",
    "한 번에",
    "전반",
    "리팩토링",
    "마이그레이션",
    "rollout",
    "all ",
    "every",
    "entire",
    "broad",
    "refactor",
    "migration",
)
COMPOUND_MARKERS = (
    " and ",
    " also ",
    " plus ",
    " as well as ",
    "그리고",
    "또한",
    "동시에",
    "까지",
)
SURFACE_TOKEN_RE = re.compile(
    r"(?:(?:GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+)?/[A-Za-z0-9_:{}/.*?-]+|"
    r"`[^`]*(?:/|\\.)[^`]*`|"
    r"\b[A-Za-z0-9_-]+(?:Service|Controller|Route|Routes|Endpoint|API|Api|Client|Provider|Repository|Store|Model|Schema|View|Viewer|Worker|Job|Command)s?\b"
)
APPLY_LIST_RE = re.compile(
    r"\b(?:apply|roll out|rollout|use|wire|migrate|update|적용|마이그레이션|연결)\b[^.\n:]*\b(?:to|across|for|에|에서)\b(?P<items>[^.\n]+)",
    re.IGNORECASE,
)
REQUIRED_TASK_FIELDS = (
    "id",
    "name",
    "blocked_by",
    "human_gate",
    "done",
    "spec",
)


def normalize_human_gate(value: Any) -> str | None:
    if value == "null":
        return None
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return str(value)


def normalize_output(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str) and item]
    return []


def validate_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    """Validate a stored plan and return stable, repeatable issues."""

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    meta = plan.get("meta")
    tasks = plan.get("tasks")
    if not isinstance(meta, dict):
        errors.append(_issue("missing_meta", None, "plan meta must be an object"))
    if not isinstance(tasks, list):
        errors.append(_issue("missing_tasks", None, "plan tasks must be a list"))
        return _result(errors, warnings)

    section_ids = _validate_optional_sections(plan, errors, warnings)

    ids: list[str] = []
    valid_tasks: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    duplicates: set[str] = set()
    task_by_id: dict[str, Mapping[str, Any]] = {}

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append(_issue("invalid_task", None, "task must be an object", index=index))
            continue

        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(_issue("missing_task_id", None, "task id is required", index=index))
            continue

        ids.append(task_id)
        valid_tasks.append(task)
        if task_id in seen:
            duplicates.add(task_id)
        else:
            seen.add(task_id)
            task_by_id[task_id] = task

        for field in REQUIRED_TASK_FIELDS:
            if field not in task:
                errors.append(
                    _issue(
                        "missing_required_field",
                        task_id,
                        f"{task_id}: missing required field {field}",
                        field=field,
                    )
                )

        blocked_by = task.get("blocked_by", [])
        if not isinstance(blocked_by, list) or not all(isinstance(dep, str) for dep in blocked_by):
            errors.append(_issue("invalid_blocked_by", task_id, f"{task_id}: blocked_by must be a list of ids"))

        human_gate = normalize_human_gate(task.get("human_gate"))
        if human_gate not in VALID_HUMAN_GATES:
            errors.append(
                _issue(
                    "invalid_human_gate",
                    task_id,
                    f"{task_id}: invalid human_gate {human_gate!r}",
                    human_gate=human_gate,
                )
            )

        status = task.get("status")
        if status is not None and status not in VALID_STATUSES:
            errors.append(
                _issue(
                    "invalid_status",
                    task_id,
                    f"{task_id}: invalid status {status!r}",
                    status=status,
                )
            )
        if status == "committed" and task.get("done") is not True:
            errors.append(_issue("invalid_status_done", task_id, f"{task_id}: status committed requires done true"))
        if status == "retired" and task.get("done") is not True:
            errors.append(_issue("invalid_status_done", task_id, f"{task_id}: status retired requires done true"))
        if status in {"pending", "started", "verified"} and task.get("done") is True:
            errors.append(_issue("invalid_status_done", task_id, f"{task_id}: status {status} requires done false"))

        lifecycle = task.get("lifecycle")
        if lifecycle is not None and not isinstance(lifecycle, dict):
            errors.append(_issue("invalid_lifecycle", task_id, f"{task_id}: lifecycle must be an object"))

        output = normalize_output(task.get("output"))
        if not output:
            errors.append(_issue("missing_output", task_id, f"{task_id}: missing output"))

    for task_id in sorted(duplicates):
        errors.append(_issue("duplicate_id", task_id, f"duplicate task id {task_id}"))

    unique_ids = set(task_by_id)
    for task in valid_tasks:
        task_id = str(task["id"])
        for blocker in sorted(set(task.get("blocked_by") or [])):
            if blocker not in unique_ids:
                errors.append(
                    _issue(
                        "missing_blocker",
                        task_id,
                        f"{task_id}: blocker {blocker} is missing",
                        blocker=blocker,
                    )
                )
        _validate_reference_list(
            task,
            "invariant_refs",
            section_ids["invariants"],
            errors,
            "missing_invariant_ref",
            task_id=task_id,
        )
        _validate_reference_list(
            task,
            "surface_refs",
            section_ids["surfaces"],
            errors,
            "missing_surface_ref",
            task_id=task_id,
        )
        _validate_reference_list(
            task,
            "criteria_refs",
            section_ids["criteria_map"],
            errors,
            "missing_criteria_ref",
            task_id=task_id,
        )
        if _task_has_assessment_refs(task) and not normalize_output(task.get("verify_checks")):
            warnings.append(
                _issue(
                    "missing_verify_checks",
                    task_id,
                    f"{task_id}: invariant or criteria references should include verify_checks",
                )
            )

    for cycle in _dependency_cycles(task_by_id):
        errors.append(
            _issue(
                "dependency_cycle",
                cycle[0] if cycle else None,
                "dependency cycle: " + " -> ".join(cycle),
                cycle=cycle,
            )
        )

    for task_id in ids:
        task = task_by_id.get(task_id)
        if task is None:
            continue
        warnings.extend(granularity_issues(task))

    return _result(errors, warnings)


def granularity_issues(task: Mapping[str, Any]) -> list[dict[str, Any]]:
    task_id = str(task.get("id", ""))
    spec = task.get("spec")
    spec_text = spec if isinstance(spec, str) else ""
    output = normalize_output(task.get("output"))
    issues: list[dict[str, Any]] = []
    estimated_size = task.get("estimated_size")
    broad = _has_broad_keyword(spec_text)
    requirement_count = _requirement_count(spec_text)
    surface_groups = _surface_groups(spec_text)
    compound_marker_count = _compound_marker_count(spec_text)

    if estimated_size is None:
        issues.append(_issue("needs_granularity_metadata", task_id, f"{task_id}: missing estimated_size"))
    elif estimated_size not in VALID_ESTIMATED_SIZES:
        issues.append(
            _issue(
                "needs_granularity_metadata",
                task_id,
                f"{task_id}: estimated_size must be S, M, or L",
                estimated_size=estimated_size,
            )
        )

    if estimated_size == "L":
        issues.append(_issue("oversized_task", task_id, f"{task_id}: estimated_size L should be split"))
    if estimated_size == "M" and (broad or requirement_count > 4 or len(output) > 2):
        issues.append(
            _issue(
                "medium_task_needs_split",
                task_id,
                f"{task_id}: estimated_size M with broad scope should be split into commit-sized tasks",
                requirement_count=requirement_count,
                output_count=len(output),
            )
        )

    if len(output) > 3:
        issues.append(_issue("too_many_outputs", task_id, f"{task_id}: more than 3 output paths", output_count=len(output)))

    if broad and len(output) > 2:
        issues.append(
            _issue(
                "broad_spec_many_outputs",
                task_id,
                f"{task_id}: broad spec with more than 2 outputs should be split",
                output_count=len(output),
            )
        )

    if requirement_count > 5:
        issues.append(
            _issue(
                "too_many_requirements",
                task_id,
                f"{task_id}: more than 5 required behavior bullets should be split",
                requirement_count=requirement_count,
            )
        )

    if len(surface_groups) > 2:
        issues.append(
            _issue(
                "too_many_surfaces",
                task_id,
                f"{task_id}: multiple implementation surfaces should be split",
                surfaces=surface_groups,
            )
        )

    if _has_broad_output(output) and (broad or len(output) > 1):
        issues.append(
            _issue(
                "broad_output_scope",
                task_id,
                f"{task_id}: directory or glob output scope is too broad for execution",
                output=output,
            )
        )

    if _mentions_helper_rollout(spec_text, surface_groups):
        issues.append(
            _issue(
                "helper_rollout_combined",
                task_id,
                f"{task_id}: shared foundation work and broad rollout should be separate tasks",
                surfaces=surface_groups,
            )
        )

    if _mentions_contract_update(spec_text, output) and len(surface_groups) > 1:
        issues.append(
            _issue(
                "contract_many_surfaces",
                task_id,
                f"{task_id}: behavior and contract/documentation updates across multiple surfaces should be split",
                surfaces=surface_groups,
            )
        )

    if compound_marker_count > 3 and (len(output) > 2 or requirement_count > 4):
        issues.append(
            _issue(
                "compound_scope",
                task_id,
                f"{task_id}: compound scope should be split into commit-sized tasks",
                compound_marker_count=compound_marker_count,
            )
        )

    if not output or (_only_directory_outputs(output) and broad):
        issues.append(_issue("needs_metadata", task_id, f"{task_id}: output metadata is too broad"))

    return issues


def has_split_issue(validation: Mapping[str, Any]) -> bool:
    return any(issue.get("code") in SPLIT_WARNING_CODES for issue in validation.get("warnings", []))


def has_metadata_issue(validation: Mapping[str, Any]) -> bool:
    return any(issue.get("code") in METADATA_WARNING_CODES for issue in validation.get("errors", [])) or any(
        issue.get("code") in METADATA_WARNING_CODES for issue in validation.get("warnings", [])
    )


def blocking_warnings(validation: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [dict(issue) for issue in validation.get("warnings", []) if issue.get("code") in BLOCKING_WARNING_CODES]


def nonblocking_warnings(validation: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [dict(issue) for issue in validation.get("warnings", []) if issue.get("code") not in BLOCKING_WARNING_CODES]


def _validate_optional_sections(
    plan: Mapping[str, Any],
    errors: list[dict[str, Any]],
    warnings: list[dict[str, Any]],
) -> dict[str, set[str]]:
    ids_by_section: dict[str, set[str]] = {section: set() for section in OPTIONAL_PLAN_SECTIONS}
    for section in OPTIONAL_PLAN_SECTIONS:
        value = plan.get(section, [])
        if value is None:
            value = []
        if not isinstance(value, list):
            errors.append(_issue("invalid_section", None, f"{section} must be a list", section=section))
            continue

        seen: set[str] = set()
        duplicates: set[str] = set()
        for index, item in enumerate(value):
            if not isinstance(item, dict):
                errors.append(
                    _issue(
                        "invalid_section_item",
                        None,
                        f"{section}[{index}] must be an object",
                        section=section,
                        index=index,
                    )
                )
                continue
            item_id = item.get("id")
            if not isinstance(item_id, str) or not item_id:
                errors.append(
                    _issue(
                        "missing_section_item_id",
                        None,
                        f"{section}[{index}]: id is required",
                        section=section,
                        index=index,
                    )
                )
                continue
            if item_id in seen:
                duplicates.add(item_id)
            seen.add(item_id)
            ids_by_section[section].add(item_id)
            if section == "not_assessed":
                warnings.extend(_not_assessed_warnings(item))

        for duplicate in sorted(duplicates):
            errors.append(
                _issue(
                    "duplicate_section_item_id",
                    None,
                    f"{section}: duplicate id {duplicate}",
                    section=section,
                    ref=duplicate,
                )
            )

    _validate_section_references(plan, ids_by_section, errors)
    return ids_by_section


def _validate_section_references(
    plan: Mapping[str, Any],
    ids_by_section: Mapping[str, set[str]],
    errors: list[dict[str, Any]],
) -> None:
    for item in _section_items(plan, "invariants"):
        item_id = str(item.get("id"))
        _validate_reference_list(
            item,
            "surfaces",
            ids_by_section["surfaces"],
            errors,
            "missing_surface_ref",
            section="invariants",
            item_id=item_id,
        )

    task_ids = {str(task.get("id")) for task in plan.get("tasks", []) if isinstance(task, dict) and isinstance(task.get("id"), str)}
    for item in _section_items(plan, "criteria_map"):
        item_id = str(item.get("id"))
        _validate_reference_list(
            item,
            "invariants",
            ids_by_section["invariants"],
            errors,
            "missing_invariant_ref",
            section="criteria_map",
            item_id=item_id,
        )
        _validate_reference_list(
            item,
            "surfaces",
            ids_by_section["surfaces"],
            errors,
            "missing_surface_ref",
            section="criteria_map",
            item_id=item_id,
        )
        _validate_reference_list(
            item,
            "tasks",
            task_ids,
            errors,
            "missing_task_ref",
            section="criteria_map",
            item_id=item_id,
        )


def _section_items(plan: Mapping[str, Any], section: str) -> list[Mapping[str, Any]]:
    value = plan.get(section, [])
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict) and isinstance(item.get("id"), str)]


def _validate_reference_list(
    item: Mapping[str, Any],
    field: str,
    known_ids: set[str],
    errors: list[dict[str, Any]],
    missing_code: str,
    **context: Any,
) -> None:
    if field not in item:
        return
    value = item.get(field)
    owner = context.get("task_id") or context.get("item_id") or "item"
    if not isinstance(value, list) or not all(isinstance(ref, str) for ref in value):
        details = {key: item for key, item in context.items() if key != "task_id"}
        errors.append(
            _issue(
                "invalid_reference_list",
                context.get("task_id"),
                f"{owner}: {field} must be a list of ids",
                field=field,
                **details,
            )
        )
        return
    for ref in sorted(set(value)):
        if ref not in known_ids:
            details = {key: item for key, item in context.items() if key != "task_id"}
            errors.append(
                _issue(
                    missing_code,
                    context.get("task_id"),
                    f"{owner}: {field} references missing id {ref}",
                    field=field,
                    ref=ref,
                    **details,
                )
            )


def _task_has_assessment_refs(task: Mapping[str, Any]) -> bool:
    return any(task.get(field) for field in ("invariant_refs", "surface_refs", "criteria_refs"))


def _not_assessed_warnings(item: Mapping[str, Any]) -> list[dict[str, Any]]:
    item_id = str(item.get("id"))
    area = str(item.get("area") or item.get("name") or item_id)
    risk = str(item.get("risk") or "").lower()
    blocks_ready = item.get("blocks_ready")
    inferred_block = blocks_ready is None and risk == "high" and _critical_not_assessed_area(area)
    if blocks_ready is True or inferred_block:
        return [
            _issue(
                "blocking_not_assessed",
                None,
                f"{item_id}: not_assessed blocks readiness for {area}",
                not_assessed_id=item_id,
                risk=risk or None,
                surface=f"area:{area}",
                inferred_blocks_ready=inferred_block,
            )
        ]
    if risk == "high":
        return [
            _issue(
                "high_risk_not_assessed",
                None,
                f"{item_id}: high-risk area remains not assessed: {area}",
                not_assessed_id=item_id,
                risk=risk,
                surface=f"area:{area}",
            )
        ]
    return []


def _critical_not_assessed_area(area: str) -> bool:
    normalized = area.lower()
    return any(term in normalized for term in CRITICAL_NOT_ASSESSED_TERMS)


def _dependency_cycles(task_by_id: Mapping[str, Mapping[str, Any]]) -> list[list[str]]:
    adjacency = {
        task_id: sorted(dep for dep in (task.get("blocked_by") or []) if dep in task_by_id)
        for task_id, task in sorted(task_by_id.items())
    }
    cycles: list[list[str]] = []
    seen_cycles: set[tuple[str, ...]] = set()
    visited: set[str] = set()
    visiting: list[str] = []

    def visit(task_id: str) -> None:
        if task_id in visiting:
            cycle = visiting[visiting.index(task_id) :] + [task_id]
            canonical = _canonical_cycle(cycle)
            if canonical not in seen_cycles:
                seen_cycles.add(canonical)
                cycles.append(list(canonical) + [canonical[0]])
            return
        if task_id in visited:
            return
        visiting.append(task_id)
        for dep in adjacency.get(task_id, []):
            visit(dep)
        visiting.pop()
        visited.add(task_id)

    for task_id in sorted(adjacency):
        visit(task_id)

    cycles.sort(key=lambda item: "->".join(item))
    return cycles


def _canonical_cycle(cycle: list[str]) -> tuple[str, ...]:
    body = cycle[:-1] if len(cycle) > 1 and cycle[0] == cycle[-1] else cycle
    rotations = [tuple(body[index:] + body[:index]) for index in range(len(body))]
    return min(rotations)


def _only_directory_outputs(outputs: list[str]) -> bool:
    if not outputs:
        return False
    return all(path.endswith("/") or "." not in path.rsplit("/", 1)[-1] for path in outputs)


def _has_broad_output(outputs: list[str]) -> bool:
    return any("*" in path or path.endswith("/") or "." not in path.rsplit("/", 1)[-1] for path in outputs)


def _has_broad_keyword(spec: str) -> bool:
    normalized = spec.lower()
    return any(keyword in normalized for keyword in BROAD_KEYWORDS)


def _compound_marker_count(spec: str) -> int:
    normalized = spec.lower()
    return sum(normalized.count(marker) for marker in COMPOUND_MARKERS)


def _requirement_count(spec: str) -> int:
    return len([line for line in spec.splitlines() if line.lstrip().startswith(("- ", "* "))])


def _surface_groups(spec: str) -> list[str]:
    normalized = spec.lower()
    surfaces: set[str] = set()

    for match in SURFACE_TOKEN_RE.finditer(spec):
        token = match.group(0).strip("`").strip()
        surface = _surface_from_token(token)
        if surface:
            surfaces.add(surface)

    for match in APPLY_LIST_RE.finditer(spec):
        items = re.split(r",|/|\band\b|\b및\b|\b와\b|\b과\b", match.group("items"), flags=re.IGNORECASE)
        for item in items:
            item = item.strip(" `:;()[]{}")
            if not item:
                continue
            if len(item.split()) > 4:
                continue
            surfaces.add("area:" + item.lower())

    if "openapi" in normalized or "swagger" in normalized:
        surfaces.add("contract:openapi")
    if "api contract" in normalized or "schema" in normalized or "contract" in normalized:
        surfaces.add("contract:api")

    return sorted(surfaces)


def _surface_from_token(token: str) -> str | None:
    if not token:
        return None
    route_match = re.match(r"^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(/.+)$", token, flags=re.IGNORECASE)
    if route_match:
        return "route:" + route_match.group(1).upper() + " " + _normalize_route_path(route_match.group(2))
    if token.startswith("/"):
        return "route:ANY " + _normalize_route_path(token)
    lowered = token.lower()
    if "/" in lowered or "\\" in lowered:
        return "file:" + _normalize_file_surface_path(lowered)
    return "component:" + lowered


def _mentions_helper_rollout(spec: str, surface_groups: list[str]) -> bool:
    normalized = spec.lower()
    helper = (
        "helper" in normalized
        or "foundation" in normalized
        or "base" in normalized
        or "shared" in normalized
        or "common" in normalized
        or "공용" in normalized
        or "기반" in normalized
    )
    rollout = "apply" in normalized or "rollout" in normalized or "적용" in normalized or "use it" in normalized
    return helper and rollout and len(surface_groups) > 1


def _mentions_contract_update(spec: str, outputs: list[str]) -> bool:
    normalized = spec.lower()
    return (
        "openapi" in normalized
        or "swagger" in normalized
        or "schema" in normalized
        or "contract" in normalized
        or "documentation" in normalized
        or "docs" in normalized
        or any(path.endswith(("openapi.js", "schema.json", "schema.yaml", "schema.yml")) for path in outputs)
    )


def _issue(code: str, task_id: str | None, message: str, **details: Any) -> dict[str, Any]:
    issue = {"code": code, "task_id": task_id, "message": message}
    issue.update(details)
    return issue


def _result(errors: list[dict[str, Any]], warnings: list[dict[str, Any]]) -> dict[str, Any]:
    normalized_warnings = [_normalize_issue_surfaces(issue) for issue in warnings]
    return {
        "valid": not errors,
        "schema_valid": not errors,
        "errors": errors,
        "warnings": normalized_warnings,
    }


def _normalize_issue_surfaces(issue: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(issue)
    original: list[str] = []
    surfaces: list[str] = []

    raw_surfaces = normalized.get("surfaces")
    if isinstance(raw_surfaces, list):
        for item in raw_surfaces:
            if isinstance(item, str):
                original.append(item)
                surface = _normalize_surface_identifier(item)
                if surface:
                    surfaces.append(surface)
    raw_surface = normalized.get("surface")
    if isinstance(raw_surface, str):
        original.append(raw_surface)
        surface = _normalize_surface_identifier(raw_surface)
        if surface:
            surfaces.append(surface)
    output = normalize_output(normalized.get("output"))
    for path in output:
        surface = _normalize_surface_identifier("file:" + path)
        if surface:
            surfaces.append(surface)

    if surfaces:
        normalized["surfaces"] = sorted(set(surfaces))
        if original:
            normalized["original_surfaces"] = original
    elif "surfaces" in normalized and not isinstance(normalized["surfaces"], list):
        normalized.pop("surfaces", None)
    return normalized


def _normalize_surface_identifier(value: str) -> str | None:
    value = " ".join(value.strip().split())
    if not value or len(value) > 160:
        return None
    lowered = value.lower()
    if lowered.startswith("path:"):
        return "file:" + _normalize_file_surface_path(value[5:])
    if lowered.startswith("file:"):
        path = value.split(":", 1)[1]
        return "file:" + _normalize_file_surface_path(path)
    if lowered.startswith("route:"):
        route = value.split(":", 1)[1].strip()
        route_match = re.match(r"^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|ANY)\s+(/.*)$", route, flags=re.IGNORECASE)
        if route_match:
            return "route:" + route_match.group(1).upper() + " " + _normalize_route_path(route_match.group(2))
        if route.startswith("/"):
            return "route:ANY " + _normalize_route_path(route)
        return None
    if lowered.startswith(("component:", "contract:", "channel:", "job:", "command:", "data:", "area:")):
        prefix, body = value.split(":", 1)
        body = " ".join(body.strip().split())
        if not body or len(body) > 120:
            return None
        return prefix.lower() + ":" + body
    if value.startswith("/"):
        return "route:ANY " + _normalize_route_path(value)
    if "/" in value or "\\" in value:
        return "file:" + _normalize_file_surface_path(value)
    if len(value.split()) <= 3:
        return "area:" + value.lower()
    return None


def _normalize_route_path(path: str) -> str:
    path = "/" + path.strip().lstrip("/")
    parts = []
    for part in path.split("/"):
        if not part or part in {"*", "**"} or part.startswith(":"):
            continue
        parts.append(part.lower())
        if len(parts) >= 2:
            break
    return "/" + "/".join(parts) if parts else "/"


def _normalize_file_surface_path(path: str) -> str:
    return "/".join(part for part in path.replace("\\", "/").strip(" `").split("/") if part and part not in {".", "*", "**"})
