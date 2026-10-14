# Packaged Research Viewer

Resolve the Inquiry package root using `research-schema.json` and
`scripts/research_store.py`. The packaged viewer is already built and requires
Python 3.10+ and a modern browser, not a Node development server.

```sh
python3 <package-root>/scripts/research_viewer.py
```

Open its printed `http://127.0.0.1:<port>/` URL using an available browser, or
add `--open` to use the system browser. `--port` can choose a port; by default it
uses an available one. Stop the foreground process with Ctrl-C or terminate the
specific process/session you started. Do not leave unnecessary background servers.

The server exposes only index.html, app.js, styles.css, build metadata and a
synthetic demo. It binds loopback and never serves the workspace, accepts writes,
or uploads research JSON. Select the actual file with **연구 파일 열기**; its
contents are read and validated in the browser. Reload a file to see edits;
automatic refresh and concurrent editing are not included.

Default view shows adopted paths (draft paths if none adopted) and relevant goals.
Unresolved required premises and ALL members remain visible even outside those
paths. An ANY group expands its candidates only when none is already supported
or complete; this display does not turn alternatives into mandatory prerequisites.
Goal/path filters, **전체 기록 펼치기**, fit and zoom controls explore the same
record. Folded alternatives remain listed, including exhausted paths. In the
demo, B's inspector shows A's failure, A-prime support, untested A-double-prime
and contemporaneous decisions even when those nodes are folded in the main view.

The bundled Cytoscape.js canvas supports dragging nodes, panning the background,
wheel/touch zoom, and fit. Choose relationship-based automatic placement or
research-order placement with the layout selector. Use the node selector for
keyboard navigation and full labels. Selecting a node highlights its immediate
relationships and opens the same inspector; the background clears selection.
These interactions only change the view, not the research JSON or its revision.

Node type, operational state, and hypothesis evidence judgment are distinguishable.
Edge text expresses relation when selected; solid supported lines and dashed
unknown/challenged/mixed lines use assessment colors. Selection makes adjacent
relationships thicker. ALL/ANY prerequisites
are displayed in node details. No layout ordering claims to prove causation or
authorize execution. The viewer never updates downstream scientific states.

Artifacts and document references are rendered as text with versions. Arbitrary
HTML in files is not executed, and private paths are not exposed through the
server. Do not put sealed evaluation content into the record shown to mutators.

For maintainers, TypeScript development source remains private under `viewer/`.
The pinned compiler concatenates namespace-based source and the pinned
Cytoscape.js browser distribution into standalone JS, including its MIT notice;
HTML and CSS remain separate. No CDN or runtime library install is needed.
Run the repository's viewer build before the plugin dist build. Freshness and
payload hashes prevent stale or source-containing bundles from packaging.
This repository-defined build/serve convention is locally verified behavior,
not a claimed host-supplied browser or runtime cache API.
