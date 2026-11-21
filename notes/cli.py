import argparse
import sys

from .service import NoteService


def build_parser():
    parser = argparse.ArgumentParser(prog="notes", description="A simple notes app")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a note")
    add.add_argument("title")
    add.add_argument("text")

    sub.add_parser("list", help="list all notes")

    search = sub.add_parser("search", help="search notes by keyword")
    search.add_argument("keyword")

    delete = sub.add_parser("delete", help="delete a note by id")
    delete.add_argument("id", type=int)

    return parser


def print_notes(notes):
    if not notes:
        print("No notes found.")
        return
    for n in notes:
        print(f"[{n.id}] {n.title} ({n.created_at})")
        print(f"    {n.text}")


def main(argv: list[str] | None = None, service: NoteService | None = None) -> int:
    """Run the CLI. Pass a service to override the default notes.json (e.g. in tests)."""
    args = build_parser().parse_args(argv)
    service = service or NoteService()
    try:
        if args.command == "add":
            note = service.add(args.title, args.text)
            print(f"Added note {note.id}.")
        elif args.command == "list":
            print_notes(service.list_all())
        elif args.command == "search":
            print_notes(service.search(args.keyword))
        elif args.command == "delete":
            if service.delete(args.id):
                print(f"Deleted note {args.id}.")
            else:
                print(f"No note with id {args.id}.", file=sys.stderr)
                return 1
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())