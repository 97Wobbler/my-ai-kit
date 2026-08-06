import { renderValue } from "./markdown.js";

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function fieldSpec(spec) {
  return typeof spec === "string" ? { render: spec } : spec || {};
}

function valueOf(item, key) {
  if (Object.prototype.hasOwnProperty.call(item, key)) return item[key];
  return (item.fields || {})[key];
}

function currentItem(session) {
  return session.items.find((item) => item.id === session.currentId) || null;
}

function statusFor(session, id) {
  return session.statuses[id] || (session.skipped.includes(id) ? "skip" : null);
}

function statusLabel(status) {
  if (status === "A") return "A";
  if (status === "B") return "B";
  if (status === "skip") return "스킵";
  return "미분류";
}

function itemTitle(item, option, index) {
  const fields = Object.entries(option.fields || {});
  const titleField = fields.find(([, rawSpec]) => ["h1", "h2", "h3"].includes(fieldSpec(rawSpec).render));
  const preferredKey = titleField?.[0] || (Object.prototype.hasOwnProperty.call(item, "title") ? "title" : null);
  const value = preferredKey ? valueOf(item, preferredKey) : null;
  if (typeof value === "string" && value.trim()) return value.trim();
  return `항목 ${index + 1}`;
}

function progressPercent(summary) {
  return Math.round(((summary.a + summary.b) / Math.max(summary.total, 1)) * 100);
}

function renderDrawer(session, drawerOpen) {
  const { option, summary } = session;
  const rows = drawerOpen ? session.items.map((item, index) => {
    const status = statusFor(session, item.id);
    return `
      <button class="item-row ${item.id === session.currentId ? "is-current" : ""}" data-focus-id="${escapeHtml(item.id)}">
        <span class="status-dot status-${status || "empty"}" aria-hidden="true"></span>
        <span class="item-copy">
          <span class="item-title">${escapeHtml(itemTitle(item, option, index))}</span>
          <span class="item-id" title="${escapeHtml(item.id)}">${escapeHtml(item.id)}</span>
        </span>
        <span class="item-status">${statusLabel(status)}</span>
      </button>`;
  }).join("") : "";

  return `
    <button class="drawer-backdrop ${drawerOpen ? "is-open" : ""}" data-ui-action="close-drawer" aria-label="진행상황 닫기" tabindex="-1"></button>
    <aside class="progress-drawer ${drawerOpen ? "is-open" : ""}" role="dialog" aria-label="진행상황" aria-modal="${drawerOpen ? "true" : "false"}" aria-hidden="${drawerOpen ? "false" : "true"}" ${drawerOpen ? "" : "inert"}>
      <div class="drawer-head">
        <div>
          <div class="eyebrow">진행상황</div>
          <h2>${summary.a + summary.b} / ${summary.total} 분류됨</h2>
        </div>
        <button class="icon-button" data-ui-action="close-drawer" aria-label="진행상황 닫기">×</button>
      </div>
      <div class="summary-grid">
        <div class="summary-cell summary-a"><strong>${summary.a}</strong><span>${escapeHtml(option.groupAName)}</span></div>
        <div class="summary-cell summary-b"><strong>${summary.b}</strong><span>${escapeHtml(option.groupBName)}</span></div>
        <div class="summary-cell"><strong>${summary.unclassified}</strong><span>미분류</span></div>
        <div class="summary-cell"><strong>${summary.skipped}</strong><span>스킵</span></div>
      </div>
      <div class="drawer-list" role="list">${rows}</div>
    </aside>`;
}

function renderFinished(session) {
  const { option, summary } = session;
  return `
    <section class="finished-panel">
      <div class="finished-mark">✓</div>
      <h2>검토가 종료되었습니다</h2>
      <p>결과는 JSONL 파일에 저장되었습니다.</p>
      <div class="finished-summary">
        <div><strong>${summary.a}</strong><span>${escapeHtml(option.groupAName)}</span></div>
        <div><strong>${summary.b}</strong><span>${escapeHtml(option.groupBName)}</span></div>
        <div><strong>${summary.unclassified}</strong><span>미분류</span></div>
      </div>
      <code class="output-path">${escapeHtml(session.outputPath)}</code>
      <button class="primary-button" data-action="reopen">검토 계속하기</button>
    </section>`;
}

