from functions import get_todos, write_todos
from datetime import datetime

today = datetime.now().strftime("%B, %d %Y %H:%M:%S")
print(f'Today is {today}')

file_name = 'todos.txt'

while True:
    user_action = input("What do you want to do: 'show', 'add', 'edit', 'complete', 'exit': ").strip()
    
    if user_action == "show":

        todos = get_todos(file_name)

        if len(todos) < 1:
            print("There is no action to do, please add items to do")
        else:
            formatted_todos = [todo.strip('\n') for todo in todos]
            for index, todo in enumerate(formatted_todos):
                print(f"{index +1}.{todo}")
        
    elif user_action == "add":
        user_input = input("Enter todo: ") + '\n'

        todos = get_todos(file_name)

        todos.append(user_input.capitalize())

        write_todos(file_name, todos)

    elif user_action == "edit":
        to_do_number = int(input("Which number do you want to edit "))
        new_todo = input("What is the new todo ? ") + "\n"

        todos = get_todos(file_name)
        todos[to_do_number  -1] = new_todo

        write_todos(file_name, todos)
        
    elif user_action == "complete":
        try:
            to_do_number = int(input("Which number do you want to complete "))

            todos = get_todos(file_name)
            
            todos.pop(to_do_number -1)
        
            write_todos(file_name, todos)

        except ValueError:
            print("Enter a number 1,2,3....")
            continue
        
    elif user_action == "exit":
        break
    else:
            print("Correct action not selected, Choose the right action to perform")

print("Bye!")


