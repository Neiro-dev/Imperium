# Research: The constitution enforced by hooks

Every finding names its source. "Docs" means the Claude Code documentation at code.claude.com/docs/en/, the source
the Source Register gives for how the AI works; pages were read on 2026-11-24, line numbers are those of the `.md`
form of each page on that date.

## R-1 Where the hooks are configured

- **Decision**: `.claude/settings.json` at the repository root.
- **Rationale**: hooks.md, Hook locations: `.claude/settings.json` has scope "Single project" and is shareable, "can be
  committed to the repo". settings.md line 69: "Commit `.claude/settings.json` so everyone who clones the repository
  gets the same permissions, hooks, and plugin settings." Settings.md line 94: Claude Code reads it "from the
  session's primary working directory, so to use a file committed at the repository root, start Claude Code there."
- **Repository files**: the Source Register gives GitHub Docs for repository files and Spec Kit for the development
  workflow. Neither restricts a `.claude/` directory: Spec Kit itself installs this repository's `.claude/skills/`
  (`.specify/integrations/claude.manifest.json`), and its manifest does not list `.claude/settings.json`, so the file
  does not collide with a file Spec Kit manages. The repository's layout contract puts a file that serves the
  repository at the root (`specs/003-mantle-mod/contracts/repository-layout.md`, Stable, fourth entry).
- **Principle V**: the file is supported by a source (the docs above), so it is not a file "no source supports".
- **Alternatives considered**: `~/.claude/settings.json` on the maintainer's computer (hooks.md, Hook locations: "local
  to your machine", not shareable, and not in the repository); `.claude/settings.local.json` (gitignored when Claude
  Code saves to it, settings.md line 75).

## R-2 Where the hooks run, and whether project threads can run there by default

- **Cloud threads of a project**: not run. claude-projects.md line 348: "Hooks in `.claude/settings.json` | Not run. To
  use your hooks, run the thread on your own computer"; also line 57 and settings.md line 328. Confirmed in this
  thread's container: a `claude -p` child that inherits the thread's environment ran no hook from a test
  `.claude/settings.json`; the same child with a clean environment ran it.
- **The project conversation**: the docs give no way to attach hooks to it. claude-projects.md describes it as "one
  long-running session where Claude acts as coordinator" (line 53) and lists hooks only for threads on the
  maintainer's computer (line 250).
- **Threads on the maintainer's computer**: run. claude-projects.md line 250: such a thread "works with the files,
  tools, MCP servers, and Claude Code settings on that machine, including its hooks and permission rules". It reads
  the repository's `.claude/settings.json` only when its folder is the repository root (settings.md line 94), and an
  interactive session runs hooks only after the folder's workspace is trusted (hooks.md, Workspace trust).
- **Default to his computer**: the docs give no setting that makes a project's threads run on the maintainer's
  computer by default. A thread runs there when it is asked for in the project conversation, with **Work locally** or
  by saying so in the message, and "the project's other threads keep running in the cloud" (claude-projects.md lines
  248 and 263). Each such thread is allowed on a card (claude-projects.md line 269, "Allow once"). So what threads run
  locally depends on what the project conversation is told, which is the project's instructions; that text is the
  maintainer's to set (claude-projects.md, Give a project standing context).
- **Other ways considered and rejected**:
  - Server-managed settings: hooks from them do run in Anthropic-hosted cloud sessions, project threads included
    (cloud-environments.md line 481), but they need a Claude for Teams or Enterprise plan and the Owner role
    (server-managed-settings.md, Requirements). The Claude Code started in this thread logged that the account is
    "not a Team or Enterprise organization", so the docs offer no form here (Principle V).
  - Hooks in a skill's frontmatter: the docs say cloud threads load repository skills (claude-projects.md line 345)
    but do not say that a skill's frontmatter hooks run in a project's cloud thread, and such hooks run only after the
    skill is invoked (hooks.md, Hooks in skills and agents), which is Claude's choice, not enforcement. No source
    supports it (Principle V).
  - A cloud environment's setup script writing `~/.claude/settings.json`: cloud-environments.md lines 479-482 list
    the hooks an Anthropic-hosted session runs (server-managed settings, and the repository outside project threads)
    and do not list user settings. No source supports it (Principle V).

## R-3 Which hook events

