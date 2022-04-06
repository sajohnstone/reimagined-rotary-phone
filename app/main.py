from app.todo import Todo # pragma: no cover

if __name__ == "__main__": # pragma: no cover
    todo_list_json = Todo().get_todos().text  # pragma: no cover
    print(todo_list_json)  # pragma: no cover
