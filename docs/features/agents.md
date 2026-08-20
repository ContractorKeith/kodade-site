# Agents tab

The Agents tab builds reusable agent personas and prepares runs from them. A
persona captures how you want an agent to work once, so you can launch it again
without re-describing it every time.

## Build a persona

A persona is a name, a provider, a system prompt, and the KödSkills it should
lean on. Personas are kept in an app-wide or per-workspace list, so you can
share a persona across every project or scope it to one.

The persona document is versioned and never overwritten when it can't be read,
so a downgrade or a corrupt file can't wipe your agents.

## Attach Connections

A persona can attach [Connections](connections.md) — the MCP servers an agent
should reach — from a curated catalog or a custom stdio or remote server you
enter yourself. Ködade stays bring-your-own-key: a catalog entry only tells you
which token or OAuth client to set up in your own CLI config, and there are no
key fields anywhere.

## Prepare a run

Preparing a run drafts a normal [KödWork](kodwork.md) background task from the
persona and hands off to the existing spawn path. A launched persona therefore
keeps the same durable progress, scoped permissions, review, and recurrence as
any other KödWork task.

When a persona relies on KödSkills, those skills install through the same
reviewed [KödHarness](kodharness.md) flow as run preparation — nothing is
written silently. If an attached connection isn't installed for the chosen
provider, preparing the run warns you without blocking.

## What a persona can and can't do

An attached connection can't let a run do anything a KödWork task with the same
CLI config couldn't. Personas describe intent and configuration; the agent CLI
you install and authenticate still does the work, under its own permissions.
