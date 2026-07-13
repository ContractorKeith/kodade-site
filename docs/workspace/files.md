# Work with files

The **files** pane shows the active project's files and folders. Folders load
when you expand them, so a large project does not need to be read all at once.

## Browse the tree

Select a file to open it in an [editor tab](editor.md). Select a folder to load
and expand it. Select it again to collapse it.

The tree leaves these heavy dependency and build directories out of both the
listing and filesystem watcher:

- `.git`
- `node_modules`
- `target`
- `dist`
- `build`

This is an exact name-based list. Other dotfiles and folders, including a folder
named `vendor`, are not hidden by this rule.

## Filter loaded files

Enter part of a name in **filter loaded files**. Matching is
case-insensitive, and parent folders stay visible so you can follow the path to
a match.

!!! note
    The filter checks only folders already loaded in the tree. Expand a folder
    before filtering if you want its contents included. This is not a project-wide
    file search or a content search.

## Create a file or folder

1. To create at the project root, select **new file** or **new folder** in the
   **files** toolbar.
2. To create inside a folder, right-click the folder and select **new file** or
   **new folder**.
3. Enter a name, then press **Enter** or click elsewhere to create it. Press
   **Escape** to cancel.

ködade refuses an empty name, a name containing `/`, or a name that already
exists in that folder. Creating a file never replaces an existing file.

## Rename an item

1. Right-click a file or folder and select **rename**.
2. Enter the new name.
3. Press **Enter** or click elsewhere to commit the rename. Press **Escape** to
   cancel.

For a file with an extension, the initial selection covers its base name so you
can keep the extension. A rename will not overwrite an existing sibling. Open
tabs and unsaved-change markers follow a successful rename.

## Move an item to Trash

Right-click a file or folder and select **delete**. Despite the UI label, ködade
moves the item to the operating system's Trash instead of permanently deleting
it.

!!! warning
    **delete** acts immediately. Recover an item from Trash with Finder if you
    selected it by mistake.

## Reveal or copy a path

Right-click an item, then select:

- **reveal in finder** to show it in Finder.
- **copy path** to copy its absolute path to the clipboard.

## Refresh the tree

The active project is watched for filesystem changes. When another tool creates,
renames, edits, or removes an item, ködade refreshes affected folders that are
already loaded. Changes inside the five hidden directories are ignored.

Select **refresh** in the **files** toolbar to re-list every folder currently
loaded in the tree. Select **collapse all** to return to the root listing.

## File-operation boundary

Create, rename, Trash, and Finder reveal operations are checked against the
active project root. The project root itself cannot be renamed or moved to
Trash from this pane, and an in-project directory symlink cannot redirect a
mutation outside the project.

This boundary applies to the file manager. It does not sandbox terminal shells
or agent CLIs, which keep the user's normal operating-system permissions.

Next: [edit and save text files](editor.md) or [preview Markdown, images, and
PDFs](previews.md).