function renderReviewStage(session, busy) {
  const item = currentItem(session);
  if (!item) return `<section class="empty-panel">검토할 카드가 없습니다.</section>`;

  const { option } = session;
  const fields = Object.entries(option.fields || {});
  const currentStatus = statusFor(session, item.id);
  const fieldMarkup = fields.map(([key, rawSpec], index) => {
    const spec = fieldSpec(rawSpec);
    const value = valueOf(item, key);
    if (value == null || value === "") return "";
    return `
      <section class="card-field">
        <div class="field-label">${escapeHtml(spec.label || key)}</div>
        <div data-render-field="${index}"></div>
      </section>`;
  }).join("");

  return `
    <section class="review-stage" aria-busy="${busy ? "true" : "false"}">
      <div class="decision-zone decision-a">
        <button class="decision-button" data-action="classify" data-result="A" ${busy ? "disabled" : ""}>
          <span class="decision-arrow">←</span>
          <span class="decision-name">${escapeHtml(option.groupAName)}</span>
          <span class="decision-hint">왼쪽 방향키</span>
        </button>
      </div>
      <div class="card-stack">
        <div class="stack-card stack-card-back" aria-hidden="true"></div>
        <article class="review-card">
          <div class="drag-stamp stamp-a" aria-hidden="true">${escapeHtml(option.groupAName)}</div>
          <div class="drag-stamp stamp-b" aria-hidden="true">${escapeHtml(option.groupBName)}</div>
          <header class="card-meta">
            <span class="status-badge status-${currentStatus || "empty"}">${statusLabel(currentStatus)}</span>
            <span class="current-id" title="${escapeHtml(item.id)}">${escapeHtml(item.id)}</span>
          </header>
          <div class="card-fields">${fieldMarkup}</div>
          <div class="memo-box">
            <label for="memo">메모 <span>선택</span></label>
            <textarea id="memo" rows="2" placeholder="분류 이유나 다시 볼 내용을 적어두세요.">${escapeHtml(session.memos[item.id] || "")}</textarea>
          </div>
        </article>
      </div>
      <div class="decision-zone decision-b">
        <button class="decision-button" data-action="classify" data-result="B" ${busy ? "disabled" : ""}>
          <span class="decision-arrow">→</span>
          <span class="decision-name">${escapeHtml(option.groupBName)}</span>
          <span class="decision-hint">오른쪽 방향키</span>
        </button>
      </div>
      <div class="decision-zone decision-skip">
        <button class="decision-button" data-action="skip" ${busy ? "disabled" : ""}>
          <span class="decision-arrow">↓</span>
          <span class="decision-name">일단 스킵</span>
          <span class="decision-hint">목록에 남겨두기</span>
        </button>
      </div>
    </section>`;
}

function hydrateFields(root, session) {
  const item = currentItem(session);
  if (!item || session.finished) return;
  Object.entries(session.option.fields || {}).forEach(([key, rawSpec], index) => {
    const target = root.querySelector(`[data-render-field="${index}"]`);
    if (!target) return;
    const spec = fieldSpec(rawSpec);
    target.appendChild(renderValue(valueOf(item, key), spec.render || "markdown"));
  });
}

function bind(root, handlers) {
  root.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => handlers.onAction(button.dataset.action, button.dataset.result));
  });
  root.querySelectorAll("[data-ui-action]").forEach((button) => {
    button.addEventListener("click", () => handlers.onUIAction(button.dataset.uiAction));
  });
  root.querySelectorAll("[data-focus-id]").forEach((button) => {
    button.addEventListener("click", () => handlers.onFocus(button.dataset.focusId));
  });
  const memo = root.querySelector("#memo");
  if (memo) memo.addEventListener("blur", () => handlers.onMemoBlur(memo.value));
}

export function renderApp(root, model, handlers) {
  const { session, ui } = model;
  if (!session) {
    root.className = "app-loading";
    root.textContent = ui.error || "카드 검토기를 불러오는 중...";
    return;
  }

  const { option, summary } = session;
  const percent = progressPercent(summary);
  root.className = "app-shell";
  root.innerHTML = `
    <header class="topbar" ${ui.drawerOpen ? "inert" : ""}>
      <div class="topbar-main">
        <h1 title="${escapeHtml(option.title)}">${escapeHtml(option.title)}</h1>
        <div class="topbar-actions">
          <button class="progress-chip" data-ui-action="open-drawer" aria-label="진행상황 열기">
            <span>${summary.a + summary.b} / ${summary.total}</span>
            <span class="button-text">진행상황</span>
          </button>
          <button class="icon-button" data-action="undo" ${session.canUndo && !ui.busy ? "" : "disabled"} aria-label="실행 취소">↶<span class="button-text">Undo</span></button>
          <button class="icon-button" data-action="redo" ${session.canRedo && !ui.busy ? "" : "disabled"} aria-label="다시 실행">↷<span class="button-text">Redo</span></button>
          <button class="finish-button" data-action="finish" ${ui.busy ? "disabled" : ""}><span class="finish-icon">✓</span><span class="button-text">저장하고 종료</span></button>
        </div>
      </div>
      <div class="progress-line"><span style="width:${percent}%"></span></div>
    </header>
    <main class="review-main" ${ui.drawerOpen ? "inert" : ""}>
      ${session.finished ? renderFinished(session) : renderReviewStage(session, ui.busy)}
    </main>
    ${renderDrawer(session, ui.drawerOpen)}
    ${ui.error ? `<div class="error-toast" role="alert">${escapeHtml(ui.error)}</div>` : ""}`;

  hydrateFields(root, session);
  bind(root, handlers);
}
