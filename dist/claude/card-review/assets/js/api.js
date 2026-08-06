async function request(path, options = {}) {
  const response = await fetch(path, {
    cache: "no-store",
    ...options,
    headers: {
      ...(options.body ? { "Content-Type": "application/json" } : {}),
      ...(options.headers || {}),
    },
  });
  const body = await response.json();
  if (!response.ok) {
    throw new Error(body.error || "요청을 처리하지 못했습니다.");
  }
  return body;
}

export function fetchSession() {
  return request("/api/state");
}

export function postAction(payload) {
  return request("/api/action", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export function fetchDevVersion() {
  return request("/api/dev-version");
}
