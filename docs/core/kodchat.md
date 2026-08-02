# KödChat

KödChat puts Claude Code and Codex conversations beside your project, files,
editor, and terminals. It runs the official CLIs on your Mac; ködade does not
proxy model traffic or hold provider credentials.

## Start a chat

Install and authenticate Claude Code or Codex first. Then:

1. Add or select a project.
2. Expand the project under **KödChat** in the sidebar.
3. Select **+** beside the project.
4. Choose the provider, model, and access level in the composer.
5. Enter a message and press **Enter**. Use **Shift-Enter** for a new line.

The first message becomes the thread name. Each later turn resumes the same CLI
conversation when the provider supports it.

## Choose an access level

Access is selected per thread and maps to the provider CLI's own controls:

| Level | Intended use |
| --- | --- |
| **Plan only** | Read the project and propose changes without writing. |
| **Standard** | Read files, edit the project, and run commands. |
| **Full access** | Let the agent act without permission prompts. |

Review the selected level before sending. KödChat does not add a sandbox beyond
the controls supplied by the CLI.

## Add context or open a terminal

Drop files onto the chat pane to add their paths to the next message. The agent
still decides whether and how to read them under its selected access level.

Use the terminal control in the KödChat header when you need an interactive
shell, a provider login flow, or a CLI that does not yet have a chat adapter.
Claude Code and Codex are the supported KödChat providers in the current public
release; other detected CLIs remain available in a terminal.

## Understand transcript storage

KödChat saves each thread as a local JSON document in ködade's application-data
directory. Closing a chat thread deletes its transcript document. Transcript
text is not copied into KödMem activity records.

See [Local data and privacy](../trust/local-data-privacy.md) for the storage
boundary and [Agent CLIs](agent-clis.md) for installation and authentication.
