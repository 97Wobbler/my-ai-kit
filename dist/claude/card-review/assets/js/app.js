import { fetchDevVersion, fetchSession, postAction } from "./api.js";
import { animateCardIn, animateCardOut, attachCardGestures } from "./gestures.js";
import { renderApp } from "./render.js";
import { getModel, setSession, setUI, subscribe, updateModel } from "./state.js";

const root = document.querySelector("#app");
let memoTimer = null;
let devTimer = null;
let detachGestures = () => {};
let interactionLocked = false;
let requestQueue = Promise.resolve();

function memoValue() {
  return root.querySelector("#memo")?.value || "";
}

async function dispatch(payload, { showBusy = true } = {}) {
  if (showBusy && getModel().ui.busy) return null;
  if (showBusy) setUI({ busy: true, error: "" });
  try {
    const request = requestQueue.then(() => postAction(payload));
    requestQueue = request.catch(() => null);
    const session = await request;
    const model = updateModel({ session, ui: showBusy ? { busy: false } : null });
    return model.session;
  } catch (error) {
    setUI({ ...(showBusy ? { busy: false } : {}), error: error.message || String(error) });
    return null;
  }
}

async function transition(payload, exitDirection, enterDirection = "stack", origin = {}) {
  if (interactionLocked || getModel().ui.busy) return null;
  interactionLocked = true;
  clearTimeout(memoTimer);
  try {
    await animateCardOut(root, exitDirection, origin);
    const session = await dispatch(payload);
    if (session && !session.finished) await animateCardIn(root, enterDirection);
    return session;
  } finally {
    interactionLocked = false;
  }
}

function scheduleMemoSave(value) {
  clearTimeout(memoTimer);
  const itemId = getModel().session?.currentId;
  if (!itemId) return;
  const previous = getModel().session?.memos[itemId] || "";
  if (value === previous) return;
  memoTimer = setTimeout(() => {
    dispatch({ action: "memo", id: itemId, memo: value }, { showBusy: false });
  }, 180);
}

async function handleAction(action, result) {
  clearTimeout(memoTimer);
  const session = getModel().session;
  if (action === "undo" && !session?.canUndo) return;
  if (action === "redo" && !session?.canRedo) return;
  if (action === "finish") {
    if (!confirm("현재 결과를 저장하고 검토를 종료할까요? 미분류 항목은 그대로 남습니다.")) return;
    await transition({ action: "finish", memo: memoValue() }, "down");
    return;
  }
  if (action === "classify") {
    await transition({ action, result, memo: memoValue() }, result === "A" ? "left" : "right");
    return;
  }
  if (action === "skip") {
    await transition({ action, memo: memoValue() }, "down");
    return;
  }
  if (action === "undo") {
    await transition({ action }, "soft-down", "top");
    return;
  }
  if (action === "redo") {
    await transition({ action }, "soft-up", "bottom");
    return;
  }
  if (action === "reopen") {
    const session = await dispatch({ action });
    if (session) await animateCardIn(root);
    return;
  }
  await dispatch({ action });
}

function handleUIAction(action) {
  if (action === "open-drawer") {
    setUI({ drawerOpen: true });
    root.querySelector(".progress-drawer [data-ui-action='close-drawer']")?.focus();
  }
  if (action === "close-drawer") {
    setUI({ drawerOpen: false });
    root.querySelector(".progress-chip")?.focus();
  }
}

async function handleFocus(id) {
  setUI({ drawerOpen: false });
  const session = await dispatch({ action: "focus", id });
  if (session) await animateCardIn(root);
}

function handleGesture(result, direction, origin) {
  transition({ action: "classify", result, memo: memoValue() }, direction, "stack", origin);
}

function handleKeydown(event) {
  const model = getModel();
  if (!model.session) return;
  const tagName = document.activeElement?.tagName;
  const editing = tagName === "TEXTAREA" || tagName === "INPUT";

  if (event.key === "Escape") {
    if (editing) document.activeElement.blur();
    else if (model.ui.drawerOpen) handleUIAction("close-drawer");
    return;
  }
  if (event.key === "Tab" && model.ui.drawerOpen) {
    const focusable = [...root.querySelectorAll(".progress-drawer button:not(:disabled)")];
    if (!focusable.length) return;
    const currentIndex = focusable.indexOf(document.activeElement);
    const nextIndex = event.shiftKey
      ? (currentIndex <= 0 ? focusable.length - 1 : currentIndex - 1)
      : (currentIndex === focusable.length - 1 ? 0 : currentIndex + 1);
    event.preventDefault();
    focusable[nextIndex].focus();
    return;
  }
  if (editing || model.session.finished || model.ui.busy || interactionLocked) return;

  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "z") {
    event.preventDefault();
    handleAction(event.shiftKey ? "redo" : "undo");
    return;
  }
  if (event.key === "ArrowLeft") {
    event.preventDefault();
    handleAction("classify", "A");
  } else if (event.key === "ArrowRight") {
    event.preventDefault();
    handleAction("classify", "B");
  } else if (event.key === "ArrowDown") {
    event.preventDefault();
    handleAction("skip");
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    handleAction("undo");
  } else if (event.key.toLowerCase() === "m") {
    event.preventDefault();
    root.querySelector("#memo")?.focus();
  }
}

async function startDevReload() {
  if (devTimer) return;
  let baseline = null;

  const poll = async () => {
    try {
      const current = await fetchDevVersion();
      if (baseline === null) baseline = current.version;
      else if (current.version !== baseline) {
        window.location.reload();
        return;
      }
    } catch {
      // The server may be restarting; retry without interrupting the review.
    }
    devTimer = window.setTimeout(poll, 700);
  };
  poll();
}

const handlers = {
  onAction: handleAction,
  onUIAction: handleUIAction,
  onFocus: handleFocus,
  onMemoBlur: scheduleMemoSave,
};

subscribe((model) => {
  detachGestures();
  renderApp(root, model, handlers);
  detachGestures = attachCardGestures(root, {
    isLocked: () => interactionLocked || getModel().ui.busy || getModel().ui.drawerOpen,
    onCommit: handleGesture,
  });
});
window.addEventListener("keydown", handleKeydown);

fetchSession()
  .then((session) => {
    setSession(session);
    if (session.devMode) startDevReload();
  })
  .catch((error) => setUI({ error: error.message || String(error) }));
