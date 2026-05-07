#!/usr/bin/env python3
"""Prism batch document generator using haiku 4.5 via claude -p.

Generates one markdown file per entry in data/pending_items.jsonl using
class-specific prompts and golden few-shot examples. Wraps
parallel_runner.ParallelRunner with a markdown-output adapter, atomic
writes, frontmatter/section validation, and resume-safe skipping of
already-generated files.

Usage:
    python3 scripts/prism_batch.py --dry-run
    python3 scripts/prism_batch.py --limit 5 --workers 1
    python3 scripts/prism_batch.py --workers 5 --batch-size 10
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from parallel_runner import (  # noqa: E402
    ParallelRunner,
    build_claude_cmd,
    build_claude_env_and_cwd,
)

PROMPTS_DIR = SCRIPT_DIR / "prompts"
GOLDEN_DIR = SCRIPT_DIR / "golden_examples"

# 클래스 → 복수형 출력 디렉토리 (Prism 레이아웃: library/ 하위로 통합됨)
CLASS_TO_DIR = {
    "lens": "library/lenses",
    "frame": "library/frames",
    "model": "library/models",
    "stance": "library/stances",
    "heuristic": "library/heuristics",
}

# 클래스별 필수 섹션. CLASSES.md + prompts/*.system.txt 에서 합의된 헤더명과 일치.
# validate_markdown 은 "## <section>\n" 또는 "## <section>$" 존재 여부만 본다.
REQUIRED_SECTIONS = {
    "lens": ["Overview", "Analytical Procedure", "Output Format"],
    "frame": ["Overview", "Categories", "Classification Procedure"],
    "model": ["Overview", "Core Variables and Relationships", "Application Procedure"],
    "stance": ["Overview", "Foundational Commitments", "Guiding Questions"],
    "heuristic": ["The Rule", "When It Applies", "When It Misleads"],
}

# 공통 필수 프론트매터 필드 (system 프롬프트들이 모두 강제)
REQUIRED_FRONTMATTER_FIELDS = ["name:", "class:", "domain:"]

MIN_BODY_LEN = 800


def load_templates() -> dict:
    """클래스별 system/user 프롬프트를 한 번 로드한다."""
    templates = {}
    for cls in CLASS_TO_DIR:
        sys_path = PROMPTS_DIR / f"{cls}.system.txt"
        usr_path = PROMPTS_DIR / f"{cls}.user.txt"
        templates[cls] = {
            "system": sys_path.read_text(encoding="utf-8"),
            "user": usr_path.read_text(encoding="utf-8"),
        }
    return templates


def load_golden_examples(max_per_class: int = 2) -> dict:
    """클래스별 few-shot 예시 파일(.md) 내용을 로드한다.

    예시가 max_per_class개보다 적으면 빈 문자열로 채워 placeholder 치환이
    항상 안전하게 되도록 한다.
    """
    examples = {}
    for cls in CLASS_TO_DIR:
        cls_dir = GOLDEN_DIR / cls
        if not cls_dir.exists():
            examples[cls] = ["", ""]
            continue
        files = sorted(cls_dir.glob("*.md"))[:max_per_class]
        shots = [f.read_text(encoding="utf-8") for f in files]
        while len(shots) < max_per_class:
            shots.append("")
        examples[cls] = shots
    return examples


def build_user_prompt(item: dict, templates: dict, golden: dict) -> str:
    """user 템플릿의 placeholder 를 아이템 메타로 치환한다."""
    cls = item["class"]
    tmpl = templates[cls]["user"]
    shots = golden.get(cls, ["", ""])
    out = tmpl
    out = out.replace("{{display_name}}", item["display_name"])
    out = out.replace("{{name}}", item["name"])
    out = out.replace("{{domain}}", item["domain"])
    out = out.replace("{{one_liner}}", item.get("one_liner", ""))
    few_shot_1 = shots[0] if len(shots) >= 1 else ""
    few_shot_2 = shots[1] if len(shots) >= 2 else ""
    out = out.replace("{{few_shot_1}}", few_shot_1)
    out = out.replace("{{few_shot_2}}", few_shot_2)
    return out


def call_claude(user_prompt: str, system_prompt: str, model: str,
                timeout: int = 180) -> dict | None:
    """claude -p 호출. --output-format json 래퍼를 벗겨 본문만 돌려준다."""
    try:
        env, cwd = build_claude_env_and_cwd()
        cmd = build_claude_cmd(model, system_prompt=system_prompt, max_budget=0.10)
        result = subprocess.run(
            cmd,
            input=user_prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            env=env,
            cwd=cwd,
        )
        raw = result.stdout
        try:
            wrapped = json.loads(raw)
            body = wrapped.get("result", raw)
        except json.JSONDecodeError:
            body = raw
        return {"body": body.strip(), "returncode": result.returncode}
    except Exception as e:
        return {"_error": True, "error": str(e)}


def extract_markdown(raw_body: str) -> str:
    """모델 응답에서 순수 markdown 본문만 뽑아낸다.

    - 전체를 ```...``` 로 감싸 보낸 경우 벗겨낸다.
    - frontmatter 앞에 설명 텍스트가 붙으면 첫 `---` 줄 이전을 버린다.
    - 끝에 개행 하나를 보장한다.
    """
    text = raw_body.strip()

    # 전체 코드펜스 래핑 벗겨내기
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]  # 첫 ``` 라인 제거
        while lines and lines[-1].strip().startswith("```"):
            lines.pop()
        text = "\n".join(lines).strip()

    # frontmatter 가 바로 시작하지 않으면, 본문 중 첫 "---" 라인을 찾아
    # 그 앞을 버린다 (모델이 "Here is the file:" 등 서두를 붙인 경우).
    if not text.startswith("---"):
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if line.strip() == "---":
                text = "\n".join(lines[i:])
                break

    return text.rstrip() + "\n"


def validate_markdown(md: str, cls: str) -> tuple[bool, str]:
    """프론트매터 + 필수 섹션 + 최소 길이 검증."""
    if not md.startswith("---"):
        return False, "missing_frontmatter_open"

    # 두 번째 `---` 라인 찾기
    lines = md.split("\n")
    fm_close_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_close_idx = i
            break
    if fm_close_idx < 0:
        return False, "missing_frontmatter_close"

    fm = "\n".join(lines[1:fm_close_idx])
    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in fm:
            return False, f"missing_frontmatter_field:{field}"

    body = "\n".join(lines[fm_close_idx + 1:])
    for section in REQUIRED_SECTIONS[cls]:
        if f"## {section}" not in body:
            return False, f"missing_section:{section}"

    if len(md) < MIN_BODY_LEN:
        return False, "too_short"

    return True, "ok"


def atomic_write(target_path: Path, content: str) -> None:
    """같은 디렉토리에 임시파일 쓴 뒤 rename — 중간 실패 시 절반 쓰기 방지."""
    target_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False,
        dir=target_path.parent,
        prefix=".tmp-",
        suffix=".md",
    )
    try:
        tmp.write(content)
        tmp.close()
        os.replace(tmp.name, target_path)
    except Exception:
        try:
            os.unlink(tmp.name)
        except Exception:
            pass
        raise


def compute_target_path(item: dict) -> Path:
    cls_dir = CLASS_TO_DIR[item["class"]]
    return PROJECT_DIR / cls_dir / item["domain"] / f"{item['name']}.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prism batch markdown generator (haiku 4.5)"
    )
    parser.add_argument(
        "--pending",
        default=str(PROJECT_DIR / "data" / "pending_items.jsonl"),
        help="입력 JSONL 경로",
    )
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--usage-limit", type=int, default=85)
    parser.add_argument("--model", default="claude-haiku-4-5-20251001")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="테스트용 — 처리할 첫 N건만",
    )
    parser.add_argument(
        "--class",
        dest="cls",
        default=None,
        choices=list(CLASS_TO_DIR.keys()),
        help="특정 클래스만 처리",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="첫 아이템의 조립된 프롬프트만 출력하고 종료",
    )
    parser.add_argument(
        "--output-state",
        default=str(PROJECT_DIR / ".batch-state" / "prism-run"),
        help="ParallelRunner 상태/결과 JSON 저장 디렉토리",
    )
    args = parser.parse_args()

    # 입력 로드
    items: list[dict] = []
    with open(args.pending, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    if args.cls:
        items = [it for it in items if it["class"] == args.cls]
    if args.limit:
        items = items[: args.limit]

    templates = load_templates()
    golden = load_golden_examples()

    print("=== Prism batch (haiku) ===")
    print(f"  입력: {args.pending} ({len(items)}건 처리 대상)")
    print(f"  출력 상태: {args.output_state}")
    print(f"  모델: {args.model}")
    print(f"  워커: {args.workers}, 배치: {args.batch_size}, 사용량 임계: {args.usage_limit}%")
    if args.cls:
        print(f"  클래스 필터: {args.cls}")
    print()

    if args.dry_run:
        if not items:
            print("  (빈 입력 — dry-run할 아이템 없음)")
            return
        item = items[0]
        print(f"=== Dry run: {item['name']} ({item['class']}/{item['domain']}) ===")
        print()
        print("=== System Prompt ===")
        print(templates[item["class"]]["system"])
        print()
        print("=== User Prompt ===")
        print(build_user_prompt(item, templates, golden))
        print()
        print(f"=== Target Path ===")
        print(compute_target_path(item))
        return

    runner = ParallelRunner(
        output_dir=args.output_state,
        batch_size=args.batch_size,
        usage_limit=args.usage_limit,
        workers=args.workers,
    )

    def process_fn(item: dict, worker_id: int) -> dict:
        try:
            target = compute_target_path(item)
            if target.exists():
                return {
                    "name": item["name"],
                    "class": item["class"],
                    "domain": item["domain"],
                    "md_path": str(target.relative_to(PROJECT_DIR)),
                    "model": args.model,
                    "status": "already_exists",
                    "generated_at": now_iso(),
                }

            prompt = build_user_prompt(item, templates, golden)
            system = templates[item["class"]]["system"]
            result = call_claude(prompt, system, args.model, timeout=180)

            if result is None or result.get("_error"):
                return {
                    "_error": True,
                    "error": (result.get("error") if result else "no_result"),
                    "name": item["name"],
                    "class": item["class"],
                }

            md = extract_markdown(result["body"])
            ok, reason = validate_markdown(md, item["class"])
            if not ok:
                return {
                    "_error": True,
                    "reason": reason,
                    "name": item["name"],
                    "class": item["class"],
                    "body_preview": md[:500],
                }

            atomic_write(target, md)
            return {
                "name": item["name"],
                "class": item["class"],
                "domain": item["domain"],
                "md_path": str(target.relative_to(PROJECT_DIR)),
                "model": args.model,
                "status": "generated",
                "bytes": len(md),
                "generated_at": now_iso(),
            }
        except Exception as e:
            return {
                "_error": True,
                "error": str(e),
                "name": item.get("name", "?"),
            }

    key_fn = lambda item: item["name"]  # noqa: E731
    runner.run(items=items, process_fn=process_fn, key_fn=key_fn)

    results = runner.load_all_results()
    ok = [r for r in results if not r.get("_error")]
    fail = [r for r in results if r.get("_error")]
    new_count = sum(1 for r in ok if r.get("status") == "generated")
    existed_count = sum(1 for r in ok if r.get("status") == "already_exists")

    print(f"\n=== 완료 ===")
    print(f"성공: {len(ok)}건 (신규 {new_count}건 / 이미존재 {existed_count}건)")
    print(f"실패: {len(fail)}건")


if __name__ == "__main__":
    main()
