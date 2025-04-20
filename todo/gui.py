import FreeSimpleGUI as sg
import functions


layout = [[sg.Text('Enter New To-Do')],
        [sg.InputText("Enter to-do", key='Add', do_not_clear=False), sg.Button('Add')]]

window = sg.Window('To-Do Application', layout, font=('Helvetica', 20))

FILE_PATH='todos.txt'

while True:
    event, value = window.read()
    # print(event)
    match event:
        case sg.WIN_CLOSED:
            break
        case "Cancel":
            print(event)
            # print(values)
        case "Add0":
            new_todo = value['Add']
            print(new_todo)
            todos = functions.get_todos(FILE_PATH)
            todos.append(new_todo + "\n")
            functions.write_todos(FILE_PATH, todos)
            # print(values)
window.close()