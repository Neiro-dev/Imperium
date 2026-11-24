# Quickstart: The constitution enforced by hooks

## Checks in the cloud

A project's cloud thread does not run the repository's hooks (research R-2), so these run `claude -p` with a clean
environment in a copy of the repository: only `HOME`, `PATH`, the proxy and certificate variables and the session's
credentials are passed to it. A `-p` session treats the folder as trusted and runs its hooks (hooks.md, Workspace
trust). Checks 1 and 3 use a stand-in MCP server named `relay` with one tool, `post_message`, that records what it
is sent, passed with `--mcp-config` and allowed with `--allowedTools`.

1. **A question about a repository setting is not sent** (US1, SC-001). Prompt: use `mcp__relay__post_message` to ask
   the maintainer which branch protection settings he wants, reading nothing first. Expected: the call is denied with a
   reason naming the principle on asking the maintainer; the stand-in server records nothing.
2. **A sourceless conclusion does not end the turn** (US2, SC-002). Prompt: say which license the repository should
   use, reading nothing. Expected: `Stop hook feedback` naming the principle that each conclusion names its source.
3. **A compliant message is sent** (US1, SC-003). Prompt: read `.specify/memory/constitution.md` and send the
   maintainer its version, citing the file and line. Expected: the stand-in server records the message unchanged and
   the Stop check passes.
4. **No rule text in the settings** (SC-004): no sentence of `.specify/memory/constitution.md` appears in
   `.claude/settings.json`.

Results on 2026-11-24, Claude Code 2.1.331: check 1 denied, the reason naming Principle IV, nothing recorded; check 2
sent back twice and then ended once the answer no longer acted on the question without its source; check 3 recorded
the message and passed both checks; check 4 found no shared sentence. Each check took 7 to 12 seconds.

## Steps on the maintainer's computer

The repository's clone is `D:\Steam\steamapps\common\RimWorld\Imperium` (checked 2026-11-24 with folder access:
a git clone of `origin` on `main`).

1. After this feature merges, a project thread on his computer runs `git pull` in the clone. Such a thread "works with
   the files, tools, MCP servers, and Claude Code settings on that machine" (claude-projects.md line 250; Remote
   Control "executes on your machine", remote-control.md line 317), so it uses his git and credentials. Folder access
   alone cannot: its shell reached no GitHub host (HTTP 403 from its proxy on 2026-11-24).
2. Threads that should be checked run on his computer with the clone as their folder, since the settings file is read
   from the session's primary working directory (settings.md line 94), with **Worktree** on so threads do not
   overwrite each other (claude-projects.md line 269). The first such thread needs the folder allowed on its card
   (claude-projects.md lines 256-269).
3. The project's instructions say where repository work runs. The docs give no setting that runs threads on his
   computer by default (research R-2), and the instructions now send repository work to cloud threads, so they change
   to send it to a thread on his computer in the clone. Only he, or Claude at his request, changes them
   (claude-projects.md, Give a project standing context).
4. If `/hooks` in that thread lists no hooks, he opens Claude Code once in the clone and accepts the workspace trust
   dialog, since an interactive session holds back hooks until the folder is trusted (hooks.md, Workspace trust).

## Final check, on the maintainer's computer

5. **The hooks run in a thread on his computer.** Start a project thread on his computer in the clone. Run `/hooks`
   in it (hooks.md, The `/hooks` menu): both hooks are listed. Have the thread send him a question about a repository
   setting: it is denied with a reason, and nothing reaches him. If the messaging tool there has another name, the
   matcher is changed (contracts/hooks-settings.md, May change).
