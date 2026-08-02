# Agent CLIs

ködade orchestrates command-line tools; the tools do the agent work. Install,
update, and authenticate each agent CLI separately. Claude Code and Codex can
answer in KödChat or run interactively in a terminal. Other detected CLIs run
in a terminal.

## What ködade detects

The current **settings > providers** section checks these executables:

| Settings label | Executable |
| --- | --- |
| Claude Code | `claude` |
| Codex | `codex` |
| Grok | `grok` |
| OpenCode | `opencode` |
| Ollama | `ollama` |

At startup, ködade asks each executable for its version through a non-interactive
login shell. This lets the check use the same login-shell `PATH` that finds tools
installed through common shell and package-manager setups.

Open **settings > providers** and select **refresh** to run the checks again.
Each entry reports a version or **not installed**.

> **Detection has a narrow meaning**
>
> A version means the executable ran and returned usable version output. It does
> not prove that the CLI is authenticated or that its remote service is
> reachable. **not installed** can also mean that the version command failed or
> timed out.

## Install and authenticate a CLI

Use the provider's own installation instructions and sign-in flow. ködade does
not install CLIs, manage their accounts, store their credentials, or test their
authentication state.

After installing or updating a CLI:

1. Open a ködade terminal in the project you want to work on.
2. Confirm the executable is on the login-shell `PATH`:

   ```sh
   command -v codex
   ```

3. Confirm that it reports a version:

   ```sh
   codex --version
   ```

4. Replace `codex` in those commands with your CLI's executable.
5. Open **settings** and select **refresh**.

## Start a KödChat thread

KödChat runs Claude Code or Codex headlessly and renders the CLI's structured
output in the workspace. Each thread has an explicit provider, model, and access
level. It inherits the authentication you completed through that CLI.

Select **+** beside a project under **KödChat**, or choose a default provider in
**settings > KödChat**. See [KödChat](kodchat.md) for the complete workflow.

## Launch an agent manually

In the project's terminal, enter the CLI command yourself:

```sh
codex
```

Use the command and options documented by that CLI. Its prompts, authentication,
permissions, network access, and output remain the CLI's responsibility. ködade
provides the terminal session and project working directory.

See [Terminal sessions](terminal-sessions.md) to create a dedicated session,
rename it, or switch between concurrent tools.

## Inspect agent configuration

[KödHarness](../features/kodharness.md) lets you inspect the instructions,
skills, and MCP servers each detected CLI will read before it runs.
