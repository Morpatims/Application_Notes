import argparse
from app import NotesApp

class CommandLineInterface:
    def __init__(self, notes_app: NotesApp):
        self._notes_app = notes_app
        self._parser = argparse.ArgumentParser(description='Console Notes App')
        self._parser.add_argument('command', choices=['add', 'list', 'edit', 'delete'], help='Choose command')
        self._parser.add_argument('--id', type=int, help='Note ID for edit or delete operations')
        self._parser.add_argument('--title', help='Note title')
        self._parser.add_argument('--msg', help='Note message')
        self._parser.add_argument('--date', help='Filter notes by date (YYYY-MM-DD)')

    def run(self):
        args = self._parser.parse_args()

        if args.command == 'list':
            notes = self._notes_app.list_notes(args.date)
            self.display_notes(notes)

        elif args.command == 'add':
            new_note = self._notes_app.add_note(args.title, args.msg)
            print(f"Note added successfully. ID: {new_note.id}")

        elif args.command == 'edit':
            edited_note = self._notes_app.edit_note(args.id, args.title, args.msg)
            if edited_note:
                print(f"Note {args.id} edited successfully.")
            else:
                print(f"Note with ID {args.id} not found.")

        elif args.command == 'delete':
            self._notes_app.delete_note(args.id)
            print(f"Note {args.id} deleted successfully.")

    def display_notes(self, notes):
        for note in notes:
            print(f"{note.id}. {note.title} - {note.date}")
            print(note.message)
            print('-' * 30)


if __name__ == '__main__':
    storage = JsonNotesStorage()
    app = NotesApp(storage)
    cli = CommandLineInterface(app)
    cli.run()