# Use the embedded browser

The browser opens a web page beside your terminals without turning the page
into part of ködade's app interface. It ships in the macOS build; the Windows
build includes a pre-release implementation that is still in release QA.

## Open a page

1. Select **open browser** at the right of the editor tab strip.
2. Enter a URL in the **url** field.
3. Select **go** or press **Enter**.

A bare host such as `localhost:3000` or `example.com` receives an `https://`
prefix. Enter `http://` explicitly for a local server that does not use TLS.

Use **back**, **forward**, and **reload** in the browser toolbar for navigation.
The tab label changes to the current page's hostname after navigation.

## Supported URLs

The browser accepts only `http://` and `https://` URLs with a host. This rule is
checked for an address you enter and for later page navigation. Local files and
schemes such as `file:`, `data:`, `javascript:`, `tauri:`, and `kodade-doc:` are
refused.

Downloads are blocked. Requests to open a popup or new window are denied.

!!! note
    The Windows embedded browser is pre-release: human visual and release QA
    remain pending, and this page makes no feature-parity or availability-date
    claim for it. In KödWeb browser sessions the embedded browser pane is not
    available on any platform, because it is a native desktop surface.

## Browser security boundary

Remote pages run in a child web view whose app IPC bridge is removed and held
unavailable. A page cannot use that bridge to call ködade commands.

This is a narrow boundary, not a claim that the page is sandboxed, private, or
offline. A loaded page can still run normal web content and make network
requests. Use the same judgment you would use when visiting it in another
browser.

The [GitHub tab](github.md) is separate: it uses your authenticated `gh` CLI and
supports only a read-only issues and pull-request view.
