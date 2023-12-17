from abc import ABC, abstractmethod
import json
from App.note import Note

class NotesStorage(ABC):
    @abstractmethod
    def load_notes(self):
        pass

    @abstractmethod
    def save_notes(self):
        pass


class JsonNotesStorage(NotesStorage):
    def __init__(self, storage_file='notes.json'):
        self._storage_file = storage_file
        self._notes = self.load_notes()

    @property
    def notes(self):
        return self._notes

    def load_notes(self):
        try:
            with open(self._storage_file, 'r') as file:
                return [Note(**note_data) for note_data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading notes: {e}")
            return []

    def save_notes(self):
        try:
            with open(self._storage_file, 'w') as file:
                json.dump([vars(note) for note in self._notes], file, indent=2)
        except IOError as e:
            print(f"Error saving notes: {e}")