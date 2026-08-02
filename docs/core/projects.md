# Projects and workspace layout

A project is a folder on your Mac. ködade uses that folder as the working
directory for its terminal sessions and workspace tools; it does not import or
duplicate the folder.

## Add and switch projects

Select **+ add project** in the full projects sidebar and choose a folder. You
can also drop a folder into the app outside a live terminal. Adding the same
folder again selects its existing project instead of creating a duplicate.

Click a project name or tile to switch to it. Its chats, terminal, files, and
editor workspace become active. Shells belonging to other projects keep running
in the background.

The KödChat section is the full sidebar's project list. Use the chevron beside a
project to show or hide its chat threads, then select a thread to activate that
project and conversation. Live terminal workspaces appear below the project
list.

## Arrange the workspace

The desktop workspace has four panes from left to right:

1. projects
2. KödChat or terminal
3. editor
4. files

Drag a separator to resize adjacent panes. The projects, editor, and files panes
can collapse; the KödChat or terminal pane remains the central work area.
Double-click a separator to return it to its default position.

Pane sizes and collapsed states are stored per project. Switching projects can
therefore restore a different layout for each folder.

## Choose a sidebar mode

Use the control in the projects header, or press `Command-B`, to switch between:

- **Full sidebar** — project names and chat threads, terminal workspace cards,
  project removal, shortcuts, Settings, and About.
- **Compact sidebar** — a narrow rail of project tiles, plus add-project and
  Settings controls.

The selected mode applies across the app and persists locally. In compact mode,
click a project tile to switch projects; return to the full sidebar when you need
its chat threads and workspace cards.

## Set project colors

Every project gets a stable automatic color. To choose one:

1. Right-click the project row in the full sidebar or its tile in the compact
   sidebar.
2. Select a color from the picker.
3. Select **auto** to return to the assigned automatic color.

The color selection persists with the project and adapts to light and dark app
themes.

## Remove a project

In the full sidebar, hover over the project row and select **×**. This removes
the project from ködade, closes its terminal sessions, and drops its saved layout
and tab metadata.

Removing a project does not delete or modify the folder on disk.

## Understand local persistence

| Persists locally | Does not survive restart |
| --- | --- |
| Added projects and project colors | Live terminal processes |
| Last active project | In-memory terminal output |
| Per-project pane layout | Unsaved editor buffers |
| Theme and full/compact sidebar mode | Files attached to an unsent chat draft |
| Per-project open-tab metadata | Text that exists only in an unsaved buffer |
| KödChat thread metadata and transcripts | A running chat turn |
| Terminal-session identity and manual names | The command that was running in a terminal |

Open-tab metadata records what should be reopened; it does not store unsaved
file contents. On restart, files are read again from disk.

Next, start a [KödChat](kodchat.md) thread or manage [Terminal
sessions](terminal-sessions.md).
