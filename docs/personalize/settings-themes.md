# Settings and themes

Open **settings** at the bottom of the projects sidebar. In compact-sidebar
mode, select the Settings icon instead. The panel contains appearance settings
and installed-agent status.

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

## Check installed agent CLIs

The **agent CLIs** section reports whether each supported CLI was found through
the login-shell `PATH` and shows a version when one is available. Select
**refresh** to re-check after installing or updating a CLI.

This section reports installation and version only. It does not authenticate a
CLI, inspect its account, choose a model, or launch an agent. Complete the CLI's
own authentication in a terminal.

For keyboard controls, see [Keyboard shortcuts](keyboard-shortcuts.md).
