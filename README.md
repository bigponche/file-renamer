# File Renamer

A command-line tool that batch-renames all files inside a folder using a sequential numbering pattern, with an optional prefix and/or suffix. Includes a dry-run preview before any changes are applied, and an undo option to revert the last operation.

## Features

- Renames every file in a given folder with sequential numbering (`001`, `002`, `003`...).
- Optional prefix and/or suffix — the user can use one, both, or neither.
- Dry-run preview: shows exactly how each file will be renamed before touching anything on disk.
- Confirmation step before applying any changes.
- Undo: reverts the files renamed in the last run back to their original names.
- Input validation: rejects invalid folder paths and forbidden characters in the prefix/suffix.
- Subfolders are skipped — only files at the top level of the given folder are renamed.

## Project structure

```
file_renamer/
├── requirements.py    # Project constants (starting number, digit padding, forbidden characters)
├── core.py              # Core Engine + interface functions
└── main.py              # Entry point, application assembly
```

## How it works

1. The program asks for a folder path.
2. It asks for an optional prefix and an optional suffix.
3. It scans the folder and calculates the new name for every file (original extension is always preserved).
4. It shows a preview of every `old_name -> new_name` pair (dry run) — no file is touched yet.
5. The user confirms whether to apply the changes.
6. If confirmed, the files are renamed. Any file that fails (e.g. a name collision) is skipped and reported, without stopping the rest of the batch.
7. The user is asked whether to undo the changes just applied. If confirmed, the successfully renamed files are reverted to their original names.

## Naming pattern

```
prefix + sequential_number + suffix + original_extension
```

Example: with prefix `vac_`, no suffix, and starting number `1`, `photo.jpg` becomes `vac_001.jpg`.

## How to run

```bash
python main.py
```

## Requirements

- Python 3.x (no external dependencies)

## Known limitations

- No support for recursive renaming — subfolders are ignored, not renamed.
- No filtering by file type — all files in the folder are renamed, regardless of extension.
- Undo only works during the same program run — closing the program clears the undo history.
- The user is responsible for including their own separators (e.g. `_`) in the prefix or suffix; the program does not add any automatically.

## Risk Note

See [RISK_NOTE.md](./RISK_NOTE.md).