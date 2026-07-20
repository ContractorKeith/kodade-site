# KödSSH

KödSSH opens a remote terminal through the system `ssh` command you already
use. It is for a Linux or macOS workstation, homelab machine, or VPS where you
run agent CLIs.

> **Pre-release status**
>
> There is no public download. Current macOS and Windows builds are unsigned
> test builds, the macOS build is not notarized, Windows human release QA is
> in progress, and Pro licenses are not yet for sale. See [platform and
> release status](../support/platform-status.md).

## Use existing SSH configuration

KödSSH reads `~/.ssh/config`, including supported `Include` files, and lists
concrete host aliases. It is read-only: ködade never writes under `~/.ssh` and
never stores, proxies, or sees your SSH credentials.

If you do not use a host alias, enter `user@host` or `user@host:port` in the
ad-hoc host field. KödSSH then opens a normal remote terminal through the
system client. Exit SSH to return to your local shell.

The remote host must be POSIX in version 1. Remote Windows hosts are not
supported.

## Free and Pro access

| Surface | Free | Pro |
| --- | --- | --- |
| Host list | Full read-only list | Same list |
| Remote terminal | One plain SSH session at a time | Unlimited remote sessions |
| Remote project | Not included | Pin a `host:path` project |
| Remote agent CLIs | Not included | Detect and launch supported CLIs |
| Remote files | Not included | Read-only tree and editor preview |

A pinned remote project opens its terminals in the selected remote path. The
file tree and previews are read-only.

## Know the probe limits

Interactive terminals use a real SSH terminal, so password, host-key, and
two-factor prompts can appear as they normally would. Detection, remote file
listing, and previews use a non-interactive `BatchMode=yes` probe. Those probes
need key or agent-based authentication and cannot answer a password or
two-factor prompt.

Remote listings are capped at four levels and 2,000 entries. File previews are
capped at 256 KiB. A truncated result is a safety limit, not a claim that the
remote file ends there.

## Keep credentials with OpenSSH

KödSSH delegates authentication to OpenSSH. Your keys, agent, host-key checks,
and normal configuration remain there. See [agent CLIs](../core/agent-clis.md)
for the separate agent-authentication boundary and [security
boundaries](../trust/security.md) for guidance on shells and agents running
with your user permissions.
