# AGENTS.md

## Purpose
Notes App is a small command-line notes manager (Python). It is a
course project used to practise AI-assisted software engineering.
It stores notes in `notes.json`. Keep it small and simple.

## Architecture
- `notes/models.py`  - `Note` dataclass (id, title, text, created_at)
- `notes/storage.py` - load/save `notes.json` (no business logic)
- `notes/service.py` - add, list, search, delete logic (no printing)
- `notes/cli.py`     - argparse interface and output (no file access)
- `tests/test_service.py` - pytest tests for the service layer
Keep this separation: CLI -> service -> storage.

## Setup (Windows, Python 3.11+)
    pip install -r requirements.txt

## Safe commands (run without asking)
    python -m pytest -v
    python -m notes.cli list
    python -m notes.cli search <keyword>
    git status / git diff / git log

## Ask a human first
- Any command that changes data: `python -m notes.cli add|delete`
- `pip install`, or any edit to `requirements.txt`
- `git commit`, `git push`, or creating tags/branches

## Forbidden
- Never read, create or commit secrets, tokens or real personal data
- No production deployment or publishing the package
- No destructive commands: `git push --force`, `git reset --hard`,
  `Remove-Item -Recurse`, deleting files outside the project folder
- No adding, removing or upgrading dependencies without review
- Do not edit or delete the `baseline` tag or its commit
- Tests must never write to the real `notes.json` (use `tmp_path`)

## Coding conventions
- Python 3.11+, standard library only (plus pytest)
- Type hints and short docstrings on new functions
- Small functions; no duplicated logic; clear names
- Errors for invalid user input are raised as `ValueError` in the
  service layer and shown by the CLI as `Error: ...` (exit code 1)

## Test expectations
- Run `python -m pytest -v` before and after every change
- All 7 baseline tests must keep passing (acceptance criteria AC1-AC5)
- Every behaviour change or bug fix needs at least one new test
- Report the exact command and the pass/fail counts

## Review gates
- Propose a diff and wait for human approval before applying it
- One focused change per task; explain what changed and why
- Do not claim a test passed unless it was actually run