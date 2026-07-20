# KödPR

KödPR is the in-app review tab for changes in the active project. It is a
reading surface: it does not stage, commit, merge, push, or otherwise write to
your repository.

> **Pre-release status**
>
> There is no public download. Current macOS and Windows builds are unsigned
> test builds, the macOS build is not notarized, Windows human release QA is
> in progress, and Pro licenses are not yet for sale. See [platform and
> release status](../support/platform-status.md).

## Review the working tree for free

The free review tab shows the active project's working-tree diff against HEAD.
Use either a themed unified view or a side-by-side split view to inspect what
has changed before you commit.

KödPR uses an allowlisted, read-only set of Git operations. The terminal and
the agent session remain the writers.

## Review a branch or pull request with Pro

Pro adds review workflows for larger changes:

- compare a branch with its merge base
- load a GitHub pull request diff and CI-check summary through your own `gh`
- put the files most worth reading first
- mark files reviewed, with state saved per branch
- turn line comments into a fix prompt for a selected agent session

The handoff is text pasted into the chosen terminal session. It does not apply
your comments as file edits or post them to GitHub.

## Understand the reading order

The **read this first** order is a transparent local heuristic. It considers
such things as churn concentration, hunk complexity, changed source without
matching tests, file kind, and security-sensitive paths. Each file shows the
reason for its position.

There are no model calls and no cloud ranking step. The ordering works offline
from the diff itself. It is meant to help you choose where to start, not to
replace code review.

## Use your existing GitHub access

PR mode relies on your installed and authenticated `gh` command. KödPR does not
manage a GitHub account or token. See [agent CLIs](../core/agent-clis.md) for
the same responsibility boundary around command-line tools and [security
boundaries](../trust/security.md) for ködade's read-only tool surfaces.
