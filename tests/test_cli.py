import pytest

from notes.cli import main
from notes.service import NoteService


@pytest.fixture
def service(tmp_path):
    """A NoteService that saves to a temporary file, not the real notes.json."""
    return NoteService(path=tmp_path / "notes.json")


def test_add_then_list_shows_note(service, capsys):
    assert main(["add", "Shopping", "Buy milk"], service=service) == 0
    assert "Added note 1." in capsys.readouterr().out

    assert main(["list"], service=service) == 0
    out = capsys.readouterr().out
    assert "[1] Shopping" in out
    assert "Buy milk" in out


def test_empty_title_prints_error_and_exits_1(service, capsys):
    assert main(["add", "   ", "text"], service=service) == 1
    captured = capsys.readouterr()
    assert "Error: Title must not be empty" in captured.err
    assert service.list_all() == []


def test_delete_unknown_id_prints_message_and_exits_1(service, capsys):
    assert main(["delete", "999"], service=service) == 1
    assert "No note with id 999." in capsys.readouterr().err