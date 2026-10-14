#!/usr/bin/env python3
"""Portable, standard-library source registration, checks and report output.

Semantic analysis/review belongs to the skills. This tool never infers that a
claim is supported just because its references exist.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import tempfile
import os
import uuid
from pathlib import Path
from urllib.parse import urlsplit

PACKAGE = Path(__file__).resolve().parents[1]
ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
CITE = re.compile(r"\[@([A-Za-z][A-Za-z0-9_-]*)\]")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def digest_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, text, force=False):
    path = Path(path)
    if path.exists() and not force:
        raise ValueError(f"Output exists: {path}; select another path or explicitly use --force")
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False) as stream:
        temporary = stream.name
        stream.write(text)
    os.replace(temporary, path)


def read_bundle(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Expected Folio schema_version 1 object")
    for name in ("sources", "evidence", "claims", "context"):
        if not isinstance(data.get(name), list):
            raise ValueError(f"{name} must be an array")
    if not isinstance(data.get("report"), str) or not isinstance(data.get("sharing"), dict):
        raise ValueError("report must be text and sharing must be an object")
    return data


def revision(data):
    # Public presentation settings do not imply renewed semantic verification.
    return fingerprint({key: data[key] for key in
                        ("sources", "evidence", "claims", "context", "report")})


def safe_url(value):
    if not isinstance(value, str) or any(ord(c) < 32 for c in value):
        return ""
    try:
        parsed = urlsplit(value)
    except ValueError:
        return ""
    return value if parsed.scheme in ("https", "http") and parsed.netloc else ""


def empty_bundle(title=""):
    return {"schema_version": 1, "title": title, "purpose": "", "context": [],
            "sources": [], "evidence": [], "claims": [], "report": "",
            "verification": None, "sharing": {"include_sources": []}}


def register(path, source_id, title=None, shared_url=""):
    path = Path(path).resolve()
    text = path.read_text(encoding="utf-8-sig")
    if not ID.fullmatch(source_id):
        raise ValueError("Source ID must start with a letter and use letters/digits/_/-")
    source = {"id": source_id, "title": title or path.name, "origin": path.name,
              "local_path": str(path), "sha256": digest_file(path),
              "shared_url": shared_url, "units": []}
    if shared_url and not safe_url(shared_url):
        raise ValueError("Shared URL must be http(s)")
    if path.suffix.lower() == ".csv":
        import io
        reader = csv.DictReader(io.StringIO(text, newline=""))
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("CSV needs unique column headers")
        source["kind"] = "survey"
        for row_number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV row {row_number}")
            source["units"].append({"id": f"r{row_number}",
                                    "locator": f"CSV row {row_number}",
                                    "text": json.dumps(row, ensure_ascii=False), "fields": row})
    else:
        source["kind"] = "document"
        heading = ""
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith("#"):
                heading = line.lstrip("# ")
            if line.strip():
                timestamp = re.search(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", line)
                locator = f"line {line_number}" + (f", {heading}" if heading else "")
                if timestamp:
                    locator += f", {timestamp.group()}"
                source["units"].append({"id": f"l{line_number}", "locator": locator,
                                        "text": line})
    source["snapshot_sha256"] = fingerprint(source["units"])
    return source


def select_rows(source, conditions):
    units = source["units"]
    for condition in conditions:
        column, op = condition["column"], condition["op"]
        if op not in ("eq", "ne", "nonempty"):
            raise ValueError(f"Unsupported aggregate operator: {op}")
        if any(column not in unit.get("fields", {}) for unit in units):
            raise ValueError(f"Unknown CSV column: {column}")
        value = condition.get("value", "")
        units = [unit for unit in units if
                 (unit["fields"][column] == value if op == "eq" else
                  unit["fields"][column] != value if op == "ne" else
                  bool(unit["fields"][column].strip()))]
    return units


def aggregate(source, spec):
    if source.get("kind") != "survey":
        raise ValueError("Aggregate requires CSV survey source")
    population = {**source, "units": select_rows(source, spec.get("population", []))}
    matched = select_rows(population, spec.get("match", []))
    denominator = len(population["units"])
    return {"numerator": len(matched), "denominator": denominator,
            "percent": round(100 * len(matched) / denominator, 4) if denominator else None,
            "population_units": [unit["id"] for unit in population["units"]],
            "matched_units": [unit["id"] for unit in matched]}


def validate(data, check_files=False):
    errors, warnings = [], []
    maps = {}
    # Fail shape errors before dereferencing IDs or nested locators.
    for collection in ("sources", "evidence", "claims"):
        if any(not isinstance(item, dict) for item in data[collection]):
            return {"errors": [f"{collection}: every item must be an object"], "warnings": [], "revision": revision(data)}
    for source in data["sources"]:
        units = source.get("units")
        if not isinstance(units, list) or any(not isinstance(unit, dict) or
                not isinstance(unit.get("id"), str) or not isinstance(unit.get("locator"), str) or
                not isinstance(unit.get("text"), str) for unit in units):
            return {"errors": ["Source units need text IDs, locators and text"], "warnings": [], "revision": revision(data)}
    for item in data["evidence"]:
        if not isinstance(item.get("source"), str) or (item.get("kind") == "quote" and
                (not isinstance(item.get("unit"), str) or not isinstance(item.get("quote"), str))):
            return {"errors": ["Evidence needs source and exact quote/unit strings"], "warnings": [], "revision": revision(data)}
    if data.get("verification") is not None and not isinstance(data["verification"], dict):
        return {"errors": ["verification must be an object or null"], "warnings": [], "revision": revision(data)}
    for collection in ("sources", "evidence", "claims"):
        index = {}
        for item in data[collection]:
            if not isinstance(item, dict):
                errors.append(f"{collection}: expected object")
                continue
            key = item.get("id", "")
            if not isinstance(key, str) or not ID.fullmatch(key) or key in index:
                errors.append(f"{collection}: invalid or duplicate ID {key!r}")
            index[key] = item
        maps[collection] = index
    sources = maps["sources"]
    for source_id, source in sources.items():
        if not source.get("title") or not source.get("origin") or not source.get("sha256"):
            errors.append(f"{source_id}: title, origin and sha256 required")
        units = source.get("units")
        if not isinstance(units, list):
            errors.append(f"{source_id}: units must be array")
            continue
        if source.get("snapshot_sha256") != fingerprint(units):
            errors.append(f"{source_id}: snapshot changed; refresh and revalidate")
        keys = set()
        for unit in units:
            key = unit.get("id", "")
            if not ID.fullmatch(key) or key in keys or not isinstance(unit.get("text"), str) or not unit.get("locator"):
                errors.append(f"{source_id}: invalid/duplicate unit or missing locator {key}")
            keys.add(key)
        if source.get("shared_url") and not safe_url(source["shared_url"]):
            errors.append(f"{source_id}: unsafe shared URL")
        if check_files and source.get("local_path"):
            path = Path(source["local_path"])
            if not path.is_file():
                warnings.append(f"{source_id}: original unavailable; using recorded snapshot")
            elif digest_file(path) != source["sha256"]:
                errors.append(f"{source_id}: original changed; refresh source and revalidate")
    for key, item in maps["evidence"].items():
        source = sources.get(item.get("source"))
        if not source:
            errors.append(f"{key}: source missing")
            continue
        units = {unit["id"]: unit for unit in source.get("units", [])}
        if item.get("kind") == "quote":
            unit = units.get(item.get("unit"))
            if not unit or not item.get("quote") or item["quote"] not in unit["text"]:
                errors.append(f"{key}: quote does not match the exact source unit")
        elif item.get("kind") == "aggregate":
            try:
                result = aggregate(source, item["calculation"])
                if item.get("result") != result:
                    errors.append(f"{key}: aggregate result/denominator/row membership mismatch")
            except (ValueError, KeyError, TypeError) as exc:
                errors.append(f"{key}: invalid calculation: {exc}")
        elif item.get("kind") == "calculation":
            refs = item.get("units", [])
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in units for ref in refs) or not item.get("method") or "result" not in item:
                errors.append(f"{key}: calculation needs source units, method and result")
            warnings.append(f"{key}: non-count arithmetic requires independent semantic review")
        else:
            errors.append(f"{key}: expected quote, aggregate or calculation evidence")
    for key, claim in maps["claims"].items():
        if claim.get("provenance") not in ("source", "interpretation", "user_context"):
            errors.append(f"{key}: provenance must be source, interpretation or user_context")
        if not isinstance(claim.get("text"), str) or not claim["text"] or claim["text"] not in data["report"]:
            errors.append(f"{key}: claim text missing from report")
        refs = claim.get("evidence", [])
        if not isinstance(refs, list):
            errors.append(f"{key}: evidence must be array")
            continue
        if not refs and claim.get("provenance") != "user_context":
            errors.append(f"{key}: unsupported claim; supply evidence or remove claim")
        for ref in refs:
            if not isinstance(ref, str) or ref not in maps["evidence"]:
                errors.append(f"{key}: unknown evidence {ref}")
        if claim.get("provenance") == "user_context" and not claim.get("context"):
            errors.append(f"{key}: user-context claim needs context explanation")
    for ref in CITE.findall(data["report"]):
        if ref not in maps["evidence"]:
            errors.append(f"Report citation references missing evidence {ref}")
    included = data["sharing"].get("include_sources", [])
    if not isinstance(included, list) or any(not isinstance(key, str) for key in included) or len(included) != len(set(included)):
        errors.append("include_sources must be a unique array")
    elif any(key not in sources for key in included):
        errors.append("include_sources references missing source")
    verification = data.get("verification")
    if verification:
        if verification.get("revision") != revision(data):
            warnings.append("Semantic review is stale; current content is not reviewed")
        elif verification.get("status") != "reviewed":
            warnings.append("Semantic review remains unresolved")
    else:
        warnings.append("No independent semantic review recorded")
    return {"errors": errors, "warnings": warnings, "revision": revision(data)}


def review_status(data):
    review = data.get("verification")
    if not review:
        return "Independent source review not recorded"
    if review.get("revision") != revision(data):
        return "Source review stale: content changed"
    if review.get("status") != "reviewed":
        return "Source review: unresolved findings"
    return "Source review recorded for this revision"


def citations(data):
    keys = list(dict.fromkeys(CITE.findall(data["report"])))
    return {key: i + 1 for i, key in enumerate(keys)}


def evidence_text(item):
    if item["kind"] == "quote":
        return item["quote"]
    if item["kind"] == "calculation":
        return f"Result: {item['result']}. Method: {item['method']}. Units: {', '.join(item['units'])}"
    result = item["result"]
    return (f"{result['numerator']}/{result['denominator']} ({result['percent']}%). "
            f"Calculation: {json.dumps(item['calculation'], ensure_ascii=False)}. "
            f"Population: {', '.join(result['population_units'])}; "
            f"matched: {', '.join(result['matched_units'])}")


def source_trace(source, item):
    if item["kind"] == "quote":
        unit = next(unit for unit in source["units"] if unit["id"] == item["unit"])
        location = unit["locator"]
    elif item["kind"] == "calculation":
        unit_map = {unit["id"]: unit for unit in source["units"]}
        location = "; ".join(unit_map[key]["locator"] for key in item["units"])
    else:
        location = "CSV aggregate; row membership and calculation below"
    return f"{source['title']} ({source['origin']}), {location}; source {source['id']}"


def markdown(data):
    numbers = citations(data)
    text = CITE.sub(lambda match: f"[^{numbers[match[1]]}]", data["report"])
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda match: match[0] if safe_url(match[2]) or match[2].startswith("#")
                  else match[1] + " (original link unavailable to recipients)", text)
    lines = [text, "", "---", "", review_status(data)]
    review = data.get("verification") or {}
    for finding in review.get("findings", []):
        lines.append(f"- Review note: {finding['reason']}")
    index = {item["id"]: item for item in data["evidence"]}
    sources = {item["id"]: item for item in data["sources"]}
    for key, number in numbers.items():
        item, source = index[key], sources[index[key]["source"]]
        trail = source_trace(source, item)
        quote = evidence_text(item).replace("\n", " ")
        url = safe_url(source.get("shared_url", ""))
        access = f"Shared source: <{url}> (access depends on recipient permissions)." if url else (
            "Original is not attached; locate or request it using the document identity and position above.")
        # Plain prose avoids converting source quotations to active Markdown links.
        quote = re.sub(r"([\\`*_{}\[\]<>])", r"\\\1", quote)
        lines.extend(["", f"[^{number}]: {trail}. {quote}", f"    {access}"])
    return "\n".join(lines) + "\n"


def inline(text, numbers):
    # Escape first; raw input HTML is never active. Process only safe URLs.
    tokens = {}
    prefix = "FOLIO" + uuid.uuid4().hex
    def stash(value):
        key = f"{prefix}{len(tokens)}END"
        tokens[key] = value
        return key
    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{html.escape(m[1])}</code>"), text)
    text = CITE.sub(lambda m: stash(f'<a class="citation" href="#evidence/{m[1]}" data-evidence="{m[1]}" aria-label="Evidence {numbers[m[1]]}"><sup>{numbers[m[1]]}</sup></a>'), text)
    def link(match):
        url = safe_url(match[2])
        label = html.escape(match[1])
        return stash(f'<a href="{html.escape(url, quote=True)}" rel="noopener noreferrer">{label}</a>') if url else stash(label)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    for key, value in tokens.items():
        text = text.replace(key, value)
    return text


def render_prose(text, numbers):
    blocks, paragraph, list_tag, code = [], [], None, None
    def flush():
        if paragraph:
            blocks.append("<p>" + "<br>".join(inline(line, numbers) for line in paragraph) + "</p>")
            paragraph.clear()
    def close_list():
        nonlocal list_tag
        if list_tag:
            blocks.append(f"</{list_tag}>")
            list_tag = None
    lines = text.splitlines()
    skip = 0
    for position, line in enumerate(lines):
        if position < skip:
            continue
        if line.startswith("```"):
            flush(); close_list()
            if code is None:
                code = []
            else:
                blocks.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code = None
            continue
        if code is not None:
            code.append(line); continue
        if "|" in line and position + 1 < len(lines) and re.fullmatch(
                r"\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*", lines[position + 1]):
            flush(); close_list()
            def cells(row):
                return [inline(cell.strip(), numbers) for cell in row.strip().strip("|").split("|")]
            blocks.append("<div class=table-scroll><table><thead><tr>" +
                          "".join(f"<th>{cell}</th>" for cell in cells(line)) + "</tr></thead><tbody>")
            skip = position + 2
            while skip < len(lines) and "|" in lines[skip] and lines[skip].strip():
                blocks.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells(lines[skip])) + "</tr>")
                skip += 1
            blocks.append("</tbody></table></div>")
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        bullet = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.+)$", line)
        if heading:
            flush(); close_list()
            level = len(heading[1]); blocks.append(f"<h{level}>{inline(heading[2], numbers)}</h{level}>")
        elif bullet:
            flush()
            tag = "ol" if re.match(r"^\s*\d", line) else "ul"
            if list_tag != tag:
                close_list(); list_tag = tag; blocks.append(f"<{tag}>")
            blocks.append(f"<li>{inline(bullet[1], numbers)}</li>")
        elif line.startswith("> "):
            flush(); close_list()
            blocks.append("<blockquote>" + inline(line[2:], numbers) + "</blockquote>")
        elif not line.strip():
            flush(); close_list()
        else:
            close_list(); paragraph.append(line)
    flush(); close_list()
    if code is not None:
        blocks.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
    return "\n".join(blocks)


def webpage(data):
    numbers = citations(data)
    included = set(data["sharing"].get("include_sources", []))
    public_sources = [{key: source[key] for key in
                       ("id", "title", "origin", "kind", "sha256", "shared_url", "units", "coverage") if key in source}
                      for source in data["sources"]]
    for source in public_sources:
        source["included"] = source["id"] in included
        if not source["included"]:
            source["units"] = []
    source_map = {source["id"]: source for source in data["sources"]}
    evidence = [{**item, "display_text": evidence_text(item),
                 "trace": source_trace(source_map[item["source"]], item),
                 "number": numbers.get(item["id"])} for item in data["evidence"]]
    payload = {"sources": public_sources, "evidence": evidence,
               "review": review_status(data),
               "findings": (data.get("verification") or {}).get("findings", [])}
    template = (PACKAGE / "assets" / "shell.html").read_text()
    replacements = {"TITLE": html.escape(data.get("title") or "Report"),
                    "PROSE": render_prose(data["report"], numbers),
                    "DATA": json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c"),
                    "STYLE": (PACKAGE / "assets" / "style.css").read_text(),
                    "SCRIPT": (PACKAGE / "assets" / "app.js").read_text()}
    return re.sub(r"\{\{(TITLE|PROSE|DATA|STYLE|SCRIPT)\}\}",
                  lambda match: replacements[match[1]], template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init"); init.add_argument("output"); init.add_argument("--title", default="")
    add = sub.add_parser("add-source"); add.add_argument("bundle"); add.add_argument("source")
    add.add_argument("--id", required=True); add.add_argument("--title"); add.add_argument("--shared-url", default="")
    check = sub.add_parser("check"); check.add_argument("bundle"); check.add_argument("--check-originals", action="store_true")
    calc = sub.add_parser("calculate"); calc.add_argument("bundle"); calc.add_argument("evidence_id")
    review = sub.add_parser("record-review"); review.add_argument("bundle"); review.add_argument("review_file")
    render = sub.add_parser("render"); render.add_argument("bundle"); render.add_argument("output")
    render.add_argument("--format", choices=("html", "md"), required=True); render.add_argument("--force", action="store_true")
    shell = sub.add_parser("shell"); shell.add_argument("output"); shell.add_argument("--format", choices=("html", "md"), required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            write(args.output, json.dumps(empty_bundle(args.title), ensure_ascii=False, indent=2) + "\n")
        elif args.command == "shell":
            text = webpage(empty_bundle()) if args.format == "html" else (
                "<!-- Report content goes here. Cite evidence using numbered footnotes. -->\n\n"
                "<!-- Footnote format: document identity; exact location; supporting quote or calculation; shared URL or original availability. -->\n")
            write(args.output, text)
        else:
            data = read_bundle(args.bundle)
            if args.command == "add-source":
                if any(source["id"] == args.id for source in data["sources"]):
                    raise ValueError("Source ID exists; refresh explicitly while preserving stable unit IDs")
                data["sources"].append(register(args.source, args.id, args.title, args.shared_url))
                write(args.bundle, json.dumps(data, ensure_ascii=False, indent=2) + "\n", True)
            elif args.command == "calculate":
                item = next(item for item in data["evidence"] if item["id"] == args.evidence_id)
                source = next(source for source in data["sources"] if source["id"] == item["source"])
                print(json.dumps(aggregate(source, item["calculation"]), ensure_ascii=False, indent=2))
            elif args.command == "check":
                result = validate(data, args.check_originals)
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return 1 if result["errors"] else 0
            elif args.command == "record-review":
                checks = validate(data, True)
                if checks["errors"]:
                    raise ValueError("Resolve structural/source errors before recording review: " + "; ".join(checks["errors"]))
                record = json.loads(Path(args.review_file).read_text())
                if record.get("revision") != revision(data):
                    raise ValueError("Review must name the current revision from check")
                required = {"quotations", "aggregates", "claim_support", "counterevidence", "coverage"}
                if set(record.get("checks", {})) != required or any(
                        not isinstance(value, str) or not value.strip() for value in record["checks"].values()):
                    raise ValueError("Review needs concrete notes for all five checks; explain not-applicable checks")
                findings = record.get("findings")
                if not isinstance(findings, list) or any(not isinstance(item, dict) or
                        item.get("status") not in ("resolved", "unresolved") or not item.get("reason") for item in findings):
                    raise ValueError("Review findings need resolved/unresolved status and reason")
                record["status"] = "unresolved" if any(item["status"] == "unresolved" for item in findings) else "reviewed"
                data["verification"] = record
                write(args.bundle, json.dumps(data, ensure_ascii=False, indent=2) + "\n", True)
            elif args.command == "render":
                checks = validate(data, True)
                if checks["errors"]:
                    raise ValueError("Cannot render invalid references: " + "; ".join(checks["errors"]))
                # Unreviewed rendering is allowed and visibly labelled; never auto-review.
                write(args.output, webpage(data) if args.format == "html" else markdown(data), args.force)
                for warning in checks["warnings"]:
                    print("WARNING:", warning)
        return 0
    except (ValueError, KeyError, TypeError, OSError, StopIteration, json.JSONDecodeError) as exc:
        parser.exit(2, f"Folio: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
