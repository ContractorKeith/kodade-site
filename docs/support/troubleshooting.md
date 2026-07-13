# Troubleshooting

Start with the symptom you can see. The steps below match the current macOS
pre-release build.

## macOS blocks the test build

**Symptom:** macOS says Apple cannot check ködade for malicious software, or the
app cannot be opened because the developer cannot be verified.

The current test build is unsigned and not notarized. If you trust where the
build came from:

1. Drag `kodade.app` into **Applications**.
2. In Finder, Control-click or right-click the app and select **Open**.
3. Select **Open** again in the confirmation dialog.

If Gatekeeper still blocks a trusted local test copy, you can clear quarantine
for that copy:

```sh
xattr -dr com.apple.quarantine /Applications/kodade.app
```

!!! warning "Local testing only"

    Clearing quarantine does not sign, notarize, or verify the app. Do not use
    this command for a build whose source you cannot verify.

See [Platform and release status](platform-status.md) before treating any build
as ready for distribution.

## A project does not open at a working prompt

**Symptom:** adding a project shows no usable prompt, the session exits, or a
previous project no longer starts.

1. Confirm the folder still exists and your macOS account can open it.
2. If the folder moved or was renamed outside ködade, remove the stale project
   entry and add its current folder.
3. In macOS Terminal, check the configured shell:

   ```sh
   printf '%s\n' "$SHELL"
   "$SHELL" -l
   ```

4. Fix any error printed by your login-shell startup files, then open a new
   ködade session.
5. If an exited session remains dimmed in the sidebar, close it and select
   **+ new session**.

ködade starts the shell with the project folder as its working directory. Once
the prompt appears, run `pwd` to verify it. See [Terminal sessions](../core/terminal-sessions.md).

## An installed agent CLI shows **not installed**

**Symptom:** the CLI works somewhere else, but **settings > agent CLIs** reports
**not installed**.

Detection runs `<command> --version` in a non-interactive login shell and gives
the check five seconds. Test the same essentials in macOS Terminal:

```sh
"$SHELL" -l -c 'command -v codex && codex --version'
```

Replace `codex` with `claude`, `grok`, `opencode`, or `ollama` as needed.

- If `command -v` prints nothing, put the executable on the login-shell `PATH`.
- If the version command errors or hangs, fix that CLI or the shell startup file
  that blocks a non-interactive login shell.
- After a change, open **settings** and select **refresh**.

A reported version proves only that the executable responded. If the agent
later asks you to sign in, complete the CLI's own authentication flow. See
[Agent CLIs](../core/agent-clis.md).

## The GitHub view cannot load

### It says `install gh`

Install GitHub CLI, then restart ködade so it can resolve the new executable:

```sh
brew install gh
gh --version
```

### It says `sign in with the gh cli`

Run:

```sh
gh auth login
gh auth status
```

Then return to the GitHub tab and select **refresh**. Authentication stays in
`gh`; ködade does not store the token.

### It says `no github remote`

In the project's terminal, inspect the repository and its remotes:

```sh
git status
git remote -v
gh repo view --json url
```

The folder must be a Git repository with a remote that `gh` recognizes on
`github.com`. Add or correct the remote using the URL for your repository, then
refresh the tab. The current view does not support GitHub Enterprise hosts.

The GitHub view lists open issues and pull requests only; it does not mutate
them. See [GitHub issues and pull requests](../workspace/github.md).

## A file or folder is missing from the tree

**Symptom:** the item exists on disk but does not appear in the files pane or in
filtered results.

- Select the files-pane **refresh** button.
- Expand the parent folder. The filter searches only folders already loaded in
  the tree; it does not search unopened directories.
- Clear the filter to see the full loaded tree.
- Dotfiles are shown, but heavy metadata, dependency, and build directories are
  intentionally omitted: `.git`, `node_modules`, `target`, `dist`, and `build`.

Use the terminal or Finder when you need to inspect an omitted directory.

## A file says it is too large or binary

**Symptom:** the editor shows **File too large to preview** or **Binary file —
no preview**.

Current preview limits are:

| Content | Limit |
| --- | ---: |
| Text | 1 MiB |
| PNG, JPEG, GIF, WebP, or SVG image | 10 MiB |
| PDF | 25 MiB |

Text containing a null byte or invalid UTF-8 is treated as binary. Other binary
formats do not have an embedded preview. Open the file with an appropriate
external tool, or inspect it from the terminal. Reducing a supported file below
its limit allows ködade to preview it.

See [Previews](../workspace/previews.md) for supported formats and security boundaries.

## The editor reports a save conflict

**Symptom:** a banner says the file changed or was deleted on disk while you had
unsaved edits. This commonly happens when an agent edits the same file.

- Select **Reload from disk** to discard your buffer and use the external version.
- Select **Keep my version** to keep your buffer as unsaved work. Review it, then
  save when you are ready to replace the disk version.
- If the file was deleted, choose **Close file** to accept the deletion or
  **Keep my version (re-create)** to keep a buffer you can save as the file again.

Saving is disabled while the conflict banner is unresolved. Compare the two
versions before choosing when both contain work you need.

**Symptom:** a **Could not save** banner appears.

The unsaved buffer remains in memory. Read the error, confirm the file and its
parent folder still exist and are writable, fix the permission or path problem,
then save again.

## A browser page or action does not work

**Symptom:** the URL is rejected.

Enter an HTTP or HTTPS address. A bare hostname such as `example.com` becomes
HTTPS. `file:`, `data:`, `javascript:`, custom-scheme, and hostless URLs are not
supported.

**Symptom:** a download, sign-in popup, or new window does nothing.

The embedded browser blocks downloads and popup or new-window requests. Open the
site in your normal browser for a flow that requires one of them, then return to
ködade. The embedded browser is currently macOS-only.

**Symptom:** a local development site does not load.

Confirm its server is running in a terminal, then enter the full address, for
example `http://localhost:3000`. Use the browser's **reload** button after the
server starts. See [Browser tab](../workspace/browser.md).

## Unsaved changes disappeared after restart

**Symptom:** tabs reopen, but edits that were not saved are gone.

ködade persists tab metadata, not editor buffers. Dirty edits can survive
switching files or closing and reopening a tab during the same app run, but they
do not survive quitting, restarting, or removing the project. A dirty dot marks
unsaved work. Save with `Command-S` before quitting or installing another build.

For the complete boundary, see [Local data and privacy](../trust/local-data-privacy.md).
