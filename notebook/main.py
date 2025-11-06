#!/usr/bin/env python3
import argparse
from .commands import NoteCommands


def main():
    parser = argparse.ArgumentParser(description="Note Manager")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new note')
    add_parser.add_argument('--title', required=True, help='Note title')
    add_parser.add_argument('--content', required=True, help='Note content')
    add_parser.add_argument('--tags', nargs='+', help='Note tags')
    add_parser.add_argument('--status', choices=['active', 'completed', 'archived'],
                            default='active', help='Note status')
    add_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                            default='medium', help='Note priority')

    # List command
    list_parser = subparsers.add_parser('list', help='List notes')
    list_parser.add_argument('--status', choices=['active', 'completed', 'archived'],
                             help='Filter by status')
    list_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                             help='Filter by priority')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search notes')
    search_parser.add_argument('keyword', help='Keyword to search for')
    search_parser.add_argument('--no-tags', action='store_true',
                               help='Exclude tags from search')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a note')
    delete_parser.add_argument('note_id', type=int, help='Note ID to delete')

    args = parser.parse_args()
    commands = NoteCommands()

    if args.command == 'add':
        commands.add_note(args.title, args.content, args.tags, args.status, args.priority)
    elif args.command == 'list':
        commands.list_notes(args.status, args.priority)
    elif args.command == 'search':
        commands.search_notes(args.keyword, not args.no_tags)
    elif args.command == 'delete':
        commands.delete_note(args.note_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()