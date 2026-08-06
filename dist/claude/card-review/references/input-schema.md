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

Allowed renderers are `h1`, `h2`, `h3`, `markdown`, `ol`, `ul`, `text`, and
`link`. An item may also place displayed fields under an optional nested
`fields` object; top-level item properties take precedence.

The GUI writes one JSON object per line to the result JSONL. It preserves input
order and includes every item, including unresolved items:

```jsonl
{"id":"item-001","result":"A","memo":"Reason"}
{"id":"item-002","result":null}
```

`result` is `A`, `B`, or `null`. `memo` is omitted when empty. The adjacent
`.state.json` file is an implementation detail used for resume and history; do
not treat it as the review result.
