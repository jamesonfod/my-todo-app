
def get_todo_items(filepath="todo_data.txt"):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath) as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_items(todo_list_local, filepath="todo_data.txt"):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, "w") as file:
        file.writelines(todo_list_local)