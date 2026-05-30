"""공통 유틸리티 — 체크포인트, JSONL 처리 등."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def checkpoint_load(path: Path) -> dict:
    """체크포인트 파일을 로드한다. 파일이 없으면 빈 dict를 반환."""
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def checkpoint_save(path: Path, data: dict) -> None:
    """체크포인트 데이터를 JSON으로 저장한다."""
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def safe_json_loads(line: str, filepath: Path | str = "") -> dict | None:
    """JSONL 한 줄을 안전하게 파싱. 실패 시 None 반환."""
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        if filepath:
            logger.warning("JSON 파싱 실패 (skip): %s", filepath)
        return None


def jsonl_read(path: Path) -> list[dict]:
    """JSONL 파일을 읽어 dict 리스트로 반환. 불완전한 라인은 skip."""
    if not path.exists():
        return []
    results = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                msg = safe_json_loads(line, path)
                if msg is not None:
                    results.append(msg)
    return results


def jsonl_append(path: Path, record: dict) -> None:
    """JSONL 파일에 레코드 1건 추가."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
