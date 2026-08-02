# Requirements and release status

## macOS requirements

The current public release requires:

- macOS 13 or newer
- an Apple silicon Mac
- a project folder you can access from your macOS user account

## Install on macOS

1. Open the [ködade Releases
   page](https://github.com/Kodade/kodade/releases).
2. Download the macOS Apple-silicon `.dmg` from the latest release.
3. Open the DMG and drag `kodade.app` into **Applications**.
4. Open ködade from **Applications**.

Use only a release downloaded from the public repository. See
[Troubleshooting](../support/troubleshooting.md) if the app does not open.

## Other platforms

- Windows is coming the first week of August 2026.
- Linux support is planned; no release date has been set.

## Agent CLI requirements

An agent CLI is optional for using the terminal, but required for agent work.
Install and authenticate each CLI separately using its provider's instructions.
The executable must be available through your login shell's `PATH`.

KödChat currently supports Claude Code and Codex. ködade also detects Grok,
OpenCode, and Ollama for terminal use. The check reports whether each executable
returns version information; it does not install a CLI, update it, or confirm
that its account authentication is valid. See [Agent
CLIs](../core/agent-clis.md) for the exact workflow.

Continue with [Your first project](first-project.md).
