# View GitHub work

ködade can show a project's open GitHub issues and pull requests in an editor
tab. The integration is read-only and runs the installed `gh` CLI with the
project folder as its working directory.

## Before you open GitHub

The active project needs:

1. The `gh` CLI installed and available through your login-shell `PATH`.
2. An authenticated `gh` session.
3. A repository remote that `gh repo view` resolves to an HTTPS URL on
   `github.com`.

GitHub Enterprise hosts and non-GitHub remotes are not supported by this view.

## Open the GitHub tab

Select **open github** at the right of the editor tab strip. ködade checks `gh`,
authentication, and the repository before loading two sections:

- **open issues**
- **open pull requests**

Each section lists up to 50 open items with number, title, author, labels, and
last update. Select an item to open its page on `github.com` in the system
browser. Select **refresh** to request the current lists again.

!!! note
    The tab does not create, edit, comment on, close, or merge anything. It also
    is not a general Git interface: it does not show working-tree status,
    branches, commits, diffs, or push controls.

## Install or authenticate `gh`

If `gh` is missing, the tab shows **install gh to view issues and pull
requests** and a copyable `brew install gh` command. Install it in a terminal,
restart ködade so it resolves the newly installed executable, then open the
GitHub tab again.

If `gh` is not authenticated, the tab shows **sign in with the gh cli**. Select
**open gh auth login** to put `gh auth login` into a terminal session, complete
the CLI's prompts, then return to the GitHub tab and select **refresh**.

Authentication stays in `gh`; ködade does not receive or store a GitHub token.
The `gh` CLI makes the GitHub network requests using its own authenticated
configuration.

## Fix a repository state

- **no github remote** — add or select a `github.com` remote for the project,
  then select **refresh**.
- **could not load github repository** — read the detail in the card, confirm
  `gh repo view --json url` works from the project folder, then select
  **refresh**.
- An error inside one list — run the equivalent `gh issue list` or `gh pr list`
  command in a terminal to inspect the CLI error, then refresh.

Use the [embedded browser](browser.md) for general HTTP(S) pages. Its security
boundary is separate from the authenticated `gh` integration.
