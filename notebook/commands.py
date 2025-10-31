import argparse
from typing import List
from .models import Note
from .storage import NoteStorage


class NoteCommands:
    def __init__(self):
        self.storage = NoteStorage()

    def add_note(self, title: str, content: str, tags: List[str] = None,
                 priority: str = "medium") -> None:
        """Добавляет новую заметку"""
        note = Note(title=title, content=content, tags=tags, priority=priority)
        self.storage.add_note(note)
        print(f"✅ Заметка '{title}' успешно добавлена (ID: {note.note_id})")

    def list_notes(self, status: str = None, priority: str = None,
                   show_all: bool = False) -> None:
        """Показывает список заметок с фильтрацией"""
        notes = self.storage.load_notes()

        if not notes:
            print("📝 Нет сохраненных заметок")
            return

        # Фильтрация
        filtered_notes = notes
        if status and not show_all:
            filtered_notes = [note for note in filtered_notes if note.status == status]
        if priority and not show_all:
            filtered_notes = [note for note in filtered_notes if note.priority == priority]

        if not filtered_notes:
            print("🔍 Заметки по заданным критериям не найдены")
            return

        print(f"\n📋 Найдено заметок: {len(filtered_notes)}")
        print("=" * 50)
        for note in filtered_notes:
            print(note)

    def search_notes(self, keyword: str, search_in_tags: bool = False) -> None:
        """Ищет заметки по ключевым словам"""
        notes = self.storage.load_notes()
        keyword = keyword.lower()

        found_notes = []
        for note in notes:
            # Поиск в заголовке и содержании
            if (keyword in note.title.lower() or
                    keyword in note.content.lower()):
                found_notes.append(note)
            # Поиск в тегах
            elif search_in_tags and any(keyword in tag.lower() for tag in note.tags):
                found_notes.append(note)

        if found_notes:
            print(f"\n🔍 Найдено заметок по запросу '{keyword}': {len(found_notes)}")
            print("=" * 50)
            for note in found_notes:
                print(note)
        else:
            print(f"🔍 По запросу '{keyword}' ничего не найдено")

    def delete_note(self, note_id: int) -> None:
        """Удаляет заметку по ID"""
        if self.storage.delete_note(note_id):
            print(f"✅ Заметка с ID {note_id} успешно удалена")
        else:
            print(f"❌ Заметка с ID {note_id} не найдена")

    def update_note_status(self, note_id: int, status: str) -> None:
        """Обновляет статус заметки"""
        notes = self.storage.load_notes()
        for note in notes:
            if note.note_id == note_id:
                note.status = status
                self.storage.update_note(note)
                print(f"✅ Статус заметки {note_id} изменен на '{status}'")
                return
        print(f"❌ Заметка с ID {note_id} не найдена")


def main():
    commands = NoteCommands()
    parser = argparse.ArgumentParser(description="Менеджер заметок")

    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    # Команда добавления
    add_parser = subparsers.add_parser('--add', help='Добавить новую заметку')
    add_parser.add_argument('--title', required=True, help='Заголовок заметки')
    add_parser.add_argument('--content', required=True, help='Содержание заметки')
    add_parser.add_argument('--tags', nargs='+', help='Теги через пробел')
    add_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                            default='medium', help='Приоритет заметки')

    # Команда списка
    list_parser = subparsers.add_parser('--list', help='Показать список заметок')
    list_parser.add_argument('--status', choices=['active', 'completed', 'archived'],
                             help='Фильтр по статусу')
    list_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                             help='Фильтр по приоритету')
    list_parser.add_argument('--all', action='store_true',
                             help='Показать все заметки без фильтрации')

    # Команда поиска
    search_parser = subparsers.add_parser('--search', help='Поиск заметок')
    search_parser.add_argument('keyword', help='Ключевое слово для поиска')
    search_parser.add_argument('--tags', action='store_true',
                               help='Искать также в тегах')

    # Команда удаления
    delete_parser = subparsers.add_parser('--delete', help='Удалить заметку')
    delete_parser.add_argument('id', type=int, help='ID заметки для удаления')

    # Команда обновления статуса
    status_parser = subparsers.add_parser('--status', help='Изменить статус заметки')
    status_parser.add_argument('id', type=int, help='ID заметки')
    status_parser.add_argument('status', choices=['active', 'completed', 'archived'],
                               help='Новый статус')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == '--add':
            commands.add_note(args.title, args.content, args.tags, args.priority)

        elif args.command == '--list':
            commands.list_notes(args.status, args.priority, args.all)

        elif args.command == '--search':
            commands.search_notes(args.keyword, args.tags)

        elif args.command == '--delete':
            commands.delete_note(args.id)

        elif args.command == '--status':
            commands.update_note_status(args.id, args.status)

    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    main()