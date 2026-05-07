# ──────────────────────────────────────────────────────────────────
# parallel_runner.py
#
# Adapted from an earlier internal batch runner.
#
# Used in Prism for batch document generation (Phase 3 — 600 items, haiku 4.5).
# Key features: lock-based parallel safety + 5h quota auto-wait + multi-threaded workers.
#
# Do not modify the core logic; adapt via the calling driver (prism_batch.py).
# ──────────────────────────────────────────────────────────────────
"""
병렬 실행 공통 모듈 — lock 기반 중복 방지, 사용량 자동 대기, multiprocessing 워커

사용법:
    from parallel_runner import ParallelRunner

    runner = ParallelRunner(
        output_dir="output/round-b/relations-all",
        batch_size=5,
        usage_limit=90,
        workers=3,
    )

    def process_one(item, worker_id):
        # LLM 호출 등 실제 처리
        return {"result": ...}  # JSON-serializable dict

    runner.run(
        items=[{"key": "unique_id", ...}, ...],
        process_fn=process_one,
        key_fn=lambda item: item["key"],
    )
"""

import json
import os
import subprocess
import sys
import tempfile
import time
from threading import Lock, Thread

# ── Windows cp949 인코딩 문제 방지 ──
# parallel_runner를 import하는 모든 스크립트에 자동 적용
if sys.platform == "win32":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


# ── 모드 감지 + claude -p 헬퍼 ──

def is_api_key_mode() -> bool:
    """ANTHROPIC_API_KEY가 설정되어 있으면 API Key(프록시) 모드."""
    return bool(os.environ.get("ANTHROPIC_API_KEY", ""))


def build_claude_cmd(model: str, system_prompt: str = None,
                     max_budget: float = 0.10) -> list[str]:
    """현재 모드에 따라 claude -p 명령어를 구성한다.

    - API Key 모드: --bare 추가 (컨텍스트 로딩 완전 차단)
    - 구독제 모드: --bare 없음 (OAuth 인증 필요)
    """
    cmd = ["claude", "-p"]
    if is_api_key_mode():
        cmd.append("--bare")
    cmd.extend(["--model", model])
    if system_prompt:
        cmd.extend(["--system-prompt", system_prompt])
    cmd.extend(["--output-format", "json", "--max-budget-usd", str(max_budget)])
    return cmd


def build_claude_env_and_cwd() -> tuple[dict, str | None]:
    """현재 모드에 따라 env와 cwd를 결정한다.

    - API Key 모드: cwd 변경 불필요 (--bare가 컨텍스트 차단)
    - 구독제 모드: cwd=tempdir (프로젝트 CLAUDE.md 로딩 방지)
    """
    env = os.environ.copy()
    # 자식 프로세스(claude CLI 등)도 UTF-8 출력하도록 강제
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    if is_api_key_mode():
        return env, None
    else:
        return env, tempfile.gettempdir()


# ── Usage API / 429 백오프 ──

_usage_lock = Lock()  # 멀티스레드 동시 접근 보호

