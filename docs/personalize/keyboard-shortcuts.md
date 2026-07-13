# Keyboard shortcuts

These are the current macOS bindings. They are fixed in this release; there is
no shortcut editor in **settings**.

| Action | Shortcut |
| --- | --- |
| Toggle projects sidebar | **Command-B** (`⌘B`) |
| New terminal session | **Command-T** (`⌘T`) |
| Save file | **Command-S** (`⌘S`) |
| Next session | **Command-Shift-]** (`⌘⇧]`) |
| Previous session | **Command-Shift-[** (`⌘⇧[`) |
| Next project | **Command-Option-Down Arrow** (`⌘⌥↓`) |
| Previous project | **Command-Option-Up Arrow** (`⌘⌥↑`) |
| Close tab | **Command-W** (`⌘W`) |
| Next tab | **Control-Tab** (`⌃⇥`) |
| Previous tab | **Control-Shift-Tab** (`⌃⇧⇥`) |

**Command-T** opens a terminal in the active project. Session and project
shortcuts wrap from the last item to the first. **Command-W** closes the active
editor, GitHub, or browser tab; if no tab is active, it does nothing.

## When a terminal has focus

Command-based app shortcuts continue to work while a terminal has focus. For
example, **Command-T**, **Command-B**, and **Command-W** still act on ködade.

Plain keys and Control chords stay with the shell. That includes **Control-C**,
and it also means **Control-Tab** and **Control-Shift-Tab** do not switch editor
tabs while a terminal has focus. Move focus to the file tree or editor before
using those two tab shortcuts.

For save and conflict behavior, see [Edit and save files](../workspace/editor.md).
For the live theme picker, see [Settings and themes](settings-themes.md).
