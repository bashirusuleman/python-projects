def get_todos(file_name):
    with open(file_name, 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(file_name, todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

if __name__ == 'main':
    print("Hello World")