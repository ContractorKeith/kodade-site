# Requirements and release status

## Current platform

The current ködade release path requires:

- macOS 13 or newer
- an Apple silicon Mac
- a project folder you can access from your macOS user account

Windows support is in development. No Windows release date or feature-parity
claim is available.

## Installation status

ködade is still in pre-release testing. There is no public installer or download
yet, and the current macOS build is not signed or notarized.

> **Before following the guides**
>
> You need a current test build supplied through the project. These pages do not
> provide a Gatekeeper workaround or a public installation package.

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
