import json
from dataclasses import asdict
from pathlib import Path

from .models import Note

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "notes.json"


def load_notes(path=DEFAULT_PATH):
    """Return the list of saved notes (empty list if the file doesn't exist)."""
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [Note(**item) for item in json.load(f)]


def save_notes(notes, path=DEFAULT_PATH):
    """Write all notes to the JSON file."""
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump([asdict(n) for n in notes], f, indent=2, ensure_ascii=False)