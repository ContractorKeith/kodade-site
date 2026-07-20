# KödMCP

KödMCP lets an agent CLI use the project memory in KödMem without sending that
memory through a hosted service. The bundled `kodade-mcp` server runs as a local
stdio process and reads the local KödMem database directly.

> **Pre-release status**
>
> There is no public download. Current macOS builds are unsigned test builds,
> and Windows human QA remains pending. See [platform and release
> status](../support/platform-status.md).

## What the server does

An MCP client launches `kodade-mcp` for a registered project. The server can
return current focus, checkpoints, decisions, tasks, and full-text memory
searches. With permission, it can also record a typed memory or checkpoint.

The server works while the ködade desktop UI is closed. It opens no network
port and requires no token or other shared secret. Its trust boundary is the
local executable and your operating-system user account.

KödMCP is deliberately local stdio only. Remote MCP transport is not included.

## Connect agents safely

KödMem's **Connect agents** section prepares a configuration change for
supported clients. For Claude Code it targets a project `.mcp.json`; for Codex
it targets `~/.codex/config.toml`.

Before writing, the setup flow detects the existing configuration, prepares a
single-entry merge, and shows the diff. It makes a backup, applies the merge,
verifies it, and can restore the backup. Existing MCP servers remain intact.
This is the same safety discipline used by [KödHarness](kodharness.md): it
never replaces a whole third-party configuration file.

## Keep memory scoped and visible

Each connection is scoped to a project already registered in ködade. A client
cannot select an arbitrary filesystem path through an MCP request. You can make
a connection read-only, revoke it, review recent reads and writes, export
memory, or delete it from the app.

Every memory mutation records its source and timestamp. KödMem does not
automatically capture raw terminal transcripts and guards against oversized or
likely credential-bearing writes. Read [Köd Workspace and KödMem](kodmem.md)
for what the local database contains, and [security
boundaries](../trust/security.md) for the separate permissions of the terminal
and agent CLI.
