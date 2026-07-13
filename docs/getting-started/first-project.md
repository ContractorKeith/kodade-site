# Your first project

Use any folder you want to work in. Adding it to ködade does not copy or move its
contents.

## Add the folder

1. Open a current ködade test build.
2. Select **+ add project** at the bottom of the full projects sidebar.
3. Choose your project folder in the macOS folder picker.

ködade adds the folder as a project, selects it, and opens an initial terminal
session at the folder's root. The project name comes from the folder name.

You can confirm the terminal's working directory with:

```sh
pwd
```

The output should be the folder you selected.

## Run an agent CLI

At the prompt, enter the command for an agent CLI you installed and authenticated
outside ködade. For example:

```sh
codex
```

Replace `codex` with the CLI you use. Launch it manually; the **settings** panel's
agent list reports installation and version information but does not start the
CLI or verify its login.

> **Use the prompt you already configured**
>
> Each terminal is a real login shell. Your normal login-shell startup and
> `PATH` apply, and the session starts in the active project's folder.

## Open another terminal

1. Expand the project with the chevron beside its name if its sessions are
   hidden.
2. Select **+ new session**.
3. Click a session row to switch between terminals.

Each session has its own live shell. Switching projects or sessions does not stop
the other shells; they continue running until you close them or quit ködade.

Continue with [Terminal sessions](../core/terminal-sessions.md) for naming,
closing, and path drops, or [Projects and workspace
layout](../core/projects.md) to arrange the workspace.

## Before you quit

Projects and selected workspace metadata persist locally. Live terminal
sessions, running commands, manual session names, and unsaved editor buffers do
not survive a restart. Save editor changes and stop any work you need to finish
before quitting.
