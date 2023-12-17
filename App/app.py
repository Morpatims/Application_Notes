from datetime import datetime
from App.storage import NotesStorage
from App.note import Note

class NotesApp:
    def __init__(self, storage: NotesStorage):
        self._storage = storage

    def list_notes(self, date_filter=None):
        if date_filter:
            return [note for note in self._storage.notes if note.date == date_filter]
        else:
            return self._storage.notes

    def add_note(self, title, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(self._storage.notes) + 1, title, message, timestamp)
        self._storage.notes.append(new_note)
        self._storage.save_notes()
        return new_note

    def edit_note(self, note_id, title, message):
        for note in self._storage.notes:
            if note.id == note_id:
                note._title = title
                note._message = message
                note._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._storage.save_notes()
                return note
        return None

    def delete_note(self, note_id):
        self._storage.notes = [note for note in self._storage.notes if note.id != note_id]
        self._storage.save_notes()