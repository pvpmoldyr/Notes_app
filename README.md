# Notes App

A small command-line notes app written in Python 3.11+. Notes are saved in
`notes.json` in the project folder (created on the first `add`).

## Features

- Add a note (title + text)
- List all notes
- Search notes by keyword (title or text, case-insensitive)
- Delete a note by id

## Setup

```bash
pip install -r requirements.txt
```

## Run

Run all commands from the `notes-app/` folder:

```bash
python -m notes.cli add "Shopping" "Buy milk and bread"
python -m notes.cli list
python -m notes.cli search milk
python -m notes.cli delete 1
```

## Test

```bash
pytest
```

## Project layout

- `notes/models.py`: the `Note` dataclass
- `notes/storage.py`: loads and saves `notes.json`
- `notes/service.py`: add, list, search and delete logic
- `notes/cli.py`: argparse command-line interface
- `tests/test_service.py`: pytest tests for the service layer