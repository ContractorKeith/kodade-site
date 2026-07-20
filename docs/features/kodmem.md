# Köd Workspace and KödMem

Köd Workspace helps you see active work. KödMem keeps the project context that
should outlive a terminal session. Both stay local to your machine.

> **Pre-release status**
>
> There is no public download. Current macOS builds are unsigned test builds,
> and Windows human QA remains pending. See [platform and release
> status](../support/platform-status.md).

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

KödMem stores project memory in a SQLite database in ködade's application-data
directory. It uses full-text search and does not need a ködade account, cloud
service, API key, or embedding provider.

Memories are visible Markdown records. Each has a type, source, timestamps, and
history. You can edit, export, or delete it. The KödMem tab can show a current
focus, pinned decisions, open tasks, recent records, and search results.

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

KödMCP lets a compatible agent read relevant project memory and write an
explicit checkpoint. It does not turn terminal output into an automatic memory
stream. See [KödMCP](kodmcp.md) for the local connection model.
