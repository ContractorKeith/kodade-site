# Start here

ködade is a desktop Agentic Development Environment. It organizes project
folders, real terminal sessions, and the agent CLIs you already use in one workspace.
The terminal is not a simulated console: each session runs your login shell in
the selected project folder.

> **Pre-release status**
>
> There is no public download yet. Pre-release builds exist for Apple silicon
> Macs and Windows x64; both are unsigned, and the macOS build is not notarized.

## Begin with a project

1. Check the [requirements and release status](getting-started/requirements.md).
2. Follow [Your first project](getting-started/first-project.md) to add a folder
   and reach a working prompt.
3. Run an installed agent CLI yourself, just as you would in another terminal.

Adding a project opens an initial terminal at that folder's root. Your normal
login-shell startup, prompt, and `PATH` apply. ködade does not proxy the shell or
sign in to agent providers for you.

## Learn the core workflow

- [Projects and workspace layout](core/projects.md) explains project switching,
  pane layouts, sidebar modes, colors, and local persistence.
- [Terminal sessions](core/terminal-sessions.md) covers creating, naming,
  switching, closing, and dropping paths into terminals.
- [Agent CLIs](core/agent-clis.md) explains installation detection, version
  reporting, authentication boundaries, and manual launch.

## Beyond the core workspace

- [KödHarness](features/kodharness.md) shows what an agent CLI will read before
  it runs.
- [KödWhisper](features/kodwhisper.md) adds local voice input for agent prompts.
- [Köd Workspace and KödMem](features/kodmem.md) keep activity and durable
  project memory visible and local.
- [KödMCP](features/kodmcp.md) gives agent tools controlled access to KödMem.
- [KödPR](features/kodpr.md) provides an in-app surface for reading changes
  before they ship.
- [KödSSH](features/kodssh.md) connects the workspace to agent CLIs on a remote
  machine.
- [KödWeb](features/kodweb.md) connects a browser to a box running
  `kodade-serve`.
- [KödLocal](features/kodlocal.md) runs a local model through the bundled
  daemon.
- [Free and Pro](features/free-and-pro.md) explains the available feature tiers.

## What survives a restart

ködade stores your projects and selected UI metadata locally. Project colors,
pane layouts, theme, sidebar mode, and open-tab metadata can return after a
restart. Live terminal sessions, running processes, session names, and unsaved
editor buffers do not.

That boundary matters: save editor changes and finish or stop terminal work
before quitting the app.
