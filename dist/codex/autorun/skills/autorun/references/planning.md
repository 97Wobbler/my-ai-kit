# PLAN 모드 상세 — workplan.yaml 생성

작업 스펙에서 workplan.yaml까지 도달하는 절차. 메인 세션이 직접 수행하거나(작은 스펙), 큰 스펙은 Codex explorer subagent에 as-is 분석을 위임한 뒤 메인이 통합한다.

## Step 1. 스펙 수집

사용자가 제공하는 인풋 형태:
- 자연어 요구사항 ("이 모듈 리팩토링해줘")
- PRD/티켓/개선 제안 문서
- 버그 리포트 + 수정 방향
- "iris-workplan.yaml 스타일로 일감 분해해줘" 같은 메타 요청

**불명확성이 있으면 최대 3개 질문만.** 핵심은:
1. **범위(scope)** — 어디까지 손대는가? 건드리지 말아야 할 것은?
2. **완료 기준(success criteria)** — 어떤 상태가 되면 끝인가?
3. **제약(constraints)** — 지켜야 할 원칙/기한/의존성?

반문 없이 넘어갈 수 있는 경우: 스펙이 이미 충분히 구체적이거나, 사용자가 "알아서 판단해" 모드.

## Step 2. as-is 분석

현재 상태 파악. 분석 대상:
- 관련 파일 구조와 주요 모듈
- 기존 테스트/스크립트/문서
- 유사 기능 구현 흔적
- 관련 최근 커밋 (`git log --oneline -20 <path>`)

**빠른 확인 (파일 몇 개)**: 메인이 직접 Read/Grep/Glob.

**광범위 조사 (코드베이스 전반)**: autorun 요청은 bounded explorer subagent 위임에 대한 명시 승인으로 취급한다. 광범위한 as-is 조사가 계획 품질을 높이면 `spawn_agent(agent_type: "explorer")`로 위임한다. 프롬프트 예:
```
이 프로젝트에서 X 관련 코드의 as-is를 조사해주세요.
- 관련 파일 위치와 역할
- 현재 동작 방식 요약
- Y와의 연결 지점
- 레거시/더미 코드 여부
보고는 300단어 이내.
```

## Step 3. to-be 정의

스펙에서 도달해야 할 최종 상태를 **한 문단으로 명시**. 모호한 동사("개선", "정리") 피하고 검증 가능한 상태어로.

좋은 예:
- "X 모듈이 Y 인터페이스를 구현하고, Z 테스트가 통과하며, 기존 caller의 동작이 변하지 않는다."

나쁜 예:
- "X를 개선한다."
- "Y를 잘 동작하게 만든다."

큰 스펙이면 사용자에게 to-be 요약을 보고하고 확인받는다. 작은 스펙이면 workplan에 주석으로 박고 진행.

## Step 4. gap 분해

as-is → to-be 사이의 차이를 태스크로 쪼갠다.

**태스크 입도 기준:**
- **커밋 단위**: 한 태스크는 worker가 구현하고 메인이 독립 검증한 뒤 하나의 의미 있는 커밋으로 남길 수 있는 최소 단위다.
- **시간 예산**: 사람 기준 시간이 아니라 agent 기준으로 본다. 일반 구현 태스크는 1~5분 worker 작업을 목표로 하고, 5~10분을 넘길 것 같으면 먼저 split한다.
- **한 가지 목적**: 하나의 태스크는 하나의 주된 behavior/docs/test/dependency 변화만 담는다. "A도 하고 B도 하고 C도"는 split 대상이다.
- **좁은 write scope**: 파일 1~3개 정도가 기본 예산이다. 디렉터리/glob output, 여러 implementation surface, 공통 기반 작업과 대규모 rollout 결합, 핵심 런타임 파일+계약/문서+여러 test 파일 조합은 대부분 split 대상이다.
- **원자성**: 하나의 태스크는 자기완결적 산출물을 내야 한다. 중간 상태로 남으면 다음 태스크가 시작 못 함.
- **검증 가능성**: 메인이 짧은 L2/L3 체크로 결과를 판정할 수 있어야 한다. 검증 기준이 여러 독립 정책을 동시에 확인해야 하면 split한다.

사용자가 제공한 work item, 번호 목록, bullet, ticket, 요청 과업은 final executable task가 아니라 후보 scope다. 각 후보 scope는 반드시 commit-sized task 기준으로 재평가하고, 크거나 여러 목적을 담고 있으면 더 작은 task로 분해한다.

