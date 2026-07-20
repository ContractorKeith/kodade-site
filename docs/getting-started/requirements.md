# Requirements and release status

## Current platforms

The macOS pre-release build path requires:

- macOS 13 or newer
- an Apple silicon Mac
- a project folder you can access from your macOS user account

The Windows pre-release build path requires:

- x64 Windows 10 version 1809 or newer, or Windows 11
- the WebView2 Evergreen Runtime; the installer embeds its bootstrapper and may
  need an internet connection if the runtime is missing
- a project folder you can access from your Windows user account

The Windows installer is per-user and does not require administrator access.
Unsigned preview builds trigger a SmartScreen confirmation. ködade uses your
normal Windows shell, preferring PowerShell 7 (`pwsh`), then Windows PowerShell,
then `cmd`.

## Browser path

With [KödWeb](../features/kodweb.md), a box running `kodade-serve` can be used
from a modern browser.

## Installation status

ködade is still in pre-release testing. There is no public installer or download
yet. The macOS and Windows builds are unsigned; the macOS build is also not
notarized.

> **Before following the guides**
>
> You need a current test build supplied through the project. These pages do not
> provide a public installation package. If macOS blocks a trusted test build,
> follow the limited local-testing steps in [Troubleshooting](../support/troubleshooting.md#macos-blocks-the-test-build);
> those steps do not sign, notarize, or verify the app.

## Agent CLI requirements

An agent CLI is optional for using the terminal, but required for agent work.
Install and authenticate each CLI separately using its provider's instructions.
The executable must be available through your login shell's `PATH`.

ködade currently checks for Claude Code, Codex, Grok, OpenCode, and Ollama. The
check reports whether each executable returns version information. It does not
install a CLI, update it, or confirm that its account authentication is valid.
See [Agent CLIs](../core/agent-clis.md) for the exact workflow.

When a current build is ready, continue with [Your first
project](first-project.md).
