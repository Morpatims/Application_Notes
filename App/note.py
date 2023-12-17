from datetime import datetime

class Note:
    def __init__(self, note_id, title, message, date):
        self._id = note_id
        self._title = title
        self._message = message
        self._date = date

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def message(self):
        return self._message

    @property
    def date(self):
        return self._date

    def __repr__(self):
        return f"Note(id={self.id}, title='{self.title}', date='{self.date}')"