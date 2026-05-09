# RUN 모드 상세 — 실행 루프

workplan.yaml 기반 실행 루프의 단계별 상세. 각 단계에서 메인 세션이 수행하는 것과 subagent에 위임하는 것을 구분한다.

## 사전 로딩

RUN 모드 진입 시점마다 (첫 실행 + 세션 재개 모두):

**0. (세션 재개 한정) workplan.yaml 발견 시 사용자 확인.** PLAN 직후 같은 세션에서 RUN으로 넘어온 게 아니라 새 세션에서 workplan.yaml을 발견했다면, 자동 진입 금지. "이전 workplan을 발견했습니다 — 재개 / 폐기 / 무시 중 어떻게 할까요?" 명시 확인 후 "재개" 응답이 있어야 아래 절차로 들어간다.

1. 프로젝트 `AGENTS.md` 읽기 (있으면). `CLAUDE.md`도 있으면 보조 컨텍스트로 읽어 프로젝트 고유 용어/원칙 파악.
2. workplan.yaml 전체 읽기. 각 태스크의 `done`, `blocked_by`, `human_gate` 상태 스캔.
3. `git log --oneline -20` 확인. `chore(autorun): start workplan` 커밋이 라이프사이클 시작점, 그 이후 `<type>: <T번호>` 커밋들이 진행분. 마지막 완료된 태스크와 커밋 시점 확인.
4. workplan에 wip 주석이 있으면 재개 지점 파악.
5. **Codex `update_plan` 호출 (필수, 생략 금지)**: 미완료 태스크 전부를 Codex plan에 등록. 각 항목 텍스트는 `<T번호> <태스크명>` 형식, 초기 status는 `pending`. 세션 재개 시 이미 plan이 있으면 workplan과 대조해서 정합성만 맞춘다. 이 단계를 건너뛰면 루프 도는 동안 메인 세션이 진행 상태를 잃는다.

## Step 1: DRAIN — background 잔여 수확

이전 루프에서 background로 띄운 subagent가 있는지 확인. 완료 알림이 왔으면 결과를 가져와 VERIFY 수행. 미완료면 상태만 기록하고 새 태스크로 진행.

**첫 루프이거나 background 잔여가 없으면 이 단계 스킵.**

## Step 2: HUMAN-GATE PREFLIGHT — 준비된 인간 게이트 우선 확인

조건:
- `done: false`
- `blocked_by` 내 모든 태스크가 `done: true` (빈 배열이면 자동 충족)
- `human_gate: approve` 또는 `human_gate: execute`

매칭되는 태스크가 있으면 새 자동 worker를 spawn하기 전에 사용자에게 먼저 보고한다.
각 gate마다 다음을 포함한다:
- 태스크 id/name
- `approve`인지 `execute`인지
- 승인/수행 판단에 필요한 산출물 또는 사람이 해야 할 행동
- 이 gate를 기다리는 후속 태스크

동시에 `human_gate: null`인 자동 태스크도 실행 가능하다면, 자동 태스크를 먼저
돌리지 말고 인간 gate를 지금 처리하거나 명시적으로 미룰지 물어본다. 사용자가
"미루고 자동 진행"처럼 명시적으로 답하면 그 RUN 세션에서는 같은 ready gate를
반복 질문하지 않고, 새로 ready가 된 human gate만 다시 보고한다.

모든 ready task가 human_gate뿐이면 정상적인 gate 대기 상태로 멈추고
`workplan.yaml`을 남긴다.

## Step 3: SCAN — 자동 실행 가능 태스크 탐색

조건:
- `done: false`
- `blocked_by` 내 모든 태스크가 `done: true` (빈 배열이면 자동 충족)
- `human_gate: null`

매칭되는 태스크들의 리스트를 메모. 수가 많으면 다음 루프에 남겨도 OK.

## Step 4: PLAN — 배치 구성 + fg/bg 결정

SCAN 결과를 다음 기준으로 배치로 묶는다:

**병렬화 가능한 묶음:**
- 서로 의존성이 없고
- 출력 파일이 겹치지 않고
- 수정할 파일이 충돌하지 않는 것

**직렬 체인:**
- 한 태스크의 출력이 다음 태스크의 입력
- 같은 파일을 순차 수정
- 순서가 중요한 마이그레이션

**실행 모드 결정:**

| 모드 | Codex 처리 | 조건 | VERIFY 시점 |
|---|---|---|---|
| foreground | `spawn_agent` 후 필요할 때 `wait_agent` | 후속이 결과에 즉시 의존, 또는 검수 후 체인 이어가기 | EXEC 직후 즉시 |
| background | `spawn_agent` 후 메인은 비충돌 작업 계속 진행 | 독립 태스크, 후속 없음, 시간 오래 걸림 | 다음 루프의 DRAIN에서 |

