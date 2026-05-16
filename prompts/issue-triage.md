# Issue Triage Prompt

Classify GitHub issues quickly and consistently.

Input:
- Repository purpose:
- Issue title:
- Issue body:
- Recent related issues or PRs:

Return:

```yaml
category: bug | feature | docs | question | maintenance | security
priority: low | medium | high | urgent
status: needs-info | ready | duplicate | invalid | blocked
labels:
  - label-one
  - label-two
maintainer_reply: |
  Short reply that explains the next step.
next_action: close | ask-question | add-to-backlog | create-pr | investigate
risk: low | medium | high
```

Rules:
- Ask for reproduction steps for bugs without enough detail.
- Never promise implementation timelines.
- Security issues get private disclosure guidance.
- Duplicates must include the suspected duplicate link when available.
