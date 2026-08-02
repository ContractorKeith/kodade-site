# Your first project

Use any folder you want to work in. Adding it to ködade does not copy or move its
contents.

## Add the folder

1. Open ködade from **Applications**.
2. Select **+ add project** at the bottom of the full projects sidebar.
3. Choose your project folder in the macOS folder picker.

ködade adds the folder as a project, selects it, and opens an initial terminal
session at the folder's root. The project name comes from the folder name.

You can confirm the terminal's working directory with:

```sh
pwd
```

The output should be the folder you selected.

## Start an agent chat

Claude Code and Codex can run in KödChat after you install and authenticate
their CLIs:

1. Expand the project under **KödChat** in the sidebar.
2. Select **+** beside the project.
3. Choose the provider, model, and access level.
4. Enter a message and press **Enter**.

See [KödChat](../core/kodchat.md) for access levels, attachments, transcript
storage, and the terminal split.

## Run an agent CLI in the terminal

At the prompt, enter the command for an agent CLI you installed and authenticated
outside ködade. For example:

```sh
codex
```

Replace `codex` with the CLI you use. You can also start an installed CLI in a
new terminal from **settings > providers**. Detection and launch do not verify
that the CLI is signed in.

> **Use the prompt you already configured**
>
> Each terminal is a real login shell. Your normal login-shell startup and
> `PATH` apply, and the session starts in the active project's folder.

## Open another terminal

Press **Command-T** while the project is active. Select a workspace card in the
full sidebar to switch between live terminals.

Each session has its own live shell. Switching projects or sessions does not stop
the other shells; they continue running until you close them or quit ködade.

Continue with [Terminal sessions](../core/terminal-sessions.md) for naming,
closing, and path drops, or [Projects and workspace
layout](../core/projects.md) to arrange the workspace.

## Before you quit

Projects, chat transcripts, terminal-session names, and selected workspace
metadata persist locally. Running commands, terminal output, and unsaved editor
buffers do not survive a restart. Save editor changes and stop any work you
need to finish before quitting.