**반드시 split하는 신호:**
- `estimated_size: L`
- `estimated_size: M`이면서 broad spec, output 3개 초과, 또는 required behavior가 5개 초과
- required behavior bullet이 5개 초과
- implementation surface가 3개 이상 (예: 여러 API route group, UI surface, worker/job, data model, storage layer, external integration, generated contract)
- 공통 helper/foundation 생성과 여러 surface rollout이 같은 task에 있음
- behavior 변경과 contract/schema/docs 갱신이 여러 surface에 걸쳐 있음
- output이 디렉터리나 glob으로만 표현되어 실제 write set을 숨김

`autorun_plan_refine`이 `ready_to_run: false`를 반환하면 RUN에 들어가지 않는다. `next_action`이 `split_tasks`, `add_metadata`, `assess_surfaces`, `resolve_human_gate` 중 하나면 해당 blocker를 먼저 해결한다. `output` 항목을 디렉터리로 뭉치거나 파일을 빼서 warning을 없애는 것은 허용되지 않는다. 실제로 `autorun_task_split` 또는 `autorun_refine_apply`를 호출하거나 workplan을 직접 수정한 뒤 다시 validate/refine한다.

### planning coverage 모델

큰 스펙 또는 high-risk 변경은 태스크 그래프만으로 부족하다. 가능한 경우 아래 optional section을 채운다:

- `invariants`: 지켜야 할 핵심 불변식. 예: authorization, tenant isolation, data integrity, compatibility.
- `surfaces`: invariant가 적용되는 route/file/component/job/contract/data 영역.
- `criteria_map`: requirement가 어떤 invariant, surface, task, verification에 연결되는지.
- `not_assessed`: 아직 평가하지 못한 critical surface. `risk: high`이거나 `blocks_ready: true`면 MCP가 RUN readiness를 막을 수 있다.

각 task에는 필요한 경우 `invariant_refs`, `surface_refs`, `criteria_refs`를 넣고, 이 ref가 있으면 `verify_checks`로 확인 방법을 명시한다.

**태스크 유형 분류 (선택):**
- 구현(feat): 새 코드 작성
- 수정(fix): 기존 코드 변경
- 리팩토링(refactor): 동작 유지, 구조 변경
- 테스트(test)
- 문서(docs)
- 측정/분석(data): 스크립트 실행해서 결과 수집

### human_gate 승인 경계 점검

`human_gate: approve`가 필요한 요구사항은 PLAN 단계에서 승인 경계를 먼저 나눈다.
승인 gate는 승인 이후의 행동(구현, 배포, 대규모 치환, 비가역 변경)을 막는
체크포인트이지, 승인 판단에 필요한 산출물 생성을 막는 조건이 아니다.

반드시 아래 질문을 통과한 뒤 task를 만든다:
- 이 gate가 막는 행동은 무엇인가?
- 인간이 승인하려면 먼저 검토할 문서/리포트/선택지/diff 초안이 필요한가?
- 그 승인 판단 산출물이 `human_gate: null`인 별도 자동 실행 task로 분리되어 있는가?
- `human_gate: approve` task가 산출물 생성까지 막는 전체 중단 조건처럼 쓰이지 않았는가?

권장 패턴:
1. `T01` 제안서/분석 리포트/선택지 문서 생성 (`human_gate: null`)
2. `T02` 선행 산출물을 기준으로 인간 승인 대기 (`human_gate: approve`, `blocked_by: [T01]`)
3. `T03` 승인 이후 구현/적용 (`blocked_by: [T02]`)

승인 전 구현 금지는 "승인 전 아무것도 하지 않음"이 아니다. 승인에 필요한
판단 자료는 먼저 자동 생성되어야 한다.

## Step 5. 의존성 분석

각 태스크의 `blocked_by` 필드를 채운다.

**의존성 종류:**
1. **출력 → 입력**: A가 생성한 파일을 B가 읽음. B.blocked_by = [A]
2. **스키마 합의**: A가 인터페이스를 정의해야 B, C가 구현 가능. B.blocked_by = [A]
3. **파일 충돌**: A, B가 같은 파일을 수정. 병렬 불가. 순서 정하고 B.blocked_by = [A]
4. **논리 순서**: 테스트 작성은 구현 뒤. test_X.blocked_by = [X]
5. **human_gate 뒤**: 인간 승인 뒤에만 진행 가능한 것들은 승인 체크포인트 태스크를 blocker로. 승인 판단 산출물은 그 앞의 `human_gate: null` task에서 만든다.

