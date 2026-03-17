# Andres Ugalde
# Goal: Make a Todo app 

from datetime import datetime
import json

# Todo Class
class Todo:
    def __init__(self, id, title, completed = False):
        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = datetime.now() # Saves the time when the object is created

    def to_dict(self):
        temp = {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat() # Converts it to a string
        }
        return temp

    def __str__(self):
        return f"[X] {self.title}" if self.completed else f"[ ] {self.title}"
    
    @classmethod 
    def from_dict(cls, data):
        todo = cls(data["id"], data["title"], data["completed"])
        todo.created_at = datetime.fromisoformat(data["created_at"])
        return todo
    
class TodoList:
    def __init__(self):
        self.todos = []
        self.next_id = 1

    def add(self, title):
        new_todo = Todo(self.next_id, title)
        self.todos.append(new_todo)
        self.next_id += 1

    def list_all(self):
        return self.todos
    
    def complete(self, id):
        for todo in self.todos:
            if todo.id == id:
                todo.completed = True
                return True
        
        return False # Returns false if id isn't in todo list
    
    def delete(self, id):
        for todo in self.todos:
            if todo.id == id:
                self.todos.remove(todo)
                return True
            
        return False
        

def save_todos(todo_list, filepath):
    temp_list = []
    all_todos = todo_list.list_all()
    for todo in all_todos:
        temp_list.append(todo.to_dict())

    with open(filepath, "w") as f:
        json.dump(temp_list, f)

def load_todos(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        new_todo_list = TodoList()

        for todo in data:
            new_todo_list.todos.append(Todo.from_dict(todo))

        if new_todo_list.todos:
            new_todo_list.next_id = max(new_todo_list.todos, key=lambda t: t.id).id + 1
        return new_todo_list
        
    except FileNotFoundError:
        return TodoList()
    

        
