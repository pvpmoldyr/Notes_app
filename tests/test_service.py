import pytest

from notes.service import NoteService


@pytest.fixture
def service(tmp_path):
    """A NoteService that saves to a temporary file, not the real notes.json."""
    return NoteService(path=tmp_path / "notes.json")


def test_add_note_saves_and_assigns_id(service):
    note = service.add("Shopping", "Buy milk")
    assert note.id == 1
    assert [n.title for n in service.list_all()] == ["Shopping"]


def test_ids_increase_with_each_note(service):
    first = service.add("One", "a")
    second = service.add("Two", "b")
    assert second.id == first.id + 1


@pytest.mark.parametrize("bad_title", ["", "   "])
def test_empty_title_is_rejected(service, bad_title):
    with pytest.raises(ValueError):
        service.add(bad_title, "some text")
    assert service.list_all() == []


def test_search_matches_title_or_text_case_insensitively(service):
    service.add("Groceries", "Buy MILK")
    service.add("Homework", "Finish the essay")
    assert [n.title for n in service.search("milk")] == ["Groceries"]
    assert [n.title for n in service.search("HOMEWORK")] == ["Homework"]
    assert service.search("zebra") == []


def test_delete_removes_note(service):
    note = service.add("Temp", "to be deleted")
    assert service.delete(note.id) is True
    assert service.list_all() == []


def test_delete_unknown_id_returns_false(service):
    service.add("Keep", "me")
    assert service.delete(999) is False
    assert len(service.list_all()) == 1