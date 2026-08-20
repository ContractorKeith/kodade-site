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

## Set up project knowledge

New KödMem setups keep project knowledge in a git-ignored `.kodade/knowledge`
directory inside the project, with zero setup. Enabling KödMem for a project
creates the knowledge surface and its files in the same step, so there is
nothing to choose and nothing to connect first.

Sync with an Obsidian projects vault is the explicit option, collapsed under
**settings > KödMem**. Switching a project from local knowledge to vault sync
asks first and leaves the files already in `.kodade/knowledge` on disk.

A project can only have one knowledge surface. Mapping a project to an Obsidian
vault is refused while local project knowledge is on, and asks you to turn it
off first. Existing vault setups are unchanged and keep their current screen; a
project that had KödMem enabled before this release is never converted on its
own and can set up local project knowledge with one click.

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
