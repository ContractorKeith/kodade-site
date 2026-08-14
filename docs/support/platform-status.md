# Platform and release status

ködade is open source under Apache License 2.0. The public app has no paid tier
or required ködade account.

## Current availability

| Platform | Status |
| --- | --- |
| macOS 13 or newer, Apple silicon | Available now as a DMG from [GitHub Releases](https://github.com/Kodade/kodade/releases) |
| Intel Mac | No current release build |
| Windows | No current release package |
| Linux | Planned; no release date set |

The current supported release is the Apple-silicon macOS app. Windows and Linux
support are not available yet; their final requirements will be documented with
their releases.

## Install the macOS release

Download the latest `.dmg` from the public [Releases
page](https://github.com/Kodade/kodade/releases), open it, and drag `kodade.app`
into **Applications**.

The current requirements are:

- macOS 13 or newer
- an Apple silicon Mac
- access to the project folders you want to add
- separately installed and authenticated agent CLIs for agent work

The terminal works without an agent CLI. See [Requirements and release
status](../getting-started/requirements.md) and [Your first
project](../getting-started/first-project.md).

## Updates

ködade does not currently include an automatic updater. Moving to a newer
release is a manual replacement. Save editor changes and stop running terminal
work before quitting the old build.

## Development-feature status

Some experimental source remains in the repository but is intentionally absent
from public release builds:

| Feature | Status |
| --- | --- |
| KödSSH | In development |
| KödWhisper | In development |
| KödLocal | In development |
| KödWeb | Discontinued; no longer under development |

These are not usable public features. KödWork and KödPR are included in the
supported public app. Source or historical engineering documents do not change
the remaining release boundary.
