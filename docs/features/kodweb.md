# KödWeb

KödWeb lets you run `kodade-serve` on an always-on machine and use that
machine's ködade workspace from a browser. Terminals, projects, agent CLIs,
files, and project memory stay on the machine running the server.

> **Pre-release status**
>
> There is no public download. The hosted shell at `app.kodade.com` may not be
> live during pre-release. Current macOS builds are unsigned test builds, and
> Windows human QA remains pending. See [platform and release
> status](../support/platform-status.md).

## Start a local server and pair a browser

Run `kodade-serve` on the always-on box. It serves a browser client and prints
a one-time pairing URL. Pairing creates a server-side session, so a browser can
reload or reconnect to the same workspace.

Each terminal keeps up to 1 MiB of output in a replay ring buffer. On reconnect,
the browser receives what it missed within that limit. Earlier output is dropped
when the buffer fills.

Treat the pairing URL as a secret. Anyone who uses its token can pair with that
box and access its available workspace. Revoke a session when it is no longer
needed.

## Keep the server private by default

`kodade-serve` binds to loopback by default. For access from another machine,
use Tailscale and put HTTPS in front of the local server with `tailscale serve`.
This also gives the browser a secure WebSocket path when you open an HTTPS
frontend.

Do not expose the server directly on a public address without understanding the
network and TLS implications. The server does not handle the credentials of the
agent CLIs on the box; authenticate those CLIs there as you would over SSH.

## Use the hosted shell when it is available

`app.kodade.com` is a static convenience frontend. It never proxies traffic.
The browser connects directly to the `kodade-serve` instance you paired, so the
hosted shell does not receive your terminal traffic, files, or credentials.

## Expect browser-specific limits

Web mode hides native-only surfaces:

| Hidden surface | Reason |
| --- | --- |
| Embedded browser pane | It is a native desktop webview. |
| Native folder picker | Browser sessions use a server-side directory browser instead. |
| Reveal in Finder or Explorer | The file is on the server, not the browser's machine. |
| Voice input | Voice capture is desktop-only in version 1. |

The daemon can outlive a browser tab, but it does not preserve PTY sessions
across its own restart. A restart, reboot, deploy, or termination ends the
running sessions in version 1.

Read [KödLocal](kodlocal.md) for the separate desktop-only model-management
boundary and [security boundaries](../trust/security.md) before exposing a
machine that can run your shell and agent tools.
