# my-ai-kit

`my-ai-kit`은 Claude Code와 Codex CLI에서 함께 사용할 수 있는 개인용
플러그인 마켓플레이스입니다.

반복해서 사용하는 에이전트 워크플로우를 런타임별 설치 가능한 플러그인으로
묶어 배포합니다.

플러그인이 예상과 다르게 동작하면 `97Wobbler/my-ai-kit`에 plugin name,
runtime, expected behavior, observed behavior를 포함해 issue를 열어주세요.

## 플러그인

### `autorun`

- 큰 작업을 dependency-aware `workplan.yaml`로 나눈 뒤, 검증과 커밋 단위로
  자동 실행하는 오케스트레이션 워크플로우입니다.
- `0.3.3` 기준 두 가지 워크플로우를 제공합니다. Full Autorun은 번들 MCP
  서버로 계획 생성, 검증, task split, 실행 배치, lifecycle 상태 전이,
  active-task readiness filtering, proposal-worker timeout classification,
  advisory task-graph budgeting을 관리합니다.
- `autorun:lite`는 작은 작업을 위한 별도 MCP-less workflow입니다. 작은
  작업에서도 durable `workplan.yaml`, visible progress, 검증, 명시적 path
  staging, task별 commit 규칙을 유지합니다.
- OpenAI/Codex tool schema 변환과 호환되도록 MCP tool input schema는
  object-root 형태로 노출합니다.

#### 스킬 목록

- `autorun`: PLAN 모드에서 작업 그래프를 만들고, RUN 모드에서 실행 가능한
  작업을 project-root `workplan.yaml` state 기반으로 위임, 검증, 커밋.
- `lite`: 작은 작업을 MCP 없이 project-root `workplan.yaml` state 기반으로
  계획, 실행, 검증, 커밋.

### `skill-forge`

- Claude Code와 Codex CLI용 skill을 하나의 runtime-neutral spec에서
  관리하기 위한 작성/컴파일 도구입니다.
- 같은 workflow를 두 런타임에 따로 손으로 맞추는 대신, 하나의 원형을
  관리하고 런타임 차이만 명시적으로 분리합니다.
- 현재 공개 버전은 `0.1.6`입니다.

#### 스킬 목록

- `skill-forge-spec`: cross-runtime skill의 원형 spec을 작성.
- `skill-forge-compile`: spec을 Claude Code와 Codex CLI용 `SKILL.md`로 컴파일.

### `scribe`

- 로컬 STT로 음성 파일을 전사하고, 같은 음성에서 나온 여러 STT 전사본을
  비교해 canonical transcript를 작성하는 기록 정리 워크플로우입니다.
- Scribe 0.1.4 기준, 로컬 STT MCP MVP는 사용자 머신에 설치된
  `faster-whisper`, `ffmpeg`, 모델 파일을 사용합니다. STT 모델은
  플러그인에 포함되지 않습니다.
- `scribe_stt_status`는 로컬 STT 의존성 상태와 간단한 설치 안내를
  확인합니다.
- `scribe_setup_stt`는 명시적으로 요청했을 때 MCP 서버 Python 환경에
  누락된 Python package 의존성을 설치할 수 있습니다. `ffmpeg` 같은 OS
  package는 시스템 package manager로 설치하도록 안내합니다.
- `scribe_transcribe_file`은 하나의 preset으로 음성 파일을 전사하고,
  `scribe_transcribe_variants`는 같은 음성 파일에서 1~4개의 deterministic
  variant를 만듭니다. 긴 음성처럼 synchronous 호출이 불안정할 수 있는
  입력은 guard가 background job API 사용을 권장합니다.
- `scribe_transcribe_job_start`, `scribe_transcribe_job_status`,
  `scribe_transcribe_job_collect`, `scribe_transcribe_job_cancel`은 완료된
  variant를 점진적으로 저장하는 background STT job 흐름을 제공합니다.
