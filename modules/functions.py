FILEPATH = "src/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return list of to-do itens"""
    with open(FILEPATH, "r") as file:
        result = file.readlines()
    return result


def write_todos(todos, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello main")
    print(get_todos())
