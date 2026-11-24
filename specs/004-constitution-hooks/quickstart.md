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

## Maintainer's steps

These are done on the maintainer's computer and in the project's settings, where only he can act.

1. After this feature merges, update the clone at `D:\Steam\steamapps\common\RimWorld\Mods\Imperium` from `main`
   with his own git (`git pull`).
2. Have Claude Code v2.1.280 or later (claude-projects.md line 256). In the Claude desktop app, **Settings > Code** (or
   **Settings > Claude Code**), turn on **Use this computer from your phone and claude.ai** and add that clone's folder
   to the list under it (claude-projects.md line 258). The folder must be the repository root, since the settings file
   is read from the session's primary working directory (settings.md line 94).
3. Open Claude Code once in that folder and accept the workspace trust dialog, since an interactive session holds back
   hooks until the folder is trusted (hooks.md, Workspace trust).
4. Keep **Require trusted devices** off, or a project cannot run a thread on his computer (claude-projects.md line
   265). Optionally turn on **Keep this computer awake for Remote Control** (line 278).
5. In **Project settings > Memory > Project instructions**, say that work on the repository runs as a thread on his
   computer in that folder, with **Worktree** on so threads do not overwrite each other (claude-projects.md line 269).
   The docs give no setting that does this by default (research R-2), and the current instructions send repository
   work to cloud threads.

## Final check, on the maintainer's computer

5. **The hooks run in a thread on his computer.** Start a project thread on his computer in the clone. Run `/hooks`
   in it (hooks.md, The `/hooks` menu): both hooks are listed. Have the thread send him a question about a repository
   setting: it is denied with a reason, and nothing reaches him. If the messaging tool there has another name, the
   matcher is changed (contracts/hooks-settings.md, May change).
