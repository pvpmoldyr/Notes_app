import pytest

from notes.models import Note
from notes.storage import load_notes, save_notes


def test_load_missing_file_returns_empty_list(tmp_path):
    assert load_notes(tmp_path / "missing.json") == []


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "notes.json"
    notes = [Note(1, "Title", "Text", "2026-01-01T00:00:00")]
    save_notes(notes, path)
    assert load_notes(path) == notes


@pytest.mark.parametrize("content", ["{broken", '[{"x": 1}]', '{"a": 1}', "null"])
def test_load_invalid_content_raises_value_error(tmp_path, content):
    path = tmp_path / "notes.json"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError, match="Cannot read notes file"):
        load_notes(path)