# KödHarness

KödHarness shows what an agent will read before it runs. It brings instruction
files, skills, subagents, and MCP registrations into one project-aware view
instead of making you hunt through separate CLI folders and configuration files.

> **Pre-release status**
>
> There is no public download. Current macOS and Windows builds are unsigned
> test builds, the macOS build is not notarized, Windows human release QA is
> in progress, and Pro licenses are not yet for sale. See [platform and
> release status](../support/platform-status.md).

## Inspect an agent's harness

Open a project's KödHarness tab to inspect its harness artifacts:

- instruction files such as `CLAUDE.md`, `AGENTS.md`, and `GROK.md`
- installed skills and their enabled state
- subagent definitions
- MCP server registrations

The free view is read-only. It shows the active project and its primary CLI, so
you can check the instructions and capabilities that CLI will see before you
start it.

## Compare or change configuration with Pro

Pro adds the multi-CLI matrix, global scope, cross-project visibility, and
controlled edits. It can:

- compare instructions, skills, subagents, and MCP registrations across
  supported CLIs
- edit instruction files
- enable or disable a skill by renaming it with a reversible `.disabled` suffix
- merge one MCP registration into a third-party configuration file
- restore a backup made before a change

The `.disabled` rename is visible on disk and does not delete the skill. It is
used where a CLI does not have its own portable enable or disable control.

## Review every write

KödHarness follows one sequence for every configuration change: plan, apply,
verify, then restore if needed. The plan shows the proposed diff before anything
is written. Apply makes a backup first, then verifies the result. Restore uses
that backup.

For a third-party JSON, JSONC, or TOML configuration, KödHarness merges only
the intended entry. It rejects a change that would replace or alter unrelated
configuration. It never clobbers an entire third-party config file.

Skills linked from a dotfiles repository are treated as symlinks, not ordinary
directories. KödHarness can operate on the link entry but never writes through
it into the linked repository. A broken link is reported instead of being
silently treated as an empty skill.

## Use it with your CLI

KödHarness does not install, authenticate, or run an agent CLI. It gives you a
clearer view of the files and registrations the CLI uses. Start the CLI in a
normal ködade terminal when you are ready. See [agent
CLIs](../core/agent-clis.md) for that workflow and [security
boundaries](../trust/security.md) for the distinction between a project working
directory and an operating-system permission boundary.

KödMCP setup uses the same merge and backup discipline. See [KödMCP](kodmcp.md).