**독립적인 것은 blocked_by를 비워라.** 과도한 의존성은 병렬화를 죽인다. "왠지 순서가 있어 보인다"는 이유로 체인을 만들지 말 것.

**cycle 금지.** workplan 작성 후 topological sort가 가능한지 머릿속으로 체크. cycle이 있으면 디자인 문제.

## Step 6. workplan.yaml 작성

**파일 위치는 고정**: 프로젝트 루트의 `workplan.yaml`. 단일 파일. 서브 디렉토리(`.workplan/`, `.autorun/` 등)에 두지 않는다. 한 저장소에 동시에 여러 workplan을 두지 않는다. MCP를 사용할 때도 이 파일이 durable source of truth다.

**전제 조건**: PLAN 모드 진입 시점에 이미 `git rev-parse --is-inside-work-tree`로 git 저장소임을 확인했어야 한다. 안 했다면 지금 확인. 실패면 중단.

`assets/workplan-template.yaml`을 복사해서 시작. 스키마 상세는 `references/workplan-schema.md`.

각 태스크에 최소한:
- `id`: 짧은 식별자 (T01, T02... 또는 주제 약자)
- `name`: 한 줄 이름
- `blocked_by`: 의존 태스크 id 배열
- `done: false`
- `status: pending`
- `human_gate`: null / approve / execute
- `spec`: subagent에 그대로 전달할 상세 명세 (멀티라인)
- `output`: 기대 산출물 경로(들)
- `verify_checks`: 내용 검증 기준 (선택, 텍스트 산출물에만)
- `estimated_size`: S/M/L. 새 workplan에서는 반드시 채운다. S는 바로 실행 가능한 commit-sized task, M은 split하지 않는 이유가 spec에 명확해야 하는 경계값, L은 RUN 전 split 대상이다.
- `invariant_refs` / `surface_refs` / `criteria_refs`: optional planning coverage 참조
- `lifecycle`: started/verified/committed 시각, worker id, commit 메타데이터 기본값

이 단계에서는 파일을 디스크에 쓰되 **커밋하지 않는다.** 사용자 승인 후에 커밋한다 (Step 8).

## Step 7. 사용자 확인

workplan 저장 후 사용자에게 요약 보고:
- 총 태스크 수
- phase 구조 (의존성 레벨별 그룹)
- human_gate 지점 (있다면)
- 예상 병렬성 / 직렬 체인
- MCP로 생성/검증했는지, MCP 실패로 직접 YAML을 편집했는지

`blocked_by: []`인 human_gate 태스크가 있으면 요약의 맨 앞에 배치한다.
이는 RUN 진입 직후 자동 태스크와 동시에 실행 가능해지는 인간 확인 작업이다.
사용자에게 먼저 처리하거나 명시적으로 미루는 것을 권장하고, 미루지 않았다면
RUN 시작 후 자동 worker를 spawn하기 전에 이 gate를 다시 확인한다.

"이대로 RUN 모드 시작할까요?" 확인받고 진행. 사용자가 수정 요청하면 반영 (이때도 아직 커밋 안 함).

## Step 8. RUN 승인 시: workplan 시작 커밋

사용자가 RUN 모드 진입을 승인하면, 그 시점에 workplan.yaml을 단독 커밋한다.

```bash
git add workplan.yaml
git commit -m "chore(autorun): start workplan — <한 줄 요약>"
```

**규칙:**
- `workplan.yaml`만 단독 스테이징. 다른 변경(unstaged/staged)은 그대로 둔다 — `git add -A` / `git add .` 절대 금지.
- 커밋 메시지 prefix는 `chore(autorun):` 고정. 나중에 git log에서 라이프사이클 추적이 가능해야 한다.
- dirty working tree는 그대로 둬도 된다. autorun이 stash 하지 않는다.

이 시작 커밋이 RUN 모드의 진입점이자, 다음 세션 재개 시 "어디서부터 시작했는지"의 기준점이 된다.

## 작은 스펙 단순화

태스크 수가 적다고 작은 작업이라고 판단하지 않는다. 작은 작업인지 여부는 각 태스크가 commit-sized인지, write scope가 좁은지, 1~5분 agent 작업으로 독립 검증 가능한지로 판단한다. 정말 작은 스펙이면 as-is 분석과 to-be 정의를 한 문단으로 축약해도 되지만, **태스크 입도 검토와 의존성 명시**는 생략하지 않는다.
