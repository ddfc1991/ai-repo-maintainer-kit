# demo-tool

Clean, rename, and summarize project files from the command line.

## Who this is for

Use `demo-tool` when you maintain a folder full of logs, exports, or generated files and need a repeatable cleanup step.

## Quick start

```bash
pip install demo-tool
demo-tool scan ./exports --format markdown
```

## What it does

- Lists files by type and size
- Detects duplicate filenames
- Produces a Markdown summary

## What it does not do

- It does not delete files automatically.
- It does not upload files anywhere.

## Common errors

| Error | Fix |
|---|---|
| `permission denied` | Run against a folder you own. |
| `no files found` | Check the path passed to `scan`. |