**판단 기준:**
- 직렬 체인의 일부 → **foreground** (체인 진행 위해 즉시 검수)
- 병렬 독립 태스크 → **foreground-parallel** (단일 메시지에 여러 Agent 콜)
- 독립적이고 긴 태스크 → **background** 가능
- 확신 없으면 → **foreground** (안전 기본값)

**주의:** background로 띄워놓고 메인이 다른 태스크를 병행 진행할 때는 **두 태스크가 같은 파일이나 환경을 건드리지 않는지** 반드시 확인. race condition 위험.

## Step 5: EXEC — subagent 위임

**먼저 `update_plan`**: 이 태스크(들)를 `in_progress`로 변경. 병렬로 여러 개 동시 위임할 땐 전부 in_progress로. `spawn_agent` 호출 **직전**에 반드시 업데이트.

autorun RUN 모드 진입은 사용자가 workplan 실행과 subagent 위임을 명시적으로
허용한 것으로 간주한다. `spawn_agent`로 모든 자동 구현 태스크를 위임한다.
적절한 subagent를 띄울 수 없으면 메인이 직접 구현하지 말고 즉시 정지해서
사용자에게 보고한다.

프롬프트는 `assets/subagent-prompt-template.md` 기반.

**필수 포함:**
1. 프로젝트 `AGENTS.md`를 먼저 읽고, `CLAUDE.md`가 있으면 보조로 읽으라는 지시
2. 태스크 id + name + spec 원문
3. 기대 산출물 (output 경로)
4. 제약 (코딩 스타일, 기존 코드 패턴 따르기)
5. **"git commit 금지"** — 메인이 검수 후 커밋
6. self-check 체크리스트
7. 결과 보고 형식 (self-check: PASS/WARN)

**agent_type 선택:**
- 일반 구현 → `worker`
- 코드베이스 탐색/독립 검증 → `explorer`
- 계획 수립 → 메인 세션에서 수행. 별도 subagent는 독립 분석이 필요할 때만 사용.

## Step 6: VERIFY — 독립 검증

메인이 수행하는 3계층 검증. subagent self-check는 **신뢰하되 의존하지 않는다**.

### L1: subagent self-check (subagent 내부)

위임 프롬프트에 포함된 자기 점검. 결과 보고에 "self-check: PASS/WARN" 포함.

### L2: 구조 검증 (메인 세션, 범용)

모든 태스크에 적용:
```
□ 산출물 파일이 spec의 output 경로에 존재하는가
□ JSON/JSONL이면 파싱 가능한가 (python -m json.tool)
□ YAML이면 파싱 가능한가
□ 스키마 필수 필드가 모두 있는가
□ 빈 값/null이 비정상적으로 많지 않은가 (>20%이면 경고)
□ 파일 인코딩 UTF-8
```

### L3: 내용 검증 (메인 세션, 텍스트 산출물)

workplan의 `verify_checks`가 있으면 그 기준으로. 없으면 범용:
```
□ 텍스트 필드 3~5개 랜덤 샘플링 → 육안 확인
□ 비문/깨짐 패턴 grep
□ 의미 일관성 확인
```

### L3+: 별도 subagent 위임 검증 (큰 태스크)

태스크가 크거나 구현 품질이 의심스러우면 **별도 Agent 호출**로 독립 검증. 구현 subagent와 다른 컨텍스트에서 평가.

```
spawn_agent({
  agent_type: "explorer",
  message: "T05가 변경한 파일 X, Y, Z를 읽고 다음을 확인해주세요:
    - spec의 요구사항 A, B, C가 충족되었는가
    - 기존 테스트가 깨지지 않는가 (관련 테스트 찾아서 확인)
    - 코드 스타일 일관성
    보고는 PASS/FAIL + 이유. 200단어 이내."
})
```

**verify 실패 시:**
1. 1차 실패 → 원인 분석 후 재시도 1회 (subagent 새로 위임)
2. 2차 실패 → 즉시 정지. 사용자에게 보고.

## Step 7: COMMIT

검증 통과한 태스크만 커밋.

1. **workplan.yaml 수정**: 해당 태스크의 `done: false` → `done: true`. 필요하면 주석에 완료 노트.
2. **관련 추적 문서 업데이트** (있다면): todo.md 체크, status.md 등.
3. **git commit**: 태스크 1개 = 커밋 1개. 메시지 형식:
   ```
   <type>: <태스크 id> <태스크 name> — <한줄 요약>
   ```
   type: feat/fix/refactor/docs/test/data/chore
