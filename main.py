import argparse
from src.todo import Todo, TodoList, save_todos, load_todos
import subprocess

FILEPATH = "/Users/andresugalde/Downloads/todo-app-python/data/todos.json"

def main():
    parser = argparse.ArgumentParser(description="Simple todo list as a CLI")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add")
    add_parser.add_argument("title", type=str)

    complete_parser = subparser.add_parser("complete")
    complete_parser.add_argument("id", type=int)

    delete_parser = subparser.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    list_parser = subparser.add_parser("list")

    args = parser.parse_args()

    todo_list = load_todos(filepath=FILEPATH)

    if args.command == "add":
        todo_list.add(args.title)
        save_todos(todo_list=todo_list, filepath=FILEPATH)
        print(f"Added {args.title} to todo list.")
    elif args.command == "complete":
        result = todo_list.complete(args.id)
        save_todos(todo_list=todo_list, filepath=FILEPATH)
        if result:
            print(f"Completed {args.id} in todo list.")
        else:
            print(f"Todo {args.id} was not found.")
    elif args.command == "delete":
        result = todo_list.delete(args.id)
        save_todos(todo_list=todo_list, filepath=FILEPATH)
        if result:
            print(f"Deleted {args.id} in todo list.")
        else:
            print(f"Todo {args.id} was not found.")
    elif args.command == "list":
        for todo in todo_list.list_all():
            print(todo)

    else :
        parser.print_help()

if __name__ == "__main__":
    main()
