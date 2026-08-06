function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function renderMarkdown(value, forcedList = null) {
  const lines = String(value ?? "").replace(/\r/g, "").split("\n");
  const root = document.createElement("div");
  let paragraph = [];
  let list = null;

  const flushParagraph = () => {
    if (!paragraph.length) return;
    const element = document.createElement("p");
    element.innerHTML = inlineMarkdown(paragraph.join(" "));
    root.appendChild(element);
    paragraph = [];
  };

  const closeList = () => {
    if (!list) return;
    root.appendChild(list);
    list = null;
  };

  for (const line of lines) {
    const heading = line.match(/^(#{1,3})\s+(.+)$/);
    const unordered = line.match(/^\s*[-*]\s+(.+)$/);
    const ordered = line.match(/^\s*\d+[.)]\s+(.+)$/);

    if (heading) {
      flushParagraph();
      closeList();
      const element = document.createElement(`h${heading[1].length}`);
      element.innerHTML = inlineMarkdown(heading[2]);
      root.appendChild(element);
      continue;
    }

    if (unordered || ordered || forcedList) {
      const isOrdered = forcedList === "ol" || Boolean(ordered);
      const tagName = isOrdered ? "ol" : "ul";
      if (!list || list.tagName.toLowerCase() !== tagName) {
        flushParagraph();
        closeList();
        list = document.createElement(tagName);
      }
      const text = unordered ? unordered[1] : ordered ? ordered[1] : line;
      if (text.trim()) {
        const item = document.createElement("li");
        item.innerHTML = inlineMarkdown(text);
        list.appendChild(item);
      }
      continue;
    }

    if (!line.trim()) {
      flushParagraph();
      closeList();
      continue;
    }
    paragraph.push(line.trim());
  }

  flushParagraph();
  closeList();
  return root;
}

export function renderValue(value, renderer) {
  const wrapper = document.createElement("div");
  wrapper.className = "field-value";

  if (renderer === "text") {
    wrapper.textContent = value == null ? "" : String(value);
    return wrapper;
  }

  if (renderer === "link") {
    const link = document.createElement("a");
    const href = String(value ?? "");
    link.href = /^(https?:)\/\//i.test(href) ? href : "#";
    link.target = "_blank";
    link.rel = "noreferrer";
    link.textContent = href;
    wrapper.appendChild(link);
    return wrapper;
  }

  if (["h1", "h2", "h3"].includes(renderer)) {
    const heading = document.createElement(renderer);
    heading.textContent = value == null ? "" : String(value);
    wrapper.appendChild(heading);
    return wrapper;
  }

  const forcedList = ["ol", "ul"].includes(renderer) ? renderer : null;
  wrapper.appendChild(renderMarkdown(value, forcedList));
  return wrapper;
}
