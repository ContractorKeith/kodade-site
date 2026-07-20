# Platform and release status

ködade is in pre-release testing. There is no public installer or download yet.

## Current availability

| Platform | Status |
| --- | --- |
| macOS 13 or newer, Apple silicon | Pre-release build path; unsigned and not notarized |
| Intel Mac | No current release build |
| Windows 10 version 1809 or newer, or Windows 11 (x64) | Pre-release build path; unsigned, with human release QA in progress |
| Browser (KödWeb) | Client for a self-hosted `kodade-serve` daemon; ships with the app builds |

The Windows app exists and is exercised in automated verification. Signing and
human release QA remain before public availability. This page makes no Windows
release-date or feature-parity commitment.

## macOS test builds

The current build produces an Apple-silicon app and DMG. It is not signed with a
Developer ID certificate and is not notarized by Apple, so Gatekeeper warnings
are expected on a new Mac.

This is a test path, not the public release experience. Follow [the Gatekeeper
steps](troubleshooting.md#macos-blocks-the-test-build) only for a build from a
source you trust.

The current requirements are:

- macOS 13 or newer
- an Apple silicon Mac
- access to the project folders you want to add
- separately installed and authenticated agent CLIs for agent work

The terminal works without an agent CLI. See [Requirements and release
status](../getting-started/requirements.md) and [Your first
project](../getting-started/first-project.md).

## Pro licensing

ködade has free and Pro tiers. Activation uses a one-time license token in
Settings that the app verifies offline. Licenses are not yet on sale during
pre-release. See [Free and Pro](../features/free-and-pro.md).

## Updates

ködade does not currently include an automatic updater. Moving to a newer test
build is a manual replacement. Save editor changes and stop terminal work before
quitting the old build; live sessions and unsaved buffers do not survive a
restart.

Release availability can change as signing, notarization, packaging, and manual
QA are completed. This page makes no promise about a date.
