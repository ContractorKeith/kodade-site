# Terminal sessions

Each terminal session is a real pseudo-terminal running your login shell. It
starts at the active project's root and uses the shell environment available to
ködade, including your login-shell `PATH`. If no shell is identified in the
environment, ködade falls back to `/bin/zsh`.

## Start a session

The first time you add or activate a project with no live sessions, ködade opens
one at the project root. Default names use your shell name and a number, such as
`zsh 1` and `zsh 2`.

To add another session:

1. Use the full projects sidebar.
2. Expand the project with its chevron.
3. Select **+ new session**.

You can also press `Command-T` while a project is active.

## Switch sessions

Click a session row in the full projects sidebar. Selecting a session under a
different project activates both that project and its terminal.

Only one terminal is visible at a time, but other sessions remain live. A steady
status dot marks a live session. When ködade can identify a foreground command,
the row can temporarily show that process name and pulse its status dot.

## Rename a session

Double-click a session row, enter a name, then press `Return` or click away to
commit it. Press `Escape` to cancel. An empty name keeps the current name.

A manual name takes priority over temporary foreground-process naming. Session
names are runtime-only and do not survive an app restart.

## Close a session

Hover over the session row and select **×**. Closing a session kills that
session's shell. If you close the active session, ködade selects the newest
remaining session for that project when one exists.

If a shell exits on its own, its dimmed row remains so you can inspect the
terminal output. Close that row when you are finished with it. After closing the
last session, select **+ new session** or press `Command-T` to start another.

Quitting ködade stops its live terminal sessions. On restart, a fresh shell may
open for the active project; the previous shell, its process, name, and terminal
output are not restored.

## Paste paths by dragging

Drag one or more files or folders from Finder onto the visible terminal. ködade
pastes their absolute paths at the prompt as shell-quoted arguments and leaves a
space after the last one. Review the command and press `Return` yourself.

The drop does not run a command. Filenames containing spaces or apostrophes are
quoted for the shell.

Drop location changes the result:

- Onto a live terminal: paste the paths into that session.
- Elsewhere in the app: add any dropped folders as projects.
- Onto an empty terminal with no live session: a dropped folder follows the
  add-project path.

To run agent tools in a session, continue with [Agent CLIs](agent-clis.md).
