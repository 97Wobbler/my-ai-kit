# workplan.yaml 스키마

## 목차
- [전체 구조](#전체-구조)
- [meta 섹션](#meta-섹션)
- [tasks 배열](#tasks-배열)
- [필드 상세](#필드-상세)
- [전체 예시](#전체-예시)

## 전체 구조

```yaml
meta:
  created: <날짜>
  spec_source: <원본 스펙 경로 또는 요약>
  as_is: <현재 상태 한 문단>
  to_be: <목표 상태 한 문단>
  human_gate_values:
    null: AI 단독 진행
    approve: 선행 AI 산출물을 기준으로 인간 승인 대기
    execute: 인간 직접 수행 (AI는 준비물만)

tasks:
  - id: T01
    name: ...
    blocked_by: []
    human_gate: null
    done: false
    status: pending
    spec: |
      ...
    output: [path1, path2]
    verify_checks:
      - ...
    lifecycle:
      started_at: null
      verified_at: null
      committed_at: null
      worker_id: null
      commit: null
```

## meta 섹션

workplan 전체 맥락. 길게 쓰지 말고 한 문단씩.

**필수:**
- `created`: 생성 날짜 (YYYY-MM-DD)
- `to_be`: 도달할 최종 상태 (한 문단)

**권장:**
- `spec_source`: 원본 스펙이 어디서 왔는지 (티켓 번호, 문서 경로, 대화 요약)
- `as_is`: PLAN 단계에서 파악한 현재 상태 (한 문단)
- `human_gate_values`: 값 설명 (혼란 방지)
- `principles`: 이 프로젝트 고유 제약/원칙 배열 (있으면)

## tasks 배열

각 태스크는 다음 필드를 가진다:

### 필수 필드

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | string | 유니크 식별자. `T01`~`T99` 또는 주제 약자(`auth-fix`). 짧고 일관되게. |
| `name` | string | 한 줄 이름. 사람이 읽기 쉬운 제목. |
| `blocked_by` | list[string] | 의존 태스크 id 배열. 없으면 `[]`. |
| `human_gate` | null \| string | `null`/`approve`/`execute` 중 하나. |
| `done` | bool | 초기는 전부 `false`. 완료 시 메인이 `true`로 수정. |
| `status` | string | `pending`/`started`/`verified`/`committed`/`retired`. 새 workplan은 `pending`으로 시작. |
| `spec` | string (multiline) | subagent에 그대로 전달할 상세 명세. |

### 선택 필드

| 필드 | 타입 | 설명 |
|---|---|---|
| `output` | string \| list[string] | 기대 산출물 경로. 검증과 충돌 감지에 쓰임. |
| `verify_checks` | list[string] | L3 내용 검증 기준. 텍스트 산출물에만. |
| `category` | string | feat/fix/refactor/docs/test/data 등. 참고용. |
| `track` | string | 대규모 워크플랜에서 작업축 그룹핑 (A.1, B.2 등). |
| `notes` | string | 디자인 결정, 주의사항, 배경 설명. |
| `estimated_size` | string | S/M/L — 태스크 크기 감각. |
| `lifecycle` | object | MCP/메인 세션이 쓰는 시작/검증/커밋 시각, worker id, 커밋 메타데이터. |

## 필드 상세

### `blocked_by`

의존 태스크 id 배열. 같은 workplan 내 다른 태스크를 참조한다.

```yaml
blocked_by: []                # 독립 태스크
blocked_by: [T01]             # T01 완료 후 실행 가능
blocked_by: [T01, T02, T03]   # 세 개 전부 완료되어야 시작
```

**주의:**
- cycle 금지 (A→B→A). 작성 후 topological sort 가능한지 확인.
- 과도한 의존성 금지. 진짜 의존성만 넣을 것 (출력→입력, 파일 충돌, 논리 순서).

### `human_gate`

- `null` (기본): autorun 루프가 자동 실행
- `approve`: 선행 AI 산출물을 기준으로 인간 승인 대기 (예: 디자인 확정, 대규모 리팩토링 방향)
- `execute`: 인간이 직접 실행해야 함 (예: 외부 API 키 발급, 프로덕션 배포, 수동 데이터 수집). AI는 준비물만.

**승인 경계 규칙:** 승인 판단에 필요한 proposal, 리포트, 선택지 정리,
diff 초안 같은 산출물은 `human_gate: null`인 선행 task에서 생성한다.
`human_gate: approve` task는 그 산출물을 검수하기 위한 체크포인트로 두고,
승인 이후 구현/적용 task는 이 체크포인트를 `blocked_by`로 참조한다.
승인 전 구현 금지를 승인 전 산출물 생성 금지로 해석하지 말 것.

### `status` / `done`

`done`은 사람이 빠르게 읽는 완료 플래그이고, `status`는 MCP lifecycle guard가
사용하는 세부 상태다.

- `status`가 없고 `done: false`면 `pending`으로 해석한다.
- `status`가 없고 `done: true`면 완료로 해석한다.
- `status: committed` 또는 `status: retired`는 `done: true`여야 한다.
- `status: pending`, `started`, `verified`는 `done: false`여야 한다.

새 workplan은 각 task에 아래 기본값을 둔다.

```yaml
done: false
status: pending
lifecycle:
  started_at: null
  verified_at: null
  committed_at: null
  worker_id: null
  commit: null
```

### `spec`

subagent에 **그대로 전달**될 명세. 멀티라인 문자열(`|`) 사용.

**좋은 spec:**
```yaml
spec: |
  `src/auth/session.ts`에 `refreshToken(token: string): Promise<string>` 함수를 추가한다.
  - 기존 토큰이 만료되었으면 refresh API 호출 (`POST /auth/refresh`)
  - 유효하면 그대로 반환
  - API 호출 실패 시 AuthError throw
  - 반환 타입은 새 access token (string)
  - 테스트 파일 `src/auth/session.test.ts`에 3가지 케이스 추가:
    1. 만료된 토큰 → 새 토큰 반환
    2. 유효한 토큰 → 그대로 반환
    3. refresh 실패 → AuthError
```

**나쁜 spec:**
```yaml
spec: "refreshToken 함수 추가해서 토큰 갱신 구현"
```

구체적일수록 subagent가 정확히 구현한다.

### `output`

기대 산출물 경로. 파일이거나 디렉토리거나 모두 가능.

```yaml
output: src/auth/session.ts
# 또는
output:
  - src/auth/session.ts
  - src/auth/session.test.ts
```

**용도:**
1. VERIFY L2에서 파일 존재 확인
2. PLAN 단계에서 병렬 실행 시 파일 충돌 감지

### `verify_checks`

L3 내용 검증에서 메인 세션이 확인할 태스크 고유 기준. 없으면 범용 체크만 적용.

```yaml
verify_checks:
  - "refreshToken 함수가 export되었는지"
  - "AuthError가 기존 에러 클래스를 상속하는지"
  - "테스트 3개 모두 통과하는지"
```

## 전체 예시

```yaml
meta:
  created: 2026-04-11
  spec_source: "사용자 대화 — 세션 만료 시 자동 갱신 기능 요구"
  as_is: |
    현재 src/auth/session.ts는 getToken/setToken만 제공. 만료 체크 없음.
    API 호출 시 401이 나면 사용자에게 재로그인 요구.
  to_be: |
    세션 토큰이 만료되면 자동으로 refresh API를 호출해 갱신한다.
    caller는 만료 여부를 신경 쓰지 않고 refreshToken() 한 번 호출하면 된다.
    실패 시 명확한 AuthError를 throw한다.

tasks:
  - id: T01
    name: AuthError 클래스 정의
    blocked_by: []
    human_gate: null
    done: false
    status: pending
    category: feat
    spec: |
      `src/auth/errors.ts` 파일을 새로 생성하고 AuthError 클래스를 정의한다.
      - Error를 상속
      - code: string 속성 포함 (REFRESH_FAILED, INVALID_TOKEN 등 enum)
      - message 생성자 인자로 받음
    output: src/auth/errors.ts
    lifecycle:
      started_at: null
      verified_at: null
      committed_at: null
      worker_id: null
      commit: null

  - id: T02
    name: refreshToken 함수 구현
    blocked_by: [T01]
    human_gate: null
    done: false
    status: pending
    category: feat
    spec: |
      `src/auth/session.ts`에 refreshToken 함수 추가. 시그니처:
        refreshToken(token: string): Promise<string>
      로직:
      - 토큰 만료 체크 (jwt decode로 exp 확인)
      - 만료되면 POST /auth/refresh 호출 후 새 토큰 반환
      - 유효하면 그대로 반환
      - API 실패 시 AuthError(code='REFRESH_FAILED') throw
    output: src/auth/session.ts
    verify_checks:
      - "refreshToken이 export되었는지"
      - "AuthError import 경로가 올바른지"
    lifecycle:
      started_at: null
      verified_at: null
      committed_at: null
      worker_id: null
      commit: null

  - id: T03
    name: refreshToken 테스트
    blocked_by: [T02]
    human_gate: null
    done: false
    status: pending
    category: test
    spec: |
      `src/auth/session.test.ts`에 refreshToken 테스트 3개 추가:
      1. 만료된 토큰 입력 → refresh API 모킹 → 새 토큰 반환 확인
      2. 유효한 토큰 입력 → API 호출 없이 그대로 반환 확인
      3. refresh API 실패 → AuthError throw 확인
    output: src/auth/session.test.ts
    verify_checks:
      - "3개 테스트 모두 정의됨"
      - "npm test 통과"
    lifecycle:
      started_at: null
      verified_at: null
      committed_at: null
      worker_id: null
      commit: null

  - id: T04
    name: 기존 caller 마이그레이션 제안서 작성
    blocked_by: [T02, T03]
    human_gate: null
    done: false
    category: docs
    spec: |
      기존 getToken() 호출 위치를 조사하고 마이그레이션 제안서를 작성한다.
      - grep으로 호출 지점 전수 조사
      - 각 caller의 컨텍스트와 위험도 정리
      - 치환 전략, 예상 영향, 테스트 계획 작성
      - 아직 실제 caller 코드는 변경하지 않음
    output: docs/auth-caller-migration-plan.md

  - id: T05
    name: caller 마이그레이션 승인
    blocked_by: [T04]
    human_gate: approve
    done: false
    category: review
    spec: |
      인간이 docs/auth-caller-migration-plan.md를 검토하고 승인한다.
      승인 전에는 실제 caller 마이그레이션을 수행하지 않는다.

  - id: T06
    name: 기존 caller 마이그레이션 적용
    blocked_by: [T05]
    human_gate: null
    done: false
    category: refactor
    spec: |
      승인된 docs/auth-caller-migration-plan.md에 따라 기존 getToken() 호출을 refreshToken()으로 전환한다.
      - 승인된 범위 밖의 caller는 변경하지 않음
      - 각 caller 컨텍스트에 맞게 안전하게 치환
      - 테스트 통과 확인
    notes: "호출 지점이 많아 T05 승인 뒤에만 적용한다."
```

## 팁

- **id 네이밍**: 숫자 접두어(`T01`)는 순서와 무관하게 유니크 식별자. 실행 순서는 `blocked_by`가 결정.
- **크기 조절**: 태스크 하나가 30분 넘어갈 것 같으면 쪼갤 것. 반대로 5분짜리 여러 개면 합칠 것.
- **done 초기값**: 전부 `false`. 이미 구현된 부분이 있으면 해당 태스크에 `done: true  # 소급 반영`로 표시.
- **주석 활용**: YAML 주석(`#`)으로 결정 배경, 완료 노트, 진행 상태(wip)를 기록.
