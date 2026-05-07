# Phase 3 실행 가이드

Phase 3는 `data/pending_items.jsonl`에 있는 639개 pending 항목에 대해 Haiku 4.5로
마크다운 문서를 배치 생성하는 단계이다.

## 사전 조건

- Phase 2 전체 완료 (T1~T6)
- `claude` CLI 사용 가능 (claude --version 으로 확인)
- macOS: OAuth OR ANTHROPIC_API_KEY 설정
- 5h Claude Code quota 여유 있음 (최소 15% 이상 권장)

## 실행 명령

### 기본 실행 (권장)
```bash
cd /path/to/prism
python3 scripts/prism_batch.py \
  --workers 5 \
  --batch-size 10 \
  --usage-limit 85
```

### 로그 파일로 남기기
```bash
python3 scripts/prism_batch.py --workers 5 --batch-size 10 --usage-limit 85 \
  2>&1 | tee -a logs/phase3-$(date +%Y%m%d-%H%M).log
```

### 테스트용 소규모 실행
```bash
python3 scripts/prism_batch.py --limit 20 --workers 2
```

### 특정 클래스만 (예: heuristic만 62개)
```bash
python3 scripts/prism_batch.py --class heuristic --workers 3
```

## 예상 소요 시간

| 항목 | 예상치 |
|---|---|
| 건당 Haiku 호출 시간 | 30~90초 |
| 5 워커 병렬 처리 | ~1분/건당 효율 |
| 순수 처리 시간 (quota 무시) | ~3시간 |
| 5h quota 대기 포함 | 6~12시간 (2~3회 리셋 발생 가능) |

## 예상 비용

Haiku 4.5 기준 (2026-04 시세):
- 입력: ~$1/M tokens
- 출력: ~$5/M tokens
- 건당 평균 입력: ~3000 토큰 (system + few-shot + user)
- 건당 평균 출력: ~1500 토큰
- 건당 비용: $0.003 + $0.0075 ≈ $0.01
- **639건 총합: ~$6.5**

## 중단 시 재개 방법

**정말 좋은 소식**: 파이프라인은 **완전히 resume-safe**하다.

중단 후 같은 명령을 재실행하면:
1. `parallel_runner`가 `.batch-state/prism-run/items/*.json`을 보고 이미 처리된 항목 스킵
2. `prism_batch`도 대상 md 파일이 이미 존재하면 LLM 호출 없이 스킵
3. lock 파일(`*.lock`)은 무시되고 신규 재획득

중간 단계 실패(네트워크, 타임아웃)도 동일 전략으로 처리: 같은 명령 재실행.

## 5h Quota 자동 대기

`parallel_runner`의 `check_usage_and_wait()`가 배치 10건마다 Anthropic Usage API를 호출해
5h 윈도우 사용률을 체크한다.

- `--usage-limit 85` 초과 시: 자동으로 `resets_at`까지 대기 (보통 1~5시간)
- 대기 중 로그: `[대기] 사용률 87% >= 85%. 리셋까지 47분 대기합니다...`
- 리셋 후 자동 재개

## 실행 후 해야 할 일

1. **생성 결과 확인**:
   ```bash
   find lenses frames models stances heuristics -name "*.md" -newer scripts/PHASE3_RUN.md | wc -l
   ```
   기대: 639 근처 (기존 파일 + 신규 639)

2. **실패 항목 확인**:
   ```bash
   python3 <<'PY'
   import json, glob
   fails = []
   for f in glob.glob(".batch-state/prism-run/items/*.json"):
       with open(f) as fh:
           r = json.load(fh)
       if r.get("_error"):
           fails.append((r.get("name"), r.get("reason") or r.get("error")))
   print(f"실패: {len(fails)}건")
   for name, reason in fails[:20]:
       print(f"  {name}: {reason}")
   PY
   ```

3. **catalog.yml 업데이트** (수동 또는 별도 스크립트 필요):
   생성된 md 파일들을 catalog.yml의 엔트리로 등록. 현재 이 작업을 위한
   스크립트는 없음 — 필요 시 별도 태스크로 작성.

4. **결과 커밋** (권장: 클래스별로 분리):
   ```bash
   git add library/lenses/
   git commit -m "v0.3: add generated lens files from phase 3 batch"

   git add library/frames/
   git commit -m "v0.3: add generated frame files from phase 3 batch"

   # ... 나머지 클래스
   ```

## 문제 해결

### `[429 백오프]` 로그 반복 발생
API Key 모드일 때만 발생. 구독제 OAuth 모드로 전환하거나 대기.

### 특정 아이템이 계속 실패
해당 아이템만 격리해서 재시도:
```bash
python3 scripts/prism_batch.py --class lens --limit 1 \
  --pending <(grep "problem-item-name" data/pending_items.jsonl)
```

또는 일시적으로 `data/pending_items.jsonl`에서 제거하고 원인 조사 후 복구.

### validation_failed 빈발
생성물이 프론트매터/섹션 조건을 만족하지 못하는 경우.
`.batch-state/prism-run/items/<name>.json`의 `body_preview` 필드 확인.
프롬프트 튜닝이 필요할 수 있음.
