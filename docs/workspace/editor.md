# Edit and save files

Select a text file in the **files** pane to open it in an editor tab. ködade
uses CodeMirror for editing, adds syntax highlighting for common source formats,
and falls back to plain text when it has no matching language grammar.

## Open and switch tabs

Each selected file gets one tab. Select a tab to return to it, use
**Ctrl-Tab** and **Ctrl-Shift-Tab** when a terminal does not have focus, or
select the tab's **×** to close it. A middle-click also closes a tab.

Two files with the same name receive a parent-folder suffix in their tab labels.
Tabs scroll horizontally when they no longer fit in the pane.

Open-tab metadata is saved locally per project. Editor view state and unsaved
buffers are not durable project data.

## Save an edit

1. Make a change in the editor.
2. Look for the amber unsaved-changes dot on the tab and next to the file in the
   tree.
3. Press **Command-S** to save.

The status line shows **saving…** while a write is in progress. A failed save
shows **Could not save:** followed by the error; the editor keeps the buffer so
you can correct the problem and try again.

!!! warning
    Save before switching projects or quitting. Closing a dirty tab keeps its
    buffer available if you reopen that file before leaving the current project,
    but unsaved buffers do not survive a project switch or app restart.

Text files larger than 1 MiB are not loaded. Files containing a null byte or
text that is not valid UTF-8 appear as **Binary file — no preview** instead of
opening in the editor. See [Preview files](previews.md) for the separate image
and PDF limits.

## Handle a change from another tool

The project watcher reconciles the open file when an agent, terminal command, or
another editor changes it on disk:

- If your buffer is clean, the editor reloads the disk version automatically.
- If you have unsaved edits, the editor keeps your buffer and shows **This file
  changed on disk while you had unsaved edits.**

Resolve that banner before saving:

- Select **Reload from disk** to discard your buffer and use the external
  version.
- Select **Keep my version** to keep your buffer. It remains unsaved; press
  **Command-S** afterward to replace the disk version.

If the file was deleted, the choices change to **Close file** and **Keep my
version (re-create)**. Re-create keeps the buffer as an unsaved file; press
**Command-S** to write it back to disk.

!!! note
    **Command-S** does not overwrite a file while the conflict banner is open.
    Choose one of the banner actions first.

For the complete key table and terminal-focus behavior, see [Keyboard
shortcuts](../personalize/keyboard-shortcuts.md).