def get_access_token() -> str:
    """macOS Keychain에서 Claude OAuth 토큰 읽기"""
    import platform
    if platform.system() == "Darwin":
        try:
            result = subprocess.run(
                ["/usr/bin/security", "find-generic-password", "-s", "Claude Code-credentials", "-w"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                raw = json.loads(result.stdout.strip())
                return raw.get("claudeAiOauth", {}).get("accessToken") or raw.get("accessToken", "")
        except Exception:
            pass
    creds_path = os.path.expanduser("~/.claude/.credentials.json")
    if os.path.exists(creds_path):
        with open(creds_path) as f:
            raw = json.load(f)
        return raw.get("claudeAiOauth", {}).get("accessToken") or raw.get("accessToken", "")
    return ""


_usage_cache = {"utilization": 0, "resets_at": "", "last_call": 0.0}
_sleep_until = 0.0  # epoch — 이 시각까지 모든 스레드가 sleep
_USAGE_MIN_INTERVAL = 60  # 초 — Usage API 호출 최소 간격 (rate limit 보호)


def fetch_five_hour_usage() -> tuple[int, str]:
    """5시간 윈도우 사용률(%)과 resets_at 반환.

    멀티스레드 안전: _usage_lock으로 동시 API 호출 방지.
    캐싱: _USAGE_MIN_INTERVAL 이내 재호출 시 캐시 반환.
    """
    with _usage_lock:
        now = time.time()
        if now - _usage_cache["last_call"] < _USAGE_MIN_INTERVAL:
            return _usage_cache["utilization"], _usage_cache["resets_at"]

        token = get_access_token()
        if not token:
            return _usage_cache["utilization"], _usage_cache["resets_at"]
        try:
            result = subprocess.run(
                ["curl", "-s", "--max-time", "5",
                 "-H", f"Authorization: Bearer {token}",
                 "-H", "anthropic-beta: oauth-2025-04-20",
                 "-H", "Content-Type: application/json",
                 "https://api.anthropic.com/api/oauth/usage"],
                capture_output=True, text=True, timeout=10,
            )
            _usage_cache["last_call"] = time.time()
            if result.returncode != 0 or not result.stdout.strip():
                return _usage_cache["utilization"], _usage_cache["resets_at"]
            data = json.loads(result.stdout)
            if "error" in data:
                # rate_limit_error — 다음 호출까지 간격 2배
                _usage_cache["last_call"] = time.time() + _USAGE_MIN_INTERVAL
                return _usage_cache["utilization"], _usage_cache["resets_at"]
            utilization = int(round(data.get("five_hour", {}).get("utilization", 0)))
            resets_at = data.get("five_hour", {}).get("resets_at", "")
            _usage_cache["utilization"] = utilization
            _usage_cache["resets_at"] = resets_at
            return utilization, resets_at
        except Exception:
            return _usage_cache["utilization"], _usage_cache["resets_at"]


_backoff_round = 0     # API Key 모드: 429 누적 라운드 (lock 보호)
_BACKOFF_BASE = 60     # 초기 대기 60초
_BACKOFF_MAX = 600     # 최대 10분


def check_usage_and_wait(usage_limit: int):
    """사용량 확인 후 임계값 초과 시 대기.

    모드별 동작:
    - 구독제 OAuth: 5h usage API로 사용률 확인 → resets_at까지 대기
    - API Key 프록시: usage API 없음 → 연속 실패 시 지수 백오프
    """
    global _sleep_until

    if is_api_key_mode():
        # API Key 모드: usage API 사용 불가, 정상 호출만 확인
        print(f"  [사용량] API Key 모드 (--bare)")
        return

    # ── 구독제 OAuth 모드 ──
    # 다른 스레드가 설정한 대기 시각이 아직 유효하면 그냥 sleep
    remaining = _sleep_until - time.time()
    if remaining > 0:
        wait_min = int(remaining) // 60
        print(f"  [대기] 다른 워커가 설정한 대기 중. {wait_min}분 남음...")
        time.sleep(remaining)
        return

    utilization, resets_at = fetch_five_hour_usage()
    print(f"  [사용량] 5h: {utilization}% (임계: {usage_limit}%)")

    if utilization < usage_limit:
        return

    if not resets_at:
        return

    from datetime import datetime, timezone
    try:
        reset_str = resets_at.replace("+00:00", "+0000").replace("Z", "+0000")
        if "." in reset_str:
            reset_str = reset_str[:reset_str.index(".")] + reset_str[reset_str.index("+"):]
        reset_dt = datetime.strptime(reset_str, "%Y-%m-%dT%H:%M:%S%z")
        now_dt = datetime.now(timezone.utc)
        wait_sec = int((reset_dt - now_dt).total_seconds()) + 60

        if wait_sec > 0:
            with _usage_lock:
                _sleep_until = time.time() + wait_sec
                _usage_cache["last_call"] = 0.0

            wait_min = wait_sec // 60
            print(f"  [대기] 사용률 {utilization}% >= {usage_limit}%. 리셋까지 {wait_min}분 대기합니다...")
            print(f"  [대기] 리셋 시각: {resets_at}")
            time.sleep(wait_sec)
            print(f"  [재개] 리셋 완료. 계속 진행합니다.")
    except Exception as e:
        print(f"  [사용량] 리셋 시간 파싱 실패: {e} — 계속 진행")


def backoff_wait_apikey():
    """API Key 모드 전용: 429 발생 시 지수 백오프 대기.

    _backoff_round를 누적하여 60→120→240→600초로 대기 시간 증가.
    _usage_lock으로 멀티스레드 안전 보장.
    """
    global _backoff_round
    with _usage_lock:
        _backoff_round += 1
        wait = min(_BACKOFF_BASE * (2 ** (_backoff_round - 1)), _BACKOFF_MAX)
    print(f"  [429 백오프] {wait}초 대기 (누적 {_backoff_round}회)...")
    time.sleep(wait)


def reset_backoff():
    """API Key 모드: 성공 시 백오프 리셋."""
    global _backoff_round
    with _usage_lock:
        _backoff_round = 0


# ── ParallelRunner ──

class ParallelRunner:
    """lock 기반 병렬 안전 배치 실행기"""

    def __init__(self, output_dir: str, batch_size: int = 5, usage_limit: int = 90,
                 workers: int = 1, max_consecutive_fails: int = 3, flat: bool = False):
        self.output_dir = output_dir
        self.items_dir = output_dir if flat else os.path.join(output_dir, "items")
        self.batch_size = batch_size
        self.usage_limit = usage_limit
        self.workers = workers
        self.max_consecutive_fails = max_consecutive_fails
        self.last_run_new = 0  # 직전 run()에서 새로 처리한 건수
        os.makedirs(self.items_dir, exist_ok=True)

    def _safe_key(self, key: str) -> str:
        """파일명 안전 키 — 대괄호 전체 제거, 슬래시→하이픈"""
        return key.replace("[", "").replace("]", "").replace("/", "-")

    def is_done(self, key: str) -> bool:
        return os.path.exists(os.path.join(self.items_dir, f"{self._safe_key(key)}.json"))

    def try_lock(self, key: str) -> bool:
        lock_path = os.path.join(self.items_dir, f"{self._safe_key(key)}.lock")
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return True
        except FileExistsError:
            return False

    def release_lock(self, key: str):
        lock_path = os.path.join(self.items_dir, f"{self._safe_key(key)}.lock")
        try:
            os.unlink(lock_path)
        except FileNotFoundError:
            pass

    def save_result(self, key: str, result: dict):
        result_path = os.path.join(self.items_dir, f"{self._safe_key(key)}.json")
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

    def load_all_results(self) -> list[dict]:
        results = []
        for f in sorted(os.listdir(self.items_dir)):
            if f.endswith(".json"):
                with open(os.path.join(self.items_dir, f), encoding="utf-8") as fh:
                    results.append(json.load(fh))
        return results

    def clean_stale_locks(self):
        for f in os.listdir(self.items_dir):
            if f.endswith(".lock"):
                os.unlink(os.path.join(self.items_dir, f))
                print(f"  cleaned stale lock: {f}")

    def _worker_loop(self, items: list, process_fn, key_fn, worker_id: int, total: int):
        """단일 워커 루프"""
        batch_succeeded = 0
        consecutive_fails = 0
        processed = 0
        prefix = f"[W{worker_id}]" if self.workers > 1 else ""

        for item in items:
            key = key_fn(item)

            if self.is_done(key):
                continue
            if not self.try_lock(key):
                continue

            print(f"  {prefix} {key}...", end=" ", flush=True)

            try:
                result = process_fn(item, worker_id)

                if result is None or result.get("_error"):
                    print(f"FAIL")
                    self.release_lock(key)
                    consecutive_fails += 1
                    if consecutive_fails >= self.max_consecutive_fails:
                        print(f"\n=== {prefix} 연속 {self.max_consecutive_fails}건 실패 — 리밋 도달 추정 ===")
                        if is_api_key_mode():
                            backoff_wait_apikey()
                        else:
                            check_usage_and_wait(self.usage_limit)
                        consecutive_fails = 0
                    continue

                self.save_result(key, result)
                self.release_lock(key)
                processed += 1
                consecutive_fails = 0
                reset_backoff()
                batch_succeeded += 1
                print(f"OK")

                if batch_succeeded >= self.batch_size:
                    print(f"\n--- {prefix} 배치 {self.batch_size}건 완료 (처리: {processed}) ---")
                    check_usage_and_wait(self.usage_limit)
                    batch_succeeded = 0

            except Exception as e:
                print(f"ERROR: {e}")
                self.release_lock(key)

            time.sleep(0.3)

        return processed

    def run(self, items: list, process_fn, key_fn):
        """메인 실행. items를 process_fn으로 처리, key_fn으로 고유 키 추출"""
        remaining = [item for item in items if not self.is_done(key_fn(item))]
        done = len(items) - len(remaining)
        print(f"  완료 {done}건, 잔여 {len(remaining)}건 (워커: {self.workers})")

        self.last_run_new = len(remaining)

        if not remaining:
            print("  모든 항목 완료!")
            return

        if self.workers <= 1:
            self._worker_loop(items, process_fn, key_fn, 0, len(items))
        else:
            threads = []
            for wid in range(self.workers):
                t = Thread(target=self._worker_loop, args=(items, process_fn, key_fn, wid, len(items)))
                t.start()
                threads.append(t)
                time.sleep(0.5)
            for t in threads:
                t.join()

        self.clean_stale_locks()
