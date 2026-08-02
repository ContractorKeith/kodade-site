# Local data and privacy

ködade keeps its own workspace state on your computer. It does not currently have
a ködade cloud account, telemetry, analytics, a hosted agent API, or an automatic
updater.

That statement covers ködade itself. Agent CLIs, GitHub CLI, and websites can use
the network under their own terms when you run or open them.

## What ködade stores

ködade writes its core workspace metadata to the app's local application-data
directory:

```text
~/Library/Application Support/com.kodade.desktop/kodade.json
```

The file can contain:

- project names, identifiers, folder paths, and chosen colors
- the last active project
- per-project pane sizes and collapsed states
- the selected theme and projects-sidebar mode
- per-project open-tab metadata, including file paths, the GitHub tab, and an
  embedded browser tab's last URL
- chat-thread identity and terminal-session identity

`kodade.json` is workspace metadata, not a copy of your projects. Your source
files stay in the folders you added.

KödChat stores one transcript document per thread under the app-data `chats/`
directory. KödMem uses a local SQLite database and, when enabled for a project,
human-readable files under that project's `.kodade/memory/` directory.

!!! note "Paths and browser URLs are local data too"

    The metadata file can reveal folder names, absolute paths, and a previously
    open browser URL to anyone who can read your macOS account's files. Treat it
    with the same care as other local application data when sharing diagnostics
    or backups.

## What does not persist

ködade does not write these items into `kodade.json`:

- terminal output, prompt history, or running processes
- unsaved editor buffers
- project file contents
- KödChat transcript text, which is kept in separate per-thread documents
- prompts and responses from agents run manually in a terminal, except where
  the CLI or project stores them
- agent-provider or GitHub credentials

Running terminal processes and in-memory editor changes end when the app quits.
Terminal identities can reopen as fresh shells, and open-tab metadata can
restore a tab, but terminal output and unsaved editor buffers are not restored.
Save work before quitting. See [Projects and workspace
layout](../core/projects.md#understand-local-persistence) for the full
persistence table.

## Köd features and local data

[KödMem](../features/kodmem.md) stores activity metadata and memory records
locally in SQLite and can create readable project-memory files. By default, it
does not capture terminal or KödChat transcripts, keystrokes, file contents,
environment variables, clipboard contents, or credentials. Memories are
visible in the app and can be edited or deleted.

[KödChat](../core/kodchat.md) saves transcript text locally. It sends a prompt
to the selected provider CLI when you submit a turn; the provider's own CLI then
controls authentication, model traffic, and tool execution.

## Accounts and credentials

Install and authenticate agent CLIs outside ködade. Their tokens, subscriptions,
configuration, prompts, and remote requests remain under each CLI's control.
ködade detects installed executables and gives them a real terminal; it does
not collect their credentials. See [Agent CLIs](../core/agent-clis.md).

The GitHub view follows the same model. It runs a small, read-only set of
commands through your installed and authenticated `gh` executable. Authentication
stays in `gh`; ködade does not receive or store the token. See [GitHub issues and
pull requests](../workspace/github.md).

## When network access happens

ködade does not contact a ködade service. Network activity can still occur when
you use a network-capable tool:

| Action | What can use the network |
| --- | --- |
| Run an agent in a terminal | The CLI and any command it launches |
| Open the GitHub view | Your authenticated `gh` CLI |
| Open an embedded browser tab | The loaded website and its resources |
| Click an absolute link in a Markdown preview | Your default system browser |

Opening a Markdown file does not automatically fetch its remote images. Remote
images render as links, and only an explicit click can open an absolute HTTP(S)
URL. Relative links and `file:`, `javascript:`, and `data:` URLs are not opened
from rendered Markdown. Read more in [Security boundaries](security.md#rendered-markdown).

## Remove local data

Removing a project from the projects sidebar removes its ködade metadata and
stops its live sessions. It does not delete the project folder.

To reset the core ködade workspace metadata:

1. Save project files and quit ködade.
2. In Finder, select **Go > Go to Folder**.
3. Enter `~/Library/Application Support/com.kodade.desktop/`.
4. Move `kodade.json` somewhere safe as a backup, or move it to Trash.
5. Reopen ködade and add the projects you want.

To remove saved chat transcripts too, move the `chats` folder from the same
application-data directory to Trash. KödMem records and project working-memory
files have their own removal controls; deleting `kodade.json` does not remove
them.

These actions do not remove project source files, CLI configuration, CLI
credentials, or data stored by websites.