- 전사 결과는 `job.json`, `manifest.json`, `variants/<variant_id>.md`,
  `variants/<variant_id>.json` 구조로 저장되며, `canon`은 이 manifest,
  job directory, 또는 생성된 variant markdown을 입력으로 받을 수 있습니다.
- `scribe:transcribe`는 음성 파일 path를 받아 안전한 기본값으로 MCP tools를
  오케스트레이션하고, 긴 음성에 대한 기대치를 정리한 뒤 전사 결과와 다음
  권장 작업을 반환하는 skill-first 전사 표면입니다.
- 회의 목적, 인터뷰 주제, 제품명, 참여자, 약어 같은 upfront context가 함께
  제공되면 해석 단서로 사용합니다. 다만 먼저 transcript variant를 비교해
  evidence-first로 모호함을 도출하고, canonical output을 만들기 전에 전사
  근거에서 나온 material question을 provenance와 contamination risk가 표시된
  grouped/staged review로 묻습니다. 이전 Scribe context를 자동으로 기억하거나
  불러오는 기능은 구현된 기능으로 설명하지 않습니다.

#### 스킬 목록

- `transcribe`: 음성 파일 path를 받아 로컬 STT 전사 작업을 오케스트레이션하고
  전사 결과와 다음 권장 작업을 정리.
- `canon`: 여러 STT 전사본을 canonical 전사, ambiguity review,
  reconciliation ledger로 정리.

### `restate`

- 작업을 시작하기 전에 사용자 요청을 다시 서술해 목표, 범위, 제약, 가정을
  확인합니다.
- 작은 오해가 큰 구현 낭비로 이어지기 전에, 에이전트가 이해한 내용을 먼저
  드러내고 사용자가 바로잡을 수 있게 합니다.
- 현재 공개 버전은 `0.1.3`입니다.

#### 스킬 목록

- `restate`: 최신 요청을 실행 가능한 요구사항 요약으로 바꾸고 확인을 요청.

### `lucid`

- 모호한 요청을 실행 전에 선택 가능한 해석과 결정 옵션으로 나눕니다.
- 선택이 끝난 뒤에는 목표, 범위, 결정, 요구사항, 성공 기준, 미결사항을 담은
  실행 브리프로 고정합니다.
- 현재 공개 버전은 `0.1.1`입니다.

#### 스킬 목록

- `branch`: 모호한 요청을 `light`, `deep`, `interview` 모드로 나눠 선택지와
  확인 질문을 제시.
- `brief`: 선택된 의도와 결정 사항을 실행 가능한 브리프로 정리.

### `edu-sim`

- 에듀테크 정책, 기능, 사업 전략, 실험안을 한국 교사 30명 고정 페르소나에
  전수 시뮬레이션하고, 의외 반응과 블라인드스팟 중심의 보고서를 생성합니다.
- 현재 공개 버전은 `0.1.2`입니다.
- 대표성 추정이나 다수 의견 요약이 아니라, 놓치기 쉬운 우려와 기회를 찾는
  사용자 리서치 보조 워크플로우입니다.

#### 스킬 목록

- `edu-sim`: 30개 한국 교사 페르소나 응답을 수집하고
  `report.md`로 종합.

### `prism`

- 렌즈, 프레임, 모델, 스탠스, 휴리스틱 같은 분석 도구를 찾아 조합해 더
  구조적인 검토와 토론을 돕습니다.
- 막연한 "전문가처럼 봐줘" 대신, 어떤 관점과 분석 도구로 볼지 명시해
  검토의 밀도와 재현성을 높입니다.
- 현재 공개 버전은 `0.5.9`입니다.

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
- 현재 공개 버전은 `0.1.2`입니다.

#### 스킬 목록

- `studycoach`: 학습 목표를 진단하고 Known/Unknown 매트릭스, 로드맵, 세션
  기록을 관리.

### `slackbox`

