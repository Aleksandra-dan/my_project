import argparse
from typing import List
from .models import Note
from .storage import Storage


class NoteCommands:
    def __init__(self):
        self.storage = Storage()
        self.notes = self.storage.load_notes()

    def add_note(self, title: str, content: str, tags: List[str] = None,
                 status: str = "active", priority: str = "medium") -> None:
        note_id = self.storage.get_next_id(self.notes)
        note = Note(note_id, title, content, tags, status, priority)
        self.notes.append(note)
        self.storage.save_notes(self.notes)
        print(f"Note added successfully! ID: {note_id}")

    def list_notes(self, status: str = None, priority: str = None) -> None:
        filtered_notes = self.notes

        if status:
            filtered_notes = [note for note in filtered_notes if note.status == status]

        if priority:
            filtered_notes = [note for note in filtered_notes if note.priority == priority]

        if not filtered_notes:
            print("No notes found.")
            return

        for note in filtered_notes:
            print(note)
            print("-" * 40)

    def search_notes(self, keyword: str, search_in_tags: bool = True) -> None:
        results = []
        keyword_lower = keyword.lower()

        for note in self.notes:
            if (keyword_lower in note.title.lower() or
                    keyword_lower in note.content.lower() or
                    (search_in_tags and any(keyword_lower in tag.lower() for tag in note.tags))):
                results.append(note)

        if not results:
            print(f"No notes found containing '{keyword}'")
            return

        print(f"Found {len(results)} notes containing '{keyword}':")
        for note in results:
            print(note)
            print("-" * 40)

    def delete_note(self, note_id: int) -> None:
        original_length = len(self.notes)
        self.notes = [note for note in self.notes if note.note_id != note_id]

        if len(self.notes) < original_length:
            self.storage.save_notes(self.notes)
            print(f"Note with ID {note_id} deleted successfully.")
        else:
            print(f"Note with ID {note_id} not found.")