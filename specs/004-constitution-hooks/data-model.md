# Data Model: The constitution enforced by hooks

## Hook input (read)

The JSON Claude Code passes to each check as `$ARGUMENTS` (hooks.md, Common input fields; PreToolUse input; Stop
input).

| Field | Used for |
|-------|----------|
| `cwd` | Finding the repository root, where `.specify/memory/constitution.md` is |
| `transcript_path` | Seeing which sources the session read and what was asked; may lag the latest turn |
| `tool_name`, `tool_input` | PreToolUse: the message or question about to be sent |
| `last_assistant_message` | Stop: the final response |
| `stop_hook_active` | Stop: whether the turn is already continuing because of a Stop hook |

## Check answer (written)

The agent hook's response schema (hooks.md, Agent hook configuration).

| Field | Meaning |
|-------|---------|
| `ok` | `true`: the message passes. `false`: PreToolUse denies the call; Stop keeps the turn going |
| `reason` | Required when `ok` is `false`: each principle broken, the part that breaks it, and what the constitution requires instead (spec FR-005) |
