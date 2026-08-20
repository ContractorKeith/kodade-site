# Settings and themes

Open **settings** at the bottom of the projects sidebar. In compact-sidebar
mode, select the Settings icon instead. The settings workspace contains general
appearance, providers, KödChat, KödHarness, KödMem, and keybindings.

## Choose a theme

Under **appearance**, open **theme** and select one of these options:

| Option | Appearance |
| --- | --- |
| **System** | Follows the macOS light or dark appearance |
| **Catppuccin Mocha** | Dark |
| **Catppuccin Latte** | Light |
| **Tokyo Night** | Dark |
| **Tokyo Night Light** | Light |
| **Atom One Dark** | Dark |
| **Atom One Light** | Light |

**System** resolves to Catppuccin Mocha in dark appearance and Catppuccin Latte
in light appearance. It updates when the operating-system appearance changes.
An explicitly selected theme stays fixed.

The change applies immediately to the app chrome, live terminals, and editor
syntax colors. Existing terminal processes and scrollback remain in place. The
selection is saved locally and reused when ködade starts again.

## Check or start an agent CLI

The **providers** section reports whether each supported CLI was found through
the login-shell `PATH` and shows a version when one is available. Select
**refresh** to re-check after installing or updating a CLI.

Select an installed provider to start it in a new terminal for the active
project. This does not inspect its account, choose a model, or authenticate it
for you. Complete the CLI's own authentication in that terminal.

Signing an agent CLI in also lives in the surface where it fails: when a
KödChat turn or a [KödWork](../features/kodwork.md) task stops because the CLI
is signed out, that thread or task offers a terminal running the CLI's own
sign-in command, so you no longer have to route through settings to get working
again. Providers keeps the same sign-in shortcut, plus which CLIs are detected
and at what version, where to install a missing one, and which provider a new
chat starts on. Ködade never sees or stores the credential.

## Adjust the background prompt

Agents ködade starts in chat and KödWork receive a short, token-lean background
note that they are running inside ködade, so answers render well in the chat
and terminal panes. It is on by default. **settings > advanced > KödHarness**
shows the exact text, lets you rewrite it, and switches it off entirely. The
note is sent only to sessions ködade launches — it is never written to
`CLAUDE.md`, `AGENTS.md`, or any other file on disk.

For keyboard controls, see [Keyboard shortcuts](keyboard-shortcuts.md).
