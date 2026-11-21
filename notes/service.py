from .models import Note
from .storage import DEFAULT_PATH, load_notes, save_notes


class NoteService:
    def __init__(self, path=DEFAULT_PATH):
        self.path = path

    def add(self, title, text):
        title = title.strip()
        if not title:
            raise ValueError("Title must not be empty")
        notes = load_notes(self.path)
        new_id = max((n.id for n in notes), default=0) + 1
        note = Note(id=new_id, title=title, text=text.strip())
        notes.append(note)
        save_notes(notes, self.path)
        return note

    def list_all(self):
        return load_notes(self.path)

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            n
            for n in load_notes(self.path)
            if keyword in n.title.lower() or keyword in n.text.lower()
        ]

    def delete(self, note_id):
        """Delete a note by id. Returns True if it existed, False otherwise."""
        notes = load_notes(self.path)
        remaining = [n for n in notes if n.id != note_id]
        if len(remaining) == len(notes):
            return False
        save_notes(remaining, self.path)
        return True