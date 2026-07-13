# Preview files

The editor pane renders Markdown, supported images, and PDFs without sending
their contents through an agent CLI.

## Preview Markdown

Select a `.md` or `.markdown` file. It opens in rendered **view** mode by
default.

- Select **edit** in the tab strip to edit the source.
- Select **view** to return to the rendered document.

The button's label describes the mode it will open next. Markdown source is a
text file, so the 1 MiB text limit still applies.

### Markdown safety

Markdown is rendered as content, not as executable HTML:

- Raw HTML is disabled, and rendered output is sanitized before display.
- Markdown images render as links, not embedded images. Opening the Markdown file
  does not fetch their URLs.
- Only an absolute `http://` or `https://` link can open after you select it.
- Relative links and `file:`, `data:`, and `javascript:` URLs do nothing.

Selecting an allowed link opens it outside the Markdown preview. The safety
rules apply to the preview; they do not make an external website trusted.

## Preview an image

Select any supported image:

- PNG
- JPEG (`.jpg` or `.jpeg`)
- GIF
- WebP
- SVG

The image is contained within the editor pane, with its filename and size below
it. SVG is loaded as an image resource; its markup is not inserted into the app
interface.

Images larger than 10 MiB show **File too large to preview**.

## Preview a PDF

Select a `.pdf` file to open the native PDF viewer in the editor pane. The PDF
viewer supports files up to 25 MiB and can request byte ranges while you move
through the document.

PDFs larger than 25 MiB show **File too large to preview**.

## Limits and unsupported files

| Content | Maximum size | Result above the limit |
| --- | ---: | --- |
| UTF-8 text and Markdown | 1 MiB | **File too large to preview** |
| Supported images | 10 MiB | **File too large to preview** |
| PDF | 25 MiB | **File too large to preview** |

An unsupported binary file shows **Binary file — no preview**. Renaming a binary
file to a supported extension does not convert or validate its contents.

## Preview boundary

Image and PDF reads must resolve inside the active project root. A symlink that
resolves outside the project is refused. This is a document-viewer boundary,
not a sandbox for the project's terminals or agent CLIs.

See [Work with files](files.md) for tree filtering and file operations.
