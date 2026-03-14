# Creat the tests for the todo.py classes
import pytest
from src.todo import Todo, TodoList, save_todos, load_todos
import os

# Creating the fixtures
@pytest.fixture
def empty_list():
    return TodoList()

@pytest.fixture
def filled_list():
    t1 = TodoList()
    t1.add("Buy bread")
    t1.add("Go to the gym")
    return t1

# Test add function in Todo Class
def test_add_todo(empty_list):
    empty_list.add("Buy milk")
    assert len(empty_list.todos) == 1
    assert empty_list.todos[0].title == "Buy milk"
    assert empty_list.todos[0].completed == False
    assert empty_list.next_id == 2

# Test list_all function in Todo Class in a filed list
def test_list_all(filled_list):
    todos = filled_list.list_all()
    assert len(todos) == 2

# Test list_all function in Todo Class in a empty list
def test_list_all_empty(empty_list):
    assert empty_list.list_all() == []

def test_complete_todo(filled_list):
    t1 = filled_list.complete(1)
    assert t1 == True
    assert filled_list.todos[0].completed == True

def test_complete_missing_todo(filled_list):
    t1 = filled_list.complete(999)
    assert t1 == False

# Test delete function in Todo Class
def test_delete_todo(filled_list):
    t1 = filled_list.delete(1)
    assert t1 == True
    assert len(filled_list.todos) == 1

def test_delete_missing_todo(filled_list):
    t1 = filled_list.delete(999)
    assert t1 == False
    assert len(filled_list.todos) == 2

# Test save and load functions in Todo Class
def test_save_and_load(filled_list, tmp_path):
    filepath = tmp_path / "todo.json"
    save_todos(filled_list, filepath)
    loaded = load_todos(filepath)
    assert len(loaded.todos) == 2
    assert loaded.todos[0].title == "Buy bread"
    assert loaded.todos[1].title == "Go to the gym"

def test_load_missing_file():
    loaded = load_todos("nonexistent.json")
    assert len(loaded.todos) == 0
    assert loaded.next_id == 1