4. workplan과 산출물을 같은 커밋에. **스테이징은 명시적으로** — `git add workplan.yaml <산출물 경로들>` 식으로 파일을 나열한다. `git add -A` / `git add .` 금지 (사용자의 무관한 dirty 변경을 끌고 들어가지 않게).
5. **`update_plan` → completed** (즉시, 커밋 직후). 다음 태스크로 넘어가기 전에 반드시. 여러 태스크를 몰아서 한꺼번에 완료 처리하지 말 것 — 하나 끝날 때마다 즉시 갱신해야 세션 복구/추적이 정확하다.

## Step 8: LOOP

SCAN으로 복귀. 반복.

## Step 9: TEARDOWN — 모든 태스크 done 시 삭제 커밋

SCAN 결과 미완료 태스크가 0이 되면(전부 done이 되면) workplan.yaml을 삭제하고 커밋한다.

```bash
git rm workplan.yaml
git commit -m "chore(autorun): complete workplan — <한 줄 요약>"
```

이 커밋이 라이프사이클의 종료점. 이후 git log에서 `chore(autorun): start workplan` ↔ `chore(autorun): complete workplan` 페어로 한 사이클이 식별된다.

**유의:**
- 이 단계는 **모든 태스크가 done인 경우에만** 실행. human_gate 대기, VERIFY 실패, 사용자 중단 등으로 멈출 때는 workplan.yaml을 남긴다 (다음 세션에서 재개 가능하게).
- 이 커밋도 단독으로. `git rm workplan.yaml` 외 다른 변경 같이 스테이징 금지.
- 삭제 커밋까지 성공한 뒤에 최종 사용자 보고를 한다. 삭제 커밋이 실패하면
  `workplan.yaml`을 남겨 재개 가능하게 두고, 실패 원인을 보고한다.

## 배치 전략

한 루프에서 너무 많이 실행하지 말 것:
- **foreground-parallel**: 3~4개까지가 실용적. 많으면 컨텍스트 관리 힘듦.
- **background**: 2~3개까지. 더 많으면 DRAIN 복잡도 상승.
- **foreground + background 혼합**: 같은 루프에 섞어도 OK. 단 충돌 검증 필수.

**규모 큰 워크플랜(20+ 태스크)**: phase별로 나눠서 "phase 1 완료 → 보고 → phase 2 진입" 식으로 진행. 한번에 전부 돌리지 말 것.

## 정지 조건 상세

| 상황 | workplan.yaml 처리 | 행동 |
|---|---|---|
| **모든 태스크 done (완전 종료)** | **삭제 커밋** (Step 8) | 정상 종료. 상태 요약 보고 |
| `human_gate: approve` 태스크만 남음 | 유지 | 선행 산출물을 기준으로 승인 대기 보고 |
| `human_gate: execute` 태스크만 남음 | 유지 | 준비물 + 요청 사항 정리하여 보고 |
| auto 실행 가능 태스크 0 (gate 대기 등 미완료 잔존) | 유지 | 정상 종료. 상태 요약 |
| VERIFY 1회 실패 | 유지 | 원인 분석 + 재시도 1회 |
| VERIFY 2회 연속 실패 | 유지 | 즉시 정지, 사용자 보고 |
| spec 불명확 | 유지 | 해석 가능하면 최선 해석 + 검수 강화. 불가능하면 정지 |
| API 한도/리소스 고갈 | 유지 (wip 주석 추가) | `wip:` 태그로 부분 커밋 + workplan 주석 기록 → 정지 |
| 구조적 문제 발견 (워크플랜 재설계 필요) | 유지 | 즉시 정지, 재설계 제안 |

**삭제 커밋은 모든 태스크가 done인 경우에만.** 그 외 정지는 workplan.yaml을 남겨서 다음 세션 재개를 가능하게 한다.

## 세션 재개

새 세션에서 RUN 모드를 재개할 때:
0. **사용자 명시 확인**: workplan.yaml이 그냥 거기 있다는 사실만으로 자동 RUN 진입 금지. "이전 workplan을 발견했습니다 — 재개 / 폐기 / 무시?" 응답 받기. "폐기" → `git rm workplan.yaml && git commit -m "chore(autorun): discard workplan"`. "무시" → 일반 모드로 복귀. "재개" → 아래 진행.
1. workplan.yaml SCAN → done 필드로 중단 지점 파악
2. `git log --oneline -20`으로 `chore(autorun): start workplan` 이후 커밋 확인
3. 마지막 진행 태스크에 wip 주석이 있으면 그 지점부터 재개
4. background 태스크가 미완료로 남았던 흔적이 있으면 확인 (가능하면 재실행)
5. `update_plan`으로 미완료 태스크 재등록 (사전 로딩 5번)
