import json
from dataclasses import asdict
from pathlib import Path

from .models import Note

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "notes.json"

def load_notes(path=DEFAULT_PATH):
    """Return the list of saved notes (empty list if the file doesn't exist).

    Raises ValueError with a clear message if the file is corrupted.
    """
    path = Path(path)
    if not path.exists():
        return []
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        return [Note(**item) for item in data]
    except (json.JSONDecodeError, TypeError) as error:
        raise ValueError(f"Cannot read notes file {path.name}: {error}") from error


def save_notes(notes, path=DEFAULT_PATH):
    """Write all notes to the JSON file."""
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump([asdict(n) for n in notes], f, indent=2, ensure_ascii=False)