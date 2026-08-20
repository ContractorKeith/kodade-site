# Embedded browser (archived)

!!! note "Archived in 2.0.0"

    The embedded browser pane is archived. Public release builds no longer ship
    the browser tab, its title-bar action, the native browser commands, or the
    KödBrowser agent tools. Chat links open in your system browser instead.

Ködade removed the in-app browser surface from public builds in 2.0.0. On first
launch after upgrading, persisted browser tabs from earlier versions are dropped
on restore without affecting your other tabs.

The surface stays in ködade's source behind a development-feature flag while it
is reworked, so it can be revived in a later release. It is not a usable feature
in the current public app.

To view a web page, use your normal system browser. The read-only [GitHub
tab](github.md) is a separate feature and remains part of the public app.
