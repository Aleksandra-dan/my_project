import json
from datetime import datetime
from typing import List, Optional


class Note:
    def __init__(self, note_id: int, title: str, content: str,
                 tags: Optional[List[str]] = None, status: str = "active",
                 priority: str = "medium", created_at: Optional[str] = None):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.tags = tags or []
        self.status = status  # active, completed, archived
        self.priority = priority  # low, medium, high
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            'id': self.note_id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Note':
        return cls(
            note_id=data['id'],
            title=data['title'],
            content=data['content'],
            tags=data['tags'],
            status=data['status'],
            priority=data['priority'],
            created_at=data['created_at']
        )

    def __str__(self) -> str:
        return (f"ID: {self.note_id}\n"
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Tags: {', '.join(self.tags)}\n"
                f"Status: {self.status}\n"
                f"Priority: {self.priority}\n"
                f"Created: {self.created_at}\n")