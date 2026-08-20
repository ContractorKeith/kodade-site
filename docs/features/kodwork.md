# Run background tasks with KödWork

KödWork is the outcome-based task inbox in the project sidebar. Use KödChat for
conversation; use KödWork when an agent should keep working toward a result
while you move elsewhere in ködade.

KödWork runs your own installed agent CLI in the selected project folder. Task
records, progress, plans, tool activity, summaries, and review state persist
locally across project and tab switches.

## Start a task

1. In the project sidebar, find the KödWork section for the project and select
   **New task**.
2. Describe the outcome that should be true when the work is complete.
3. Confirm the working folder, provider, and access level.
4. Optionally apply a template discovered from an installed skill.
5. Select **Start task**.

The task stays in KödWork while it runs. Open it to inspect the plan, current
status, tool activity, and summary. Use the steering field to redirect a live
task without starting over, or select **Cancel** to stop it.

## Answer permission requests

When a provider asks for permission, KödWork shows the exact operation in the
task. Choose **Deny**, **Allow once**, or an operation-scoped persistent choice
offered by the provider. Unanswered requests are denied after 60 seconds.

If a task stops because its CLI is signed out, the task says so and offers a
terminal running that CLI's own sign-in command — `claude auth login`,
`codex login`, `grok login`, or `opencode auth login`. Sign in there, then
return to the task and select **Resume**. ködade never sees or stores the
credential.

## Review file output

Every changed file is held for review when a run ends, including failed or
cancelled runs that changed files.

- Select a file to inspect it, or open the full diff for a Git worktree.
- Select **Accept** to keep the output and finish the review.
- Add feedback and select **Reject & continue** to run another pass from the
  original task baseline.
- For a non-Git folder, **Restore output** returns reviewed files to their
  pre-task state. KödWork refuses to overwrite files changed after review was
  collected.

## Run a task on a schedule

When a task is not running, its schedule can be set to an interval or a daily
time. The editor shows a 30-day token projection based on prior runs.

Schedules run only while ködade is open. After a restart, overdue intervals are
collapsed into explicit schedule receipts instead of silently replaying every
missed run.