- Local Slackbox mode는 로컬 stdio MCP 서버로 Slack 채널, 사용자, 검색,
  멘션, 스레드 context를 crawl/cache/retrieval하는 플러그인입니다.
- Codex local mode는 매번 shell 환경변수를 export하지 않고도
  `~/.slackbox/config.env` 로컬 설정 파일에서 Slack User OAuth Token을
  읽을 수 있습니다.
- Codex setup guide는 macOS/Windows용 짧은 setup launcher 실행 절차를
  안내하며, 사용자는 토큰을 chat이 아니라 새 terminal의 wizard prompt에
  붙여넣습니다.
- 현재 MVP는 제한된 범위의 수집과 로컬 조회까지만 다룹니다. 결과 해석
  workflow는 이번 release 범위에 포함하지 않습니다.
- Official Slack Remote MCP는 별도의 OAuth-backed 경로입니다. `/mcp` 또는
  `codex mcp login`으로 연결하는 Slack 공식 remote MCP이며, Slackbox의
  로컬 crawl/cache/retrieval 동작과 동일하지 않습니다.
- 예시는 합성 값만 사용합니다: `#project-updates`, `U123EXAMPLE`,
  `"release checklist"`.
- 현재 공개 버전은 `0.1.3`입니다.

#### 스킬 목록

- `slackbox`: 자연어 Slack 수집 요청을 사용 가능한 Slackbox MCP tools로
  라우팅.

### `waypoint`

- docs-first repository recovery harness를 만드는 플러그인입니다.
- `AGENTS.md`와 visible `docs/` 문서들을 중심으로, 다음 세션이 어디에서
  다시 시작해야 하는지 알 수 있는 waypoint를 남깁니다.
- 현재 MVP는 greenfield 생성, brownfield `init` audit-only 검사,
  documentation cleanup dry-run audit을 지원합니다. brownfield repository의
  기존 규칙이나 문서를 덮어쓰지 않습니다.
- `.waypoint/config.yaml`은 문서 home을 찾기 위한 locator일 뿐이며, primary
  state는 visible docs에 둡니다.
- 현재 공개 버전은 `0.1.2`입니다.

#### 스킬 목록

- `waypoint`: Waypoint workflow 라우터와 설명.
- `init`: greenfield docs harness 생성 또는 brownfield audit-only
  discovery.
- `audit`: 문서 비대화, SSOT drift, 역할 혼합, stale plan,
  decision-consolidation 후보를 dry-run으로 점검.
- `doctor`: routing, configured document homes, marker blocks, local
  Markdown links를 read-only로 검사.

## 설치

Claude Code:

```bash
claude plugin marketplace add 97Wobbler/my-ai-kit
```

Codex CLI:

```bash
codex plugin marketplace add 97Wobbler/my-ai-kit
codex
/plugins
```

마켓플레이스를 추가한 뒤 필요한 플러그인을 설치합니다.

Autorun MCP tools는 플러그인 설치 후 새 세션에서 노출됩니다. Codex에서는
`/mcp`로 `autorun` 서버와 tools 상태를 확인할 수 있습니다. 작은 작업은
`autorun:lite` workflow로 MCP 없이 진행할 수 있습니다.

Slackbox는 설치 후 새 세션에서 로컬 MCP tools를 사용합니다. 요청한 수집
범위에 맞는 `xoxp-` Slack User OAuth Token과 읽기 권한이 필요합니다.
Claude Code에서는 plugin sensitive configuration으로 설정하고, Codex에서는
환경 변수 또는 MCP config로 전달합니다. 실제 token을 chat, 예시, 문서에
붙여넣지 마세요.

Slack 공식 remote MCP를 쓰려면 Claude Code에서는 `/mcp` OAuth 흐름을,
Codex에서는 `codex mcp login <server-name>`을 사용합니다. 이 경로는
Slackbox local mode의 로컬 수집 cache를 만들거나 조회하지 않습니다.

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
