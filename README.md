# my-ai-kit

`my-ai-kit`은 Claude Code와 Codex CLI에서 함께 사용할 수 있는 개인용
플러그인 마켓플레이스입니다.

반복해서 사용하는 에이전트 워크플로우를 런타임별 설치 가능한 플러그인으로
묶어 배포합니다.

## 플러그인

### `autorun`

- 큰 작업을 dependency-aware `workplan.yaml`로 나눈 뒤, 검증과 커밋 단위로
  자동 실행하는 오케스트레이션 워크플로우입니다.
- `0.2.2` 기준 Claude Code와 Codex CLI에 번들 MCP 서버를 함께 제공해,
  계획 생성, 검증, task split, 실행 배치, lifecycle 상태 전이를 MCP tool로
  관리할 수 있습니다.
- OpenAI/Codex tool schema 변환과 호환되도록 MCP tool input schema는
  object-root 형태로 노출합니다.
- MCP tool은 별도 숨은 plan state가 아니라 project-root `workplan.yaml`을
  직접 읽고 쓰며, 이 파일이 durable source of truth입니다.
- 막연한 "알아서 해줘"를 추적 가능한 작업 그래프로 바꾸고, 각 단계가 검증과
  커밋으로 남도록 합니다.
- MCP가 등록되지 않았거나 실행 환경에서 사용할 수 없으면 같은
  project-root `workplan.yaml`을 직접 편집하는 방식으로 계속 동작합니다.

#### 스킬 목록

- `autorun`: PLAN 모드에서 작업 그래프를 만들고, RUN 모드에서 실행 가능한
  작업을 project-root `workplan.yaml` state 기반으로 위임, 검증, 커밋.

### `skill-forge`

- Claude Code와 Codex CLI용 skill을 하나의 runtime-neutral spec에서
  관리하기 위한 작성/컴파일 도구입니다.
- 같은 workflow를 두 런타임에 따로 손으로 맞추는 대신, 하나의 원형을
  관리하고 런타임 차이만 명시적으로 분리합니다.

#### 스킬 목록

- `skill-forge-spec`: cross-runtime skill의 원형 spec을 작성.
- `skill-forge-compile`: spec을 Claude Code와 Codex CLI용 `SKILL.md`로 컴파일.

### `restate`

- 작업을 시작하기 전에 사용자 요청을 다시 서술해 목표, 범위, 제약, 가정을
  확인합니다.
- 작은 오해가 큰 구현 낭비로 이어지기 전에, 에이전트가 이해한 내용을 먼저
  드러내고 사용자가 바로잡을 수 있게 합니다.

#### 스킬 목록

- `restate`: 최신 요청을 실행 가능한 요구사항 요약으로 바꾸고 확인을 요청.

### `lucid`

- 모호한 요청을 실행 전에 선택 가능한 해석과 결정 옵션으로 나눕니다.
- 선택이 끝난 뒤에는 목표, 범위, 결정, 요구사항, 성공 기준, 미결사항을 담은
  실행 브리프로 고정합니다.
- `restate`가 하나의 이해안을 확인하는 도구라면, `lucid`는 여러 해석이
  가능한 요청에서 선택지를 만들고 합의된 방향을 문서화하는 도구입니다.

#### 스킬 목록

- `branch`: 모호한 요청을 `light`, `deep`, `interview` 모드로 나눠 선택지와
  확인 질문을 제시.
- `brief`: 선택된 의도와 결정 사항을 실행 가능한 브리프로 정리.

### `my-ai-kit-feedback`

- my-ai-kit 플러그인이나 스킬을 쓰다가 이상하다고 느낀 점을 GitHub issue
  draft로 정리하는 피드백 워크플로우입니다.
- 사용자가 명시적으로 호출하고 제공한 세션 근거만 분석합니다. `.codex`,
  `.claude`, 로컬 로그, transcript를 자동으로 수집하지 않습니다.
- 최소 3단계 동의 흐름을 사용합니다: 분석 범위와 근거 출처 확인, 근거 요약과
  redaction 승인, GitHub issue 발행 전 최종 승인.
- 기본은 요약 중심이며, 민감정보와 개인/회사/경로 정보는 issue draft에
  포함하기 전에 redaction합니다.

#### 스킬 목록

- `my-ai-kit-feedback`: 기대 동작, 실제 동작, 사용 runtime, 사용자가 제공한
  근거를 바탕으로 privacy-conscious GitHub issue draft를 작성.

### `prism`

- 렌즈, 프레임, 모델, 스탠스, 휴리스틱 같은 분석 도구를 찾아 조합해 더
  구조적인 검토와 토론을 돕습니다.
- 막연한 "전문가처럼 봐줘" 대신, 어떤 관점과 분석 도구로 볼지 명시해
  검토의 밀도와 재현성을 높입니다.

#### 스킬 목록

- `prism`: Prism 소개와 새 instrument 생성 라우터.
- `search`: 상황에 맞는 Prism instrument를 검색.
- `fetch`: 선택한 instrument를 subagent나 다른 workflow에 전달할 수 있게 준비.
- `debate`: 여러 instrument 관점으로 문서, 제안, 문제를 검토하거나 해결.

### `studycoach`

- 프로젝트 로컬 학습 상태를 기반으로 자기주도 학습을 이어갈 수 있게 돕는
  학습 코치입니다.
- 무엇을 알고 모르는지부터 정리해, 학습을 일회성 메모가 아니라 이어지는
  프로젝트로 관리합니다.

#### 스킬 목록

- `studycoach`: 학습 목표를 진단하고 Known/Unknown 매트릭스, 로드맵, 세션
  기록을 관리.

### `stateful`

- 레포지토리 안에 agent state를 남겨 다음 세션이 채팅 기억에 의존하지 않고
  복구할 수 있게 합니다.
- 긴 작업을 여러 세션에 걸쳐 이어갈 때, "어디까지 했는지"를 다시 설명하는
  시간을 줄이고 workplan, 결정, handoff를 파일로 남깁니다.

#### 스킬 목록

- `stateful`: Stateful 플러그인의 라우터.
- `stateful-init`: 현재 레포지토리에 `.stateful/`, 복구 스크립트, 런타임별
  진입 지침을 설치.
- `stateful-doctor`: workplan과 generated state의 정합성을 검사.
- `stateful-close`: 다음 세션을 위한 handoff를 기록.
- `stateful-plan`: roadmap 내용을 실행 가능한 workplan 후보로 변환.
- `stateful-archive`: 완료된 workplan 작업을 검토하고 durable summary를 제안.

## 설치

Claude Code:

```bash
claude plugin marketplace add 97Wobbler/my-ai-kit
claude plugin install stateful@my-ai-kit
```

Codex CLI:

```bash
codex plugin marketplace add 97Wobbler/my-ai-kit
codex
/plugins
```

마켓플레이스를 추가한 뒤 Codex 플러그인 브라우저에서 필요한 플러그인을
설치합니다.

Autorun MCP tools는 플러그인 설치 후 새 세션에서 노출됩니다. Codex에서는
`/mcp`로 `autorun` 서버와 tools 상태를 확인할 수 있습니다.

## 저장소 구성

이 공개 저장소에는 마켓플레이스 manifest와 런타임별 배포 패키지만 포함됩니다.

```text
.claude-plugin/       Claude Code 마켓플레이스 카탈로그
.agents/plugins/      Codex CLI 마켓플레이스 카탈로그
dist/claude/          Claude Code 플러그인 패키지
dist/codex/           Codex CLI 플러그인 패키지
```

개발 소스, Skill Forge spec, private state, report는 공개 스냅샷에 포함하지
않습니다.
