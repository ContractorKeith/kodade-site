# Start here

ködade is a desktop Agentic Development Environment. It organizes project
folders, real terminal sessions, and the agent CLIs you already use in one workspace.
The terminal is not a simulated console: each session runs your login shell in
the selected project folder.

> **Pre-release status**
>
> There is no public download yet. The current release path is for Apple silicon
> Macs running macOS 13 or newer, and the build is not yet signed or notarized.
> Windows support is in development; it is not currently available.

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

## What survives a restart

ködade stores your projects and selected UI metadata locally. Project colors,
pane layouts, theme, sidebar mode, and open-tab metadata can return after a
restart. Live terminal sessions, running processes, session names, and unsaved
editor buffers do not.

That boundary matters: save editor changes and finish or stop terminal work
before quitting the app.
