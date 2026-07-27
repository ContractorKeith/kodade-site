# Free and Pro

ködade's core workspace is free, with no account or login: projects, real
terminal sessions, KödChat as the primary surface for the agent CLIs you
installed yourself, the editor and file tree, the GitHub tab and browser pane,
and Light/Dark/System themes. Köd features add focused local workflows around
that workspace. Each has a free
slice that is useful on its own and a Pro slice for the work that needs more
coordination, automation, or scope.

> **Pre-release status**
>
> There is no public download. Current macOS and Windows builds are unsigned
> test builds, the macOS build is not notarized, and Windows human release QA
> is in progress. The initial public release targets macOS and self-hosted web
> (KödWeb); Windows follows after release QA. Pro licenses are not yet for sale — these tiers describe the
> product, not a store. See [platform and release
> status](../support/platform-status.md).

## What stays free

The free tier includes the core workspace and the following feature slices.

| Feature | Free | Pro |
| --- | --- | --- |
| KödChat | Full chat workspace over your installed agent CLIs | No separate Pro slice |
| [KödHarness](kodharness.md) | Inspect the active project for the primary CLI | Compare CLIs and scopes, reversible configuration changes, and the KödSkills pack |
| [KödWhisper](kodwhisper.md) | Local push-to-talk dictation and model management | Prompt cleanup, vocabulary, voice commands, streaming, and larger models |
| [Köd Workspace and KödMem](kodmem.md) | Adaptive work list and local project memory | No separate Pro slice currently |
| [KödMCP](kodmcp.md) | Local memory access for connected agents | No separate Pro slice currently |
| [KödPR](kodpr.md) | Working-tree diff review in the active project | Branch and PR review, ranking, review state, and fix-prompt handoff |
| [KödSSH](kodssh.md) | Read host configuration and open one remote terminal | Remote projects, remote agent tools and file previews, and more sessions |
| [KödWeb](kodweb.md) | Self-hosted browser access in the current release shape | No separate Pro slice in version 1 |
| [KödLocal](kodlocal.md) | Manage a local model and use raw local chat | Local agent loop, project memory, delegation, and saved remote backends |

Some features are included with the core workspace rather than split into
tiers.

## Activate Pro locally

When Pro licenses become available, paste the license token once in Settings
under **license**. ködade verifies its Ed25519 signature locally
and offline. It does not require an account, hardware fingerprint, phone-home
check, or a running ködade service.

Only a valid token enables paid features. An expired, malformed, or invalid
token returns the app to its free capabilities without breaking projects,
terminals, or local data. Your workspace continues to work.

## Keep the boundary clear

Feature access does not change the responsibility of an agent CLI. ködade
organizes the workspace and feature surfaces; the CLI still owns its account,
authentication, permissions, and network activity. Read [agent
CLIs](../core/agent-clis.md) and [local data and
privacy](../trust/local-data-privacy.md) for those boundaries.
