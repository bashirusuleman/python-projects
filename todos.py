while True:
    user_action = input("What do you want to do: 'show', 'add', 'edit', 'complete', 'exit' ").strip()
    match user_action:
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()

            if len(todos) == 0:
                print("There is no action to do, please add items to do")
            else:
                for index, todo in enumerate(todos):
                    print(f"{index +1}.{todo}")
        case "add":
            user_input = input("Enter todo: ") + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(user_input.capitalize())

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "edit":
            to_do_number = int(input("Which number do you want to edit "))
            new_todo = input("What is the new todo ? ")
            file = open('todos.txt', 'r')
            todos = file.readlines()
            print(todos)
            file.close()

            todos[to_do_number  -1] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "complete":
            to_do_number = int(input("Which number do you want to complete "))
            todos.pop(to_do_number -1)
        case "exit":
            break

print("Bye!")


