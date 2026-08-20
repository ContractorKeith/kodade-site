# Security boundaries

ködade is a local desktop workspace around real development tools. It adds
specific checks around file-manager actions, document previews, GitHub commands,
and rendered Markdown. It is not a sandbox for your shell or agent CLIs.

## The project boundary

Adding a project selects a working folder. Different features enforce that
boundary in different ways:

| Surface | Current boundary |
| --- | --- |
| File-manager actions | Create, rename, Trash, and reveal actions are confined to entries inside the active project. Rename checks both source and destination. The project root itself cannot be renamed or trashed. |
| Image and PDF previews | The document server resolves the requested file and refuses paths or symlinks that leave the active project. It serves only supported image types and PDFs, with size limits. |
| File tree and editor | The UI starts from the active project's tree. Editor reads and saves use normal filesystem access; do not treat the editor as a process sandbox. |
| Terminal and agents | A real login shell starts in the project folder with the macOS user's normal permissions. The shell, an agent, or any command it launches can access other locations that user can access. |

The file-manager checks also resolve parent directories before a mutation, so a
directory symlink cannot be used to create or move an item outside the project.
Moving an item to Trash uses the operating system's Trash rather than permanent
deletion.

!!! warning "Project folder does not mean permission boundary"

    Starting a shell in a project sets its working directory. It does not revoke
    access to your home folder, credentials, other repositories, network, or
    applications. Review the permissions requested by each agent CLI and the
    commands it proposes before approving them.

## Agent and shell permissions

ködade launches the login shell configured by your macOS environment and falls
back to `/bin/zsh` when no shell is available. Agent CLIs run inside that shell,
using the same account, `PATH`, configuration, and operating-system permissions.

ködade does not add a hosted agent layer, intercept provider authentication, or
reduce a CLI's access. Use each provider's own authentication and permission
controls. For a narrower task, use the CLI's supported restrictions or a
separate macOS account, container, or virtual machine as appropriate.

## GitHub view

The GitHub view is read-only. It permits only the `gh` operations needed to:

- check authentication
- identify the active repository
- list open issues
- list open pull requests

The commands run in the active project's folder with fixed arguments. The view
cannot create, edit, merge, close, or delete GitHub resources. Selecting an
issue or pull request opens its HTTPS page. Authentication and network access
remain owned by `gh`. See [GitHub issues and pull requests](../workspace/github.md).

## Embedded browser (archived)

The embedded browser pane is archived in 2.0.0 and is not part of public
release builds, so it no longer presents a browser surface to secure. Chat
links and GitHub items open in your system browser, under that browser's own
trust model. See [Embedded browser (archived)](../workspace/browser.md).

## Rendered Markdown

Markdown preview treats project files as untrusted content:

- raw HTML is disabled and rendered output is sanitized
- remote images become click-to-open links instead of loading automatically
- only absolute HTTP(S) links can open, and they open in the default system browser
- relative links and `file:`, `javascript:`, and `data:` URLs do nothing

When opened directly, supported local images are rendered as image resources
rather than inserted as raw markup. Directly opened image and PDF bytes are
served only after the active-project path and file type pass the document checks
described above. See [Previews](../workspace/previews.md).

## Release and update boundary

Download the public macOS DMG only from the
[Kodade/kodade Releases page](https://github.com/Kodade/kodade/releases). Do not
bypass Gatekeeper for a public release that macOS refuses to open; delete it and
download a fresh copy from the repository.

ködade has no automatic updater. Installing a newer release is a manual
replacement, so verify where it came from before opening it. Current
availability is listed in [Platform and release
status](../support/platform-status.md).
