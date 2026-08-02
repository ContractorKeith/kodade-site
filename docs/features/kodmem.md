# Köd Workspace and KödMem

Köd Workspace helps you see active work. KödMem keeps the project context that
should outlive a terminal session. Both stay local to your machine.

## See work at the right density

Köd Workspace replaces a uniform session list with adaptive session cards. A
card has a status of **working**, **idle**, **exited**, or **failed**. It can
also show an attention signal when activity is unread or an agent has explicitly
reported that it needs you.

Card density is a current projection, not saved layout state. Selected, failed,
or attention-worthy sessions expand. Recent work stays standard. Old idle or
exited sessions compact into the settled part of the sidebar. The project name
and color remain visible, and selecting a card activates that project and
session.

## Keep project memory local and inspectable

Enable KödMem for the active project from **settings > KödMem**. It creates
human-readable working-memory files under `.kodade/memory/`:

```text
.kodade/memory/
  STATE.md
  WORKLOG.md
  decisions.md
```

`STATE.md` keeps the current handoff concise. `WORKLOG.md` is an append-only
checkpoint journal, and `decisions.md` records dated decisions. You can commit
the directory with the project or keep it local with a managed `.gitignore`
entry.

The files are the portable source of truth. A local SQLite store indexes them
for search and keeps activity, durable records, provenance, and checkpoint
bookkeeping. KödMem does not need a ködade account, cloud service, API key, or
embedding provider.

Durable memories are visible records with a type, source, timestamps, and
history. You can edit, export, or delete them. The KödMem view shows the readable
working-memory files, checkpoint timeline, saved memories, and search results.

## Understand default capture

KödMem records low-sensitivity activity metadata by default:

- project and session lifecycle
- active and idle transitions
- files opened or saved in the app
- provider launches
- timestamps

It does not capture terminal transcripts, keystrokes, file contents,
environment variables, clipboard contents, or credentials by default. You can
pause capture for a workspace, change retention, or remove its memory. See
[local data and privacy](../trust/local-data-privacy.md) for the broader
workspace-data boundary.

## Connect an agent when you choose

KödMCP lets a compatible agent load project context, search memory, and write an
explicit checkpoint. It does not turn terminal output or KödChat transcripts
into an automatic memory stream. See [KödMCP](kodmcp.md) for the local
connection model.
