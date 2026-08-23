# Card Review input schema

Use one UTF-8 JSON object as the GUI input. Keep every `id` stable and unique.

```json
{
  "version": "1",
  "option": {
    "title": "Review title",
    "groupAName": "Approve",
    "groupBName": "Reject",
    "fields": {
      "title": { "label": "Title", "render": "h2" },
      "body": { "label": "Body", "render": "markdown" },
      "path": { "label": "Path", "render": "text" }
    }
  },
  "items": [
    {
      "id": "item-001",
      "title": "A stable item title",
      "body": "## Details\n\n- One point\n- Another point",
      "path": "src/example.ts"
    }
  ]
}
```

Allowed renderers are `h1`, `h2`, `h3`, `markdown`, `ol`, `ul`, `text`,
`link`, and `image`. An item may also place displayed fields under an optional nested
`fields` object; top-level item properties take precedence.

An `image` value is one local image path. Relative paths resolve from the
directory containing the input JSON; absolute paths are also accepted. The
server validates that the file exists and has an image MIME type, exposes only
files explicitly referenced by `image` fields, and sends an opaque loopback
URL to the browser instead of the local path. Click the displayed image to
open the full-size version. Remote URLs and multi-image galleries are not
supported in version 1 of this renderer.

Items do not need to contain every key declared in `option.fields`. Omit a
field when it is not relevant to that item's decision; missing and empty
values are not rendered.

## Review packet guidance

Use the schema as a presentation packet, not as a mirror of the source data.
Every item should answer the same independent A/B question. If different item
types need different decision semantics, earlier answers control later cards,
or more than A/B/null is structurally required, use a task-specific review
harness instead.

For a blind review, keep only anonymized reviewer-visible information in this
file. Store real candidate IDs, automatic scores or selections, experiment
conditions, and shuffle mappings separately, then join them with the result
only after review completion.

The GUI writes one JSON object per line to the result JSONL. It preserves input
order and includes every item, including unresolved items:

```jsonl
{"id":"item-001","result":"A","memo":"Reason"}
{"id":"item-002","result":null}
```

`result` is `A`, `B`, or `null`. `memo` is omitted when empty. The adjacent
`.state.json` file is an implementation detail used for resume and history; do
not treat it as the review result.
