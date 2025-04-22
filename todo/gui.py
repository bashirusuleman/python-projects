import FreeSimpleGUI as sg
import functions

FILE_PATH='todos.txt'

layout = [[sg.Text('Enter New To-Do')],
        [sg.InputText(tooltip='Enter to do', key='todo', do_not_clear=False),
         sg.Button('Add')],
         [sg.Listbox(functions.get_todos(FILE_PATH), size=(45,20),key='todos'), sg.Button("Edit")]]

window = sg.Window('To-Do Application', layout, font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            new_todo = value['todo']
            print(new_todo)
            todos = functions.get_todos(FILE_PATH)
            todos.append(new_todo + "\n")
            functions.write_todos(FILE_PATH, todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()