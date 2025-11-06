import json
import os
from typing import List, Dict, Any
from .models import Note


class Storage:
    def __init__(self, filename: str = "notes.json"):
        self.filename = filename

    def load_notes(self) -> List[Note]:
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Note.from_dict(note_data) for note_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_notes(self, notes: List[Note]) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([note.to_dict() for note in notes], f, indent=2, ensure_ascii=False)

    def get_next_id(self, notes: List[Note]) -> int:
        if not notes:
            return 1
        return max(note.note_id for note in notes) + 1