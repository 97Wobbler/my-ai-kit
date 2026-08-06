const model = {
  session: null,
  ui: {
    busy: false,
    drawerOpen: false,
    error: "",
  },
};

const listeners = new Set();

function emit() {
  listeners.forEach((listener) => listener(model));
}

export function getModel() {
  return model;
}

export function setSession(session) {
  return updateModel({ session });
}

export function setUI(patch) {
  return updateModel({ ui: patch });
}

export function updateModel({ session, ui } = {}) {
  if (session) model.session = model.session ? { ...model.session, ...session } : session;
  if (ui) model.ui = { ...model.ui, ...ui };
  emit();
  return model;
}

export function subscribe(listener) {
  listeners.add(listener);
  listener(model);
  return () => listeners.delete(listener);
}
