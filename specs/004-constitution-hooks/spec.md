# Feature Specification: The constitution enforced by hooks

**Feature Branch**: `claude/project-thread-mjdz9x`

**Created**: 2026-11-24

**Status**: Draft

**Input**: Description: "Enforce the constitution with Claude Code hooks instead of relying on instructions alone. Before
a message or question reaches the maintainer, and when Claude finishes a response, a check reads the constitution's
current text from the repository and judges the message against it, so that a conclusion that names no source and a
question to the maintainer about anything other than game content are stopped. The check must not restate the
constitution's rules; it reads the original."

## Why

Claude treats `CLAUDE.md` files as context, not enforced configuration; "to block an action regardless of what Claude
decides, use a PreToolUse hook instead" (code.claude.com/docs/en/memory.md, line 36). Hooks give "deterministic
control: certain actions always happen rather than relying on the LLM to choose to run them" (hooks-guide.md, line 9).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - A message to the maintainer that breaks the constitution does not reach him (Priority: P1)

When Claude, in a session that runs this repository's hooks, is about to send the maintainer a message or a question,
the message is first judged against the constitution as `.specify/memory/constitution.md` states it at that moment. A
message that breaks it is not sent: Claude gets the reason, naming the principle and the part that breaks it, and can
correct the message and try again.

**Why this priority**: the maintainer sees only what is sent to him. Stopping a message before it is sent is the only
point at which a breach can still be kept from him.

**Independent Test**: in a session that runs the repository's hooks, have Claude send the maintainer a question about a
repository setting through a messaging tool; the call is refused with a reason naming the principle. Have it send a
message that names its source; the message is sent.

**Acceptance Scenarios**:

1. **Given** a session in the repository, **When** Claude calls a tool that sends the maintainer a question about
   something other than game content, **Then** the call is denied and the reason names the principle it breaks.
2. **Given** the same session, **When** Claude sends a message whose conclusion names no source, **Then** the call is
   denied and the reason says which conclusion lacks a source.
3. **Given** the same session, **When** Claude sends a message that complies, **Then** it is sent unchanged.

---

### User Story 2 - A final answer that breaks the constitution is sent back for correction (Priority: P2)

When Claude finishes a response, its final text is judged against the constitution the same way. A response that breaks
it does not end the turn: the reason is fed back to Claude, which continues and corrects it.

**Why this priority**: outside a project thread, Claude's final text is the answer the reader sees, and no messaging
tool is called, so User Story 1 does not see it.

**Independent Test**: in a session that runs the repository's hooks, ask a question about a topic the Source Register
assigns, and tell Claude not to read anything; its first answer is sent back with a reason naming the principle.

**Acceptance Scenarios**:

1. **Given** a session in the repository, **When** Claude ends a response with a conclusion that names no source,
   **Then** the turn continues with the reason as Claude's next instruction.
2. **Given** the same session, **When** Claude ends a response that holds no answer, conclusion or question, or one that
   complies, **Then** the turn ends.

---

### Edge Cases

- The constitution changes: the check reads the file each time it runs, so it judges by the text current in the
  session's checkout, with no copy to update.
- A session that does not run the repository's hooks, such as a project's cloud thread or the project conversation, is
  not checked (claude-projects.md lines 57 and 348). This feature cannot change that; research.md R-2 records where
  the hooks run.
- The session transcript is written asynchronously and may lag (hooks.md, Common input fields, `transcript_path`): the
  Stop check judges the final text from `last_assistant_message`, and the messaging check from `tool_input`, and uses
  the transcript only to see what the session read before.
- A check that keeps refusing at Stop: Claude Code ends the turn after eight consecutive continuations (hooks.md, Stop
  input).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The hooks MUST be configured in `.claude/settings.json` at the repository root, the shared project
  settings file that is committed so everyone who clones the repository gets its hooks (hooks.md, Hook locations;
  settings.md, lines 28 and 69).
- **FR-002**: Before a tool call that sends the maintainer a message or a question, a check MUST judge that message
  against the constitution and deny the call when the message breaks it (hooks.md, PreToolUse).
- **FR-003**: When Claude finishes a response, a check MUST judge the response's final text against the constitution
  and, when it breaks it, keep the turn going with the reason (hooks.md, Stop).
- **FR-004**: Each check MUST read the constitution from `.specify/memory/constitution.md` when it runs and judge by
  that text. The hook configuration MUST NOT restate any rule of the constitution (this feature's input).
- **FR-005**: A denial or continuation MUST give a reason that names each principle broken, quotes the part that breaks
  it, and says what the constitution requires instead, so Claude can correct it.
- **FR-006**: A message that complies MUST pass unchanged.

### Key Entities

- **Constitution check**: one hook handler that reads the constitution and the session's record, judges one message,
  and returns allow, or deny with a reason.
- **Message to the maintainer**: the text of a messaging tool's input (PreToolUse) or of the final response (Stop).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a session that runs the repository's hooks, a question to the maintainer about a repository setting is
  never delivered.
- **SC-002**: In such a session, a response whose conclusion names no source does not end the turn; the reason names
  the principle.
- **SC-003**: A compliant message that names its source is delivered unchanged.
- **SC-004**: `.claude/settings.json` holds no sentence of the constitution.

## Assumptions

- The hooks run where Claude Code reads the repository's `.claude/settings.json`: a session started in the repository
  root (settings.md, line 94), including a project thread on the maintainer's computer started in his clone
  (claude-projects.md, line 250), after the folder's workspace is trusted (hooks.md, Workspace trust).
- The messaging tools are the ones a project thread has for writing to the maintainer, `post_message` and
  `request_decision` of the project's messaging server, and Claude Code's `AskUserQuestion` (hooks.md, PreToolUse
  input, AskUserQuestion). research.md R-5 records how they are matched.
