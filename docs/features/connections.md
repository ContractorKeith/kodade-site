# Connections

Connections are the MCP servers an agent should reach. You attach them to an
[agent persona](agents.md), and enabling one installs its server into the CLI's
own MCP config through the same reviewed flow the [KödHarness](kodharness.md)
tools use.

## Choose from the catalog or add your own

Attach a connection from the curated catalog — vidIQ, fal Docs, Gmail, GitHub,
Notion, Context7, Playwright, and Fetch — each shown with its provenance and its
auth requirement. You can also enter a custom stdio or remote server yourself.

## Bring-your-own-key posture

Ködade never stores, bundles, or proxies a credential, and there are no key
fields anywhere. A catalog entry only tells you which token or OAuth client to
set up in your own CLI config. For remote endpoints — including Codex and Grok
`config.toml`, verified against each CLI's own docs — only the server URL is
ever written, so authentication stays in your hands.

## Reviewed installs

Enabling a connection installs its server into the CLI's own MCP config through
the same preview-then-apply review the KödHarness tools use, so nothing is
written silently. Remote endpoints install into every supported CLI.

An attached connection can't let a run do anything a KödWork task with the same
CLI config couldn't. When you prepare a run and an attached connection isn't
installed for the chosen provider, Ködade warns you without blocking the run.

For the local KödMem connection model — a separate, stdio-only server that reads
project memory — see [KödMCP](kodmcp.md).