- **Decision**: `PreToolUse` on the tools that send the maintainer a message or a question, and `Stop`.
- **Rationale**: memory.md line 36: "To block an action regardless of what Claude decides, use a PreToolUse hook".
  PreToolUse "runs after Claude creates tool parameters and before processing the tool call" (hooks.md, PreToolUse),
  so a message can be judged before it is sent. In a project thread, Claude's own text is not delivered; only its
  messaging tool calls reach the maintainer. Outside a project, the final text is the answer, which `Stop` sees in
  `last_assistant_message` (hooks.md, Stop input: "contains the text content of Claude's final response").
- **Alternatives considered**: `UserPromptSubmit` judges the maintainer's prompt, not Claude's answer; `PostToolUse`
  "can't undo actions since the tool has already executed" (hooks-guide.md, Limitations).

## R-4 Which hook type

- **Decision**: `agent`.
- **Rationale**: hooks-guide.md line 11: "For decisions that require judgment rather than deterministic rules, you can
  also use prompt-based hooks or agent-based hooks". hooks-guide.md, Agent-based hooks: "Use prompt hooks when the
  hook input data alone is enough to make a decision. Use agent hooks when you need to verify something against the
  actual state of the codebase." The judgment needs the constitution, which is a file in the repository and not in
  the hook input, and needs to read the constitution itself rather than a copy (spec FR-004); a prompt hook has no
  tool to read it, and putting its text in the prompt would restate it.
- **The docs' warning**: hooks.md and hooks-guide.md mark agent hooks as experimental: "For production workflows,
  prefer command hooks." A command hook runs a shell command and can only apply "deterministic rules" (hooks-guide.md
  line 11), which cannot judge whether a conclusion names its source. The docs' own rule for this case (judgment
  against the codebase) is the agent hook; the warning is recorded here so that a change to agent hooks in a later
  Claude Code release is looked for first when the check stops working.
- **Block behavior**: "On `ok: false`, Claude Code handles an agent hook the way it handles a prompt hook with
  `continueOnBlock: true`" (hooks.md, How agent hooks work): on PreToolUse the call is denied and the reason returned
  to Claude as the tool error, so it can correct the message; on Stop the reason becomes Claude's next instruction.

## R-5 Which tools the PreToolUse matcher names

- **Decision**: the matcher `mcp__.*__(post_message|request_decision)|^AskUserQuestion$`.
- **Rationale**: a project thread writes to the maintainer through the project messaging server's `post_message` and
  puts a choice to him through its `request_decision` (the tool list of this thread). MCP tools are matched as
  `mcp__<server>__<tool>` (hooks.md, Match MCP tools), and a matcher with characters other than letters, digits, `_`,
  `-`, spaces, `,` and `|` is an unanchored JavaScript regular expression (hooks.md, Matcher patterns). The server
  part is left as `.*` because the docs do not name the server a thread on the maintainer's computer gets.
  `AskUserQuestion` is Claude Code's own tool for asking the user (hooks.md, PreToolUse input) and is anchored so
  that no other tool whose name contains it matches.
- **Verified**: with a stand-in MCP server named `relay`, the matcher fired on `mcp__relay__post_message`
  (quickstart.md, Check 1). The name `hearthbot` is reserved and cannot be used for a stand-in server.

## R-6 Timeout and model

- **Decision**: the defaults: no `timeout` and no `model` field.
- **Rationale**: Principle V: a source that names a default is followed. hooks.md, Common fields: `timeout` defaults to
  60 seconds for `agent`; Prompt and agent hook fields: `model` "Defaults to the model Claude Code uses for background
  functionality". The checks in quickstart.md each finished in 7 to 12 seconds with these defaults.

## R-7 The check's instructions

- **Decision**: the prompt tells the check where the constitution is, what message to judge, where the session's
  record is, and the form of its answer; it states no rule of the constitution (spec FR-004).
- **Rationale**: `$ARGUMENTS` is replaced with the hook input JSON (hooks.md, Prompt and agent hook fields), which
  carries `cwd`, `transcript_path`, `tool_input` for PreToolUse and `last_assistant_message` for Stop (hooks.md,
  Common input fields, Stop input). The transcript "may lag the in-memory conversation" (Common input fields), so the
  message itself is taken from `tool_input` or `last_assistant_message`, and the transcript only shows what the
  session read before. The answer form `{"ok": true}` or `{"ok": false, "reason": ...}` is the agent hook's response
  schema (hooks.md, Agent hook configuration).
