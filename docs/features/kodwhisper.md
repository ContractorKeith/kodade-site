# KödWhisper

KödWhisper is local push-to-talk input for a focused terminal or text field.
Hold the configured key, speak, and release it. The transcript lands in the
focused prompt unsent, so you can read or edit it before sending.

> **Pre-release status**
>
> There is no public download. Current macOS and Windows builds are unsigned
> test builds, the macOS build is not notarized, Windows human release QA is
> in progress, and Pro licenses are not yet for sale. See [platform and
> release status](../support/platform-status.md).

## Dictate locally

KödWhisper runs local `whisper.cpp` models. There is no cloud speech-to-text
service, no API key, and no transcript sent through ködade infrastructure.
Models download when you choose them, with checksum verification before use.

The free tier includes:

- push-to-talk dictation into the focused terminal or input
- `base.en` as the default model and `small.en` as an upgrade
- a model manager for downloads and local model selection
- transcription after key release
- review before send

Open Settings to set the push-to-talk key and manage the voice setup. The
inserted text does not include a trailing return, so dictation cannot submit a
prompt by itself.

## Add project-aware voice with Pro

Pro adds work that depends on the active project and agent context:

- prompt cleanup for spoken punctuation, identifiers, paths, and command forms
- custom project vocabulary
- guarded voice commands
- streaming partial transcripts on capable hardware
- larger and faster voice models

Voice commands use an explicit command capture rather than trying to guess
whether a sentence is a command. State-changing actions ask for confirmation.
Ordinary dictation remains reviewable text.

## Keep audio and provider access separate

KödWhisper is an input layer. It does not authenticate an agent CLI, choose a
provider account, or send your prompt to a hosted transcription service. The
agent CLI and any command you submit retain their normal network and permission
boundaries. See [agent CLIs](../core/agent-clis.md) and [local data and
privacy](../trust/local-data-privacy.md).
