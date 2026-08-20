# KödHarness

KödHarness is the set of reviewed tools that change what an agent CLI reads:
the KödSkills pack, project skills, and MCP registrations. Each change uses the
same preview-then-apply confirmation, so nothing is written silently.

## Where it lives

The KödHarness tools are inline under **settings > advanced > KödHarness**.
Ködade retired the earlier inventory pane — the artifact matrix, its scope
toggle, the in-app instruction editor, and the per-artifact enable/disable
switches are gone. Instruction files such as `CLAUDE.md` and `AGENTS.md` are
yours to edit directly in the editor, and Ködade's own guidance to agents is
the background prompt (see [Settings and themes](../personalize/settings-themes.md)).

## The tools that change something

From **settings > advanced > KödHarness** you can:

- install and update the pinned KödSkills engineering pack for the supported
  CLI targets
- add a project skill to the right target directories
- merge one MCP server into a detected config file

Each of these previews the exact change and asks you to confirm before it
writes. The same discipline applies when an [agent persona](agents.md) installs
its KödSkills while preparing a run, and when a [Connection](connections.md)
installs an MCP server into a CLI's own config.

## Use it with your CLI

KödHarness does not install, authenticate, or run an agent CLI. Start the CLI in
a normal ködade terminal when you are ready. See [agent
CLIs](../core/agent-clis.md) for that workflow and [security
boundaries](../trust/security.md) for the distinction between a project working
directory and an operating-system permission boundary.

KödMem connection setup uses a separate preview, merge, verify, and backup flow.
See [KödMCP](kodmcp.md).
