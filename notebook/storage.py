import json
import os
from typing import List, Optional
from .models import Note


class NoteStorage:
    def __init__(self, filename: str = "notes.json"):
        self.filename = filename
        self.ensure_storage_file()

    def ensure_storage_file(self) -> None:
        """Создает файл для хранения, если он не существует"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load_notes(self) -> List[Note]:
        """Загружает все заметки из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Note.from_dict(note_data) for note_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_notes(self, notes: List[Note]) -> None:
        """Сохраняет все заметки в файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([note.to_dict() for note in notes], f, indent=2, ensure_ascii=False)

    def get_next_id(self) -> int:
        """Генерирует следующий ID для новой заметки"""
        notes = self.load_notes()
        if not notes:
            return 1
        return max(note.note_id for note in notes) + 1

    def add_note(self, note: Note) -> None:
        """Добавляет новую заметку"""
        notes = self.load_notes()
        note.note_id = self.get_next_id()
        notes.append(note)
        self.save_notes(notes)

    def delete_note(self, note_id: int) -> bool:
        """Удаляет заметку по ID"""
        notes = self.load_notes()
        notes = [note for note in notes if note.note_id != note_id]
        if len(notes) != len(self.load_notes()):
            self.save_notes(notes)
            return True
        return False

    def update_note(self, updated_note: Note) -> bool:
        """Обновляет существующую заметку"""
        notes = self.load_notes()
        for i, note in enumerate(notes):
            if note.note_id == updated_note.note_id:
                notes[i] = updated_note
                self.save_notes(notes)
                return True
        return False