# Contract: `.claude/settings.json`

## Stable

- The file is the repository's shared Claude Code project settings at the repository root (research R-1).
- `hooks.PreToolUse` holds one matcher group whose matcher names the tools that send the maintainer a message or a
  question (research R-5), with one `agent` handler.
- `hooks.Stop` holds one matcher group with no matcher and one `agent` handler.
- Each handler's `prompt` holds `$ARGUMENTS`, points the check at `.specify/memory/constitution.md` at the repository
  root and at the session transcript, names the message it judges (`tool_input` or `last_assistant_message`), and asks
  for `{"ok": true}` or `{"ok": false, "reason": ...}` as data-model.md describes.
- No handler states a rule of the constitution; each judges by the file's text when it runs (spec FR-004).
- No `timeout` or `model` field: the documented defaults apply (research R-6).

## May change

- The matcher, if the messaging tools of a thread on the maintainer's computer turn out to have other names (research
  R-5; quickstart.md, check 5).
- The hook type, if a later Claude Code release changes agent hooks, which the docs mark as experimental (research
  R-4).
