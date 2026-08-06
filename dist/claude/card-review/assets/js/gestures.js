const INTERACTIVE_SELECTOR = "textarea, input, button, a, select, [contenteditable='true']";
const AXIS_LOCK_DISTANCE = 7;

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function reducedMotion() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function elements(root) {
  return {
    card: root.querySelector(".review-card"),
    stage: root.querySelector(".review-stage"),
  };
}

function thresholdFor(card) {
  return clamp(card.getBoundingClientRect().width * .22, 84, 140);
}

function clearFeedback(stage, card) {
  if (stage) {
    stage.classList.remove("is-dragging", "drag-left", "drag-right");
    stage.style.setProperty("--drag-progress", "0");
  }
  if (card) {
    card.style.transform = "";
    card.style.opacity = "";
  }
}

function showFeedback(stage, direction, progress) {
  stage.classList.toggle("drag-left", direction === "left");
  stage.classList.toggle("drag-right", direction === "right");
  stage.style.setProperty("--drag-progress", String(progress));
}

async function snapBack(stage, card) {
  if (!card) return;
  const from = card.style.transform || "translate3d(0, 0, 0) rotate(0deg)";
  const animation = card.animate([
    { transform: from },
    { transform: "translate3d(0, 0, 0) rotate(0deg)" },
  ], {
    duration: reducedMotion() ? 1 : 210,
    easing: "cubic-bezier(.2, .85, .3, 1)",
  });
  try { await animation.finished; } catch { /* DOM may be replaced. */ }
  clearFeedback(stage, card);
}

export function attachCardGestures(root, { isLocked, onCommit }) {
  const { card, stage } = elements(root);
  if (!card || !stage) return () => {};

  let drag = null;

  const reset = () => {
    drag = null;
    stage.classList.remove("is-dragging");
  };

  const onPointerDown = (event) => {
    if (isLocked() || !event.isPrimary || (event.pointerType === "mouse" && event.button !== 0)) return;
    if (event.target.closest(INTERACTIVE_SELECTOR)) return;
    drag = {
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
      startedAt: performance.now(),
      axis: null,
      x: 0,
      y: 0,
    };
  };

  const onPointerMove = (event) => {
    if (!drag || drag.pointerId !== event.pointerId || isLocked()) return;
    const dx = event.clientX - drag.startX;
    const dy = event.clientY - drag.startY;
    const distance = Math.hypot(dx, dy);

    if (!drag.axis && distance >= AXIS_LOCK_DISTANCE) {
      drag.axis = Math.abs(dx) > Math.abs(dy) * 1.12 ? "horizontal" : "vertical";
      if (drag.axis === "horizontal") stage.classList.add("is-dragging");
    }
    if (drag.axis !== "horizontal") return;

    if (event.cancelable) event.preventDefault();
    drag.x = dx;
    drag.y = clamp(dy * .14, -24, 24);
    const rotation = clamp(dx / 34, -11, 11);
    const progress = clamp(Math.abs(dx) / thresholdFor(card), 0, 1);
    card.style.transform = `translate3d(${dx}px, ${drag.y}px, 0) rotate(${rotation}deg)`;
    showFeedback(stage, dx < 0 ? "left" : "right", progress);
  };

  const finishPointer = (event, cancelled = false) => {
    if (!drag || drag.pointerId !== event.pointerId) return;
    const snapshot = drag;
    reset();

    if (snapshot.axis !== "horizontal" || cancelled) {
      snapBack(stage, card);
      return;
    }

    const elapsed = Math.max(performance.now() - snapshot.startedAt, 1);
    const velocity = Math.abs(snapshot.x) / elapsed;
    const committed = Math.abs(snapshot.x) >= thresholdFor(card)
      || (Math.abs(snapshot.x) >= 44 && velocity >= .62);

    if (!committed) {
      snapBack(stage, card);
      return;
    }

    const direction = snapshot.x < 0 ? "left" : "right";
    onCommit(direction === "left" ? "A" : "B", direction, { x: snapshot.x, y: snapshot.y });
  };

  const onPointerUp = (event) => finishPointer(event, false);
  const onPointerCancel = (event) => finishPointer(event, true);

  card.addEventListener("pointerdown", onPointerDown);
  window.addEventListener("pointermove", onPointerMove, { passive: false });
  window.addEventListener("pointerup", onPointerUp);
  window.addEventListener("pointercancel", onPointerCancel);

  return () => {
    card.removeEventListener("pointerdown", onPointerDown);
    window.removeEventListener("pointermove", onPointerMove);
    window.removeEventListener("pointerup", onPointerUp);
    window.removeEventListener("pointercancel", onPointerCancel);
  };
}

export async function animateCardOut(root, direction, origin = {}) {
  const { card, stage } = elements(root);
  if (!card || !stage) return;

  stage.classList.add("is-animating");
  const rect = card.getBoundingClientRect();
  const start = card.style.transform || "translate3d(0, 0, 0) rotate(0deg)";
  const viewportWidth = Math.max(window.innerWidth, rect.width);
  const viewportHeight = Math.max(window.innerHeight, rect.height);
  let end;
  let duration = 245;

  if (direction === "left") {
    end = `translate3d(${-Math.max(viewportWidth * .78, rect.width * 1.25)}px, ${origin.y || 8}px, 0) rotate(-15deg)`;
  } else if (direction === "right") {
    end = `translate3d(${Math.max(viewportWidth * .78, rect.width * 1.25)}px, ${origin.y || 8}px, 0) rotate(15deg)`;
  } else if (direction === "down") {
    end = `translate3d(0, ${Math.max(viewportHeight * .72, rect.height)}px, 0) rotate(2deg)`;
  } else if (direction === "soft-up") {
    end = "translate3d(0, -70px, 0) scale(.97)";
    duration = 180;
  } else {
    end = "translate3d(0, 70px, 0) scale(.97)";
    duration = 180;
  }

  const animation = card.animate([
    { transform: start, opacity: 1 },
    { transform: end, opacity: 0 },
  ], {
    duration: reducedMotion() ? 1 : duration,
    easing: "cubic-bezier(.35, .05, .2, 1)",
    fill: "forwards",
  });
  try { await animation.finished; } catch { /* DOM may be replaced. */ }
}

export async function animateCardIn(root, direction = "stack") {
  const { card } = elements(root);
  if (!card) return;
  let from = "translate3d(0, 12px, 0) scale(.985)";
  if (direction === "top") from = "translate3d(0, -70px, 0) rotate(-1.5deg)";
  if (direction === "bottom") from = "translate3d(0, 70px, 0) rotate(1.5deg)";
  const animation = card.animate([
    { transform: from, opacity: .25 },
    { transform: "translate3d(0, 0, 0) scale(1) rotate(0deg)", opacity: 1 },
  ], {
    duration: reducedMotion() ? 1 : 230,
    easing: "cubic-bezier(.18, .82, .25, 1)",
  });
  try { await animation.finished; } catch { /* DOM may be replaced. */ }
}
