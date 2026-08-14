# Start here

> your agents. one window

ködade is a desktop Agentic Development Environment. It brings agent chats,
project folders, real terminal sessions, files, and the agent CLIs you already
use into one workspace.

ködade is [open source under Apache License
2.0](trust/open-source.md). The macOS app is available now from
[GitHub Releases](https://github.com/Kodade/kodade/releases). Windows has no
current release package, and Linux is planned.

## Begin with a project

1. [Download the macOS DMG](getting-started/requirements.md#install-on-macos).
2. Follow [Your first project](getting-started/first-project.md) to add a folder
   and reach a working agent or terminal prompt.
3. Start a KödChat thread with Claude Code or Codex, or run any supported agent
   CLI in a terminal.

Adding a project opens an initial terminal at that folder's root. Your normal
login-shell startup, prompt, and `PATH` apply. ködade does not proxy the shell or
sign in to agent providers for you.

## Learn the core workflow

- [Projects and workspace layout](core/projects.md) explains project switching,
  pane layouts, sidebar modes, colors, and local persistence.
- [KödChat](core/kodchat.md) covers provider, model, access, attachments, and
  local transcript storage.
- [Terminal sessions](core/terminal-sessions.md) covers creating, naming,
  switching, closing, and dropping paths into terminals.
- [Agent CLIs](core/agent-clis.md) explains installation detection, version
  reporting, authentication boundaries, chat support, and manual launch.

## Beyond the core workspace

- [KödWork](features/kodwork.md) runs durable background tasks and holds their
  progress, permission requests, and file output for review.
- [KödHarness](features/kodharness.md) shows what an agent CLI will read before
  it runs.
- [Köd Workspace and KödMem](features/kodmem.md) keep activity and durable
  project memory visible and local.
- [KödMCP](features/kodmcp.md) gives agent tools controlled access to KödMem.

## What survives a restart

ködade stores your projects, KödChat transcripts, and selected UI metadata
locally. Project colors, pane layouts, theme, sidebar mode, chat threads, and
open-tab metadata can return after a restart. Live terminal processes and
unsaved editor buffers do not.

That boundary matters: save editor changes and finish or stop terminal work
before quitting the app.
