# KödHarness

KödHarness shows what an agent will read before it runs. It brings instruction
files, skills, subagents, and MCP registrations into one project-aware view
instead of making you hunt through separate CLI folders and configuration files.

## Inspect an agent's harness

Select the active project, then open **settings > KödHarness** to inspect its
harness artifacts:

- instruction files such as `CLAUDE.md`, `AGENTS.md`, and `GROK.md`
- installed skills and their enabled state
- subagent definitions
- MCP server registrations

The public view is read-only. It shows the active project and the installed
agent configuration, so you can check the instructions and capabilities an
agent will see before you start it. Symlinks and broken links are reported as
such instead of being treated as ordinary or empty skill directories.

## Inspect KödSkills

The public app includes the pinned KödSkills engineering pack. KödHarness shows
the pack and the supported CLI targets without relying on an online catalog.
Review a skill before adding it to an agent's configuration.

## Use it with your CLI

KödHarness does not install, authenticate, or run an agent CLI. It gives you a
clearer view of the files and registrations the CLI uses. Start the CLI in a
normal ködade terminal when you are ready. See [agent
CLIs](../core/agent-clis.md) for that workflow and [security
boundaries](../trust/security.md) for the distinction between a project working
directory and an operating-system permission boundary.

KödMCP connection setup uses a separate preview, merge, verify, and backup flow.
See [KödMCP](kodmcp.md).
